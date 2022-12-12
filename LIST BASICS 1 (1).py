#------------------------------------------------------------------------
#                CHAPTER :  11   LIST MANIPULATIONS 1
#------------------------------------------------------------------------

# List is a collection of homogeneous and hetrogeneous elements.

'''
#Creating an empty list:
L=[]

print(L)

#Output
# []


# List of integers

L=[1,2,3,4,5]   

print(L)
#Output
#[1, 2, 3, 4, 5]

# List of float elements

L=[11.1,12.1,13.1,14.1] 

print(L)

#Output
#[11.1, 12.1, 13.1, 14.1]
'''
# List of Hetrogeneous elements

L=[1,"Kartikey",99.9]

print(L)

#Output
#[1, 'Kartikey', 99.9]

print(L[0]," ",L[-1])

#Nested List

#  0     1             2            3 
L=[1,"Kartikey",[99,99.9,99,99,100],"MV1"] #Nested List
#                0   1  2   3   4
#  -4    -3          -2             -1 

print(L)

#Output
#[1, 'Kartikey', [99, 99.9, 99, 99, 100], 'MV1']



#Accessing elements


print(L[2])

# [99, 99.9, 99, 99, 100]


print(L[-1])

#MV1

print(L[2][4], " ", L[-2][-1])

#100   100


print(L[-1][-1])

#1


#using forward indexing

print(L[0])

#Output
#1

print(L[1])

#Output
#Kartikey

print(L[2])
#Output
#[99, 99.9, 99, 99, 100]

#using backward indexing

print(L[-2][-4], " ",L[-2][-1])
#Output
#99.9   100



print(L[-1])

#Output
#MV1


'''
