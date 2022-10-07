import pandas as pd
import pickle

# Load model
scaler  = pickle.load(open('./model/scaler.pickle', 'rb'))
pca  = pickle.load(open('./model/pca.pickle', 'rb'))
kmeans  = pickle.load(open('./model/kmeans_pca.pickle', 'rb'))

# Cluster map
cluster_map = {
    '0': 'average/standard',
    '1': 'career-focused',
    '2': 'fewer-opportunity',
    '3': 'well-off'
}

# Predict function
def Clustering(x):
    
    """Predict cluster from request"""

    scaled = scaler.transform(x)
    pcad = pca.transform(scaled)
    cluster = str(kmeans.predict(pcad)[0])
    label = cluster_map[cluster]

    
    result = {'cluster':[cluster, label]}

    return result