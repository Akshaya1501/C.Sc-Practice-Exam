#WAP to rearrange the element in a list as per the following
#input
#2  4  6  1  8  9  3  10  12  16
#output
#1  9  3  16  12  10  8  6  4  2

def  rearrangement_List(L1):
    print("Original list ")
    print(L1)
    L2=[]
    '''
    for i in range(10):
        L2.append(0)    
    j=0
    k=len(L1)-1
    print("List after rearrengement")
    for i in range(0,len(L1)):
        if L1[i]%2!=0:
            L2[j]=L1[i]
            j=j+1
        else:
            L2[k]=L1[i]
            k=k-1
     
    
    '''
    for i in range(0,len(L1)):
        if L1[i]%2!=0:
            L2.append(L1[i])
            
    for i in range(len(L1)-1,-1,-1):
        if L1[i]%2==0:
            L2.append(L1[i])
            
    print(L2)
   

#_main_
N=int(input("Enter how many number of elements you want to enter"))
L1=[]
for i in range(1,N+1):
    elem=int(input("Enter element"))
    L1.append(elem)

rearrangement_List(L1)
