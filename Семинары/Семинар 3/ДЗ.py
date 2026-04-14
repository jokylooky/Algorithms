from typing import Optional, List
import heapq

'''Очередь'''


print('Задание 1. Реализовать очередь на двух стеках.')
'''1. Реализовать очередь на двух стеках.'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        """Добавить элемент в конец стека"""
        self.items.append(x)

    def pop(self):
        """Удалить и вернуть последний элемент (выбросит ошибку на пустом стеке)"""
        return self.items.pop()

    def peek(self):
        """Вернуть последний элемент без удаления (выбросит ошибку на пустом стеке)"""
        return self.items[-1]

    def view(self):
        """Вернуть весь стек"""
        return self.items

    def isEmpty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.leftStack = Stack()
        self.rightStack = Stack()
        self._size = 0

    def __str__(self):
        right_rev = self.rightStack.items[::-1]  # т.к. в rightStack элементы в обратном порядке
        return str(right_rev + self.leftStack.items)

    def enqueue(self, x):
        self.leftStack.push(x)
        self._size += 1

    def dequeue(self):
        if not self.rightStack.isEmpty():
            self._size -= 1
            return self.rightStack.pop()
        else:
            while not self.leftStack.isEmpty():
                self.rightStack.push(self.leftStack.pop())
            self._size -= 1
            return self.rightStack.pop()

    def isEmpty(self):
        return self.leftStack.isEmpty() and self.rightStack.isEmpty()

    def peek(self):
        if not self.rightStack.isEmpty():
            return self.rightStack.peek()
        while not self.leftStack.isEmpty():
            self.rightStack.push(self.leftStack.pop())
        return self.rightStack.peek()

    def view(self):
        return self.leftStack.view() + self.rightStack.view()[::-1]

    def size(self):
        return self._size

test_q = Queue()
test_q.enqueue(1)
test_q.enqueue(2)
test_q.enqueue(3)
print(test_q)
print('Peek:', test_q.peek())
print('Достаю элемент из очереди: ',test_q.dequeue())
print('Достаю элемент из очереди: ',test_q.dequeue())
print('Достаю элемент из очереди: ',test_q.dequeue())

'''2. Написать функцию для проверки корректности скобок с использованием очереди 
(по аналогии с тем что делали со стеком на лабах).'''

print('\nЗадание 2. Функция для проверки корректности скобок с использованием очереди ')
def is_valid(s: str) -> bool:
    matching = {')': '(', ']': '[', '}': '{'}
    queue = Queue()

    for ch in s:
        if ch in '([{':
            queue.enqueue(ch)
        else:
            if queue.isEmpty() or queue.dequeue() != matching[ch]:
                return False

    return queue.isEmpty()

# Тесты
tests = ["((()))", ")(", "([]){}"]
for t in tests:
    print(f"{t!r:>12} -> {is_valid(t)}")
print("При "'([]){}'" выводится False, хотя должно быть True. Алгоритм работает только для плоских последовательностей без вложений.")
print("Для проверки корректности скобок лучше всего подходит стек (LIFO), "
      "так как открывающая скобка должна быть закрыта последней. "
      "Использование очереди (FIFO) не подходит для вложенных структур, "
      "так как она нарушает порядок сопоставления.")

'''3. Решить 3 задачи из списка LeetCode на выбор.'''
print('\nЗадание 3. LeetCode')
print('LeetCode 933. Number of Recent Calls')

'''
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:
RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]
'''

class RecentCounter:
    def __init__(self):
        self.q = Queue()
    def ping(self, t: int) -> int:
        self.q.enqueue(t)
        while not self.q.isEmpty() and self.q.peek() < t - 3000:
            self.q.dequeue()

        return self.q.size()

# Тест
rc = RecentCounter()
print(rc.ping(1))
print(rc.ping(100))
print(rc.ping(3001))
print(rc.ping(3002))

print('\nLeetCode 102. Binary Tree Level Order Traversal')

'''
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Строит бинарное дерево из списка значений."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = Queue()
    queue.enqueue(root)
    i = 1
    while not queue.isEmpty() and i < len(values):
        node = queue.dequeue()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.enqueue(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.enqueue(node.right)
        i += 1
    return root

class BTLOT:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = Queue()
        queue.enqueue(root)

        while not queue.isEmpty():
            level_size = queue.size()  # количество узлов на текущем уровне
            cur_level = []

            for _ in range(level_size):
                node = queue.dequeue()
                cur_level.append(node.val)
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)

            res.append(cur_level)

        return res

bt = BTLOT()
tree_root = build_tree_from_list([3, 9, 20, None, None, 15, 7])
result = bt.levelOrder(tree_root)
print(result)

print('\nLeetCode 622. Design Circular Queue')

'''
Implement the MyCircularQueue class:
MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.

Input:
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output:
[null, true, true, true, false, 3, true, true, true, 4]
'''

class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size

# Пример
cq = MyCircularQueue(3)
print('enQueue(1): ', cq.enQueue(1))
print('enQueue(2): ', cq.enQueue(2))
print('enQueue(3): ', cq.enQueue(3))
print('enQueue(4): ', cq.enQueue(4))
print('Rear(): ', cq.Rear())
print('isFull(): ', cq.isFull())
print('deQueue(): ', cq.deQueue())
print('enQueue(4): ', cq.enQueue(4))
print('Rear(): ', cq.Rear())

'''4. Реализовать систему обработки заказов в ресторане (с приоритетами).'''
print('\nЗадание 4. Реализовать систему обработки заказов в ресторане (с приоритетами).')

# Класс приоритетной очереди
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self._counter = 0

    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (-priority, self._counter, item))
        self._counter += 1

    def dequeue(self):
        if not self.heap:
            raise IndexError("Очередь пуста")
        return heapq.heappop(self.heap)[2]

    def is_empty(self):
        return len(self.heap) == 0

class Order:
    def __init__(self, dish, table, priority):
        self.dish = dish
        self.table = table
        self.priority = priority

    def __repr__(self):
        return f"Order({self.dish!r}, table={self.table}, priority={self.priority})"

# Система обработки заказов
class RestaurantOrderSystem:
    PRIORITY_VIP = 3
    PRIORITY_HIGH = 2
    PRIORITY_NORMAL = 1

    def __init__(self):
        self.queue = PriorityQueue()

    def add_order(self, order):
        self.queue.enqueue(order, order.priority)
        print(f"Добавлен заказ: {order.dish} (стол {order.table}, приоритет {order.priority})")

    def process_next_order(self):
        if self.queue.is_empty():
            print("Нет заказов для обработки.")
            return
        order = self.queue.dequeue()
        print(f"Обрабатывается заказ: {order.dish} для стола {order.table} (приоритет {order.priority})")

    def pending_orders_count(self):
        return len(self.queue.heap)

# Тест
system = RestaurantOrderSystem()

orders = [
    Order("Суп", 5, RestaurantOrderSystem.PRIORITY_NORMAL),
    Order("Стейк", 2, RestaurantOrderSystem.PRIORITY_VIP),
    Order("Паста", 1, RestaurantOrderSystem.PRIORITY_HIGH),
    Order("Десерт", 7, RestaurantOrderSystem.PRIORITY_NORMAL),
    Order("Пицца", 3, RestaurantOrderSystem.PRIORITY_VIP)
]

for order in orders:
    system.add_order(order)

print(f"\nВсего заказов в очереди: {system.pending_orders_count()}\n")

while not system.queue.is_empty():
    system.process_next_order()