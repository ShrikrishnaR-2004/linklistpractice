class node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertatbeg(self,data):
        new=node(data)
        new.next=self.head
        if self.head is not None:
            self.head.prev=new
        self.head=new

    def insertatend(self,data):
        new=node(data)
        if self.head is None:
            self.head=new
            self.tail=new
            return
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=new
        new.prev=cur
        self.tail=new



    def display(self):
        current = self.head
        print("None",end="<->")
        while(current):
            print(current.data,end="<->")
            current = current.next
        print("None")

new=DoubleLinkedList()
no_nodes=int(input("Enter the number of nodes: "))
for i in range(no_nodes):
    data=int(input())
    new.insertatend(data)
new.display()

