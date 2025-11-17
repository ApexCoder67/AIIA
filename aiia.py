# # Data Preprocessing Template

# # Importing the libraries
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd

# # Importing the dataset
# dataset = pd.read_csv('Data.csv')
# X = dataset.iloc[:, :-1].values
# y = dataset.iloc[:, -1].values

# # Splitting the dataset into the Training set and Test set
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# for x , y , z in X_train:
#     print(x , y , z)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#taking the input
df = pd.read_csv("Data.csv")

#seperating into dependant and independent variables
X = df.iloc[: , :-1 ]
y = df.iloc[: , -1]

#seperating categorical data into seperate columns , to avoid having some kind of relation
#so creating yes no for each option
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder' , OneHotEncoder() , [0])] , remainder = 'passthrough')
X = np.array(ct.fit_transform(X))


#for binary encoding of data
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

print(y)



#splitting the data
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.5 , random_state = 0)



#for scaling using normalization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[ : , 3 :] = sc.fit_transform(X_train[ : , 3 : ])



#Classification

# #decision tree
# from sklearn.tree import DecisionTreeClassifier
# model = DecisionTreeClassifier(criterion='entropy', random_state=0)

# # random forest
# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=100, random_state=0)

# #svm
# from sklearn.svm import SVC
# model = SVC(kernel='linear')

# # naive bayes
# from sklearn.naive_bayes import GaussianNB
# model = GaussianNB()

# #knn
# from sklearn.neighbors import KNeighborsClassifier
# model = KNeighborsClassifier(n_neighbors=5)


# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)

# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred))
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))



#Clustering

# from sklearn.cluster import KMeans
# model = KMeans(n_clusters=3, random_state=0)

# from sklearn.cluster import DBSCAN
# model = DBSCAN(eps=0.5, min_samples=5)

# from sklearn.cluster import AgglomerativeClustering
# model = AgglomerativeClustering(n_clusters=3, linkage='ward')

# from sklearn.mixture import GaussianMixture
# model = GaussianMixture(n_components=3, random_state=0) # use y = model.predict(X)


# model.fit(X) 
# y = model.labels_ # model.predict(X)
# plt.scatter(X[:,0], X[:,1], c=y)
# plt.title("KMeans Clustering")
# plt.xlabel("Feature 1")
# plt.ylabel("Feature 2")
# plt.show()


# #regression
# # Model (change only these 2 lines) - > LinearRegression , LogisticRegression , Ridge , Lasso
# from sklearn.linear_model import Lasso
# model = Lasso()

# # Train
# model.fit(X_train, y_train)

# # Predict
# y_pred = model.predict(X_test)

# # Evaluation
# from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
# print("R2 Score:", r2_score(y_test, y_pred))
# print("MSE:", mean_squared_error(y_test, y_pred))
# print("MAE:", mean_absolute_error(y_test, y_pred))


# from statsmodels.tsa.arima.model import ARIMA
# model = ARIMA(y, order=(2, 1, 2))   # p, d, q

# # Train
# model_fit = model.fit()

# # Predict / Forecast
# y_pred = model_fit.forecast(steps=10)

# # Evaluation (optional for time series)
# print(y_pred)

# # Plot
# plt.plot(y, label="Original")
# plt.plot(y_pred, label="ARIMA Forecast")
# plt.legend()
# plt.show()

# from statsmodels.tsa.statespace.sarimax import SARIMAX
# model = SARIMAX(y,
#                 order=(1, 1, 1),
#                 seasonal_order=(1, 1, 1, 12))   # P, D, Q, s

# # Train
# model_fit = model.fit()

# # Predict / Forecast
# y_pred = model_fit.get_forecast(steps=12).predicted_mean

# # Evaluation (optional)
# print(y_pred)

# # Plot
# plt.plot(y, label="Original")
# plt.plot(y_pred, label="SARIMA Forecast")
# plt.legend()
# plt.show()
