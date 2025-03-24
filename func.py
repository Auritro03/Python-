
# def func(*args, **kwargs):
#     print (args, kwargs)
    
# func('Tros', 'Ver', key1='Ori', key2= 'Se')

# # map

# list = [1, 2, 3, 4, 5]

# newL= set(map(lambda x : x*x*x*x, list))
# snewl = sorted(newL)
# print(snewl)

# filter function 

# def func(x):
#     return x % 2 == 0

# l = [1,2,3,4,5,6,7,8,9,10]

# newl = list(filter(func, l))
# print(newl)

# # reduce function
# from functools import reduce  

# li = [1,2,3,4,5,6,7,8,9,10]

# newl = reduce(lambda x, y : x+y, li)
# print (newl)

#higher order function

# def func(x):
#    print(x.__name__)
#    x()

# def Ami_Auritro():
#     print("Ami manush hoite chai")

# def Tumi():
#     print("tomake manush banaite chai")

# # func(Ami_Auritro)
# # func(Tumi)

# ki = [-2, -1,2,3,4]

# newl= set(filter(lambda x : x%2== 1, ki))
# print(newl)

#wrapper 

def mywrapper(n):
    def ori ():
        n()
        print("I am the wrapper")
        
    return ori
@mywrapper
def greet():
    print("I am the greet")
def hell():
    print("I am the hell")

hell()
greet()