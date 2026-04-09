# import re
# count=0
# pattern = re.compile("function")
# matcher=pattern.finditer("A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.")
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurence: ",count)

#-----------------------------------------------------------------------------------------------------------------------

# import re
# count=0
# matcher = re.finditer("Hi","HiHiHiHi")
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurence: ",count)

#-----------------------------------------------------------------------------------------------------------------------
# import re  
# obj = input("enter any charecter")  
# objmatch=re.finditer(obj,"a7b @k9z")  
# #print(objmatch)  
# for match in objmatch:  
#     print(match.start(),"...",match.end(),"...",match.group())

#-----------------------------------------------------------------------------------------------------------------------

# import re
# a = input("enter string to perform match opration :")
# mtch = re.match(a,'pyhton is very important language')
# print(mtch)
# if mtch!=None:
#     print("match found at begining level of the string")
#     print(mtch.strart()," ",mtch.end())
# else:
#     print("match not found at the beginig level:")
    
#-----------------------------------------------------------------------------------------------------------------------

# import re
# a = input("enter string to perform match opration :")
# mtch = re.fullmatch(a,'pyhton is very important language')
# print(mtch)
# if mtch!=None:
#     print("match found at begining level of the string")
#     print(mtch.strart()," ",mtch.end())
# else:
#     print("match not found")

#-----------------------------------------------------------------------------------------------------------------------

#search() function
#if the match is found anywhere imn the string then it return object else it will return None

# import re
# a= input("enter the string to perform match operation :")
# mtch=re.search(a,"pyhton is very important language")
# print(mtch)
# if mtch!=None:
#     print("match found at begining level of the string")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("match not found")

#-----------------------------------------------------------------------------------------------------------------------

# import re
# a= input("enter the string to perform match operation :")
# f=open("paragraph.txt","r")
# mtch=re.search(a,f.read())
# print(mtch)
# if mtch!=None:
#     print("match found at begining level of the string")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("match not found")

#-----------------------------------------------------------------------------------------------------------------------

#Substitute 
#sub()
# this function performs substitution or replacement re.sub(expression ,replacement,string)

# import re
# obj=re.sub('[a-zA-Z]','X','2345 ABCD Fabc deff')
# print(obj)

#-----------------------------------------------------------------------------------------------------------------------

# import re
# mo=input("enter the mobile number :")
# obj=re.fullmatch("[0-9]\d{9}",mo)
# if obj!=None:
#     print("valid mobile number")
# else:
#     print("invalid mobile number")

#-----------------------------------------------------------------------------------------------------------------------

# import re
# s=input("enter the mail id:")
# obj=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if obj!=None:
#     print("valid mail id")
# else:
#     print("invalid mail id")

#-----------------------------------------------------------------------------------------------------------------------


