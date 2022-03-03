#Program showing total cost of purchase plus sales tax
#03/01/2022
#CTI-110-P2HW1 - Total Purchases
#Justin Baldwin
#
item1 = float (input ('Price of item 1:' ))
item2 = float (input ( 'Price of item 2:' ))
item3 = float (input ( 'Price of item 3:' ))
item4 = float (input ( 'Price of item 4:' ))
item5 = float (input ( 'Price of item 5:' ))
Subtotal = item1 + item2 + item3 + item4 + item5
Tax = Subtotal * .07
Total = Subtotal + Tax

print('-------Results-------')
print('Subtotal:', round(Subtotal,2))
print('Sales Tax:', round(Tax,2))
print('Total:', round(Total,2))

