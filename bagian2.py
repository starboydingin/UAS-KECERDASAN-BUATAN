import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('student-scores.csv')

X = data[['math_score', 'history_score', 'physics_score', 'chemistry_score',
          'biology_score', 'english_score', 'geography_score']]
y = data['career_aspiration']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("Accuracy:", knn.score(X_test, y_test))
