from time import time,sleep
from requests import get,post

import function_similarity as sim

class APIError(Exception):
    """Custom exception class for API errors."""

    def __init__(self, message="API request fail, check your internet connection"):
        self.message = message
        super().__init__(self.message)

class FrontmatterError(ValueError):
    """Custom error class for frontmatter-related errors."""
    def __init__(self):
        self.value = None
        self.message = "No 'title' key found in frontmatter, "
        "you can add it to your template by adding 'title: {{title}}' in the frontmatter part"

        super().__init__(self.message)

def get_frontmatter_article_title(note_path):
    """
    Returns the title of a note based on the .md frontmatter

    Args:
    note_path (str): The path to the note.

    Returns:
    str: The title of the note.
    """
    with open(note_path, "r",encoding="UTF-8") as f:
        note = f.read()
    try:
        frontmatter = note.split("---")[1]
        title = [line[7:] for line in frontmatter.split("\n") if line[0:7] == "title: "][0]
        return title
    except FrontmatterError as exc:
        raise exc

def api_get(url, apikey):
    """
    Sends a GET request to the specified URL with the provided API key.

    Args:
        url (str): The URL to send the GET request to.
        apikey (str): The API key to include in the request headers.

    Returns:
        dict: The JSON response from the GET request.

    Raises:
        APIError: If the response contains the message "Too Many Requests".
    """
    response = get(url, headers={'X-API-KEY': apikey}, timeout=10).json()
    if "message" in response:
        if response["message"][:18] == 'Too Many Requests':
            raise APIError
    return response

def api_post(ids:list,fields:list,apikey:str="",endpoint:str="paper"):
    """
    Sends a POST request to the Semantic Scholar API to retrieve information for a batch of IDs.

    Parameters:
    - ids (list): A list of IDs for which information is requested.
    - fields (list): A list of fields to include in the response.
    - apikey (str): The API key for authentication (optional).
    - endpoint (str): The API endpoint to use (default is "paper").

    Returns:
    - response (dict): The JSON response from the API.

    Raises:
    - APIError: If the API returns a "Too Many Requests" error message.
    """
    response = post(
        f'https://api.semanticscholar.org/graph/v1/{endpoint}/batch',
        params={'fields': ",".join(fields)},
        json={"ids": ids},
        headers={'X-API-KEY': apikey},timeout=10).json()
    if "message" in response:
        if response["message"][:18] == 'Too Many Requests':
            raise APIError
    return response

def search_by_title(title, apikey):
    """
    Search for papers by title using the Semantic Scholar API.

    Args:
        title (str): The title of the paper to search for.
        apikey (str): The API key for accessing the Semantic Scholar API.

    Returns:
        dict: The query result from the Semantic Scholar API.
    """
    title = "+".join(title.split(" "))
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={title}"
    query = api_get(url, apikey)
    return query

def get_paper_id(title, apikey, restrict_name=True):
    """
    Retrieves the paper ID for a given title using the provided API key.

    Parameters:
    title (str): The title of the paper.
    apikey (str): The API key for accessing the paper database.
    restrict_name (bool, optional): Restrict the search to exact title matches.

    Returns:
    str or None: The paper ID if found, or None if not found.
    """
    query = search_by_title(title, apikey)
    if query == {'total': 0, 'offset': 0}:
        return None
    else:
        paper_id = get_proper_paperid(title, query, apikey, restrict_name)
        return paper_id

def get_proper_paperid(title, query, apikey, restrict_name):
    """
    Get the proper paper ID based on the given title and query.

    Args:
        title (str): The title of the paper to check.
        query (dict): The query containing the paper data.
        apikey (str): The API key for accessing the Semantic Scholar API.
        restrict_name (bool): Restrict the search to papers with the same title.

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

        paper = api_get(url, apikey)
        same_title = sim.same_name(paper["title"],title)
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

def get_reference_ids(title, apikey):
    """
    Retrieves the reference IDs for a given paper title.

    Parameters:
    title (str): The title of the paper.
    apikey (str): The API key for accessing the Semantic Scholar API.

    Returns:
    list: A list of reference IDs for the paper.
    """
    paper_id = get_paper_id(title, apikey)
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,references"
    query = api_get(url, apikey)
    ref_titles = list({
        reference["title"]
        for reference in query["references"] if reference["title"] is not None})

    ref_ids = get_proper_references(ref_titles, apikey)
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
        if ref["journal"] is not None:
            journal = ref["journal"]
        else:
            journal = None
    year = ref["year"]
    doi = ref["externalIds"]["DOI"]

    # formating authours informations
    if len(authors) > 3:
        f_authors = authors[0]["name"].split(" ")[-1] + " et al."
    else:
        f_authors = ""
        for i, author in enumerate(authors):
            author = author["name"].split(" ")
            author = "".join(
                [word[0].upper() + ". " if i != len(author) - 1 else word
                for i, word in enumerate(author)])
            if i == len(authors) - 2:
                f_authors += author + " & "
            elif i == len(authors) - 1:
                f_authors += author
            else:
                f_authors += author + ", "
        f_authors = f_authors[:-2]

    # formating journal information
    f_journal = ""
    if journal is not None:
        if "name" in journal:
            f_journal += "*" + journal["name"] + "*"
            if "volume" in journal:
                if journal["volume"] != "":
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

    json_refs = api_post(
        fields=["title","authors","year","journal","externalIds"],
        ids = references_ids,
        apikey=apikey)
    formated_refs_list = [format_ref(ref) for ref in json_refs]
    references = "\n".join(formated_refs_list)
    return references
