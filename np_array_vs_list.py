import numpy as np 
import time 
import sys 

SIZE = 1000000
l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE) 

# python list 
start = time.time()
# result= [print(zip(l1,l2)) for x,y in zip(l1,l2)]

result= [(x+y) for x,y in zip(l1,l2)]
print("python list took:", (time.time() - start) *1000)

# numpy array
start2= time.time()
result = a1+ a2 
print("numpy took:", (time.time() - start2) *1000)