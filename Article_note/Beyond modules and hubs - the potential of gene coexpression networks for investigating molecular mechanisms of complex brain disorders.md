---
type: literature-note
title: Beyond modules and hubs - the potential of gene coexpression networks for investigating molecular mechanisms of complex brain disorders
authors: C. Gaiteri, Y. Ding, B. French, G. C. Tseng, E. Sibille,
journal: Genes, Brain and Behavior
tags: co-expression, neurological disorders, network, review, 📗, ⭐, regulation, differential co-expression, 📚
citekey: gaiteriModulesHubsPotential2014
---
# Beyond modules and hubs: the potential of gene coexpression networks for investigating molecular mechanisms of complex brain disorders
```table-of-contents
style: nestedList # TOC style (nestedList|inlineFirstLevel)
maxLevel: 0 # Include headings up to the speficied level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
*Hello : if you did get that git repository for your own this link might not work =)*
 Zotero PDF links : [PDF](zotero://open-pdf/library/items/AKI446Q5)
## Article summary :
Article by *Gaiteri et al.* published in *Genes, Brain and Behavior* the 01-01-2014 
> [!ABSTRACT]- ABSTRACT
>  
> Abstract                            In a research environment dominated by reductionist approaches to brain disease mechanisms, gene network analysis provides a complementary framework in which to tackle the complex dysregulations that occur in neuropsychiatric and other neurological disorders. Gene–gene expression correlations are a common source of molecular networks because they can be extracted from high‐dimensional disease data and encapsulate the activity of multiple regulatory systems. However, the analysis of gene coexpression patterns is often treated as a mechanistic black box, in which looming ‘hub genes’ direct cellular networks, and where other features are obscured. By examining the biophysical bases of coexpression and gene regulatory changes that occur in disease, recent studies suggest it is possible to use coexpression networks as a multi‐omic screening procedure to generate novel hypotheses for disease mechanisms. Because technical processing steps can affect the outcome and interpretation of coexpression networks, we examine the assumptions and alternatives to common patterns of coexpression analysis and discuss additional topics such as acceptable datasets for coexpression analysis, the robust identification of modules, disease‐related prioritization of genes and molecular systems and network meta‐analysis. To accelerate coexpression research beyond modules and hubs, we highlight some emerging directions for coexpression network research that are especially relevant to complex brain disease, including the centrality–lethality relationship, integration with machine learning approaches and network pharmacology               .
> 
%% begin notes %%
## Notes

Really good article that is a good introduction to the principle of co-expression and that address several problematic and limitations of this method.

%% end notes %%
## PDF Annotations

*Imported: 2023-11-30 14:16*
#### ✅ Comment, noticeable point

> [!quote|green]+ Highlight ([page. 21](zotero://open-pdf/library/items/AKI446Q5?page=21&annotation=HBDS3NVY))
> An ideal experiment to associate specific molecular mechanisms with differential coexpression would be to assess the regulatory structure of multiple systems in a disease model (Hudson et al. 2012). This would require multiple assays to be measured in pure cell populations, including chromosome interactions, ChIP-seq on at least several TFs, miRNA and methylation. 
> - **I guess you might lose the scalability of the co-expression then.**

#### 💙 To keep in mind/usefull/good reference

> [!quote|blue]+ Highlight ([page. 13](zotero://open-pdf/library/items/AKI446Q5?page=13&annotation=EMUYVR4P))
> For example, major depressive disorder and other neuropsychiatric disorders involve changes in multiple genes, each conferring small and incremental risk that potentially converge in deregulated biological pathways, cellular functions and local circuit changes, eventually scaling up to brain region pathophysiology (Belmaker & Agam 2008; Sibille & French 2013). 
> - **Belmaker, R. & Agam, G. (2008) Major depressive disorder. NEnglJ Med 358, 55–68.<br />
Sibille, E. & French, B. (2013) Biological substrates underpinning diagnosis of major depression. Int J Neuropsychopharmacol 16, 1893 – 1909.**

> [!quote|blue]+ Highlight ([page. 17](zotero://open-pdf/library/items/AKI446Q5?page=17&annotation=JKQI28YL))
> From a theoretical perspective, information flow through small-world, scale-free networks is unlikely to be affected by random node deletion, but is especially vulnerable to targeted hub attack (Albert et al. 2000). In a disease context, this is termed the ‘lethality–centrality’ relationship (Jeong et al. 2001) and is supported by examples from multiple molecular and brain networks in which hub targeting leads to crucial functional impairment (Stam et al. 2007). Practically, hubs provide a specific focus for investigations into disease-correlated modules of genes (next section), (Miller et al. 2008; Ray et al. 2008; Torkamani et al. 2010; Voineagu et al. 2011). However, restricting experimental attention to coexpression hubs may discount other relevant molecules and is no guarantee of phenotypic effects, as coexpression links may represent a variety of causal or non-causal interactions (Fig. 1). 
> - **Interesting view of the "Pro & Cons" of looking at Hub genes.**

#### 🗝️ Key point

> [!quote|purple]+ Highlight ([page. 13](zotero://open-pdf/library/items/AKI446Q5?page=13&annotation=INKHBS4P))
> However, the analysis of gene coexpression patterns is often treated as a mechanistic black box, in which looming ‘hub genes’ direct cellular networks, and where other features are obscured. 
> - **Although most paper don't address any of this when using co-expression...**

> [!quote|purple]+ Highlight ([page. 13](zotero://open-pdf/library/items/AKI446Q5?page=13&annotation=LIN7QYSF))
> At the level of genes, dynamic modeling approaches, such as probabilistic Boolean networks, can mimic processes 
> - **"involved in cellular decisions, such as stochastic switching of transcription factors (TFs) that represent cellular decisions (Hein  ̈ aniemi et al. 2013). In practice, dynamic simulations and modeling efforts are limited to small systems in which prediction can be easily verified (Choi et al. 2012). Notably, none of these techniques permit multisystem genome-scale dynamic simulations of disease processes, due to uncharacterized genetic and molecular dynamics-related parameters, computational limitations and a paucity of biomarkers for intermediate phenotypes (Przytycka etal. 2010)."**

> [!quote|purple]+ Highlight ([page. 14](zotero://open-pdf/library/items/AKI446Q5?page=14&annotation=AVI6ZQ7D))
> Studies in multiples species, tissues and platforms have shown that coexpressed genes tend to be functionally related (Obayashi et al. 2008; Oldham et al. 2006). 
> - **Obayashi, T., Hayashi, S., Shibaoka, M., Saeki, M., Ohta, H. & Kinoshita, K. (2008) COXPRESdb: a database of coexpressed gene networks in mammals. NucleicAcidsRes 36, D77–D82.<br />
Oldham, M., Horvath, S. & Geschwind, D. (2006) Conservation and evolution of gene coexpression networks in human and chimpanzee brains. ProcNatlAcadSciUSA 103, 17973–17978.<br />
Horvath on this paper**

> [!quote|purple]+ Highlight ([page. 17](zotero://open-pdf/library/items/AKI446Q5?page=17&annotation=Z7NBNL2C))
> While clustering methods attempt to minimize links between modules, thousands of such links remain after clustering, which would be expected given the overlapping regulatory domains of systems that generate coexpression (Figs. 1,3) indicating that the concept of functionally and structurally independent modules is a convenient simplification of the structure of gene–gene correlations. 
> - **keeping in mind that modules are far from an absolute and perfect representation of the biology.**
####  🌟 Critical point for personal/work interest

> [!quote|yellow]+ Highlight ([page. 13](zotero://open-pdf/library/items/AKI446Q5?page=13&annotation=AQ9ULMBZ))
> To accelerate coexpression research beyond modules and hubs, we highlight some emerging directions for coexpression network research that are especially relevant to complex brain disease, including the centrality–lethality relationship, integration with machine learning approaches and network pharmacology. 
> - **Study still mainly focus on modules, functional annotation on modules and hub genes.**

> [!quote|yellow]+ Image ([page. 14](zotero://open-pdf/library/items/AKI446Q5?page=14&annotation=VXK3EGZS))
> ![[Media/zotero_images/gaiteriModulesHubsPotential2014/gaiteriModulesHubsPotential2014-2-x298-y493.png]]
> - **Figure 1: Summary of molecular, cellular, tissue and technical regulatory sources of observed gene–gene correlations/coexpression links.<br />
Good figure to pictures the different sources of variation leading to a potential observed coexpression even if its not the first "goal" of the figure it still interesting to see it that way**

> [!quote|yellow]+ Highlight ([page. 14](zotero://open-pdf/library/items/AKI446Q5?page=14&annotation=KIL3XSK6))
> Interpreting coexpression networks that are composed of thousands of gene–gene correlations is challenging because these correlations can arise from several biological and non-biological sources that are mathematically indistinguishable (Fig. 1). Any mechanism that synchronously regulates transcription of multiple genes may potentially generate coexpression relationships. 
> - **THIS**

> [!quote|yellow]+ Image ([page. 15](zotero://open-pdf/library/items/AKI446Q5?page=15&annotation=BMZXZ2YW))
> ![[Media/zotero_images/gaiteriModulesHubsPotential2014/gaiteriModulesHubsPotential2014-3-x58-y453.png]]
> - **Quite related to figure 1 and point out why its kinda cool to be able to do "differential co-expression analysis"**

> [!quote|yellow]+ Highlight ([page. 17](zotero://open-pdf/library/items/AKI446Q5?page=17&annotation=SHQY7Q4U))
> However, all clustering results can be evaluated through statistics on their reproducibility under data resampling and ability to find locally dense clusters (Fortunato 2010). 
> - **Beyond having a decent n for doing co-expression it would be interesting to have enough sample to be able to resample in order to assess module robustness. If there is change in for example most co-expressed genes list with gene of interest or other marker, it could be interesting to see if some genes keep being pulled out to ensure that they are relevant.**

> [!quote|yellow]+ Highlight ([page. 21](zotero://open-pdf/library/items/AKI446Q5?page=21&annotation=VGKGB7LU))
> Disease severity may interact with molecular connectivity in such a way that places disease genes at different network locations. This interaction may explain some of the apparently conflicted results mentioned previously. Specifically, more severe diseases are associated with deficits in more central genes (Barrenas et al. 2009). Such a relationship could be tested in compiling differential gene expression signatures from diseases of varying severity/lethality and may be useful in understanding control mechanisms in complex diseases. The relationship of disease to network structure will likely be more complex than a linear relationship between the number of connections of disease-associated genes vs. disease severity (Park & Kim 2009). 
> - **interesting**


%% begin references %%
## References
%% references anchor %%
```shell
# Change the path to the path to be the absolute path to your vault
vault_path="/home/jules/Documents/phd/obsidian_vault/"
#Change that path to be the relative path from your vault root to the folder you store zotero imported literature notes
lit_note_path_from_vault="Article_note/"
cd $vault_path
# Change the script to match the naming pattern of yout note,
# You can refer to how they are named in the zotero integration plugin # settings for that template
python3 .obsidian/scripts/python/buildReferences.py "Beyond modules and hubs - the potential of gene coexpression networks for investigating molecular mechanisms of complex brain disorders.md"

```
%% references anchor %%

%% end references %%



%% Import Date: 2023-11-30T14:16:23.474+01:00 %%
