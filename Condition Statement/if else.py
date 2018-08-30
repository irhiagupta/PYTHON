# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:42:31 2018

@author: Rhia
"""


#Question 1: verify if the year entered by the user is a leap year
year=int(input("Enter the year: "))
a=year%100
if(a%4==0):
    print("{} is a leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))




#Question 2: square or rectangle dimensions
length=input("Enter the length: ")
breadth=input("Enter the breadth: ")
if(length==breadth):
    print("These dimensions are for square as length=breadth")
else:
    print("These dimensions are for rectangle as length is not equal to breadth")




#Question 3: determine oldest and youngest.
p1=int(input("Enter the age of person1: "))
p2=int(input("Enter the age of person2: "))
p3=int(input("Enter the age of person3: "))
if(p1>p2 and p1>p3):
    print("Person 1 is the oldest.")
    if(p2>p3):
        print("Person 3 is the youngest.")
    else:
        print("Person 2 is the youngest.")
elif(p2>p1 and p2>p3):
    print("Person 2 is the oldest.")
    if(p1>p3):
        print("Person 3 is the youngest.")
    else:
        print("Person 1 is the youngest.")
else:
    print("Person 3 is the oldest.")
    if(p1>p2):
        print("Person 2 is the youngest.")
    else:
        print("Person 1 is the youngest.")



#Question 4: conditions
age=int(input("Enter your age: "))
sex=input("Enter your sex(M or F): ")
m_status=input("Are you married(Y or N): ")
if(sex=='F'):
    print("YOU WILL ONLY WORK IN URBAN AREAS.")
else:
    if(20<=age<=40):
        print("YOU CAN WORK ANYWHERE YOU WANT.")
    elif(40<age<=60):
        print("YOU WILL ONLY WORK IN URBAN AREAS.")
    else:
        print("Wrong Input.")




#Question 5: discount
amt=int(input("Enter the quatity: "))
price=amt*100
if(price>1000):
    print("You will 10% discount.")
    dis=(int)(0.1*price)
    print("Your price: ",dis)
else: 
    print("You won't get the discount.")
    



#LOOPS:

#Question 1:take 10 inputs from user and print them on sceen
for i in range(10):
    a=int(input("Enter the integer: "))
    print("You entered: ",a)




#Question 2: write an infinite loop
while(True):
    print("Hello Buddy")





#Question 3: write a list of integers and another for the squares fo the first one
l=input("Enter the integers: ")
l1=l.split()
l2=[]
for i in l1:
    n=(int)(i)*(int)(i)
    l2.append(n)
print("The List: ",l1)
print("The List with squares: ",l2)
  



#Question 4: differentiate between int,strings,float and put them separately
list=input("Enter the list with integers, strings and floats: ")
l=list.split()
integer=[]
strings=[]
float_=[]
for i in l:
    if(i.isdigit()):
        integer.append(i)
    elif(i.isalpha()):
        strings.append(i)
    else:
        float_.append(i)
print("List of integers: ",integer)
print("List of strings: ",strings)
print("List of float: ",float_)     
 



#Question 5: prime number from (1,101)
import math as m
temp=0
for i in range(2,101):
    temp=0
    for j in range(2,i):
        if(i%j==0):
            temp=1
            break
    if(temp==0):
         print(" ",i)
  



#Question 6: Pattern printing
def pypart(n):
    for i in range(0, n):
        for j in range(0, i+1):
         
            print("* ",end="")
      
        print("\r")
n = 5
pypart(n)       



#Question 7: find an element and delete it 
l1=input("Enter the list of numbers: ")
l2=l1.split()
num=int(input("Enter the number: "))
for i in l2:
    if(i==num):
        l2.remove(i)
        break
print("The list: ",l2)
       


     