def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count = count + 1
    return count

str1 = "TheBigBoy"
res = count_vowels(str1)
print(res)

