# seasonal.py
# Lisa Thoms
# Final Project

# these are the functions seen in my midterm, fixed and one of the menu options.

import random

def seasons():
    print('\nWhat season is it? Spring, Summer, Fall, Winter?')
    
    while True:
        curSeason = input() #getting season input
        # random number between 1-7 for color grab
        randomColor = random.randint(0,6)
        if curSeason.lower() == 'spring':
            spring(randomColor)
            break
        elif curSeason.lower() == 'summer':
            summer(randomColor)
            break
        elif curSeason.lower() == 'fall':
            fall(randomColor)
            break
        elif curSeason.lower() == 'winter':
            winter(randomColor)
            break
        elif curSeason.lower() != ('spring', 'summer', 'fall', 'winter') or curSeason.isalnum():
            print('\nPlease enter a valid season. Spring, Summer, Fall, Winter')
            continue

#creating the color lists for the seasons
#each list has 7 colors
springColors = ['peach', 'light pink', 'mint green', 'baby blue', 'nude', 'soft yellow', 'lavender']
summerColors = ['white', 'yellow', 'bright red', 'orange', 'fuchsia', 'turquoise', 'royal blue']
fallColors = ['brown', 'mustard yellow', 'burnt orange', 'hunter green', 'mauve', 'maroon', 'black']
winterColors = ['white', 'black', 'dark grey', 'ruby red', 'dark purple', 'emerald green', 'dark blue']

# creating the season type functions, using the randomColor int to pick from the lists
def spring(randomColor): #spring
    # generate the random color from the list
    print('\nThe color you should pick is ' + springColors[randomColor] + '.')
    topper()
    
def summer(randomColor): #summer
    # generate the random color from the list
    print('\nThe color you should pick is ' + summerColors[randomColor] + '.')
    topper()

def fall(randomColor): #fall
    # generate the random color from the list
    print('\nThe color you should pick is ' + fallColors[randomColor] + '.')
    topper()
    
def winter(randomColor): #winter
    # generate the random color from the list
    print('\nThe color you should pick is ' + winterColors[randomColor] + '.')
    topper()

#creating the topper list
toppers = ['holographic', 'flakies', 'glitter', 'microshimmer']

def topper(): #topper function (this is what makes a nail polish pretty!)
    print('\nDo you want a nail polish topper?')
    while True:
        topper = input() #getting input
        # random number between 1-4 for topper grab
        randomTop = random.randint(0,3)
        if topper.upper() == 'N' or topper.upper() == 'NO':
            print('A clear glossy top coat it is!')
            break
        elif topper.upper() == 'Y' or topper.upper() == 'YES':
            print('The topper you should use is ' + toppers[randomTop] + '.')
            break
        elif topper.upper() != ('N', 'NO', 'Y', 'YES') or topper.isalnum():
            print('\nPlease enter a valid input. Y or N.')
            continue

    print('\nDo you want a different combination? Y or N: ')
    # while loop to go back through game until user selects no
    # then loop to main menu
    while True:
        newCombo = input()
        if newCombo.upper() == 'N' or newCombo.upper() == 'NO':
            # exit minigame
            break
        elif newCombo.upper() == 'Y' or newCombo.upper() == 'YES':
            print('\nLet\'s try again.')
            seasons() # going back to num picker
            break
        elif newCombo.upper() != ('N', 'NO', 'Y', 'YES') or newCombo.isalnum():
            print('\nPlease enter a valid input. Y or N.')
            # proceed back to start to enter correct input
            continue
        
