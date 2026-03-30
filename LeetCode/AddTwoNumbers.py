'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

from typing import Optional

class ListNode: # класс был дан в условии задачи
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def __str__(self): # красивый вывод
        res = []
        cur = self
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return ' -> '.join(res) + ' -> None'

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0) # создаём дамми и указатель на него
    curr = dummy
    perenos = 0

    while l1 or l2 or perenos:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + perenos

        perenos = total // 10 # перенос - часть числа, которую нужно добавить к сумме (перенос остатков)
        last_digit = total % 10

        curr.next = ListNode(last_digit) # создаём узел в конце списка
        curr = curr.next # переставляем указатель на него

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print(l1)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(l2)

print(addTwoNumbers(l1, l2))
