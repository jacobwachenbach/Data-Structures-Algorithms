



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
        # CHANGED: ensure this '#' is actually a length header
        if s[i] == "#" and i + 1 < len(s) and s[i + 1].isdigit():
            j = i + 1

            while j < len(s) and s[j].isdigit():
                j += 1

            length = int(s[i + 1:j])
            start = j
            end = start + length

            word = s[start:end]
            arr.append(word)

            i = end
        else:
            i += 1  # CHANGED: safely skip literal characters like '#'

    return arr
            




print(encode(dummy_input))