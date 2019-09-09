# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:51:26 2019

@author: Ankit
"""
print("Welcome to python Basics Review !! ")
print("Kindly Remove individual comments and respective output statements to refresh you python basics")
# =============================================================================
# Python Basics useful for financial data
# =============================================================================
#Lists:
#Initialization:
#mylist1 = [1,2,3,4]
#mylist1.append(5)
#print(mylist1)
#Access:
#print(mylist1[1])

#Dictionary
#myDict = {'key1':10,'key2':20,'key3':30}
#print(myDict)
#print(myDict['key1'])

#Tuples (immutable)
#tup = (1,2,3)
#Access
#print(tup[2])

#Sets
#mySet = {1,2,2,3,3,4,4,5}
#print(mySet)

#loops For while
#list2 = [1,2,3,4,5]
#for i in list2:
#     print(i)
#i = 0 
#while i < len(list2):
#    print(list2[i])
#    i+=1

#Functions - lambda exp. - Maps - Filters
#def foo(i = 5):
#    return i*2
#print(foo(3))

#k = lambda var:var*2 + 1
#print(k(1))

#list3 = [1,2,3,4,5]
#result = list(map(lambda var:var*3, list3))
#print(result)

#result = map(lambda var:var*3, list3) 
#print(next(result))
#print(next(result))

#def is_even(i):
#    return i%2==0
#list4 = [1,2,3,4,5]
#result1 = list(filter(is_even, list4))
#result2 = filter(is_even, list4)
#print(result1)
#print(result2)

# =============================================================================
# NumPy useful components
# =============================================================================
import numpy as np
#Numpy Arrays
#myArray = np.array([3,4,5,6,7]) 
#print(myArray)

#myArray1 = np.arange(1,7,1)
#print(myArray1)

#myArray2 = np.zeros((2,2)) 
#print(myArray2)

#print(np.ones(3))
#
#print(np.ones((3,3)))
#
#print(np.linspace(1,5,10))
#
#print(np.eye(3))

#print(np.random.rand(2))
#
#print(np.random.randn(2))
#
#print(np.random.standard_normal(2))

#numpy operations
#myArray2 = np.array([1,2,3,4,5])
#
#print(myArray2 + myArray2)
#
#print(myArray2)
#
#print(myArray2 + 1)
#
#print(myArray2[1:-1])
#
#print(myArray2[2])
#
#myArray3 = myArray2.copy()
#print(myArray3)
#
#bool_arr = myArray3 > 3
#print(bool_arr)
#
#print(myArray3[bool_arr])

#myMatrix = np.ones((4,3))
#print(myMatrix)
#
#print(myMatrix.sum(axis = 0))
#print((myMatrix.sum(axis = 0)).shape)
#
#print(myMatrix.sum(axis = 1))
#print((myMatrix.sum(axis = 1)).shape)