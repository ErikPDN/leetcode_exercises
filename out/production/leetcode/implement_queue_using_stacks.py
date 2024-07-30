class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop()
    
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2[-1]
    
    def empty(self):
        return max(len(self.s1), len(self.s2)) == 0
    


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())