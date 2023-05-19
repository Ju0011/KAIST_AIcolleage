class Node:
    def __init__(self, item ):  # 노드 생성자
        self.item = item
        self.next = None

class CList:
    def __init__(self):  # 환형연결리스트 생성자
        self.head = None
        self.tail = None    # CList의 마지막 노드
        self.size = 0  # 항목 수

    def no_items(self):  return self.size

    def is_empty(self):  return self.size == 0

    def insert(self, item):
        #노드를 맨 뒤에 넣기
        if self.is_empty():
            new_node = Node(item)
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node

        else:
            new_node = Node(item)   #새로운 노드 생성
            prev_tail = self.tail   #이전 꼬리
            prev_tail.next = new_node   #이전 꼬리의 다음으로 새로운 노드 연결
            self.tail = new_node    #새로운 꼬리 = 새로운 노드
            new_node.next = self.head   #새로운 노드가 다시 head를 가르키도록!(순환)

    def first(self):  # 첫 노드 접근
        pass

    def delete(self):  # 첫 노드 삭제

        if self.is_empty():
            print("삭제 실패 : 리스트가 비어있습니다.")
            return

        #길이가 1인 리스트인 경우
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return

        new_head = self.head.next #두번째 노드 -> 새로운 헤드
        self.head = new_head
        self.tail.next = new_head
        self.size -= 1

    def print_list(self):  # 연결리스트 출력
        pass


class EmptyError(Exception):  # underflow 시 에러 처리
    pass