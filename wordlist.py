s=input("enter a sentences:")
print(s)
wordslist=s.split()
print(wordslist)
uniquewords=set(wordslist)
for word in uniquewords:
    print(f"{word}occurs{wordslist.count(word)}times")
    
