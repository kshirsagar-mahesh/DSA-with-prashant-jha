#-------------------------------------reverse list-------------------------------------

# list=[1,2,3,4,5]
# list.reverse()
# print(list) # [5, 4, 3, 2, 1] 
#else method 

# print(list[::-1]) 

#------------------------------------palindrome----------------------------------------------

# list =[1,2,3,4,5]
# if (list)==(list[::-1]):
#     print("list is palindrome.")
# else:
#     print("list is not a palindrome.")


#--------------------------------------common element in two list-----------------------------

#===============================================Class========================================

# class Student:
#     roll_no=101 #data member
    
#     def studentData(self):          # method/member function
#         print("student information")
# obj = Student()
# print(obj.roll_no)
# obj.studentData()

#-----------------------------------------------------------------------------------------------------

# class Demo:
#     def __init__(self):
#             print("I Am Constructor:")
#     def msg(self):
#           print("Hello class!")
# obj1=Demo()
# obj1.msg()
# obj2=Demo()
# obj2.msg

#-----------------------------------------------------------------------------------------------------

# class Hod:
#     def __init__(self,name,age,empid):
#         self.name="prashant"
#         self.age=20
#         self.empid=101
#     def show(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("empid:",self.empid)
# obj=Hod("arjun",45,101)
# obj.show()

#-----------------------------------------------------------------------------------------------------

# class New:
#     def __init__(self):
#         self.a=10

# obj1=New()
# obj2=New()
# obj3=New()
# # obj1.a=20   value change for the perticular object
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#-----------------------------------------------------------------------------------------------------

# class Student:
#     def __init__(self):
#         self.s_name="prashant"
#         self.s_roll_no=101  declare a instance var inside a constructor
        
#     def getdata(self):
#         self.s_mb=2828282828   declaring a instance var inside a instance method

# obj=Student()
# obj.getdata()
# del obj.s_mb              delete the instance variable using obj
# obj.s_branch ="CSE"       adding instance variable by using object
# print(obj.__dict__)

#-----------------------------------------------------------------------------------------------------


# class Student:
#     a=10  #static variable
#     def __init__(self):
#         self.name="prashant"  #instance variable

# obj1=Student()
# obj2=Student()
# obj3=Student()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# Student.a=20

# obj1=Student()
# obj2=Student()
# obj3=Student()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#----------------------------------------------------------------------------------------------------

# import sys

# class CRUD:
#     def __init__(self):
#         print("student management sytem")
#         self.student_id=[]
#         self.student_name=[]
#         self.student_roll_no=[]
#         self.student_city=[]

#     def add_student(self):
#         student_id=int(input("enter the student id:"))
#         student_name=input("enter the student name:")
#         student_roll_no=int(input("enter the student roll no:"))
#         student_city=input("enter the student city:")
#         self.student_id.append(student_id)
#         self.student_name.append(student_name)
#         self.student_roll_no.append(student_roll_no)
#         self.student_city.append(student_city)
#         print("student added successfully")

#     def show_student(self):
#         print(self.student_id)
#         print(self.student_name)
#         print(self.student_roll_no)
#         print(self.student_city)


#     def update_student(self):
#         student_id=int(input("enter the student id:"))
#         if student_id in self.student_id:
#             index=self.student_id.index(student_id)
#             self.student_name[index]=input("enter the new name:")
#             self.student_roll_no[index]=int(input("enter the new roll no:"))
#             self.student_city[index]=input("enter the new city:")
#             print("student updated successfully")
#         else:
#             print("student not found")

#     def delete_student(self):
#         student_id=int(input("enter the student id:"))
#         if student_id in self.student_id:
#             index=self.student_id.index(student_id)
#             del self.student_id[index]
#             del self.student_name[index]
#             del self.student_roll_no[index]
#             del self.student_city[index]
#             print("student deleted successfully")
#         else:
#             print("student not found")                 
# obj1=CRUD()
# while True:
#     print("1.add student")
#     print("2.show student")
#     print("3.update student")
#     print("4.delete student")
#     print("5.exit")
#     choice=int(input("enter the choice:"))
#     if choice==1:
#         obj1.add_student()
#     elif choice==2:
#         obj1.show_student()
#     elif choice==3:
#         obj1.update_student()
#     elif choice==4:
#         obj1.delete_student()
#     elif choice==5:
#         sys.exit()
#     else:
#         print("invalid choice")

#-----------------------------------------------------------------------------------------------------------

#method 

#1.static method

# class Student:
#     def __int__(self,name,roll_no,mob):
#         self.name=name
#         self.roll_no=roll_no
#         self.mob=mob
    
#     def display(self):
#         print(self.name," ",self.roll_no," ",self.mob)

# stud=Student("prashant",101,2828282828)
# stud.display()

#---------------------------------------------------------------------------------------------------------------

# class Student:
#     @staticmethod
#     def get_personal_detail(firstname,lastname):
#         print("your personal details=",firstname,lastname)

#     @staticmethod
#     def contact_detail(mobile,email):
#         print("your contact details=",mobile,email)

# Student.get_personal_detail("prashant","jha")
# Student.contact_detail(282828282,1001)






#===============================================single inheritance==============================================

# class College:
#     def college_name(self):
#         print("Yashawantrao bhonsale institute of technology")

# class Student(College):
#     def student_name(self):
#         print("name:mahesh kshirsagar")
#         print("branch:cse")

# obj=Student()
# obj.college_name()
# obj.student_name()

#-------------------------------------------------------------------------------------------------------------

#=================================multilevel inheritence===================================================


# class College:
#     def college_name(self):
#         print("Yashawantrao bhonsale institute of technology")
    
# class Student(College):
#     def student_name(self):
#         print("name:mahesh kshirsagar")
#         print("branch:cse")

# class Exam(Student):
#     def subject(self):
#         print("subject1:math")
#         print("subject2:science")
#         print("subject3:english")

# obj=Exam()
# obj.college_name()
# obj.student_name()
# obj.subject()

#=========================================================================================================


# class SubMarks:
#     c=int(input("enter the c marks:"))

# class PractMarks:
#     c_pract=int(input("enter the c pract marks:"))

# class Result(SubMarks,PractMarks):
#     def total(self):
#         if self.c>=40 and self.c_pract>=40:
#             print("pass")
#         else:
#             print("fail")

# obj=Result()
# obj.total()


#=============================================Polymorphism===============================================

# class Principal:
#     def role(self):
#         print("Principal = i am managing all activity of college")
    
# class dean:
#     def role(self):
#         print("Dean= i am decision taking person")

# class Hod:
#     def role(self):
#         print("Hod= I have responsibility of teachers and students")
    
# class faculty:
#     def role(self):
#         print("Faculty = I have to complete syllybus successfully")
    
# def func(obj):
#     obj.role()          #calling function

# campus=[Principal(),dean(),Hod(),faculty()]
# for obj in campus:
#     func(obj)   #calling function

#------------------------------------------------------------------------------------------------------------

# class arithmatic:
#     def add(self,a):
#         print(a)

#     def add(self,a,b):
#         print(a+b)

#     def add(self,a,b,c):
#         print(a+b+c)

# obj=arithmatic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)

# class arithmatic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None:
#             print(a+b)
#         elif a!=None and b!=None and c!=None:
#             print(a+b+c)
#         else:
#             print("enter atleast two value")

# obj=arithmatic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)


#----------------------------------------------------------------------------------------------------------

# class Arithmatic:
#     def __init__(self):
#         print("There is no argument")
#     def __init__(self,a):
#         print("There is one argument")
#     def __init__(self,a,b):
#         print("There is two argument")
        
# obj=Arithmatic()
# obj=Arithmatic(10)
# obj=Arithmatic(2,2)


#===============================================Over Rinding================================================


#over riding is support by python

# class Rbi:
#     def home_loan(self):
#         print("home loan = 7.5 % interest rate")

#     def car_loan(self):
#         print("car loan = 1 % interest rate")

# class Sbi(Rbi):
#     def home_loan(self):
#         print("Sbi provided home loan = 6.5 % interest rate")
#         super().home_loan() #using super() you can access parent class
# obj=Sbi()
# obj.home_loan()
#----------------------------------------------------------------------------------------------------------


# class Father:
#     def __init__(self):
#         print("Father = i am allready at brekfast table")

# class Child(Father):
#     def __init__(self):
#         print("Child = i will be late for breakfast")
#         super().__init__()

# obj = Child()

#====================================================THE END======================================