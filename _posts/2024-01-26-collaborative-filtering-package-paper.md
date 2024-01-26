---
title: "We released our first paper!"
date: 2023-09-14T00:00:00-00:00
categories:
  - blog
tags:
  - Python
  - collaborative filtering
  - drug repurposing
  - open science
  - reproducibility
---

We are glad to announce that our first (tool) paper has been accepted at *Journal of Open Source Software* [![JOSS](https://joss.theoj.org/papers/10.21105/joss.05973/status.svg)](https://doi.org/10.21105/joss.05973)!

**Abstract**: Drug development is still a time-consuming and costly process as of today, while the failure rate in the successful commercialization of drug candidates is high. Drug repurposing is an approach which screens currently available chemical compounds and tool molecules to uncover novel therapeutic indications. In particular, collaborative filtering has sparked interest, as this framework allows us to deal with implicit information on drug-disease associations. As popular as drug repurposing might be, the lack of standard training, validation pipelines and benchmark datasets hinders the development and assessment of drug repurposing methods. To overcome this issue, we propose the Python package **stanscofi** (*STANdard for drug Screening in COllaborative FIltering*), which permits the quick implementation of ready-to-go drug repurposing models and ensures proper training and validation of the methods. We also built the Python package **benchscofi** (*BENCHmark for drug Screening in COllaborative FIltering*) upon **stanscofi** to implement several algorithms from the state-of-the-art and enable the first large-scale benchmark of the field.

We have been making sure of satisfying the criteria for reproducible and well-documented *open-source* packages, which is a marker of the future livelihood of [stanscofi]({{ url }}blog/release-of-the-stanscofi-package/) and [benchscofi]({{ url }}/blog/release-of-the-benchscofi-package/). Those tools also offer access to the two drug repurposing [datasets]({{ url }}/blog/publication-of-new-drug-repurposing-datasets/) that we have previously released. Note that contributions are welcome to both packages, by pushing merge requests to the corresponding GitHub repositories. Please make sure to have a look at the README files before doing so! Should you encounter any issue with using those packages, please use the corresponding tab on GitHub, or simply tell us using our [contact form]({{ url }}/contact)!

The first chapter of the RECeSS project (out of three) now finally closes, and we are very excited for the next one! Spoiler alert: we will be dealing with interpretability this time. Stay tuned!

### References

[[1]](https://joss.theoj.org/papers/10.21105/joss.05973#) Réda et al., (2024). stanscofi and benchscofi: a new standard for drug repurposing by collaborative filtering. Journal of Open Source Software, 9(93), 5973, https://doi.org/10.21105/joss.05973
