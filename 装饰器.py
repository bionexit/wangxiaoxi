import time

def display_time(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print(t2 - t1)
        return result
    return wrapper


def is_prime(num):
    if num < 2:
        return False
    elif num ==2:
        return True
    else:
        for i in range (2,num):
            if num % i == 0:
                return False
        return True

@display_time
def count_prime_nums(maxnum):
    count = 0
    for i in range (2, 10000):
        if is_prime(i):
            # print(i)
            count = count + 1
    return count
    
count = count_prime_nums(10000)
print('result:',count)


def arg_fun(sex):
    def func1(func):
        def func2():
            if sex == 'man':
                print('func1 man')
            if sex == 'woman':
                print('func1 woman')
            return func()
        return func2
    return func1


@arg_fun(sex='man')
def man():
    print('man')

@arg_fun(sex='woman')
def woman():
    print('woman')
    
man()


def func1(func):
    def func2(x,y):
        print(x,y)
        x += 5
        y += 15
        return func(x,y)
    return func2

@func1
def mysum(a,b):
    print(a+b)

mysum(1,2)