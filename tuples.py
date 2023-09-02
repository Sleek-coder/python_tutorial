my_tuple = ("apple","orange","banana")
print(f"my tuple is:{my_tuple} with its lengthe:{len(my_tuple)}")

print(f"one item tuple {('sam',)}  of string type must have ,i.e: {type('sam',)}")

print(f"tuple with int: {(1,2,3)} is {type((1,2,3))}")
print(f" tuple with  boolean: {(True,)} of type:{type((True,))}")
print("----------------------------------------------------------------")

heter_tup= (1,2,3,True,'apple')
print(f"tuple is heterogenous: {heter_tup} of type:{type((1,2,3,True,'apple'))}")

print("the tuple constructor")
print(f"tuple:{tuple((1,2,3))} with type: {type(tuple((1,2,3)))}")
print("----------------------------------------------------------------")
x= tuple((1,2,3,4,5,6,7))
print(f" acess tuple by index: tuple element at index 2 is: {x[2]}")
print(f"access tuple by negative idx: {x[-1]}")
print(f"access tuple with range {x[3:5]} or {x[:4]} or {x[2:]} ")

print("##############")

print(f"update tuple: by convert to list first")
list_x= list(x)
# list_x[-1] =15
# print(f"x.update and x: becomes{tuple(list_x)}")

print("ORR append to list")
list_x.append(15)
print(f"tuple: {tuple(list_x)}")

print("to add without conversion to list")
x +=(8,)
print(f"tuple updated with summation symbol: {x}")

print("----------------------------------------------------------------")
print("unpack tuple")
small_x= list_x[:4]
print(f"small_x: {small_x}")
print(f" small_x list unpack: ")
one,two,three,four = small_x
print(f"upacked: {one},  {two}, {three},{four}")

print("loop ")
for i in x:
    print(f"element x in the tuple is {x}")
    
print("loop through:")
for i in range(len(x)):
    print(f" tuple element at indexes {x}  is: {x[i]}")
    
print("join multiple tuples:")
print("####################")
print(f"joint tuples are: {my_tuple + x}")

print("count method on tuples:")
ele= 1
a_count= x.count(ele)
print(f"a_count of {ele} specified element in the tuple", a_count)

print("------------------------------------------------")
print(f"find index of {ele} in x")
x.index(1)
print(f"idx of {ele} in {x} is {x.index(ele)}")
