class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def get_array_list(self, node):
        array_list = []
        while node:
            array_list.append(node.value)
            node = node.next

        array_list.reverse()
        return array_list


if __name__ == '__main__':
    s = Solution()
    # 链表(表头->表尾): 100 200 300
    n1 = Node(100)
    n1.next = Node(200)
    n1.next.next = Node(300)
    # 调用反转方法: [300, 200, 100]
    array_list = s.get_array_list(n1)
    print(array_list)
