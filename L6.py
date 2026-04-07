#WAP a program to compress a string by repalcing consecutive with their counts

# def compress_string(s):
#     result = ""
#     count = 1

#     for i in range(len(s)):``
#         if i + 1 < len(s) and s[i] == s[i + 1]:
#             count += 1
#         else:
#             result += s[i] + str(count)
#             count = 1

#     return result
# s = input("Enter a string: ")
# print("Compressed string:", compress_string(s))

#-------------------------------------------------------------------------------------------------------------------
# #WAP to reverse string
# s = input("Enter a string: ")
# rev = s[::-1]
# print("Reversed string:", rev)

#-------------------------------------------------------------------------------------------------------------------


#====================================================Abstraction====================================================



# from abc import ABC,abstractmethod
# class help4code(ABC):
#     @abstractmethod
#     def training(self):
#         pass

#     @abstractmethod
#     def placement(self):
#         pass

# class prashant(help4code):
#     def training(self):
#         print("c","c++","java")
#     def placement(self):
#         print("java plscement")


# class Ashish(help4code):
#     def training(self):
#         print("python | django")
#     def placement(self):
#         print("python placement")

# class ankush(help4code):
#     def training(self):
#         print("machine learning")
#     def placement(self):
#         print("data science placement")

# obj1=prashant()
# obj1.training()
# obj1.placement()

# obj2=Ashish()
# obj2.training()
# obj2.placement()

# obj3=ankush()
# obj3.training()
# obj3.placement()

#-------------------------------------------------------------------------------------------------------------------

# from abc import ABC, abstractmethod   
# class Irctc(ABC):#abstract class  
  
#     @abstractmethod  
#     def bookTicket(self): # abstract method  
#         pass  
  
# class MakeMyTrip(Irctc):  
  
#     def bookTicket(self):  
#         print( "  ==========================================")  
#         print("    Welcome To makemytrip   ")  
#         source      = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date        = input("Enter date")  
#         print( "  ==========================================")  
          
# class GoIbibo(Irctc):  
      
#     def bookTicket(self):  
#         print("    Welcome To GOIBIBO")  
#         source      = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date        = input("Enter date")  
  
# class Yatra(Irctc):  
      
#     def bookTicket(self):  
#         print("    Welcome To Yatra  ")  
#         source      = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date        = input("Enter date")  
  
# m = MakeMyTrip()  
# m.bookTicket()  
# g = GoIbibo()  
# g.bookTicket()  
# y = Yatra()  
# y.bookTicket()  

#-------------------------------------------------------------------------------------------------------------------


# class Base:
#     def __init__(self):
#         print("parent class constructor called")
#         self.a="prashant" #public variable
#         self.__c="ashish" #privet member

# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         #calling constructor of base class
#         Base.__init__(self)
#         # print("Calling privet member of base classs")
#         # print(self.a)
#         # print(self.__c)

# # obj1=Derived()
# # print(obj1.a)
# # print(obj1.__c)

# obj2=Base()
# print(obj2.a) #Accesible
# print(obj2.__c) #not Accesible


#-------------------------------------------------------------------------------------------------------

# class Rbi:
#     def publicpolicy(self):
#         print("Check the public policy of RBI")

#     def __privatepolicy(self):
#         print("there is some private policy which is not accesible for public")

# class Sbi(Rbi):
#     def __init__(self):
#         Rbi.__init__(self)

#     def callingpublicmethod(self):
#         print("\nInside child class")
#         self.publicpolicy()

#     def callingprivateMethod(self):
#         self.__privatepolicy()

# obj1=Sbi()
# obj1.callingpublicmethod()
# obj1.callingprivateMethod()
# obj1.publicpolicy()
# obj1.__privatepolicy()

# obj2=Rbi()
# obj2.publicpolicy()
# obj2.__privatepolicy()

# obj2=Rbi()
# obj2.publicpolicy()
# obj2._Rbi__privatePolicy

#------------------------------------------------------------------------------------------------------------------------


# n = int(input("Enter size: "))
# print("Enter the element equal to size")
# arr = list(map(int, input("Enter elements: ").split()))

# if len(arr) != n:
#     print("Error: You must enter exactly", n, "elements")
# else:
#     even_list = []
#     odd_list = []

#     for num in arr:
#         if num % 2 == 0:
#             even_list.append(num)
#         else:
#             odd_list.append(num)

#     result = even_list + odd_list
#     print("Result:", *result)