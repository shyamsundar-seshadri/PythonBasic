'''
    Tally
'''
import calculator as calc

veg_cost = 120
fruits_cost = 55
cash_payed = 200
cart_total = calc.add(veg_cost , fruits_cost)
print("Veg Cost",veg_cost)
print("Fruits Cost", fruits_cost)
print("Customer Paid",cash_payed)
print("Cashier should pay him",calc.sub(cash_payed,cart_total))

