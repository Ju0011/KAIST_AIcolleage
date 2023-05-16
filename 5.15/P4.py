from elice_utils import EliceUtils
import pandas as pd

elice_utils = EliceUtils()

#최댓값과 그 위치 구하기

def get_max(df):
    max_index = df["residual sugar"].index() #최대값의 위치
    max_val, density_val = df.loc[max_index, ["residual sugar", "density"]]

    density_at = 0

    return max_val, density_at

def get_stats_pd(df):
    selected = df.loc[(df['hypertension']==1)&(df['heart_disease'] == 1), ['age']]
    mean_val = float(selected.mean(axis=0))
    std_val = float(selected.std(axis=0))

    return mean_val, std_val
def main():
    df = pd.read_csv('data/wine.csv')
    print(df.head())

    max_val, density_at = get_max(df)
    print('Max residual sugar:', max_val)
    print('Density value of maximal residual sugar:', density_at)


if __name__ == "__main__":
    main()