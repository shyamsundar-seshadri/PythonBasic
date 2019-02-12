'''
    reader
'''

def print_lines():
    with open('captains.txt') as FH:
        for lines in FH:
            print (lines)
    

def fetch_lines(fileName, startLine, endLine):
    with open(fileName) as FH:
        lines = FH.read()
        split_lines = lines.split("\n")
        if endLine == 0:
            endLine = len(split_lines)
        while startLine < endLine:
            print(split_lines[startLine])
            startLine += 1
            
if __name__ == "__main__":
    print_lines()
