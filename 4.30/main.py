score = {"John": 89, "Jenny": 19, "Henry": 58, "Leia": 93, "Minsaku": 91, "Juho": 78, "Harry": 49, "Kim":67,"Gabriel": 37}

# 여기서부터 코딩해주시면 됩니다.

threshold = int(input())

sorted_scores = sorted(score.items(), key=lambda x: x[1], reverse=True)

for name, score in sorted_scores:
    if score > threshold:
        print(name)