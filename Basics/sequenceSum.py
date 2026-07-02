#find sum of 1/1!+2/2!+3/3!+....Nth term
n=int(input("enter n "))
sum=0
fact=1
for i in range (1,n+1):
    fact=fact*n
    sum=sum+n/fact

print(sum)     
