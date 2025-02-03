class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to rotate the linked list by N positions
def rotate_list(head, k):
    if not head or not head.next or k == 0:
        return head  # No rotation needed

    # Step 1: Find length and last node
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Handle cases where k is greater than the length
    k = k % length
    if k == 0:
        return head  # No rotation needed

    # Step 3: Find the new tail (length - k - 1)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    # Step 4: Re-arrange pointers
    new_head = new_tail.next
    new_tail.next = None  # Break the connection
    tail.next = head  # Connect last node to old head

    return new_head

# Function to insert a new node at the end of the linked list
def insert(head, val):
    if not head:
        return ListNode(val)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = ListNode(val)
    return head

# Function to print the linked list
def print_list(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("NULL")

# Driver code
head = None

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = insert(head, 1)
head = insert(head, 2)
head = insert(head, 3)
head = insert(head, 4)
head = insert(head, 5)

print("Original List:")
print_list(head)

# Rotate by N positions
N = 2
head = rotate_list(head, N)

print(f"List after rotating by {N} positions:")
print_list(head)
