class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new=node(data)
        new.next=self.head
        self.head=new

    def perfectsquare(self):
        if self.head is None:
            print("SLL is empty")
            return
        curr=self.head
        while curr:
            sr=int(curr.data ** 0.5)
            if sr*sr == curr.data:
                print(curr.data,"is a Perfect Square")
            else:
                print(curr.data,"is a not Perfect Square")
            curr=curr.next
new=Solution()
no_nodes=int(input("No of nodes"))
for i in range(no_nodes):
    new.insert(int(input()))
new.perfectsquare()
