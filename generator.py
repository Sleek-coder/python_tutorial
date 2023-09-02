def fib():
    a, b = 0,1 
    while True:
        yield a 
        a,b = b, a+b
    
# fb_func = fib()
# print(fb_func)
# print(next(fb_func))
# print(next(fb_func))
# print(next(fb_func))
# print(next(fb_func))
# print(next(fb_func))
# print(next(fb_func))
for i in fib():
    if i > 100:
        break
    print(i)