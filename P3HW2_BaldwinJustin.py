#CTI-110-0901
#P3HW2 Pizza Order
#Justin Baldwin
#03/24/2022

num_students = int(input('How many students do you want to order pizza for? '))
PPP = float(input('Enter number of people per pizza (1.5, 2 or 3): '))
Num_Pizza = round(num_students / PPP)
Price = Num_Pizza * 5
Tax_price = Price * .06
Total_price = Price + Tax_price
Total_price =  format(Total_price, '.2f')

if PPP != 1.5 and PPP != 2 and PPP != 3:
    print('INVALID ENTRY!!!! \nShould have entered 1.5, 2 or 3 \nRun Program again')

print('----Pizza Order--------')
print('Number of Students :', num_students)
print('Pizzas Needed :', Num_Pizza)
print('Price $', Total_price)
print('--------------------------')

#Acquire number of students from user
#Acquire number of students per pizza from user
#To find number of pizzas needed divide number of students by number of students per pizza then round to whole number
#To find the price for all pizzas multiple number of pizzas times 5 as each pizza is $5
#To get the price of tax multiple the price of number of pizzas by .06 for 6% sales tax
#For the total price add the sales tax to price of number of pizzas
#Apply descion structure to notify user of incorrect input if numbers do not equal 1.5, 2 or 3 and display error message of invalid input and to run program again
#Print all results in order to allow user to read easily

