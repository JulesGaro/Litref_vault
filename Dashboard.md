> Here is a dashboard where yo can display things, put buttons, whatever you want...

```table-of-contents
style: nestedList # TOC style (nestedList|inlineFirstLevel)
maxLevel: 0 # Include headings up to the speficied level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Article note overview
```dataview
TABLE without id file.link as "Title",
file.frontmatter.authors as "Authors"
FROM "Article_note"
where contains(type,"literature-note")
```