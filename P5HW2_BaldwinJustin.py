#Create a math quiz using loops, functions and imports
#04/28/2022
#CTI-110 P5HW2 - Math Quiz
#Justin Baldwin
#

import random

def addNums():
    num1 = random.randint(100,1000)
    num2 = random.randint(100,1000)
    print(' ' + str(num1))
    print('+' + str(num2))
    user_sum = int(input())
    if (user_sum == (num1 + num2)):
        print('Congratulations! Your answer is correct.')
        main()
    else:
        print('Sorry, your answer is incorrect.')
        print('The correct answer is:  ' + str(num1+num2))
        main()

def subNums():
    num1 = random.randint(100,1000)
    num2 = random.randint(100,1000)
    print(' ' + str(num1))
    print('-' + str(num2))
    user_sub = int(input())
    if (user_sub == (num1 - num2)):
        print('Congratulations! Your answer is correct.')
        main()
    else:
        print('Sorry, your answer is incorrect.')
        print('The correct answer is:  ' + str(num1-num2))
        main()

def main():
    print('MAIN MENU:')
    print('-----------------')
    print('1) Add Random Numbers')
    print('2) Subtract Random Numbers')
    print('3) Exit')
    menu_input = int(input('Please choose a menu option:  '))
    if (menu_input == 1):
        addNums()
    elif (menu_input == 2):
        subNums()
    elif (menu_input == 3):
        print('Thank you have a good day!')
        exit()
    else:
        print('INVALID CHOICE')
        print('Please choose valid option; 1, 2 or 3')
        main()


main()
    
        
