# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 09:09:34 2018

@author: Rhia
"""


#Question 1:Create a function to find the area of the sphere
import math as m
def area_sphere(radius):
    area=4*m.pi*float(radius^2)
    print("Area of the sphere with radius {} is {}".format(radius,area))

radius=input("Enter the Radius: ")
area_sphere(radius)



#Question 2: check if the number is a perfect number
def perfect_number(num):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum=sum+i
    if(sum==num):
        print("{} is a perfect number".format(num))
    else:
        print("{} is not a perfect number as the sum is {}".format(num,sum))
num=int(input("Enter the Number: "))
perfect_number(num)
"""
import math as m
def perfect_number(num):
    sum=0
    //a=(int)(m.sqrt(num))
    for i in range(1,num):

        if(num%i==0):
            sum=sum+i
    if(sum==num):
        print("{} is a perfect number".format(num))
    else:
        print("{} is not a perfect number as the sum is {}".format(num,sum))
num=int(input("Enter the Number: "))
perfect_number(num)

"""


#Question 3: multiplication table of n (input by the user)
def table(num):
    prod=1
    for i in range(1,11):
        prod=num*i
        print("{} * {}= {}".format(i,num,prod))
num=int(input("Enter the Number: "))
table(num)




#Question 4: find the power of the number using recurrsion (a^b)
def power(num,exp):
    if(exp==1):
        return num;
    else:
        return num*power(num,exp-1)
num=int(input("Enter the number: "))
exp=int(input("Enter the exponent: "))
result=power(num,exp)
print("Answer: ",result)
