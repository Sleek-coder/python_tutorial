indian=["samosa","daal","naan"]

chinese=["egg role","pot sticker","fried rice"]

italian=["pizza","pasta","risotto"]

dish=input("Enter a dish name: ")

if dish in indian:
    print("Dish is indian")
elif dish in italian:
    print("Dish is  Italian")
elif dish  in chinese:
    print("Dish is Chinese")
else:
    print("Dish is unknown")