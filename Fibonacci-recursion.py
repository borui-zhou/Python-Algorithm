import time

def fibs(n):
    if n==0: return 0
    elif n==1: return 1
    else:
        return fibs(n-1)+fibs(n-2)

def fibs2(n):
    if n==0: return 0
    elif n==1: return 1
    else :
        a=0
        b=1
        c=0
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return (c)
            



t=time.time()
for i in range(35):
    #print("i=",i,"fib=",fibs(i))
    fibs(i)
t2=time.time()-t
print ("time is",t2)


t=time.time()   
for i in range(10000):
    #print("i=",i,"fib=",fibs2(i))
    fibs2(i)
t2=time.time()-t
print ("time is",t2)
