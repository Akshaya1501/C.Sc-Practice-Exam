
'''
#WAP TO ENTER N ELEMENT OF INTEGERS AND COUNT TOTAL PERFECT NUMBERS.

L=[]

N=int(input("Enter How many number of elements you want to enter"))

print("Enter ", N, " Elements")


for i in range(N):
    print("Enter number : ",i+1)
    num=int(input())
    L.append(num)

p=0

for i in L:
    s=0
    for j in range(1,i//2+1):
        if i%j==0:
            s=s+j
            
    if s==i:
        p=p+1

print("Total number of Perfect elements  are ",p)

'''


#WAP TO DISPLAY ALL PERFECT NUMBERS BETWEEN 1 TO N WHERE N IS ENTERED BY USER



N=int(input("Enter How many number of elements you want to enter"))


for i in range(1,N+1):
    
    s=0
    for j in range(1,i):
        if i%j==0:
            s=s+j
            
    if s==i:
        print(i)
   





