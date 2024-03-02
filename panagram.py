#Pangram is a string that contains every letter of an alphabet atleast once

def pangram(str1):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    newStr1 = str1.lower()
    for char in alphabets:
        if char not in newStr1:
            return False
    return True

string = "The quick brown fox jumps over the lazy dog"
res = pangram(string)
print(res)

