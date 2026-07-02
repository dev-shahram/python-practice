#pop increases by 10% every year what is pop of last 10 years if current pop is 10000
curpop=10000
for i in range(10,0,-1):
    print(i,curpop)
    curpop=curpop/1.1

    #pop in 9th year=x
    #x+10% of x=10000
    #x+0.1x=10000
    #1.1x=10000
    #x=10000/1.1
