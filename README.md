# Customer Segmentation
This repository contains a personal project on customer segmentation using hierarchical clustering and k-means clustering techniques with an added API implementation for customer segment prediction. The project aims to understand the customer behavior and divide them into different segments based on their characteristics and behaviors. The data used in this project is a supermarket demographic customer's data and also purchase data. 

## Usage
The project is implemented in Python and uses the [Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) and [Scipy](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html) library for the clustering algorithms and [FastAPI](https://fastapi.tiangolo.com/) for the API implementation.

There are 3 notebooks in this repo. Ideal order for reading: `customer_segmentation.ipynb` -> `customer_purchase_EDA.ipynb` -> `customer_purchase_model.ipynb`

Notebook | Description | Colab
------------- | ------------- | -------------
`customer_segmentation.ipynb` | Starting notebook of this project, using demographic customer's data. Contains EDA and Clustering (Hierarchical, KMeans), and also Dimensionality Reduction.| [![open-in-colab]](https://colab.research.google.com/drive/1l--D_f1aAzmpU1I00LxOAzF88_OQLO6S?usp=sharing)
`customer_purchase_EDA.ipynb` | Exploratory Data Analysis for customer's purchase data | [![open-in-colab]](https://colab.research.google.com/drive/1oEaHjtk48u-ahsZIpRYavTX73o0agnkQ?usp=sharing)
`customer_purchase_model.ipynb` | Price elasticity modelling of customer's purchase data | [![open-in-colab]](https://colab.research.google.com/drive/1nsuCeMIomKpIUDmj8pXAm01GoqYkBNCd?usp=sharing)


[open-in-colab]: https://colab.research.google.com/assets/colab-badge.svg
