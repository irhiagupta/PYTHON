#LIST AND STRING METHODS


#Question 1- Reverse the whole list using list methods.
l=[1,2,3,4,5,6,7,8,9]
print("The list is: ",l)
l.reverse()
print("Reversed List: ",l)

# Question 2- Print all the uppercase letters from a string.
string=input("Enter the string: ")
for i in string:
    if(i.isupper()):
        print(i)




#Question 3- Split the user input on comma's and store the values in a list as integers
str1=input("Enter the numbers seperated with commas")
list1=[]
list1=str1.split(",")
print("List : ",list1)




# Question 4- Check whether a string is palindromic or not.
'''
strr=input("Enter the string: ")
rev="".join(reversed(strr))
print(strr,rev)
if(strr==rev):
    print("String is Palindromic")
else:
    print("String is not Palindromic")
'''
string = input("Enter the string: ")
rev_string=string[::-1]
if(rev_string==string):
    print("The string is palindrome.")
else:
    print("The string is not a palindrome.")
print("String: ",string)
print("Reversed String: ",rev_string)   
    
    
    
#Question 5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
print("DeepCopy")
import copy
l1=[1,3,[7,9,5],11,15,22,19,10]
l2=copy.deepcopy(l1)
print('List 1: ',l1)
print('List 2(deepcopy of list 1): ',l2)
l2[2][1]=13
print('After changing List 2')
print('List 1: ',l1)
print('List 2(deepcopy of list 1): ',l2)
print(" ")

print("ShallowCopy")
import copy
l1=[1,3,[7,9,5],11,15,22,19,10]
l2=copy.copy(l1)
print('List 1: ',l1)
print('List 2(Shallow copy of list 1): ',l2)
l2[2][1]=13
l2[2][2]=17
print('After changing List 2')
print('List 1: ',l1)
print('List 2(Shallow copy of list 1): ',l2)



'''
#DIFFERENCE BETWEEN SHALLOW COPY AND DEEP COPY
Changes made in deep copy of a list are NOT reflected in the original list
where as changes made in shallow copy of a list are always reflected in original
list.
In deep copy copy of object is copied to other object where as in shallow copy
reference of object is copied in other object
'''
