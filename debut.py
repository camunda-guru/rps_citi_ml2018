# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:59:17 2018

@author: Balasubramaniam
"""
print("Welcome to Python and R Training to work with Machine Learning")

#identifiers

firstName=input("Enter First Name")
lastName=input("Enter Last Name")
print("First Name=%s\t\tLast Name=%s" %(firstName,lastName))
age=int(input("Enter Age"))
print("Age= %d" %(age))

#conditional statement
if(age>21)and(age<=58):
    print("permitted to use Premium CC")
elif(age>58):
    print("permitted to use Basic CC")
else:
    print("Not Allowed")





firstName="CITI"
print("Organization Name%s" %(firstName))

firstName="78"
print("Organization Name%s" %(firstName))

#multi line statements
productDescription="The product is introduced to cover   middle class segment. I would like to invite 'Amitabh' to introduce "
print(productDescription)