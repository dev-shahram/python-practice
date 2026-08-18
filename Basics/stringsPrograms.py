#find out the name form the email 
a= input("enter our email ")
b="@"

for i in a:
     if i==b:
            break
     else:
           print(i , end=" ")

#by slicing method 

z=input("enter your email")
x=z.index('@')
print(z[0:x])
