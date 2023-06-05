import random
import numpy as np

class KMeans:
    def __init__(self,k=2,max_iter=100):
        self.k = k
        self.max_iter = max_iter
        self.centroids = None

    def fit_predict(self,X):
        random_index = random.sample(range,X.shape[0], self.k)
        self.cetriods = X[random_index]

        for i in range(self.max_iter):
            cluster_group = self.assign_clusters(X)
            old_centroids = self.centroids
            self.centroids = self.update_centroids(X,cluster_group)

            if np.all(old_centroids == self.centroids):
                break
        return cluster_group


    def update_centroids(self,X,cluster_group):
        new_centriods = []
        k_cluster  = np.unique(cluster_group)

        for type in k_cluster:
            new_centriods.append(np.mean(X[cluster_group == type],axis=0))


    def assign_clusters(self,X):
        cluster_group = []
        distances = []

        for row in X:
            for centroid in self.centroids:
                distances.append(np.sqrt(np.sum((row - centroid)**2)))
            min_distance = min(distances)
            cluster_group.append(distances.index(min_distance))
            distances.clear()
        return np.array(cluster_group)

