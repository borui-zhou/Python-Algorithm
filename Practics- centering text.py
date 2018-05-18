lenth=int(input("Please input the width of the text"))
s=[]
a=input("please input ")
while a!="END":
    s.append(a)
    a=input("please input ")
print (s,len(s))
for i in range (0,len(s)):
    wide=len(s[i])
    left=int((lenth-wide)/2)
    right=lenth-left-wide
    print ("."*left,s[i],"."*right)
