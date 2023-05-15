import math
from collections import Counter

class DecisionNode:
    def __init__(self, feature=None, threshold=None, results=None, left_child=None, right_child=None):
        self.feature = feature
        self.threshold = threshold
        self.results = results
        self.left_child = left_child
        self.right_child = right_child
        
class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
    
    def fit(self, X, y):
        self.tree = self._build_tree(X, y)
    
    def predict(self, X):
        return [self._predict(sample, self.tree) for sample in X]
    
    def _build_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        
        # If all samples belong to the same class, create a leaf node
        if len(set(y)) == 1:
            return DecisionNode(results=Counter(y))
        
        # If there are no features left or maximum depth is reached, create a leaf node with the most common class
        if n_features == 0 or depth == self.max_depth:
            return DecisionNode(results=Counter(y))
        
        # Find the best feature to split on based on information gain
        best_feature, best_threshold = self._get_best_split(X, y)
        
        # Split the data based on the best feature and threshold
        left_indices = X[:, best_feature] <= best_threshold
        right_indices = X[:, best_feature] > best_threshold
        left_child = self._build_tree(X[left_indices], y[left_indices], depth+1)
        right_child = self._build_tree(X[right_indices], y[right_indices], depth+1)
        
        # Create a decision node with the best feature and threshold, and its left and right children
        return DecisionNode(feature=best_feature, threshold=best_threshold, left_child=left_child, right_child=right_child)
    
    def _get_best_split(self, X, y):
        n_samples, n_features = X.shape
        
        # Calculate the entropy of the whole dataset
        entropy = self._calculate_entropy(y)
        
        # Initialize variables for storing the best feature and threshold, and the highest information gain
        best_feature, best_threshold, highest_info_gain = None, None, -1
        
        # Iterate over each feature and each value in that feature to find the best split
        for feature in range(n_features):
            feature_values = X[:, feature]
            unique_values = set(feature_values)
            for threshold in unique_values:
                left_indices = feature_values <= threshold
                right_indices = feature_values > threshold
                
                # Skip if there is no split for these indices
                if sum(left_indices) == 0 or sum(right_indices) == 0:
                    continue
                
                # Calculate the information gain for this split
                info_gain = self._calculate_information_gain(y, left_indices, right_indices, entropy)
                
                # Update the best feature, threshold, and information gain if this split is better
                if info_gain > highest_info_gain:
                    best_feature = feature
                    best_threshold = threshold
                    highest_info_gain = info_gain
        
        return best_feature, best_threshold
    
    def _calculate_entropy(self, y):
        n_samples = len(y)
        _, counts = zip(*Counter(y).items())
        probabilities = [count / n_samples for count in counts]
        return -sum([p * math.log2(p) for p in probabilities])
    
