rows=int(input("enter no of rows"))

for i in range (1,rows+1):
    for j in range(1,i+1):
        a=j-1
        if j==1:
            print(j,end=" ")
        else:
           print(j,end=" ")
    for a in range(j-1,0,-1): 
     print(a,end=" ")        
    print()    


        

        

        
          
