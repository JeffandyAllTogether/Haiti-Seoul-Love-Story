def main_game():
    while True:
        print('''
*******************************************************************************
_   _    _    ___ _____ ___ 
| | | |  / \  |_ _|_   _|_ _|
| |_| | / _ \  | |  | |  | | 
|  _  |/ ___ \ | |  | |  | | 
|_| |_/_/   \_\___| |_| |___|

 ____  _____ ___  _   _ _     
/ ___|| ____/ _ \| | | | |    
\___ \|  _|| | | | | | | |    
 ___) | |__| |_| | |_| | |___ 
|____/|_____\___/ \___/|_____|

  ♥ LOVE STORY ♥
*******************************************************************************
''')
        print("Welcome to Haiti Seoul love story. ")
        print("Your mission is to start true love between Jeffandy and Ladi Seoul.")
        print("Please type your answers!")

        answer1 = input("\nDoes Ladi turn left to patio or turn right to exit? \n left or right? ").lower()
        if answer1 == "left":
            print("nice move! \n")
            answer2 = input("Does Ladi walk to Jeffandy in corner or stand with friends? \n walk or stand? ").lower()
            if answer2 == "walk":
                print("Ladi walks over to Jeffandy")
                # Fixed: added input()
                answer3 = input("Does Jeffandy share that he's on a prayer call talking about Jesus, pretend like it's nothing, or compliment Ladi on her beauty \n share, pretend or compliment? ").lower()
                if answer3 == "compliment":
                    print("Ladi thanks him for compliment and says good bye.\n game over.")
                elif answer3 == "share":
                    print("They talk about life God and start what will be the most important friendship of their lives. YOU WIN!")
                    print(r'''
**********************************************
* HAPPILY EVER AFTER!               *
**********************************************
                    ''')
                else:
                    print("The connection wasn't made. \n game over.")
            elif answer2 == "stand":
                print("they never meet.. \ngame over.")
            else:
                print("Ladi walks away.\n game over")
        else:
            print("they never meet... \n game over.")

        # Play Again Logic
        retry = input("\nWould you like to play again? (yes/no): ").lower()
        if retry != "yes":
            print("Thanks for playing the Haiti Seoul Love Story! Goodbye.")
            break 

# Start the game
main_game()