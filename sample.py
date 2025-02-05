class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def traverse_middle_out(self):
        if not self.head:
            return []

        mid = self.find_middle()
        left_stack = []
        right_queue = []

        # Push left elements to stack
        temp = self.head
        while temp != mid:
            left_stack.append(temp)
            temp = temp.next

        # Add mid to queue
        right_queue.append(mid)
        temp = mid.next

        # Push right elements to queue
        while temp:
            right_queue.append(temp)
            temp = temp.next

        result = []
        while left_stack or right_queue:
            if right_queue:
                result.append(right_queue.pop(0))
            if left_stack:
                result.append(left_stack.pop())

        return result

    def print_result(self, nodes):
        for node in nodes:
            print(node.data, end="->")
        print("None")

# Taking dynamic input
ll = LinkedList()
elements = list(map(int, input("Enter linked list elements separated by space: ").split()))

for el in elements:
    ll.append(el)

output_nodes = ll.traverse_middle_out()
ll.print_result(output_nodes)