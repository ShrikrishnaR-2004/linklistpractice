class ListNode:
    def __init__(self, data ):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def push(self,data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode

    def isPalindrome(self, head):
        if self.head or self.head.next:
            return True
        else:
            slow=self.head
            fast=self.head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            prev=None
            while slow:
                temp=slow.next
                slow.next=prev
                prev=slow
                slow=temp
            while prev:
                if prev.data!=head.data:
                    return False
                prev=prev.next
                head=head.next
            return True

new=Solution()

no_nodes=int(input("No of Nodes:"))
for i in range(no_nodes):
    new.push(int(input()))
if new.isPalindrome(new.head):
    print("Yes")
else:
    print("No")
