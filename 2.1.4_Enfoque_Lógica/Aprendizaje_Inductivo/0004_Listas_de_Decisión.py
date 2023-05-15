import numpy as np
from collections import Counter

class KDNode:
    def __init__(self, data, left, right, split_dim, split_val):
        self.data = data
        self.left = left
        self.right = right
        self.split_dim = split_dim
        self.split_val = split_val

class KDecisionTree:
    def __init__(self, k=2):
        self.k = k

    def build_tree(self, data):
        if not data:
            return None

        n, m = data.shape

        # Split along dimension with the largest variance
        variances = np.var(data, axis=0)
        split_dim = np.argmax(variances)
        split_val = np.median(data[:, split_dim])
        left_mask = data[:, split_dim] < split_val
        right_mask = data[:, split_dim] >= split_val

        # Recursively build left and right subtrees
        left_data = data[left_mask, :]
        right_data = data[right_mask, :]
        left_subtree = self.build_tree(left_data)
        right_subtree = self.build_tree(right_data)

        return KDNode(data, left_subtree, right_subtree, split_dim, split_val)

    def predict(self, root, point):
        if not root:
            return None

        if root.left is None and root.right is None:
            return Counter(root.data[:, -1]).most_common(1)[0][0]

        if point[root.split_dim] < root.split_val:
            return self.predict(root.left, point)
        else:
            return self.predict(root.right, point)
