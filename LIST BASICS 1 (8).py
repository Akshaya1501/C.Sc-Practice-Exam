
#WAP TO ENTER N ELEMENTS OF INTEGER TYPE AND REARRANGE ELEMENTS AS PER THE
#FOLLOWING.
#IF INPUT IN LIST L1 IS :
#10  12  5  7  8  9  3  2  13  15
#THEN AFTER REARRANGEMENT CONTENT OF LIST L2 SHOULD BE :
#10  12  8  2  5  7  9  3  13  15

'''
L1=[]

N=int(input("How many elements you want to enter"))

print("Enter :",N," Elements")

for i in range(N):
    print("Enter Element Number : ",i+1)
    num=int(input())
    L1.append(num)


L2=[0]*10

j=0

for i in range(N):
    if L1[i]%2==0:
        L2[j]=L1[i]
        j=j+1

for i in range(N):
    if L1[i]%2==1:
        L2[j]=L1[i]
        j=j+1

print("After rearrangement the elements in L2 are :", L2)



#WAP TO ENTER N ELEMENTS OF INTEGER TYPE AND REARRANGE ELEMENTS AS PER THE
#FOLLOWING.
#IF INPUT IN LIST L1 IS :
#10  12  5  7  8  9  3  2  13  15
#THEN AFTER REARRANGEMENT CONTENT OF LIST L2 SHOULD BE :
#10  12  8  2  15 13  3  9  7  5

L1=[]

N=int(input("How many elements you want to enter"))

print("Enter :",N," Elements")

for i in range(N):
    print("Enter Element Number : ",i+1)
    num=int(input())
    L1.append(num)

print("Before Rearrangement The list will be :", L1)

L2=[0]*N

j=0

for i in range(N):
    if L1[i]%2==0:
        L2[j]=L1[i]
        j=j+1

for i in range(-1,-(N+1),-1):
    if L1[i]%2==1:
        L2[j]=L1[i]
        j=j+1   

print("After Rearrangement The list will be :", L2)



#WAP TO ENTER N ELEMENTS OF INTEGER TYPE AND SORT THE ELEMENTS IN ASCEDNING ORDER
#USING BUBBLE SORT

L1=[]

N=int(input("How many elements you want to enter"))

print("Enter :",N," Elements")

for i in range(N):
    print("Enter Element Number : ",i+1)
    num=int(input())
    L1.append(num)

print("Before Rearrangement The list will be :", L1)


for i in range(N-1):

    for j in range(0,N-i-1):
        
        if L1[j]>L1[j+1]:
            
            L1[j],L1[j+1]=L1[j+1],L1[j]

print("After sorting elements in the list are   ;",L1)


'''


#WAP TO ENTER N ELEMENTS OF INTEGER TYPE AND SORT THE ELEMENTS IN DESCENDING ORDER
#USING BUBBLE SORT

L1=[]

N=int(input("How many elements you want to enter"))

print("Enter :",N," Elements")

for i in range(N):
    print("Enter Element Number : ",i+1)
    num=int(input())
    L1.append(num)

print("Before Rearrangement The list will be :", L1)


for i in range(N-1):

    for j in range(0,N-i-1):
        
        if L1[j]<L1[j+1]:
            
            L1[j],L1[j+1]=L1[j+1],L1[j]

print("After sorting elements in the list are   ;",L1)


