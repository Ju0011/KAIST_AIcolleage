from elice_utils import EliceUtils

import pandas as pd

elice_utils = EliceUtils()

#1번
df = pd.read_csv('data/defaults.csv')
print(df.head())
print(df.columns)
print(df.describe())

#2번

def main():
    employed_bank_balance = 0
    non_employed_bank_balance = 0

    return (non_employed_bank_balance, employed_bank_balance)


if __name__ == "__main__":
    main()