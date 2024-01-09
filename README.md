# Obsidian_LitRef
Simple and efficient Obsidian vault for note taking on scientific project and literature.

# Installation

Install obsidian here: https://help.obsidian.md/Getting+started/Download+and+install+Obsidian

git clone that repo where you want the vault to be, and open it in Obsidian

# Tutorial and usefull information

This vault meant to be simple in order to be easily customizable. Also it imply that you know a bit about zotero integration plugin mainly.

## Semantic scholar references builder
**For now work only on linux with python3 installed**

Default zotero integration template integrate a codeblock replacing itself by the article references gathered through semantic scholar API if executed (to execute the codeblock swith to reading mode and mouseover the codeblock to see the 'Run' button).

To work in the context of the vault this require several things :

  - Having the article name in the Note frontmatter as 'title: My article title in frontmatter' as it is done in the CreateArticleNote template with the replacement of the ":" by " -".
  - Having a semantic scholar API key, without it the script is most likely to crash as it won't be able to make enough request to the API. You can easily request an API key here https://www.semanticscholar.org/product/api#api-key-form
  - Storing that apikey in a text file

Changes related to path in order to make this work is indicated in the codeblock section int the CreateArticleNote template.

To work outside the context of this vault this require the above things and : 
  - having the obsidian **Execute code** module installed and setup  
  - having the `buildReferences.py`, `function_litref.py`, and `function_similarity.py` scripts in a folder at this position : vault_root/.obsidian/scripts/python/
  - having the codeblocks and the proper anchor around it in your note template
  - having your note stored at vault_root/Article_note/ or changed this path in the `buildReference.py` script

