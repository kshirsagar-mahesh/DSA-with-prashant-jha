# #string 
# # indexing start form 0 and also space have  index
# #srting slicing

# Name = "mahesh"
# #indexing = 0122345
# print(Name[0]) # m
# print(Name[1]) # a
# print(Name[2]) # h
# print(Name[3]) # e
# print(Name[4]) # s
# print(Name[5]) # h 
# print(Name[-1]) # h
# print(Name[-2]) # s
# print(Name[-3]) # h
# print(Name[-4]) # e
# print(Name[-5]) # a
# print(Name[-6]) # m
# # print(Name[6]) # error because index out of range
# # slicing
# print(Name[0:3]) # mah
# print(Name[1:]) # ahesh
# print(Name[2:5]) # hes
# print(Name[3:6]) # esh
# print(Name[:6]) # mahes
# print(Name[:]) # mahesh
# print(Name[0:6:2]) # mhs
# print(name[::-1]) # reverse string

#======================================================================================================

# str = "Python is a High level programming language"
# print(str.lower())
# print(str.upper())
# print(str.swapcase())            #makes lower case to upper case and upper case to lower case
# print(str.title())               #makes first letter of each word to capital
# print(str.capitalize())          #makes first letter of string to capital and rest to small
# print(str.count("a"))            # counts the number of times "a" appears in the string

#======================================================================================================

# print("subject marks:")
# phy=50
# chem=60
# math=70

# print("physics ={} chemistry ={} math ={}".format(phy,chem,math))

# print("physics = {0} chemistry = {1} math p= {2}".format(phy,chem,math))

# print("physics = {x} chemistry = {y} math = {z}".format(x=phy ,y=chem,z=math))

# total = phy + chem + math
# print("total marks ",f"{total}")

# print ("roll no=","7",zfill(4)) #zfill is used to fill the number with zeros to make it 4 digits

#=====================================================================================================

#Looping statements
# for loop

#for(intialization; condition; increment/decrement)

# for i in range(5):
#     print(i)

# for i in range (1,5):
#     print(i)

# for i in range (1,11,2):
#     print(i)

# for i in range (1,11):
#     print (i*2)


# for i in range (1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)

# print()

# for i in range (1,11):
#     print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)

#=====================================================================================================

# name = "racear"
#       #012345
# for i in name:
#     print(i) 

#wap to remove duplicate character from string

# name = "racear"
# new_name = ""
# for i in name:
#     if i not in new_name:
#         new_name = new_name + i
# print(name)
# print(new_name)

#=====================================================================================================

# for i in range (10,-1,-2):
#     print(i)

# name = "mumbai"
# n=len(name)
# print(n)
# new_name = ""
# for i in range(n-1,-1,-1):
#     new_name += name[i]
# print(new_name)

#=====================================================================================================
# name = "hello"
# n=len(name)
# new_name = ""
# for i in range(n-1,-1,-1):
#     new_name += name[i]
# print(new_name)
# if name == new_name:
#     print("palindrome")
# else:
#     print("not palindrome")


# name1 = "racecar"
# print(name1)
# print(name1[::-1])
# if name1 == name1[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

#=====================================================================================================


