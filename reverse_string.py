def reverse_string(strs):
    reversed_str = " "
    for i in range(len(strs)-1,-1,-1):
        reversed_str = reversed_str + strs[i]
    return reversed_str

strs = "Hello"
res = reverse_string(strs)
print(res)

"""This Python code defines a function `reverse_string` that takes a string as input and returns the reversed version of that string.

Here's a breakdown of how the code works:

1. `def reverse_string(string):`: This line defines a function named `reverse_string` which takes one parameter `string`, 
    representing the string to be reversed.

2. `reversed_str = ''`: This line initializes an empty string `reversed_str` which will store the reversed version of the input string.

3. `for i in range(len(string)-1, -1, -1):`: This line sets up a for loop that iterates over the indices of the input string in reverse order. 
    It starts from the index `len(string)-1` (the last character of the string) and goes down to index `0` (the first character of the string), 
    moving backwards with a step of `-1`.

4. `reversed_str += string[i]`: Within the loop, each character of the input string is appended to the `reversed_str`, effectively 
    building the reversed string.

5. `return reversed_str`: Finally, the function returns the `reversed_str`, which contains the reversed version of the input string.

6. The example usage at the end `print(reverse_string("hello"))` demonstrates how to call the function with the string "hello" and 
    prints the reversed string "olleh" as the output."""