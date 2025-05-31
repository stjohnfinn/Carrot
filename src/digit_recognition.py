class KMeans:
  def __init__(self, k=10, max_iter=100):
    self.k = k
    self.max_iter = max_iter
    self.centroids = None
    self.labels = None

  def fit(self, X):
    # initialize cluster centers randomly within the data space
    pass

  def classify(self, x):
    # check which cluster center is closest to x
    pass
