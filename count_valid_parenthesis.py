class Stacks:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def is_empty(self):
        return not self.stack

    def valid_parenthesis(self, data):
        stack = []
        matching_parentheses = {"]": "[", ")": "(", "}": "{"}
        count=0
        for char in data:
            if char in "({[":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    continue
                top_element = stack[-1]
                if matching_parentheses[char] == top_element:
                    count += 1
                stack.pop()
            else:
                pass

        return count

stack = Stacks()
data = input()
print(stack.valid_parenthesis(data))