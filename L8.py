# import sys
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class LinkedList:    
#     def __init__(self):
#         self.head = None

#     def addNode(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node

#     def addNodeBegining(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def addNodeBetween(self, data, position):
#         new_node = Node(data)
#         if position == 0:
#             self.addNodeBegining(data)
#             return
#         temp = self.head
#         for i in range(position - 1):
#             if temp is not None:
#                 temp = temp.next
#         if temp is None:
#             print("Position out of bounds")
#         else:
#             new_node.next = temp.next
#             temp.next = new_node

#     def addNodeEnd(self, data):
#         self.addNode(data)

#     def display(self):
#         temp = self.head
#         if temp is None:
#             print("List is empty")
#             return
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")
    
# object = LinkedList()
# if __name__ == '__main__':

#     while True:
#         print("1.add node Linkedlist:")
#         print("2.add node in begining:")
#         print("3.add node in between:")
#         print("4.add node in end:")
#         print("5.display linked list:")
#         print("6.exit")

#         ch=int(input("enter the choice:"))
#         if ch==1:
#             value=int(input("enter the value for node:"))
#             object.addNode(value)
#             print("node added successfully")
#         elif ch==2:
#             value=int(input("enter the value for node:"))
#             object.addNodeBegining(value)
#             print("node added successfully")
#         elif ch==3:
#             value=int(input("enter the value for node:"))
#             position=int(input("enter the position for node:"))
#             object.addNodeBetween(value,position)
#             print("node added successfully")
#         elif ch==4:
#             value=int(input("enter the value for node:"))
#             object.addNodeEnd(value)
#             print("node added successfully")
#         elif ch==5:
#             object.display()
#         elif ch==6:
#             break
#         else:
#             print("invalid choice")

#===============================================================================================================

#types of linked list

# 1.singly linked list
# 2.doubly linked list
# 3.circular linked list
# 4.circular doubly list


#--------------------------------------------------------------------------------------------------------------


# #WAP to remove only leading zeros from a list of integers using for loop
# s = [0,0,1,2,0,3,0,0,4]
# result = []
# started = False

# for num in s:
#     if num != 0:
#         started = True
#     if started:
#         result.append(num)

# print(s)
# print(result)

#-------------------------------------------------------------------------------------------------------------


