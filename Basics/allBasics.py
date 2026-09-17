#1. lists

# initialize
'''
list=[1,2,3,4,5]
l2=[]
'''
#indexing
'''
print(list(0)) #its will print 1
print(list(-1))#it will print 5
'''
#oprations
'''
list.append(6)
l2=list.copy()
print(l2)
'''
#take vlaue form the user
'''
z=int(input("how many values you want to enter in the list "))

li=[]

for i in range(z):
    num=input("enter values")
    li.append(num)

print(li)
'''
#join list
'''
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
'''
# how to create nested list and print
'''
xyz=[1,2],[3,4]
print(xyz[1][0])
'''

# take user input for nested list 

'''
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row_list = []  # Create a fresh, empty list for the current row
    for j in range(columns):
        value = input(f"Enter value for row {i+1}, column {j+1}: ")
        row_list.append(value)  # Add the value to the current row
    matrix.append(row_list)  # Add the completed row to the matrix

print("\nYour final 2D list:")
print(matrix)
'''

# 2. Dictionaries

#intilize 
'''
Student={
    "name":"ali",
    "marks":60,
    "section":"A"
    }
print(Student["name"])

'''
#update
'''
Student={
    "name":"ali",
    "marks":60,
    "section":"A"
    }
Student["grade"]="B"
print(Student)
'''
#user input dic
'''
Student={}

name=input("enter the name")
Student["name"]=name
marks=int(input("enter marks of student"))
Student["marks"]=marks
print(Student)
'''
#order Dic
'''
from collections import OrderedDict
a=OrderedDict()
a["1"]="present"
a["2"]="absent"
print(a)
'''
#chained map 
'''
from collections import ChainMap

default={"fan":"off",
         "light":"on"
         }
cur={"fan":"on"}

default={"fan":"off"}
state=ChainMap(cur,default)
print(state)
'''


# 3. Tuples

#intilize
'''
a=(1,2,3)
print(a)
'''
#indexing
'''
a=(1,2,3)
print(a[0])
'''
# named tuple 
'''
from collections import namedtuple
stu=namedtuple("stu",["name","age"])
s1=stu("ali",8)
print(s1)
'''
# 4. sets 
'''
numbers={1,2,3,3,6,6}
numbers.add(9)
print(numbers)
'''

#5. strings
'''
a="ali"
print(a[0])
'''


# 6. Functions
'''
def add(id,name=None,Class=None):
    print(id)
    if name is not None:
        print(name)
    if Class is not None:
        print(Class)

add(1,"Ali")            
'''
#  7. tracemelloc 
'''
import tracemalloc

tracemalloc.start()

data=list(range(1000))

curr,peek=tracemalloc.get_traced_memory()

print("curr",curr)
print("peek",peek)


tracemalloc.stop()
'''


