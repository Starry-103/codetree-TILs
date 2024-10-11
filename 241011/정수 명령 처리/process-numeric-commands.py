class stack:
    def __init__(self):
        self.items=[]

    def push(self, A):
        self.items.append(A)

    def pop(self):
        

        print(self.items.pop())

    def size(self):
        print(len(self.items))

    def empty(self):
        print(0 if len(self.items) != 0 else 1)

    def top(self):
        print(self.items[-1])

n=int(input())
s=stack()
for _ in range(n):
    command = input()
    
    if command.startswith("push"):
        x = int(command.split()[1])
        s.push(x)
    elif command.startswith("pop"):
        s.pop()
    elif command == "size":
        s.size()
    elif command == "empty":
        s.empty()
    else:
        s.top()