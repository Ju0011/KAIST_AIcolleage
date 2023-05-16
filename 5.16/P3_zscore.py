from elice_utils import EliceUtils
import pandas as pd

elice_utils = EliceUtils()

'''
Bank Balance 변수를 z-score로 변환해주세요. 
변환된 값은 z_score_balance의 이름을 갖는 column으로 원래의 dataframe에 추가해주시면 됩니다.'''

def main():
    df = pd.read_csv('data/defaults.csv')
    print(df.head())
    print(df.columns)
    print(df.describe())

    #z = (x-mu)/sigma
    df["z_score_balance"] = (df["Bank Balance"] - df["Bank Balance"].mean()) / df["Bank Balance"].std()
    print(df)
    return df


if __name__ == "__main__":
    main()