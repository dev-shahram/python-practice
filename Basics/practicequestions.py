#Sum Values Until 0 Is Entered

#total=0


#a=-1
#while a!=0:
  #  a=int(input("enter your number"))
   # total=total+a



#print("sum of all neter values are",total) 
   

#Grade Calculator
''''
num=int(input("enter your numbers")) 

if num>89 and num<101:
    print("your grade is A")
elif num>79 and num<91:
    print("your grade is B")    
elif num>69 and num<81:
    print("your gradfe is C")
elif num>59 and num<71:
    print("your grade is D")
elif num >49 and num<61:
    print("your grade is E")
elif num<50:
    print("your grade is F")
elif num>100:
    print("enter marks under 100")    
    '''


#find teh enetered num is prime or not 
'''
a=2
b=int(input("enter your num "))
c=b%a
bool=True

while b>a:
    c=b%a
    if c==0:

        print("num is not prime")
        bool=False
        break
    else:
        a=a+1

if bool==True:
    print("num is prime")
    "'''

#factorial
'''
z=int(input("enter your num "))

x=0

for i in range(z,1,-1):
    x=z*i

print(x)   
'''

#febinachi 

list=[]
a=int(input("enter the number for fabinachi series"))

for i in range(0,a):
    z=1
    x=z+i
    list.append(x)
    z=i-1

print(list)       