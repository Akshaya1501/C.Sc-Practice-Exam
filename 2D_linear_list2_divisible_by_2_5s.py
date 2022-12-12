#------------------------------------------------------------------------------
#                     DATA STRUCTURE WITH LINEAR LIST - I
#------------------------------------------------------------------------------

#WAP to create a 2D Linear List and display  elements divisible by 2 and 5

#1 2 3
#4 5 6
#7 8 9



def TwoD_Linear_List2(L1):
        
    for i in range(0,R):        
        for j in range(0,C):
            print(L1[i][j], end="\t")            
        print("\n")
   
    
    print("Elements Divisible by 2 and 5 are")
    for i in range(0,R):            
        for j in range(0,C):
            if (L1[i][j]%2==0 and L1[i][j]%5==0):
                print(L1[i][j], end="  ") 
            else:
                print("* ",end="  ")
                
        print("\n")

    

#_main_
R=int(input("Enter number of rows"))
C=int(input("Enter number of cols"))
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
