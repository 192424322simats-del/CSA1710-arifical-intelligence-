import numpy as np
from sklearn.neural_network import MLPClassifier

# Input data
# [Study Hours, Attendance]
X = np.array([
    [1, 60],
    [2, 65],
    [3, 70],
    [4, 75],
    [5, 80],
    [6, 85]
])

# Output
# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 1, 1, 1])

# Create Feed Forward Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    solver='lbfgs',
    max_iter=1000,
    random_state=1
)

# Train the network
model.fit(X, y)

# Test input
test_data = np.array([[5, 82]])

# Prediction
prediction = model.predict(test_data)

if prediction[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")
