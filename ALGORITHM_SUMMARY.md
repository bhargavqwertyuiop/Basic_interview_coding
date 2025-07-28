# 🚀 Comprehensive Algorithms and Data Structures Implementation

This repository contains a complete collection of fundamental algorithms and data structures implemented in Python with detailed explanations, complexity analysis, and educational demonstrations.

## 📋 Complete Implementation List

### 🏗️ Data Structures

#### 1. **Arrays** (`data_structures/arrays/array_operations.py`)
- **Dynamic Array Implementation**
  - Resizable array with automatic capacity management
  - O(1) amortized append, O(1) access
  - Insert, delete, find, reverse operations
- **Array Algorithms**
  - Two Sum Problem (O(n) with hash map)
  - Maximum Subarray Sum (Kadane's Algorithm)
  - Array Rotation (O(n) time, O(1) space)
  - Merge Sorted Arrays

#### 2. **Linked Lists** (`data_structures/linked_lists/linked_list_implementation.py`)
- **Singly Linked List**
  - Insert, delete, search operations
  - Reverse, find middle, cycle detection
- **Doubly Linked List**
  - Bidirectional traversal
  - O(1) insertion/deletion at both ends
- **Circular Linked List**
  - Round-robin applications
  - Continuous traversal capability
- **Advanced Algorithms**
  - Merge sorted linked lists
  - Remove duplicates
  - Floyd's cycle detection algorithm

#### 3. **Stacks** (`data_structures/stacks/stack_implementation.py`)
- **Array-based Stack**
  - Fixed capacity with overflow protection
  - O(1) all operations
- **Linked List-based Stack**
  - Dynamic size, no capacity limit
  - Memory efficient for variable sizes
- **Applications**
  - Balanced Parentheses Checker
  - Postfix Expression Evaluation
  - Infix to Postfix Conversion (Shunting Yard Algorithm)
  - Next Greater Element
  - Largest Rectangle in Histogram

#### 4. **Queues** (`data_structures/queues/queue_implementation.py`)
- **Array-based Queue**
  - Circular implementation to avoid wastage
  - Front and rear pointer management
- **Linked List-based Queue**
  - Dynamic size with O(1) operations
  - Memory efficient
- **Circular Queue**
  - Efficient space utilization
  - Fixed size with wraparound
- **Priority Queue**
  - Min-heap based implementation
  - O(log n) insertion and extraction
- **Double-ended Queue (Deque)**
  - Operations at both ends
  - Combines stack and queue functionality
- **Applications**
  - Breadth-First Search (BFS)
  - Sliding Window Maximum
  - Task Scheduling

#### 5. **Binary Trees** (`data_structures/trees/binary_tree_implementation.py`)
- **Basic Binary Tree**
  - Level-order insertion
  - Tree traversals (inorder, preorder, postorder, level-order)
  - Height calculation, node counting
- **Binary Search Tree (BST)**
  - Insert, delete, search operations
  - Find min/max values
  - BST validation
- **AVL Tree (Self-balancing BST)**
  - Automatic balancing with rotations
  - Guaranteed O(log n) operations
  - Left and right rotations
- **Tree Algorithms**
  - Lowest Common Ancestor (LCA)
  - Tree balance checking
  - Diameter calculation
  - Visual tree printing

### 🔄 Algorithms

#### 6. **Sorting Algorithms** (`algorithms/sorting/sorting_algorithms.py`)
- **Comparison-based Sorts**
  - **Bubble Sort**: O(n²), stable, adaptive
  - **Selection Sort**: O(n²), not stable
  - **Insertion Sort**: O(n²) worst, O(n) best, stable, adaptive
  - **Merge Sort**: O(n log n) all cases, stable, divide & conquer
  - **Quick Sort**: O(n log n) average, O(n²) worst, in-place
  - **Heap Sort**: O(n log n) all cases, in-place, not stable
- **Non-comparison Sorts**
  - **Counting Sort**: O(n + k), stable, for integers
  - **Radix Sort**: O(d × (n + k)), stable, for fixed-width data
  - **Bucket Sort**: O(n + k) average, for uniformly distributed data
- **Performance Analysis**
  - Detailed complexity comparison
  - Best-case scenarios for each algorithm
  - Real-world application guidelines

#### 7. **Search Algorithms** (`algorithms/searching/search_algorithms.py`)
- **Linear Search**
  - O(n) time, works on unsorted data
  - Simple implementation
- **Binary Search**
  - Iterative and recursive implementations
  - O(log n) time, requires sorted data
- **Advanced Search Algorithms**
  - **Jump Search**: O(√n), good for sorted data
  - **Interpolation Search**: O(log log n) average for uniform data
  - **Exponential Search**: O(log n), good for unbounded arrays
  - **Fibonacci Search**: O(log n), uses Fibonacci numbers
  - **Ternary Search**: O(log₃ n), divides into three parts
- **Graph Search Algorithms**
  - **Depth-First Search (DFS)**: O(V + E), uses stack/recursion
  - **Breadth-First Search (BFS)**: O(V + E), uses queue
  - **Shortest Path (BFS)**: Finds shortest path in unweighted graphs

#### 8. **Dynamic Programming** (`algorithms/dynamic_programming/dp_algorithms.py`)
- **Classic DP Problems**
  - **Fibonacci Sequence**: Memoization, tabulation, space-optimized
  - **Longest Common Subsequence (LCS)**: String comparison
  - **Knapsack Problems**: 0/1 and unbounded variants
  - **Coin Change**: Minimum coins and number of ways
  - **Longest Increasing Subsequence (LIS)**: O(n²) and O(n log n)
  - **Edit Distance**: Levenshtein distance with operations
  - **Maximum Subarray Sum**: Kadane's algorithm
  - **Matrix Chain Multiplication**: Optimal parenthesization
  - **Palindrome Problems**: LPS and minimum cuts
- **DP Techniques**
  - Memoization (top-down) vs Tabulation (bottom-up)
  - Space optimization techniques
  - State compression methods
- **Pattern Recognition**
  - Linear DP, interval DP, grid DP patterns
  - When to apply dynamic programming

## 📊 Complexity Analysis Summary

### Time Complexities
| Data Structure | Access | Search | Insertion | Deletion |
|---------------|--------|--------|-----------|----------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1)* |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue | O(n) | O(n) | O(1) | O(1) |
| BST | O(log n)† | O(log n)† | O(log n)† | O(log n)† |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) |

*At known position  
†Average case, O(n) worst case for unbalanced BST

### Sorting Algorithm Complexities
| Algorithm | Best Case | Average Case | Worst Case | Space | Stable |
|-----------|-----------|--------------|------------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |
| Radix Sort | O(d(n + k)) | O(d(n + k)) | O(d(n + k)) | O(n + k) | Yes |

### Search Algorithm Complexities
| Algorithm | Time Complexity | Space | Prerequisites |
|-----------|----------------|-------|---------------|
| Linear Search | O(n) | O(1) | None |
| Binary Search | O(log n) | O(1) | Sorted array |
| Jump Search | O(√n) | O(1) | Sorted array |
| Interpolation Search | O(log log n)* | O(1) | Sorted, uniform distribution |
| Fibonacci Search | O(log n) | O(1) | Sorted array |
| DFS/BFS | O(V + E) | O(V) | Graph representation |

*Average case for uniformly distributed data

## 🎯 Learning Path Recommendations

### **Beginner Level**
1. **Start with Arrays**: Understanding indexing, basic operations
2. **Move to Linked Lists**: Pointer manipulation, dynamic memory
3. **Learn Stacks and Queues**: LIFO/FIFO principles, applications
4. **Basic Sorting**: Bubble, Selection, Insertion sorts
5. **Linear and Binary Search**: Foundation of searching

### **Intermediate Level**
1. **Binary Trees**: Tree traversals, BST operations
2. **Advanced Sorting**: Merge Sort, Quick Sort, Heap Sort
3. **Basic Dynamic Programming**: Fibonacci, simple DP problems
4. **Graph Basics**: DFS, BFS traversals

### **Advanced Level**
1. **Self-balancing Trees**: AVL rotations, tree balancing
2. **Advanced DP**: Complex state transitions, optimization
3. **Specialized Searches**: Interpolation, exponential search
4. **Algorithm Optimization**: Space-time tradeoffs, advanced techniques

## 🔧 Usage Instructions

### Running Individual Modules
```bash
# Run specific algorithm demonstrations
python3 data_structures/arrays/array_operations.py
python3 algorithms/sorting/sorting_algorithms.py
python3 algorithms/dynamic_programming/dp_algorithms.py
```

### Interactive Demo Runner
```bash
# Run the comprehensive demo with interactive menu
python3 run_all_demos.py
```

### Features of Each Implementation
- **Detailed Code Comments**: Every function documented with complexity analysis
- **Verbose Mode**: Step-by-step execution visualization
- **Error Handling**: Comprehensive edge case management
- **Multiple Test Cases**: Various scenarios and inputs
- **Educational Focus**: Clear explanations of algorithmic thinking

## 🎓 Educational Benefits

### **Interview Preparation**
- Complete coverage of common coding interview topics
- Time/space complexity analysis for every algorithm
- Multiple implementation approaches
- Real-world application scenarios

### **Academic Learning**
- Theoretical concepts implemented in practice
- Visual demonstrations of algorithm execution
- Complexity analysis with Big O notation
- Algorithm comparison and selection criteria

### **Professional Development**
- Best practices in algorithm implementation
- Clean, readable, and maintainable code
- Performance optimization techniques
- Problem-solving methodologies

## 🔄 Contributing and Extension

This implementation provides a solid foundation that can be extended with:
- Additional algorithms (graph algorithms, string algorithms)
- More data structures (hash tables, heaps, tries)
- Performance benchmarking tools
- Visualization components
- More advanced DP problems
- Geometric algorithms
- Network flow algorithms

## 📚 References and Further Learning

Each implementation includes references to:
- Original algorithm papers and sources
- Time/space complexity proofs
- Real-world applications
- Alternative implementations
- Optimization techniques
- Related algorithms and data structures

This comprehensive collection serves as both a learning resource and a reference implementation for fundamental computer science concepts, providing a strong foundation for algorithmic thinking and problem-solving skills.