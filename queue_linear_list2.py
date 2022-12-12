#WAP to perform the following operation in a Queue using List
 #          1. Insert      2. Delete   3. Display   4. exit

from collections import deque

def Insert(queue,item):
    global front,rear
    queue.append(item)
    if(front==None):
        front=rear=0
    else:
        rear=rear+1

def Delete(queue):
    global front,rear
    if front==None:
        return None
    else:
        item=queue.popleft()
        rear=rear-1
        if(front>rear):
            front=rear=None
        return item

def Display(queue):
    global front,rear
    print("front :",front," rear :",rear)
    if front==None:
        print("Underflow Queue is empty can not display")
    else:
        for i in range(front,rear+1):
            print (queue[i], end =" >")

#_main_
Queue=deque([])
front=rear=None
ans='y'
while(ans=='y'):
    print("Queue Operations")
    print("Press 1 to Insert")
    print("Press 2 to Delete")
    print("Press 3 to Display")
    print("Press 4 to exit")
    ch=int(input("Enter your choice"))
    if (ch==1):
        item=int(input("Enter Item Value"))
        Insert(Queue,item)
    elif(ch==2):
        item=Delete(Queue)
        if (item==None):
            print("Queue is Empty, Can not delete")
        else:
            print("Deleted item is ",item)
    elif(ch==3):
        Display(Queue)
    elif(ch==4):
        break
    else:
        print("Invalid choice")
        
    ans=input("Do you wish to continue")
    
    

    
    



