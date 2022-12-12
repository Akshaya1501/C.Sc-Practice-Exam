'''
#WAP TO ENTER N ELEMENT OF INTEGERS AND COUNT TOTAL EVEN ELEMENTS.

L=[]

N=int(input("Enter How many number of elements you want to enter"))

print("Enter ", N, " Elements")


for i in range(N):
    print("Enter number : ",i+1)
    num=int(input())
    L.append(num)

c=0

for i in L:
    if i%2==0:
        c=c+1

print("Total number of Even elements  are ",c)


# WAP TO ENTER N ELEMENT OF INTEGERS AND replace each odd with it's double.

L=[]

N=int(input("Enter How many number of elements you want to enter"))

print("Enter ", N, " Elements")


for i in range(N):
    print("Enter number : ",i+1)
    num=int(input())
    L.append(num)


for i in range(N):
    if L[i]%2!=0:
        L[i]=L[i]*2

print("Total List after manipulation is as follows : \n ",L)

#WAP TO ENTER N ELEMENT OF INTEGERS AND COUNT TOTAL ODD ELEMENTS.

L=[]

N=int(input("Enter How many number of elements you want to enter"))

print("Enter ", N, " Elements")


for i in range(N):
    print("Enter number : ",i+1)
    num=int(input())
    L.append(num)

c=0

for i in L:
    if i%2!=0:
        c=c+1

print("Total number of Odd elements  are ",c)




#WAP TO ENTER N ELEMENT OF INTEGERS AND COUNT TOTAL PRIME ELEMENTS.

L=[]

N=int(input("Enter How many number of elements you want to enter"))

print("Enter ", N, " Elements")


for i in range(N):
    print("Enter number : ",i+1)
    num=int(input())
    L.append(num)

p=0

for i in L:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
            
    if c==2:
        p=p+1

print("Total number of Odd elements  are ",p)



'''
