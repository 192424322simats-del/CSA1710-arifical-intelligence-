from sklearn.tree import DecisionTreeClassifier

# Training data
# [Study Hours, Attendance]
X = [
    [1, 60],
    [2, 65],
    [3, 70],
    [4, 75],
    [5, 80],
    [6, 85]
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

# Create Decision Tree
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# Test data
study_hours = 4
attendance = 78

prediction = model.predict(
    [[study_hours, attendance]]
)

if prediction[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")
