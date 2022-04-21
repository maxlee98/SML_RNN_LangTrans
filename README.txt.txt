# Overview
Repository containing content related to Recurrent Neural Networks (RNN) and its applications. Two applications created using R that are covered in this repository are Prediction of a Sine Wave and Language Translation.

# Libraries Required

## Sine Wave Prediction
library(dplyr)
library(tidyverse)

## Language Translation 
library(keras)  
library(tensorflow)  
library(tokenizers)  
library(dplyr)     
library(reticulate)     
library(ramify)     
library(stringr)     
library(deepviz)   


# How to run the program:

## Sine Wave Prediction
1. Download the `.rmd` file  
2. Ensure all libraries required are installed
3. Run all chunks of the code. (May take some time to complete all Epochs, to reduce number of Epochs edit Line 67)
4. Observe the differences between a predicted Sine Wave curve via RNN and the actual Sine wave curve.


## Language Translation
1. Download the `.rmd` file and the `.Rproj` file.
2. Ensure that all libraries required are installed.
3. Run all chunks for the `.rmd` file. Reducing waiting time by reducing number of epochs at Line 304. **Reducing number of epochs may result in reduced accuracy**
4. Observe the differences between actual translation and predicted translation.

>Accuracy for Language Translation depends on the Dataset used as well.



# References
Week 10 slides from 50.038: Computational Data Science by Prof. Soujanya Poria 

Poorly Translated French to English image:[My French Life™ - Ma Vie Française®](https://www.myfrenchlife.org/2012/07/17/french-literature-sans-translation/) 

The deep learning-simple problem image: [Reddit](https://www.reddit.com/r/datascience/comments/ael5rz/dont_be_this_guy_xpost_from_rprogrammerhumor/?utm_source=share&utm_medium=web2x&context=3) 

Sine wave example: [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2019/01/fundamentals-deep-learning-recurrent-neural-networks-scratch-python/) 

[Mathcha to create tikz diagrams](https://www.mathcha.io/) \\
[Tracey, T. (29 August, 2018). Language Translation with RNNs](https://towardsdatascience.com/language-translation-with-rnns-d84d43b40571) 

[Adrian, G.(22 June, 2018). A review of Dropout as applied to RNNs](https://adriangcoder.medium.com/a-review-of-dropout-as-applied-to-rnns-72e79ecd5b7b#:~:text=RNN's\%20differ\%20from\%20feed\%2Dforward,their\%20memory\%2C\%20hindering\%20their\%20performance.) 

[Niklas Donges (29 July, 2021) A Guide to RNN: Understanding Recurrent Neural Networks and LSTM Networks](https://builtin.com/data-science/recurrent-neural-networks-and-lstm) 