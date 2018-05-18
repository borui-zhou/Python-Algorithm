# The functions
def checkodd(x):
    for i in range(2,int(x/2+1)):
        if x%i==0 :
            return False
    return True

def findprime(x):
    a=[]
    for i in range(2,x):
        if checkodd(i):
            a.append(i)
    return a

def sboddlist(x):
    sb=[]
    subprime= findprime(int(x/2))
    while not checkodd(x):
        for i in range(0,len(subprime)):
            if x%subprime[i]==0:
                sb.append(subprime[i])
                x=x/subprime[i]
    if x!=1:
        sb.append(int(x))
    sb.sort()
    return sb

# The main program
number=int(input("please in put a int number :"))
print ("number is",number)
if checkodd(number):
    print (number,"is a odd number")
else: 
    print (number,end="=")            
    sb=sboddlist(number)
    for i in range(0,len(sb)-1):
        print (sb[i],end="*")
    print (sb[i+1])
