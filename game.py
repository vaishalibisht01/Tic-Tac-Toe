l=[""]*10
l[0]=""
def display(l):
    print("\t"+l[1]+"\t"+"|"+"\t"+l[2]+"\t"+"|"+"\t"+l[3])
    print("---------------------------------------------")
    print("\t"+l[4]+"\t"+"|"+"\t"+l[5]+"\t"+"|"+"\t"+l[6])
    print("---------------------------------------------")
    print("\t"+l[7]+"\t"+"|"+"\t"+l[8]+"\t"+"|"+"\t"+l[9])
def placeCharPos(player):
    pos=int(input("Player "+player+" : Enter position "))
    p=placeChar(pos,player)
    
    return(p)
def placeChar(pos,player):
    if l[pos]=='':
        l[pos]=player
        display(l)
    else:
        print ("This position is already filled!!")
        placeCharPos(player)
        
def isWin(player):
    if((l[1]==l[2]==l[3]==player)or(l[5]==l[4]==l[6]==player)or(l[7]==l[8]==l[9]==player)or(l[1]==l[4]==l[7]==player)or(l[2]==l[5]==l[8]==player)or(l[3]==l[6]==l[9]==player)or(l[1]==l[5]==l[9]==player)or(l[3]==l[5]==l[7]==player)):
        print("Congratulations!!")
        print("Player "+player+" won!!")
        exit()
def checkfull(l):
    if (l[1]!='' and l[2]!='' and l[3]!='' and l[4]!='' and l[5]!='' and l[6]!='' and l[7]!='' and l[8]!='' and l[9]!=''):
        print("It's a Tie....")
        print("Better luck next time")
        exit()
def startgame():
    player="X"
    while not isWin(player):
        
        if player=="X":
            placeCharPos("X")
            isWin("X")
            player="O"
        else:
            placeCharPos("O")
            isWin("O")
            player="X"
        checkfull(l)
startgame()
