
# Let's Play TIC TAC TOE Game........

import random
print("Welcome to TIC TAC TOE Game")
print("***************\n")

row = 3
cols = 3
board = [[1,2,3],[4,5,6],[7,8,9]]
possiblenum = [1,2,3,4,5,6,7,8,9]

def printgameboard():
    for x in range(row):
        print("+---+---+---+")
        print("|",end=" ")
        for y in range(cols):
            print("",board[x][y],end=" |")
        print("\n+---+---+---+")

def modifyarray(num,turn):
    # turn is "X or O"
    num-=1
    if(num==0):
        board[0][0]=turn
    elif(num==1):
        board[0][1]=turn
    elif(num==2):
        board[0][2]=turn
    elif(num==3):
        board[1][0]=turn
    elif(num==4):
        board[1][1]=turn
    elif(num==5):
        board[1][2]=turn
    elif(num==6):
        board[2][0]=turn
    elif(num==7):
        board[2][1]=turn
    elif(num==8):
        board[2][2]=turn

turn="X"
leaveloop="False"
turncounter=0

# Checking - Winner or Looser or Tie

def checkwinner(board):
    # Horizontally check
    
    if(board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X"):
        print("X has won!!")
    elif(board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O"):
        print("O has won!!")
    elif(board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X"):
        print("X has won!!")
        
    elif(board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O"):
        print("O has won!!")
        
    elif(board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X"):
        print("X has won!!")
        
    elif(board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O"):
        print("O has won!!")
        
    # Vertical Check

    elif(board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X"):
        print("X has won!!")
        
    elif(board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O"):
        print("O has won!!")
        
    elif(board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X"):
        print("X has won!!")
        
    elif(board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O"):
        print("O has won!!")
        
    elif(board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X"):
        print("X has won!!")
       
    elif(board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O"):
        print("O has won!!")
        
    # Diagnoal Check

    elif(board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X"):
        print("X has won!!")
        
    elif(board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O"):
        print("O has won!!")
        
    elif(board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X"):
        print("X has won!!")
        
    elif(board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O"):
        print("O has won!!")
        
    else:
        
        return "Continue"
        

while(leaveloop == "False"):

    #player Turn

    if(turncounter%2==0):
        printgameboard()
        numberpicked= int(input("Enter thr num within [0-9]:::"))
        if(numberpicked>=0 and numberpicked<=8):
            modifyarray(numberpicked , "X")
            possiblenum.remove(numberpicked)
        else:
            print("Enter valid input...")
        turncounter+=1
        
    # Computer;s turn
    
    else:
        while(True):
            com_choice=random.choice(possiblenum)
            if(com_choice in possiblenum):
                modifyarray(com_choice,"O")
                possiblenum.remove(com_choice)
                turncounter+=1
                break
    winner = checkwinner(board)
    if(winner != "Continue"):
        print("\nGame over!! Buddy Thank you for playing guy :)")
        break
  


















        
    
