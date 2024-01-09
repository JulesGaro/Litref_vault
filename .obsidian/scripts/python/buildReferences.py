import argparse

from time import sleep

import function_litref as fct

# limitations are:
#     - semantic scholar sometimes don't have the paper in a good version with proper metadata
#     - titles of some paper are the Journal + the title merged together
#     - Paper with short titles like 'Ensemble 2018' might not appear in top 10 paper in title query 
#     - probably other things that I did not encounterd yet
# thus this tool might generate partial but yet correct references

parser = argparse.ArgumentParser()
parser.add_argument("note_file", help="Title of the note")
parser.add_argument("--apikey", help="API key")
args = parser.parse_args()

def build_references(api_requests = 0):
    """
    Builds references in an Obsidian note using the provided API request.

    Args:
        api_requests (int): The number of API requests made (default is 0).

    Returns:
        int: 1 if successful.

    Raises:
        KeyError: If the API request fails after 5 attempts.

    """
    note_file = args.note_file
    apikey = args.apikey

    try:
        article_title = fct.get_frontmatter_article_title(f"Article_note/{note_file}")
        print(article_title)
        # query for The Article reference Ids
        references_ids = fct.get_reference_ids(article_title,apikey)
        # with the list of reference ids, querying of the information
        # for each reference
        references = fct.get_formated_refs(references_ids,apikey)

    except fct.APIError as exc:
        if api_requests < 5:
            sleep(2)
            build_references(api_requests = api_requests + 1)
            return 1
        else:
            raise exc

    # write down the references in the Obsidian note using the template
    # Anchors
    with open(f"Article_note/{note_file}", "r", encoding = "UTF-8") as f:
        content = f.read()
        above_ref = content.split("%% references anchor %%")[0]
        below_ref = content.split("%% references anchor %%")[2]

    new_content = above_ref + references + below_ref
    with open(f"Article_note/{note_file}", "w", encoding = "UTF-8") as f:
        f.write(new_content)
    return 1

if __name__ == "__main__":
    build_references()
