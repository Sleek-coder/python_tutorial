import numpy as np 
n = np.array([2,3,4])
print(n[0:2])
print("==========")
print("also supports python list")
n2 = [2,3,4]
print(n2[0:2])
print("n last index is:",  n[-1])
print("****************************************************************")
print("multidim array")
a = np.array([[1,2,3],[4,5,6], [6,7,8]])
print("element at specific range of index  r by specific column of the index of the number in a", a[0:2,2])
print(a[2,2], "element in row of idx 2 and coolumn of index 2")
print(a[-1],"last row all columns")
print(a[-1, 0:2], "get idx 0 and 1 o fthe last row")
print(a[:, 1:3], "all rows but last two columns")
print("range works as range: it never reaches the last number!!1")

for row in a:
    print(row ,"row is")
print("================================================================")
for cell in a.flat:
    print("cell", cell)
        
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print("stack two arrays together")
b= np.array([[6,7,8],[4,5,6],[1,2,3]])
c =np.vstack((a,b))
print(f"c is stack: {np.vstack((a,b))}")
print(f" hstack: {np.hstack((a,b))}")

print("================================================")
print("forming arrays using np version of range")
v = np.arange(30).reshape(2,15)
print(f"v : {v}")

result = np.hsplit(v,3)
print(f"result is: {result}")
print(result[0])
result2= np.vsplit(v,2)
print(f"result2:{result2} with the first element-array:{result2[0]}")

f= np.arange(12).reshape(3,4)
k = f>4
print(f"k: {k} and f[k] is {f[k]}")
f[k] = -1
print(f"f is :{f}")