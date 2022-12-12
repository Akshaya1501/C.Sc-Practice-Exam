#WAP TO ENTER N ELEMENTS OF INTEGER TYPE AND REARRANGE ELEMENTS AS PER THE
#FOLLOWING.
#IF INPUT IN LIST L1 IS :
#10  12  45  67  8  9  34  23  3  5
#THEN AFTER REARRANGEMENT CONTENT OF LIST L1 SHOULD BE :
#12  10  67  45  9  8  23  34  5  3
'''

L1=[]

N=int(input("How many elements you want to enter"))

print("Enter :",N," Elements")

for i in range(N):
    print("Enter Element Number : ",i+1)
    num=int(input())
    L1.append(num)

print("Before Rearrangement List Elements are :",L1)


for i in range(0,N-1,2):
    L1[i],L1[i+1]=L1[i+1],L1[i]


print("After Rearrangement List Elements are :",L1)


'''

#WAP TO ENTER N ELEMENTS OF INTEGER TYPE AND REARRANGE ELEMENTS AS PER THE
#FOLLOWING.
#IF INPUT IN LIST L1 IS :
#10  12  45  67  8  9  34  23  3  5
#THEN AFTER REARRANGEMENT CONTENT OF LIST L1 SHOULD BE :
#9  34  23  3  5  10  12  45  67  8



L1=[]

N=int(input("How many elements you want to enter"))

print("Enter :",N," Elements")

for i in range(N):
    print("Enter Element Number : ",i+1)
    num=int(input())
    L1.append(num)

print("Before Rearrangement List Elements are :",L1)


for i in range(0,N//2):
    L1[i],L1[i+(N//2)]=L1[i+(N//2)],L1[i]


print("After Rearrangement List Elements are :",L1)


