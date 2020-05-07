class Stack:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push(self, val):
        self.elems.append(val)

    def destack(self):
        if self.is_empty():
            raise Exception("pop from empty stack")
        return self.elems.pop()

    def travel(self):
        for elem in self.elems:
            print(elem, end=' ')
        print()

    def top(self):
        """
        查看栈顶元素
        :return:
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.elems[-1]


if __name__ == '__main__':
    s = Stack()
    s.push(100)
    s.push(200)
    s.push(300)
    print(s.top())
    s.travel()
    while not s.is_empty():
        print(s.destack())
