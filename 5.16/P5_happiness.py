from elice_utils import EliceUtils
import pandas as pd

elice_utils = EliceUtils()

#우리나라의 행복지수(Ladder score) 순위 구하기

def main():
    df = pd.read_csv('data/world_happiness_scores.csv')
    rank = 0

    print('Ranking of South Korea:', rank)
    return rank


if __name__ == "__main__":
    main()