#remove particular charcter from the string 
a=input("enter your string ")

b=input("enter the charter you want to romove from the string ")
#because strings are imputeable so we make an empty sring 
c=''
for i in a:
    if i !=b:
        c=c+i

print(c)            
