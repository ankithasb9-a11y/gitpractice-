# function 
# def greet():
#     print("hello")
# greet()  


# types of function
# built in function
# a = (10,20,30,40)
# print(len(a))
# print(max(a))
# print(min(a))
# print(type(a))
# print(sum(a))
# print(input(a))


# user defined function
# def add():
#     a = 10
#     b = 20
#     print(a+b)
# add()    

# four types of user defined function
# without arguments and without return values
def add():
    a = 10
    b = 20
    print(a+b)
add()    

# with arguments and without return values
def add(a,b):
    print(a+b)
add(10,30)   

# without arguments and with return values
def add():
    a = 20
    b = 30
    return a+b
result = add()
print(result)  

# with arguments and with return values
def add(a,b):
    return a+b
result = add(30,40)
print(result)      

