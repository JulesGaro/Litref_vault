import requests
import json
import os
from time import time,sleep

import function_similarity as sim


def get_frontmatter_article_title(note_path):
    """
    Returns the title of a note based on the .md frontmatter

    Args:
    note_path (str): The path to the note.

    Returns:
    str: The title of the note.
    """
    with open(note_path, "r") as f:
        note = f.read()
    try:
        frontmatter = note.split("---")[1]
        title = [line[7:] for line in frontmatter.split("\n") if line[0:7] == "title: "][0]
        return title
    except(ValueError):
        raise(ValueError("No 'title' key found in frontmatter, you can add it to your template by adding 'title: {{title}}' in the frontmatter part"))

def query_api(url,apikey):
    """
    Sends a GET request to the specified URL and returns the response in JSON format.

    Args:
    url (str): The URL to send the GET request to.

    Returns:
    dict: The response from the API in JSON format.
    """
    response = requests.get(url,headers={'X-API-KEY':apikey})
    return response.json()


def search_by_title(title,apikey):
    """
    Searches for papers on Semantic Scholar API by title.

    Args:
    title (str): The title of the paper to search for.

    Returns:
    dict: The response from the API in JSON format.
    """
    title = "+".join(title.split(" "))
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={title}"
    query = query_api(url,apikey)
    return query

def get_paper_id(title,apikey,restrict_name=True):
    """
    Retrieves the paper ID for a given title by performing a search.

    Args:
        title (str): The title of the paper.

    Returns:
        str: The paper ID corresponding to the given title.
    """
    query = search_by_title(title,apikey)
    # try catch error due to connection/api error
    
    paper_id = get_proper_paperId(title,query,apikey,restrict_name)

    return paper_id

def get_proper_paperId(title, query, apikey, restrict_name):
    """
    Get the proper paper ID based on the given title and query.

    Args:
        title (str): The title of the paper to check.
        query (dict): The query containing the paper data.
        apikey (str): The API key for accessing the Semantic Scholar API.
        restrict_name (bool): Flag indicating whether to restrict the search to papers with the same title.

    Returns:
        str or None: The paper ID of the proper paper, or None if no valid paper is found.
    """
    print(f"Checking paper: {title}")

    # get paper with same or similar name
    similar_paper_ids = []
    for paper in query["data"]:
        if sim.similar_name(paper["title"], title):
            similar_paper_ids.append(paper["paperId"])

    valid_paper = []
    clock = time()
    request = 0
    # Get information on paper sharing similar names
    for paper_id in similar_paper_ids:
        request += 1
        if request >= 9 and (clock - time()) < 1:
            request = 0
            clock = time()
            sleep(1)
        url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,externalIds,references,authors,year"

        paper = query_api(url, apikey)

        same_title = paper["title"] == title
        # check for:
        #   - authors being referenced
        #   - paper have references
        #   - DOI is present
        #   - minimum release date is 1950

        if (
            paper["authors"] != []
            and paper["references"] != []
            and "DOI" in paper["externalIds"]
            and paper["year"] >= 1950
        ):
            if restrict_name:
                if same_title:
                    valid_paper.append(paper)
            else:
                valid_paper.append(paper)

    if len(valid_paper) == 1:
        print("     Valid paper found!")
        return valid_paper[0]["paperId"]
    # if there is still several valid paper we take the most recent
    elif len(valid_paper) >= 1:
        print("     Valid paper found!")
        paper = max(valid_paper, key=lambda x: int(x.get("year", 0)))
        return paper["paperId"]
    else:
        print("     No valid paper")
        return None

def get_proper_references(titles, apikey):
    """
    Retrieves the proper references for a given list of titles.

    Args:
        titles (list): A list of titles.
        apikey (str): The API key for accessing the reference database.

    Returns:
        list: A list of reference IDs corresponding to the given titles.
    """
    titles = list(set(titles))  # Remove duplicates
    ref_ids = []
    clock = time()
    request = 0
    
    for title in titles:
        request += 1
        if request >= 9 and (clock - time()) < 1:
            request = 0
            clock = time()
            sleep(1)
        paper_id = get_paper_id(title, apikey, restrict_name=False)
        ref_ids.append(paper_id)
    
    return ref_ids

def get_reference_ids(title,apikey):
    """
    Retrieves the reference IDs for a given paper title.

    Args:
        title (str): The title of the paper.

    Returns:
        list: A list of reference IDs.
    """
    paper_id = get_paper_id(title,apikey)
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,references"
    query = query_api(url,apikey)
    ref_titles = [reference["title"] for reference in query["references"] if reference["title"] is not None]
    ref_ids = get_proper_references(ref_titles,apikey)
    return [ref_id for ref_id in ref_ids if ref_id is not None]

def format_ref(ref):
    """
    Formats a reference object into a citation string.

    Args:
        ref (dict): The reference object containing metadata.

    Returns:
        str: The formatted citation string.
    """

    # retrieving metadatas
    title = ref["title"]
    authors = ref["authors"]
    if "journal" in ref:
        journal = ref["journal"]
    year = ref["year"]
    doi = ref["externalIds"]["DOI"]

    # formating authours informations
    if len(authors) > 3:
        f_authors = authors[0]["name"].split(" ")[-1] + " et al."
    else:
        f_authors = ""
        for i, author in enumerate(authors):
            author = author["name"].split(" ")
            author = "".join([word[0].upper() + ". " if i != len(author) - 1 else word for i, word in enumerate(author)])
            if i == len(authors) - 2:
                f_authors += author + " & "
            elif i == len(authors) - 1:
                f_authors += author
            else:
                f_authors += author + ", "
        f_authors = f_authors[:-2]

    # formating journal information
    f_journal = ""
    if "name" in journal:
        f_journal += "*" + journal["name"] + "*"
        if "volume" in journal:
            f_journal += " **" + journal["volume"] + "**"
        if "pages" in journal:
            f_journal += ", " + journal["pages"].strip()

    # formating web link
    weblink = f"[web](https://doi.org/{doi})"

    # formating title
    f_title = title.replace("′", "'")
    f_title = f_title.replace(":", " -")
    
    return f" - {f_authors} [[{f_title}]] {f_journal} ({year}) ({weblink})\n"

def get_formated_refs(references_ids, apikey):
    """
    Retrieves formatted references for the given reference IDs using the Semantic Scholar API.

    Args:
        references_ids (list): A list of reference IDs.
        apikey (str): The API key for accessing the Semantic Scholar API.

    Returns:
        str: A string containing the formatted references.
    """
    r = requests.post(
        'https://api.semanticscholar.org/graph/v1/paper/batch',
        params={'fields': 'title,authors,year,journal,externalIds'},
        json={"ids": references_ids},
        headers={'X-API-KEY': apikey})

    json_refs = r.json()
    formated_refs_list = [format_ref(ref) for ref in json_refs]
    references = "\n".join(formated_refs_list)
    return references



