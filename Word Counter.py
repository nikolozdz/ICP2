def capitalize(word):
    if word.isalpha():
        word=word.lower()
        word=word[0].upper()+word[1:]
    return word

wordCount=dict() # Dictionary on
file = open('readFile.txt','r')
lines = file.readlines()
file.close()
filteredText=''
for line in lines:
    if line!='\n':
        filteredText+=(line.replace('\n',' '))

print(filteredText)

filteredText=filteredText.split(' ')

for word in filteredText:
    capitalized=capitalize(word)
    if capitalized in wordCount:
        wordCount[capitalized]+=1
    else:
        wordCount[capitalized]=1

print(wordCount)

writeFile = open('writeFile.txt','w')
for keys in wordCount:
    writeFile.write("{}:{} \n".format(keys,wordCount[keys]))

writeFile.close()




