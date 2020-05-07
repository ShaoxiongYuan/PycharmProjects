class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        """判断是否为空栈"""
        if self.top:
            return False
        return True

    def push(self, val):
        """入栈: 相当于在链表头部添加节点"""
        node = Node(val)
        node.next = self.top
        self.top = node

    def pop(self):
        """出栈: 相当于删除头节点"""
        if self.is_empty():
            raise Exception('pop from empty stack')

        val = self.top.value
        self.top = self.top.next
        return val

    def stack_top(self):
        """查看栈顶元素: 查看头节点"""
        if self.is_empty():
            return None
        return self.top.value

    def size(self):
        """查看栈的大小"""
        if self.is_empty():
            return 0
        count = 0
        current = self.top
        while current:
            current = current.next
            count += 1
        return count


if __name__ == '__main__':
    s = LinkStack()
    s.push(100)
    s.push(200)
    s.push(300)
    print(s.pop())
    print(s.stack_top())
    print(s.size())
