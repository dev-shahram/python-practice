import random

z=random.randint(1,20)
count=0
while count<5:
    a=int(input("guess the number between 1 -20"))
    count=count+1
    if a<z:
        print("guess higher")
    elif a>z:
        print("guess lower")
    else:
        print("you found the number")
        break
else:
    print("out of tries")