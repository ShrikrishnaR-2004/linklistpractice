class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to reverse a linked list
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

# Function to check if a linked list is a palindrome
def is_palindrome(head):
    if not head or not head.next:
        return True  # Single node or empty list is always a palindrome

    # Step 1: Find the middle (slow-fast pointer technique)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    second_half = reverse_list(slow)

    # Step 3: Compare first and second half
    first_half = head
    temp = second_half  # Save reference to restore the list later

    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    # Step 4: Optional - Restore the list to its original form
    reverse_list(temp)

    return True

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

# Create a palindrome linked list: 1 -> 2 -> 3 -> 2 -> 1
head = insert(head, 1)
head = insert(head, 2)
head = insert(head, 3)
head = insert(head, 2)
head = insert(head, 1)

print_list(head)

if is_palindrome(head):
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
