def sum_of_digits(nums):
    sum = 0
    while nums>0:
        sum = sum + nums%10
        nums = nums // 10
    return sum

nums = 1234
res = sum_of_digits(nums)
print(res)

"""This Python code defines a function `sum_of_digits` that calculates the sum of the digits of a given number. Here's how it works:

1. `def sum_of_digits(nums):`: This line defines a function named `sum_of_digits` which takes one parameter `nums`, 
    representing the number for which the sum of digits needs to be calculated.

2. `sum = 0`: This line initializes a variable `sum` to store the sum of the digits. It starts at `0`.

3. `while nums > 0:`: This sets up a while loop that continues as long as the value of `nums` is greater than `0`. 
    This loop iterates through each digit of the number.

4. Inside the loop:
   - `sum = sum + nums % 10`: This line adds the last digit of `nums` to the current value of `sum`. 
    The last digit of a number can be obtained by performing modulo (`%`) operation with `10`.
   - `nums = nums // 10`: This line updates the value of `nums` by removing the last digit. 
    This is achieved by performing integer division (`//`) with `10`.

5. Once the loop completes, all digits of the number have been added to `sum`, and the function returns the final value of `sum`, 
which represents the sum of the digits of the given number.

6. `nums = 1234`: This line defines a variable `nums` containing the value `1234`.

7. `res = sum_of_digits(nums)`: This line calls the `sum_of_digits` function with the argument `nums` and stores the result in the variable `res`.

8. `print(res)`: This line prints the result, which is the sum of the digits of the number `1234`.

In this case, the sum of the digits of the number `1234` is `1 + 2 + 3 + 4 = 10`, so the output of the code will be `10`."""