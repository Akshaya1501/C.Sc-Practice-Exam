#WAP to create a 2D Linear List                                        
#(input and output all the elements in 2D List)
def TwoD_Linear_List2(L1):        
    for i in range(0,R):        
        for j in range(0,C):
            print(L1[i][j], end="\t")            
        print("\n")
    if R==C:
        print("Diagonal Elements are")
        for i in range(0,R):            
            for j in range(0,C):
                if i==j or i+j==R-1:
                    print(L1[i][j], end="  ") 
                else:
                    print("",end="  ")                
            print("\n")
    else:
        print("Diagonal Elements can not be displayed")   

#_main_
R=int(input("Enter number of rows"))
C=int(input("Enter number of cols"))
if R==C:
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
    print("Diagonal Elements can not be displayed")

    
