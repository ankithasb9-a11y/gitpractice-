# words = ["madam", "python", "level", "hello"]

# for i in words:
#     if i == i[::-1]:
#         print(f"{i} is a palindrome")
#     else:
#         print(f"{i} is not a palindrome")


# user_name = input("enter the username\n")
# password = input("enter the password\n")

# if user_name != "admin" and password != "strong":
#     print("invalid credentials")
# elif user_name != "admin":
#     print("wrong username")
# elif password != "strong":
#     print("wrong password")
# elif user_name == "admin" and password == "strong":
#     print("login is successful")


# def greet():
#     return "hii"
# # greet()
# # out = greet()
# print(greet)

# def square_print(number):
#     return number * number      
# square_print(2)
# result = square_print(4) * 2
# print(result)                   


# def add(name):
#     print(f"hello {name} ")
# print(add("nikitha"))

# def even(n1,n2):
#     if n1%2==0 and n2%2==0:
#         return "both even"
#     elif n1%2!=0 and n2%2!=0:
#         return "both odd"
    
# print(even(4,9))


# def check_prime(n):
   
# print(check_prime(7))


# Create a list of numbers from 1 to 20.
# Create a list of squares from 1 to 15.

# l = [number for number in range(1,21)]
# print(l)
# l1 = [number**2 for number in range(1,16)]
# print(l1)

# Extract all even numbers from a list.
# Extract all odd numbers from a list.
# l = [number for number in range(1,11) if number%2 ==0]
# print(l)

# Convert all strings in a list to uppercase.
# Extract words whose length is greater than 5.

# l = ["word","madam","long","least"]
# rev = []
# for i in l:
#     rev.append(i.upper())
# print(rev)

# l1 = [123,345,567]

# for i in l1:
#     str_data = str(i)
#     sum = 0
#     for ch in str_data:
#         sum+=int(ch)
#     print(sum)


# Create a list containing the length of each word.

# l = ["word","madam","long","least"]
# l1 = []
# for i in l:
#     l1.append(len(i))
# print(l1)


# numbers = [10, -5, 20, -8, 30, -2]
# l= [num if num > 0 else 0 for num in numbers]
# print(l)


# numbers = [10, 15, 20, 30, 45, 50, 60, 75]
# l = [num for num in numbers if num%3==0 and num%5==0 ]
# print(l)

# Create a list of numbers divisible by 2 or 7 between 1 and 100.

# Extract vowels from a string.

# l = [num for num in range(1,101) if num%2==0 or num%7 ==0]
# print(l)

# s = "education"
# for i in s:
#     if i in "aeiou":
#         print(i)
# l = [s for s in "education" if s in "aeiou"]
# print(l)

# Multiplication table as a nested list

# n = int(input("enter the number"))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count+=1
# if count == 2:
#     print("prime")
# else:
#     print("not prime")

number = 5832
sum = 0
for i in str(number):
    sum += int(i)
print(sum)

