import pandas as pd

def rename_columns(dataframe):
    dataframe = dataframe.rename(columns={
        'Unnamed: 0': 'id',
        'applicantincome': 'applicant_income',
        'coapplicantincome': 'coapplicant_income',
        'loanamount': 'loan_amount'
    })
    return dataframe

def main():
    df = pd.read_csv('data/loan_prediction.csv')
    df = rename_columns(df)
    print(df)

if __name__ == "__main__":
    main()