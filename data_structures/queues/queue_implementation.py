"""
Queue Data Structures - Comprehensive Implementation

This module demonstrates various queue implementations with detailed explanations,
time/space complexity analysis, and real-world applications.

Queue: FIFO (First In, First Out) data structure
- Elements are added at rear and removed from front
- Main operations: enqueue, dequeue, front, is_empty

Types covered:
1. Simple Queue (Array and Linked List based)
2. Circular Queue
3. Priority Queue
4. Double-ended Queue (Deque)

Author: Algorithm Learning Repository
"""

import heapq
from collections import deque


class ArrayQueue:
    """
    Array-based Queue Implementation
    
    Uses Python list with front and rear pointers.
    Simple but can waste space due to shifting elements.
    """
    
    def __init__(self, capacity=100):
        """
        Initialize queue with given capacity.
        
        Time Complexity: O(1)
        Space Complexity: O(n) where n is capacity
        """
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def is_empty(self):
        """
        Check if queue is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.size == 0
    
    def is_full(self):
        """
        Check if queue is full.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.size == self.capacity
    
    def enqueue(self, item):
        """
        Add item to the rear of queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_full():
            raise OverflowError("Queue overflow: Cannot enqueue to full queue")
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"Enqueued {item}")
    
    def dequeue(self):
        """
        Remove and return front item from queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue underflow: Cannot dequeue from empty queue")
        
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued {item}")
        return item
    
    def peek_front(self):
        """
        Return front item without removing it.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek empty queue")
        return self.queue[self.front]
    
    def peek_rear(self):
        """
        Return rear item without removing it.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek empty queue")
        return self.queue[self.rear]
    
    def get_size(self):
        """Return the number of items in queue."""
        return self.size
    
    def __str__(self):
        """Return string representation of queue."""
        if self.is_empty():
            return "Queue: []"
        
        items = []
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            items.append(str(self.queue[index]))
        
        return f"Queue: [front] {' <- '.join(items)} [rear]"


class Node:
    """Node class for linked list-based queue."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    """
    Linked List-based Queue Implementation
    
    Uses singly linked list with front and rear pointers.
    Dynamic size, no capacity limit.
    """
    
    def __init__(self):
        """
        Initialize empty queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.front = None
        self.rear = None
        self.size = 0
    
    def is_empty(self):
        """
        Check if queue is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.front is None
    
    def enqueue(self, item):
        """
        Add item to the rear of queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(item)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        print(f"Enqueued {item}")
    
    def dequeue(self):
        """
        Remove and return front item from queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue underflow: Cannot dequeue from empty queue")
        
        item = self.front.data
        self.front = self.front.next
        
        if self.front is None:  # Queue became empty
            self.rear = None
        
        self.size -= 1
        print(f"Dequeued {item}")
        return item
    
    def peek_front(self):
        """
        Return front item without removing it.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek empty queue")
        return self.front.data
    
    def get_size(self):
        """Return the number of items in queue."""
        return self.size
    
    def __str__(self):
        """Return string representation of queue."""
        if self.is_empty():
            return "Queue: []"
        
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        
        return f"Queue: [front] {' <- '.join(items)} [rear]"


class CircularQueue:
    """
    Circular Queue Implementation
    
    Efficiently uses array space by treating it as circular.
    No space wastage unlike simple array queue.
    """
    
    def __init__(self, capacity=10):
        """
        Initialize circular queue with given capacity.
        
        Time Complexity: O(1)
        Space Complexity: O(n) where n is capacity
        """
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
    
    def is_empty(self):
        """Check if queue is empty."""
        return self.size == 0
    
    def is_full(self):
        """Check if queue is full."""
        return self.size == self.capacity
    
    def enqueue(self, item):
        """
        Add item to the rear of circular queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_full():
            raise OverflowError("Circular queue overflow")
        
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        print(f"Enqueued {item}")
    
    def dequeue(self):
        """
        Remove and return front item from circular queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Circular queue underflow")
        
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued {item}")
        return item
    
    def peek_front(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek empty queue")
        return self.queue[self.front]
    
    def __str__(self):
        """Return string representation of circular queue."""
        if self.is_empty():
            return "Circular Queue: []"
        
        items = []
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            items.append(str(self.queue[index]))
        
        return f"Circular Queue: [front] {' <- '.join(items)} [rear]"


class PriorityQueueItem:
    """Item for priority queue with priority and data."""
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __str__(self):
        return f"({self.data}, priority={self.priority})"


class PriorityQueue:
    """
    Priority Queue Implementation using Min-Heap
    
    Elements are served based on priority, not insertion order.
    Higher priority (lower number) elements are served first.
    """
    
    def __init__(self):
        """
        Initialize empty priority queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.heap = []
        self.size = 0
    
    def is_empty(self):
        """Check if priority queue is empty."""
        return self.size == 0
    
    def enqueue(self, data, priority):
        """
        Add item with given priority.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        item = PriorityQueueItem(data, priority)
        heapq.heappush(self.heap, item)
        self.size += 1
        print(f"Enqueued {item}")
    
    def dequeue(self):
        """
        Remove and return highest priority item.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Priority queue underflow")
        
        item = heapq.heappop(self.heap)
        self.size -= 1
        print(f"Dequeued {item}")
        return item.data
    
    def peek(self):
        """
        Return highest priority item without removing it.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek empty priority queue")
        return self.heap[0].data
    
    def get_size(self):
        """Return the number of items in priority queue."""
        return self.size
    
    def __str__(self):
        """Return string representation of priority queue."""
        if self.is_empty():
            return "Priority Queue: []"
        
        items = [str(item) for item in self.heap]
        return f"Priority Queue: {items}"


class Deque:
    """
    Double-ended Queue (Deque) Implementation
    
    Allows insertion and deletion at both front and rear.
    Combines features of stack and queue.
    """
    
    def __init__(self):
        """
        Initialize empty deque.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.deque = deque()
    
    def is_empty(self):
        """Check if deque is empty."""
        return len(self.deque) == 0
    
    def add_front(self, item):
        """
        Add item to the front.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.deque.appendleft(item)
        print(f"Added {item} to front")
    
    def add_rear(self, item):
        """
        Add item to the rear.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.deque.append(item)
        print(f"Added {item} to rear")
    
    def remove_front(self):
        """
        Remove and return front item.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Deque underflow")
        
        item = self.deque.popleft()
        print(f"Removed {item} from front")
        return item
    
    def remove_rear(self):
        """
        Remove and return rear item.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Deque underflow")
        
        item = self.deque.pop()
        print(f"Removed {item} from rear")
        return item
    
    def peek_front(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek empty deque")
        return self.deque[0]
    
    def peek_rear(self):
        """Return rear item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek empty deque")
        return self.deque[-1]
    
    def size(self):
        """Return the number of items in deque."""
        return len(self.deque)
    
    def __str__(self):
        """Return string representation of deque."""
        if self.is_empty():
            return "Deque: []"
        return f"Deque: [front] {list(self.deque)} [rear]"


class QueueApplications:
    """Collection of real-world queue applications."""
    
    @staticmethod
    def breadth_first_search(graph, start):
        """
        BFS traversal using queue.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = set()
        queue = LinkedQueue()
        result = []
        
        queue.enqueue(start)
        visited.add(start)
        
        while not queue.is_empty():
            vertex = queue.dequeue()
            result.append(vertex)
            
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
        
        return result
    
    @staticmethod
    def sliding_window_maximum(arr, k):
        """
        Find maximum in each sliding window using deque.
        
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        from collections import deque
        dq = deque()
        result = []
        
        for i in range(len(arr)):
            # Remove elements outside current window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove elements smaller than current
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            
            dq.append(i)
            
            # Add to result if window is complete
            if i >= k - 1:
                result.append(arr[dq[0]])
        
        return result
    
    @staticmethod
    def task_scheduler(tasks, priorities):
        """
        Schedule tasks based on priority using priority queue.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        pq = PriorityQueue()
        
        # Add all tasks to priority queue
        for task, priority in zip(tasks, priorities):
            pq.enqueue(task, priority)
        
        execution_order = []
        while not pq.is_empty():
            task = pq.dequeue()
            execution_order.append(task)
        
        return execution_order


def demonstrate_basic_queues():
    """Demonstrate basic queue operations."""
    print("=== Array-based Queue ===\n")
    
    # Array-based queue
    queue = ArrayQueue(5)
    
    # Test enqueue operations
    for i in range(1, 6):
        queue.enqueue(i * 10)
    
    print(f"Queue after enqueues: {queue}")
    print(f"Front element: {queue.peek_front()}")
    print(f"Rear element: {queue.peek_rear()}")
    
    # Test dequeue operations
    print("\nDequeuing elements:")
    for _ in range(3):
        queue.dequeue()
    
    print(f"Queue after 3 dequeues: {queue}")
    
    print(f"\n=== Linked List-based Queue ===\n")
    
    # Linked list-based queue
    lq = LinkedQueue()
    
    for char in ['A', 'B', 'C', 'D']:
        lq.enqueue(char)
    
    print(f"Queue after enqueues: {lq}")
    
    lq.dequeue()
    lq.dequeue()
    print(f"Queue after 2 dequeues: {lq}")


def demonstrate_special_queues():
    """Demonstrate circular queue, priority queue, and deque."""
    print("\n=== Circular Queue ===\n")
    
    cq = CircularQueue(4)
    
    # Fill the circular queue
    for i in range(1, 5):
        cq.enqueue(i)
    
    print(f"Circular queue: {cq}")
    
    # Dequeue and enqueue to show circular nature
    cq.dequeue()
    cq.dequeue()
    cq.enqueue(5)
    cq.enqueue(6)
    
    print(f"After dequeue/enqueue: {cq}")
    
    print(f"\n=== Priority Queue ===\n")
    
    pq = PriorityQueue()
    
    # Add tasks with different priorities
    tasks = [("Task A", 3), ("Task B", 1), ("Task C", 2), ("Task D", 1)]
    for task, priority in tasks:
        pq.enqueue(task, priority)
    
    print(f"Priority queue: {pq}")
    
    print("\nProcessing tasks by priority:")
    while not pq.is_empty():
        pq.dequeue()
    
    print(f"\n=== Double-ended Queue (Deque) ===\n")
    
    dq = Deque()
    
    # Test various operations
    dq.add_rear(1)
    dq.add_rear(2)
    dq.add_front(0)
    dq.add_front(-1)
    
    print(f"Deque after additions: {dq}")
    
    dq.remove_front()
    dq.remove_rear()
    
    print(f"Deque after removals: {dq}")


def demonstrate_queue_applications():
    """Demonstrate real-world queue applications."""
    print("\n=== Queue Applications ===\n")
    
    # BFS example
    print("--- Breadth-First Search ---")
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    bfs_result = QueueApplications.breadth_first_search(graph, 'A')
    print(f"BFS from A: {bfs_result}")
    
    # Sliding window maximum
    print(f"\n--- Sliding Window Maximum ---")
    arrays = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3),
        ([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)
    ]
    
    for arr, k in arrays:
        max_values = QueueApplications.sliding_window_maximum(arr, k)
        print(f"Array: {arr}, k={k}")
        print(f"Sliding window maximums: {max_values}")
    
    # Task scheduling
    print(f"\n--- Task Scheduling ---")
    tasks = ["Email", "Meeting", "Code Review", "Documentation", "Testing"]
    priorities = [2, 1, 1, 3, 2]
    
    execution_order = QueueApplications.task_scheduler(tasks, priorities)
    print(f"Tasks: {tasks}")
    print(f"Priorities: {priorities}")
    print(f"Execution order: {execution_order}")


def test_edge_cases():
    """Test edge cases and error handling."""
    print("\n=== Edge Cases Testing ===\n")
    
    # Test empty queue operations
    queue = ArrayQueue(3)
    
    try:
        print("Testing dequeue on empty queue...")
        queue.dequeue()
    except IndexError as e:
        print(f"✓ Caught expected error: {e}")
    
    try:
        print("Testing peek on empty queue...")
        queue.peek_front()
    except IndexError as e:
        print(f"✓ Caught expected error: {e}")
    
    # Test queue overflow
    try:
        print("Testing queue overflow...")
        for i in range(5):  # Capacity is 3
            queue.enqueue(i)
    except OverflowError as e:
        print(f"✓ Caught expected error: {e}")


if __name__ == "__main__":
    print("🚀 Queue Data Structures - Comprehensive Tutorial\n")
    print("=" * 60)
    
    # Demonstrate basic operations
    demonstrate_basic_queues()
    
    # Demonstrate special queues
    demonstrate_special_queues()
    
    # Test edge cases
    test_edge_cases()
    
    # Demonstrate applications
    print("\n" + "=" * 60)
    demonstrate_queue_applications()
    
    print("\n" + "=" * 60)
    print("✅ Queue tutorial completed!")
    print("\n📝 Key Takeaways:")
    print("• Queue follows FIFO (First In, First Out) principle")
    print("• Basic operations are O(1) for all implementations")
    print("• Circular queue efficiently uses array space")
    print("• Priority queue serves elements by priority, not insertion order")
    print("• Deque allows operations at both ends")
    print("• Essential for BFS, task scheduling, and buffering")
    print("• Choose implementation based on specific requirements")