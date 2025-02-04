class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_list(head, k):
    if not head or not head.next or k == 0:
        return head

    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    k = k % length
    if k == 0:
        return head

    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head

def insert(head, val):
    if not head:
        return ListNode(val)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = ListNode(val)
    return head

def print_list(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("NULL")

head = None

head = insert(head, 1)
head = insert(head, 2)
head = insert(head, 3)
head = insert(head, 4)
head = insert(head, 5)

print("Original List:")
print_list(head)

N = 2
head = rotate_list(head, N)

print(f"List after rotating by {N} positions:")
print_list(head)
