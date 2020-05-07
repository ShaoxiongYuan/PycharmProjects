class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next

            cur.next = node
            node.next = None

    def dequeue(self):
        if self.is_empty():
            raise Exception('queue is empty')
        result = self.head.value
        self.head = self.head.next
        return result

    def top(self):
        if self.is_empty():
            raise Exception('queue is empty')
        return self.head.value

    def travel(self):
        if self.is_empty():
            return
        else:
            current = self.head
            while current is not None:
                print(current.value, end=" ")
                current = current.next
            print()


if __name__ == '__main__':
    q = Queue()
    # q:  100 200 300
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    # 出队列: 100
    print(q.dequeue())
    # 是否为空: False
    print(q.is_empty())
    # 队头元素: 200
    print(q.top())
    # 遍历: 200 300
    q.travel()
