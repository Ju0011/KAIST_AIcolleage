from elice_utils import EliceUtils
import pandas as pd

elice_utils = EliceUtils()

'''
입학 확률을 예측할 때 쓰이는 데이터셋을 활용하여 데이터프레임에서 value count를 해보겠습니다.

CGPA의 사분위수 중 3/4분위값을 넘는 값들을 가진 행들의 Research 값이 각각 몇개가 있는지를 표시해주세요.
'''

df = pd.read_csv("./data/admission.csv")

##quantile 써서 풀기 --->제일 좋은 방법
'''입학관련 데이터
성적(CGPA)이 높은 사람들은 연구(Reasearch)경험이 있을까'''
cgpa75 = df["CGPA"].quantile(0.75)
print(df.CGPA)
cgpa75_research = df.loc[df["CGPA"] > cgpa75, "Research"]
print(cgpa75_research.value_counts())

def main():
    # 1. data 폴더 안 admission.csv 파일을 데이터프레임으로 읽어주세요

    # 2. CGPA 변수의 3/4 분위수를 구해주세요. 3/4 분위수는 75% 값을 말합니다.

    # 3. CGPA 변수의 3/4 분위수를 넘는 값을 가지는 행들에 들어 있는 Research의 값은 0, 1입니다. 0의 갯수와 1의 갯수를 프린트해주세요.

    r_zero = 0
    r_one = 0

    print('Number of occurrences of 0 in Research column:', r_zero)
    print('Number of occurrences of 1 in Research column:', r_one)


if __name__ == "__main__":
    main()