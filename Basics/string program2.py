#find the frequency of the num in the given string by the user 

a=input("enter your string ")

z=input("enter the digit which you want to find the frequency ")

count=0
for i in a:
    if i==z:
        count +=1

print("the frequency of ",z,"is",count)
       