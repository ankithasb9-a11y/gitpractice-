#s = "hello"
#print(s.upper())
#print(s.lower())
#print(s.capitalize())
#print(s.replace("hello","hi"))
#print(s.title())
#print(s.find('l'))


#name = "Ankitha"
#age =25
#print(f"my name is {name} and my age is {age}")


#nane = "Ankitha"
#age =25
#print("my name is {} and my age is {}".format(name,age))


#name = "Ankitha"
#age = 25
#print("my name is %s and my age is %d"%(name,age))



# name = "pcleaython"
# print(name[0:6:2])
# print(name[1:6:3])
# pwd = input("Enter the password\n")

# if len(pwd) < 8:
#     print("Password should contain at least 8 characters")
# elif not any(ch.isdigit() for ch in pwd):
#     print("Password should contain at least one digit")
# elif not any(ch.isupper() for ch in pwd):
#     print("Password should contain at least one uppercase letter")
# else:
#     print("Strong password")





# Cafe menu: 1 Tea ₹20, 2 Coffee ₹30, 3 Juice ₹50. Ask for the choice and quantity, 
# and print the bill. Invalid choice should print a message.

# choice = input("enter your choice\n")
# quantity = int(input("enter the quantity\n"))
# if choice == "tea":
#     bill = quantity*20
#     print(bill)
# elif choice == "coffee":
#     bill = quantity*30
#     print(bill)
# elif choice == "juice":
#     bill = quantity*50
#     print(bill)
# else:
#     print("invalid choice")

# print("1. Tea - ₹20")
# print("2. Coffee - ₹30")
# print("3. Juice - ₹50")

# choice = int(input("Enter your choice: "))

# if choice != 1,2,3:
#     print("invalid choice")
# quantity = int(input("Enter quantity: "))
# if choice == 1:
#     total = 20 * quantity
#     print("Item: Tea")
#     print("Total bill: ₹", total)

# elif choice == 2:
#     total = 30 * quantity
#     print("Item: Coffee")
#     print("Total bill: ₹", total)

# elif choice == 3:
#     total = 50 * quantity
#     print("Item: Juice")
#     print("Total bill: ₹", total)




# Month name to season using match-case, and again using elif.

# season = input("enter the season")

# match season:
#     case "rainny":
#         print("june - july")
#     case "hot":
#         print("march - april")
#     case "spring":
#         print("jan - feb")
#     case "winter":
#         print("nov - dec")



# Parking: weekday rate ₹20 per hour, weekend ₹30. Over 5 hours, take 10% off the total.

# day = input("enter the day")
# hour = int(input("enter the hour"))

# if day == "weekday":
#     rate = hour*20
#     print(rate)
#     if hour > 5:
#         discount = 10
#         print(rate - (rate*discount/100))
# elif day == "weekend":
#     rate = hour*30
#     print(rate)
#     if hour > 5:
#         discount = 10
#         print(rate - (rate*discount/100))


# Library: a member can borrow if the fine is ₹0 and fewer than 5 books are issued.
#  Print the specific reason if not.

# member = True

# if member:
#     print("fee is zero and only 5 books are issued")
# if not member:
#     print("fee need to be payed")


# # Streaming plan: Basic ₹199 (1 screen), Standard ₹499 (2 screens), Premium ₹649 (4 screens). 
# # Print the cheapest plan that supports the screens entered.

# plan = input("enter your plan")
# if plan == "Basic":
#     print("199 need to be payed offers 1 screen")
# elif plan == "standard":
#     print("499 need to be payed offers 2 screens")
# elif plan == "Premium":
#     print("649 need to be payed offers 4 screens")


# # File upload: accept only .jpg or .png, and reject files of 5 MB or more.

# file = "pdf"
# size = "4mb"
# if file == (".jpg" or ".png") and size < "5mb":
#     print("file upload accepted")
# else:
#     print("rejected")


# Order three numbers (descending) using conditions only.

# order1 = int(input("enter the order numbers"))
# order2 = int(input("enter the order numbers"))
# order3 = int(input("enter the order numbers"))
# if order1>order2 and order1>order3:
#     if order2>order3:
#         print(order1,order2,order3)
#     else :
#         print(order1,order3,order2)
# if order2>order1 and order2>order3:
#     if order1>order3:
#         print(order2,order1,order3)
#     else :
#         print(order2,order3,order1)
# if order3>order2 and order3>order1:
#     if order1>order2:
#         print(order3,order1,order2)
#     else :
#         print(order3,order2,order1)


# Elevator: a user can enter if the weight is at most 700 kg and the person count is at most 8. 
# Print which limit failed.

# weight = int(input("enter the weight"))
# count = int(input("enter the count of person"))

# if weight <= 700 and count <= 8:
#     print("you can use elevator")
# else:
#     print("limit failed")


# # Time zone check: the office is open Monday to Friday, 9 to 18 (end exclusive). 
# # Print Open or Closed given a day name and an hour.

# days = input("enter the day")
# hours = int(input("enter the hour"))
# if days in ("monday","tuesday","wednesday","thursday","friday","saturday","sunday") and 9 <= hours <= 18:
#     print("open")
# else:
#     print("closed")


# for i in range(1,11):
#     print(f"7*{i}={7*i}")


# for i , ch in enumerate([4,5,6,7,7]):
#     print(i,ch)


# n, fact = 5, 1
# for i in range(1, n + 1):
#     fact *= i
#     print(fact) 

l =[1,2,3,5]
largest = second = l[0]
for i in l:
    if i>largest:
        second = largest
        largest = i
    elif i>second and i!=largest:
        second = i
print(largest,second)
# n=7
# count = 0
# for i in range(1,n+1):
#     if n%i==0:
#        count += 1
# if count == 2:
#         print("prime")
# else:
#         print("not prime")


# pos=neg=zero =0
# for i in [1,-9,0,7,-8,0,0]:
#     if i>0:
#         pos += 1
#     elif i<0:
#         neg += 1
#     elif i == 0:
#         zero += 1
# print(pos,neg,zero)

# a,b=0,1
# for _ in range(8):
#     print(a,end="")
#     a,b=b,a+b
