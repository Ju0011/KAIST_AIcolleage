class DList:
    class Node:
        def __init__(self, item):  # 노드 생성자
            self.item = item
            self.prev = None
            self.next = None

    def __init__(self):  # 이중연결리스트 생성자
        self.head = None
        self.size = 0  # 항목 수

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_before(self, p, item):  # p 앞에 삽입

        new_node = self.Node(item)
        t = p.prev

        p.prev = new_node
        t.next = new_node
        new_node.prev = t
        new_node.next = p
        self.size += 1

    def insert_after(self, p, item):  # p 다음에 삽입
        if self.is_empty():
            new_node = self.Node(item)
            self.head = new_node
        else:
            new_node = self.Node(item)
            t = p.next

            p.next = new_node
            t.prev = new_node
            new_node.next = t
            new_node.prev = p

        self.size += 1

    # [미션] 인자로 주어지는 노드 x를 삭제하는 delete() 메소드를 작성하세요
    def delete(self, x):  # x가 참조하는 노드 삭제
        # x 앞뒤로 노드가 존재한다고 가정
        prev_node = x.prev
        next_node = x.next
        
        #delete 시에는 바꿔야하는 변수가 2가지이다
        # 1. prev_node가 next를 가르키도록
        prev_node.next = next_node

        # 2. next_node의 이전에 x가 아닌 prev_node
        next_node.prev = prev_node

        self.size -= 1
        return x.item

    
    def print_list(self):  # 리스트 출력
        if self.is_empty():
            print('리스트 비어있음')
        else:
            cur = self.head
            while cur is not None:
                print(cur.item)
                cur = cur.next


class EmptyError(Exception):  # underflow 시 에러 처리
    pass

# 채점 전 아래의 코드를 모두 주석 해제해 주세요.
# s = DList()

# s.insert_after(s.head,'apple')
# s.print_list()
# s.insert_before(s.tail, 'orange')
# s.print_list()
# s.insert_before(s.tail,'cherry')
# s.print_list()
# s.insert_after(s.head.next,'pear')
# s.print_list()

# print('마지막 노드 삭제 후:\t', end='')
# s.delete(s.tail.prev)
# s.print_list()