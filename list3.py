 numbers = [10,15,20,25,30,35,40,45]
 even_list = numbers[::2]
 odd_list = numbers[1::2]
 print(numbers)
 print(even_list)
 print(odd_list)

factorial of a number
num = 5
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("Factorial:",fact) 

count the vowels
s = "python programming"
count = 0
for ch in s:
    if ch in "aeiou":
        count+=1
print("vowel count:",count)  

 palindrome
s = "madam"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)
if rev == s:
    print("it is palindrome")
else:
    print("not palindrome")


multiplication table
num = 5
for i in range(1,11):
    print(num,"X",i,"-",num*i)


#prime numbers
num = 7
count = 0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("prime number")
else:
     print("not a prime number")


# fibonacci series
a = 0
b = 1
for i in range(7):
    print(a)
    c = a + b
    a = b
    b = c







           
    





