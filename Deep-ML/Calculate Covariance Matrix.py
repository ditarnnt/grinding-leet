'''
Write a Python function that calculates the covariance matrix from a list of vectors. Assume that the input list represents a dataset where each vector is a feature, and vectors are of equal length.

Example:
        input: vectors = [[1, 2, 3], [4, 5, 6]]
        output: [[1.0, 1.0], [1.0, 1.0]]
        reasoning: The dataset has two features with three observations each. The covariance between each pair of features (including covariance with itself) is calculated and returned as a 2x2 matrix.
'''

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
  n_features = len(vectors)
  n_observation = len(vectors[0])
  
  convariance_matrix = [] 
  for _ in range (n_features):
    row = []
    for _ in range (n_features):
      row.append(0)
    convariance_matrix.append(row) 
  
  means = [] 
  
  for feature in vectors:
    feature_sum = sum(feature)
    feature_mean = feature_sum / n_observation
    means.append(feature_mean) 
  
  for i in range (n_features):
    for j in range(i, n_features):
      covariance = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(n_observation)) / (n_observation - 1)
      convariance_matrix[i][j] = convariance_matrix[j][i] = covariance

  return convariance_matrix