import random
import os

def find(word):
    wrong = 0
    stages = ["",
              "▄───▄",
              "█▀█▀█",
              "█▄█▄█",
              "─███──▄▄",
              "─████▐█─█",
              "─████───█",
              "─▀▀▀▀▀▀▀",
              "_YOU_LOSE_"
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("THE WORD HAVE {} LETTERS!".format(len(word)))
    while wrong < len(stages) - 1:
        print("TIME {} / {}".format(wrong, len(stages)-2))
        print((" ".join(board)))
        print("\n".join(stages[0: wrong+1]))
        msg = "Enter the letter: "
        char = input(msg)
        os.system('cls')
        if char in rletters:
            while(char in rletters):
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        else:
            wrong += 1
        # e = wrong + 1
        if "__" not in board:
            print("You won! The word was:")
            print(" ".join(board))
            win = True
            break
        
    if not win:
        print("\n".join(stages[0: wrong+1]))
        print("You lost! The word was: {}.".format((word)))
    
def main():
    file  = "word.txt"
    myl=[]
    with open(file) as lines:
        for line in lines:
            line = line.replace("\n", "")
            myl.append(line)
    # print(myl[random.randint(0,len(myl))])
    find(myl[random.randint(0,len(myl)-1)])

if __name__ == "__main__":  
    main()