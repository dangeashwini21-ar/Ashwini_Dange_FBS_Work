
str=[
     "Firstbit solution is a"
     "training and placement "
    "institute in pune"
     "It is good institute "
     ]


words="".join(str).split()
uniqueWords=set(words)
print("unique words :",uniqueWords)
for word in uniqueWords:
    print(word,":",words.count(word))