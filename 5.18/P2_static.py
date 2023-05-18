#정적인 버전

class Queue:
    def __init__(self, N=4):
        self.arr = []
        self.length = N

    def is_full(self):
        # 큐가 가득 차있는지 확인
        if self.length == len(self.arr):
            print("Q가 가득 차있습니다.")
            return True
        else:
            return False
    def is_empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False


    def enqueue(self, item):
        # q안에 item을 넣는다
        if self.is_full():
            return

        self.arr.append(item)

    def dequeue(self):
        #q에서 첫번째 item 제거한다 + 돌려준다
        if self.is_empty():
            print("Q가 비어있음")
            return

        return self.arr.pop(0)

    def top(self):
        #Q에서 첫번째 item 돌려준다/ 확인한다
        if self.is_empty():
            print("Q가 비어있음")
            return
        return self.arr[0]
    def tail(self):
        # Q에서 마지막 item 돌려준다/ 확인한다
        if self.is_empty():
            print("Q가 비어있음")
            return
        return self.arr[-1]

queue = Queue(4)
print(queue.is_empty())