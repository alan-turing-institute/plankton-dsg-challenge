# Rapid identification of plankton using machine learning - Alan Turing Institute Data Study Group Challenge

## Start here

More information about this challenge is available
[here](https://github.com/alan-turing-institute/plankton-dsg-challenge),
including several Python Jupyter notebooks with some ideas for getting
started.

## Introduction

The Plankton Imager (PI) is a high speed imaging and analysis
instrument that photographs plankton in the size range 100 micron to
20 mm in water.  Each specimen imaged is timestamped, GPS located and
recorded to disk for further analysis.

This dataset comprises 58791 TIF images taken from the PI and split
into two groups: one for training machine learning classifiers
(`train.csv`) and one for testing (`test.csv`). These CSV files
include image names and labels.

The images contain examples of various plankton species. We also
include examples of detritus (sand, seaweed, particulates etc.)

The dataset was assembled by Cefas for use by the Alan Turing
Institute Data Study Group, December 2021.

For more information, and to find the canonical version of this
document, please see
https://github.com/alan-turing-institute/plankton-dsg-challenge

## Ecological background

Zooplankton taxonomy can be confusing due to complex hierarchical
classification, in which organisms are organised into groups or
types. The maximum discernible taxonomic rank (from images or
otherwise) does not infer ecological importance. For example, copepods
account for approx. 70-80 % of the zooplankton and serve as food for
fish larvae and many adult fish and important in the global carbon
cycle. Identifying them to species label (sometimes impossible with
imagery or even visually via microscope) is 'less important' than
classifying all images to copepod. For this reason, we have divided
the data into three idealised labels. Each label is an increase in
taxonomic resolution, although this resolution will vary between
taxonomic groups.

## The challenge

1. Build a classifier that can distinguish between copepods and
   non-copepods in images that do not include detritus.

2. Build a classifier that can distinguish amongst labelled plankton
   in images that do not include detritus.

3. Stretch Goal - Repeat the experiment including detritus images.

Please report the accuracy and precision of your classifiers along
with their computational performance (i.e., how long does your
classifier take to classify 1000 images?).

## Notes

label1 is one of "zooplankton" or "detritus".

label2 is one of "noncopepod", "copepod" or "detritus".

label3 is one of 39 different kinds of specimens or "detritus".

## Licence

These data are copyright Centre for Environment, Fisheries and
Aquaculture Science (CEFAS) and Plankton Analytics Ltd and are
provided for the purposes and duration of the data study group only.

## References

Pitois SG, et al. (2021) A first approach to build and test the
Copepod Mean Size and Total Abundance (CMSTA) ecological indicator
using in-situ size measurements from the Plankton Imager
(PI). Ecological Indicators 123
(2021) 107307. https://doi.org/10.1016/j.ecolind.2020.107307

Pitois SG, et al. (2018). Comparison of a cost-effective integrated
plankton sampling and imaging instrument with traditional systems for
mesozooplankton sampling in the Celtic
Sea. Front. Mar. Sci. 5, 5. https://doi.org/10.3389/fmars.2018.00005

Scott J, et al.  (2021) In situ automated imaging, using the Plankton
Imager, captures temporal variations in mesozooplankton using the
Celtic Sea as a case study. J. Plankton
Research. https://doi.org/10.1093/plankt/fbab018.

https://github.com/mbaityje/plankifier

Schroeder SM, et al. (2018) Low Shot learning of plankton
categories. In GCPR 2018.
https://www.researchgate.net/profile/Simon-Martin-Schroeder/publication/331115929_Low-Shot_Learning_of_Plankton_Categories_40th_German_Conference_GCPR_2018_Stuttgart_Germany_October_9-12_2018_Proceedings/links/5f1180a592851c1eff184607/Low-Shot-Learning-of-Plankton-Categories-40th-German-Conference-GCPR-2018-Stuttgart-Germany-October-9-12-2018-Proceedings.pdf
