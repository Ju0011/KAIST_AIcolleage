import pandas as pd

def get_stats(df):
    # Write your code here
    # hypertension 이 1이고 heart_disease가 1인 사람들의 평균 나이와 나이의 표준편차를 구해주세요
    mean_val = 0
    std_val = 0

    return mean_val, std_val


def main():
    df = pd.read_csv('data/health.csv')

    mean_val, std_val = get_stats(df)
    print('Mean age:', mean_val)
    print('Standard deviation of age:', std_val)

if __name__ == "__main__":
    main()