#CTI-110-0901
#P4HW2 - Pizza Order
#Justin Baldwin
#04/04/2022
#

import math

condition = True
while condition:
    students = int(input('Enter the number of students: '))
    num_ppl = float(input('Enter the number of people per pizza: (1.5, 2 or 3)'))
    
    if num_ppl == 1.5 or num_ppl == 2 or num_ppl == 3:
        whole_pizzas = math.ceil(students / num_ppl)
        price = whole_pizzas * 5
        price = price + (price * 0.06)
        print('----Pizza Order-------')
        print('Number of stuents: ', students)
        print('Number of Pizzas: ', whole_pizzas)
        print('Price: $', price)
        print('------------------------')

    elif num_ppl != 1.5 or num_ppl != 2 or num_ppl != 3:
        print('INVALID ENTRY!!!')
        print('Should have entered 1.5, 2 or 3')
        num_ppl = float(input('Enter number of people per pizza again (1.5, 2 or 3): '))
        
    if input('Would you like to run the program again? (y for yes) ') == 'y':
        continue
    else:
        break



#PSEUDOCODE
#Import math functions
#Set while condition to true
#Define while condition
#Ask user for input of number of students
#Ask use for input of how many students per whole pizza has to be 1.5, 2 or 3
#Set if condition for num_ppl being equal to 1.5, 2 or 3
#If num_ppl is equal to 1.5, 2 or 3 number of whole_pizzas is a rounded answer using ceil of students divided by num_pp;
#Find price by multiple whole_pizzas by 5 as each pizza is $5
#Find price plus sales tax by adding price to the product of price and 0.06
#Print out ---pizza order---
#Print the number of students
#Print the number of whole_pizzas
#Print price
#Set condition if num_ppl does not equal 1.5, 2 or 3
#If not equal to 1.5, 2 or 3 print INVALID ENTRY!!!
#Print should have been 1.5, 2 or 3
#Prompt user to re-enter using a correct number and run program correctly
#Set if condition to prompt user asking if they want to run the program again
#If user input is y for yes continue to restart the program over and run again
#If user input is anything but y break program




  
    


    
        
