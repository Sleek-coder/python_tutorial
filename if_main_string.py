def calculate_area(base,height):
    print(f"__name__ is", __name__)
    return 1/2 * (base*height)

# used as entrypoint  for  your python program : similarly in c and java
if __name__== "__main__":
    print("I am in area.py")
    a = calculate_area(10,20)
    print("area: ", a)
    
    print(__name__)