class stacks:
    def __init__(self,size):
        self.stack=[]
        self.size=size

    def push(self,data):
        if len(self.stack)<self.size:
            self.stack.append(data)
            return print(data,"is added to stack")
        else:
            return print("Stack Overflow")

    def pop(self):
        if len(self.stack)==0:
            return print("Stack Underflow")
        else:
            return print(self.stack.pop(),"is removed from stack")

    def get_size(self):
        return print(len(self.stack),"is the length of the stack")

    def isempty(self):
        return self.stack==[]

    def getstack(self):
        return print(self.stack[::-1])

ob=stacks(5)
a =int(input("Enter the size of the stack: "))
for i in range(a):
    ob.push(int(input()))
ob.getstack()
ob.pop()
ob.get_size()
ob.isempty()
ob.getstack()