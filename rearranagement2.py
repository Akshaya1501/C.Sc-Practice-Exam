#WAP to rearrange the element in a list as per the following
#input
#2  4  6  1  8  9  3  10  12  16
#output
#9  3  10  12  16  2  4  6  1  8




def  rearrangement_List(L1):
    '''
    print("Original list ")
    print(L1)
    print("List after rearrengement")
    for i in range(0,len(L1)//2):
        L1[i],L1[i+len(L1)//2]=L1[i+len(L1)//2],L1[i]
    '''
    # or
    #global N
    #L1=L1[N//2:]+L1[0:N//2]
    print(L1)
   

#_main_
N=int(input("Enter how many number of elements you want to enter"))
L1=[]
for i in range(1,N+1):
    elem=int(input("Enter element"))
    L1.append(elem)

rearrangement_List(L1)
