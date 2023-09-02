x="sally was a male engineer"
print(f" x with split is a list of word  is {x.split(',' )}", end = " ")

x= "sally was a male engineer"

print(f"x with split as a character {list(x)}",end="")

print("OR")

print(f"x with split as character approach2 is {[*x]}", end="")

print(f"------")
print(f" x with split as character approach3 is{[y for y in x]}")

# # NB: List on a list does not change the datatype
# print("********************************")
# print(f"x  with split as a character {list(x.split(','))}")
x,y,z =2,3,4

print(f"{x} \n {y} \n {z}")

print("OR")
print(f'''{x} {y} {z}''')
f= "sally"; k="Olu"
print(f"f+k is {f+k}")

print("indexing string")

print(f"f index 0 to 3 {f[0:3]}")