def palin_number(num):
    if num < 10:
        return False
    else:
        original_number = num
        reversed_number = 0
        while num > 0:
            last_digit = num % 10
            reversed_number = (reversed_number*10) + last_digit
            num = num // 10
        return original_number == reversed_number
    
num = 102
res = palin_number(num)
print(res)

"""This Python code defines a function `palin_number` that checks if a given number is a palindrome number. A palindrome number is 
    a number that reads the same forwards and backwards. Here's how the code works:

1. `def palin_number(num):`: This line defines a function named `palin_number` which takes one parameter `num`, representing the 
    number to be checked for being a palindrome.

2. `if num < 10:`: This `if` statement checks if the input number `num` is less than `10`. If it is, it means the number is a single digit number, 
    and single digit numbers are not considered palindromes. So, the function immediately returns `False`.

3. `else:`: If the number is not a single digit number, the code execution continues to the `else` block.

4. `original_number = num`: This line stores the original value of the number in a variable `original_number` for comparison later.

5. `reversed_number = 0`: This line initializes a variable `reversed_number` to `0`. This variable will store the reversed version of the input number.

6. The `while` loop:
   - `while num > 0:` This loop continues as long as the value of `num` is greater than `0`.
   - Inside the loop:
     - `last_digit = num % 10`: This line extracts the last digit of the number `num`.
     - `reversed_number = (reversed_number*10) + last_digit`: This line builds the reversed number by shifting the existing 
        `reversed_number` left by one position and adding the last digit of `num` to the units place.
     - `num = num // 10`: This line updates the value of `num` by removing the last digit, effectively moving towards the beginning of the number.
     
7. `return original_number == reversed_number`: After the loop completes, the function returns `True` if the original number is equal 
    to its reversed version (`reversed_number`), indicating that it's a palindrome number. Otherwise, it returns `False`.

8. `num = 102`: This line defines a variable `num` containing the value `102`.

9. `res = palin_number(num)`: This line calls the `palin_number` function with the argument `num` and 
    stores the result in the variable `res`.

10. `print(res)`: This line prints the result, which indicates whether the number `102` is a palindrome number or not.

In summary, the function checks whether a given number is a palindrome number by reversing the number and comparing it with the original number. 
If they are equal, it returns `True`; otherwise, it returns `False`."""