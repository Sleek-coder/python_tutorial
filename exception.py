x = input("Enter number1: ")
y = input("Enter number2:")
try:
    z = int(x) /int(y)
except Exception as e:
    print('Exception type is:',  type(e).__name__)
    z = None
print("Division is:", z)

