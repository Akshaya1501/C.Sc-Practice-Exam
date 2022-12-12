#WAP to create a 2D Linear List and display middle row and middle column elements

#1 2 3
#4 5 6
#7 8 9



def TwoD_Linear_List2(L1):
        
    for i in range(0,R):        
        for j in range(0,C):
            print(L1[i][j], end="\t")            
        print("\n")

    print("Diagonal Elements are")
    for i in range(0,R):            
        for j in range(0,C):
            if i==R//2 or j==C//2:
                print(L1[i][j], end="  ") 
            else:
                print(" ",end="  ")
        print("\n")

    

#_main_
R=int(input("Enter number of rows"))
C=int(input("Enter number of cols"))
if R%2!=0 and C%2!=0:
    A=[]
    for i in range(0,R):
        B=[]
        for j in range(0,C):
            elem=int(input("Enter element"))
            B.append(elem)
        A.append(B)
    print("Calling List")
    TwoD_Linear_List2(A)
    print(A)
else:
    print("Can not display")
