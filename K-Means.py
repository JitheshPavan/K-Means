from matplotlib.pyplot import imshow,scatter,show
from math import sqrt
from numpy import mean,int64
from matplotlib.image import imread

class KMeans:
    # constructor
    def __init__(self, k=3, max_iterations=10):
        self.k = k
        self.max_iterations = max_iterations
        self.i = 0
        self.j = 0
        self.centroids = {}
        self.classes = {}
        self.sum = 0
        self.param = 1.001

    def euclidean_distance(self, point1, point2):
        self.sum = 0
        for w in range(3):
            self.sum += ((point1[w]-self.x[point2[0]][point2[1]][w])**2)
        self.sum += (self.i-point2[0])**2
        self.sum += (self.j-point2[1])**2
        return sqrt(self.sum)

    def fit(self, x):
        self.x=x*self.param
        self.centroids = {}  # (r,g,b,1,1)
        # Initializing Centroid
        for i in range(self.k):
            self.centroids[i] = [i, i]
        for _ in range(self.max_iterations):
            self.classes = {}
            for j in range(self.k):
                self.classes[j] = []
            self.i = 0
            for pt1 in x:
                self.j = 0
                for point in pt1:
                    distances = []
                    for index in self.centroids:
                        distances.append(self.euclidean_distance(point, self.centroids[index]))
                    cluster_index = distances.index(min(distances))
                    self.classes[cluster_index].append([self.i, self.j])
                    self.j = self.j+1
                self.i += 1

            # Defining new Centroids
            for cluster_index in self.classes:
                # averaging Position Coordinates
                self.centroids[cluster_index] = mean(self.classes[cluster_index], axis=0, dtype=int64)




K = 4
# Image Turned into array
X = imread(r"C:\Users\jeeth\Desktop\index.webp")
X1 = X.astype(int)  # float to Int
# Calling The Model
k_means = KMeans(K)
# fit the model
k_means.fit(X1)
# plotting
colors = 10 * ["r", "g", "c", "k"]
imgplot = imshow(X)
for centroid in k_means.centroids:
    color = colors[centroid]
    scatter(k_means.centroids[centroid][1], k_means.centroids[centroid][0], s=130, marker="x")
show()
