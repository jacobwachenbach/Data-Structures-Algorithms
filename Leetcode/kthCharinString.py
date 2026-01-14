
letters = "abcdefghijklmnopqrstuvwxyz"
i = 0

def myString(k, word):
    if len(word) >= k:
        return word[k -1]
    shifted_copy = ""
    for char in word:
        # Find the next letter (with wrap-around logic using %)
        current_index = letters.find(char)
        next_index = (current_index + 1)
        shifted_copy += letters[next_index]
    
    # 2. Append the shifted copy to the word
    word = word + shifted_copy
    
    # 3. Repeat until word is long enough
    return myString(k, word)

print(myString(5, "a"))