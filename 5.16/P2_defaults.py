from elice_utils import EliceUtils

import pandas as pd

elice_utils = EliceUtils()

'''
csv파일을 읽어온 후, 취업 상태인 사람들과 아닌 사람들의 Bank Balance의 차이 구하기
'''




def main():
    # 1번
    df = pd.read_csv('data/defaults.csv')

    # 2번
    employed_bank_balance = df.loc[df["Employed"] == 1, "Bank Balance"].mean()
    print(employed_bank_balance)

    # 3번
    non_employed_bank_balance = df.loc[df["Employed"] == 0, "Bank Balance"].mean()
    print(non_employed_bank_balance)

    # 4번
    employed_bank_balance, non_employed_bank_balance = df.loc[df["Employed"] == 1, "Bank Balance"].mean(), df.loc[
        df["Employed"] == 0, "Bank Balance"].mean()

    return (non_employed_bank_balance, employed_bank_balance)


if __name__ == "__main__":
    main()