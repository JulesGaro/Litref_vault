import requests
import json
import os


def parse_frontmatter(frontmatter_string):
    """
    Parses the frontmatter of a note and returns a dictionary of the frontmatter.

    Args:
    frontmatter_string (str): The frontmatter of a note.

    Returns:
    dict: The frontmatter of a note as a dictionary.
    """
    frontmatter = {}
    for line in [line for line in frontmatter_string.split("\n") if line != ""]:
        key, value = line.split(": ")
        if "," in value:
            value = value.split(",")
        frontmatter[key] = value
    
    return frontmatter

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
        frontmatter = parse_frontmatter(note.split("---")[1])
    try:
        return frontmatter["title"]
    except(KeyError):
        raise(KeyError("No 'title' key found in frontmatter, you can add it to your template by adding 'title: {{title}}' in the frontmatter part"))

def query_api(url):
    """
    Sends a GET request to the specified URL and returns the response in JSON format.

    Args:
    url (str): The URL to send the GET request to.

    Returns:
    dict: The response from the API in JSON format.
    """
    response = requests.get(url)
    return response.json()


def search_by_title(title):
    """
    Searches for papers on Semantic Scholar API by title.

    Args:
    title (str): The title of the paper to search for.

    Returns:
    dict: The response from the API in JSON format.
    """
    title = "+".join(title.split(" "))
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={title}"
    query = query_api(url)
    return query

def get_paper_id(title):
    query = search_by_title(title)
    # try catch error due to connection/api error
    return query["data"][0]["paperId"]

def get_paper_info(paper_id):
    """
    Retrieves the paper information for a specified paper ID.

    Args:
    paper_id (str): The paper ID.

    Returns:
    dict: The paper information.
    """
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,references"
    query = query_api(url)
    return query

def get_reference_titles(title):
    paper_id = get_paper_id(title)
    paper_info = get_paper_info(paper_id)
    return [reference["title"] for reference in paper_info["references"]]

def format_ref(references):
    references = [f" - [[{reference}]]".replace(":"," -") for reference in references]
    return "\n".join(references)
