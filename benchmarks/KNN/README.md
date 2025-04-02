# K-Nearest Neighbors (KNN) Algorithm
K-Nearest Neighbors (KNN) is a simple yet powerful supervised machine learning algorithm used for classification and regression tasks. It classifies data points based on the majority vote of their nearest neighbors. KNN is non-parametric and instance-based, meaning it does not make assumptions about data distribution and relies on the entire dataset during inference.

## Algorithm
1. Choose the number of neighbors (K).
2. Compute the distance between the test sample and all training samples.
3. Select the K nearest neighbors based on distance.
4. Assign the most common class label (for classification) or compute the average (for regression) from the selected neighbors.
5. Return the predicted class or value.

## Pseudocode
```
Input: Training data, Test data, Number of neighbors (K)
Output: Predicted class/values for test data

For each test sample:
    Compute the distance to all training samples
    Sort training samples by distance
    Select the K nearest neighbors
    Determine the majority class (classification) or compute average (regression)
    Assign the class/value to the test sample
Return predictions
```

## Implementation Approach
- Use Euclidean distance as the metric.
- Store training data as a list of tuples.
- Implement a function to calculate distance.
- Use sorting to find the nearest neighbors.
- Use majority voting for classification.


## Time Complexity
- **Distance computation:** O(n) per test sample
- **Sorting neighbors:** O(n log n)
- **Selecting K nearest neighbors:** O(K)
- **Overall complexity:** O(n log n) per test instance

## Space Complexity
- O(n) for storing distances
- O(K) for storing nearest neighbors
- **Overall space complexity:** O(n)

## References Used for Implementation and Information
1. Cover, T., & Hart, P. (1967). "Nearest neighbor pattern classification." IEEE Transactions on Information Theory.
2. Hastie, T., Tibshirani, R., & Friedman, J. (2009). "The Elements of Statistical Learning." Springer.
3. Wikipedia: K-Nearest Neighbors Algorithm (https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)