str=input("enter the string: ")
charCount=0
wordCount=1
for ch in str:
    charCount+=1
    if ch==' ':
        wordCount+=1
print(charCount)
print(wordCount)