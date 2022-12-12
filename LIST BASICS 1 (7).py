
'''
#WAP TO ENTER N ELEMENTS OF INTEGER TYPE AND REARRANGE ELEMENTS AS PER THE
#FOLLOWING.
#IF INPUT IN LIST L1 IS :
#10  12  45  67  8  9  34  23  3  5
#THEN AFTER REARRANGEMENT CONTENT OF LIST L1 SHOULD BE :
#5   3  23  34  9  8  67  45  12  10



L1=[]

N=int(input("How many elements you want to enter"))

print("Enter :",N," Elements")

for i in range(N):
    print("Enter Element Number : ",i+1)
    num=int(input())
    L1.append(num)

print("Before Rearrangement List Elements are :",L1)


for i in range(0,N//2):
    L1[i],L1[i+(N-i-1)]=L1[i+(N-i-1)],L1[i]


print("After Rearrangement List Elements are :",L1)








#WAP TO ENTER N ELEMENTS OF INTEGER TYPE AND REARRANGE ELEMENTS AS PER THE
#FOLLOWING.
#IF INPUT IN LIST L1 IS :
#10  12  5  7  8  9  3  2  13  15
#THEN AFTER REARRANGEMENT CONTENT OF LIST L1 SHOULD BE :
#20  24  15 21 16  27 9 4  39  45



L1=[]

N=int(input("How many elements you want to enter"))

print("Enter :",N," Elements")

for i in range(N):
    print("Enter Element Number : ",i+1)
    num=int(input())
    L1.append(num)

print("Before Rearrangement List Elements are :",L1)



for i in range(N):
    if  L1[i]%2==0:
        L1[i]=L1[i]*2
    else:
        L1[i]=L1[i]*3
    

print("After Rearrangement List Elements are :",L1)




#WAP TO ENTER N ELEMENTS OF INTEGER TYPE AND REARRANGE ELEMENTS AS PER THE
#FOLLOWING.
#IF INPUT IN LIST L1 IS :
#10  12  5  7  8  9  3  2  13  15
#THEN AFTER REARRANGEMENT CONTENT OF LIST L2 SHOULD BE :
#10  12  8  2  15  13  3  9  7  5


L1=[]

N=int(input("How many elements you want to enter"))

print("Enter :",N," Elements")

for i in range(N):
    print("Enter Element Number : ",i+1)
    num=int(input())
    L1.append(num)

print("Before Rearrangement List Elements are :",L1)


L2=[0]*N
'''
j=0

for i in range(N):
    if  L1[i]%2==0:
        L2[j]=L1[i]
        j=j+1

for i in range(-1,-(N+1),-1):
    if  L1[i]%2==1:
        L2[j]=L1[i]
        j=j+1  
'''

#ALTERNATE
j,k=0,N-1
for i in range(N):
    if  L1[i]%2==0:
        L2[j]=L1[i]
        j=j+1
    else:
        L2[k]=L1[i]
        k=k-1


print("After Rearrangement List Elements are :",L2)


#WAP TO ENTER N ELEMENTS OF INTEGER TYPE AND REARRANGE ELEMENTS AS PER THE
#FOLLOWING.
#IF INPUT IN LIST L1 IS :
#10  12  5  7  8  9  3  2  13  15
#THEN AFTER REARRANGEMENT CONTENT OF LIST L2 SHOULD BE :
#10  12  8  2  5  7  9  3 13 15


L1=[]

N=int(input("How many elements you want to enter"))

print("Enter :",N," Elements")

for i in range(N):
    print("Enter Element Number : ",i+1)
    num=int(input())
    L1.append(num)

print("Before Rearrangement List Elements are :",L1)


L2=[0]*10

j=0
for i in range(N):
    if  L1[i]%2==0:
        L2[j]=L1[i]
        j=j+1

for i in range(N):
    if  L1[i]%2==1:
        L2[j]=L1[i]
        j=j+1  

print("After Rearrangement List Elements are :",L2)

'''



#WAP TO ENTER N ELEMENTS OF INTEGER TYPE AND REARRANGE ELEMENTS AS PER THE
#FOLLOWING.
#IF INPUT IN LIST L1 IS :
#10  12  5  7  8  9  3  2  13  15
#THEN AFTER REARRANGEMENT CONTENT OF LIST L2 SHOULD BE :
#2  3  5  7  8  9  10  12  13  15


