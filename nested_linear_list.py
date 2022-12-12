#WAP to create a nested linear list

def nested_Linear_List(L1,L2,L3):
    
    L1.append(L2)
    print(L1)
    L1.append(L3)
    print(L1)
    

#_main_
A=[]
N=int(input("Enter number of elements you want to enter for List1"))
for i in range(N):
    elem=int(input("Enter element"))
    A.append(elem)
    
B=[]
N=int(input("Enter how many number of elements you want to enter for List2"))
for i in range(1,N+1):
    elem=int(input("Enter element"))
    B.append(elem)
    
C=[]
N=int(input("Enter how many number of elements you want to enter for List3"))
for i in range(1,N+1):
    elem=int(input("Enter element"))
    C.append(elem)
    
nested_Linear_List(A,B,C)
