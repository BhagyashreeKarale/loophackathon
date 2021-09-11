# Loops
# 1. Write a program to print the following using while loop 
# a. First 10 Even numbers

#while loop
num = 1
while num <= 10 :
    if num % 2 == 0 :
        print(num)
    num = num + 1

#for loop
for num in range(1,11):
    if num % 2 == 0 :
        print(num)
########################################################################################################

# b. First 10 Odd numbers

num = 1
while num <= 10 :
    if num % 2 != 0 :
        print(num)
    num = num + 1

#for loop
for num in range(1,11):
    if num % 2 != 0 :
        print(num)
########################################################################################################

# c. First 10 Natural numbers

#while loop
num = 1
while num<=10:
    print(num)
    num=num+1
#for loop
for num in range(1,11):
    print(num)
########################################################################################################

# d. First 10 Whole numbers

#while loop
num=0
while num<10:
    print(num)
    num=num+1
#for loop
for num in range(0,10):
    print(num)
########################################################################################################

# 2. Write a program to print first 10 integers and their squares like
# 1 1
# 2 4
# 3 9 
# ………………...and so on

#while loop
num=1
while num<=10:
    print(num,num**2)
    num=num+1
#for loop
for num in range(1,11):
    print(num,num**2)
########################################################################################################

# 3. Write while loop  statement to print the following series:
# 10, 20, 30 … … 300

#while loop
num=10
while num<=300:
    print(num)
    num=num+10
#for loop
for num in range(10,301,10):
    print(num)
########################################################################################################

# 4. Write a while loop  statement to print the following series
# 105, 98, 91 ………7

#while loop
num=105
while num>=7:
    print(num)
    num=num-7
#for loop
for num in range(105,6,-7):
    print(num)
########################################################################################################

# 5. Write a program to print the first 10 natural numbers in reverse order.

#while loop
num=10
while num>=1:
    print(num)
    num=num-1
#for loop
for num in range(10,0,-1):
    print(num)
########################################################################################################

# 6. Write a program to print the sum of the first 10 Natural numbers.

#while loop
num=1
sum=0
while num<=10:
    sum=sum+num
    num=num+1
print(sum,"is the sum of first 10 natural numbers")
#for loop
sum=0
for num in range(1,11):
    sum=sum+num
print(sum,"is the sum of first 10 natural numbers")
########################################################################################################

# 7. Write a program to print the sum of the first 10 Even numbers.

#while loop
num = 1
counter=1
sum=0
while num <= 10 :
    if counter % 2 == 0 :
        num = num + 1
        sum=sum+counter
    counter=counter + 1
print(sum,"is the sum of first 10 even numbers")
#for loop
sum=0
count=0
for count in range(0,2*11,2):
    sum=sum+count
print(sum)
# 8. Write a program to print a table of a number entered from the user.

#while loop
num=int(input("Enter a number:\n"))
print("Table of the entered number is:\n")
count=1
while count<=10:
    print(num,"*",count,"=",num*count)
    count=count+1
#for loop
num=int(input("Enter a number:\n"))
print("Table of the entered number is:\n")
for i in range(1,11):
    print(num,"*",i,"=",num*i)

# 9. Write a program to display all even numbers that fall between two numbers 
# (exclusive both numbers) entered by the user.

#while loop
num1=int(input("Enter lower limit number:\n"))
num2=int(input("Enter upper limit number:\n"))
counter=num1+1
while counter<num2:
    if counter % 2 == 0 :
        print(counter)
    counter=counter+1

#for loop
num1=int(input("Enter lower limit number:\n"))
num2=int(input("Enter upper limit number:\n"))
for i in range(num1+1,num2):
    if i % 2 == 0:
        print(i)


# 10. Write a program to check whether a number is prime or not.

#while loop
num = int(input("Enter a number ( greater than 1)"))
f = 0
i = 2
while i <= num / 2:
    if num % i == 0:
        f=1
        break
    i=i+1
    
if f==0:
    print(num,"is a PRIME number")
else:
    print(num,"is not a PRIME number")
#for loop
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")
# 11. Write a program to find the sum of the digits of a number accepted from the user.

#while loop
num=int(input("Enter the number:\n"))
if len(str(num))<=1:
    print(num)
else:
    temp=num
    sum=0
    while temp>0:
        digit=temp % 10
        sum=sum+digit
        temp=temp//10
    print(sum,"is the sum of the digits of the entered number")

# 12. Write a program to find the product of the digits of a number accepted from the user.
num=int(input("Enter the number:\n"))
if len(str(num))<=1:
    print(num)
else:
    temp=num
    product=1
    while temp>0:
        digit=temp % 10
        product=product+digit
        temp=temp//10
    print(product,"is the sum of the digitd of the entered number")
# 13. Write a program to reverse the number accepted by the user.
num=int(input("Enter the number:\n"))
if len(str(num))<=1:
    print(num)
else:
    temp=num
    rev=0
    while temp>0:
        digit=temp % 10
        rev=rev*10+digit
        temp=temp//10
    print(rev,"is the reversed number")
# 14. Write a program to display the number names of the digits of if the number is 231 then output should be Two a number entered by user, for example Three One
# 15. Write a program to print the Fibonacci series till n terms (Accept n from user)
n=int(input("Enter a number:\n"))
a,b=0,1
counter=0
while counter<n:
    if counter==0:
        print(0)
    print(b)
    a,b=b,a+b#this is similar to:temp=a a=b b=temp+a
    counter=counter+1
# 16. Write a program to print the factorial of a number accepted by the user.
num=int(input("enter "))
# 17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)
# 18. Write a program to convert binary to decimal.
# 19. Write a program to add first n terms of the following series using a while loop :
# 1/1! + 1/2! + 1/3! + …….. + 1/n!
# 20. Write a program to check whether a number is palindrome or not.
# 21. Write a python program  to sum the sequence:
# 1 + 1/1! + 1/2! + 1/3! + …….. + 1/n!
# 22. Write a program to accept 10 numbers from the user and display it’s average.
# 23. Write a program to accept 10 numbers from the user and display the largest & smallest number.
# 24. Write a program to display sum of odd numbers and even numbers separately that fall between two numbers accepted from the user.(including both numbers) 100 and 500.
# 26. Write a program to print the following series till n terms.
# 2 , 22 , 222 , 2222 _ _ _ _ _ n terms
# 27. Write a program to print the following series till n terms.1 4 9 16 25 _ _ _ _ _ n  terms

# 28. Write a program to find the sum of the following series(accept values of x and n from user)
# 1 + x/1! + x2/2! + ……….xn/n!
 
# x + x2/2 + ……….xn/n
# 30. Write a program to find the sum of following series
# 1 + 8 + 27 …………n terms
# 31. Write a program to find the sum of following series:
# 1 + 2 + 6 + 24 + 120 . . . . . n terms
# 32. Write a program to find the sum of following series:
# S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms
# 33. Write a Program to print all the characters in the string ‘COMPUTER’ using a while loop .
# 34. Write a program to print only odd numbers from the given list using  a while loop . L = [23, 45, 32, 25, 46, 33, 71, 90]
# 35. Write a program to print all the factors of a number using a while loop .
# 36. Accept two numbers from the user and display sum of even numbers between them(including both)
# 37.Write a program to print the factorial of a number.
# 38.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).`
# 39.Write a Python program to guess a number between 1 to 9
# 340.Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
