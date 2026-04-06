# print('prashantjha777'.isalnum())
# print('prashantjha'.isalpha())
# print('777f'.isdigit())
# print('prashantjha777'.islower())
# print(''.isupper())
# print('PRASHANTj'.isupper())
# print("My Name Is Prashant".istitle())
# print("".istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo")) 


#---------------------------------------------------------------------------------------------------------


# print("Prashant".find("r"))
# print("Prashant".index("r"))
# print("Prashant jha".count("a"))

#---------------------------------------------------------------------------------------------------------

#WAP to to check if a key exists in a dictionary 
# dict = {"name":"Alice","age":25,"city":"New York"}
# key =input("enter the key: ")
# if key in dict:
#     print("exist")
# else:
#     print("not exist")

#---------------------------------------------------------------------------------------------------------

#WAP to count the frequency of list using dictionary

#---------------------------------------------------------------------------------------------------------


#=================================================Exception Handling=======================================


# n1=int(input("enter the first value:"))
# n2=int(input("enter the second value:"))
# try:
#     print(n1/n2)
# except:
#     print("can't divide by zero")

# print("to be continued")

#---------------------------------------------------------------------------------------------------------

# try:
#     n1=int(input("Enter the first value:"))
#     n2=int(input("Enter the second value:"))
#     print(n1/n2)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("Enter only integer value")
# except:
#     print("Something went wrong")  #default block

# print("To be continued")

#---------------------------------------------------------------------------------------------------------

#handling multiple differnt kinds of exception with single except block.

# try:
#     a=int(input("Enter the first integer:"))
#     b=int(input("Enter the second integer:"))
#     print(a/b)
# except(ValueError,ZeroDivisionError)as message:
#     print(message)

#---------------------------------------------------------------------------------------------------------

# try:
#     a=int(input("Enter the first integer:"))
#     b=int(input("Enter the second integer:"))
#     print(a/b)
# except(ValueError,ZeroDivisionError)as message:
#     print("Enter correct number",message)
# else:
#     print("Everithing is ok")

#---------------------------------------------------------------------------------------------------------

# try:
#     a=int(input("Enter the first integer:"))
#     b=int(input("Enter the second integer:"))
#     print(a/b)
# except(ValueError,ZeroDivisionError)as message:
#     print("Enter correct number",message)
# finally:
#     print("I will always execute")

#-------------------------------------------------------------------------------------------------------

#nested try except block

# try:
#     a=int(input("Enter the first integer:"))
#     b=int(input("Enter the second integer:"))
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("Can't divide by zero")
# except ValueError:
#     print("Enter only integer value")


#-------------------------------------------------------------------------------------------------------

# try:
#     a=int(input("Enter the first integer:"))
#     b=int(input("Enter the second integer:"))
#     print(a/b)
# except(ValueError,ZeroDivisionError)as message:
#     print("Enter correct number",message)
# else:
#     print("Everithing is ok")
# finally:
#     print("I will always execute")

#-------------------------------------------------------------------------------------------------------


# count repetitive digits and find security key if no repetitive digits are there print -1 as security key
# a = [5,7,8,3,7,8,9,2,3]
# b = {}
# print(a)
# count = 0
# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# print(b)
# for key, value in b.items():
#     if value > 1:
#         count += 1
# if count > 0:
#     print("Security key is: ", count)
# else:
#     print("Security key is: -1")

#-------------------------------------------------------------------------------------------------------


# mylist=[5,7,8,3,7,8,9,2,3]
# newlist=[]
# for i in range(len(mylist)):
#     count=0
#     key=mylist[i]

#     j=i+1
#     while j<len(mylist):
#         if key==mylist[j]:
#             count+=1
#         j+=1
# print(len(newlist)) 

# #-------------------------------------------------------------------------------------------------------

# list=[7,3,9,2,8]
# list.sort()
# print(list)
# print(list[-2])

#-------------------------------------------------------------------------------------------------------

# i=1
# while i<=5:
#     print(i)
#     i=i+1

#-------------------------------------------------------------------------------------------------------

# name="programing"
# vowels=["a","e","i","o","u"]
# cons=0
# vowel=0
# for i in name:
#     if i in vowels:
#         vowel+=1
#     else:
#         cons+=1
# print("consonent",cons)
# print("vowel",vowel)

#-------------------------------------------------------------------------------------------------------

# list=[1,2,2,3,4,2]
# new_list=[]
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
#     else:
#         i==i in new_list
#         new_list.remove(i)
# print(new_list)


# wrong code

#==============================================File Handling in Python========================================

# f=open("myfile.txt","w")
# print("name of the file:",f.name)
# print("mode of the file:",f.mode)
# print("is file readable:",f.readable())
# print("is file writable:",f.writable())
# print("is file closed:",f.closed)
# f.close()
# print("is file closed:",f.closed)

#-------------------------------------------------------------------------------------------

# f=open("myfile.txt","a") #"a" for append the data
# f.write("\n hello mahesh")
# f.close()
# print("is file closed:",f.closed)

#-------------------------------------------------------------------------------------------

# f=open("myfile.txt","w")
# mylist=["\nprashant"," ","mahesh"," ","suresh"]
# tuple=("\nprashant"," ","mahesh"," ","suresh")
# dict={"\nprashant":1,"mahesh":2,"suresh":3}
# f.writelines(dict)
# f.writelines(tuple)
# f.writelines(mylist)
# f.close()
# print("Written work has done successfully")

#-------------------------------------------------------------------------------------------

# f=open("myfile.txt","r")
# print(f.read())
# f.close()
# # print(f.read())

#-------------------------------------------------------------------------------------------

# with open("myfile.txt","w") as f:
#     f.write("amit\n")
#     f.write("mahesh\n")
#     f.write("suresh\n")
#     print("filed closed",f.closed)
# print("filed closed",f.closed)

#-------------------------------------------------------------------------------------------

# with open("myfile.txt","r") as f:
#     content=f.read()
#     print(content)

#-------------------------------------------------------------------------------------------

# f1=open("mahesh.jpg","rb")
# f2=open("mahesh_copy.jpg","wb")
# data=f1.read()
# f2.write(data)
# print("New Image is available with the name:")

#-------------------------------------------------------------------------------------------

# import csv
# f=open("student.csv","a",newline="")
# a=csv.writer(f)
# # a.writerow(["studentid","name","marks","mobile_no"])

# #-------------------------------------------------------------------------------------------

# import csv
# f=open("student.csv","a",newline="")
# a=csv.writer(f)
# studentid=input("enter the student id:")
# name=input("enter the name:")
# marks=input("enter the marks:")
# mobile_no=input("enter the mobile number:")
# a.writerow([studentid,name,marks,mobile_no])
# print("student record added successfully")

#-------------------------------------------------------------------------------------------


import csv
f=open("student_data.csv","a",newline="")
a=csv.writer(f)
a.writerow(["rolI_no","name","mobile_no","p1","p2","p3","total","percentage","email","result"])
studentid=input("enter the roll_no:")
name=input("enter the name:")
mobile_no=input("enter the mobile number:")
p1=input("enter the paper 1 marks:")
p2=input("enter the paper 2 marks:")
p3=input("enter the paper 3 marks:")
email=input("enter the email:")
if p1>=40 and p2>=40 and p3>=40:
    result="pass"
    print("your pass")
else:
    result="fail"
    print("your fail")
a.writerow(["rolI_no","name","mobile_no","p1","p2","p3","total","percentage","email","result"])
print("student record added successfully")
