#WAP to enter N elements in a List and  insert an element at a specific position

def insertion_Linear_List(L1,num,pos):
    L1.append(0)
    print(L1)
    for i in range(len(L1)-1,pos-1,-1):
      L1[i]=L1[i-1]
    L1[pos-1]=num
    print(L1)

#_main_
L=[]
N=int(input("Enter how many number of elements you want to enter"))

for i in range(1,N+1):
    elem=int(input("Enter element"))
    L.append(elem)
    
Num=int(input("Enter number to insert"))

Check=True
while(Check):
    pos=int(input("Enter position to insert (values should be beween 1 to N)"))
    if pos<=0 or pos>len(L):
        Check=True
    else:
        Check=False
insertion_Linear_List(L,Num,pos)
