def palindrome(strs):
    left = 0
    right = len(strs) - 1
    while left < right:
        if strs[left] != strs[right]:
            return False
        left+=1
        right-=1
    return True
    
strs = "RacecaR"
res = palindrome(strs)
print(res)

"""This code defines a function `palindrome` that checks if a given string is a palindrome, meaning it reads the same forwards and backwards. Here's how it works:

1. `def palindrome(strs):`: This line defines a function named `palindrome` that takes one argument `strs`, representing the string to check for being a palindrome.

2. `left = 0` and `right = len(strs) - 1`: These lines initialize two pointers, `left` pointing to the start of the string, and `right` pointing to the end of the string.

3. `while left < right:`: This sets up a while loop that continues as long as the `left` pointer is less than the `right` pointer, indicating that there are still characters to compare.

4. Inside the loop:
   - `if strs[left] != strs[right]:` This checks if the characters at the `left` and `right` pointers are not equal. If they're not, 
      it means the string is not a palindrome, so the function returns `False`.
   - `left+=1` and `right-=1`: These statements move the `left` pointer to the right and the `right` pointer to the left, respectively, 
      to continue comparing characters towards the center of the string.

5. If the loop completes without returning `False`, it means all characters were matching, so the string is a palindrome, and the function returns `True`.

6. `strs = "RacecaR"`: This line defines a string `strs` containing the value "RacecaR".

7. `res = palindrome(strs)`: This line calls the `palindrome` function with the string `strs` and stores the result in the variable `res`.

8. `print(res)`: This line prints the result, indicating whether the string is a palindrome or not.

In this case, since "RacecaR" reads the same forwards and backwards, the output would be `True`."""