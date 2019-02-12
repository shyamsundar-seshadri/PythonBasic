'''
    Fibanocci
'''
print("#"*40)
print("Excercise 11 - Fibonocci")
def fibanocci(a,b):
    temp = a+b
    a = b
    b = temp
    return a,b


a=0
b=1
i = 1
rage_val = input("Enter Fibonocci limit: ")
print(a)
print(b)
while i < int(rage_val) - 1:
    (a,b) = fibanocci (a,b)
    print(b)
    i += 1
