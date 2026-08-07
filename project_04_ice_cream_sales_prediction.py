from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array ([[ 20], [ 25], [30], [ 35], [ 40]])
y = np.array ([[100], [ 150], [ 220], [300],
 [ 380]])
model = LinearRegression()
model.fit (x, y)
prediction = model.predict ( [[45] ] )
print(prediction)

