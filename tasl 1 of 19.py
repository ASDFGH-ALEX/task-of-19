'''
author:Alex Sabu
Date:19-10-2024
Description:Simple desktop calculator using Python. Only the five basic arithmetic operators.
'''
num1=int(input("enter the first  number"))
num2=int(input("enter the second number"))
num3=int(input("Enter a third Number"))
str1=num1+num2
print("THe sum of num1 and num2 is:",str1)
str2=num2-num1
print("The difference when num2 is subtracted from num1 is",str2)
str3=num1*num2
print("The product of num1 and num2 is",str3)
str4=num1/num2
print("The quotient when num1 is divided by num2 is",str4)
str5=num1%num2
print("The remainder when num1 is divided by num2 is",str5)
str6=(num2+num2) * num3 / 2
print("The result of (num1 + num2) * num3 / 2 is: ",str5)