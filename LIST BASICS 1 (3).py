'''
#WAP TO ENTER N ELEMENT OF INTEGERS AND FIND THE GREATEST ONE.
L=[]

N=int(input("Enter How many number of elements you want to enter"))

for i in range(N):
    num=int(input("Enter number"))
    L.append(num)


max=L[0]

for i in L:
    if i>max:
        max=i

print("The greatest value is ",max)




#Alternate

L=[]

N=int(input("Enter How many number of elements you want to enter"))

for i in range(N):
    num=int(input("Enter number"))
    L.append(num)

print("The greatest number is ", max(L))



#WAP TO ENTER N ELEMENT OF INTEGERS AND FIND THE SMALLEST ONE.

L=[]

N=int(input("Enter How many number of elements you want to enter"))

for i in range(N):
    num=int(input("Enter number"))
    L.append(num)

min=L[0]
for i in range(1,N):
    if L[i]<min:
        min=L[i]

print("The smallest value is ", min)


#Alternate

L=[]

N=int(input("Enter How many number of elements you want to enter"))

for i in range(N):
    num=int(input("Enter number"))
    L.append(num)


print("The smallest value is ", min(L))
        


L=[]

N=int(input("Enter How many number of Names you want to enter"))

for i in range(N):
    num=input("Enter Name")
    L.append(num)


print("The smallest value is ", min(L))




#WAP TO ENTER N ELEMENT OF INTEGERS AND FIND THE AVERAGE VALUES OF ALL THE ELEMENTS

L=[]

N=int(input("Enter How many number of elements you want to enter"))

for i in range(N):
    num=int(input("Enter number"))
    L.append(num)


print("The average value is ",sum(L)/len(L))















