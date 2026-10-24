# Type 1: No arg, No return
def greet():
    print("Hello LPU")

# Type 2: With arg, With return - Most Used
def add(a,b):
    return a+b

# Type 3: Default argument - Asked in TCS
def power(a, b=2): # b default 2
    return a**b
print(power(5)) # 25
print(power(5,3)) # 125

# Type 4: *args, **kwargs - Infosys asks
def show(*args, **kwargs):
    print(args) # tuple (1,2,3)
    print(kwargs) # dict {'name':'joy'}
show(1,2,3, name="joy")