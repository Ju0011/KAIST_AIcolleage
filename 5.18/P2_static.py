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

    def pop(self,index):
        if self.is_empty():
            print("Q가 비어있음")
            return
        return self.arr.pop(index)

'''
import collections
queue = collections.deque()
queue.insert(0,'서울')
queue.insert(0,'인천')
queue.insert(0,'대구')
queue.insert(0,'부산')

print(queue)

print(queue.pop())
print(queue)
'''



'''
1번 왕자부터 n번 왕자까지 원탁에 앉아있는다. 1번 왕자부터 시계방향으로 돌아가며 1부터 시작하여 번호를 외치게 한다.
한 왕자가 k(특정숫자)를 외치면 그 왕자는 공주를 구하러 가는데서 제외되고 원 밖으로 나오게 된다.
그리고 다음 왕자부터 다시 1부터 시작하여 번호를 외친다.
'''

N = 20
K = 7

def findLast(N,K):
    '''마지막 왕자를 찾아라'''
    princeQ = Queue()
    for i in range(N):
        princeQ.enqueue(str(i+1))

    #pseudo Code
    count = 1   #몇을 외치고 있는지
    point = 0   #

    while(not princeQ.is_empty()):
        if count % K == 0 and point != 0:
            last = princeQ.pop(point)
            count -= K
            point -= 1

        if point == N:
            point = point -N

        count += 1
        point += 1

    print(princeQ.arr)
    return

findLast(N,K)