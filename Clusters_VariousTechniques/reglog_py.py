import numpy as np  # Import NumPy for numerical operations (arrays, vectors, matrices)
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from sklearn.base import BaseEstimator, ClassifierMixin# dla poprawnego dzialania VotingClassifier


class LogisticRegression(BaseEstimator, ClassifierMixin):
    _estimator_type = "classifier"

    def __init__(self, learning_rate=0.01, n_iterations=1000):
        """
        Logistic Regression Classifier (Student Template)

        This class implements binary classification using logistic regression
        trained with gradient descent.

        Parameters:
        - learning_rate: Step size for gradient updates
        - n_iterations: Number of training iterations (epochs)
        """
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y): #train
        """
        Train the logistic regression model.

        Parameters:
        - X: Feature matrix (n_samples, n_features)
        - y: Binary labels (0 or 1)
        """
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)  # Initialize weights
        self.bias = 0  # Initialize bias

        for _ in range(self.n_iterations):
            linear_model = np.dot(X, self.weights) + self.bias  # Linear combination
            y_predicted = self.sigmoid(linear_model)  # Apply sigmoid function

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
      
        return self#do poprawnego dzialania votingClassifier

    def predict(self, X):
        """
        Predict binary class labels.

        Parameters:
        - X: Input data

        Returns:
        - Predicted labels (0 or 1)
        """
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)

        # Convert probabilities to class labels using threshold 0.5
        # y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted]
        # return y_predicted_cls
        return (y_predicted > 0.5).astype(int) #dla ujednolicenia ze sklearn

    def predict_probability(self, X):
        """
        Predict class probabilities.

        Parameters:
        - X: Input data

        Returns:
        - Probabilities in range [0, 1]
        """
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)
        return y_predicted
    
    def predict_proba(self, X):
        """
        Dla dzialania poprawnego VotingClassifier
        """
        probs = self.predict_probability(X)
        return np.c_[1 - probs, probs]

    def sigmoid(self, x):
        """
        Sigmoid activation function.

        Uses clipping to prevent numerical overflow.
        """
        return 1 / (1 + np.exp(-np.clip(x, -250, 250)))

    def accuracy(self, X, y):
        """
        Compute classification accuracy.

        Parameters:
        - X: Input data
        - y: True labels

        Returns:
        - Accuracy (fraction of correct predictions)
        """
        predictions = self.predict(X)
        correct = np.sum(predictions == y)
        total = len(y)
        return correct / total


def main():
    # Generate synthetic dataset
    np.random.seed(0)

    # Create two Gaussian clusters (binary classification)
    X_train = np.vstack([
        np.random.normal(loc=[4, 4], scale=[1, 1], size=(50, 2)),
        np.random.normal(loc=[2, 2], scale=[1, 1], size=(50, 2))
    ])

    # Labels: 1 and 0 (required for logistic regression)
    y_train = np.array([1] * 50 + [0] * 50)

    # Shuffle and split data into training and test sets (80/20)
    indices = np.random.permutation(len(X_train))
    split = int(0.8 * len(X_train))

    X_train, X_test = X_train[indices[:split]], X_train[indices[split:]]
    y_train, y_test = y_train[indices[:split]], y_train[indices[split:]]

    # Train model
    n_iterations = 10000
    logisticregression = LogisticRegression(n_iterations=n_iterations)
    logisticregression.fit(X_train, y_train)

    # Evaluate model
    accuracy = logisticregression.accuracy(X_test, y_test)

    # Plot training data
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title(f'Iterations: {n_iterations}\nAccuracy: {accuracy:.2f}')

    # Create grid for decision boundary visualization
    x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
    y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1

    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, 0.1),
        np.arange(y_min, y_max, 0.1)
    )

    # Predict class for each point in the grid
    Z = np.array(logisticregression.predict(np.c_[xx.ravel(), yy.ravel()]))
    Z = Z.reshape(xx.shape)

    # Plot decision boundary
    plt.contourf(xx, yy, Z, alpha=0.4)

    plt.show()


if __name__ == '__main__':
    main()