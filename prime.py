num = 7
if num%3 != 0 and num%5 != 0:
    print("number is not divisible by both")
elif num%3 == 0 and num%5 ==0:
    print("both divisible")
elif num%3 == 0:
    print("only divisible by three")     
elif num%5 == 0:
    print("only divisible by five") 


num = 141
total = 0
for i in str(num):
    total = total + int(i)
print(total)


num = 12345
rev = 0
for i in range(len(str(num))):
    digit = num % 10
    rev = rev * 10 + digit
    num = num//10
print(rev)  











    



          