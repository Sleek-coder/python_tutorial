item1="bread"
item2="pasta"
item3="fruits"
items=["bread","pasta","fruit","veggies"]
print(f"items[0], {items[0]}")
print(f"items[3], {items[3]}")
print("******")
print(f"items[0:3] are {items[0:3]}")
items.insert(1,"butter")
print(f"items.insert to any position in the list  are{items}")
items.append("fish")
print(f"items append to the end of list: are {items}")
print(f"lengthe of list is {len(items)})")

food_list  = ["bread","pasta","fruit","veggies"]

random_list = ["shampoo","hair cream"]
print(f"concatenated items were {food_list + random_list}")

#NB
# print(f"wrong add item {food_list + 'chicken'}")
print(f"'bread' in {items}")
random_list = ["shampoo","hair cream"]
random_list[1] = "comb"
new_list= random_list
print(f"new_list  with a chnaged list item is {new_list}")

print(f"remove functiion on list")
print(f'----------------')
new_list.remove('comb')
print(f"remove specific item {new_list}")
random_list.pop(0)
print(f"remove specified index {random_list}")

# print(f"delete list")
# del new_list
# print(f"{new_list}")

print(f"-------")
print(f"clear list")
food_list.clear()
print(f" print {food_list}")

print(f"--------------------------------")

print(f"loop through a list")
for x in items:
    print(f" item,x is {x}")
print(f"--------------------------------")

print(f"loop through the index number")
for i in range(len(items)):
    print(f" i is looped by indexes: {i} the element in those idx are {items[i]}")

print("looping with list comprehension")
iterator = [x for x in items]
print(f"iterator element is the element in list comprehension is  {iterator}")

print(f"************")
print(f"loop with list comp with index")
iterator = [print(x) for x in range(len(items))]
print(f"iterator is an index for this list comprehension")
#NB A list comprehension can only work with an iterable object i.e list, range

print(f"list comprehension with if statement")
iterator= [print(x) for x in items if "a" in x]

print(f"ORRRRRRRRRRRRRR")
print(f"this list comp prints the index by iter range of the if control  statement ")
iterator = [print(x) for x in range(len(items)) if "a" in items[x]]

print(f" if statement varies")
iterator  = [print(x) for x in range(len(items)) if x < len(items)/3]


print(f" set value in the new list to upper or lower ")
items2 = [x.upper() for x in items]
print(f"nel list in uppercase {items2}")
print(f"!!!!!!!!!!!!!!!")
items3 = [x.lower() for x in items2]
print(f"derived list back in lowercase {items3}")

print(f"********************************")
print("forming a list of specific item")

iterator= ['ope' for x in range(len(items))]
print(f" iterator {iterator}")
print(f" forming boss")
print(f"*****")

iterator = ['ope' for x in items]
print(f"iterator :{iterator}")

print(f" replacing a list itme with conditionals ")
iterator = [x if x != "bread" else "orange" for x in items]

print(f" {iterator}")

print(f"method2")
new_l= [x  if x !="butter" else "avocado pear" for x in items]
print(f"new_l:{new_l}")

print(f"sort list: a sorted list  is acted upon the original list variable  ")
new_l.sort()
print(f"items.sort is {new_l}")

print(f" copy a list: A copied list is stored in a new variable")
copy_list = new_l.copy()
print(f"copied list is {copy_list}")

print(f" copy with the list() method")
copy_list = list(new_l)
print(f"copy with the list method: {copy_list}")

print("***copy by equating")
copy_list = new_l
print(f"copy by equating: { copy_list}")

print(f"join list by : concatenation, .extend() and .append()")
print(f"---------------")
lista= ["a"]
listb=["b"]
listc=["c"]
list_all = lista +listb+listc
print(f"list_all :{list_all}")
print("########## append behind #########")
mini_list= ["A","B","C"]

list_all.append(mini_list)
print(f" list_all new multi element is appended as a group :{list_all}")
mini_list= ["A","B","C"]
list_all.extend(mini_list)

print(f"list_all new elements are added as single entitity with A using .extend() : {list_all}")

print("****************")
print("list.reverse tutorial")
list_all.reverse()
print(f"list_reverse also works similar to sort, the changes is effected on the original variable: {list_all}")

print("*******count list element*********")
list_all.extend(["A","A","A"])
countA= list_all.count("A")
print(f"countA:{countA} ")

