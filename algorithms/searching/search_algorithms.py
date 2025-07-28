"""
Searching Algorithms - Comprehensive Implementation

This module demonstrates fundamental searching algorithms with detailed explanations,
time/space complexity analysis, and multiple implementation approaches.

Searching is the process of finding a particular element in a collection of elements.
Different algorithms are optimal for different scenarios and data structures.

Algorithms covered:
1. Linear Search
2. Binary Search (Iterative and Recursive)
3. Jump Search
4. Interpolation Search
5. Exponential Search
6. Fibonacci Search
7. Ternary Search
8. Depth-First Search (DFS)
9. Breadth-First Search (BFS)

Author: Algorithm Learning Repository
"""

import math
from typing import List, Optional, Dict, Set, Callable
from collections import deque


class SearchingAlgorithms:
    """Collection of searching algorithm implementations."""
    
    @staticmethod
    def linear_search(arr: List[int], target: int, verbose: bool = False) -> int:
        """
        Linear Search: Search sequentially through the array.
        
        Algorithm: Check each element one by one until target is found
        Time Complexity: O(n)
        Space Complexity: O(1)
        Best for: Unsorted arrays, small datasets
        """
        if verbose:
            print(f"Linear Search for {target} in {arr}")
        
        for i in range(len(arr)):
            if verbose:
                print(f"  Checking index {i}: {arr[i]}")
            
            if arr[i] == target:
                if verbose:
                    print(f"  ✓ Found {target} at index {i}")
                return i
        
        if verbose:
            print(f"  ✗ {target} not found")
        return -1
    
    @staticmethod
    def binary_search_iterative(arr: List[int], target: int, verbose: bool = False) -> int:
        """
        Binary Search (Iterative): Search in sorted array by dividing search space in half.
        
        Algorithm: Compare target with middle element, eliminate half of search space
        Time Complexity: O(log n)
        Space Complexity: O(1)
        Prerequisite: Array must be sorted
        """
        if verbose:
            print(f"Binary Search (Iterative) for {target} in {arr}")
        
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if verbose:
                print(f"  Range: [{left}, {right}], Mid: {mid}, Value: {arr[mid]}")
            
            if arr[mid] == target:
                if verbose:
                    print(f"  ✓ Found {target} at index {mid}")
                return mid
            elif arr[mid] < target:
                left = mid + 1
                if verbose:
                    print(f"    Target > {arr[mid]}, search right half")
            else:
                right = mid - 1
                if verbose:
                    print(f"    Target < {arr[mid]}, search left half")
        
        if verbose:
            print(f"  ✗ {target} not found")
        return -1
    
    @staticmethod
    def binary_search_recursive(arr: List[int], target: int, left: int = None, right: int = None, verbose: bool = False) -> int:
        """
        Binary Search (Recursive): Recursive implementation of binary search.
        
        Time Complexity: O(log n)
        Space Complexity: O(log n) due to recursion stack
        """
        if left is None:
            left = 0
        if right is None:
            right = len(arr) - 1
        
        if verbose and left == 0 and right == len(arr) - 1:
            print(f"Binary Search (Recursive) for {target} in {arr}")
        
        if left > right:
            if verbose:
                print(f"  ✗ {target} not found")
            return -1
        
        mid = (left + right) // 2
        
        if verbose:
            print(f"  Range: [{left}, {right}], Mid: {mid}, Value: {arr[mid]}")
        
        if arr[mid] == target:
            if verbose:
                print(f"  ✓ Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            if verbose:
                print(f"    Target > {arr[mid]}, search right half")
            return SearchingAlgorithms.binary_search_recursive(arr, target, mid + 1, right, verbose)
        else:
            if verbose:
                print(f"    Target < {arr[mid]}, search left half")
            return SearchingAlgorithms.binary_search_recursive(arr, target, left, mid - 1, verbose)
    
    @staticmethod
    def jump_search(arr: List[int], target: int, verbose: bool = False) -> int:
        """
        Jump Search: Search by jumping ahead by fixed steps, then linear search.
        
        Algorithm: Jump by sqrt(n) steps, then linear search in found block
        Time Complexity: O(√n)
        Space Complexity: O(1)
        Prerequisite: Array must be sorted
        """
        if verbose:
            print(f"Jump Search for {target} in {arr}")
        
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        
        if verbose:
            print(f"  Jump step size: {step}")
        
        # Jump until we find a block where target might be
        while prev < n and arr[min(step, n) - 1] < target:
            if verbose:
                print(f"  Jumping: block[{prev}:{min(step, n)}], last value: {arr[min(step, n) - 1]}")
            prev = step
            step += int(math.sqrt(n))
        
        # Linear search in the identified block
        if verbose:
            print(f"  Linear search in block starting at index {prev}")
        
        for i in range(prev, min(step, n)):
            if verbose:
                print(f"    Checking index {i}: {arr[i]}")
            
            if arr[i] == target:
                if verbose:
                    print(f"  ✓ Found {target} at index {i}")
                return i
        
        if verbose:
            print(f"  ✗ {target} not found")
        return -1
    
    @staticmethod
    def interpolation_search(arr: List[int], target: int, verbose: bool = False) -> int:
        """
        Interpolation Search: Improved binary search for uniformly distributed data.
        
        Algorithm: Estimate position based on value distribution
        Time Complexity: O(log log n) average, O(n) worst case
        Space Complexity: O(1)
        Prerequisite: Array must be sorted and uniformly distributed
        """
        if verbose:
            print(f"Interpolation Search for {target} in {arr}")
        
        left, right = 0, len(arr) - 1
        
        while left <= right and target >= arr[left] and target <= arr[right]:
            # If only one element
            if left == right:
                if arr[left] == target:
                    if verbose:
                        print(f"  ✓ Found {target} at index {left}")
                    return left
                break
            
            # Estimate position using interpolation formula
            pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
            
            if verbose:
                print(f"  Range: [{left}, {right}], Estimated pos: {pos}, Value: {arr[pos]}")
            
            if arr[pos] == target:
                if verbose:
                    print(f"  ✓ Found {target} at index {pos}")
                return pos
            elif arr[pos] < target:
                left = pos + 1
                if verbose:
                    print(f"    Target > {arr[pos]}, search right")
            else:
                right = pos - 1
                if verbose:
                    print(f"    Target < {arr[pos]}, search left")
        
        if verbose:
            print(f"  ✗ {target} not found")
        return -1
    
    @staticmethod
    def exponential_search(arr: List[int], target: int, verbose: bool = False) -> int:
        """
        Exponential Search: Find range using exponential growth, then binary search.
        
        Algorithm: Find range [2^(i-1), 2^i] containing target, then binary search
        Time Complexity: O(log n)
        Space Complexity: O(1)
        Prerequisite: Array must be sorted
        """
        if verbose:
            print(f"Exponential Search for {target} in {arr}")
        
        n = len(arr)
        
        # If target is at first position
        if arr[0] == target:
            if verbose:
                print(f"  ✓ Found {target} at index 0")
            return 0
        
        # Find range for binary search by exponential growth
        bound = 1
        while bound < n and arr[bound] < target:
            if verbose:
                print(f"  Checking bound {bound}: {arr[bound]}")
            bound *= 2
        
        # Binary search in found range
        left = bound // 2
        right = min(bound, n - 1)
        
        if verbose:
            print(f"  Binary search in range [{left}, {right}]")
        
        return SearchingAlgorithms.binary_search_iterative(
            arr[left:right+1], target, verbose
        ) + left if SearchingAlgorithms.binary_search_iterative(
            arr[left:right+1], target, verbose
        ) != -1 else -1
    
    @staticmethod
    def fibonacci_search(arr: List[int], target: int, verbose: bool = False) -> int:
        """
        Fibonacci Search: Use Fibonacci numbers to divide array.
        
        Algorithm: Use Fibonacci numbers instead of mid-point division
        Time Complexity: O(log n)
        Space Complexity: O(1)
        Prerequisite: Array must be sorted
        """
        if verbose:
            print(f"Fibonacci Search for {target} in {arr}")
        
        n = len(arr)
        
        # Generate Fibonacci numbers
        fib2 = 0  # (m-2)'th Fibonacci number
        fib1 = 1  # (m-1)'th Fibonacci number
        fib = fib2 + fib1  # m'th Fibonacci number
        
        # Find smallest Fibonacci number >= n
        while fib < n:
            fib2 = fib1
            fib1 = fib
            fib = fib2 + fib1
        
        if verbose:
            print(f"  Using Fibonacci numbers: fib2={fib2}, fib1={fib1}, fib={fib}")
        
        offset = -1
        
        while fib > 1:
            # Calculate index to check
            i = min(offset + fib2, n - 1)
            
            if verbose:
                print(f"  Checking index {i}: {arr[i]}")
            
            if arr[i] < target:
                fib = fib1
                fib1 = fib2
                fib2 = fib - fib1
                offset = i
                if verbose:
                    print(f"    Target > {arr[i]}, move right")
            elif arr[i] > target:
                fib = fib2
                fib1 = fib1 - fib2
                fib2 = fib - fib1
                if verbose:
                    print(f"    Target < {arr[i]}, move left")
            else:
                if verbose:
                    print(f"  ✓ Found {target} at index {i}")
                return i
        
        # Check last element
        if fib1 and offset + 1 < n and arr[offset + 1] == target:
            if verbose:
                print(f"  ✓ Found {target} at index {offset + 1}")
            return offset + 1
        
        if verbose:
            print(f"  ✗ {target} not found")
        return -1
    
    @staticmethod
    def ternary_search(arr: List[int], target: int, left: int = None, right: int = None, verbose: bool = False) -> int:
        """
        Ternary Search: Divide search space into three parts.
        
        Algorithm: Compare with two middle points, eliminate 2/3 of search space
        Time Complexity: O(log₃ n)
        Space Complexity: O(log n) for recursion
        Prerequisite: Array must be sorted
        """
        if left is None:
            left = 0
        if right is None:
            right = len(arr) - 1
        
        if verbose and left == 0 and right == len(arr) - 1:
            print(f"Ternary Search for {target} in {arr}")
        
        if left > right:
            if verbose:
                print(f"  ✗ {target} not found")
            return -1
        
        # Calculate two middle points
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if verbose:
            print(f"  Range: [{left}, {right}], Mid1: {mid1}({arr[mid1]}), Mid2: {mid2}({arr[mid2]})")
        
        if arr[mid1] == target:
            if verbose:
                print(f"  ✓ Found {target} at index {mid1}")
            return mid1
        
        if arr[mid2] == target:
            if verbose:
                print(f"  ✓ Found {target} at index {mid2}")
            return mid2
        
        if target < arr[mid1]:
            if verbose:
                print(f"    Target < {arr[mid1]}, search left third")
            return SearchingAlgorithms.ternary_search(arr, target, left, mid1 - 1, verbose)
        elif target > arr[mid2]:
            if verbose:
                print(f"    Target > {arr[mid2]}, search right third")
            return SearchingAlgorithms.ternary_search(arr, target, mid2 + 1, right, verbose)
        else:
            if verbose:
                print(f"    {arr[mid1]} < Target < {arr[mid2]}, search middle third")
            return SearchingAlgorithms.ternary_search(arr, target, mid1 + 1, mid2 - 1, verbose)


class GraphSearchAlgorithms:
    """Graph traversal and search algorithms."""
    
    @staticmethod
    def depth_first_search(graph: Dict[str, List[str]], start: str, target: str = None, verbose: bool = False) -> List[str]:
        """
        Depth-First Search: Explore as far as possible along each branch.
        
        Algorithm: Use stack (recursion) to explore deeply before backtracking
        Time Complexity: O(V + E)
        Space Complexity: O(V) for recursion stack
        """
        if verbose:
            print(f"DFS starting from {start}" + (f" looking for {target}" if target else ""))
        
        visited = set()
        path = []
        
        def dfs_helper(node: str) -> bool:
            visited.add(node)
            path.append(node)
            
            if verbose:
                print(f"  Visiting: {node}")
            
            if target and node == target:
                if verbose:
                    print(f"  ✓ Found target {target}!")
                return True
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs_helper(neighbor):
                        return True
            
            return False
        
        dfs_helper(start)
        
        if verbose:
            print(f"  DFS path: {' -> '.join(path)}")
        
        return path
    
    @staticmethod
    def breadth_first_search(graph: Dict[str, List[str]], start: str, target: str = None, verbose: bool = False) -> List[str]:
        """
        Breadth-First Search: Explore all neighbors before going deeper.
        
        Algorithm: Use queue to explore level by level
        Time Complexity: O(V + E)
        Space Complexity: O(V) for queue
        """
        if verbose:
            print(f"BFS starting from {start}" + (f" looking for {target}" if target else ""))
        
        visited = set([start])
        queue = deque([start])
        path = []
        
        while queue:
            node = queue.popleft()
            path.append(node)
            
            if verbose:
                print(f"  Visiting: {node}")
            
            if target and node == target:
                if verbose:
                    print(f"  ✓ Found target {target}!")
                break
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        if verbose:
            print(f"  BFS path: {' -> '.join(path)}")
        
        return path
    
    @staticmethod
    def find_shortest_path_bfs(graph: Dict[str, List[str]], start: str, target: str, verbose: bool = False) -> List[str]:
        """
        Find shortest path using BFS.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        if verbose:
            print(f"Finding shortest path from {start} to {target}")
        
        if start == target:
            return [start]
        
        visited = set([start])
        queue = deque([(start, [start])])
        
        while queue:
            node, path = queue.popleft()
            
            if verbose:
                print(f"  Exploring: {node}, Current path: {' -> '.join(path)}")
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    
                    if neighbor == target:
                        if verbose:
                            print(f"  ✓ Found shortest path: {' -> '.join(new_path)}")
                        return new_path
                    
                    visited.add(neighbor)
                    queue.append((neighbor, new_path))
        
        if verbose:
            print(f"  ✗ No path found from {start} to {target}")
        return []


class SearchAnalyzer:
    """Analyzer for comparing search algorithm performance."""
    
    @staticmethod
    def compare_search_algorithms():
        """Compare performance of different search algorithms."""
        # Test data - sorted array
        test_data = list(range(0, 1000, 2))  # [0, 2, 4, 6, ..., 998]
        target = 500
        
        algorithms = {
            "Linear Search": SearchingAlgorithms.linear_search,
            "Binary Search (Iterative)": SearchingAlgorithms.binary_search_iterative,
            "Binary Search (Recursive)": SearchingAlgorithms.binary_search_recursive,
            "Jump Search": SearchingAlgorithms.jump_search,
            "Interpolation Search": SearchingAlgorithms.interpolation_search,
            "Fibonacci Search": SearchingAlgorithms.fibonacci_search,
            "Ternary Search": SearchingAlgorithms.ternary_search,
        }
        
        print("=== Search Algorithm Comparison ===\n")
        print(f"Data: Sorted array of {len(test_data)} elements")
        print(f"Target: {target}")
        print("-" * 60)
        
        for name, algorithm in algorithms.items():
            try:
                result = algorithm(test_data, target)
                status = f"Found at index {result}" if result != -1 else "Not found"
                print(f"{name:<25} | {status}")
            except Exception as e:
                print(f"{name:<25} | Error: {str(e)}")
        
        print()


def demonstrate_linear_searches():
    """Demonstrate linear and basic search algorithms."""
    print("=== Linear and Basic Search Algorithms ===\n")
    
    # Test data
    unsorted_data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    
    print(f"Unsorted data: {unsorted_data}")
    print(f"Sorted data: {sorted_data}")
    print(f"Target: {target}\n")
    
    # Linear Search
    print("--- Linear Search ---")
    result = SearchingAlgorithms.linear_search(unsorted_data, target, verbose=True)
    print()
    
    # Binary Search
    print("--- Binary Search (Iterative) ---")
    result = SearchingAlgorithms.binary_search_iterative(sorted_data, target, verbose=True)
    print()
    
    # Binary Search Recursive
    print("--- Binary Search (Recursive) ---")
    result = SearchingAlgorithms.binary_search_recursive(sorted_data, target, verbose=True)
    print()


def demonstrate_advanced_searches():
    """Demonstrate advanced search algorithms."""
    print("=== Advanced Search Algorithms ===\n")
    
    # Large sorted array for better demonstration
    sorted_data = list(range(1, 101, 2))  # [1, 3, 5, 7, ..., 99]
    target = 47
    
    print(f"Data: {sorted_data}")
    print(f"Target: {target}\n")
    
    # Jump Search
    print("--- Jump Search ---")
    result = SearchingAlgorithms.jump_search(sorted_data, target, verbose=True)
    print()
    
    # Interpolation Search
    print("--- Interpolation Search ---")
    result = SearchingAlgorithms.interpolation_search(sorted_data, target, verbose=True)
    print()
    
    # Fibonacci Search
    print("--- Fibonacci Search ---")
    result = SearchingAlgorithms.fibonacci_search(sorted_data, target, verbose=True)
    print()
    
    # Ternary Search
    print("--- Ternary Search ---")
    result = SearchingAlgorithms.ternary_search(sorted_data, target, verbose=True)
    print()


def demonstrate_graph_searches():
    """Demonstrate graph search algorithms."""
    print("=== Graph Search Algorithms ===\n")
    
    # Sample graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("Graph structure:")
    for node, neighbors in graph.items():
        print(f"  {node}: {neighbors}")
    print()
    
    # DFS
    print("--- Depth-First Search ---")
    dfs_path = GraphSearchAlgorithms.depth_first_search(graph, 'A', verbose=True)
    print()
    
    # BFS
    print("--- Breadth-First Search ---")
    bfs_path = GraphSearchAlgorithms.breadth_first_search(graph, 'A', verbose=True)
    print()
    
    # Shortest Path
    print("--- Shortest Path (BFS) ---")
    shortest = GraphSearchAlgorithms.find_shortest_path_bfs(graph, 'A', 'F', verbose=True)
    print()


def complexity_analysis():
    """Provide complexity analysis of search algorithms."""
    print("=== Search Algorithms Complexity Analysis ===\n")
    
    complexities = {
        "Linear Search": ("O(n)", "O(1)", "Unsorted data"),
        "Binary Search": ("O(log n)", "O(1)", "Sorted data"),
        "Jump Search": ("O(√n)", "O(1)", "Sorted data"),
        "Interpolation Search": ("O(log log n)*", "O(1)", "Uniformly distributed"),
        "Exponential Search": ("O(log n)", "O(1)", "Sorted, unbounded"),
        "Fibonacci Search": ("O(log n)", "O(1)", "Sorted data"),
        "Ternary Search": ("O(log₃ n)", "O(log n)", "Sorted data"),
        "DFS": ("O(V + E)", "O(V)", "Graph traversal"),
        "BFS": ("O(V + E)", "O(V)", "Graph traversal"),
    }
    
    print(f"{'Algorithm':<20} {'Time':<15} {'Space':<10} {'Best For':<20}")
    print("-" * 70)
    
    for algorithm, (time, space, best_for) in complexities.items():
        print(f"{algorithm:<20} {time:<15} {space:<10} {best_for:<20}")
    
    print("\n* Average case for uniformly distributed data")


def search_algorithm_insights():
    """Provide insights about when to use each search algorithm."""
    print("\n=== Search Algorithm Selection Guide ===\n")
    
    insights = {
        "Linear Search": [
            "• Use for unsorted data",
            "• Small datasets (< 100 elements)",
            "• When simplicity is important",
            "• No preprocessing required"
        ],
        
        "Binary Search": [
            "• Best for sorted data",
            "• Large datasets",
            "• Frequent searches on same data",
            "• Most commonly used efficient search"
        ],
        
        "Jump Search": [
            "• Alternative when binary search is not suitable",
            "• Better than linear for sorted data",
            "• Good balance between time and simplicity"
        ],
        
        "Interpolation Search": [
            "• Uniformly distributed data",
            "• Large datasets with numeric keys",
            "• Better than binary search for uniform data"
        ],
        
        "Exponential Search": [
            "• Unbounded or infinite arrays",
            "• When you don't know the size",
            "• Target is likely to be near the beginning"
        ],
        
        "Graph Searches": [
            "DFS:",
            "  • Path finding with backtracking",
            "  • Topological sorting",
            "  • Detecting cycles",
            "",
            "BFS:",
            "  • Shortest path in unweighted graphs",
            "  • Level-order traversal",
            "  • Finding connected components"
        ]
    }
    
    for category, points in insights.items():
        print(f"{category}:")
        for point in points:
            if point:
                print(f"  {point}")
        print()


if __name__ == "__main__":
    print("🚀 Search Algorithms - Comprehensive Tutorial\n")
    print("=" * 70)
    
    # Demonstrate different categories of search algorithms
    demonstrate_linear_searches()
    
    print("\n" + "=" * 70)
    demonstrate_advanced_searches()
    
    print("\n" + "=" * 70)
    demonstrate_graph_searches()
    
    # Performance comparison
    print("\n" + "=" * 70)
    SearchAnalyzer.compare_search_algorithms()
    
    # Complexity analysis
    print("\n" + "=" * 70)
    complexity_analysis()
    
    # Algorithm insights
    print("\n" + "=" * 70)
    search_algorithm_insights()
    
    print("\n" + "=" * 70)
    print("✅ Search algorithms tutorial completed!")
    print("\n📝 Key Takeaways:")
    print("• Choose algorithm based on data characteristics")
    print("• Binary search requires sorted data but is very efficient")
    print("• Linear search works on any data but is slow for large datasets")
    print("• Advanced searches offer optimizations for specific scenarios")
    print("• Graph searches are essential for network and tree problems")
    print("• Consider preprocessing cost vs. search frequency")