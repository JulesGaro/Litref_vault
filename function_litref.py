import requests
import json
import os


def get_files_in_folder(folder_path):
    """
    Returns the names of files inside a specific folder as a list.

    Args:
    folder_path (str): The path to the folder.

    Returns:
    list: The names of files inside the folder.
    """
    file_names = []
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            file_names.append(file_name)
    return file_names


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

def get_vault_paper_ids(path):
    """
    Retrieves the paper IDs for the papers in a specified folder.

    Args:
    path (str): The path to the folder containing the papers.

    Returns:
    list: The paper IDs.
    """
    paper_titles = get_files_in_folder(path)
    paper_ids = []
    for paper in paper_titles:
        query = search_by_title(paper)
        paper_ids.append(get_paper_id(paper))
    
    return paper_ids

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
    references = [f" - [[{reference}]]" for reference in references]
    return "\n".join(references)

def add_references(title,vault_path):
    note_path = os.path.join(vault_path, title)
    with open(note_path, "r") as f:
        note = f.read()
            
    if not "# References" in note:
        note += "\n# References\n"
    else:
        index = note.find("# References")
        if index != -1:
            note = note[:index + len("# References")]
    
    references = get_reference_titles(title)
    references = format_ref(references)

    note += references

    with open(note_path, "w") as f:
        f.write(note)


def build_vault_references():
    pass