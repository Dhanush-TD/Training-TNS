# K-Means Clustering
from sklearn.cluster import KMeans

data = [
    [500, 2],
    [600, 3],
    [550, 2],
    [5000, 15],
    [4500, 12],
    [4800, 14],
    [1000, 5],
    [1200, 6],
    [1100, 5]
]

model = KMeans(n_clusters=3, random_state=42)

model.fit(data)

print(model.labels_)


# Elbow method
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = [
    [500, 2], [600, 3], [550, 2],
    [5000, 15], [4500, 12], [4800, 14],
    [1000, 5], [1200, 6], [1100, 5]
]

inertia_values = []
k_range = range(1, 7)

for k in k_range:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(data)
    inertia_values.append(model.inertia_)

for k, inertia in zip(k_range, inertia_values):
    print(f"k = {k} | Inertia = {inertia:,.2f}")

plt.figure(figsize=(6, 4))
plt.plot(k_range, inertia_values, marker='o')
plt.title("Elbow Method For Optimal k")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia (WCSS)")
plt.grid(True)
plt.show()


# Hierarchical Clustering
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

data = [
    [90, 85],
    [88, 90],
    [60, 65],
    [58, 62],
    [55, 60],
    [30, 40],
    [35, 38]
]

model = AgglomerativeClustering(n_clusters=3)

labels = model.fit_predict(data)

print(labels)

linkage_matrix = sch.linkage(data, method='ward')
sch.dendrogram(linkage_matrix)
plt.title("Dendrogram")
plt.show()


# PCA - Dimensionality Reduction
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = [[90, 85, 95, 15], [88, 90, 90, 14], [45, 40, 60, 5], [50, 52, 65, 6]]

scaled = StandardScaler().fit_transform(data)

reduced = PCA(n_components=2).fit_transform(scaled)

print(reduced)


# t-SNE (t-Distributed Stochastic Neighbor Embedding)
import numpy as np
from sklearn.manifold import TSNE

data = np.array([
    [1, 2, 3, 4],
    [1, 2, 3, 5],
    [10, 11, 12, 13],
    [10, 11, 12, 14],
    [20, 21, 22, 23],
    [20, 21, 22, 24]
])

model = TSNE(n_components=2, perplexity=2, random_state=42)

result = model.fit_transform(data)

print(result)