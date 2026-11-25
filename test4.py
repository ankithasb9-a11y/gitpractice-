# marks = int(input("enter the marks\n"))

# if marks <= 0:
#     print("invalid marks")
# elif marks> 100:
#     print("enter valid marks")
# elif marks >= 90:
#     print("grade A+")
# elif marks >= 80:
#     print("garde A")
# elif marks >= 70:
#     print("grade B+")
# elif marks >= 60:
#     print("grade B")
# elif marks >= 35:
#     print("pass")
# else:
#     print("fail")



pwd = input("enter the password\n")
if len(pwd) < 8:
    print("Password should contain at least 8 characters")
elif not any(ch.isdigit() for ch in pwd):
    print("Password should contain at least one digit")
elif not any(ch.isupper() for ch in pwd):
    print("Password should contain at least one uppercase letter")
else:
    print("strong password")