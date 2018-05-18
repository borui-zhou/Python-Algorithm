a=[]
for i in range(100,999):
    x=int(i/100)
    y=int((i-x*100)/10)
    z=i-x*100-y*10
    if (i-x**3-y**3-z**3)==0: a.append(i)
print (a)

