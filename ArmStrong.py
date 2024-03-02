"""Let's calculate the sum of the cubes of the digits of 123 to see if it equals 123 itself:
    1+8+27=36
As you can see, the sum of the cubes of the digits (which is 36) is not equal to the original number (123). 
Therefore, 123 does not qualify as an Armstrong number."""

def arm_strong(num):
    order = len(str(num))
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum += (last_digit ** order) 
        num = num // 10
    return sum == order

numb = 111
res = arm_strong(numb)
print(res)

"""This Python code defines a function `arm_strong` that checks if a given number is an Armstrong number. 
    An Armstrong number (also known as a narcissistic number, plenary number, or pluperfect digital invariant) 
    of order `n` is an integer such that the sum of its own digits raised to the power of `n` is equal to the number itself. 
    Here's how the code works:

1. `def arm_strong(num):`: This line defines a function named `arm_strong` which takes one parameter `num`, representing the 
    number to be checked for being an Armstrong number.

2. `order = len(str(num))`: This line calculates the number of digits in the input number `num` by converting it to a string using 
    `str()` and then finding its length using `len()`. This determines the order of the Armstrong number.

3. `sum = 0`: This line initializes a variable `sum` to store the sum of the digits raised to the power of `order`.

4. The `while` loop:
   - `while num > 0:` This loop continues as long as the value of `num` is greater than `0`.
   - Inside the loop:
     - `last_digit = num % 10`: This line extracts the last digit of the number `num`.
     - `sum += (last_digit ** order)`: This line adds the `order`th power of the last digit to the variable `sum`.
     - `num = num // 10`: This line updates the value of `num` by removing the last digit, effectively moving towards the beginning of the number.

5. `return sum == order`: After the loop completes, the function returns `True` if the sum of the digits raised to the power of `order` 
    is equal to the original number `num`. Otherwise, it returns `False`.

6. `numb = 111`: This line defines a variable `numb` containing the value `111`.

7. `res = arm_strong(numb)`: This line calls the `arm_strong` function with the argument `numb` and stores the result in the variable `res`.

8. `print(res)`: This line prints the result, which indicates whether the number `111` is an Armstrong number or not.

In summary, the function checks whether a given number is an Armstrong number by summing the digits raised to the power of the 
number of digits and comparing the result with the original number. If they are equal, it returns `True`; otherwise, it returns `False`."""