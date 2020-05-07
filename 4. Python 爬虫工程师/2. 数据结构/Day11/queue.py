# 队列的操作有入队，出队，判断队列的空满等操作
"""
思路分析:
1. 基于列表完成数据的存储
2. 通过封装功能完成队列的基本行为
3. 无论那边做对头/队尾 都会在操作中有内存移动
"""


# 队列操作
class SQueue:
    def __init__(self):
        self.elems = []

    # 判断队列是否为空
    def is_empty(self):
        return self.elems == []

    # 入队
    def enqueue(self, val):
        self.elems.append(val)

    # 出队
    def dequeue(self):
        if not self.elems:
            raise Exception("Queue is empty")
        return self.elems.pop(0)  # 弹出第一个数据


if __name__ == '__main__':
    sq = SQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    while not sq.is_empty():
        print(sq.dequeue())
