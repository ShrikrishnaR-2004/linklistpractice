class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

class Solution:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new= Node(data)
        new.next=self.head
        self.head=new

    def sumofdigits(self):
        if self.head is None:
            print("SLL is empty")
            return
        cur=self.head
        while cur:
            if cur.data<9:
                print(cur.data,end='->')
            elif cur.data==9:
                print(cur.data,end='->')
            else:
                print(cur.data%9,end='->')
            cur=cur.next
        print("None")

new=Solution()
no_nodes=int(input("No of nodes"))
for i in range(no_nodes):
    new.insert(int(input()))
new.sumofdigits()