# INF360 - Programming in Python
# Lisa Thoms
# Final Project

'''
Will need to download pandas for my project, seen in polish.py
Program uses OOP via a pandas DataFrame to grab information about a nail
polish from my nail polish spreadsheet. The user can either select a
number or the program will pick a random one for them.

I have added loops to go through each mini game, and a final loop for the
main menu. The user can exit out of the mini game and main menu, or
continue through the file endlessly.

I have added logging to the main file to make sure that the imported
functions run properly, as well as logging in the polish.py function
for info to collect the user inputted numbers or the randomly generated
numbers.

Thank you for a great semester!
'''

import logging
import sys
## adding required logging - chose to import to file 
logging.basicConfig(filename='myProgramLog.txt',
                    level=logging.DEBUG,
                    format=' %(asctime)s -  %(levelname)s-  %(message)s')

# logging tries for import functions
try:
    import seasonal as szn
except:
    logging.critical('Missing seasonal.py!')
    print('Missing seasonal.py! Program is closing.')
    sys.exit()
try:
    import polish as polish
except:
    logging.critical('Missing polish.py!')
    print('Missing polish.py! Program is closing.')
    sys.exit()


def playloop(): # creating a loop to play again if wanted
    print('\nDo you want to try a different game? Y or N: ')

    while True:
        newGame = input()
        if newGame.upper() == 'N' or newGame.upper() == 'NO':
            print('\nEnjoy your manicure! Thanks for playing.')
            # exit game
            sys.exit()
        elif newGame.upper() == 'Y' or newGame.upper() == 'YES':
            main() # going back to seasons function as they have already established they wear nail polish.
        elif newGame.upper() != ('N', 'NO', 'Y', 'YES') or newGame.isalnum():
            print('\nPlease enter a valid input. Y or N.')
            # proceed back to start to enter correct input
            continue

# starting the program function
def main():
    # create menu
    print('\n')
    print(7 * '*', 'LISA\'S NAIL POLISH ROOM', 7* '*') #header 
    print('1. Random Nail Polish Picker') #random polish from xl 
    print('2. Enter A Number Polish Picker') #enter a number from xl
    print('3. Seasonal Manicure Picker') #seasonal function
    print('4. Exit') # exit
    print(39 * '*')
    
    while True: # loop for options
        choice = 0 # setting int input to 0
        print("Which would you like? Enter 1-4: ")
        #try statement to catch errors
        try:
            choice = int(input()) # getting selection from user
        except ValueError: # error if not an option or int
            print('Invalid input. Try again')

        if choice == 1:
            print('\nRandom Nail Polish Picker Selected') # from polish
            polish.randpol()
            playloop()
        elif choice == 2:
            print('\nEnter A Number Polish Picker Selected') # from polish
            polish.number()
            playloop()
        elif choice == 3:
            print('\nSeasonal Color Picker Selected') # from szn
            szn.seasons() # import seasonal functions (as seen in midterm project)
            playloop()
        elif choice == 4:
            print('\nThanks for playing!')
            sys.exit() # exit game
        else:
            continue

main()
