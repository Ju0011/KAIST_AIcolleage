from elice_utils import EliceUtils
import pandas as pd

elice_utils = EliceUtils()

def make_variables(df):
    df['PER'] = 0
    df['PBR'] = 0

    return df

def main():
    df = pd.read_csv('data/S&P500.csv')
    df = make_variables(df)


if __name__ == "__main__":
    main()
