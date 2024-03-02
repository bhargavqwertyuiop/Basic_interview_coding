def remove_duplcate(nums):
    non_duplicate_nums = []
    for num in nums:
        if num not in non_duplicate_nums:
            non_duplicate_nums.append(num)
    return non_duplicate_nums

or_list = [1,2,3,4,4,2,1,5]
res = remove_duplcate(or_list)
print(res)

"""This Python code defines a function `remove_duplicate` that removes duplicate elements from a given list. Here's how the code works:

1. `def remove_duplicate(nums):`: This line defines a function named `remove_duplicate` which takes one parameter `nums`, 
    representing the list from which duplicate elements need to be removed.

2. `non_duplicate_nums = []`: This line initializes an empty list `non_duplicate_nums` which will store the unique elements from the input list.

3. The `for` loop:
   - `for num in nums:` This loop iterates over each element `num` in the input list `nums`.
   - Inside the loop:
     - `if num not in non_duplicate_nums:` This `if` statement checks if the current element `num` is not already present in the 
        `non_duplicate_nums` list.
       - If it is not, it means the element is unique, so it's appended to the `non_duplicate_nums` list.

4. After the loop completes, the function returns the `non_duplicate_nums` list, which contains only the unique elements from the input list.

5. `or_list = [1,2,3,4,4,2,1,5]`: This line defines a list `or_list` containing some elements, including duplicates.

6. `res = remove_duplicate(or_list)`: This line calls the `remove_duplicate` function with the argument `or_list` and 
    stores the result in the variable `res`.

7. `print(res)`: This line prints the result, which is the list containing unique elements, as duplicates have been removed.

In summary, the function removes duplicate elements from a given list by iterating over each element and adding it to a new list 
only if it's not already present in the new list. This ensures that only unique elements are retained in the output list."""