def second_largest(nums):
    if(len(nums) < 2):
        return None
    max_num = float('-inf')
    sec_num = float('-inf')
    for num in nums:
        if num > max_num:
            sec_num = max_num
            max_num = num
        elif num > sec_num and num != max_num:
            sec_num = num
    if sec_num == float('-inf'):
        return None
    return sec_num

nums = [1,2,3,4,5]
res = second_largest(nums)
print(res)

"""This Python code defines a function `second_largest` that finds the second largest element in a given list. Here's how the code works:

1. `def second_largest(arr):`: This line defines a function named `second_largest` which takes one parameter `arr`, representing the input list.

2. `if len(arr) < 2:`: This `if` statement checks if the length of the input list `arr` is less than `2`. If it is, it means 
    there are fewer than two elements in the list, and in such cases, there is no second largest element, so the function immediately 
    returns `None`.

3. `max_num = float('-inf')` and `second_max = float('-inf')`: These lines initialize two variables, `max_num` and `second_max`, 
    to negative infinity. These variables will keep track of the maximum and second maximum elements encountered in the list so far.

4. The `for` loop:
   - `for num in arr:` This loop iterates over each element `num` in the input list `arr`.
   - Inside the loop:
     - `if num > max_num:` This `if` statement checks if the current element `num` is greater than the current maximum `max_num`.
       - If it is, it updates the second maximum `second_max` to the value of the current maximum `max_num`, and then updates the 
         maximum `max_num` to the value of the current element `num`.
     - `elif num > second_max and num != max_num:` This `elif` statement checks if the current element `num` is greater than 
        the current second maximum `second_max` and not equal to the maximum `max_num`.
       - If it is, it updates the second maximum `second_max` to the value of the current element `num`.
   
5. After the loop completes, if the second maximum remains as negative infinity, it means there is no distinct second maximum 
    element in the list (e.g., all elements are the same). In such cases, the function returns `None`. Otherwise, 
    it returns the value of `second_max`, which represents the second largest element in the list.

6. The example usage demonstrates how to call the `second_largest` function with a list `[3, 1, 4, 2, 5]` and 
    prints the result, which is the second largest element `4`.

In summary, the function iterates through the list once to find the second largest element by keeping track of the 
maximum and second maximum elements encountered. It returns the second largest element if it exists; otherwise, it returns `None`."""
