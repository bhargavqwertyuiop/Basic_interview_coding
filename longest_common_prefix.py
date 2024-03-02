def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


arr = ["flower",'flows','flight']
res = longest_common_prefix(arr)
print(res)

"""The function takes a list of strings strs as input.

If the list is empty (if not strs:), it means there are no strings, so it returns an empty string.

Otherwise, it initializes the prefix with the first string in the list (prefix = strs[0]).

It iterates over the remaining strings in the list (for string in strs[1:]).

For each string, it checks if it starts with the current prefix. If not (while string.find(prefix) != 0:), 
it removes the last character from the prefix (prefix = prefix[:-1]).

If the prefix becomes empty during this process (if not prefix:), 
it means there's no common prefix among the strings, so it returns an empty string.
Finally, it returns the longest common prefix found"""