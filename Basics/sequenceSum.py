#find sum of 1/1!+2/2!+3/3!+....Nth term
n=int(input("enter n "))
sum=0
fact=1
for i in range (1,n+1):
    fact=fact*i
    sum=sum+i/fact

print(sum)     


### by using math 
import math
z=int(input("enter n "))
su=0
fac=1
for i in range(1,z+1):
     fac=math.factorial(i)
     su=su+i/fac

print(su)