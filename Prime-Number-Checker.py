x=int(input("Please input a number"))
count=0
dividend=1
while count<=2 and dividend<=x :
    if int(x/dividend)==(x/dividend) :count=count+1
    dividend=dividend+1
if count<=2 : print (x,"is a prime number")
else : print(x," isn't prime number")

#Regina
def isPrime(n):
    for i in range(2, n):
      if n % i == 0:
        return False
      else:
        return True
