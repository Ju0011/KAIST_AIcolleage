# 입력값 설정
# N = input()
N = 2
sentences = ['I am happy today', 'We want to win the first prize']

# 알고리즘 풀이

# Solution 1 - indexing
for i in range(N):
    # input_string = input()
    input_string = sentences[i]

    # Code
    stack = []
    for c in input_string:
        if c == " ":
            while len(stack) != 0:
                print(stack.pop(), end='')
            print(' ', end='')

        else:
            stack.append(c)

    while len(stack) != 0:
        print(stack.pop(), end='')

    print(' ', end='')

    print()

# Solution 2 - Split
for i in range(N):
    input_string = sentences[i]

    # Code
    stack = []
    words = input_string.split()
    for word in words:
        for c in word:
            stack.append(c)

        while len(stack) != 0:
            print(stack.pop(), end='')
        print(' ', end='')

    print()

## Solution 3 - Without Stack Concept
for i in range(N):
    # input_string = input()
    input_string = sentences[i]

    # Code
    words = input_string.split()
    for word in words:
        print(''.join(reversed(word)),end=' ')
    print()


## Solution 4 -
for i in range(N):
    # input_string = input()
    input_string = sentences[i]

    # Code
    words = input_string.split()

    for word in words:
        print(word[::-1],end=' ')
    print()