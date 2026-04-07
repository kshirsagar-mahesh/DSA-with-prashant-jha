# #WAP to demonstrate  a game "tower of honai"
# import sys

# class TowerOfHanoi:
#     def __init__(self, disks):
#         self.disks = disks
#         self.towers = [[], [], []]

#         # Initialize source tower
#         for i in range(disks, 0, -1):
#             self.towers[0].append(i)

#         print("Initial State:", self.towers)

#         # Start solving
#         self.move(disks, 0, 2, 1)

#     def move(self, disks, source, destination, helper):
#         if disks == 1:
#             self.towers[destination].append(self.towers[source].pop())
#             print(self.towers)
#         elif disks > 1:
#             self.move(disks - 1, source, helper, destination)
#             self.move(1, source, destination, helper)
#             self.move(disks - 1, helper, destination, source)
#         else:
#             print("Invalid number of disks")
#             sys.exit()


# # Driver code
# n = int(input("Enter number of disks: "))
# TowerOfHanoi(n)












import time
class Tower:
    def __init__(self):
        print("welcome to tower of hanoi")
        print()
        print("given problem A=[3,2,1]      B=[]     C=[]")
        print()
        print("Expected Output A=[]     B=[]     C=[3,2,1]")
        self.A=[]
        self.B=[]
        self.C=[]

    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower A\n")

    def pass1(self):
        self.temp=self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A)
        print("Pass One Completed========================================\n")

    def pass2(self):
        self.temp=self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A)
        print("Pass Two Completed========================================\n")

    def pass3(self):
        self.temp=self.A.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A)
        print("Pass Three Completed========================================\n") 

    def pass4(self):
        self.temp=self.B.pop(1)
        self.C.append(self.temp)
        time.sleep(3)
        print("B=",self.B)
        print("Pass Four Completed========================================\n")

    def pass5(self):
        self.temp=self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("B=",self.B)
        print("Pass Five Completed========================================\n")

    def pass6(self):
        self.temp=self.C.pop(2)
        self.A.append(self.temp)
        time.sleep(3)
        print("C=",self.C)
        print("Pass Six Completed========================================\n")

    def pass7(self):
        self.temp=self.C.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("C=",self.C)
        print("Pass Seven Completed========================================\n")

t=Tower()
t.tower(3)
t.tower(2)
t.tower(1)
t.pass1()
t.pass2()
t.pass3()
t.pass4()
t.pass5()
t.pass6()
t.pass7()