def foo():
    print("starting...")
    res = 3
    while res>0:
        yield res
        print("res:",res)
        res = res - 1
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print("*"*30)
print(next(g))
print("*"*40)
print(next(g))
print("*"*20)