class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_members(head):
    count = 0
    temp = head
    while temp:
        if is_prime(temp.val):
            count += 1
        temp = temp.next
    return count

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


head = insert(head, 10)
head = insert(head, 3)
head = insert(head, 5)
head = insert(head, 7)
head = insert(head, 12)
head = insert(head, 2)
head = insert(head, 16)

print("Linked List:")
print_list(head)

prime_count = count_prime_members(head)
print(f"Number of prime numbers in the linked list: {prime_count}")
