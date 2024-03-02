def are_anagrams(str1,str2):
    if len(str1) != len(str2):
        return False
    
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        else:
            return False
        
    return len(char_count) == 0

str1 = "silent"
str2 = "listen"
res = are_anagrams(str1,str2)
print(res)


"""This Python code defines a function `are_anagrams` that checks if two given strings are anagrams of each other. 
    Anagrams are words or phrases formed by rearranging the letters of another word or phrase. Here's how the code works:

1. `def are_anagrams(str1, str2):`: This line defines a function named `are_anagrams` which takes two parameters `str1` and `str2`, 
    representing the two strings to be checked for anagrams.

2. `if len(str1) != len(str2):`: This `if` statement checks if the lengths of the two input strings `str1` and `str2` are not equal. 
    If they are not equal, it means the strings cannot be anagrams (since anagrams must have the same number of characters), 
    so the function immediately returns `False`.

3. `char_count = {}`: This line initializes an empty dictionary `char_count` which will store the count of each character in `str1`.

4. The first `for` loop:
   - `for char in str1:` This loop iterates over each character `char` in the first string `str1`.
   - Inside the loop:
     - `if char in char_count:` This `if` statement checks if the current character `char` is already present in the `char_count` dictionary.
       - If it is, it increments its count in the dictionary by 1.
       - If it's not, it adds the character to the dictionary with a count of 1.

5. The second `for` loop:
   - `for char in str2:` This loop iterates over each character `char` in the second string `str2`.
   - Inside the loop:
     - `if char in char_count:` This `if` statement checks if the current character `char` is present in the `char_count` dictionary.
       - If it is, it decrements its count in the dictionary by 1, effectively canceling out the occurrence of that character in `str2`.
       - If the count becomes zero after decrementing, the character is removed from the dictionary.
       - If the character is not found in the dictionary, it means `str2` contains a character not present in `str1`, 
        so the function returns `False`.

6. After both loops, if the lengths of `str1` and `str2` are equal and all characters in `str2` have been accounted for, 
    the function checks if the dictionary `char_count` is empty. If it is, it means all characters in `str1` have been 
    canceled out by their occurrences in `str2`, and vice versa, so the function returns `True` indicating that the two strings are anagrams of each other.

7. The example usage demonstrates how to call the `are_anagrams` function with different strings and prints whether they are anagrams or not.

In summary, the function determines whether two strings are anagrams by counting the occurrences of each character in both strings 
and ensuring they have the same counts for each character. If they do, the strings are anagrams, and the function returns `True`; 
otherwise, it returns `False`."""
