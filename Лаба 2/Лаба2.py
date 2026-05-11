class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    """Создать список из массива: build_list([1,2,3]) → 1→2→3→None"""
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_list(head):
    """Напечатать список"""
    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next
    print(" → ".join(parts) + " → None")

def list_to_array(head):
    """Список → массив (для проверки)"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def insert_sorted(head, val):
    new_node = ListNode(val)

    if head is None or val < head.val:
        new_node.next = head
        return new_node

    current = head
    while current.next is not None and current.next.val < val:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head

# Тест
head = build_list([1, 3, 5, 7])
head = insert_sorted(head, 4)
print_list(head)  # 1 → 3 → 4 → 5 → 7 → None

head = insert_sorted(None, 10)
print_list(head)  # 10 → None

head = build_list([5, 10])
head = insert_sorted(head, 1)
print_list(head)  # 1 → 5 → 10 → None

def second_to_last(head):
    if not head or not head.next:
        return None

    cur = head
    while cur.next.next:
        cur = cur.next

    return cur.val

# Тест
print(second_to_last(build_list([5, 10, 15, 20])))  # 15
print(second_to_last(build_list([42])))   # None

def swap_pairs(head):
    cur = head
    while cur and cur.next:
        # Меняем значения
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next
    return head

# Тест
head = build_list([1, 2, 3, 4, 5])
head = swap_pairs(head)
print_list(head)  # 2 → 1 → 4 → 3 → 5 → None

def delete_duplicates(head):
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

# Тест
head = build_list([1, 1, 2, 3, 3, 3, 4])
head = delete_duplicates(head)
print_list(head)  # 1 → 2 → 3 → 4 → None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, val):
        new_node = ListNode(val)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return val

    def peek(self):
        return self.head.val if self.head else None

    def is_empty(self):
        return self.size == 0

# Тест
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.peek())     # 2
print(q.dequeue())  # 2
print(q.dequeue())  # 3
print(q.is_empty()) # True