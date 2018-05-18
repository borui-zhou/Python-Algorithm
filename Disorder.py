# Function

def disorder(a):
    b=[]
    for i in range(1,len(a)):
        max=len(a)
        x=int(random.uniform(1,max))
        b.append(a[x])
        a.remove(a[x])      
    b.append(a[0])
    return b

# Main
import random
a=[1,2,3,4,"asc","def","ffg"]
a=disorder(a)
print (a)



