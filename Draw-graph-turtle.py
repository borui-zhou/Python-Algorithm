import turtle as t
def Trg(L,A):
    t.left(90+A)
    t.fd(L/2)
    t.right(120)
    t.fd(L)
    t.right(120)
    t.fd(L)
    t.right(120)
    t.fd(L/2)
    
def drawxy(draftx,drafty,lenth):
    t.penup()
    t.goto(draftx,drafty)
    t.pendown()
    t.fd(lenth)
    t.begin_fill()
    Trg(15,0)
    t.end_fill()
    t.penup()
    t.setheading(0)
    t.goto(draftx,drafty)
    t.left(90)
    t.pendown()
    t.fd(lenth)
    t.begin_fill()
    Trg(15,0)
    t.end_fill()
    t.hideturtle()

def drawline(x,y):
    t.penup()
    t.goto(x[0]-300,y[0]-300)
    t.pendown()
    for i in range(1,len(x)):
        t.goto(x[i]-300,y[i]-300)
    t.penup()

def readnumber(fname):
    f=open(fname,"r")
    a=[]
    new=f.read(1)
    while new :
        k=0
        n=1
        if new=="-":
            n=-1
            new=f.read(1)
        elif new=="0":
            a.append(0)
            new=f.read(1)
        else :
            while new!=",":
                k=k*10+int(new)
                new=f.read(1)
        new=f.read(1)
        a.append(k*n)
    f.close()
    return a





ax=[]
filename="CMPresult.txt"
ax=readnumber(filename)
n=ax[0:27]
bub=ax[27:56]
inset=ax[56:83]
sel=ax[83:]
factor=3000
for i in range(27):
    n[i]=int(n[i]/factor*10)
    bub[i]=int(bub[i]/factor)
    inset[i]=int(inset[i]/factor)
    sel[i]=int(sel[i]/factor)


drawxy(-300,-300,600)
t.pensize(5)
t.color ("blue")
drawline(n,bub)
t.color ("red")
drawline(n,inset)
t.color ("black")
drawline(n,sel)
