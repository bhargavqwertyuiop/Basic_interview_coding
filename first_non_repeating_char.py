from collections import defaultdict

def non_repeating_chars(str1):
    char_count = defaultdict(int) # Initialize a defaultdict to store character counts
    for char in str1:
        char_count[char] += 1 # Increment count for each character
    for char in str1:
        if char_count[char] == 1:
            return char  # Return the first non-repeating character
    return None

str = "Bhargav"
res = non_repeating_chars(str)
print(res)
