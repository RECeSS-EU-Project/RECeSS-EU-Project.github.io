---
title: "JELI: an interpretable classifier"
date: 2025-01-14T00:00:00-00:00
categories:
  - blog
tags:
  - collaborative filtering
  - drug repurposing
  - interpretability
  - knowledge graph
  - embedding learning
---

The second chapter of the RECeSS project aims at providing interpretable classification (into positive and negative associations) of drug-disease pairs. We are proud to announce that the related paper [[1]](https://hal.science/hal-04625183/) is currently in press at *BMC Bioinformatics*!

**Abstract**: *Background:* Interpretability is a topical question in recommender systems, especially in healthcare applications. An interpretable classifier quantifies the importance of each input feature for the predicted item-user association in a non-ambiguous fashion. *Results:* We introduce the novel Joint Embedding Learning-classifier for improved Interpretability (JELI). By combining the training of a structured collaborative-filtering classifier and an embedding learning task, JELI predicts new user-item associations based on jointly learned item and user embeddings while providing feature-wise importance scores. Therefore, JELI flexibly allows the introduction of priors on the connections between users, items, and features. In particular, JELI simultaneously (a) learns feature, item, and user embeddings; (b) predicts new item-user associations; (c) provides importance scores for each feature. Moreover, JELI instantiates a generic approach to training recommender systems by encoding generic graph-regularization constraints. *Conclusions:* First, we show that the joint training approach yields a gain in the predictive power of the downstream classifier. Second, JELI can recover feature- association dependencies. Finally, JELI induces a restriction in the number of parameters compared to baselines in synthetic and drug-repurposing data sets. 

We published the related methodological package [*jeli*](https://github.com/recess-eu-project/JELI) in open-source. You can also download it in [PyPI](https://pypi.org/project/jeli/). Should you encounter any issue with using those packages, please use the corresponding tab on GitHub, or simply tell us using our [contact form](https://recess-eu-project.github.io/contact)!

We will soon publish a short blog post that highlights the main results of the paper. Stay tuned!

### References

[[1]](https://hal.science/hal-04625183/) Réda et al., (2024). Joint Embedding-Classifier Learning for Interpretable Collaborative Filtering (in press at BMC Bioinformatics), https://hal.science/hal-04625183/
