"""
Linked Lists - Comprehensive Implementation

This module demonstrates various types of linked lists with detailed explanations,
time/space complexity analysis, and multiple test scenarios.

Linked Lists are linear data structures where elements are stored in nodes,
and each node contains data and a reference to the next node.

Types covered:
1. Singly Linked List
2. Doubly Linked List  
3. Circular Linked List

Author: Algorithm Learning Repository
"""

class Node:
    """Node class for singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyNode:
    """Node class for doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    """
    Singly Linked List Implementation
    
    Each node points to the next node in the sequence.
    Provides efficient insertion/deletion at the beginning.
    """
    
    def __init__(self):
        """
        Initialize empty linked list.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head = None
        self.size = 0
    
    def append(self, data):
        """
        Add element to the end of the list.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data):
        """
        Add element to the beginning of the list.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert(self, index, data):
        """
        Insert element at given index.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, data):
        """
        Delete first occurrence of data.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not self.head:
            raise ValueError("List is empty")
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            self.size -= 1
        else:
            raise ValueError(f"Data {data} not found in list")
    
    def delete_at(self, index):
        """
        Delete element at given index.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        current.next = current.next.next
        self.size -= 1
    
    def find(self, data):
        """
        Find index of first occurrence of data.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
    
    def reverse(self):
        """
        Reverse the linked list in-place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = self.head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        self.head = prev
    
    def get_middle(self):
        """
        Find middle element using two-pointer technique.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not self.head:
            return None
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def has_cycle(self):
        """
        Detect cycle using Floyd's algorithm.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not self.head:
            return False
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
    
    def __len__(self):
        """Return the size of the list."""
        return self.size
    
    def __str__(self):
        """Return string representation of the list."""
        if not self.head:
            return "[]"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        
        return " -> ".join(result) + " -> None"


class DoublyLinkedList:
    """
    Doubly Linked List Implementation
    
    Each node has references to both next and previous nodes.
    Allows efficient bidirectional traversal.
    """
    
    def __init__(self):
        """
        Initialize empty doubly linked list.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        """
        Add element to the end of the list.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def prepend(self, data):
        """
        Add element to the beginning of the list.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def delete(self, data):
        """
        Delete first occurrence of data.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self.size -= 1
                return
            current = current.next
        
        raise ValueError(f"Data {data} not found in list")
    
    def reverse(self):
        """
        Reverse the doubly linked list.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        
        self.head, self.tail = self.tail, self.head
    
    def __str__(self):
        """Return string representation of the list."""
        if not self.head:
            return "[]"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        
        return " <-> ".join(result)


class CircularLinkedList:
    """
    Circular Linked List Implementation
    
    The last node points back to the first node, forming a circle.
    Useful for round-robin scheduling and cyclic operations.
    """
    
    def __init__(self):
        """
        Initialize empty circular linked list.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head = None
        self.size = 0
    
    def append(self, data):
        """
        Add element to the end of the list.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.size += 1
    
    def prepend(self, data):
        """
        Add element to the beginning of the list.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
        self.size += 1
    
    def delete(self, data):
        """
        Delete first occurrence of data.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not self.head:
            raise ValueError("List is empty")
        
        if self.head.data == data:
            if self.size == 1:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        while current.next != self.head and current.next.data != data:
            current = current.next
        
        if current.next.data == data:
            current.next = current.next.next
            self.size -= 1
        else:
            raise ValueError(f"Data {data} not found in list")
    
    def __str__(self):
        """Return string representation of the list."""
        if not self.head:
            return "[]"
        
        result = []
        current = self.head
        while True:
            result.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        
        return " -> ".join(result) + " -> (back to start)"


def linked_list_algorithms():
    """Demonstrate advanced linked list algorithms."""
    
    def merge_sorted_lists(list1, list2):
        """
        Merge two sorted linked lists.
        
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        dummy = Node(0)
        current = dummy
        
        l1, l2 = list1.head, list2.head
        while l1 and l2:
            if l1.data <= l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 or l2
        
        result = SinglyLinkedList()
        result.head = dummy.next
        return result
    
    def remove_duplicates(linked_list):
        """
        Remove duplicates from sorted linked list.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not linked_list.head:
            return
        
        current = linked_list.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
                linked_list.size -= 1
            else:
                current = current.next
    
    # Demonstration
    print("=== Advanced Linked List Algorithms ===\n")
    
    # Merge sorted lists
    list1 = SinglyLinkedList()
    list2 = SinglyLinkedList()
    
    for val in [1, 3, 5]:
        list1.append(val)
    for val in [2, 4, 6]:
        list2.append(val)
    
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    
    merged = merge_sorted_lists(list1, list2)
    print(f"Merged: {merged}")
    
    # Remove duplicates
    dup_list = SinglyLinkedList()
    for val in [1, 1, 2, 3, 3, 3, 4]:
        dup_list.append(val)
    
    print(f"\nBefore removing duplicates: {dup_list}")
    remove_duplicates(dup_list)
    print(f"After removing duplicates: {dup_list}")


def demonstrate_linked_lists():
    """Comprehensive demonstration of all linked list types."""
    
    print("=== Singly Linked List ===\n")
    sll = SinglyLinkedList()
    
    # Test operations
    for i in range(1, 6):
        sll.append(i)
    print(f"After appending 1-5: {sll}")
    
    sll.prepend(0)
    print(f"After prepending 0: {sll}")
    
    sll.insert(3, 99)
    print(f"After inserting 99 at index 3: {sll}")
    
    print(f"Middle element: {sll.get_middle()}")
    
    sll.reverse()
    print(f"After reversing: {sll}")
    
    print(f"Find 99: index {sll.find(99)}")
    
    print(f"\n=== Doubly Linked List ===\n")
    dll = DoublyLinkedList()
    
    for i in range(1, 6):
        dll.append(i)
    print(f"After appending 1-5: {dll}")
    
    dll.prepend(0)
    print(f"After prepending 0: {dll}")
    
    dll.reverse()
    print(f"After reversing: {dll}")
    
    print(f"\n=== Circular Linked List ===\n")
    cll = CircularLinkedList()
    
    for i in range(1, 5):
        cll.append(i)
    print(f"After appending 1-4: {cll}")
    
    cll.prepend(0)
    print(f"After prepending 0: {cll}")


if __name__ == "__main__":
    print("🚀 Linked Lists - Comprehensive Tutorial\n")
    print("=" * 50)
    
    # Demonstrate all linked list types
    demonstrate_linked_lists()
    
    # Show advanced algorithms
    print("\n" + "=" * 50)
    linked_list_algorithms()
    
    print("\n" + "=" * 50)
    print("✅ Linked Lists tutorial completed!")
    print("\n📝 Key Takeaways:")
    print("• Singly: O(1) insertion at head, O(n) at arbitrary position")
    print("• Doubly: O(1) insertion/deletion at both ends")
    print("• Circular: Useful for round-robin and cyclic operations")
    print("• Two-pointer technique for cycle detection and finding middle")
    print("• Linked lists excel when frequent insertions/deletions needed")