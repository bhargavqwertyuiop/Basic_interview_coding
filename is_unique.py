def is_unique(strs):
    unique_chars = set()
    for char in strs:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    return True

strs = "Race"
res = is_unique(strs)
print(res)

"""This Python code defines a function `has_unique_characters` that checks whether a given string contains only unique characters. Here's how it works:

1. `def has_unique_characters(string):`: This line defines a function named `has_unique_characters` which takes one parameter `string`, 
    representing the string to be checked for unique characters.

2. `char_set = set()`: This line initializes an empty set `char_set` which will store unique characters encountered in the string.

3. `for char in string:`: This sets up a loop that iterates over each character `char` in the input string.

4. `if char in char_set:`: Inside the loop, this line checks if the current character `char` is already present in the set `char_set`. 
    If it is, it means the character is not unique, so the function returns `False`.

5. `char_set.add(char)`: If the character is not already in the set, it is added to the set using the `add()` method. 
This ensures that only unique characters are stored in the set.

6. After the loop completes, if the function hasn't returned `False`, it means all characters in the string are unique, so the function returns `True`.

7. The example usage demonstrates how to call the `has_unique_characters` function with different strings and prints 
    whether they contain only unique characters or not.

So, in summary, the function checks whether a given string contains only unique characters by iterating over each character and storing them in a set. 
If any character is encountered more than once, the function returns `False`; otherwise, it returns `True`."""