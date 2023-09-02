import numpy as np 
a = np.arange(12).reshape(3,4)
print(a)

print("====================")
print("print the individual row")
for row in a:
    print("print the individual cell")
    for cell in row:
        print(f"cell {cell},  is from row {row}")
        
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("get all array element in a list")
for cell in a.flatten():
    print(f"cell {cell} is got from {a.flatten()}")
    
print("*****************")
print("get cell using nditer")
for x in np.nditer(a, order = 'C'):
    print(x)

#A , K
print("print in fourth order dim")
for x in np.nditer(a,order='F'):
    print(x)

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

print("use the order to create a list")
for x in np.nditer(a, order='F', flags=['external_loop']):
    print(x)

print("*********************")

for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = x*x

print("a is", a)
    
b = np.arange(3,15,4).reshape(3,1)
# .reshape(3,1)
print(f"b is {b}")

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for x,y in np.nditer([a,b]):
    print(x,y)
