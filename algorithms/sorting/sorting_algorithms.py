"""
Sorting Algorithms - Comprehensive Implementation

This module demonstrates fundamental sorting algorithms with detailed explanations,
time/space complexity analysis, step-by-step visualizations, and performance comparisons.

Sorting is a fundamental algorithmic problem that arranges elements in a specific order.
Understanding different sorting algorithms helps in choosing the right approach for specific scenarios.

Algorithms covered:
1. Bubble Sort
2. Selection Sort  
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Heap Sort
7. Counting Sort
8. Radix Sort
9. Bucket Sort

Author: Algorithm Learning Repository
"""

import random
import time
import math
from typing import List, Callable


class SortingAlgorithms:
    """Collection of sorting algorithm implementations."""
    
    @staticmethod
    def bubble_sort(arr: List[int], verbose: bool = False) -> List[int]:
        """
        Bubble Sort: Repeatedly swaps adjacent elements if they're in wrong order.
        
        Algorithm:
        1. Compare adjacent elements
        2. Swap if they're in wrong order
        3. Repeat until no swaps needed
        
        Time Complexity: O(n²) worst/average, O(n) best (optimized version)
        Space Complexity: O(1)
        Stable: Yes
        Adaptive: Yes (optimized version)
        """
        arr = arr.copy()
        n = len(arr)
        
        if verbose:
            print(f"Initial array: {arr}")
        
        for i in range(n):
            swapped = False
            
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    
                    if verbose:
                        print(f"Pass {i+1}, Step {j+1}: Swapped {arr[j+1]} and {arr[j]} -> {arr}")
            
            # Early termination optimization
            if not swapped:
                if verbose:
                    print(f"No swaps in pass {i+1}, array is sorted!")
                break
        
        return arr
    
    @staticmethod
    def selection_sort(arr: List[int], verbose: bool = False) -> List[int]:
        """
        Selection Sort: Finds minimum element and places it at beginning.
        
        Algorithm:
        1. Find minimum element in unsorted portion
        2. Swap it with first element of unsorted portion
        3. Move boundary of unsorted portion
        
        Time Complexity: O(n²) all cases
        Space Complexity: O(1)
        Stable: No (can be made stable)
        Adaptive: No
        """
        arr = arr.copy()
        n = len(arr)
        
        if verbose:
            print(f"Initial array: {arr}")
        
        for i in range(n):
            min_idx = i
            
            # Find minimum element in remaining array
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            # Swap minimum element with first element
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                
                if verbose:
                    print(f"Pass {i+1}: Found min {arr[i]} at index {min_idx}, swapped -> {arr}")
            elif verbose:
                print(f"Pass {i+1}: {arr[i]} already in correct position -> {arr}")
        
        return arr
    
    @staticmethod
    def insertion_sort(arr: List[int], verbose: bool = False) -> List[int]:
        """
        Insertion Sort: Builds sorted array one element at a time.
        
        Algorithm:
        1. Take next element from unsorted portion
        2. Find correct position in sorted portion
        3. Insert element at correct position
        
        Time Complexity: O(n²) worst/average, O(n) best
        Space Complexity: O(1)
        Stable: Yes
        Adaptive: Yes
        """
        arr = arr.copy()
        n = len(arr)
        
        if verbose:
            print(f"Initial array: {arr}")
        
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            
            if verbose:
                print(f"Pass {i}: Inserting {key}")
            
            # Move elements greater than key one position ahead
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                
                if verbose:
                    print(f"  Shifted {arr[j+2]} to position {j+2}")
            
            arr[j + 1] = key
            
            if verbose:
                print(f"  Inserted {key} at position {j+1} -> {arr}")
        
        return arr
    
    @staticmethod
    def merge_sort(arr: List[int], verbose: bool = False) -> List[int]:
        """
        Merge Sort: Divide and conquer algorithm that recursively sorts subarrays.
        
        Algorithm:
        1. Divide array into two halves
        2. Recursively sort both halves
        3. Merge sorted halves
        
        Time Complexity: O(n log n) all cases
        Space Complexity: O(n)
        Stable: Yes
        Adaptive: No
        """
        def merge(left: List[int], right: List[int]) -> List[int]:
            """Merge two sorted arrays."""
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            
            if verbose:
                print(f"  Merged {left} and {right} -> {result}")
            
            return result
        
        def merge_sort_helper(arr: List[int], depth: int = 0) -> List[int]:
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            
            if verbose:
                indent = "  " * depth
                print(f"{indent}Dividing {arr} -> {left} | {right}")
            
            left_sorted = merge_sort_helper(left, depth + 1)
            right_sorted = merge_sort_helper(right, depth + 1)
            
            return merge(left_sorted, right_sorted)
        
        if verbose:
            print(f"Initial array: {arr}")
        
        return merge_sort_helper(arr)
    
    @staticmethod
    def quick_sort(arr: List[int], verbose: bool = False) -> List[int]:
        """
        Quick Sort: Divide and conquer using pivot partitioning.
        
        Algorithm:
        1. Choose pivot element
        2. Partition array around pivot
        3. Recursively sort subarrays
        
        Time Complexity: O(n log n) average, O(n²) worst
        Space Complexity: O(log n) average, O(n) worst
        Stable: No
        Adaptive: No
        """
        def partition(arr: List[int], low: int, high: int) -> int:
            """Partition array around pivot."""
            pivot = arr[high]
            i = low - 1
            
            if verbose:
                print(f"  Partitioning around pivot {pivot}")
            
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    
                    if verbose and i != j:
                        print(f"    Swapped {arr[i]} and {arr[j]} -> {arr}")
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            
            if verbose:
                print(f"  Placed pivot {pivot} at position {i + 1} -> {arr}")
            
            return i + 1
        
        def quick_sort_helper(arr: List[int], low: int, high: int, depth: int = 0):
            if low < high:
                indent = "  " * depth
                if verbose:
                    print(f"{indent}Sorting subarray {arr[low:high+1]}")
                
                pi = partition(arr, low, high)
                
                quick_sort_helper(arr, low, pi - 1, depth + 1)
                quick_sort_helper(arr, pi + 1, high, depth + 1)
        
        arr = arr.copy()
        
        if verbose:
            print(f"Initial array: {arr}")
        
        quick_sort_helper(arr, 0, len(arr) - 1)
        return arr
    
    @staticmethod
    def heap_sort(arr: List[int], verbose: bool = False) -> List[int]:
        """
        Heap Sort: Uses binary heap data structure.
        
        Algorithm:
        1. Build max heap from array
        2. Extract maximum element (root)
        3. Restore heap property
        4. Repeat until heap is empty
        
        Time Complexity: O(n log n) all cases
        Space Complexity: O(1)
        Stable: No
        Adaptive: No
        """
        def heapify(arr: List[int], n: int, i: int):
            """Maintain heap property."""
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                
                if verbose:
                    print(f"  Heapify: Swapped {arr[i]} and {arr[largest]} -> {arr}")
                
                heapify(arr, n, largest)
        
        arr = arr.copy()
        n = len(arr)
        
        if verbose:
            print(f"Initial array: {arr}")
        
        # Build max heap
        if verbose:
            print("Building max heap:")
        
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        
        if verbose:
            print(f"Max heap: {arr}")
            print("Extracting elements:")
        
        # Extract elements from heap
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            
            if verbose:
                print(f"  Extracted {arr[i]}, heap size now {i} -> {arr}")
            
            heapify(arr, i, 0)
        
        return arr
    
    @staticmethod
    def counting_sort(arr: List[int], verbose: bool = False) -> List[int]:
        """
        Counting Sort: Non-comparison based sorting for integers.
        
        Algorithm:
        1. Find range of input values
        2. Count occurrences of each value
        3. Calculate cumulative counts
        4. Place elements in output array
        
        Time Complexity: O(n + k) where k is range
        Space Complexity: O(k)
        Stable: Yes
        Adaptive: No
        """
        if not arr:
            return arr
        
        # Find range
        min_val = min(arr)
        max_val = max(arr)
        range_val = max_val - min_val + 1
        
        # Initialize count array
        count = [0] * range_val
        output = [0] * len(arr)
        
        if verbose:
            print(f"Initial array: {arr}")
            print(f"Range: {min_val} to {max_val}")
        
        # Count occurrences
        for num in arr:
            count[num - min_val] += 1
        
        if verbose:
            print(f"Count array: {count}")
        
        # Calculate cumulative counts
        for i in range(1, range_val):
            count[i] += count[i - 1]
        
        if verbose:
            print(f"Cumulative counts: {count}")
        
        # Build output array
        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_val] - 1] = arr[i]
            count[arr[i] - min_val] -= 1
            
            if verbose:
                print(f"  Placed {arr[i]} at position {count[arr[i] - min_val]} -> {output}")
        
        return output
    
    @staticmethod
    def radix_sort(arr: List[int], verbose: bool = False) -> List[int]:
        """
        Radix Sort: Sorts by processing digits from least to most significant.
        
        Algorithm:
        1. Find maximum number to determine digits
        2. Sort by each digit using counting sort
        3. Process from least to most significant digit
        
        Time Complexity: O(d * (n + k)) where d is digits, k is base
        Space Complexity: O(n + k)
        Stable: Yes
        Adaptive: No
        """
        def counting_sort_for_radix(arr: List[int], exp: int) -> List[int]:
            """Modified counting sort for radix sort."""
            n = len(arr)
            output = [0] * n
            count = [0] * 10
            
            # Count occurrences of digits
            for num in arr:
                index = (num // exp) % 10
                count[index] += 1
            
            # Calculate cumulative counts
            for i in range(1, 10):
                count[i] += count[i - 1]
            
            # Build output array
            for i in range(n - 1, -1, -1):
                index = (arr[i] // exp) % 10
                output[count[index] - 1] = arr[i]
                count[index] -= 1
            
            return output
        
        if not arr:
            return arr
        
        # Find maximum number
        max_num = max(arr)
        
        if verbose:
            print(f"Initial array: {arr}")
            print(f"Maximum number: {max_num}")
        
        # Sort by each digit
        exp = 1
        while max_num // exp > 0:
            if verbose:
                print(f"Sorting by digit at position {exp} (1s, 10s, 100s, ...):")
            
            arr = counting_sort_for_radix(arr, exp)
            
            if verbose:
                print(f"  After sorting by {exp}s place: {arr}")
            
            exp *= 10
        
        return arr
    
    @staticmethod
    def bucket_sort(arr: List[float], verbose: bool = False) -> List[float]:
        """
        Bucket Sort: Distributes elements into buckets and sorts each bucket.
        
        Algorithm:
        1. Create buckets
        2. Distribute elements into buckets
        3. Sort each bucket individually
        4. Concatenate sorted buckets
        
        Time Complexity: O(n²) worst, O(n + k) average
        Space Complexity: O(n + k)
        Stable: Yes (if underlying sort is stable)
        Adaptive: Yes
        """
        if not arr:
            return arr
        
        # Determine number of buckets
        n = len(arr)
        buckets = [[] for _ in range(n)]
        
        if verbose:
            print(f"Initial array: {arr}")
            print(f"Created {n} buckets")
        
        # Distribute elements into buckets
        for num in arr:
            bucket_index = int(num * n)
            if bucket_index == n:  # Handle edge case
                bucket_index = n - 1
            buckets[bucket_index].append(num)
            
            if verbose:
                print(f"  Added {num} to bucket {bucket_index}")
        
        if verbose:
            print(f"Buckets after distribution: {buckets}")
        
        # Sort each bucket and concatenate
        result = []
        for i, bucket in enumerate(buckets):
            if bucket:
                sorted_bucket = sorted(bucket)  # Using built-in sort for simplicity
                result.extend(sorted_bucket)
                
                if verbose:
                    print(f"  Sorted bucket {i}: {bucket} -> {sorted_bucket}")
        
        return result


class SortingAnalyzer:
    """Analyzer for comparing sorting algorithm performance."""
    
    @staticmethod
    def time_algorithm(algorithm: Callable, arr: List[int]) -> float:
        """Time a sorting algorithm."""
        start_time = time.time()
        algorithm(arr.copy())
        end_time = time.time()
        return end_time - start_time
    
    @staticmethod
    def generate_test_cases() -> dict:
        """Generate various test cases for algorithm testing."""
        return {
            "Random": [random.randint(1, 100) for _ in range(50)],
            "Sorted": list(range(1, 51)),
            "Reverse Sorted": list(range(50, 0, -1)),
            "Nearly Sorted": [1, 2, 3, 5, 4, 6, 7, 8, 10, 9] * 5,
            "Duplicates": [1, 3, 2, 3, 1, 2, 1, 3, 2] * 5,
            "Single Element": [42],
            "Empty": []
        }
    
    @staticmethod
    def compare_algorithms():
        """Compare performance of different sorting algorithms."""
        algorithms = {
            "Bubble Sort": SortingAlgorithms.bubble_sort,
            "Selection Sort": SortingAlgorithms.selection_sort,
            "Insertion Sort": SortingAlgorithms.insertion_sort,
            "Merge Sort": SortingAlgorithms.merge_sort,
            "Quick Sort": SortingAlgorithms.quick_sort,
            "Heap Sort": SortingAlgorithms.heap_sort,
        }
        
        test_cases = SortingAnalyzer.generate_test_cases()
        
        print("=== Sorting Algorithm Performance Comparison ===\n")
        
        for case_name, test_array in test_cases.items():
            if len(test_array) == 0:
                continue
                
            print(f"Test Case: {case_name} (Size: {len(test_array)})")
            print("-" * 50)
            
            for algo_name, algorithm in algorithms.items():
                try:
                    execution_time = SortingAnalyzer.time_algorithm(algorithm, test_array)
                    sorted_array = algorithm(test_array.copy())
                    is_sorted = sorted_array == sorted(test_array)
                    
                    print(f"{algo_name:15} | Time: {execution_time:.6f}s | Correct: {is_sorted}")
                    
                except Exception as e:
                    print(f"{algo_name:15} | Error: {str(e)}")
            
            print()


def demonstrate_sorting_algorithms():
    """Demonstrate all sorting algorithms with examples."""
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    algorithms = [
        ("Bubble Sort", SortingAlgorithms.bubble_sort),
        ("Selection Sort", SortingAlgorithms.selection_sort),
        ("Insertion Sort", SortingAlgorithms.insertion_sort),
        ("Merge Sort", SortingAlgorithms.merge_sort),
        ("Quick Sort", SortingAlgorithms.quick_sort),
        ("Heap Sort", SortingAlgorithms.heap_sort),
        ("Counting Sort", SortingAlgorithms.counting_sort),
        ("Radix Sort", SortingAlgorithms.radix_sort),
    ]
    
    print("=== Sorting Algorithms Demonstration ===\n")
    print(f"Original array: {test_array}\n")
    
    for name, algorithm in algorithms:
        print(f"{'='*20} {name} {'='*20}")
        
        if name == "Bucket Sort":
            # Use floating point numbers for bucket sort demo
            float_array = [x/100 for x in test_array]
            result = algorithm(float_array, verbose=True)
        else:
            result = algorithm(test_array, verbose=True)
        
        print(f"Final result: {result}")
        print(f"Correctly sorted: {result == sorted(test_array)}")
        print()


def educational_insights():
    """Provide educational insights about sorting algorithms."""
    print("=== Sorting Algorithms Educational Insights ===\n")
    
    insights = {
        "When to use Bubble Sort": [
            "• Educational purposes only",
            "• Very small datasets (< 10 elements)",
            "• When simplicity is more important than efficiency"
        ],
        
        "When to use Selection Sort": [
            "• Small datasets",
            "• Memory writes are expensive (minimizes swaps)",
            "• Educational purposes"
        ],
        
        "When to use Insertion Sort": [
            "• Small datasets (< 50 elements)",
            "• Nearly sorted data",
            "• As subroutine in hybrid algorithms",
            "• Online algorithms (sorting as data arrives)"
        ],
        
        "When to use Merge Sort": [
            "• Stable sorting required",
            "• Guaranteed O(n log n) performance",
            "• Large datasets",
            "• External sorting (data doesn't fit in memory)"
        ],
        
        "When to use Quick Sort": [
            "• General-purpose sorting",
            "• Average case performance matters",
            "• In-place sorting preferred",
            "• Most built-in sort implementations"
        ],
        
        "When to use Heap Sort": [
            "• Guaranteed O(n log n) with O(1) space",
            "• When worst-case performance is critical",
            "• Priority queue implementations"
        ],
        
        "When to use Counting Sort": [
            "• Small range of integer values",
            "• When range k is O(n)",
            "• Stable sorting needed",
            "• Part of radix sort"
        ],
        
        "When to use Radix Sort": [
            "• Large datasets of integers/strings",
            "• Fixed-width data",
            "• When comparison-based sorts are too slow",
            "• Parallel processing available"
        ],
        
        "When to use Bucket Sort": [
            "• Uniformly distributed data",
            "• Floating-point numbers in [0, 1)",
            "• When data can be divided into ranges",
            "• Parallel processing available"
        ]
    }
    
    for category, points in insights.items():
        print(f"{category}:")
        for point in points:
            print(f"  {point}")
        print()


if __name__ == "__main__":
    print("🚀 Sorting Algorithms - Comprehensive Tutorial\n")
    print("=" * 70)
    
    # Demonstrate all algorithms
    demonstrate_sorting_algorithms()
    
    # Performance comparison
    print("=" * 70)
    SortingAnalyzer.compare_algorithms()
    
    # Educational insights
    print("=" * 70)
    educational_insights()
    
    print("=" * 70)
    print("✅ Sorting algorithms tutorial completed!")
    print("\n📝 Key Takeaways:")
    print("• No single sorting algorithm is best for all scenarios")
    print("• Consider data characteristics: size, distribution, constraints")
    print("• Time vs. space complexity trade-offs")
    print("• Stable vs. unstable sorting requirements")
    print("• Comparison-based vs. non-comparison-based algorithms")
    print("• Hybrid approaches often work best in practice")