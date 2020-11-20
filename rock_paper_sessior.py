#this is a rock paper scissor game
import random,sys

#variable
win =0
lose=0
tie =0

while True:#the game loop

    while True:#the input loop
        print('Enter your move : r(Rock)p(paper)s(scissor)q(quit)')
        playermode = input()
        if playermode=='q':
            sys.exit()
        if playermode == 'r' or playermode == 'p' or playermode == 's':
            break
            #out of input loop

    #players choice based on input
    if playermode == 'r':
        print("The Rock verses...")
    elif playermode == 'p':
        print("The paper verses...")
    elif playermode == 's':
        print("The scissor versus...")

    #computers choice based on random number
    randomnumber = random.randint(1,3)
    if randomnumber == 1:
        computerMode ='r'
        print("Rock")
    elif randomnumber == 2:
        computerMode ='p'
        print("Paper")
    elif randomnumber == 3:
        computerMode = 's'
        print("Scissor")

    #check out win/lose/ties

    if playermode == computerMode:
        print("tie")
        tie+=1
    elif playermode == 'r' and computerMode =='s':
        print("You win")
        win+=1
    elif playermode == 'p' and computerMode=='r':
        print("You win")
        win+=1
    elif playermode =='s' and computerMode =="p":
        print("You win")
        win+=1

    elif playermode =='r' and computerMode=='p':
        print("you lose")
        lose+=1
    elif playermode =='p' and computerMode=='s':
        print("you lose")
        lose+=1
    elif playermode =='s' and computerMode=='r':
        print("you lose")
        lose+=1

    print("%s win %s lose %s tie" % (win, lose, tie))



