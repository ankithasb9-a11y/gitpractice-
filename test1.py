# You are developing an online event registration system. A user can enter only if they are 18 or older and have a valid ID.

# age = 17
# valid_id = 1234
# id = 1234
# if age>= 18 and id == valid_id:
#     print("A user is allowd")
# else:
#     print("user is not allowed")

# order, prime, blocked = 450, True, True
# if (order >= 500 or prime) and blocked:
#     print("Free delivery")
# else:
#     print("Delivery charges apply")



# verified, banned, admin = True, True, False
# if (verified and banned) or admin:
#     print("Can post")
# else:
#     print("Cannot post")



# username = input("enter user name\n")
# password = input("enter password\n")



# if username != "admin":
#     print("wrong username")
# elif password != "admin123":
#     print("wrong password")
# else:
#     print("valid user")


# age = int(input("enter your age:\n"))

# if age <= 0:
#     print("invalid age")
# elif age < 5:
#     print("free")
# elif 5<= age <= 12:
#     print("pay 100")
# elif 13 <= age <= 59:
#     print("pay 200")
# elif age>= 60:
#     print("pay 120")

# Free above ₹1,000. ₹50 for ₹500 to ₹1,000. ₹100 below ₹500.

# price = 10
# if price >= 1000:
#     print("free")
# elif 500 <= price <= 1000:
#     print("pay 50")
# elif price < 500:
#     print("pay 100")


# registered, paid, exam_open = True, True, False
# if registered:
#     if paid:
#         if exam_open:
#             print("Start exam")
#         else:
#             print("Exam not open yet")
#     else:
#         print("Pay the fee first")
# else:
#     print("Register first")

# Coupon SAVE10 gives 10% off only on orders above ₹1,000. Coupon FREESHIP removes shipping. 
# Any other code is invalid.

coupon = input("enter the coupon")
order = int(input("enter you order price"))

 if coupon == "SAVE10" and order > 1000:
    print("gives 10% off")
elif coupon == "FREESHIP":
    print("Remove shipping")
else:
    print("invalid code")

