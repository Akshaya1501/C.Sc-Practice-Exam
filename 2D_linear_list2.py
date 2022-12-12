#WAP to create a 2D Linear List (input and output all              
#the elements in 2D List)
def TwoD_Linear_List2(L1):        
    for i in range(0,R):        
        for j in range(0,C):
            print(L1[i][j], end="  ")            
        print("\n") 
#_main_
R=int(input("Enter number of rows"))
C=int(input("Enter number of cols"))
#SIZE=int(input("Enter the size of 2D List"))
A=[]
for i in range(0,R):
    B=[]
    print("Enter elements for row : ", (i+1))
    for j in range(0,C):
        print("Enter element : ", j+1, end=" ")
        elem=int(input())
        B.append(elem)
    A.append(B)
TwoD_Linear_List2(A)
