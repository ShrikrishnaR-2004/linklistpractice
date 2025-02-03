class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class list1:
    def __init__(self):
        self.head = None

    def insertatbeg(self, data):
        new = node(data)
        new.next = self.head
        self.head = new

    def insertatend(self, data):
        new = node(data)
        if self.head is None:
            self.head = new
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new
            new.next = None

    def insertatpos(self, pos, data):
        new = node(data)
        if pos == 0:
            self.head = new
        else:
            cur = self.head
            for _ in range(pos - 1):
                cur = cur.next
        new.next = cur.next
        cur.next = new

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end="->")
                cur = cur.next
            print("None")

    def search(self, data):
        if self.head is None:
            print("Linked List is empty")
        else:
            cur = self.head
            while cur is not None:
                if cur.data == data:
                    print("True")
                    return
                cur = cur.next
            print("False")

    # def find_midnode(self):
    #     count=0
    #     cur=self.head
    #     if self.head is None:
    #         print("Linked List is Empty")
    #     while cur is not None:
    #         cur=cur.next
    #         count+=1
    #     count //=2
    #     cur=self.head
    #     for _ in range(count):
    #         cur=cur.next
    #     print(cur.data)

    def findmid(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        else:
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print(slow.data)

    def reverse(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        else:
            cur = self.head
            prev = None
            while cur is not None:
                front = cur.next
                cur.next = prev
                prev = cur
                cur = front
            self.head = prev

    def printuptomid(self):
        if self.head is None:
            print("List is empty")
        else:
            slow = self.head
            fast = self.head
            cur = self.head
            while fast and fast.next:
                print(slow.data, end="->")
                slow = slow.next
                fast = fast.next.next
            # print(slow.data)

    def sortList(self):
        current = self.head
        index = None

        if (self.head == None):
            return
        else:
            while (current != None):
                index = current.next

                while (index != None):
                    if (current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

    def binarytoint(self):
        s=""
        cur=self.head
        while cur:
            s+=str(cur.data)
            cur=cur.next
        print(int(s,2))
    def inttobin(self):
        s=0
        cur=self.head
        while cur:
            s+=(cur.data)
            cur=cur.next
        print(bin(s)[2:])

    def removefirst(self):
        if self.head is None:
            print("Linked List is empty")
            return
        self.head = self.head.next

    def delatlast(self):
        if self.head is None or self.head.next is None:
            print("None")
            return
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None






new = list1()

no_node = int(input("Enter the numbers of node:"))
for _ in range(no_node):
    new.insertatend(int(input()))
new.display()
# new.insertatpos(3,100)
# new.display()
# new.search(100)
# new.findmid()
# new.printuptomid()
# new.sortList()
# new.display()
# new.binarytoint()
# new.inttobin()
# new.removefirst()
new.delatlast()
new.display()