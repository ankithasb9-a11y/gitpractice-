#right angle triangle
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()   

#inverted triangle
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()   

#square pattern
for i in range(5):
    for j in range(5):
        print("*",end="")
    print() 

# pyramid patterns
for i in range(1,6):
    print(" " * (5-i) + "*" * (2*i-1))

# alphabet pattern
for i in range(1,6):
    for j in range(i):
         print(chr(65+j),end="")
    print() 


# 9:0 pattern
for i in range(1,6):
    for j in range(i):
         print((i+j)%2,end="")
    print() 


# hallow square pattern
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
         print("*" , end=" ")
        else: 
         print(" " , end=" ") 
    print()


# reverse a string
S = "python"
rev = ""
for i in S:
    rev = i + rev
print(rev)  

s = "python"
rev = ""
i = len(s) - 1
while i >= 0:
    rev =  rev + s[i]
    i = i - 1
print(rev)  


# reverse a number
num = 12345
rev = 0
for i in range(len(str(num))):
    digit = num % 10
    rev = rev * 10 + digit
    num = num//10
print(rev) 


num = 12345
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num//10
print(rev) 


# armstrong number
num = 153
temp = num
total = 0
while num>0:
    digit = num % 10
    total = total + digit**3
    num = num//10
if temp == total:
    print("Armstrong Number")
else:
    print("Not Armstrong Number ")         



    








