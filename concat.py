fullTxt = input("Enter the sentence:")
splitted = fullTxt.split()
finalStr = "#"
idx = 0
while(idx<len(splitted)):
    finalStr = finalStr+splitted[idx].capitalize()
    print(idx, finalStr)
    idx += 1

print(finalStr)
