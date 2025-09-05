li=['eat','listen','tea','silent','cat','bat','ate']
anagram={}
for i in li:
    key=''.join(sorted(i))
    if key not in anagram:
        anagram[key]=[]
    anagram[key].append(i)
for i in anagram.values():
    print(i)
    