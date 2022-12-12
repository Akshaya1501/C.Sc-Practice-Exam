#WAP to enter N elements of integer type in a                        
#Linear List and an element of integer type
#and count the occurance of the  element
def Linearsearch(list,n): 
    c=0  
    for i in range(len(list)): 
        if list[i] == n:
            c=c+1            
    return c  
# _main_

N=int(input("Enter how many number of elements "
            "you want to enter"))
L=[]
for i in range(1,N+1):
    elem=int(input("Enter element"))
    L.append(elem)
num=int(input("Enter element to search"))
  
occ=Linearsearch(L, num) 
print("Total number of ", num, "is",occ)
