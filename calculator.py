'''
    Calculator
'''

def add(x,y):
    return x+y

def sub(big,small):
    return big-small

def multiply(x=1,y=1):
    return x*y

def divide(big,small):
    return big/small

def percent(big, small):
    return big*(small/100)

#Main Start here
a=10
b=20
print("addition of ",a,"and",b,"is :",add(a,b))
print("subtraction of ",a,"and",b,"is :",sub(b,a))
print("multiplication of ",a,"and",b,"is :",multiply(b,a))
print("division of ",a,"and",b,"is :",divide(b,a))
print("percentage of ",a,"and",b,"is :",percent(b,a))
print('\n\n')
print("#"*20)
print('World Cup Finals')
print("#"*20)
aus_inn1_run = 250
ind_inn1_run = 220
aus_inn2_run = 150
tot_aus_run = add(aus_inn1_run, aus_inn2_run)
print('Aus Innings 1:',aus_inn1_run)
print('India Innings 1:', ind_inn1_run)
print('Aus Innings 2:', aus_inn2_run)
print("Runs Required by India:", add(sub(tot_aus_run , ind_inn1_run),1) )

print("#"*40)
print('\n\n')

veg_cost = 120
fruits_cost = 55
cash_payed = 200
cart_total = veg_cost + fruits_cost
print("Cashier should pay him",sub(cash_payed,cart_total))

print("#"*40)
print("#"*20)
print("Default Params")
print("#"*20)
print(multiply())
print(multiply(10))
print(multiply(10,2))
print("#"*40)

print("Excercise 09")
print('###odd numbers from 120 to 150##')
vals = range(121,150,2)
print("odd nums are:")
for val in vals:
    print(val)

print("Excercise 10")
vals = range(94,109)
for val in vals:
    if(val%100 == 0):
        print(val/2)
    elif(val %100 == 1):
        print(val * 2)

print("Excercise 11 - Fibonocci")
def fibanocci(a,b):
    temp = a+b
    a = b
    b = temp
    return a,b

print("#"*40)
a=0
b=1
i = 1
rage_val = input("Enter Fibonocci limit")
print(a)
print(b)
while i < int(rage_val) - 1:
    (a,b) = fibanocci (a,b)
    print(b)
    i += 1

print("#"*40)
print("Excercise 12")
lucky_num = 12
user_num = 0
user_num = input("Give it first try: ")
while int(lucky_num) != int(user_num):
    if abs(int(lucky_num) -  int(user_num)) < 3:
        user_num = input("Dood . Yo Almost There !!. Just Try Once Again: ")
    elif int(lucky_num) > int(user_num):
        user_num = input("Hmm :( Too Low ! Try Again: ")
    else:
        user_num = input("Woah ! That's too high. Try again: ")
        

print("Bingo !! Yo Got it right !! There you go. IT IS - ",lucky_num)

    

