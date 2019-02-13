'''
    list practice
'''

runs = [70,110,30,90,40]
runClone = runs[:]
runs.sort()
print(runs)
runs.sort(reverse = True)
print(runs)
print("Original List:",runClone)
print(sorted(runs))
