print("SJC23MCA030 : GEORGE SCARIA")

import numpy as np;
X=np.array([[1,2,3],
           [4,5,6],
           [7,8,9]])
X_cube_array=np.multiply(X,np.multiply(X,X))
X_operator=(X*X*X)
X_power=np.power(X,3)
X_cube_doublestar=(X**3)
identity_matrix=np.identity(X.shape[0])
X_power_2=np.power(X,2)
X_power_3=np.power(X,3)
X_power_4=np.power(X,4)
print("Original Matrix")
print(X)
print("Cube Array",X_cube_array)
print("Cube Array using operator",X_operator)
print("Cube Array using power",X_power)
print("Cube Array using doublestar",X_cube_doublestar)
print("Identity matrix of the array")
print(identity_matrix)
print("\nMatrix to different powers")
print("\nX^2",X_power_2)
print("\nX^3",X_power_3)
print("\nX^4",X_power_4)