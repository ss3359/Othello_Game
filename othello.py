import random 
import pygame
import numpy 
import pandas 

#Constants
PLAYERONE="X"
PLAYERTWO="O"
WIDTH=8
HEIGHT=8

#Variables 
board=[]

#Functions/Classes


def GetNewBoard():
    for i in range(WIDTH):
        board.append(['','','','','','','','']) 

    for i in range(WIDTH): 
        for j in range(HEIGHT):  
            if(i==3 and j==3): 
                board[i][j]=PLAYERONE
            elif(i==3 and j==4): 
                board[i][j]=PLAYERTWO
            elif(i==4 and j==3):
                board[i][j]=PLAYERTWO
            elif(i==4 and j==4):
                board[i][j]=PLAYERONE
    return board; 

def CheckBoard(board):
    result=False
    for i in range(8): 
        for j in range(8): 
            if board[i][j]!= '': 
                result=True 
    return result

def PrintBoard(board): 
    print("+ - - - - - - - +")
    for i in board: 
        print(i)
    print("+ - - - - - - - +")

def IsValidPosition(board,i,j,marker): 
    return 0<=i<WIDTH and 0<=j<HEIGHT and board[i][j]==marker

def IsValidMove(board,i,j,player,opponent): 
    directions=[(-1,0), (1,0), (0,-1), (0,1), (1,1),(-1,-1), (-1,1), (1,-1)]
    PiecesToFlip=[]
    for dx, dy in directions: 
        xloc=i+dx
        yloc=j+dy
        while(IsValidPosition(board,xloc,yloc,opponent)):
            xloc+=dx
            yloc+=dy
            if(IsValidPosition(board,xloc,yloc,player)):
                while(True): 
                    xloc-=dx
                    yloc-=dy 
                    if(xloc==i and yloc==j): 
                        break
                    PiecesToFlip.append((xloc,yloc))
            elif(IsValidPosition(board,xloc,yloc,'')): 
                #This is an invalid move
                #continue
                break
                    
    if(len(PiecesToFlip)==0): 
        #This piece is an invalid move
        return False
    FlipTheChips(board,PiecesToFlip,player)
    return True

                              

def FlipTheChips(board,PiecesToFlip,player): 
    for i,j in PiecesToFlip: 
        board[i][j]=player


    
def PlayerTurn(board): 
    print("Enter A Marker On The Board: ")
    i=int(input("Row: "))
    j=int(input("Column: "))
    if(IsValidMove(board,i,j,PLAYERONE,PLAYERTWO)): 
        board[i][j]=PLAYERONE
    PrintBoard(board)


def ComputerTurn(board):
    directions=[(-1,0), (1,0), (0,-1), (0,1), (1,1),(-1,-1), (-1,1), (1,-1)]
    OpponentPieces=[]
    PlayerSpaces=[]
    for i in range(WIDTH): 
        for j in range(HEIGHT): 
            if(IsValidPosition(board,i,j,PLAYERONE)):
                OpponentPieces.append((i,j))

    for r, c in OpponentPieces:
        for dx, dy in directions: 
            if(IsValidPosition(board,r+dx,c+dy,'')and (r+dx,c+dy) not in PlayerSpaces): 
                PlayerSpaces.append((r+dx,c+dy)) 

    for m,n in PlayerSpaces: 
        if(IsValidMove(board,m,n,PLAYERTWO,PLAYERONE)): 
            board[m][n]=PLAYERTWO
            break
    PrintBoard(board)
            
           
    

def main(): 
    board=GetNewBoard()
    decision=True 
    PrintBoard(board)

    while(CheckBoard(board)): 
        PlayerTurn(board)
        ComputerTurn(board)

main()



















































