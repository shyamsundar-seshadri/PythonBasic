'''
    inspector
'''

import readfile as readFile
import sys

fileName = ""
startLineArg = ""
endLineArg = ""

argSize = len(sys.argv)
if argSize > 3:
    endLineArg = sys.argv[3]
if argSize > 2:
    startLineArg = sys.argv[2]
if argSize > 1:
    fileName = sys.argv[1]

if startLineArg == "":
   startLine = 0
else:
    startLine = int(startLineArg)

if startLineArg  == "":
    endLine = 0
else:
    endLine = int(endLineArg)

if fileName != "":
    readFile.fetch_lines(fileName,startLine,endLine )

