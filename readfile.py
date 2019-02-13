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

        if startLine > len(split_lines):
            print (f"Start Line {startLine} is greater than File Line Count {len(split_lines)}")
            return

        elif endLine > len(split_lines):
            print (f"Start Line {endLine} is greater than File Line Count {len(split_lines)}")
            return
        
        while startLine < endLine:
            print(split_lines[startLine])
            startLine += 1

            
if __name__ == "__main__":
    print_lines()
