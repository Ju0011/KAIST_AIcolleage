from elice_utils import EliceUtils
import pandas as pd
import numpy as np

elice_utils = EliceUtils()

#우리나라의 행복지수(Ladder score) 순위 구하기

def main():
    df = pd.read_csv('data/world_happiness_scores.csv')
    print(df.head())
    print(df.columns)

    df_sorted = df.sort_values(by="Ladder score", ascending=False, ignore_index=True)
    #sort_values 함수 인자로 ignore_index = True로 두면,
    #원래 있던 index 무시한 채로 0번부터 매겨 내려감(칼럼 추가 안함)
    print(df_sorted)


    '''
    df_sorted = df.reset_index(inplace=True)
    #칼럼 추가해서 0번부터 매겨 내려감
    #칼럼 추가 안하고 싶으면 drop인자를 True로 주자
    print(df_sorted)

    rank = df.loc[df["Country name"] == "South Korea"]
    print(rank)
    '''

    ## numpy 식
    sk_rank = np.where(df_sorted["Country name"] == "South Korea")[0][0] + 1
    print(sk_rank)

    ## pandas 식
    sk_rank = df_sorted.index[df_sorted["Country name"]== "South Korea"].tolist()
    print(sk_rank[0]+1)

    print('Ranking of South Korea:', sk_rank)
    return sk_rank

if __name__ == "__main__":
    main()