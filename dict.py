d = {"tom":791591554,"rob": 791591774,"bom":791591560}
print(d)
print(f"to access tom is:{d['tom']}")

print("********")
print(F"add new number ")
d["sam"]= 791591557
print(f"updated d is {d}")
print(f"to del sam")

del d["sam"]

print(f"updated d is:{d}")

for key in d :
    print(f"key is{key}, value is : {d[key]}")
    
print(f" ORR")

for k,v in d.items():
    print(f"key is{k}, valueis: {v}")
    
print("tom" in d)
print("----------------------------------------------------------------")
print(f"dict lenght of items: {len(d)} ")
d['unknowns'] = [791591234, 791591634, 791591356]

print(f"updated d is: {d}")
print(f"its data type is: {type(d)}")

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(f"using dict contructor to amke a dict")
d_D= dict(apple=2, orange=4,mango=5) 
print(f"new_dict is {d_D}")

print("---------")
print("get value of a key using .get()")
print(f"{d_D.get('apple')}")

print("get a list of all available  keys in the dict")
print(f"{d_D.keys()}")
print("it also stores change automatically")
d_D['avocado'] = 5
d_keys = d_D.keys()
print(f"d_keys are:{d_keys}")
print("--------")

print("get the values of dict as list")
print(f"{d_D.values()}")
print("^^^^^")
print("get both the keys and values of your dict as items of tuples")
print(f"the dict items are:{d_D.items()}")

print("*****************")

print("asserting the existence  of a key")
if 'apple' in d_D:
    print("yes! apple exist!") 

print("------------")
print("update value in dict")
d_D['apple']=7
print(f" updated val of apple:{d_D}")

print("------------")
d_D.update({"orange":6})

print("adding items")
print("----------------")
print("pop a dict")
print(d_D.pop("orange"))
print(f"the updated dict is:{d_D}")

print("####################")
print("popitem method")
print(f"{d_D.popitem()}")
print(f" updated dict is:{d_D}")
# del d_D
print(f"d_D:{d_D}")
# d_D.clear()
# print(f"d_D is cleared of all its elements :{d_D}")

print("--------------------------------")
print("loop through dict with list comprehension")
iterator = [print(x) for x in d]
print("ORRR")
print("--------------------------------")

for x in d:
    print(x)
print("to print the values within")
iterator = [print(d[x]) for x in d]

print("Orrrrr")
iterator = [print(x) for x in d.values()]
print("--------------------------------")
print(" to print the keys instead")
iterator = [print(x) for x in d.keys()]
print("to loop both key and values pair")

iterator = [print(f" key:{key},value: {value}") for key,value in d.items()]

print("----------------------------------------------------------------")
# dict copying
d_copy = d.copy()
print(f" a copy of the dict using copy methodis :  {d_copy}")
print("method 2: using the dict () method ")
d_copy2= dict(d)
print(f" a copy of dict using  the dict() method:{d_copy2}")

print("----------------------------------------------------------------")
print("nested dict tutorial")

fruits={
    'apple':8,
    'orange':3,
    'avocado':1,
    'water melon':1
    
}
cereals={
    'rice flour':3,
    'soyabeans': 2,
    'maize flour': 3,
    'quaker oats':4
}
fats={
    'groundnutoils':2,
    'palmoil': 1,
    'palmkerneloil':3,
}
food={
    "fruits":fruits,
    "cereals":cereals,
    "fats":fats,
}

print(f" my nested dict is: {food}")
print("####################")
print("how to access item in nested dict")
print(f"food['fruits']['apple']:  {food['fruits']['apple']}")

print("####################")
print("fromkeys; used to form multiple dict with same valuees")
x= ['key1','key2','key3']
y=3
d_reformed= dict.fromkeys(x,y)
print(f" dict formed from fromkeys: {d_reformed}")   
# x= ['key1','key2','key3']
# y=[1,2,3]
# for i in y:
#     d_reformed= dict.fromkeys(x,i)
#     print(f" dict formed from fromkeys: {d_reformed}")   

print("----------")

print("setdefault example: sets a default key value")
fruits.setdefault('banana',1)
print(f"the modified fruits value is :{fruits}")
