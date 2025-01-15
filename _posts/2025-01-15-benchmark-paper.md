---
title: "A large-scale benchmark for collaborative filtering applied to drug repurposing"
date: 2025-01-15T00:00:00-00:00
categories:
  - blog
tags:
  - collaborative filtering
  - drug repurposing
  - benchmark
  - reproducible science
---

2025 starts with another of our papers [[1]](https://hal.science/hal-04626970) being currently in press at *Scientific Reports*!

**Abstract**:  Drug development is known to be a costly and time-consuming process, which is prone to high failure rates. Drug repurposing allows drug discovery by reusing already approved compounds. The outcomes of past clinical trials can be used to predict novel drug-disease associations by leveraging drug- and disease-related similarities. To tackle this classification problem, collaborative filtering with implicit feedback (and potentially additional data on drugs and diseases) has become popular. It can handle large imbalances between negative and positive known associations and known and unknown associations. However, properly evaluating the improvement over the state of the art is challenging, as there is no consensus approach to compare models. We propose a reproducible methodology for comparing collaborative filtering-based drug repurposing. We illustrate this method by comparing 11 models from the literature on eight diverse drug repurposing datasets. Based on this benchmark, we derive guidelines to ensure a fair and comprehensive evaluation of the performance of those models. In particular, an uncontrolled bias on unknown associations might lead to severe data leakage and a misestimation of the model’s true performance. Moreover, in drug repurposing, the ability of a model to extrapolate beyond its training distribution is crucial and should also be assessed. Finally, we identified a subcategory of collaborative filtering that seems efficient and robust to distribution shifts. Benchmarks constitute an essential step towards increased reproducibility and more accessible development of competitive drug repurposing methods. 

We published the code for the benchmark in open-source, available in the following [repository](https://github.com/RECeSS-EU-Project/benchmark-code), and our numerical results can be fully accessed at this [repository](https://github.com/RECeSS-EU-Project/benchmark-results). Should you encounter any issue with those repositories, please use the corresponding tab on GitHub, or simply tell us using our [contact form](https://recess-eu-project.github.io/contact)!

### References

[[1]](https://hal.science/hal-04626970) Réda et al., (2025). Comprehensive evaluation of pure and hybrid collaborative filtering in drug repurposing (in press at Scientific Reports), https://hal.science/hal-04626970
