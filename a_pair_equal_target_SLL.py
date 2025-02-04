class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class solution:
    def __init__(self):
        self.head=None
    def insert(self, data):
        new = Node(data)
        new.next=self.head
        self.head=new

    def paireqaultotar(self,target):
        prev=self.head
        count=0
        if self.head is None:
            return

        while prev.next:
            front=prev.next
            while front:
                if prev.data+front.data==target:
                    count+=1
                    print(prev.data,front.data)
                front=front.next
            prev=prev.next
        if count:
            print("Yes")
            print(count)
        else:
            print("No")
new=solution()

no_nodes=int(input("No of Nodes:"))
for i in range(no_nodes):
    new.insert(int(input()))
tar=int(input("Target:"))
new.paireqaultotar(tar)