# Send all zero's' at end
# I/P:[12, 0, 5, 2, 0, 3, 12]
# O/P:[12, 5, 2, 3, 12, 0, 0]

def send_zeros_at_end(stack1):
    stack2=[]
    stack3=[]
    for i in range (0,len(stack1)):
        if stack1[i]!=0:
            stack2.append(stack1[i])
        else:
            stack3.append(stack1[i])

    stack2+=stack3

    return stack2

stack1=[int(x) for x in input().split()]
print(send_zeros_at_end(stack1))