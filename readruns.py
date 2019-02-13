'''
    readruns
'''

def add(numList):
    return sum(i for i in numList)
    

with open('runs.txt') as FH:
    all_lines = FH.read()
    numbersStr = all_lines.split("\n")
    numbers = [int(i) for i in  all_lines.split("\n")]
    print(sorted(numbers))
    print (add(numbers))


print(sum( [ int (val) for val in open("runs.txt")]))
