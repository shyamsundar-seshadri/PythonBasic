'''
    
'''

wordsCount = 0
aCount = 0
vowels = ['a','e','i','o','u']

with open('news.txt') as FH:
    sentences = FH.read()
    editSentence = sentences.replace('.', ' ')
    for word in editSentence.split(' '):
        wordsCount += 1
        if 'a' in word:
            aCount += 1


print (wordsCount, aCount)
