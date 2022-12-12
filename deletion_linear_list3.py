#WAP to delete all the occurance of the number in a list

def  deletion_Linear_List(L1,num):
    print(L1)
    if (num in L1):
        c=L1.count(num)
        print(c)
        for i in range(c):
            L1.remove(num)
    else:
        print("Number does not exists to delete")
    print(L1)

#_main_
N=int(input("Enter how many number of elements you want to enter"))
L=[]
for i in range(1,N+1):
    elem=int(input("Enter element"))
    L.append(elem)
num=int(input("Enter number to delete"))
deletion_Linear_List(L,num)
