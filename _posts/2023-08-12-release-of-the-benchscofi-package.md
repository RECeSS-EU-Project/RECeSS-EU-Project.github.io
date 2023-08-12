---
title: "Release of the *benchscofi* package"
date: 2023-08-12T00:00:00-00:00
categories:
  - blog
tags:
  - Python
  - collaborative filtering
  - drug repurposing
  - open science
  - reproducibility
---

The Python package *benchscofi* for the benchmark of collaborative filtering-based approaches to drug repurposing is out!

The goal of *benchscofi* was to implement state-of-the-art algorithms for drug repurposing, and run the benchmarks on the drug repurposing datasets shown in the [drug repurposing dataset blog post](https://recess-eu-project.github.io/blog/publication-of-new-drug-repurposing-datasets/). For further information on collaborative filtering and its application to drug repurposing, please refer to our previous [post](https://recess-eu-project.github.io/blog/release-of-the-stanscofi-package/). 

This package will facilitate the development of collaborative filtering algorithms applied to drug repurposing, and to better assess the improvement over the state-of-the-art. Right now, *benchscofi* integrates 19 collaborative filtering algorithms from the literature, 16 accuracy and ranking metrics, and 9 drug repurposing datasets, with a large variety of drug and disease biologically meaningful features. Its modular structure allows for adding new algorithms and datasets in a straightforward way.

Below are some of the results we have obtained using this package (see ``README.md`` file in the repository for further details):

  Algorithm  (AUC)         | TRANSCRIPT    [a] | Gottlieb [b]  | Cdataset [c] | LRSSL [d]  | 
-------------------------- | ----------------- | ------------- | ------------ | ---------- |
PMF [1]                    |  0.579            |  0.598        |  0.604       |  0.611     |
ALSWR [2]                  |  0.507            |  0.677        |  0.724       |  0.685     |
FastaiCollabWrapper [3]    |  0.876            |  0.856        |  0.837       |  0.851     |
NIMCGCN [4]                |  0.854            |  0.843        |  0.841       |  0.873     |
DRRS [5]                   |  0.662            |  0.838        |  0.878       |  0.892     |
SCPMF [6]                  |  0.680            |  0.548        |  0.538       |  0.708     |
BNNR [7]                   |  0.922            |  0.949        |  0.959       |  0.972     |
LRSSL [8]                  |  0.581 (90%)      |  0.159        |  0.846       |  0.665     |
MBiRW [9]                  |  0.913            |  0.954        |  0.965       |  0.975     |
LibMFWrapper [10]          |  0.919            |  0.892        |  0.912       |  0.873     |
LogisticMF [11]            |  0.910            |  0.941        |  0.955       |  0.933     |
DDA_SKF [12]               |  0.453            |  0.544        |  0.264 (20%) |  0.542     |
HAN [13]                   |  0.870            |  0.909        |  0.905       |  0.923     | 

This package is a step towards increased reproducibility, easier development and testing of competitive drug repurposing methods.

**benchscofi** is hosted on the [PyPI](https://pypi.org/project/benchscofi/) repository. In order to have an overview of the package, please have a look at the [notebooks](https://github.com/RECeSS-EU-Project/benchscofi/blob/master/docs/). Feel free to report issues or to make suggestions on the [GitHub issue flagging page](https://github.com/RECeSS-EU-Project/benchscofi/issues) or using our [contact form](https://recess-eu-project.github.io/contact/)!

### References

**[a]** Réda, Clémence. (2023). TRANSCRIPT drug repurposing dataset (2.0.0) [Data set]. Zenodo. doi:10.5281/zenodo.7982976

**[b]** Gottlieb, A., Stein, G. Y., Ruppin, E., & Sharan, R. (2011). PREDICT: a method for inferring novel drug indications with application to personalized medicine. Molecular systems biology, 7(1), 496.

**[c]** Luo, H., Li, M., Wang, S., Liu, Q., Li, Y., & Wang, J. (2018). Computational drug repositioning using low-rank matrix approximation and randomized algorithms. Bioinformatics, 34(11), 1904-1912.

**[d]** Réda, Clémence. (2023). PREDICT drug repurposing dataset (2.0.1) [Data set]. Zenodo. doi:10.5281/zenodo.7983090

**[e]** Liang, X., Zhang, P., Yan, L., Fu, Y., Peng, F., Qu, L., … & Chen, Z. (2017). LRSSL: predict and interpret drug–disease associations based on data integration using sparse subspace learning. Bioinformatics, 33(8), 1187-1196.

**[1]** Probabilistic Matrix Factorization (using Bayesian Pairwise Ranking) implemented at [this page](https://ethen8181.github.io/machine-learning/recsys/4_bpr.html). 

**[2]** Alternating Least Square Matrix Factorization algorithm implemented at [this page](https://ethen8181.github.io/machine-learning/recsys/2_implicit.html#Implementation). 

**[3]** Collaborative filtering approach *collab_learner* implemented by package [fast.ai](https://docs.fast.ai/collab.html). 

**[4]** Jin Li, Sai Zhang, Tao Liu, Chenxi Ning, Zhuoxuan Zhang and Wei Zhou. Neural inductive matrix completion with graph convolutional networks for miRNA-disease association prediction. Bioinformatics, Volume 36, Issue 8, 15 April 2020, Pages 2538–2546. doi: 10.1093/bioinformatics/btz965. ([implementation](https://github.com/ljatynu/NIMCGCN)).

**[5]** Luo, H., Li, M., Wang, S., Liu, Q., Li, Y., & Wang, J. (2018). Computational drug repositioning using low-rank matrix approximation and randomized algorithms. Bioinformatics, 34(11), 1904-1912. ([download](http://bioinformatics.csu.edu.cn/resources/softs/DrugRepositioning/DRRS/index.html)). 

**[6]** Meng, Y., Jin, M., Tang, X., & Xu, J. (2021). Drug repositioning based on similarity constrained probabilistic matrix factorization: COVID-19 as a case study. Applied soft computing, 103, 107135. ([implementation](https://github.com/luckymengmeng/SCPMF)). 

**[7]** Yang, M., Luo, H., Li, Y., & Wang, J. (2019). Drug repositioning based on bounded nuclear norm regularization. Bioinformatics, 35(14), i455-i463. ([implementation](https://github.com/BioinformaticsCSU/BNNR)). 

**[8]** Liang, X., Zhang, P., Yan, L., Fu, Y., Peng, F., Qu, L., ... & Chen, Z. (2017). LRSSL: predict and interpret drug–disease associations based on data integration using sparse subspace learning. Bioinformatics, 33(8), 1187-1196. ([implementation](https://github.com/LiangXujun/LRSSL)). 

**[9]** Luo, H., Wang, J., Li, M., Luo, J., Peng, X., Wu, F. X., & Pan, Y. (2016). Drug repositioning based on comprehensive similarity measures and bi-random walk algorithm. Bioinformatics, 32(17), 2664-2671. ([implementation](https://github.com/bioinfomaticsCSU/MBiRW)).

**[10]** W.-S. Chin, B.-W. Yuan, M.-Y. Yang, Y. Zhuang, Y.-C. Juan, and C.-J. Lin. LIBMF: A Library for Parallel Matrix Factorization in Shared-memory Systems. JMLR, 2015. ([implementation](https://github.com/cjlin1/libmf)). 

**[11]** Johnson, C. C. (2014). Logistic matrix factorization for implicit feedback data. Advances in Neural Information Processing Systems, 27(78), 1-9. ([implementation](https://github.com/MrChrisJohnson/logistic-mf)).

**[12]** Gao, C. Q., Zhou, Y. K., Xin, X. H., Min, H., & Du, P. F. (2022). DDA-SKF: Predicting Drug–Disease Associations Using Similarity Kernel Fusion. Frontiers in Pharmacology, 12, 784171. ([implementation](https://github.com/GCQ2119216031/DDA-SKF)).

**[13]** Gu, Yaowen, et al. "MilGNet: a multi-instance learning-based heterogeneous graph network for drug repositioning." 2022 IEEE International Conference on Bioinformatics and Biomedicine (BIBM). IEEE, 2022. ([implementation](https://github.com/gu-yaowen/MilGNet)). 