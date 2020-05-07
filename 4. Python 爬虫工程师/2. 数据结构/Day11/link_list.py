class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList:
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return self.head is None

    def length(self):
        """
        获取链表长度
        :return:
        """
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def add(self, value):
        """
        链表头部添加1个节点
        :param value:
        :return:
        """
        node = Node(value)
        # 1、把新添加的节点指针指向原来头节点
        node.next = self.head
        # 2、添加的节点设置为新的头
        self.head = node

    def travel(self):
        """
        遍历整个链表
        :return:
        """
        cur = self.head
        while cur:
            print(cur.value, end=" ")
            cur = cur.next
        # 因为上面是end=" ",所以此处打印一个换行
        print()

    def append(self, value):
        """
        链表尾部添加1个节点,考虑空链表特殊情况
        :param value:
        :return:
        """
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            # 循环结束后,current指向尾节点
            cur.next = node
            node.next = None

    def search(self, value):
        """
        查看在链表中是否存在
        :param value:
        :return:
        """
        cur = self.head
        while cur:
            if cur.value == value:
                return True
            else:
                cur = cur.next
        return False

    def insert(self, pos, item):
        """
        在指定索引添加一个节点,索引值从0开始
        :param pos:
        :param item:
        :return:
        """
        if pos < 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next

            # 循环结束后,pos指向(pos-1)位置
            node = Node(item)
            node.next = pre.next
            pre.next = node


if __name__ == '__main__':
    s = SingleLinkList()
    s.add(300)
    s.add(200)
    s.add(100)
    print(s.is_empty())
    s.travel()
    s.append(400)
    print(s.length())
    s.travel()
    print(s.search(300))
    print(s.search(666))
