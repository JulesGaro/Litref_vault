---
type: literature-note
title: Beyond modules and hubs - the potential of gene coexpression networks for investigating molecular mechanisms of complex brain disorders
authors: 
 -  C. Gaiteri 
 -  Y. Ding 
 -  B. French 
 -  G. C. Tseng 
 -  E. Sibille
journal: Genes, Brain and Behavior
tags: co-expression, neurological disorders, network, review, ⭐, regulation, differential co-expression, 📚
citekey: gaiteriModulesHubsPotential2014
creationdate: 08-01-2024
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
## References
 - Kang et al. [[Spatiotemporal transcriptome of the human brain]] *Nature* **478**, 483 - 489 (2011) ([web](https://doi.org/10.1038/nature10523))

 - Barrenas et al. [[Network Properties of Complex Human Disease Genes Identified through Genome-Wide Association Studies]] *PLoS ONE* **4** (2009) ([web](https://doi.org/10.1371/journal.pone.0008090))

 - P. Langfelder, P. Mischel & S. Horva [[When Is Hub Gene Selection Better than Standard Meta-Analysis?]] *PLoS ONE* **8** (2013) ([web](https://doi.org/10.1371/journal.pone.0061505))

 - M. Vidal, M. Cusick & A. Barabá [[Interactome Networks and Human Disease]] *Cell* **144**, 986-998 (2011) ([web](https://doi.org/10.1016/j.cell.2011.02.016))

 - Voineagu et al. [[Transcriptomic Analysis of Autistic Brain Reveals Convergent Molecular Pathology]] *Nature* **474**, 380 - 384 (2011) ([web](https://doi.org/10.1038/nature10110))

 - A. E. Ivliev, P. ’. ’. Hoen & M. Sergee [[Coexpression network analysis identifies transcriptional modules related to proastrocytic differentiation and sprouty signaling in glioma.]] *Cancer research* **70 24**, 10060-70 (2010) ([web](https://doi.org/10.1158/0008-5472.CAN-10-2465))

 - Nazarov et al. [[Interplay of microRNAs, transcription factors and target genes - linking dynamic expression changes to function]] *Nucleic Acids Research* **41**, 2817 - 2831 (2013) ([web](https://doi.org/10.1093/nar/gks1471))

 - D. Watts & S. Stroga [[Collective dynamics of ‘small-world’ networks]] *Nature* **393**, 440-442 (1998) ([web](https://doi.org/10.1038/30918))

 - Obayashi et al. [[COXPRESdb - a database of coexpressed gene networks in mammals]] *Nucleic Acids Research* **36**, D77 - D82 (2007) ([web](https://doi.org/10.1093/nar/gkm840))

 - Steuer et al. [[The mutual information - Detecting and evaluating dependencies between variables]] *Bioinformatics* **18 Suppl 2**, S231-40 (2002) ([web](https://doi.org/10.1093/BIOINFORMATICS/18.SUPPL_2.S231))

 - F. R. Cohen, T. Kohno & M. Xicoténca [[Orbit configuration spaces associated to discrete subgroups of PSL(2,R)]] *Journal of Pure and Applied Algebra* **213**, 2289-2300 (2009) ([web](https://doi.org/10.1016/J.JPAA.2009.04.003))

 - Oldham et al. [[Functional organization of the transcriptome in human brain]] *Nature Neuroscience* **11**, 1271-1282 (2008) ([web](https://doi.org/10.1038/nn.2207))

 - Horvath et al. [[Aging effects on DNA methylation modules in human brain and blood tissue]] *Genome Biology* **13**, R97 - R97 (2012) ([web](https://doi.org/10.1186/gb-2012-13-10-r97))

 - Clarke et al. [[Large scale microarray profiling and coexpression network analysis of CHO cells identifies transcriptional modules associated with growth and productivity.]] *Journal of biotechnology* **155 3**, 350-9 (2011) ([web](https://doi.org/10.1016/j.jbiotec.2011.07.011))

 - Ho et al. [[Differential variability analysis of gene expression and its application to human diseases]] *Bioinformatics* **24**, i390 - i398 (2008) ([web](https://doi.org/10.1093/bioinformatics/btn142))

 - Ponomarev et al. [[Gene Coexpression Networks in Human Brain Identify Epigenetic Modifications in Alcohol Dependence]] *The Journal of Neuroscience* **32**, 1884 - 1897 (2012) ([web](https://doi.org/10.1523/JNEUROSCI.3136-11.2012))

 - Hu et al. [[VisANT - data-integrating visual framework for biological networks and modules]] *Nucleic Acids Research* **33**, W352 - W357 (2005) ([web](https://doi.org/10.1093/nar/gki431))

 - Jothi et al. [[Genomic analysis reveals a tight link between transcription factor dynamics and regulatory network architecture]] *Molecular Systems Biology* **5**, 294 - 294 (2009) ([web](https://doi.org/10.1038/msb.2009.52))

 - C. Wolfe, I. Kohane & A. But [[Systematic survey reveals general applicability of "guilt-by-association" within gene coexpression networks]] *BMC Bioinformatics* **6**, 227 - 227 (2005) ([web](https://doi.org/10.1186/1471-2105-6-227))

 - Lee et al. [[Coexpression analysis of human genes across many microarray data sets.]] *Genome research* **14 6**, 1085-94 (2004) ([web](https://doi.org/10.1101/GR.1910904))

 - T. Evans & R. Lambiot [[Line graphs, link partitions, and overlapping communities.]] *Physical review. E, Statistical, nonlinear, and soft matter physics* **80 1 Pt 2**, 016105 (2009) ([web](https://doi.org/10.1103/PhysRevE.80.016105))

 - S. Bandyopadhyay & M. Bhattachary [[Analyzing miRNA co-expression networks to explore TF-miRNA regulation]] *BMC Bioinformatics* **10**, 163 - 163 (2009) ([web](https://doi.org/10.1186/1471-2105-10-163))

 - D. Kupfer, E. Frank & M. Philli [[Major depressive disorder - new clinical, neurobiological, and treatment perspectives]] *The Lancet* **379**, 1045-1055 (2012) ([web](https://doi.org/10.1016/S0140-6736(11)60602-8))

 - M. Ray, J. Ruan & W. Zha [[Variations in the transcriptome of Alzheimer's disease reveal molecular networks involved in cardiovascular diseases]] *Genome Biology* **9**, R148 - R148 (2008) ([web](https://doi.org/10.1186/gb-2008-9-10-r148))

 - I. Feldman, A. Rzhetsky & D. Vitk [[Network properties of genes harboring inherited disease mutations]] *Proceedings of the National Academy of Sciences* **105**, 4323 - 4328 (2008) ([web](https://doi.org/10.1073/pnas.0701722105))

 - G. A. Pavlopoulos, A. Wegener & R. Schneid [[A survey of visualization tools for biological network analysis]] *BioData Mining* **1**, 12 - 12 (2008) ([web](https://doi.org/10.1186/1756-0381-1-12))

 - Numata et al. [[DNA methylation signatures in development and aging of the human prefrontal cortex.]] *American journal of human genetics* **90 2**, 260-72 (2012) ([web](https://doi.org/10.1016/j.ajhg.2011.12.020))

 - S. Baskerville & D. Bart [[Microarray profiling of microRNAs reveals frequent coexpression with neighboring miRNAs and host genes.]] *RNA* **11 3**, 241-7 (2005) ([web](https://doi.org/10.1261/RNA.7240905))

 - Heinäniemi et al. [[Gene pair signatures in cell type transcriptomes reveal lineage control]] *Nature methods* **10**, 577 - 583 (2013) ([web](https://doi.org/10.1038/nmeth.2445))

 - Marco et al. [[Relationship between gene co-expression and sharing of transcription factor binding sites in Drosophila melanogaster]] *Bioinformatics* **25 19**, 2473-7 (2009) ([web](https://doi.org/10.1093/bioinformatics/btp462))

 - J. Gillis & P. Pavlid [[“Guilt by Association” Is the Exception Rather Than the Rule in Gene Networks]] *PLoS Computational Biology* **8** (2012) ([web](https://doi.org/10.1371/journal.pcbi.1002444))

 - Csermely et al. [[Structure and dynamics of molecular networks - A novel paradigm of drug discovery. A comprehensive review]] *Pharmacology & therapeutics* **138 3**, 333-408 (2012) ([web](https://doi.org/10.1016/j.pharmthera.2013.01.016))

 - Lieberman-Aiden et al. [[Comprehensive Mapping of Long-Range Interactions Reveals Folding Principles of the Human Genome]] *Science* **326**, 289 - 293 (2009) ([web](https://doi.org/10.1126/science.1181369))

 - Niida et al. [[A novel meta-analysis approach of cancer transcriptomes reveals prevailing transcriptional networks in cancer cells.]] *Genome informatics. International Conference on Genome Informatics* **22**, 121-31 (2010) ([web](https://doi.org/10.1142/9781848165786_0010))

 - Gaiteri et al. [[Altered Gene Synchrony Suggests a Combined Hormone-Mediated Dysregulated State in Major Depression]] *PLoS ONE* **5** (2010) ([web](https://doi.org/10.1371/journal.pone.0009970))

 - Lonsdale et al. [[The Genotype-Tissue Expression (GTEx) project]] *Nature Genetics* **45**, 580-585 (2013) ([web](https://doi.org/10.1038/ng.2653))

 - Dong et al. [[Integrated analysis of mutations, miRNA and mRNA expression in glioblastoma]] *BMC Systems Biology* **4**, 163 - 163 (2010) ([web](https://doi.org/10.1186/1752-0509-4-163))

 - Menashe et al. [[Co-expression Profiling of Autism Genes in the Mouse Brain]] *PLoS Computational Biology* **9** (2013) ([web](https://doi.org/10.1371/journal.pcbi.1003128))

 - Zhang et al. [[Integrated Systems Approach Identifies Genetic Nodes and Networks in Late-Onset Alzheimer’s Disease]] *Cell* **153**, 707-720 (2013) ([web](https://doi.org/10.1016/j.cell.2013.03.030))

 - Jong et al. [[A Gene Co-Expression Network in Whole Blood of Schizophrenia Patients Is Independent of Antipsychotic-Use and Enriched for Brain-Expressed Genes]] *PLoS ONE* **7** (2012) ([web](https://doi.org/10.1371/journal.pone.0039498))

 - S. Vega-Pons & J. Ruiz-Shulclop [[A Survey of Clustering Ensemble Algorithms]] *Int. J. Pattern Recognit. Artif. Intell.* **25**, 337-372 (2011) ([web](https://doi.org/10.1142/S0218001411008683))

 - P. F. Jonsson & P. Bat [[Global topological features of cancer proteins in the human interactome]] *Bioinformatics* **22 18**, 2291-7 (2006) ([web](https://doi.org/10.1093/bioinformatics/btl390))

 - Erraji-Benchekroun et al. [[Molecular aging in human prefrontal cortex is selective and continuous throughout adult life]] *Biological Psychiatry* **57**, 549-558 (2005) ([web](https://doi.org/10.1016/j.biopsych.2004.10.034))

 - Miller et al. [[Genes and pathways underlying regional and cell type changes in Alzheimer's disease]] *Genome Medicine* **5**, 48 - 48 (2013) ([web](https://doi.org/10.1186/gm452))

 - Ebisuya et al. [[Ripples from neighbouring transcription]] *Nature Cell Biology* **10**, 1106-1113 (2008) ([web](https://doi.org/10.1038/ncb1771))

 - Gulsuner et al. [[Spatial and Temporal Mapping of De Novo Mutations in Schizophrenia to a Fetal Prefrontal Cortical Network]] *Cell* **154**, 518-529 (2013) ([web](https://doi.org/10.1016/j.cell.2013.06.049))

 - Iskar et al. [[Characterization of drug-induced transcriptional modules - towards drug repositioning and functional understanding]] *Molecular Systems Biology* **9**, 662 - 662 (2013) ([web](https://doi.org/10.1038/msb.2013.20))

 - Natsoulis et al. [[The liver pharmacological and xenobiotic gene response repertoire]] *Molecular Systems Biology* **4**, 175 - 175 (2008) ([web](https://doi.org/10.1038/msb.2008.9))

 - Stam et al. [[Small-world networks and functional connectivity in Alzheimer's disease.]] *Cerebral cortex* **17 1**, 92-9 (2006) ([web](https://doi.org/10.1093/CERCOR/BHJ127))

 - Krzywinski et al. [[Hive plots - rational approach to visualizing networks]] *Briefings in bioinformatics* **13 5**, 627-44 (2012) ([web](https://doi.org/10.1093/bib/bbr069))

 - Jay et al. [[A systematic comparison of genome-scale clustering algorithms]] *BMC Bioinformatics* **13**, S7 - S7 (2012) ([web](https://doi.org/10.1186/1471-2105-13-S10-S7))

 - K. Park & D. K [[Localized network centrality and essentiality in the yeast–protein interaction network]] *PROTEOMICS* **9** (2009) ([web](https://doi.org/10.1002/pmic.200900357))

 - S. Fortuna [[Community detection in graphs]] *ArXiv* **abs/0906.0612** (2009) ([web](https://doi.org/10.1016/j.physrep.2009.11.002))

 - W. J. R. Longabau [[Combing the hairball with BioFabric - a new approach for visualization of large networks]] *BMC Bioinformatics* **13**, 275 - 275 (2012) ([web](https://doi.org/10.1186/1471-2105-13-275))

 - Konopka et al. [[Modeling the functional genomics of autism using human neurons]] *Molecular psychiatry* **17**, 202 - 214 (2010) ([web](https://doi.org/10.1038/mp.2011.60))

 - Rhinn et al. [[Alternative α-synuclein transcript usage as a convergent mechanism in Parkinson's disease pathology]] *Nature Communications* **3** (2012) ([web](https://doi.org/10.1038/ncomms2032))

 - Shannon et al. [[Cytoscape - a software environment for integrated models of biomolecular interaction networks.]] *Genome research* **13 11**, 2498-504 (2003) ([web](https://doi.org/10.1101/GR.1239303))

 - N. Hudson, B. Dalrymple & A. Revert [[Beyond differential expression - the quest for causal mutations and effector molecules]] *BMC Genomics* **13**, 356 - 356 (2012) ([web](https://doi.org/10.1186/1471-2164-13-356))

 - D. Amar, H. Safer & R. Sham [[Dissection of Regulatory Networks that Are Altered in Disease via Differential Co-expression]] *PLoS Computational Biology* **9** (2013) ([web](https://doi.org/10.1371/journal.pcbi.1002955))

 - Hawrylycz et al. [[An anatomically comprehensive atlas of the adult human brain transcriptome]] *Nature* **489**, 391-399 (2012) ([web](https://doi.org/10.1038/nature11405))

 - Li et al. [[Integrative Analysis of Many Weighted Co-Expression Networks Using Tensor Computation]] *PLoS Computational Biology* **7** (2011) ([web](https://doi.org/10.1371/journal.pcbi.1001106))

 - Gennarino et al. [[Identification of microRNA-regulated gene networks by expression analysis of target genes]] *Genome Research* **22**, 1163 - 1172 (2012) ([web](https://doi.org/10.1101/gr.130435.111))

 - Bell et al. [[Integrated Genomic Analyses of Ovarian Carcinoma]] *Nature* **474**, 609 - 615 (2011) ([web](https://doi.org/10.1038/nature10166))

 - Lamb et al. [[The Connectivity Map - Using Gene-Expression Signatures to Connect Small Molecules, Genes, and Disease]] *Science* **313**, 1929 - 1935 (2006) ([web](https://doi.org/10.1126/science.1132939))

 - Langfelder et al. [[Is My Network Module Preserved and Reproducible?]] *PLoS Computational Biology* **7** (2011) ([web](https://doi.org/10.1371/journal.pcbi.1001057))

 - H. Zou & T. Hast [[Addendum - Regularization and variable selection via the elastic net]] *Journal of the Royal Statistical Society: Series B (Statistical Methodology)* **67** (2005) ([web](https://doi.org/10.1111/j.1467-9868.2005.00527.x))

 - Torkamani et al. [[Coexpression network analysis of neural tissue reveals perturbations in developmental processes in schizophrenia.]] *Genome research* **20 4**, 403-12 (2010) ([web](https://doi.org/10.1101/gr.101956.109))

 - Jeong et al. [[Lethality and centrality in protein networks]] *Nature* **411**, 41-42 (2001) ([web](https://doi.org/10.1038/35075138))

 - N. Hudson, A. Reverter & B. Dalrymp [[A Differential Wiring Analysis of Expression Data Correctly Identifies the Gene Containing the Causal Mutation]] *PLoS Computational Biology* **5** (2009) ([web](https://doi.org/10.1371/journal.pcbi.1000382))

 - M. Oldham, S. Horvath & D. Geschwi [[Conservation and evolution of gene coexpression networks in human and chimpanzee brains]] *Proceedings of the National Academy of Sciences* **103**, 17973 - 17978 (2006) ([web](https://doi.org/10.1073/pnas.0605938103))

 - T. Przytycka, M. Singh & D. Slon [[Toward the dynamic interactome - it's about time]] *Briefings in bioinformatics* **11 1**, 15-29 (2010) ([web](https://doi.org/10.1093/bib/bbp057))

 - J. A. Miller, M. Oldham & D. Geschwi [[A Systems Level Analysis of Transcriptional Changes in Alzheimer's Disease and Normal Aging]] *The Journal of Neuroscience* **28**, 1410 - 1420 (2008) ([web](https://doi.org/10.1523/JNEUROSCI.4098-07.2008))

 - Jojic et al. [[Identification of transcriptional regulators in the mouse immune system]] *Nature immunology* **14**, 633 - 643 (2013) ([web](https://doi.org/10.1038/ni.2587))

 - D. Kostka & R. Spa [[Finding disease specific alterations in the co-expression of genes]] *Bioinformatics* **20 Suppl 1**, i194-9 (2004) ([web](https://doi.org/10.1093/BIOINFORMATICS/BTH909))

 - J. Leek & J. D. Stor [[Capturing Heterogeneity in Gene Expression Studies by Surrogate Variable Analysis]] *PLoS Genetics* **3** (2007) ([web](https://doi.org/10.1371/JOURNAL.PGEN.0030161))

 - Breitkreutz et al. [[Molecular signaling network complexity is correlated with cancer patient survivability]] *Proceedings of the National Academy of Sciences* **109**, 9209 - 9212 (2012) ([web](https://doi.org/10.1073/pnas.1201416109))

 - E. Sibille & B. J. Fren [[Biological substrates underpinning diagnosis of major depression.]] *The international journal of neuropsychopharmacology* **16 8**, 1893-909 (2013) ([web](https://doi.org/10.1017/S1461145713000436))

 - Mar et al. [[Variance of Gene Expression Identifies Altered Network Constraints in Neurological Disease]] *PLoS Genetics* **7** (2011) ([web](https://doi.org/10.1371/journal.pgen.1002207))

 - M. Jali [[Error and attack tolerance of small-worldness in complex networks]] *J. Informetrics* **5**, 422-430 (2011) ([web](https://doi.org/10.1016/J.JOI.2011.03.002))

 - Chen et al. [[Two Gene Co-expression Modules Differentiate Psychotics and Controls]] *Molecular psychiatry* **18**, 1308 - 1314 (2012) ([web](https://doi.org/10.1038/mp.2012.146))

 - L. Song, P. Langfelder & S. Horva [[Comparison of co-expression measures - mutual information, correlation, and model based indices]] *BMC Bioinformatics* **13**, 328 - 328 (2012) ([web](https://doi.org/10.1186/1471-2105-13-328))

 - Mabbott et al. [[Meta-analysis of lineage-specific gene expression signatures in mouse leukocyte populations.]] *Immunobiology* **215 9-10**, 724-36 (2010) ([web](https://doi.org/10.1016/j.imbio.2010.05.012))

 - Basso et al. [[Reverse engineering of regulatory networks in human B cells]] *Nature Genetics* **37**, 382-390 (2005) ([web](https://doi.org/10.1038/ng1532))

 - Gerstein et al. [[Architecture of the human regulatory network derived from ENCODE data]] *Nature* **489**, 91-100 (2012) ([web](https://doi.org/10.1038/nature11245))

 - A. Ma’ay [[Insights into the Organization of Biochemical Regulatory Networks Using Graph Theory Analyses*]] *Journal of Biological Chemistry* **284**, 5451 - 5455 (2009) ([web](https://doi.org/10.1074/jbc.R800056200))

 - Lee et al. [[Network models of genome-wide association studies uncover the topological centrality of protein interactions in complex diseases]] *Journal of the American Medical Informatics Association : JAMIA* **20**, 619 - 629 (2013) ([web](https://doi.org/10.1136/amiajnl-2012-001519))

 - L. Southworth, A. Owen & S. K. K [[Aging Mice Show a Decreasing Correlation of Gene Expression within Genetic Modules]] *PLoS Genetics* **5** (2009) ([web](https://doi.org/10.1371/journal.pgen.1000776))

 - Pirooznia et al. [[A comparative study of different machine learning methods on microarray gene expression data]] *BMC Genomics* **9**, S13 - S13 (2008) ([web](https://doi.org/10.1186/1471-2164-9-S1-S13))

 - Cai et al. [[Is human blood a good surrogate for brain tissue in transcriptional studies?]] *BMC Genomics* **11**, 589 - 589 (2010) ([web](https://doi.org/10.1186/1471-2164-11-589))

 - M. Bhattacharyya & S. Bandyopadhy [[Studying the differential co-expression of microRNAs reveals significant role of white matter in early Alzheimer's progression.]] *Molecular bioSystems* **9 3**, 457-66 (2013) ([web](https://doi.org/10.1039/c2mb25434d))

 - C. Gaiteri & E. Sibil [[Differentially Expressed Genes in Major Depression Reside on the Periphery of Resilient Gene Coexpression Networks]] *Frontiers in Neuroscience* **5** (2011) ([web](https://doi.org/10.3389/fnins.2011.00095))

 - Choi et al. [[Attractor Landscape Analysis Reveals Feedback Loops in the p53 Network That Control the Cellular Response to DNA Damage]] *Science Signaling* **5**, ra83 - ra83 (2012) ([web](https://doi.org/10.1126/scisignal.2003363))

 - D. Homouz & A. Kudlic [[The 3D Organization of the Yeast Genome Correlates with Co-Expression and Reflects Functional Relations between Genes]] *PLoS ONE* **8** (2013) ([web](https://doi.org/10.1371/journal.pone.0054699))

 - A. Hopki [[Network pharmacology - the next paradigm in drug discovery.]] *Nature chemical biology* **4 11**, 682-90 (2008) ([web](https://doi.org/10.1038/nchembio.118))

 - A. G. D. L. Fuen [[From 'differential expression' to 'differential networking' - identification of dysfunctional regulatory networks in diseases.]] *Trends in genetics : TIG* **26 7**, 326-33 (2010) ([web](https://doi.org/10.1016/j.tig.2010.05.001))

 - Emmert-Streib et al. [[The human disease network]] *Systems Biomedicine* **1**, 20 - 28 (2013) ([web](https://doi.org/10.4161/sysb.22816))



%% end references %%



%% Import Date: 2023-11-30T14:16:23.474+01:00 %%
