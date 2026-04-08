#sorting the dictionary by key or values

# dict={"c":3,"b":2,"a":1}
# asc={}
# des={}
# for i in sorted(dict.keys()):
#     asc[i]=dict[i]
# print(asc)
# for i in sorted(dict.keys(),reverse=True):
#     des[i]=dict[i]
# print(des)
#------------------------------------------------------------------------------------------------------

#remove all element from dictionary
#write a function to remove all elements from a dictionary  

# def EmptyDict(dict):
#     dict.clear()
#     print(dict)
# dict={"c":3,"b":2,"a":1}
# EmptyDict(dict)
#----------------------------------------------------------------------------------------------------

#write a function to count the number of non-empty (non-null) values in a dictionary

# dict={"A":1,"B":"","C":3,"D":None,"E":"Five"}
# count=0
# for i in dict.values():
#     if i:
#         count+=1
# print(count)
#-------------------------------------------------------------------------------------------------------

#================================================QUEUE===================================================


# import sys
# class Queue:
#     def __init__(self,queuesize):
#         self.queueList=[] # queue initialise/created
#         self.queueListSize=queuesize

#     def isFull(self):
#         if len(self.queueList)==self.queueListSize:
#             return True
#         else:
#             return False

#     def Enqueue(self,value):
#         if self.isFull():
#             print("queue is full")
#         else:
#             self.queueList.append(value)

#     def displayQueue(self):
#         print("----------------------------")
#         print(self.queueList)
#         print("----------------------------")

#     def isEmpty(self):
#         if self.queueList==[]:
#             return True
#         else:
#             return False
        
#     def Dequeue(self):
#         if self.isEmpty():
#             return "queue is empty"
#         else:
#             return self.queueList.pop(0)
        
#     def deleteQueue(self):
#         self.queueList=None
#         return "Queue is deleted"
    
#     def peek(self):             # it return first element of queue 
#         if self.isEmpty():
#             return "Queue is empty"
#         else:
#             return self.queueList[0]
        
#     def exitfromstack(self):
#         exit()
    
# size=int(input("enter the size of the queue:"))
# Queueobj=Queue(size)


# while True:
#     print("1.Enqueue element in the queue:")
#     print("2.display queue element:")
#     print("3.check the queue is empty:")
#     print("4.pop the element from the queue:")
#     print("5.delete the queue:")
#     print("6.peek operation:")
#     print("7.exit:")


#     choice=int(input("enter the choice:"))
#     if choice==1:
#         val=int (input("enter the value for stack:"))
#         Queueobj.Enqueue(val)
#     elif choice==2:
#         Queueobj.displayQueue()
#     elif choice==3:
#         if Queueobj.isEmpty():
#             print("stack is empty")
#     elif choice==4:
#         print(Queueobj.Dequeue())
#     elif choice==5:
#         print(Queueobj.deleteQueue())
#     elif choice==6:
#         print(Queueobj.peek())
#     elif choice==7:
#         sys.exit()
#     else:
#         print("invalid choice")


#=======================================Big O (Wrost complexity)========================================

# O(1) --> constant time
# arry=[1,2,3,4,5]
# arry=[0] it takes constant time to access first element

#---------------------------------------------------------------------------------------------------------

# O(N) --> linear time

# arry=[1,2,3,4,5]
# for element in arry:
#     print(element)
# linear time since it is visiting every element of array

#---------------------------------------------------------------------------------------------------------

#O(Log N) --> logarithmic 

# array=[1,2,3,4,5]
# for index in range(0,len(array),3):
#     print(array[index])
# #
# logrithmic time since it is visiting only some element

#-------------------------------------------------------------------------------------------------------------

#O(N^2) --> quadratic

# array=[1,2,3,4,5]
# for x in array:
#     for y in array:
#         print(x,y)
#loooking array at a every index in the array twice

#----------------------------------------------------------------------------------------------------------------

#O(2^N) --> Expontial 

# def fibonacci(n):
#     if n<=1:
#         return n
#     return fibonacci(n-1)+fibonacci(n-2)
#double recursion in fibonacci

#----------------------------------------------------------------------------------------------------------------

#                     time complexity     space complexity
# create stack            O(1)               O(n)
# push                    O(1)               O(1)
# pop                     O(1)               O(1)
# delete                  O(1)               O(1)
# peek                    O(1)               O(1)
# isEmpty                 O(1)               O(1)
# isFull                  O(1)               O(1)

#stack implement by two level array and linked list

#-------------------------------------------------------------------------------------------------------

#                     time complexity     space complexity
# create queue            O(1)                  O(1)
# Enqueue                 O(1)                  O(n)
# Dequeue                 O(1)                  O(1)
# delete                  O(1)                  O(1)
# peek                    O(1)                  O(1)
# isEmpty                 O(1)                  O(1)
# isFull                  O(1)                  O(1)
#-------------------------------------------------------------------------------------------------------


# def findBiggestNumber(array):------------------->O(1)
#     firstvalue=array[0]------------------------->O(1)
#     for i in range(1,len(array)):--------------->O(n)----->
#         if array[i]>firstvalue:----------------->O(1)----->O(n) #overall complexity is the O(n)
#             firstvalue=array[i]----------------->O(1)----->
#     print(firstvalue)--------------------------->O(1)
    
# array=[2,4,5,6,7,1,9,3,4,5,6]
# findBiggestNumber(array)

#-------------------------------------------------------------------------------------------------------


# WAP to input consists of a string message, representing the message that need to be decode by the agency

# password = input("Enter password: ")

# special = 0
# space = 0

# for ch in password:
#     if ch.isspace():
#         space += 1
#     elif not ch.isalnum():
#         special += 1

# print("Total count =", special + space)

#-------------------------------------------------------------------------------------------------------

# Input
# import math
# n = int(input("Enter number of plots: "))
# areas = list(map(int, input("Enter areas: ").split()))

# count = 0

# # Check each area
# for area in areas:
#     root = int(math.sqrt(area))
    
#     if root * root == area:   # perfect square check
#         count += 1

# # Output
# print("Number of square plots:", count)

#-------------------------------------------------------------------------------------------------------


#Linear Search

# def LinearSearch(array,target):
#     for i in range(len(array)):
#         if array[i]==target:
#             # print("element found at index",i)
#             return i
#     # print("element not found")
#     return -1

# array=[1,2,3,4,5,6,7,8,9]
# target=4
# result=LinearSearch(array,target)
# if result==-1:
#     print("element not found")
# else:
#     print("element found at index",result)


# #-------------------------------------------------------------------------------------------------------

#Binary Search

# def BinarySearch(array,target):
#     low=0
#     high=len(array)-1
#     while low<=high:
#         mid=(low+high)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1

# array=[1,2,3,4,5,6,7,8,9]
# target=4
# result=BinarySearch(array,target)
# if result==-1:
#     print("element not found")
# else:
#     print("element found at index",result)

#-----------------------------------------------------------------------------------------------------------
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None


# class LinkedList:
#     def __init__(self):
#         self.head=None

# LinkedList=LinkedList()
# LinkedList.head=Node(5)
# second=Node(10)
# third=Node(15)
# fourth=Node(20)

# LinkedList.head.next=second
# second.next=third
# print(LinkedList.head.data)
# print(LinkedList.head.next.data)
# print(LinkedList.head.next.next.data)

# #linking part

# LinkedList.head.next=second
# second.next=third
# third.next=fourth
# fourth.next=None


# #display linkedlist

# temp=LinkedList.head
# while temp:
#     print("|",LinkedList.head.data,"|", LinkedList.head.next,"-->",end=" ")
#     LinkedList.head=LinkedList.head.next


