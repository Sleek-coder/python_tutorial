basket={"orange","apple","mango","apple","orange"}
print(f" basket, {basket} is {type(basket)}")

a= set()
a.add(1)
print(f" an element 1 was just added to a, {a}")
a.add(2)
print(f"a is {a}")
# an empty braces bracket is a dict 
number = [1,2,3,4,2,3,4,5]
set_my= set(number)
print(f"set_my: {set_my}") 
set_my.add(6)
print(f"s new set_my:{set_my}")

print("================================================================")
frozen_set_my = frozenset(set_my)
print(f"frozen_set_my:{frozen_set_my}")
print(f"not allowed to add to a rfrozen set")
# frozen_set.add(7)

print("apple" in basket)
print("g" in basket)

for x in basket:
    print(f"x: {x}")
    
y= {"a","g","h"}
x= {"b","c","a"}

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("merge or union a set")
print(f"joint of set is {x|y}")

print("get intersect of set")
print(f"intersect is {x&y}")
print("get difference of two sets")
print(f"differenc:{x-y}")
print(f"x and y do not have same content {x==y}")
print(f" is x a subset of y: ({x<y})")
x={"g","h"}
print(f" is x now a subset of y:{x<y}")