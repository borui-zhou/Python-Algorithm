a=[23,7,90,144,65,89,25]
b=[]
x=len(a)
b.append(a[0])
for i in range(1,x):
    j=0
    f=1
    if a[i]>b[i-1]:
        b.append(a[i])
    else:
        while j<i and f:
            if a[i]<b[j]:
                b.insert(j,a[i])
                f=0
            else:
                j=j+1
    print(b)
