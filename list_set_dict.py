numbers = [1,2,3,4,5,6,7]
even = []

for i in numbers:
    if i%2 ==0:
        even.append(i)
        
print(f"even is:{even}")

print("================================================")
print("its equivalenbt")

even = [x for x in  numbers if x%2 ==0]    
print(f"even from list comp: {even}")

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
square_of_num = [x*x for x in numbers]
print(f"square of num is: {square_of_num}")

print("SET")
s = set(numbers)
print(f'set is: {s}')

print("using list comp on set")

even_set = {i for i in s if i%2==0}
print(f"your even set is: {even_set}")

print("DICT forming ")
cities = ["mumbai", "new york" , "paris"];
countries = ["india","usa","france"]

print("using zip to zip two list: it creates tuples")
z = zip(cities,countries)
for a in z:
    print(f"cities and respective countries are {a}")
# approach2
d = {city:country for city, country  in zip(cities, countries)} 
print(f" formed  dict is : {d}")
