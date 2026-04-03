# list=["mahesh","maruti","siddharth","om",987654321,"prashant"]
# print(list[0]) # mahesh
# print(list[1]) # maruti
# print(type(list)) # <class 'list'>
# print(list[0:3]) # ['mahesh', 'maruti', 'siddharth']
# print(list[3:]) # ['om', 987654321, 'prashant']
# print(list[:3]) # ['mahesh', 'maruti', 'siddharth']
# print(list[::-1]) # ['prashant', 987654321, 'om', 'siddharth', 'maruti', 'mahesh']
# print(list[0:6:2]) # ['mahesh', 'siddharth', 'prashant']

# print(list[1:5:2]) # ['maruti', 'om']

# list=[1,2,3,4,5]


#=====================================================================================================

# list=["mahesh","maruti","siddharth","om",987654321,"prashant"]

# if "mahesh" in list:
#     print("yes")
# else:
#     print("no") 


# list.append("harsh")
# list.append("laxman")
# print(list)

# list.insert(2,"harsh")
# print(list) # ['mahesh', 'maruti', 'harsh', 'siddharth', 'om', 987654321, 'prashant']

# list.remove("harsh")
# print(list) #  ['mahesh', 'maruti', 'siddharth', 'om', 987654321, 'prashant']

# list.copy()
# print(list) # ['mahesh', 'maruti', 'siddharth', 'om', 987654321, 'prashant']

# list.clear()
# print(list) # []
#=====================================================================================================

# my_list = [['prashant','jha'],[85.56],[440022,"yyy"]]
# print("example of mullti dimensional list : ",my_list) # example of multi dimensional list :  [['prashant', 'jha'], [85.56], [440022, 'yyy']]
# print(my_list[0]) # ['prashant', 'jha']
# print(my_list[0][0]) # prashant
# print(my_list[1]) # [85.56]
# print(my_list[1][0]) # 85.56
# print(my_list[2]) # [440022, 'yyy']
# print(my_list[2][0]) # 440022   
# print(my_list*2) # [['prashant', 'jha'], [85.56], [440022, 'yyy'], ['prashant', 'jha'], [85.56], [440022, 'yyy']]

# list1=["prashant","jha"]

# list2=[85.56]

# print(list1+list2) # ['prashant', 'jha', 85.56]


# list = [1,2,3,4,5]
# del list # it will delete the list and it will not return any value and it will not print anything because the list is deleted and it will give an error if we try to print the list after deleting it.
#del list[3] # it will delete the element at index 3 which is 4
# print(list)

# del is used to delete the list but it will not return any value and it will not print anything because the list is deleted and it will give an error if we try to print the list after deleting it.


# list = [1,2,3,4,5]
# list.clear()
# print(list) # [] it will clear the list and it will return an empty list because all the elements are removed from the list.


# list = [1,2,3,4,5]
# list.reverse()
# print(list) # [5, 4, 3, 2, 1] it will reverse the list and it will return the reversed list.


# list=[8,5,7,37,9,1,3,6,4,2]
# list.sort()
# print(list)                     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 37] it will sort the list in ascending order and it will return the sorted list.
# list.sort(reverse=True)
# print(list)                 # [37, 9, 8, 7, 6, 5, 4, 3, 2, 1] it will sort the list in descending order and it will return the sorted list.


#make should be homogeneous list because it will give an error if we try to sort a heterogeneous list because it will not be able to compare the elements of the list and it will give an error.




# my_list = [1,2,3,4,5]
# new_list = my_list
# print(id(my_list)) 
# print(id(new_list))

# my_list[0] = 10
# print(my_list) # [10, 2, 3, 4, 5]
# print(new_list) # [10, 2, 3, 4, 5]


# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print(arr[i],end=" ")


# a=[1,2,3,4,5,6]
# print(a[3:0:-1]) # [4, 3, 2] it will print the elements from index 3 to index 0 in reverse order

#=====================================================================================================


#TUPLE  


# my_tuple = ("prashant","ashish","Rahul","sandip","komal","ankush" ,"rajesh",23,3.15,77,"sandip")
# print(my_tuple) # ('prashant', 'ashish', 'Rahul', 'sandip', 'komal', 'ankush', 'rajesh', 23, 3.15, 77, 'sandip')   
# print(type(my_tuple)) # <class 'tuple'> it will return the type of the variable which is tuple.

# my_tuple[2]="sunil"
# print(my_tuple) # it will give an error because we cannot change the elements of a tuple because it is immutable.

#MCQ's


# init_tuple = 'a','b'
# init_tuple1 = ('a','b')
# print(id(init_tuple))
# print(id(init_tuple1))
# print(init_tuple==init_tuple1) 

# init_tuple = 'a','b'
# init_tuple1 = ('a','b')
# print(init_tuple+init_tuple1)

# init_tuple = ('pyhon')*3
# print(type(init_tuple)) # <class 'str'> it will print the string 'pyhon' three times because we are multiplying the string by 3.

# init_tuple = ('pyhon',)*3
# print(type(init_tuple)) # <class 'tuple'> it will print the tuple ('pyhon', 'pyhon', 'pyhon') because we are multiplying the tuple by 3.

# init_tuple = ('pyhon',)*3
# init_tuple[0]=2
# print(init_tuple) # it will give an error because we cannot change the elements of a tuple because it is immutable.

# init_tuple = ((1,2),)*7
# print(len(init_tuple[3:8])) # 4 it will print the length of the tuple from index 3 to index 7 because we are slicing the tuple from index 3 to index 7 and it will return a new tuple with the elements from index 3 to index 7 and then we are finding the length of that new tuple which is 4.

# names=[4,2,5,6,8,2]
# for i in names:
#     print(i)

# a=[4,0,2,5,0,1]
# for i in a:
#     if i==0:
#         a.remove(i)
#         a.append(i)
# print(a) # [4, 2, 5, 1, 0, 0] it will remove the first occurrence of 0 and then it will append 0 at the end of the list and then it will remove the second occurrence of 0 and then it will append 0 at the end of the list and then it will return the modified list.


# a=[1,2,2,3,4,4,5]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)


# a=[1,2,3]
# b=[2,3,4]
# c=[3,4,5]
# for i in a:
#     if i in b and i in c:
#         print(i) # 3 it will print the common element which is 3 because 3 is present in all three lists a, b and c.




# n=int(input("enter the array size :"))
# arr=[]
# for i in range(n):
#     val=int(input("enter the value :"))
#     arr.append(val)
# sum=0
# print(arr)
# for i in range (n):
#     if i+1 in range(n):
#         sum+=abs(arr[i]-arr[i+1])
# print(sum)




# for i in range(1,5):
#     if i==3:
#         break
#     print(i)

# for i,j in zip(range(1,6), range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)


# name="prashant*is*a*good*programmer"
# new_str=""
# val=""
# for i in name:
#     if i!="*":
#         new_str+=i
#     else:
#         val+=i
# print(new_str)
# print(str(val+new_str))


# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*c/d)
# print(a+(b*c)/d)


# x=['a','b','c']
# y=['a','b','c']
# z=[1,2,3,4]
# print(x==y) # True it will compare the values of the lists x and y and it will return True because the values of the lists x and y are same.
# print(x==z) # False it will compare the values of the lists x and z and it will return False because the values of the lists x and z are different.
# print(x!=z) # True it will compare the values of the lists x and z and it will return True because the values of the lists x and z are different.


# a = "listen"
# b = "silent"
# if sorted(a) == sorted(b):
#     print("anagrams.")
# else:
#     print(" not anagrams.")

# str1="this is a sentence"
# count=1
# for i in str1:
#     if i==" ":
#         count+=1
# print(count)


arr=[1,2,3,4]
arr1=[]
i=0
for i in arr:
    print(i*i+1)