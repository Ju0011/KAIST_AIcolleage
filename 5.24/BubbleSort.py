unsorted = [14,3,7,29,44,32,24,32]
N = len(unsorted)
print("정렬 전 : ", unsorted)

for i in range(N-1, 0,-1):
    for j in range(i):
        if unsorted[j] > unsorted[j+1]:
            unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

print("정렬 후 : ", unsorted)