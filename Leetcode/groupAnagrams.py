


strs = ["act","pots","tops","cat","stop","hat"]



sArray = []
aHash = {}

for string in strs:
    word = sorted(string)
    print(word)
    word = "".join(word)
    print(word)

    print(string)
    aHash[word] = aHash.get(word, []) + [string]
    
for char in aHash:
    sArray.append(aHash[char])


print(sArray)
print(aHash)
