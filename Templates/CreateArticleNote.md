---
type: literature-note
title: {{ title | replace(":", " -") }}
authors:{%- for creator in creators %} {%- if creator.name == null %} {{"\n - "}} {{creator.firstName}} {{creator.lastName}} {%- endif -%} {%- if creator.name %}{{creator.creatorType | capitalize}}:: {{creator.name}}{%- endif -%}{%- endfor %}
journal: {{publicationTitle}}
tags: {% if allTags %}{{allTags}}{% else %}no_tags{% endif %}
citekey: {{citekey}}
creationdate: {{exportDate |format("DD-MM-YYYY")}}
---
# {{title}}
```table-of-contents
style: nestedList # TOC style (nestedList|inlineFirstLevel)
maxLevel: 0 # Include headings up to the speficied level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
 Zotero PDF links : {% for attachment in attachments | filterby("path", "endswith", ".pdf") %}[PDF{% if not loop.first %} {{loop.index}}{% endif %}]({{attachment.desktopURI|replace("/select/", "/open-pdf/")}}){% if not loop.last %}, {% endif %}{% endfor %}
## Article summary :
Article by *{% for creator in creators %}{% if loop.first %}{{creator.lastName}}{% endif %}{% endfor %} et al.* published in *{{publicationTitle}}* the {{date | format("DD-MM-YYYY")}} 
> [!ABSTRACT]- ABSTRACT
> {% if abstractNote %} 
> {{abstractNote|replace("\n"," ")}}
> {% endif %}
{% persist "notes" %}{% if isFirstImport %}
## Notes


{% endif %}
{% endpersist %}
## PDF Annotations
{%-
    set zoteroColors = {
        "#ff6666": "red",
        "#f19837": "orange",
        "#5fb236": "green",
        "#ffd400": "yellow",
        "#2ea8e5": "blue",
        "#aaaaaa": "grey",
        "#a28ae5": "purple"
    }
-%}
{%-
   set colorHeading = {
		"green": "✅ Comment, noticeable point",
		"blue": "💙 To keep in mind/usefull/good reference",
		"purple": "🗝️ Key point",
		"orange": " ✴️ Critical/Main point of the article",
	    "yellow": " 🌟 Critical point for personal/work interest",
	    "red": " 🚨 Disagreement with authors/doubting point",
	    "grey":" 🗒️ new vocabulary, details,whatever"
   }
-%}
{%- macro calloutHeader(type) -%}
    {%- switch type -%}
        {%- case "highlight" -%}
        Highlight
        {%- case "image" -%}
        Image
        {%- default -%}
        Note
    {%- endswitch -%}
{%- endmacro %}
{%- set newAnnot = [] -%}
{%- set newAnnotations = [] -%}
{%- set newAnnotations = annotations | filterby("date", "dateafter", lastImportDate) %}
{% if annotations.length > 0 %}
*Imported: {{importDate | format("YYYY-MM-DD HH:mm") }}*
{%- for annot in annotations -%}
{%- if annot.color in zoteroColors -%}
	{%- set customColor = zoteroColors[annot.color] -%}
{%- elif annot.colorCategory|lower in colorHeading -%}
	{%- set customColor = annot.colorCategory|lower -%}
{%- else -%}
	{%- set customColor = "other" -%}
{%- endif -%}
{%- set newAnnotations = (newAnnotations.push({"annotation": annot, "customColor": customColor}), newAnnotations) -%}
{%- endfor -%}
{%- for color, heading in colorHeading -%}
{%- for entry in newAnnotations | filterby ("customColor", "startswith", color) -%}
{%- set annot = entry.annotation -%}
{%- if entry and loop.first %}
#### {{colorHeading[color]}}
{%- endif %}

> [!quote{{"|" + color if color != "other"}}]+ {{calloutHeader(annot.type)}} ([page. {{annot.pageLabel}}](zotero://open-pdf/library/items/{{annot.attachment.itemKey}}?page={{annot.pageLabel}}&annotation={{annot.id}}))

{%- if annot.annotatedText %}
> {{annot.annotatedText|nl2br}} {% if annot.hashTags %}{{annot.hashTags}}{% endif -%}
{%- endif %}

{%- if annot.imageRelativePath %}
> ![[{{annot.imageRelativePath}}]]
{%- endif %}

{%- if annot.ocrText %}
> {{annot.ocrText}}
{%- endif %}

{%- if annot.comment %}
> - **{{annot.comment|nl2br}}**
{%- endif -%}

{%- endfor -%}
{%- endfor -%}
{% endif %}


{% persist "references" %}{% if isFirstImport %}
## References
%% references anchor %%
```shell
# Add here a link to a file text containing your semantic scholar API key
# !!!!!! DON'T SHARE THAT WITH PEOPLE !!!!!!
apikey=`cat your/apikey/file/location`
# Change the path to the path to be the absolute path to your vault
vault_path="/home/our/Documents/somewhere/obsidian_vault/"
#Change that path to be the relative path from your vault root to the folder you store zotero imported literature notes
lit_note_path_from_vault="Article_note/"
cd $vault_path
# Change the script to match the naming pattern of yout note,
# You can refer to how they are named in the zotero integration plugin # settings for that template
python3 .obsidian/scripts/python/buildReferences.py "{{ title | replace(":", " -") }}.md" --apikey "$apikey"

```
%% references anchor %%
{% endif %}
{% endpersist %}

