#WAP to create nested linear list and  access specific elements in list

def nested_Linear_List2(L1,L2,L3):
    L1.append(L2)
    print(L1)
    L1[2].append(L3)
    print(L1,"\n\n\n")
    
    #Accessing specific element
    print("L1[0]  :  ",L1[0])
    print("L1[2]:    ",L1[2])
    print("L1[2][0]  :  ",L1[2][0])
    print("L1[2][2]  : ",L1[2][2])
    print("L1[2][2][1]  : ", L1[2][2][1])
    

#_main_
N=int(input("Enter number of elements you want to enter for List1"))
A=[]
for i in range(1,N+1):
    elem=int(input("Enter element"))
    A.append(elem)
N=int(input("Enter how many number of elements you want to enter for List2"))
B=[]
for i in range(1,N+1):
    elem=int(input("Enter element"))
    B.append(elem)
N=int(input("Enter how many number of elements you want to enter for List3"))
C=[]
for i in range(1,N+1):
    elem=int(input("Enter element"))
    C.append(elem)
nested_Linear_List2(A,B,C)
