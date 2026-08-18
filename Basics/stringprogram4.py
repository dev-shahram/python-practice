#find the string is pelindrome or not
a=input("enter your sting ")

b=len(a)
bool=True

for i in range (0, b):
      if a[i]==a[b-1]:
            b -=1
      else:
            bool=False
                 
if bool==True:
      print ("string is pelindrome")
else:
      print("string is not pelindrome")      