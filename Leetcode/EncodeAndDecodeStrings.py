



dummy_input = ["Hello","World"]


# Encode
# Send to decode then return decoded
# Return decoded list


def encode(strs):

    arr = []

    for str in strs:
        encrypt = f"#{len(str)}"
        str = f"{encrypt}{str}"
        arr.append(str)
    res = "".join(arr)
    print(res)
        

    strs2 = decode(res);

    return strs2


def decode(s):

    arr = []
    i = 0

    while i < len(s): 

        if s[i] == "#":
            j = i + 1      # ADDED: pointer to read the full length

            while j < len(s) and s[j].isdigit():  # ADDED: supports multi-digit lengths
                j += 1

            length = int(s[i + 1:j])  # CHANGED: read full number, not just one char
            start = j                 # CHANGED: word starts after the length
            end = start + length

            word = s[start:end]
            arr.append(word)

            i = end           # CHANGED: actually skip past the decoded word
        else:
            i += 1            
    return arr
            




print(encode(dummy_input))