def is_prime(nums):
    if(nums<=1):
        return False
    else:
        for num in range(2,int(nums ** 0.5)+1):
            if(nums%num == 0):
                return False
        return True
    
nums = 4
res = is_prime(nums)
print(res)

"""This Python code defines a function `is_prime` that checks whether a given number `num` is a prime number or not. Here's how it works:

1. `def is_prime(num):`: This line defines a function named `is_prime` that takes one argument `num`, representing the number to check for primality.

2. `if num <= 1:`: This `if` statement checks if the given number `num` is less than or equal to `1`. Prime numbers are defined as natural numbers greater than `1`. 
    So, if `num` is less than or equal to `1`, the function immediately returns `False` indicating that it's not a prime number.

3. `for i in range(2, int(num**0.5) + 1):`: This sets up a `for` loop that iterates over numbers `i` from `2` to the square root of `num` (inclusive), 
    which is represented as `int(num**0.5) + 1`. This range is chosen because if `num` has any divisors, they must be less than or equal to its square root.

4. Inside the loop:
   - `if num % i == 0:` This `if` statement checks if `num` is divisible by the current value of `i` without leaving a remainder. 
   If it is, then `num` is not a prime number, because it has a divisor other than `1` and itself. So, the function returns `False`.

5. If the loop completes without finding any divisors for `num`, the function returns `True`, indicating that `num` is a prime number.

6. The example usage demonstrates how to call the `is_prime` function with different numbers and prints whether they are prime or not.

So, in summary, the function determines whether a given number `num` is prime by checking if it has any divisors other than `1` and itself. 
If it does, it returns `False`; otherwise, it returns `True`. This is done by iterating up to the square root of `num` and checking for 
divisibility."""