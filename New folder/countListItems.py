# count-list-items-1.py

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'

print("wordstring: ", wordstring)

wordlist = wordstring.split()
print("wordlist: ", wordlist)

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))
myPairFreList = list(zip(wordlist, wordfreq))

print("my list: ", myPairFreList)
print("Pairs Frequency\n", myPairFreList.sort())

