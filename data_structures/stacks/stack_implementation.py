"""
Stack Data Structure - Comprehensive Implementation

This module demonstrates stack implementations using different approaches
with detailed explanations, time/space complexity analysis, and real-world applications.

Stack: LIFO (Last In, First Out) data structure
- Elements are added and removed from the top
- Main operations: push, pop, peek/top, is_empty

Implementations covered:
1. Array-based Stack
2. Linked List-based Stack
3. Stack Applications (Expression evaluation, Balancing parentheses, etc.)

Author: Algorithm Learning Repository
"""

class ArrayStack:
    """
    Array-based Stack Implementation
    
    Uses Python list as underlying storage.
    Provides O(1) amortized operations.
    """
    
    def __init__(self, capacity=100):
        """
        Initialize stack with given capacity.
        
        Time Complexity: O(1)
        Space Complexity: O(n) where n is capacity
        """
        self.capacity = capacity
        self.stack = []
        self.top_index = -1
    
    def is_empty(self):
        """
        Check if stack is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.top_index == -1
    
    def is_full(self):
        """
        Check if stack is full.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.top_index == self.capacity - 1
    
    def push(self, item):
        """
        Add item to the top of the stack.
        
        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        """
        if self.is_full():
            raise OverflowError("Stack overflow: Cannot push to full stack")
        
        self.stack.append(item)
        self.top_index += 1
        print(f"Pushed {item}")
    
    def pop(self):
        """
        Remove and return the top item from stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from empty stack")
        
        item = self.stack.pop()
        self.top_index -= 1
        print(f"Popped {item}")
        return item
    
    def peek(self):
        """
        Return the top item without removing it.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek empty stack")
        
        return self.stack[self.top_index]
    
    def size(self):
        """
        Return the number of items in stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.top_index + 1
    
    def __str__(self):
        """Return string representation of stack."""
        if self.is_empty():
            return "Stack: []"
        return f"Stack: {self.stack} <- top"


class Node:
    """Node class for linked list-based stack."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    """
    Linked List-based Stack Implementation
    
    Uses singly linked list as underlying storage.
    No capacity limit (limited only by available memory).
    """
    
    def __init__(self):
        """
        Initialize empty stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head = None
        self._size = 0
    
    def is_empty(self):
        """
        Check if stack is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.head is None
    
    def push(self, item):
        """
        Add item to the top of the stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        print(f"Pushed {item}")
    
    def pop(self):
        """
        Remove and return the top item from stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from empty stack")
        
        item = self.head.data
        self.head = self.head.next
        self._size -= 1
        print(f"Popped {item}")
        return item
    
    def peek(self):
        """
        Return the top item without removing it.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek empty stack")
        
        return self.head.data
    
    def size(self):
        """
        Return the number of items in stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size
    
    def __str__(self):
        """Return string representation of stack."""
        if self.is_empty():
            return "Stack: []"
        
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        
        return f"Stack: {' -> '.join(items)} <- top"


class StackApplications:
    """Collection of real-world stack applications."""
    
    @staticmethod
    def is_balanced_parentheses(expression):
        """
        Check if parentheses in expression are balanced.
        
        Algorithm: Use stack to track opening brackets
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Examples:
        - "()" -> True
        - "()[]{}" -> True  
        - "([)]" -> False
        """
        stack = ArrayStack()
        opening = {'(', '[', '{'}
        closing = {')', ']', '}'}
        pairs = {'(': ')', '[': ']', '{': '}'}
        
        for char in expression:
            if char in opening:
                stack.push(char)
            elif char in closing:
                if stack.is_empty():
                    return False
                
                top = stack.pop()
                if pairs[top] != char:
                    return False
        
        return stack.is_empty()
    
    @staticmethod
    def evaluate_postfix(expression):
        """
        Evaluate postfix (RPN) expression.
        
        Algorithm: Use stack to store operands
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Example: "3 4 + 2 *" -> 14
        """
        stack = ArrayStack()
        operators = {'+', '-', '*', '/', '^'}
        
        for token in expression.split():
            if token not in operators:
                # It's a number
                stack.push(float(token))
            else:
                # It's an operator
                if stack.size() < 2:
                    raise ValueError("Invalid expression")
                
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise ValueError("Division by zero")
                    result = a / b
                elif token == '^':
                    result = a ** b
                
                stack.push(result)
        
        if stack.size() != 1:
            raise ValueError("Invalid expression")
        
        return stack.pop()
    
    @staticmethod
    def infix_to_postfix(expression):
        """
        Convert infix expression to postfix.
        
        Algorithm: Shunting Yard algorithm
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Example: "3 + 4 * 2" -> "3 4 2 * +"
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        right_associative = {'^'}
        
        output = []
        operator_stack = ArrayStack()
        
        tokens = expression.split()
        
        for token in tokens:
            if token.isdigit() or '.' in token:
                # It's a number
                output.append(token)
            elif token == '(':
                operator_stack.push(token)
            elif token == ')':
                while not operator_stack.is_empty() and operator_stack.peek() != '(':
                    output.append(operator_stack.pop())
                if not operator_stack.is_empty():
                    operator_stack.pop()  # Remove '('
            elif token in precedence:
                while (not operator_stack.is_empty() and 
                       operator_stack.peek() != '(' and
                       (precedence.get(operator_stack.peek(), 0) > precedence[token] or
                        (precedence.get(operator_stack.peek(), 0) == precedence[token] and 
                         token not in right_associative))):
                    output.append(operator_stack.pop())
                operator_stack.push(token)
        
        while not operator_stack.is_empty():
            output.append(operator_stack.pop())
        
        return ' '.join(output)
    
    @staticmethod
    def next_greater_element(arr):
        """
        Find the next greater element for each element in array.
        
        Algorithm: Use stack to store indices
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Example: [4, 5, 2, 25] -> [5, 25, 25, -1]
        """
        stack = ArrayStack()
        result = [-1] * len(arr)
        
        for i in range(len(arr)):
            while not stack.is_empty() and arr[stack.peek()] < arr[i]:
                index = stack.pop()
                result[index] = arr[i]
            stack.push(i)
        
        return result
    
    @staticmethod
    def largest_rectangle_histogram(heights):
        """
        Find the largest rectangle area in histogram.
        
        Algorithm: Use stack to maintain increasing heights
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = ArrayStack()
        max_area = 0
        
        for i, height in enumerate(heights):
            while not stack.is_empty() and heights[stack.peek()] > height:
                h = heights[stack.pop()]
                w = i if stack.is_empty() else i - stack.peek() - 1
                max_area = max(max_area, h * w)
            stack.push(i)
        
        while not stack.is_empty():
            h = heights[stack.pop()]
            w = len(heights) if stack.is_empty() else len(heights) - stack.peek() - 1
            max_area = max(max_area, h * w)
        
        return max_area


def demonstrate_stack_operations():
    """Demonstrate basic stack operations."""
    print("=== Array-based Stack ===\n")
    
    # Array-based stack
    stack = ArrayStack(5)
    
    # Test push operations
    for i in range(1, 6):
        stack.push(i * 10)
    
    print(f"Stack after pushes: {stack}")
    print(f"Stack size: {stack.size()}")
    print(f"Top element: {stack.peek()}")
    
    # Test pop operations
    print("\nPopping elements:")
    while not stack.is_empty():
        stack.pop()
    
    print(f"Final stack: {stack}")
    
    print(f"\n=== Linked List-based Stack ===\n")
    
    # Linked list-based stack
    ll_stack = LinkedListStack()
    
    for char in ['A', 'B', 'C', 'D']:
        ll_stack.push(char)
    
    print(f"Stack after pushes: {ll_stack}")
    
    # Pop a few elements
    ll_stack.pop()
    ll_stack.pop()
    print(f"Stack after 2 pops: {ll_stack}")


def demonstrate_stack_applications():
    """Demonstrate real-world stack applications."""
    print("=== Stack Applications ===\n")
    
    # Balanced parentheses
    expressions = [
        "()",
        "()[]{}", 
        "([)]",
        "((()))",
        "((("
    ]
    
    print("--- Balanced Parentheses ---")
    for expr in expressions:
        balanced = StackApplications.is_balanced_parentheses(expr)
        print(f"'{expr}' is {'balanced' if balanced else 'not balanced'}")
    
    # Postfix evaluation
    print(f"\n--- Postfix Evaluation ---")
    postfix_expressions = [
        "3 4 +",
        "3 4 + 2 *",
        "15 7 1 1 + - / 3 * 2 1 1 + + -"
    ]
    
    for expr in postfix_expressions:
        try:
            result = StackApplications.evaluate_postfix(expr)
            print(f"'{expr}' = {result}")
        except Exception as e:
            print(f"'{expr}' -> Error: {e}")
    
    # Infix to postfix conversion
    print(f"\n--- Infix to Postfix Conversion ---")
    infix_expressions = [
        "3 + 4",
        "3 + 4 * 2",
        "( 3 + 4 ) * 2",
        "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
    ]
    
    for expr in infix_expressions:
        postfix = StackApplications.infix_to_postfix(expr)
        print(f"'{expr}' -> '{postfix}'")
    
    # Next greater element
    print(f"\n--- Next Greater Element ---")
    arrays = [
        [4, 5, 2, 25],
        [13, 7, 6, 12],
        [1, 3, 2, 4]
    ]
    
    for arr in arrays:
        nge = StackApplications.next_greater_element(arr)
        print(f"{arr} -> {nge}")
    
    # Largest rectangle in histogram
    print(f"\n--- Largest Rectangle in Histogram ---")
    histograms = [
        [2, 1, 5, 6, 2, 3],
        [6, 2, 5, 4, 5, 1, 6],
        [1, 1, 1, 1]
    ]
    
    for hist in histograms:
        area = StackApplications.largest_rectangle_histogram(hist)
        print(f"Heights {hist} -> Max area: {area}")


def test_edge_cases():
    """Test edge cases and error handling."""
    print("\n=== Edge Cases Testing ===\n")
    
    # Test empty stack operations
    stack = ArrayStack(3)
    
    try:
        print("Testing pop on empty stack...")
        stack.pop()
    except IndexError as e:
        print(f"✓ Caught expected error: {e}")
    
    try:
        print("Testing peek on empty stack...")
        stack.peek()
    except IndexError as e:
        print(f"✓ Caught expected error: {e}")
    
    # Test stack overflow
    try:
        print("Testing stack overflow...")
        for i in range(5):  # Capacity is 3
            stack.push(i)
    except OverflowError as e:
        print(f"✓ Caught expected error: {e}")


if __name__ == "__main__":
    print("🚀 Stack Data Structure - Comprehensive Tutorial\n")
    print("=" * 60)
    
    # Demonstrate basic operations
    demonstrate_stack_operations()
    
    # Test edge cases
    test_edge_cases()
    
    # Demonstrate applications
    print("\n" + "=" * 60)
    demonstrate_stack_applications()
    
    print("\n" + "=" * 60)
    print("✅ Stack tutorial completed!")
    print("\n📝 Key Takeaways:")
    print("• Stack follows LIFO (Last In, First Out) principle")
    print("• All basic operations are O(1) time complexity")
    print("• Perfect for expression evaluation and syntax parsing")
    print("• Useful for backtracking and function call management")
    print("• Array-based: Fixed size, cache-friendly")
    print("• Linked list-based: Dynamic size, extra memory overhead")