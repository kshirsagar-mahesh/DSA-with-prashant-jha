# math = 50
# name = "mahesh"
# pi = 3.14
# result = True

# print(type(math))
# print(type(name))
# print(type(pi))
# print(type(result))
# Control + / 

# print(id(math))
# print(id(name))
# print(id(pi))
# print(id(result))

# math = 50
# chem = 50 
# phy = 50

# print(id(math))  #new memory
# print(id(chem))  #same address for both 
# print(id(phy))   


# print(2+2)
# print("2"+"2")

# val1 = input("enter value val1 :") #2
# val2 = input("enter value val2 :") #4
# print(val1 + val2)

# input function by deafault accept only str value 

# #type casting
# val1 = int(input("enter value val1 :"))
# val2 = int(input("enter value val2 :"))
# # print(val1 + val2)

# #int() used to convert in integer 
# print(int(3.14))
# #print(int(10+5i))
# print(int(True))
# print(int(False))
      
# #print(int("4.33"))
# print(int("4"))

# print(int(mahesh))
# we can not convert complex value to int 
# we can not convert float




# #float() used to convert 
# print(float(3))
# # print(float(10+5j)) complex value 
# print(float(True)) # 1.0
# print(float(False)) # 0.0
# print(float("4"))
# print(float("4.33"))    
# # print(float("name"))
# # we can not convert complex value ;to float 
# # can't convert str name to flaot


# # #complex() used to convert
# print(complex(3))
# print(complex(3.14))
# print(complex(True))
# print(complex(False))
# #print (complex("name")) can not convert
# print(complex(5,-3))
# print(complex(True,False))


#======================================================================

# #bool () is used to convert 
# print(bool(3)) 
# print(bool(3.14))
# print(bool(True))
# print(bool(False))
# print(bool())
# print(bool("name"))
# print(bool(-1))
# print(bool(0.0))
# print(bool(0+0j))
# print(bool(0))
# print(bool(2+4j))
# print(bool("mahesh"))
# print(bool(1))

#======================================================================


# Algorithm
# val1 = int(input("enter value val1 :"))
# val2 = int(input("enter value val2 :"))
# print("before swapping values are :val1 =",val1,"val2 =",val2)

# temp = val1
# val1 = val2
# val2 = temp
# print("after swapping values are :val1 =",val1,"val2 =",val2)


# val1 = int(input("enter value val1 :"))
# val2 = int(input("enter value val2 :"))
# print("before swapping values are :val1 =",val1,"val2 =",val2)
# # swapping without using temp variable
# val1 = val1 + val2
# val2 = val1 - val2
# val1 = val1 - val2
# print("after swapping values are :val1 =",val1,"val2 =",val2)

# val1 = int(input("enter value val1 :"))
# val2 = int(input("enter value val2 :"))
# val1,val2 = val2,val1
# print("after swapping values are :val1 =",val1,"val2 =",val2)


# p1 = int(input("enter value p1 :"))
# p2 = int(input("enter value p2 :")) 
# p3 = int(input("enter value p3 :")) 
# total = p1 + p2 + p3
# print("total marks is :",total)
# percentage = (total/3)
# print("percentage is :",percentage)

# p_amount = int(input("enter principal amount :")) #1lakh
# roi = int(input("enter rate of interest :")) #10%
# time = int(input("enter duration of loan amount :")) #1 years

# si= (p_amount * roi * time)/100
# print("simple interest is :",si)

# h=int(input("enter height in feet :"))
# inch=h*12
# cm=inch*2.54
# print("height in inch is :",inch)
# print("height in cm is :",cm)

# num = 123
# a = num%10
# num=num//10
# b = num%10
# num=num//10
# c = num%10
# rev = a*100 + b*10 + c
# print(rev)


# num = 123456
# a=num%10
# num = num//10 
# b=num%10
# num = num//10
# c=num%10
# num = num//10
# d=num%10
# num = num//10
# e=num%10
# num = num//10
# f=num%10

# rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
# print(rev)

#======================================================================

# OPERATER


# when we want do address comparison we should do go for identity operater 

# a=10
# b=10
# print(a is b) #true
# print(a is not b) #false

# a=10
# b=15
# print(a is b) #false
# print(a is not b) #true

#======================================================================

# membership operater
#by using membership operater we can check whether a value is present in sequence or not in collection data structure 

# name = "mahesh"
# print("m" in name) #true  
# print("p" in name) #false
# print("mp" not in name) #false
#===================================================================================================================

#conditional statements

#simple if statement

#WAP to check whether number is positive or not
# num=int(input("enter a number :"))
# if num>0:
#     print("number is positive")
# if num<0:
#     print("number is negative")
# if num==0:
#     print("number is zero")

#=============================================================================================

# n1=10
# n2=20
# n3=30
# n4=40
# n5=50
# if n1>n2:
#     print("n1 is greater",n1)
# if n2>n3:
#     print("n2 is greater",n2)
# if n3>n4:
#     print("n3 is greater",n3)
# if n4>n5:
#     print("n4 is greater",n4)
# if n5>n1:
#     print("n5 is greater",n5) 

#============================================================================================================================================


# n1=int(input("enter value n1 :"))
# n2=int(input("enter value n2 :"))
# n3=int(input("enter value n3 :"))
# n4=int(input("enter value n4 :"))
# n5=int(input("enter value n5 :"))
# if n1>n2 and n1>n3 and n1>n4 and n1>n5: 
#     print("n1 is greater",n1)
# if n2>n1 and n2>n3 and n2>n4 and n2>n5:
#     print("n2 is greater",n2)
# if n3>n1 and n3>n2 and n3>n4 and n3>n5:
#     print("n3 is greater",n3)
# if n4>n1 and n4>n2 and n4>n3 and n4>n5:
#     print("n4 is greater",n4)
# if n5>n1 and n5>n2 and n5>n3 and n5>n4:
#     print("n5 is greater",n5)

# username = input("enter username :")
# password = input("enter password :")
# if username==password:
#     print("login successfull")
# else:
#     print("login failed")


# phy=int(input("enter physics marks :"))
# chem=int(input("enter chemistry marks :"))
# math=int(input("enter math marks :"))
# gender=input("enter male or female gender :")

# total=phy+chem+math
# percentage=(total/3)

# if percentage>=60 and gender=="male":
#     print("eligible for placement")
# elif percentage>=60 and gender=="male":
#     print("eligible for data entery")
# else:
#     print("not valid")

#===============================================================================================================================

# print("enter three numbers to find greatest among them :")
# a=int(input("enter value a :"))
# b=int(input("enter value b :"))
# c=int(input("enter value c :"))
# if a>b:
#     if a>c:
#         print("a is greater",a)
#     else:
#         print("c is greater",c)
# else:
#     if b>c:
#         print("b is greater",b)
#     else:
#         print("c is greater",c)

#===============================================================================================================================

# day=input("enter a day :")
# if day == "saturday"or day== "SATURDAY" and day== "sunday" or day== "SUNDAY":
#     print("weekend")
# else:
#     print("workday")

#===============================================================================================================================

# a=input("enter a character,special symbol,lowercase or uppercase :")
# if a.isalpha():
#     if a.isupper():
#         print("uppercase")
#     else:
#         print("lowercase")
# elif a.isdigit():
#     print("digit")
# else:
#     print("special symbol") 

#===============================================================================================================================

# ch=ord(input("enter a character :"))
# if ch>=65 and ch<=90:
#     print("uppercase")
# elif ch>=97 and ch<=122:
#     print("lowercase")
# elif ch>=48 and ch<=57:
#     print("digit")
# else:
#     print("special symbol")

#===============================================================================================================================

amount=int(input("enter amount :"))
print("500 notes :",amount//500)
print("200 notes :",amount%500//200)
print("100 notes :",amount%500%200//100)
print("50 notes :",amount%500%200%100//50)
print("20 notes :",amount%500%200%100%50//20)
print("10 notes :",amount%500%200%100%50%20//10)
print("5 notes :",amount%500%200%100%50%20%10//5)
print("1 notes :",amount%500%200%100%50%20%10%5)





















# print("100 notes :",amount//100)
# print("50 notes :",amount%100//50)
# print("20 notes :",amount%100%50//20)
# print("10 notes :",amount%100%50%20//10)
# print("5 notes :",amount%100%50%20%10//5)
# print("1 notes :",amount%100%50%20%10%5)

