from elice_utils import EliceUtils
import pandas as pd

elice_utils = EliceUtils()

def make_variables(df):
    df['PER'] = df["price"] / df["Earnings Per Share"]
    df['book_value_per_share'] = (df["Total Assets"] - df["Total Liabilities"]) / df["Estimated Shares Outstanding"]
    df['PBR'] = df["price"] / df["book_value_per_share"]

    return df

def main():
    df = pd.read_csv('data/S&P500.csv')
    #PER은 price/earings per share
    df["PER"] = df["price"]/df["Earnings Per Share"]
    print(df.loc[0,["price", "Earnings Per Share", "PER"]])

    # PBR은 price/book value per share
    df["PBR"] = df["price"] / ((df["Earnings Per Share"] - df["Total Liabilities"])/df["Estimated Shares Outstanding"])
    print(df.loc[0, ["price", "Total Assets","Total Liabilities","Estimated Shares Outstanding","PBR"]])

    df = make_variables(df)

if __name__ == "__main__":
    main()
