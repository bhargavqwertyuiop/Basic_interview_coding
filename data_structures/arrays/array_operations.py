"""
Array Operations - Comprehensive Implementation

This module demonstrates fundamental array operations with detailed explanations,
time/space complexity analysis, and multiple test scenarios.

Arrays are fundamental data structures that store elements in contiguous memory locations.
They provide O(1) access time but may require O(n) time for insertions and deletions.

Author: Algorithm Learning Repository
Time Complexity Analysis: Included for each operation
Space Complexity Analysis: Included for each operation
"""

class DynamicArray:
    """
    A dynamic array implementation that can grow and shrink as needed.
    Similar to Python's list but implemented from scratch for educational purposes.
    """
    
    def __init__(self, initial_capacity=10):
        """
        Initialize the dynamic array.
        
        Time Complexity: O(1)
        Space Complexity: O(n) where n is initial_capacity
        """
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * self.capacity
    
    def __len__(self):
        """Return the number of elements in the array."""
        return self.size
    
    def __getitem__(self, index):
        """
        Get element at given index.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not 0 <= index < self.size:
            raise IndexError("Array index out of range")
        return self.data[index]
    
    def __setitem__(self, index, value):
        """
        Set element at given index.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not 0 <= index < self.size:
            raise IndexError("Array index out of range")
        self.data[index] = value
    
    def _resize(self):
        """
        Resize the array when capacity is exceeded.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        old_capacity = self.capacity
        self.capacity *= 2
        new_data = [None] * self.capacity
        
        for i in range(self.size):
            new_data[i] = self.data[i]
        
        self.data = new_data
        print(f"Array resized from {old_capacity} to {self.capacity}")
    
    def append(self, value):
        """
        Add element to the end of array.
        
        Time Complexity: O(1) amortized, O(n) worst case
        Space Complexity: O(1)
        """
        if self.size >= self.capacity:
            self._resize()
        
        self.data[self.size] = value
        self.size += 1
    
    def insert(self, index, value):
        """
        Insert element at given index.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if index < 0 or index > self.size:
            raise IndexError("Array index out of range")
        
        if self.size >= self.capacity:
            self._resize()
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = value
        self.size += 1
    
    def remove(self, value):
        """
        Remove first occurrence of value.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        index = self.find(value)
        if index != -1:
            self.remove_at(index)
        else:
            raise ValueError(f"Value {value} not found in array")
    
    def remove_at(self, index):
        """
        Remove element at given index.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not 0 <= index < self.size:
            raise IndexError("Array index out of range")
        
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.size -= 1
        self.data[self.size] = None  # Clear the last element
    
    def find(self, value):
        """
        Find index of first occurrence of value.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def reverse(self):
        """
        Reverse the array in-place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, self.size - 1
        while left < right:
            self.data[left], self.data[right] = self.data[right], self.data[left]
            left += 1
            right -= 1
    
    def __str__(self):
        """Return string representation of array."""
        return "[" + ", ".join(str(self.data[i]) for i in range(self.size)) + "]"


def array_algorithms():
    """Demonstrate various array algorithms."""
    
    def two_sum(arr, target):
        """
        Find two numbers that add up to target.
        
        Algorithm: Hash Map approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}
        for i, num in enumerate(arr):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return None
    
    def max_subarray_sum(arr):
        """
        Find maximum sum of contiguous subarray (Kadane's Algorithm).
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not arr:
            return 0
        
        max_ending_here = max_so_far = arr[0]
        
        for i in range(1, len(arr)):
            max_ending_here = max(arr[i], max_ending_here + arr[i])
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
    
    def rotate_array(arr, k):
        """
        Rotate array to the right by k steps.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not arr or k == 0:
            return arr
        
        n = len(arr)
        k = k % n
        
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        
        return arr
    
    def merge_sorted_arrays(arr1, arr2):
        """
        Merge two sorted arrays.
        
        Time Complexity: O(m + n)
        Space Complexity: O(m + n)
        """
        result = []
        i = j = 0
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        
        result.extend(arr1[i:])
        result.extend(arr2[j:])
        
        return result
    
    # Demonstration
    print("=== Array Algorithms Demonstration ===\n")
    
    # Two Sum
    arr = [2, 7, 11, 15]
    target = 9
    result = two_sum(arr, target)
    print(f"Two Sum: {arr}, target={target} → indices: {result}")
    
    # Maximum Subarray Sum
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_sum(arr)
    print(f"Max Subarray Sum: {arr} → {max_sum}")
    
    # Array Rotation
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotated = rotate_array(arr.copy(), k)
    print(f"Rotate by {k}: {[1, 2, 3, 4, 5, 6, 7]} → {rotated}")
    
    # Merge Sorted Arrays
    arr1, arr2 = [1, 3, 5], [2, 4, 6]
    merged = merge_sorted_arrays(arr1, arr2)
    print(f"Merge Sorted: {arr1} + {arr2} → {merged}")


def demonstrate_array_operations():
    """Comprehensive demonstration of array operations."""
    print("=== Dynamic Array Implementation ===\n")
    
    # Create a dynamic array
    arr = DynamicArray(3)
    print(f"Created array with capacity 3, size: {len(arr)}")
    
    # Test append operation
    print("\n--- Append Operations ---")
    for i in range(5):
        arr.append(i * 10)
        print(f"Appended {i * 10}: {arr}")
    
    # Test access operations
    print("\n--- Access Operations ---")
    print(f"Element at index 2: {arr[2]}")
    arr[1] = 99
    print(f"After setting index 1 to 99: {arr}")
    
    # Test insert operation
    print("\n--- Insert Operations ---")
    arr.insert(2, 555)
    print(f"After inserting 555 at index 2: {arr}")
    
    # Test find operation
    print("\n--- Find Operations ---")
    index = arr.find(99)
    print(f"Index of 99: {index}")
    
    # Test remove operations
    print("\n--- Remove Operations ---")
    arr.remove(99)
    print(f"After removing 99: {arr}")
    
    arr.remove_at(0)
    print(f"After removing element at index 0: {arr}")
    
    # Test reverse operation
    print("\n--- Reverse Operation ---")
    arr.reverse()
    print(f"After reversing: {arr}")


def test_edge_cases():
    """Test edge cases and error handling."""
    print("\n=== Edge Cases Testing ===\n")
    
    arr = DynamicArray()
    
    # Test empty array operations
    try:
        print("Testing access on empty array...")
        value = arr[0]
    except IndexError as e:
        print(f"✓ Caught expected error: {e}")
    
    # Test out of bounds access
    arr.append(10)
    try:
        print("Testing out of bounds access...")
        value = arr[5]
    except IndexError as e:
        print(f"✓ Caught expected error: {e}")
    
    # Test remove non-existent element
    try:
        print("Testing remove non-existent element...")
        arr.remove(999)
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")


if __name__ == "__main__":
    print("🚀 Array Operations - Comprehensive Tutorial\n")
    print("=" * 50)
    
    # Demonstrate dynamic array operations
    demonstrate_array_operations()
    
    # Test edge cases
    test_edge_cases()
    
    # Demonstrate array algorithms
    print("\n" + "=" * 50)
    array_algorithms()
    
    print("\n" + "=" * 50)
    print("✅ Array operations tutorial completed!")
    print("\n📝 Key Takeaways:")
    print("• Arrays provide O(1) access but O(n) insertion/deletion")
    print("• Dynamic arrays use amortized O(1) append operations")
    print("• Many algorithms can be optimized using array properties")
    print("• Always consider edge cases in array operations")