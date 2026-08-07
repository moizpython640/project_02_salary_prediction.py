from sklearn.linear_model import LinearRegression
import numpy
import numpy as np
x = np.array ([[1000], [1200], [ 1500], [1800], [2000]]) 
y = np.array ([[150000], [180000], [220000], [260000], [300000]])
model = LinearRegression()
model.fit (x, y)
prediction = model.predict ([[2200]])
print(prediction)


