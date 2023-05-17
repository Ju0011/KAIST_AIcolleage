import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# mat plot lib - 이 라이브러리는 matlab에서 그림 그리는 기능 일부를 파이썬으로 구현한 것으로 시작

'''
# line
# basic example
# arange linspace
x = np.linspace(0,20,800) #시작점 부터 끝점까지 800개 점을 반환
print(x)
y = np.sin(x) #broadcasting: 싸인 함수가 x배열에 원소별로 적용되서 y반환

plt.plot(x,y)
plt.plot(x,y+1)
plt.plot(x,y+2)
plt.show()
'''



# bar
# happiness score
# color South Korea differently
df = pd.read_csv('5.16/data/world_happiness_scores.csv')
df_sorted = df.sort_values(by="Ladder score", ascending=False)
num_countries = df.sort_values["Ladder score"].count()
print(num_countries)


# stacked bar
# loan_prediction
# applicant income and coapplicant income


# scatter
# admission
# GRE and TOEFL


# 3D interactive
# health
# age glucose bmi then color with heart_disease


# subplots


# legends


# labels


# ticks