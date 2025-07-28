"""
Dynamic Programming Algorithms - Comprehensive Implementation

This module demonstrates fundamental dynamic programming (DP) algorithms with detailed explanations,
both memoization (top-down) and tabulation (bottom-up) approaches, and optimization techniques.

Dynamic Programming: An algorithmic paradigm that solves complex problems by breaking them down
into simpler subproblems and storing the results to avoid redundant calculations.

Key principles:
1. Overlapping Subproblems
2. Optimal Substructure

Classic Problems covered:
1. Fibonacci Sequence
2. Longest Common Subsequence (LCS)
3. Knapsack Problem (0/1 and Unbounded)
4. Coin Change Problem
5. Longest Increasing Subsequence (LIS)
6. Edit Distance
7. Maximum Subarray Sum (Kadane's Algorithm)
8. Matrix Chain Multiplication
9. Palindrome Problems

Author: Algorithm Learning Repository
"""

from typing import List, Dict, Tuple
import sys


class DynamicProgramming:
    """Collection of dynamic programming algorithm implementations."""
    
    @staticmethod
    def fibonacci_memoization(n: int, memo: Dict[int, int] = None) -> int:
        """
        Fibonacci using memoization (top-down approach).
        
        Algorithm: Store previously computed values to avoid recalculation
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if memo is None:
            memo = {}
        
        if n in memo:
            return memo[n]
        
        if n <= 1:
            return n
        
        memo[n] = DynamicProgramming.fibonacci_memoization(n-1, memo) + \
                  DynamicProgramming.fibonacci_memoization(n-2, memo)
        
        return memo[n]
    
    @staticmethod
    def fibonacci_tabulation(n: int) -> int:
        """
        Fibonacci using tabulation (bottom-up approach).
        
        Algorithm: Build solution iteratively from base cases
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    @staticmethod
    def fibonacci_optimized(n: int) -> int:
        """
        Space-optimized Fibonacci.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n <= 1:
            return n
        
        prev2, prev1 = 0, 1
        
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        
        return prev1
    
    @staticmethod
    def longest_common_subsequence(text1: str, text2: str, verbose: bool = False) -> int:
        """
        Find length of Longest Common Subsequence.
        
        Algorithm: DP table where dp[i][j] represents LCS length of text1[:i] and text2[:j]
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        if verbose:
            print("LCS DP Table:")
            for row in dp:
                print(row)
        
        return dp[m][n]
    
    @staticmethod
    def lcs_with_string(text1: str, text2: str) -> str:
        """
        Find actual Longest Common Subsequence string.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Reconstruct LCS
        lcs = []
        i, j = m, n
        
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                lcs.append(text1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        
        return ''.join(reversed(lcs))
    
    @staticmethod
    def knapsack_01(weights: List[int], values: List[int], capacity: int, verbose: bool = False) -> int:
        """
        0/1 Knapsack Problem - each item can be taken at most once.
        
        Algorithm: dp[i][w] = maximum value using first i items with weight limit w
        Time Complexity: O(n * W)
        Space Complexity: O(n * W)
        """
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                # Don't include current item
                dp[i][w] = dp[i-1][w]
                
                # Include current item if possible
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
        
        if verbose:
            print("Knapsack DP Table:")
            for row in dp:
                print(row)
        
        return dp[n][capacity]
    
    @staticmethod
    def knapsack_01_items(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
        """
        0/1 Knapsack with item tracking.
        
        Returns: (max_value, selected_items_indices)
        """
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        # Fill DP table
        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                dp[i][w] = dp[i-1][w]
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
        
        # Backtrack to find selected items
        selected = []
        w = capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:
                selected.append(i-1)  # 0-based index
                w -= weights[i-1]
        
        return dp[n][capacity], selected[::-1]
    
    @staticmethod
    def unbounded_knapsack(weights: List[int], values: List[int], capacity: int) -> int:
        """
        Unbounded Knapsack - unlimited quantity of each item.
        
        Algorithm: dp[w] = maximum value with weight limit w
        Time Complexity: O(n * W)
        Space Complexity: O(W)
        """
        dp = [0] * (capacity + 1)
        
        for w in range(1, capacity + 1):
            for i in range(len(weights)):
                if weights[i] <= w:
                    dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
        
        return dp[capacity]
    
    @staticmethod
    def coin_change_min_coins(coins: List[int], amount: int) -> int:
        """
        Minimum number of coins to make amount.
        
        Algorithm: dp[i] = minimum coins needed for amount i
        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    @staticmethod
    def coin_change_ways(coins: List[int], amount: int) -> int:
        """
        Number of ways to make amount using coins.
        
        Algorithm: dp[i] = number of ways to make amount i
        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
        """
        dp = [0] * (amount + 1)
        dp[0] = 1  # One way to make amount 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]
    
    @staticmethod
    def longest_increasing_subsequence(nums: List[int]) -> int:
        """
        Length of Longest Increasing Subsequence.
        
        Algorithm: dp[i] = length of LIS ending at index i
        Time Complexity: O(n²)
        Space Complexity: O(n)
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    @staticmethod
    def lis_binary_search(nums: List[int]) -> int:
        """
        LIS using binary search optimization.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if not nums:
            return 0
        
        tails = []
        
        for num in nums:
            left, right = 0, len(tails)
            
            # Binary search for insertion position
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num
        
        return len(tails)
    
    @staticmethod
    def edit_distance(word1: str, word2: str, verbose: bool = False) -> int:
        """
        Minimum edit distance (Levenshtein distance).
        
        Operations: insert, delete, replace
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i  # Delete all characters
        for j in range(n + 1):
            dp[0][j] = j  # Insert all characters
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]  # No operation needed
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # Delete
                        dp[i][j-1],    # Insert
                        dp[i-1][j-1]   # Replace
                    )
        
        if verbose:
            print("Edit Distance DP Table:")
            for row in dp:
                print(row)
        
        return dp[m][n]
    
    @staticmethod
    def max_subarray_sum(nums: List[int]) -> int:
        """
        Maximum sum of contiguous subarray (Kadane's Algorithm).
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
        
        max_ending_here = max_so_far = nums[0]
        
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
    
    @staticmethod
    def max_subarray_indices(nums: List[int]) -> Tuple[int, int, int]:
        """
        Maximum subarray sum with start and end indices.
        
        Returns: (max_sum, start_index, end_index)
        """
        if not nums:
            return 0, 0, 0
        
        max_ending_here = max_so_far = nums[0]
        start = end = temp_start = 0
        
        for i in range(1, len(nums)):
            if max_ending_here < 0:
                max_ending_here = nums[i]
                temp_start = i
            else:
                max_ending_here += nums[i]
            
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                start = temp_start
                end = i
        
        return max_so_far, start, end
    
    @staticmethod
    def matrix_chain_multiplication(dimensions: List[int]) -> int:
        """
        Minimum scalar multiplications for matrix chain.
        
        Algorithm: dp[i][j] = minimum cost to multiply matrices from i to j
        Time Complexity: O(n³)
        Space Complexity: O(n²)
        """
        n = len(dimensions) - 1  # Number of matrices
        dp = [[0] * n for _ in range(n)]
        
        # length is chain length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                
                for k in range(i, j):
                    cost = (dp[i][k] + dp[k+1][j] + 
                           dimensions[i] * dimensions[k+1] * dimensions[j+1])
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[0][n-1]
    
    @staticmethod
    def longest_palindromic_subsequence(s: str) -> int:
        """
        Length of longest palindromic subsequence.
        
        Algorithm: dp[i][j] = LPS length in substring s[i:j+1]
        Time Complexity: O(n²)
        Space Complexity: O(n²)
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = 1
        
        # Check for subsequences of length 2 and more
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]
    
    @staticmethod
    def palindrome_partitioning_min_cuts(s: str) -> int:
        """
        Minimum cuts needed for palindrome partitioning.
        
        Time Complexity: O(n³)
        Space Complexity: O(n²)
        """
        n = len(s)
        
        # is_palindrome[i][j] = True if s[i:j+1] is palindrome
        is_palindrome = [[False] * n for _ in range(n)]
        
        # Every single character is palindrome
        for i in range(n):
            is_palindrome[i][i] = True
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            is_palindrome[i][i+1] = (s[i] == s[i+1])
        
        # Check for palindromes of length 3 and more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = (s[i] == s[j] and is_palindrome[i+1][j-1])
        
        # DP for minimum cuts
        cuts = [0] * n
        
        for i in range(n):
            if is_palindrome[0][i]:
                cuts[i] = 0
            else:
                cuts[i] = float('inf')
                for j in range(i):
                    if is_palindrome[j+1][i]:
                        cuts[i] = min(cuts[i], cuts[j] + 1)
        
        return cuts[n-1]


class DPDemonstrator:
    """Demonstrates DP algorithms with examples and comparisons."""
    
    @staticmethod
    def fibonacci_comparison():
        """Compare different Fibonacci implementations."""
        print("=== Fibonacci Sequence Comparison ===\n")
        
        n = 10
        print(f"Computing Fibonacci({n}):")
        
        # Memoization
        memo_result = DynamicProgramming.fibonacci_memoization(n)
        print(f"Memoization:     {memo_result}")
        
        # Tabulation
        tab_result = DynamicProgramming.fibonacci_tabulation(n)
        print(f"Tabulation:      {tab_result}")
        
        # Optimized
        opt_result = DynamicProgramming.fibonacci_optimized(n)
        print(f"Space-optimized: {opt_result}")
        
        # Show first 15 Fibonacci numbers
        print(f"\nFirst 15 Fibonacci numbers:")
        fib_sequence = [DynamicProgramming.fibonacci_optimized(i) for i in range(15)]
        print(fib_sequence)
    
    @staticmethod
    def lcs_demonstration():
        """Demonstrate Longest Common Subsequence."""
        print("\n=== Longest Common Subsequence ===\n")
        
        text1 = "ABCDGH"
        text2 = "AEDFHR"
        
        print(f"Text 1: {text1}")
        print(f"Text 2: {text2}")
        
        lcs_length = DynamicProgramming.longest_common_subsequence(text1, text2, verbose=True)
        lcs_string = DynamicProgramming.lcs_with_string(text1, text2)
        
        print(f"\nLCS Length: {lcs_length}")
        print(f"LCS String: '{lcs_string}'")
    
    @staticmethod
    def knapsack_demonstration():
        """Demonstrate knapsack problems."""
        print("\n=== Knapsack Problems ===\n")
        
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        
        print(f"Items: {list(zip(weights, values))}")
        print(f"Capacity: {capacity}")
        
        # 0/1 Knapsack
        max_value_01 = DynamicProgramming.knapsack_01(weights, values, capacity, verbose=True)
        max_value_01_items, selected_items = DynamicProgramming.knapsack_01_items(weights, values, capacity)
        
        print(f"\n0/1 Knapsack:")
        print(f"Maximum value: {max_value_01}")
        print(f"Selected items (indices): {selected_items}")
        
        # Unbounded Knapsack
        max_value_unbounded = DynamicProgramming.unbounded_knapsack(weights, values, capacity)
        print(f"\nUnbounded Knapsack:")
        print(f"Maximum value: {max_value_unbounded}")
    
    @staticmethod
    def coin_change_demonstration():
        """Demonstrate coin change problems."""
        print("\n=== Coin Change Problems ===\n")
        
        coins = [1, 3, 4]
        amount = 6
        
        print(f"Coins: {coins}")
        print(f"Amount: {amount}")
        
        min_coins = DynamicProgramming.coin_change_min_coins(coins, amount)
        ways = DynamicProgramming.coin_change_ways(coins, amount)
        
        print(f"Minimum coins needed: {min_coins}")
        print(f"Number of ways: {ways}")
    
    @staticmethod
    def sequence_problems_demonstration():
        """Demonstrate sequence-related DP problems."""
        print("\n=== Sequence Problems ===\n")
        
        # Longest Increasing Subsequence
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        print(f"Array: {nums}")
        
        lis_length = DynamicProgramming.longest_increasing_subsequence(nums)
        lis_length_opt = DynamicProgramming.lis_binary_search(nums)
        
        print(f"LIS Length (O(n²)): {lis_length}")
        print(f"LIS Length (O(n log n)): {lis_length_opt}")
        
        # Edit Distance
        word1 = "horse"
        word2 = "ros"
        
        print(f"\nEdit Distance:")
        print(f"Word 1: '{word1}'")
        print(f"Word 2: '{word2}'")
        
        edit_dist = DynamicProgramming.edit_distance(word1, word2, verbose=True)
        print(f"Minimum edit distance: {edit_dist}")
        
        # Maximum Subarray
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        print(f"\nMaximum Subarray:")
        print(f"Array: {arr}")
        
        max_sum = DynamicProgramming.max_subarray_sum(arr)
        max_sum_with_indices, start, end = DynamicProgramming.max_subarray_indices(arr)
        
        print(f"Maximum sum: {max_sum}")
        print(f"Subarray indices: [{start}, {end}]")
        print(f"Subarray: {arr[start:end+1]}")
    
    @staticmethod
    def advanced_problems_demonstration():
        """Demonstrate advanced DP problems."""
        print("\n=== Advanced DP Problems ===\n")
        
        # Matrix Chain Multiplication
        dimensions = [1, 2, 3, 4]  # Matrices: 1x2, 2x3, 3x4
        print(f"Matrix dimensions: {dimensions}")
        
        mcm_cost = DynamicProgramming.matrix_chain_multiplication(dimensions)
        print(f"Minimum scalar multiplications: {mcm_cost}")
        
        # Palindrome problems
        s = "bbbab"
        print(f"\nPalindrome problems with string: '{s}'")
        
        lps_length = DynamicProgramming.longest_palindromic_subsequence(s)
        min_cuts = DynamicProgramming.palindrome_partitioning_min_cuts(s)
        
        print(f"Longest palindromic subsequence length: {lps_length}")
        print(f"Minimum cuts for palindrome partitioning: {min_cuts}")


def complexity_analysis():
    """Provide complexity analysis of DP algorithms."""
    print("\n=== DP Algorithms Complexity Analysis ===\n")
    
    complexities = {
        "Fibonacci (Naive Recursion)": ("O(2^n)", "O(n)"),
        "Fibonacci (Memoization)": ("O(n)", "O(n)"),
        "Fibonacci (Tabulation)": ("O(n)", "O(n)"),
        "Fibonacci (Optimized)": ("O(n)", "O(1)"),
        "LCS": ("O(m*n)", "O(m*n)"),
        "0/1 Knapsack": ("O(n*W)", "O(n*W)"),
        "Unbounded Knapsack": ("O(n*W)", "O(W)"),
        "Coin Change": ("O(amount*coins)", "O(amount)"),
        "LIS (DP)": ("O(n²)", "O(n)"),
        "LIS (Binary Search)": ("O(n log n)", "O(n)"),
        "Edit Distance": ("O(m*n)", "O(m*n)"),
        "Max Subarray": ("O(n)", "O(1)"),
        "Matrix Chain Multiplication": ("O(n³)", "O(n²)"),
        "Longest Palindromic Subsequence": ("O(n²)", "O(n²)"),
    }
    
    print(f"{'Algorithm':<35} {'Time':<15} {'Space':<15}")
    print("-" * 65)
    
    for algorithm, (time, space) in complexities.items():
        print(f"{algorithm:<35} {time:<15} {space:<15}")


def dp_principles():
    """Explain DP principles and when to use it."""
    print("\n=== Dynamic Programming Principles ===\n")
    
    principles = {
        "When to use DP": [
            "• Problem has overlapping subproblems",
            "• Problem has optimal substructure",
            "• Recursive solution has exponential time complexity",
            "• You can break problem into smaller similar problems"
        ],
        
        "Memoization vs Tabulation": [
            "Memoization (Top-down):",
            "  • Recursive approach with caching",
            "  • Only computes needed subproblems",
            "  • May have function call overhead",
            "",
            "Tabulation (Bottom-up):",
            "  • Iterative approach",
            "  • Computes all subproblems",
            "  • Usually more space/time efficient"
        ],
        
        "DP Optimization Techniques": [
            "• Space optimization: Use only necessary previous states",
            "• State compression: Reduce dimension of DP table",
            "• Rolling array: Use circular buffer for space",
            "• Binary lifting: For certain recursive problems"
        ],
        
        "Common DP Patterns": [
            "• Linear DP: dp[i] depends on dp[i-1], dp[i-2], etc.",
            "• Interval DP: dp[i][j] for subproblems on range [i,j]",
            "• Grid DP: 2D problems with dp[i][j]",
            "• Tree DP: DP on tree structures",
            "• Bitmask DP: Use bitmask to represent states"
        ]
    }
    
    for category, points in principles.items():
        print(f"{category}:")
        for point in points:
            if point:
                print(f"  {point}")
        print()


if __name__ == "__main__":
    print("🚀 Dynamic Programming - Comprehensive Tutorial\n")
    print("=" * 70)
    
    # Demonstrate various DP problems
    DPDemonstrator.fibonacci_comparison()
    DPDemonstrator.lcs_demonstration()
    DPDemonstrator.knapsack_demonstration()
    DPDemonstrator.coin_change_demonstration()
    DPDemonstrator.sequence_problems_demonstration()
    DPDemonstrator.advanced_problems_demonstration()
    
    # Show complexity analysis
    print("\n" + "=" * 70)
    complexity_analysis()
    
    # Explain principles
    print("\n" + "=" * 70)
    dp_principles()
    
    print("\n" + "=" * 70)
    print("✅ Dynamic Programming tutorial completed!")
    print("\n📝 Key Takeaways:")
    print("• DP solves problems by storing solutions to subproblems")
    print("• Two main approaches: memoization (top-down) and tabulation (bottom-up)")
    print("• Look for overlapping subproblems and optimal substructure")
    print("• Space optimization is often possible")
    print("• Many classic problems follow common DP patterns")
    print("• Practice identifying when DP is the right approach")