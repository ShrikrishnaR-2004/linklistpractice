class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new=Node(data)
        new.next=self.head
        self.head=new

    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        self.head=self.head.next

    def isempty(self):
        return self.head is None

    def getstack(self):
        if self.head is None:
            print("Stack is empty")
            return
        cur=self.head
        while cur is not None:
            print(cur.data, end=" ")
            cur=cur.next

        print()

stack=stack()
a=int(input())
for i in range(a):
    stack.push(int(input()))
stack.getstack()
stack.pop()
stack.getstack()