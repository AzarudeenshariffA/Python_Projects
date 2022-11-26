val = [" " for i in range(1,11) ]
def board(letter, pos):
    if letter == 1:
        let = "X"
    elif letter == 2:
        let = "O"
    else:
        print("Wrong Input")
        let = " "

    if val[pos]==" ":
        val[pos] = let
        print(val[1] +" | "+ val[2]+" | "+ val[3]+"\n"+val[4] +" | "+ val[5]+" | "+ val[6]+"\n"+val[7] +" | "+ val[8]+" | "+ val[9])
    else:
        print("place is occupied please try another")
    if (val[1] == "X" and val[2] == "X" and val[3] == "X") or  (val[4] == "X" and val[5] == "X" and val[6] == "X") or (val[7] == "X" and val[8] == "X" and val[9] == "X") or (val[1] == "X" and val[5] == "X" and val[9] == "X") or (val[3] == "X" and val[5] == "X" and val[7] == "X") or (val[1] == "X" and val[4] == "X" and val[7] == "X") or (val[2] == "X" and val[5] == "X" and val[8] == "X") or (val[3] == "X" and val[6] == "X" and val[9] == "X"):
        print("X is Winner")
        return False
    if (val[1] == "O" and val[2] == "O" and val[3] == "O") or  (val[4] == "O" and val[5] == "O" and val[6] == "O") or (val[7] == "O" and val[8] == "O" and val[9] == "O") or (val[1] == "O" and val[5] == "O" and val[9] == "O") or (val[3] == "O" and val[5] == "O" and val[7] == "O") or (val[1] == "O" and val[4] == "O" and val[7] == "O") or (val[2] == "O" and val[5] == "O" and val[8] == "O") or (val[3] == "O" and val[6] == "O" and val[9] == "O"):
        print("O is Winner")
        return False
    
def isfull():
    space = val.count(" ")
    if space<1:
        return False
    else:
        return True


print("welcome...")
print("enter 1 for 'x' and 2 for '0'")
print("enter 1 and 2 for symbol 'X' and 'O' and enter position separated by spcae eg:- 1,2--> 1 is 'x' and 2 is pos ")
gameover = True
while(gameover):
    gameover = isfull()
    symbol, pos = input("enter symbol and pos: ").split(",")
    sav = board(int(symbol),int(pos))
    if sav == False:
        gameover = sav
    
