# polish.py
# INF360 - Programming in Python
# Lisa Thoms
# Final Project

"""
This will create the nail polish objects
with name, brand, type (base/top), and color

Importing excel spreadsheet for data using pandas
"""

# need to install: pandas, random
import pandas as pd
import random
import logging

## adding required logging - chose to import to file 
logging.basicConfig(filename='myProgramLog.txt',
                    level=logging.DEBUG,
                    format=' %(asctime)s -  %(levelname)s-  %(message)s')

#i import excel file and rename
polishfile = 'lisanailpolish.xlsx'
lnp = pd.read_excel(polishfile)
# create dictionary from excel file
lnp.to_dict()


# setting min row
min = 0
# get length of spreadsheet, set max rows
max = len(lnp)

# the user can select a number themselves 1 through length of xlsx
def number():
    userint = 0 # set default
    while True:
        print('\nPlease select a number 0 through ' +str(max)+ ': ')
        try:
            userint = int(input()) # getting selection from user
            logging.info(userint)
        except ValueError: # error if not an option or int
            print('Invalid input. Try again.')
            
        if userint > min and userint < max:
            tempdict = []
            tempdict = lnp.iloc[userint, [0,1,2,3]].head()
            print('Polish #' +str(userint)+ ' is...')
            print(tempdict.to_string())
            break
        else:
            continue # continue until valid input

    print('\nDo you want a different polish? Y or N: ')
    # while loop to go back through game until user selects no
    # then loop to main menu
    while True:
        newNum = input()
        if newNum.upper() == 'N' or newNum.upper() == 'NO':
            # exit minigame
            break
        elif newNum.upper() == 'Y' or newNum.upper() == 'YES':
            number() # going back to num picker
            break
        elif newNum.upper() != ('N', 'NO', 'Y', 'YES') or newNum.isalnum():
            print('\nPlease enter a valid input. Y or N.')
            # proceed back to start to enter correct input
            continue


# user chose random polish generator
# game will choose a random polish from xlsx
def randpol():
    print("\nGenerating a random polish from the collection...\n")
    # min and max set above
    randomPolish = random.randrange(min, max)
    logging.info(randomPolish)
    rand = lnp.loc[randomPolish]
    print('Polish #' +str(randomPolish)+ ' is...')
    print(rand.to_string())

    print('\nDo you want a different polish? Y or N: ')
    # while loop to go back through game until user selects no
    # then loop to main menu
    while True:
        newRan = input()
        if newRan.upper() == 'N' or newRan.upper() == 'NO':
            # exit minigame
            break
        elif newRan.upper() == 'Y' or newRan.upper() == 'YES':
            print('\nLet\'s try again.')
            randpol() # going back to num picker
            break
        elif newRan.upper() != ('N', 'NO', 'Y', 'YES') or newRan.isalnum():
            print('\nPlease enter a valid input. Y or N.')
            # proceed back to start to enter correct input
            continue

