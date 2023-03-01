# Gungi Game engine preliminary code    2/28/23
# This code is just to get ideas and notation written out, final will be written in Unreal Engine once bugs and visuals are cleaned up
import math

pieceCatalog = ["N/A", "Catapult", "Fortress","Spy","Captain","Samurai","Hidden dragon","Prodigy","Bow","Pawn(B)","Pawn(S)","Pawn(G)",
"Commander","Lance","Lance","Clandestinite","Pistol","Pike","Dragon king","Phoenix","Arrow","Bronze","Silver","Gold"]
turn = 1

#Bryce, replace the names below with whatever abbreviations you want to display:
pieceAbbreviatedCatalog = ["N/A", "Catapult", "Fortress","Spy","Captain","Samurai","Hidden dragon","Prodigy","Bow","Pawn(B)","Pawn(S)","Pawn(G)",
"Commander","Lance","Lance","Clandestinite","Pistol","Pike","Dragon king","Phoenix","Arrow","Bronze","Silver","Gold"]


def main():
    if ask("Do you want to skip the initial arrangement of the board?"/n) == "no":
        initialArangement()
    else:
        board = matrix[9,9,3]
    gamemode = "manual" if ask("Do you want to play manually?) == "yes" else "automatic"
    if gamemode == "manual":
        #create empty move history for the game
        #repeatedly take turns, moving via:
        #printBoard()
        #select move with askMove()
        #makeMove(selectedMove)
    else:
        #repeatedly:
        #for every piece, checkMove(), (and drop moves too)
             #for every move, makeMove() if that isn't already in the database

    
def initialArangement():
    #move, limited to "drop" moves, until all pieces placed

def askMove():
    if 
    #printBoard(board)
    ask("Which piece would you like to move?")
    ask("Where would you like to move the piece?")
    answer = ask("what is the meaning of the universe")
                               
def checkMove(origin):
    #this will check where pieces can go
                               
def makeMove(moveCode):
    #this will make a move happen, once selected
    #if valid, move and return true, else return false
    #add move to game move history
    #record board to database

def recordToDatabase(input):
    #linked graph for boardstates: boards are nodes, moves are edges.
    #If a board has a win condition, make it -1 or 1 "win likelihood", otherwise define one based on an average of the outcomes if all outcomes have been calculated (recursive).                               

def ask(question):
    while confirmation != "yes":
        pieceSelection = input(question)
        print("You have selected: " + pieceSelect)
        confirmation = input("Continue?")
    return(pieceSelect)

def drop():
    print("hello world")
    
def flipPiece(piece):
    return(-1*mod(abs(piece)+14,24))

def printBoard(board):
    #code to print the board "board" here

print("1,2,3,4,5,6,7,8,9" \n
      "1,2,3,4,5,6,7,8,9" \n
      "1,2,3,4,5,6,7,8,9" \n
      "1,2,3,4,5,6,7,8,9" \n
      "1,2,3,4,5,6,7,8,9" \n
      "1,2,3,4,5,6,7,8,9" \n
      "1,2,3,4,5,6,7,8,9" \n
      "1,2,3,4,5,6,7,8,9" \n
      "1,2,3,4,5,6,7,8,9")


