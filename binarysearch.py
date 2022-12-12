#WAP TO SEARCH ELEMENT USING BINARY SEARCH            
def binary_search(alist, num):           
    beg = 0
    end = len(alist)-1
    while (beg <= end):
        mid = (beg + end)//2
        if(num==alist[mid]):
            return True
        elif (num<alist[mid]):
            end = mid-1
        else:
            beg = mid + 1        
    return False
# _main_
N=int(input("Enter how many number of elements "
            "you want to enter"))
L=[]
for i in range(1,N+1):
    elem=int(input("Enter element"))
    L.append(elem)
L.sort()
num=int(input("Enter element to search"))
  
if binary_search(L, num): 
    print("Found") 
else: 
    print("Not Found") 
