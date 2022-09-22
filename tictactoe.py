
def main():

    squares = {"1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9}
    print_board(squares)

    playing = 1

    turn = 0
    xoption = 0
    ooption = 0

    while playing == 1 and turn < 9:
        turn += 1
         
        if turn % 2 == 1:
            approved = 0
            while approved == 0:
                xoption = input("x's turn to choose a square (1-9): ")
                if xoption.isdecimal():
                    xoption = int(xoption)
                    if xoption < 10:
                        if xoption in squares.values():
                            xoption = str(xoption)
                            squares[xoption] = "x"
                            print_board(squares)
                            approved = 1
                            playing = playing_rules(squares)
                        else:
                            print("Wrong option, try again")
                    else:
                        print("Wrong option, try a number 1-9")
                else:
                    print("Wrong option, try a number 1-9")
            
        elif turn % 2 == 0:
            approved = 0
            while approved == 0:
                ooption = input("o's turn to choose a square (1-9): ")
                if ooption.isdecimal():
                    ooption = int(ooption)
                    if ooption < 10:
                        if ooption in squares.values():
                            ooption = str(ooption)
                            squares[ooption] = "o"
                            print_board(squares)
                            approved = 1
                            playing = playing_rules(squares)
                        else:
                            print("Wrong option, try again")
                    else:
                        print("Wrong option, try a number 1-9")
                else:
                    print("Wrong option, try a number 1-9")
                            
                
    if turn % 2 == 0 and playing == 0:        
        print("'o' is the winner! Thanks for playing!")
    elif turn % 2 == 1 and playing == 0:
        print("'x' is the winner! Thanks for playing!")    
    elif turn == 9:
        print("It's a draw! Thanks for playing!")
    else:
        print("Error")

def print_board(squares):
    print(f"""{squares["1"]}|{squares["2"]}|{squares["3"]}\n-+-+-\n{squares["4"]}|{squares["5"]}|{squares["6"]}\n-+-+-\n{squares["7"]}|{squares["8"]}|{squares["9"]}""")

def playing_rules(squares):
    if ((squares["1"] == squares["2"] == squares["3"]) or
        (squares["4"] == squares["5"] == squares["6"]) or
        (squares["7"] == squares["8"] == squares["9"]) or 
        (squares["1"] == squares["5"] == squares["9"]) or
        (squares["3"] == squares["5"] == squares["7"]) or
        (squares["1"] == squares["4"] == squares["7"]) or
        (squares["2"] == squares["5"] == squares["8"]) or
        (squares["3"] == squares["6"] == squares["9"])):
        return 0
    else:
        return 1

    

if __name__ == "__main__":
    main()