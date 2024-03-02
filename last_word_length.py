def length_last_word(str1):
    newStr1 = str1.split()
    if len(newStr1) == 0:
        return 0
    return len(newStr1[-1])

string = "New City"
res = length_last_word(string)
print(res)