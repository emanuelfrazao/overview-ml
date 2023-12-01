# Machine Learning overview

Small overview of machine learning concepts covered

This README.md file contains an overview, then the notebooks contain some code examples and explanations.

## What is Machine Learning?

What do people mean with _a machine that learns_?
- **an algorithm** (_e.g._ learning regression) learns from **experience** `E` (_e.g._ consumes data),
    - with respect to **a task** `T` (_e.g._ estimating house prices), 
    - and **a performance measure** `P` (_e.g._ mean absolute error), 
- if its performance on `T`, as measured by `P`, improves with experience `E` (!)

There are 4 most relevant components in any machine learning project:
1. **Task** - what do we want to achieve?
2. **Performance measure** - how do we measure success?
3. **Algorithms** (Models) – what do we learn?
4. **Experiences** (Data) – how does the model learn?

### tasks and performance measures

1. Supervised tasks
    - **Classification**
        - Performance measures: accuracy, precision, recall, F1, ...
    - **Regression**
        - Performance measures: MAE, MSE, RMSE, RMSLE, ...
    - **Sequence generation**
        - Performance measures: accuracy, BLEU, ...
    - **Structured Output** (e.g. bounding boxes, segmentation masks, etc.)
        - Performance measures: depends a lot on the task
2. Unsupervised tasks
    - **Dimensionality reduction**
        - Principal Component Analysis
            - Principal Components are the directions of maximum variance
        - Auto-encoder
    - **Clustering**
        - K-means
    - **Denoising**
        - Auto-encoders
    - **Anomaly detection**
    - ...

### models covered

1. **L. Regression**
2. **Support Vector Machines**
3. **Decision Trees**
    - **Random Forests**
    - **Gradient Boosting**
4. **K-Nearest Neighbors**
5. **Naive Bayes**
6. **Neural Networks**s

### data

What types of data?
- tabular (features are usually unstructured)
- time series
- images
- text
- audio
- video
- geospacial
- genomic data (DNA sequences)

Where to get the data?
- online (scrape, web-API, downloads)
- offline (files, databases, ...)

How to treat the data?
0. Data collection, wrangling, description
1. Data cleaning
    - missing/corrupted values
    - outliers
    - if data is textual:
        - remove punctuation
        - remove stop words
        - stemming
        - lemmatization
        - ...
2. Feature engineering:
    - log-transformations, polynomial features
    - binning
    - dimensionality reduction (e.g. PCA)
    - feature selection
        - permutation importance
    - ...s
3. Preprocessing (for models)
    - scaling
        - standard – such that mean is 0, std 1
        - min-max – such that min is 0, max 1
        - robust – such that median is 0, IQR 1
    - encoding
        - one-hot encoding
        - ordinal
        - embedding






## ML workflow





## Organizing a project


1. create a virtual environment

```bash
pyenv virtualenv 3.10.6 detech  # create a virtual environment
pyenv local detech              # set the virtual environment as local
```

1. environment para o projecto
2. repo
    1. README.md
    2. requirements.txt
    3. .gitignore
    4. raw_data/
        - not shared
    5. notebooks/
        - labeled by person
    6. src/
        - source code
    7. pyproject.toml
        - ficheiro de configuração de um package de python


