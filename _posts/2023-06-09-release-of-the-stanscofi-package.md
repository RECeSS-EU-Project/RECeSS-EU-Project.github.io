---
title: "Release of the *stanscofi* package"
date: 2023-06-09T00:00:00-00:00
categories:
  - blog
tags:
  - Python
  - collaborative filtering
  - drug repurposing
  - open science
  - reproducibility
---

We introduce our Python package *stanscofi* for the development of collaborative filtering-based drug repurposing algorithms!

We have highlighted in our [introductory blog post]({{ site.base_url }}/blog/launch-of-the-recess-website/) how drug repurposing might be able to overcome several issues in drug development. In prior works [[1]](https://doi.org/10.1186/s13321-020-00450-7);[[2]](https://doi.org/10.1016/j.eswa.2017.05.004);[[3]](https://doi.org/10.1093/bib/bbab581), this approach has been implemented through collaborative filtering. 

Collaborative filtering is a flexible semi-supervised approach which has raised a lot of interest in the domain of recommender systems, more particularly for online advertising of items to users [[4]](https://dl.acm.org/doi/abs/10.1145/3341161). This framework has become popular in drug repurposing, considering drugs as items and diseases as users [[5]](https://doi.org/10.1186/s12859-019-2983-2);[[6]](https://doi.org/10.1186/s12859-019-3288-1);[[7]](https://doi.org/10.1093/bioinformatics/btz331). It leverages known drug-disease matchings in order to recommend new ones. Predicted drug-disease associations stem from a function whose parameters are learnt on a whole matrix of drug-disease matchings, instead of focusing on a single disease at a time. In particular, literature often relies on *tensor decomposition*, *i*.*e*., any drug-disease matching in the matrix is the output of a classifier in which only lower-rank tensors intervene, *e*.*g*., factorization machines (FMs) [[8]](https://doi.org/10.1609/aaai.v33i01.3301750). Recent works [[9]](https://doi.org/10.1186/s12859-020-03898-4);[[10]](https://doi.org/10.1109/TCBB.2022.3212051) have reported near-perfect predicting power (area under the curve, AUC) on several repurposing datasets (*c*.*f*., a previous [blog post](https://recess-eu-project.github.io/blog/publication-of-new-drug-repurposing-datasets/))

However, several problems remain untackled on that topic. In particular, there is currently no standard pipeline to train, to validate and to benchmark collaborative filtering-based repurposing methods. This considerably limits the impact of this research field, in terms of estimating the technological improvement over the state-of-the-art, and of science reproducibility and reusability.

This is why we have worked on the development of an open-source Python package called *stanscofi* (available at the following [GitHub repository](https://github.com/RECeSS-EU-Project/stanscofi/)), which allows to easily import existing drug repurposing datasets, to visualize them, to run any classification approach on them and to quantify and observe its performance. The main performance metric is the Area Under the Curve (AUC) averaged across all diseases, which allows to have a better idea about the actual performance of a method. Moreover, this package also tackles the issue of splitting a dataset into *weakly correlated* training and validation sets in a rather computationally tractable way. This is crucial in order to avoid *data leakage*, which is the source of a major reproducibility crisis in machine learning [[11]](https://doi.org/10.48550/arXiv.2207.07048). 

**stanscofi** is hosted on [PyPI](https://pypi.org/project/stanscofi/) and on [Anaconda](https://anaconda.org/recess/stanscofi/) repositories. In order to have an overview of the package, please have a look (and test!) at the [introductory notebook](https://github.com/RECeSS-EU-Project/stanscofi/blob/master/docs/Introduction%20to%20stanscofi.ipynb). Feel free to report issues or to make suggestions on the [GitHub issue flagging page](https://github.com/RECeSS-EU-Project/stanscofi/issues) or using our [contact form](https://recess-eu-project.github.io/contact/)!

The next steps in the development of this package is to implement state-of-the-art algorithms and run the benchmarks on the drug repurposing datasets shown in the [drug repurposing dataset blog post](https://recess-eu-project.github.io/blog/publication-of-new-drug-repurposing-datasets/).

### References

[[1]](https://doi.org/10.1186/s13321-020-00450-7) Jarada, Tamer N., Jon G. Rokne, and Reda Alhajj. "A review of computational drug repositioning: strategies, approaches, opportunities, challenges, and directions." Journal of cheminformatics 12.1 (2020): 1-23.

[[2]](https://doi.org/10.1016/j.eswa.2017.05.004) Zhang, Jia, et al. "Computational drug repositioning using collaborative filtering via multi-source fusion." Expert Systems with Applications 84 (2017): 281-289.

[[3]](https://doi.org/10.1093/bib/bbab581) Meng, Yajie, et al. "A weighted bilinear neural collaborative filtering approach for drug repositioning." Briefings in bioinformatics 23.2 (2022): bbab581.

[[4]](https://dl.acm.org/doi/abs/10.1145/3341161) Margaris et al. In Proceedings of the 2019 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (2019), 1160.

[[5]](https://doi.org/10.1186/s12859-019-2983-2) Yang, Xinxing, et al. "Additional neural matrix factorization model for computational drug repositioning." BMC bioinformatics 20 (2019): 1-11.

[[6]](https://doi.org/10.1186/s12859-019-3288-1) Liu, Hui, et al. "Predicting effective drug combinations using gradient tree boosting based on features extracted from drug-protein heterogeneous network." BMC bioinformatics 20.1 (2019): 1-12.

[[7]](https://doi.org/10.1093/bioinformatics/btz331) Yang, Mengyun, et al. "Drug repositioning based on bounded nuclear norm regularization." Bioinformatics 35.14 (2019): i455-i463.

[[8]](https://doi.org/10.1609/aaai.v33i01.3301750) Vie, Jill-Jênn, and Hisashi Kashima. "Knowledge tracing machines: Factorization machines for knowledge tracing." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 33. No. 01. 2019.

[[9]](https://doi.org/10.1186/s12859-020-03898-4) He, Jieyue, Xinxing Yang, and Zhuo Gong. "Hybrid attentional memory network for computational drug repositioning." BMC bioinformatics 21.1 (2020): 1-17.

[[10]](https://doi.org/10.1109/TCBB.2022.3212051) Yang, Xinxing, Genke Yang, and Jian Chu. "The Computational Drug Repositioning without Negative Sampling." IEEE/ACM Transactions on Computational Biology and Bioinformatics (2022).

[[11]](https://doi.org/10.48550/arXiv.2207.07048) Kapoor, Sayash, and Arvind Narayanan. "Leakage and the reproducibility crisis in ML-based science." arXiv preprint arXiv:2207.07048 (2022).