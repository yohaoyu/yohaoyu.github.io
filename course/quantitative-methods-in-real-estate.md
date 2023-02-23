---
layout: course
title: Quantitative Methods in Real Estate
subtitle: Real Estate 506A, Autumn Quarter 2023, University of Washington
---

##### Overview

Provides an overview of different data collection methods, basic statistical techniques and their appropriate application based on the size and type of various real estate and socioeconomic dataset. Students determine the appropriate method based on specific objectives and critically assess their findings.



##### Course Schedule

<table> 
    <tr> 
        <td><b>Date</b></td> 
        <td><b>Topic</b></td> 
        <td><b>Reading</b></td> 
        <td><b>Notes</b></td> 
        <td><b>Assignments</b></td> 
    </tr> 
    <tr> 
        <td>10/01</td> 
        <td>Why statistics? <br/>Course introduction <br/>Real estate data</td> 
        <td>Applied Quantitative Analysis for Real Estate, Chapter 1,2 </td> 
        <td> </td> 
        <td>HW 1 release</td> 
    </tr> 
</table>


```r
library(knitr)
opts_chunk$set(message=FALSE, collapse=TRUE,fig.align='center',tidy=TRUE, tidy.opts=list(blank=TRUE, width.cutoff=70,strip.white=TRUE), warning=FALSE,cache=FALSE)
```

## Scottish lip cancer data

In these notes we will analyze the famous Scottish lip cancer data discussed in lectures. We will fit both non-spatial and spatial random effects smoothing models.

We will also discuss some other topics including how to deal with *missing observations*, and *censored observations*.

INLA library: [INLA DOWNLOAD](https://www.r-inla.org/download-install) 

```{r, eval=T} 
library(SpatialEpi)
library(RColorBrewer)
library(ggplot2)
library(ggridges)
library(INLA)
library(sf)
```

In area $i$, let $$Y_i$$ and $E_i$ represent the disease count and expected count.An initial summary is the Standardized Morbidity Ratio (SMR), which for area $i$ is
for $i=1,\dots,56$. We also have an area-based covariate $X_i$ (proportion in agriculture, fishing and farming) in each areas. The following is taken from Section 6.2 of Moraga (2020).

We form a data frame ``scotdata`` containing key variables, and add the SMRs.