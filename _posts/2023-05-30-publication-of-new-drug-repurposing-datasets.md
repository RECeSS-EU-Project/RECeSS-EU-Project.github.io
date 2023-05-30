---
title: "New drug repurposing datasets"
date: 2023-05-30T00:00:00-00:00
categories:
  - blog
tags:
  - dataset
  - drug repurposing
  - collaborative filtering
  - science replication
---

We are really excited to present the first two drug repurposing datasets for collaborative filtering produced during the RECeSS project! 

In Machine Learning, having datasets of high quality are crucial to train performant classification methods. The quality of the data is directly related to how easily the algorithm will be able to identify key features that allow the classification of datapoints into one class or another. In particular, in collaborative filtering-based drug repurposing, these classes correspond to the identification of a positive drug-disease matching (that is, the drug is shown to treat the disease), or a negative one (either the drug is ineffective in treating the disease, or only at too high, thus toxic, doses).

A dataset for collaborative filtering-based drug repurposing comprises three matrices:

- A matrix filled with 0, 1, or -1 values, which represents the known associations between drugs and diseases. Typically, 1 (resp., -1) stands for a positive (resp., negative) drug-disease matching. Finally, 0 represents unknown (untested) drug-disease matchings.

- A matrix which encodes selected features for every drug involved in at least one matching in the previous matrix. Drug features might be the similarity of its chemical structure to the ones of other drugs, or the variation in gene activity which can be imputed to the treatment by that drug.

- A matrix which similarly encodes features for every disease involved in at least one matching in the previous matrix. In that case, features of a disease might correspond to the similarity of its associated phenotypes (*i*.*e*., observable characteristics associated with the disease), or the variation in gene activity which can be imputed to the presence of disease.

Such datasets are for instance the Gottlieb dataset [[1]](https://www.embopress.org/doi/full/10.1038/msb.2011.26), the CDataset and DNDatasets [[2]](https://academic.oup.com/bioinformatics/article/34/11/1904/4820334) (which can be downloaded at [this page](http://bioinformatics.csu.edu.cn/resources/softs/DrugRepositioning/DRRS/index.html)), the LRLSS Dataset [[3]](https://doi.org/10.1093/bioinformatics/btw770) (available at [this page](https://github.com/LiangXujun/LRSSL)), and the PREDICT-Gottlieb dataset [[4]](https://www.frontiersin.org/articles/10.3389/fphar.2021.784171/full), accessible at [this page](https://github.com/GCQ2119216031/DDA-SKF). The latter has the same drug-disease matching matrix as the Gottlieb dataset, but considers different drug and diseases features.

In that context, not only it is important to identify in a unique way each disease, drug and features involved in the dataset, but being able to access the code that has produced the dataset is also of paramount importance. As a general rule, science (and biology) is always updated, as more accurate knowledge is accrued. As such, something which might be thought correct at some point in time might be proven false or refined (*e*.*g*., disease or drug annotations), or not accurate (for instance, for gene activity measurements). Access to the code allows to provide that update to the corresponding dataset in a straightforward way. 

In the first part of the RECeSS project, we introduce the PREDICT and TRANSCRIPT datasets, uploaded on Zenodo 

- TRANSCRIPT dataset [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7982969.svg)](https://doi.org/10.5281/zenodo.7982969)

- PREDICT dataset [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7982964.svg)](https://doi.org/10.5281/zenodo.7982964)

which characteristics are described in the following table. The sparsity number is a measure of the available information about drug-disease matchings (the higher, the more there is known matchings in the dataset). The sparsity number is the percentage of known matchings (*i*.*e*., non zeros values in the matrix of matchings). Those values are compared to known drug repurposing datasets available in the litterature.

Dataset   |    #drugs★ (#features) | #diseases★ (#features) |  #positive matchings | #negative matchings  | Sparsity number✦
---------------|---------------|---------------|--------------------------|-------------------------|----------------
PREDICT v2     | 1,351 (6,265) | 1,066 (2,914) |   5,624                  |  152                    | 0.34%
TRANSCRIPT v2  | 204 (12,096)  | 116 (12,096)  |   401                    |  11                     | 0.45%
---------------|---------------|---------------|--------------------------|-------------------------|----------------
Gottlieb / FDataset [[2]](https://academic.oup.com/bioinformatics/article/34/11/1904/4820334)   |593 (593)      |313 (313)      |  1933                    |    0                    | 1.04%
CDataset [[2]](https://academic.oup.com/bioinformatics/article/34/11/1904/4820334)   |663 (663)      |409 (409)      |  2532                    |     0                   | 0.93%
DNDataset [[2]](https://academic.oup.com/bioinformatics/article/34/11/1904/4820334)  |550  (1490)    |360  (4516)    | 1008                     |     0                   | 0.01%
LRSSL [[3]](https://doi.org/10.1093/bioinformatics/btw770)      | 763 (1526)    |681 (681)      | 3051                     |      0                  | 0.59%
PREDICT-Gottlieb [[4]](https://www.frontiersin.org/articles/10.3389/fphar.2021.784171/full)   |593 (1,779)     |313 (313)      |  1933                    |    0                    | 1.04%

Contrary to all other datasets in the table, the PREDICT dataset has missing values, that is, some information about the drugs / diseases is missing. For instance, the percentage of missing values in the drug feature matrix is 31%, whereas it is 60% in the disease feature matrix. Moreover, contrary to all other datasets, the drug and disease feature matrices in TRANSCRIPT dataset are not (a concatenation of) similarity matrices, but true biological features, in terms of gene expression variation.

What is interesting in those two novel datasets is that they now allow to study *how to deal with missing values* --which is a pervasive issue when dealing with biological data of heterogenous types-- and to *apply explainability approaches* to better understand the recommendations made by a collaborative filtering approach. Moreover, PREDICT and TRANSCRIPT are the first datasets which comprise *true* negative drug-disease matchings, which can allow going beyond the Positive-Unlabeled Learning† framework. 

The type of data used to build datasets PREDICT and TRANSCRIPT, along with the associated code, are detailed respectively in notebooks *PREDICT_dataset.ipynb* and *TRANSCRIPT_dataset.ipynb* in the following [GitHub repository](https://github.com/RECeSS-EU-Project/drug-repurposing-datasets). Those notebooks can be run again or improved in order to update those datasets with novel biological information or database update.

We are really looking forward to explain more in details collaborative filtering, and to apply classic collaborative filtering methods on those datasets!

### Footnotes

★ Involved in at least one nonzero drug-disease matching.

✦ Rounded up to 0.01.

† This concept will be explained in a future blog post.

### References

[[1]](https://www.embopress.org/doi/full/10.1038/msb.2011.26) Gottlieb, A., Stein, G. Y., Ruppin, E., & Sharan, R. (2011). PREDICT: a method for inferring novel drug indications with application to personalized medicine. Molecular systems biology, 7(1), 496.

[[2]](https://academic.oup.com/bioinformatics/article/34/11/1904/4820334) Luo, H., Li, M., Wang, S., Liu, Q., Li, Y., & Wang, J. (2018). Computational drug repositioning using low-rank matrix approximation and randomized algorithms. Bioinformatics, 34(11), 1904-1912.

[[3]](https://doi.org/10.1093/bioinformatics/btw770) Liang, X., Zhang, P., Yan, L., Fu, Y., Peng, F., Qu, L., ... & Chen, Z. (2017). LRSSL: predict and interpret drug–disease associations based on data integration using sparse subspace learning. Bioinformatics, 33(8), 1187-1196.

[[4]](https://www.frontiersin.org/articles/10.3389/fphar.2021.784171/full) Gao, C. Q., Zhou, Y. K., Xin, X. H., Min, H., & Du, P. F. (2022). DDA-SKF: Predicting Drug–Disease Associations Using Similarity Kernel Fusion. Frontiers in Pharmacology, 12, 3971.
