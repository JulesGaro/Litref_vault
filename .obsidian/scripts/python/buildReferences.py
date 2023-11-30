import function_litref as fct
import argparse
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("note_file", help="Title of the note")
args = parser.parse_args()

def buildReferences(API_request = 0):
    note_file = args.note_file

    try:
        article_title = fct.get_frontmatter_article_title(f"Article_note/{note_file}")
        references = fct.get_reference_titles(article_title)
    except(KeyError):
        if API_request == 0:
            sleep(2)
            buildReferences(API_request = API_request + 1)
            return 0
        elif API_request < 5:
            sleep(2)
            buildReferences(API_request = API_request + 1)
            return 0
        else:
            raise(KeyError("API request failed,check your internet connexion"))

    references = fct.format_ref(references)

    with open(f"Article_note/{note_file}", "r") as f:
        content = f.read()
        above_ref = content.split("%% references anchor %%")[0]
        below_ref = content.split("%% references anchor %%")[2]

    new_content = above_ref + references + below_ref
    with open(f"Article_note/{note_file}", "w") as f:
        f.write(new_content)
    
    print("code run")
if __name__ == "__main__":
    buildReferences()