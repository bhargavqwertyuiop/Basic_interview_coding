def reverse__words(str1):
    words = str1.split()
    reverse = words[::-1]
    newWords = ' '.join(reverse)
    return newWords

str1 = "New World"
res = reverse__words(str1)
print(res)

"""This Python code defines a function `reverse__words` that reverses the order of words in a given string. Here's how the code works:

1. `def reverse__words(str1):`: This line defines a function named `reverse__words` which takes one parameter `str1`, 
    representing the input string whose words need to be reversed.

2. `words = str1.split()`: This line splits the input string `str1` into a list of words using the `split()` method. 
    By default, `split()` splits the string based on whitespace characters.

3. `reverse = words[::-1]`: This line creates a new list `reverse` by slicing the `words` list with a step of `-1`, 
    effectively reversing the order of the words in the list.

4. `newWords = ' '.join(reverse)`: This line joins the elements of the `reverse` list into a single string `newWords`, 
    using a single whitespace `' '` as the separator between the words.

5. `return newWords`: This line returns the string `newWords`, which represents the original string with its words reversed.

6. `str1 = "New World"`: This line defines a variable `str1` containing the value `"New World"`.

7. `res = reverse__words(str1)`: This line calls the `reverse__words` function with the argument `str1` and 
    stores the result in the variable `res`.

8. `print(res)`: This line prints the result, which is the input string `"New World"` with its words reversed, resulting in `"World New"`.

In summary, the function takes an input string, splits it into words, reverses the order of the words, and then 
joins them back into a single string, effectively reversing the order of words in the original string."""