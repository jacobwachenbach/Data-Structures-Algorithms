
# Problem:
# Two strings needle & haystack
# Return the index of first appearance of needle in haystack
# Return -1 if needle is not in haystack

# for loop through string
# Find inital char like s. thats when we start our search, store the index of potential char
# Loop for the length of needle inside the if 
# Return the index of first char if all matches

haystack = "sadbutsad"
needle = "sad"





def my_haystack():

    for i in range(len(haystack)):
        if haystack[i] == needle[0]: # 2
            for k in range(1, len(needle)):
                if needle[k] != haystack[i + k]:
                    break
                if k == len(needle) - 1 and needle[k] == haystack[i + k]:
                    return i
    return -1
            





print(my_haystack())