myset = {'apple','banana','orange'}
print(f"my_set is: {myset}, type : {type(myset)}")

set_sample_no_duplicate_true_and_1 = {True, 1}
print(f"set_sample_no_duplicate True and 1 is{set_sample_no_duplicate_true_and_1}")

print("----------------------------------------------------------------")
print("access set value  using loop only")

iterator= [print(x) if x != 'orange' else 'apple' for x in myset ]
# items=["bread","pasta","fruit","veggies"]

# iterator = [print(x) if x != "bread" else "orange" for x in items]

print("loop with forloop")
for  x in myset:
    print(f"x from myset for loop",x)
print(f"banana" in myset)
print("----------------------------------------------------------------")
print("add to set with add() method")
myset.add("avocado")
print(f"myset is: {myset}")
print("*********")
print(f" add elements from one set to another using update function")
myset.update(x)
print(f"mysset is updated:{myset}")
print("----------------------------------------------------------------")
myset.remove("a")
print(f"myset is now updated{myset}")

print("method 2 is:")
myset.discard("r")
print(f"myset is now:{myset}")

print("method 3: removes random element from random indx")
myset.pop()
print(f"myset is now:{myset}")

# print("emptying the set")
# # myset.clear()
# # print(f"myset is {myset}")

# print("----------------------------------------------------------------")
# print("delete the set completely")
# # del myset

# print(f"does myset still exist? {myset}")

print("----------------------------------------------------------------")
print("looop through a set ")
for x in myset:
    print(f"x in myset is {x}")
    
print("----------------------------------------------------------------")
print("join a set")
print("method1: union of the set")
set1={"cherry","mango","orange"}
set3 = set1.union(myset)
print(f"union of x and myset is:{set3}")

print("method2: update() method to insert one set into another")
set4= {"fish","chicken","kpomo"}
set5= set4.update(set3)
print(f"updated new set using the update method:{set5}")

print("----------------------------------------------------------------")
print("keep intersection: by modifying the original set")
set6 = {"banana"}
set3.intersection_update(set6)

print(f"intersection of set5 with set4 is {set3}")

print("----------------------------------------------------------------")
print("keep intersection by forming a new set")
set7 = set3.intersection(set6)
print(f"intersection method:{set7} ")
print("----------------------------------------------------------------")
print("prints the elements  not present jointly in both")
set3.symmetric_difference_update(set6)

print(f"set6 now contains the difference between set3 and set6:{set3}")

print("to form a new set with the symmetric difference")
set8 = set7.symmetric_difference(set6)
print(f" symmetric as a new value is {set8}")