def missing_num_sequence(arr):
    arr.sort()
    n = len(arr)
    total_sum = (n+1) * (n+2) // 2
    execpted_sum = sum(arr)
    return total_sum - execpted_sum

nums = [1,2,3,5]
res = missing_num_sequence(nums)
print(res)

""" 
1. `arr.sort()`: The function sorts the input list `arr` in ascending order using the `sort()` method. 
    This ensures that the sequence is arranged in the correct order for further processing.

2. `n = len(arr)`: The variable `n` is assigned the length of the sorted list `arr`. 
    This value represents the number of elements in the sequence.

3. `total_sum = (n+1) * (n+2) // 2`: The total sum variable `total_sum` is calculated using the formula for the sum of an arithmetic series, 
    where `(n+1)` represents the number of elements in the sequence (including the missing number), and `// 2` is used to perform integer division. The sum is calculated up to `n+1` because the sequence is expected to have `n+1` elements when including the missing number.

4. `expected_sum = sum(arr)`: The `expected_sum` variable is calculated by summing all the numbers in the sorted list `arr`. 
    This represents the sum of the numbers that are actually present in the sequence.

5. `return total_sum - expected_sum`: The missing number is determined by subtracting the `expected_sum` from the `total_sum`. 
    This calculation reveals the difference between the sum of the complete sequence and the sum of the numbers actually present, 
    which corresponds to the missing number.

6. `print(res)`: Finally, the function's result, which represents the missing number, is printed to the console."""