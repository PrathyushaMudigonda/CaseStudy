def game():
 while True:
    user1 = input("Hello!!! user1 plase enter either rock,scissor or paper: ")   
    user2 = input("Hello!!! user2 plase enter either rock,scissor or paper: ")
    if user1 == user2:             #if both users enters same
        print("Its a tie!!!")
    elif user1 == 'rock':             
        if user2 == 'scissors':     
            print("User 1 wins\n Congrations!!!")
        else:
            print("User 2 wins\n Congrations!!!")
    elif user1 == 'scissors':
        if user2 == 'paper':
            print("User1 wins\n Congrations!!!")
        else:
            print("User 2 wins\n Congrations!!!")
    elif user1 == 'paper':
        if user2 == 'rock':
            print("User1 wins\n Congrations!!!")
        else:
            print("User2 wins\n Congrations!!!")
    else:
        print("Provide the values appropriate for the game")
    print("Do you want to play again? (Y/N)")
    ans = input()
    if ans == 'n' or ans == 'N':
        break
game()
print("\nThanks for playing")
