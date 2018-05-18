#the board is 15x15
board=[["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""],
       ["","","","","","","","","","","","","","",""]]

def win():
    whiterow=0
    blackrow=0
    whitecolumn=0
    blackcolumn=0
    blackdiagonal1=0
    whitediagonal1=0
    blackdiagonal2=0
    whitediagonal2=0
    for j in range (10):
        for i in range(10):
            for d in range(5):
                if board[i+d][j]==board[i+1+d][j] and board[i+d][j]=="B" :
                    blackrow+=1
                if board[i+d][j]==board[i+1+d][j] and board[i+d][j]=="W" :
                    whiterow+=1
    for i in range(10):
        for j in range(10):
            for d in range(5):
                if board[i][j+d]==board[i][j+1+d] and board[i][j+d]=="B" :
                    blackcolumn+=1
                if board[i][j+d]==board[i][j+1+d] and board[i][j+d]=="W" :
                    whitecolumn+=1
    for j in range(10):
        for i in range (10):
            for d in range(5):
                if board[i+d][j+d]==board[i+1+d][j+1+d] and board[i+d][j+d]=="B" :
                    blackdiagonal1+=1
                if board[i+d][j+d]==board[i+1+d][j+1+d] and board[i+d][j+d]=="W" :
                    whitediagonal1+=1
    for i in range(4,15):
        for j in range(10):
            for d in range (5):
                if board[i-d][j+d]==board[i-1-d][j+1+d] and board[i-d][j+d]=="B" :
                    blackdiagonal2+=1
                if board[i-d][j+d]==board[i-1-d][j+1+d] and board[i-d][j+d]=="W" :
                    whitediagonal2+=1
    if blackrow==4 or blackcolumn==4 or blackdiagonal1==4 or blackdiagonal2==4: return "The black wins!"
    if whiterow==4 or whitecolumn==4 or whitediagonal1==4 or whitediagonal2==4: return "The white wins!"
    for i in range(15):
        for j in range(15):
            if board[i][j]=="": return "playing..."
    return"Tie!"

def availableSpots(x,y):
    if board[x][y] =="": return True
    else: return False

def play():
    flage=1
    position=[]
    while flage==1:
        x=int(input("please enter the X value of your move (0-14): " ))
        if x < 15: break
    position.append(x)
    while flage==1:
        y=int(input("please enter the Y value of your move (0-14): "))
        if y < 15: break
    position.append(y)
    return position

def showboard():
    for i in range(15):
        print(board[i])
    print("\n")

def run():
    flage=1
    for i in range(225):
        move=play()#idk
        print("You just set your chess at",move)
        while flage==1:
            if availableSpots(move[0],move[1])==False:
                print("Sorry, this spot is occupied.")
                move=play()#idk
            else:
                break
        if i%2!=0: board[move[0]][move[1]]="B"
        if i%2==0: board[move[0]][move[1]]="W"
        showboard()
        if win()=="The black wins!" or win()=="The white wins!" or  win()=="Tie!":
            print(win())
            break
        
showboard()  
run()
    


