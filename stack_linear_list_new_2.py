#WAP to perform the following operation in a                   
#Stack using List
#          1. Push
#          2. Pop
#          3. Display
#          4. exit
           

def Push(stk,L1):
    global top
    for i in L1:
        if i%2==0:
            stk.append(i)
            if top==None:
                top=0
            else:
                top=top+1

def Pop(stk):
    global top
    if stk==[]:
        return "Underflow"
    else:
        item=stk.pop()
        if top==0:
            top=None
        else:
            top=top-1
        return item

def Display(stk):
    global top
    if stk==[]:
        print("Underflow stack is empty can not display")
    else:
        for i in range(top,-1,-1):
            if i==top:
                print (stk[i]," <-")
            else:
                print (stk[i])

#_main_
Stack=[]
top=None
ans='y'
while ans.upper()=='Y':
    print("Stack Operations")
    print("Press 1 to Push")
    print("Press 2 to Pop")
    print("Press 3 to Display")
    print("Press 4 to exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        L1=[12,34,56,78,23,45,67,89,80,90]
        Push(Stack,L1)
    elif(ch==2):
        item=Pop(Stack)
        if (item=="Underflow"):
            print("Underflow ! Stack is Empty")
        else:
            print("Popped item is ",item)
    elif(ch==3):
        Display(Stack)
    elif(ch==4):
        break
    else:
        print("Invalid choice")
        
    ans=input("Do you wish to continue")
    
    

    
    

