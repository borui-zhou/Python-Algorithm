table=[['', '', ''],
       ['', '', ''],
       ['', '', '']]  

def winner():
    blackwin=0
    whitewin=0
    countrb=0
    countrw=0
    countlb=0
    countlw=0
    for i in range(3):
        countxw=0
        countyw=0
        countxb=0
        countyb=0
        for j in range(3):
            if table[i][j]=="B":countxb=countxb+1
            if table[i][j]=="W":countxw=countxw+1
            if table[j][i]=="B":countyb=countyb+1
            if table[j][i]=="W":countyw=countyw+1
        if countxw==3 or countyw==3: whitewin=1
        if countxb==3 or countyb==3: blackwin=1
        if table[i][i]=="B": countrb+=1
        if table[i][i]=="W": countrw+=1
        if table[2-i][i]=="B": countlb+=1
        if table[2-i][i]=="W": countlw+=1
    if countrb==3 or countlb==3 : blackwin=1
    if countrw==3 or countlw==3 :whitewin=1
    if blackwin+whitewin==2: return "Win-Win"
    elif blackwin+whitewin==0: return "None Win"
    elif blackwin==1: return "Black win"
    else : return "White Win"

def playing():
    chess=0
    for i in range(3):
        for j in range(3):
            if table[i][j]!="": chess+=1
    if chess==9 : return "Done"
    else : return "Playing"

def checkstate(x,y):
    if table[x][y]=="": return "Empty"
    else : return "Occuped"

def setchess():
    state=0
    position=[]
    while state==0:
        x=int(input("please input you X position 0-2,   "))
        if x<3 : break
    position.append(x)
    while state==0:
        y=int(input("please input you Y position 0-2,   "))
        if y<3 : break
    position.append(y)
    return position

p=[]
for k in range(3):
    print(table[k])
print(playing())

for i in range(9):
    p=setchess()
    while True:
        if checkstate(p[0],p[1])=="Occuped":
            print ("position  ", p," is occuped, Try again")
            p=setchess()
        else:
            break
    if i%2==0 : table[p[0]][p[1]]="W"
    else : table[p[0]][p[1]]="B"
    for k in range(3):
        print (table[k])
    print(playing())
    print()
    if winner()=="Black win" or winner()=="White Win":
        print(winner())
        break

for i in range(3):
    print(table[i])
print(playing())
print(winner())


    
