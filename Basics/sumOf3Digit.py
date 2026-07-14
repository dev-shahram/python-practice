#input user se leina ha 
num=int(input("Enter a 3 digit number:"))
#this % is a modulas opertor yay last digit nikalta ha 
a=num%10
# and thsi // is a floor division operator yay last digit nikalta ha
num=num//10
b=num%10
num=num//10
c=num%10
print(a+b+c)
