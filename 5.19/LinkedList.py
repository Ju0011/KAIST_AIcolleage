class Node:
    def __init__(self, item):  # 노드 생성자
        self.data = item
        self.next = None

class SimpleList:
    def __init__(self):  # 단순연결리스트 생성자
        self.head = None
        self.size = 0

    def size(self):
        #list크기를 알려주는
        return self.size

    def is_empty(self):
        #비어있는지 확인
        return self.size  == 0

    def insert_front(self, item):  # 첫 노드로 삽입
        if self.is_empty():
            new_node = Node(item)
            self.head = new_node
        else:
            new_node = Node(item)   #새 노드
            prev_head = self.head   #원래 헤드 저장
            self.head = new_node    #헤드 변경
            new_node.next = prev_head   #new_node -> prev_node
        
        self.size += 1  #리스트 길이 연장

    def insert_after(self, item, p):  # p 다음에 삽입
        new_node = Node(item)
        new_node.next = p.next
        p.next = new_node

        self.size += 1

    def delete_front(self):  # 첫 노드 삭제
        if self.is_empty:
            print("삭제실패 : 리스트가 비어있습니다.")
            return

        self.head = self.head.next
        self.size -= 1

    def delete_after(self, p):  # p 다음 노드 삭제
        if self.is_empty():
            print("삭제 실패 : 리스트가 비어있습니다.")
            return

        if p.next is None:
            print("삭제 실패 : 다음 노드가 없습니다.")
            return

        next.node = p.next
        p.next = p.next.next

    def search(self, target):  # target 탐색
        #target이라는 값을 가진 node가 몇번째에 있는지
        cur = self.head

        #for 문
        for i in range(self.size):
            if cur.data == target:
                return i
            cur = cur.next

        #while 문
        i = 0
        while cur is not None:
            if cur.data == target:
                return i
            cur = cur.next
            i += 1

        print("찾는 값이 리스트에 없음")
        return None
    def print_list(self):  # 연결리스트 출력
        if self.size == 0:
            print("리스트가 비어있습니다.")

        cur = self.head
        print("Printing List : ")
        while cur is not None:
            print(cur.data)
            cur = cur.next

class EmptyError(Exception):  # underflow 시 에러 처리
    pass

