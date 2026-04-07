#=======================================================stack=================================================

#1.stack implementation without size limit
#push
# pop
# isEmpty
# isFull
#isDelete

# import sys
# class Stack:
#     def __init__(self):
#         self.stackList=[] # stack initialise/created

#     def Push(self,value):
#         self.stackList.append(value)

#     def displayStack(self):
#         print("----------------------------")
#         print(self.stackList)
#         print("----------------------------")

#     def isEmpty(self):
#         if self.stackList==[]:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stackList.pop()
        
#     def deleteStack(self):
#         self.stackList=None
#         return "stack is deleted"
    
#     def peek(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stackList[-1]
        
#     def exitfromstack(self):
#         exit()
    
# stackobj=Stack()


# while True:
#     print("1.push element in the stack :")
#     print("2.display the stack element:")
#     print("3.check the stack is empty:")
#     print("4.pop the element from the stack:")
#     print("5.delete the stack:")
#     print("6.display the top element of the stack:")
#     print("7.exit:")


#     choice=int(input("enter the choice:"))
#     if choice==1:
#         val=int (input("enter the value for stack:"))
#         stackobj.Push(val)
#     elif choice==2:
#         stackobj.displayStack()
#     elif choice==3:
#         if stackobj.isEmpty():
#             print("stack is empty")
#     elif choice==4:
#         print(stackobj.pop())
#     elif choice==5:
#         print(stackobj.deleteStack())
#     elif choice==6:
#         print(stackobj.peek())
#     elif choice==7:
#         stackobj.exitfromstack()
#     else:
#         print("invalid choice")


#=================================================================================================

#2.stack implementation with size limit

# import sys
# class Stack:
#     def __init__(self,stacksize):
#         self.stackList=[] # stack initialise/created
#         self.stacksize=stacksize

#     def isFull(self):
#         if len(self.stackList)==self.stacksize:
#             return True
#         else:
#             return False

#     def Push(self,value):
#         if self.isFull():
#             print("stack is full")
#         else:
#             self.stackList.append(value)

#     def displayStack(self):
#         print("----------------------------")
#         print(self.stackList)
#         print("----------------------------")

#     def isEmpty(self):
#         if self.stackList==[]:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stackList.pop()
        
#     def deleteStack(self):
#         self.stackList=None
#         return "stack is deleted"
    
#     def peek(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stackList[-1]
        
#     def exitfromstack(self):
#         exit()
    
# size=int(input("enter the size of the stack:"))
# stackobj=Stack(size)


# while True:
#     print("1.push element in the stack :")
#     print("2.display the stack element:")
#     print("3.check the stack is empty:")
#     print("4.pop the element from the stack:")
#     print("5.delete the stack:")
#     print("6.display the top element of the stack:")
#     print("7.exit:")


#     choice=int(input("enter the choice:"))
#     if choice==1:
#         val=int (input("enter the value for stack:"))
#         stackobj.Push(val)
#     elif choice==2:
#         stackobj.displayStack()
#     elif choice==3:
#         if stackobj.isEmpty():
#             print("stack is empty")
#     elif choice==4:
#         print(stackobj.pop())
#     elif choice==5:
#         print(stackobj.deleteStack())
#     elif choice==6:
#         print(stackobj.peek())
#     elif choice==7:
#         stackobj.exitfromstack()
#     else:
#         print("invalid choice")


#=================================================================================================

