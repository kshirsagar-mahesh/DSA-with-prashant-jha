# #========================================================Dictionary=========================================================

# # mydict={
# #     101:"prashant", 
# #     102:"ashish",
# #     103: "mohini",
# #     104:"triveshi",
# #     101:"ashish",
# #     104:"ashish"
# # }
# # print(mydict)


# # with the help of pop() we can remove any key,value pair.
# # mydict.pop(102)
# # print(mydict)

# # with the help of key we have to print values 
# # a=mydict[101]
# # print(a)


# # mydict[102]="sandip" # we will replace old value by new value 
# # print(mydict)

# #only print keys 
# # for x in mydict:
# #     print(x)

# # #only print values 
# # for x in mydict.values():
# #     print(x)

# # #print both keys and values 
# # for x in mydict.items():
# #     print(x) 

# # #if i have psto add new kay and value pair in my ddictionary 
# # mydict["mobile_no"]=1234567890
# # print(mydict)

# # a={(1,2):1,(2,3):2,(4,5):3}
# # print(a[4,5])

# # a={'a':1,"b":2,"c":3}
# # print(a['a','b']) # error bcz two keys not get output at a time

# # arr={}
# # arr[1]=1
# # arr['1']=2
# # arr[1]+=1
# # print(arr)
# # sum=0
# # for k in arr:
# #     sum+=arr[k]
# # print(sum)


# # my_dict={}
# # my_dict[(1,2,4)] =8
# # my_dict[(4,2,1)] =10
# # my_dict[(1,2)] =12
# # sum=0
# # for k in my_dict:
# #     sum+=my_dict[k]
# # print(sum)
# # print(my_dict)

# # box={}
# # jars={}
# # crates={}
# # box["biscuit"]=1
# # box["cake"]=3
# # jars["jam"]=4
# # crates["box"]=box
# # crates["jars"]=jars
# # print(len(crates[box]))  #value error

# # dict = {'c':97, 'a':96, 'b':98}
# # for _ in sorted(dict):
# #     print(dict[_])   sorted by the alphabetically  when variable is not used then _ can be used


# # rec = {"name":"python","age":"20"}
# # r=rec.copy()
# # print(id(r))
# # print(id(rec))   copy () not copy the address it copies values if assing then it copy the address


# # rec = {"name":"python","age":"20","address":"NJ"}
# # id1=id(rec)
# # print(id(id1))
# # del rec
# # rec = {"name":"python","age":"20","address":"NJ"}
# # id2=id(rec)
# # print(id1==id2)
# # print(id(id1))

# # def min_key(d):
# #     min_k = None
# #     min_v = float('inf')
    
# #     for key, value in d.items():
# #         if value < min_v:
# #             min_v = value
# #             min_k = key
            
# #     return min_k

# # # Sample Input
# # data = {"X": 20, "Y": 10, "Z": 30}

# # # Output
# # print(min_key(data))

# #====================================================================================================================

# # nested for loop 

# # for i in range (1,4):
# #     for j in range(1,4):
# #         print(i,end=" ")
# #     print()

# # n=int(input("enter the number of rows :"))
# # for i in range (1,n+1):
# #     for j in range(1,i+1):
# #         print(chr(64+j),end=" ")
# #     print()

# # n = int(input("Enter the number of rows : "))
# # for i in range(1,n+1):
# #     for j in range(1,1+i):
# #         print(j,end=" ")
# #     print()


# # n=int(input("enter the number of rows :"))
# # for i in range (1,n+1):
# #     for j in range(n+2-i):
# #         print("*",end=" ")
# #     print()


# # n=int(input("enter the number of rows :"))
# # for i in range (1,n+1):
# #     for j in range(n+2-i):
# #         print(chr(64+j),end=" ")
# #     print()

# #import time 



# # import time 
# # n=int(input("enter the number of rows :"))
# # for i in range (1,n+1):
# #     print(" "*(n-i),end=" ")
# #     for j in range(1,i+1):
# #         time.sleep(0.5)
# #         print("*",end=" ")
# #     print()


# #==============================================================FUNCTION===================================================

# # types 
# # predefine
# # user_define

# # def msg(): #called function
# #     print("Hello world")

# # msg() #calling function
# # msg()

# #wap to return a muiltiple time f


# def arithmatic():
#     a=int(input("enter the first number :"))
#     b=int(input("enter the second number :"))
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add,sub,mul,div
# result=arithmatic()
# print(result)
# print(type(result))

#how many types of argument we can pass in function 
# 1.positional argument
# 2.keyword argument
# 3.deffault argument
# 4.variable number of argument/ variable length pargument


#-----------------------positional --------------------------
# def login(username,password):
#     if username==password:
#         print("login successfull")
#     else:
#         print("login failed")
#   #  pass # no body  if you want break contineu and pass
# username=input("enter the username :")
# password=input("enter the password :")
# login(username,password)


#-----------------------------keyword-----------------------------

# def login(username,password):
#     if username==password:
#         print("login successfull")
#     else:
#         print("login failed")
# login(username="admin",password="admin") #calling function

#-----------------------------default-----------------------------

# def cityname(city="goa"):
#     print(city)

# cityname("mumbai")
# cityname("pune")
# cityname()

#-----------------------------variable length-----------------------------

# def nameOfCitys(*city):
#     print("City name's=",city)

# nameOfCitys("goa","nagpur","mumbai","pune","nashik")

#-----------------------------variable length-----------------------------

#WAP for menu driven code
# import sys
# def add():
#     val1=int(input("enter the first number :"))
#     val2=int(input("enter the second number :"))
#     print("addition=",val1+val2)
# def sub():
#     val1=int(input("enter the first number :"))
#     val2=int(input("enter the second number :"))
#     print("substraction=",val1-val2)

# def mul():
#     val1=int(input("enter the first number :"))
#     val2=int(input("enter the second number :"))
#     print("Multiplication=",val1*val2)

# def div():
#     val1=int(input("enter the first number :"))
#     val2=int(input("enter the second number :"))
#     print("Division=",val1/val2)

# while True:
#     print("1.addition")
#     print("2.subtraction")
#     print("3.multiplication")
#     print("4.division")
#     print("5.exit")
#     choice=int(input("enter the choice :"))
#     if choice==1:
#         add()
#     elif choice==2:
#         sub()
#     elif choice==3:
#         mul()
#     elif choice==4:
#         div()
#     elif choice==5:
#         sys.exit()



# # 1. rstrip()--> to remove spaces at right hand side
# # 2. lstrip()--> to remove spaces at left hand side
# # 3. strip()--> to remove spaces at both sides  

# programing = input ("enter your programing name:")
# p_name = programing.rstrip()
# if p_name == "python":
#     print(p_name)
# elif p_name == "java":
#     print(p_name)
# elif p_name == "c":
#     print(p_name)
# elif p_name == "c++":
#     print(p_name)
# else:
#     print("invalid programing language")

