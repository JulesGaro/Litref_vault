




TODO :

- [ ] More biblio on how to aggregate and normalize for pseudobulk
- [ ] actually look at how I did that during M2 internship


```dataview
TABLE without id file.link as "Titre",
file.frontmatter.authors as "Authors"
FROM "Article_note"
where contains(type,"literature-note")
```