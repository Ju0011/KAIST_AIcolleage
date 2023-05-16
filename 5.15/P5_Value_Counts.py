from elice_utils import EliceUtils
import pandas as pd

elice_utils = EliceUtils()

'''
입학 확률을 예측할 때 쓰이는 데이터셋을 활용하여 데이터프레임에서 value count를 해보겠습니다.

CGPA의 사분위수 중 3/4분위값을 넘는 값들을 가진 행들의 Research 값이 각각 몇개가 있는지를 표시해주세요.
'''

df = pd.read_csv("./data/admission.csv")

##quantile 써서 풀기 --->제일 좋은 방법
#입학관련 데이터
#성적(CGPA)이 높은 사람들은 연구(Reasearch)경험이 있을까
#성적 상위 25% 중 연구 경험이 있는/없는 사람은 얼마나 될까?
'''
#강사님 방법
cgpa75 = df["CGPA"].quantile(0.75) #성적 상위 25%(0.75) 커트라인 계산
print(df.CGPA)
cgpa75_research = df.loc[df["CGPA"] > cgpa75, "Research"] #커트라인 위인 사람들의 데이터 중 Research 열(칼럽) 값 추출
print(cgpa75_research.value_counts()) #추출된 Research의 칼럼 중 1과 0의 등장 횟수 각각 계산
'''

def main():
    # 1. data 폴더 안 admission.csv 파일을 데이터프레임으로 읽어주세요
    # 2. CGPA 변수의 3/4 분위수를 구해주세요. 3/4 분위수는 75% 값을 말합니다.
    # 3. CGPA 변수의 3/4 분위수를 넘는 값을 가지는 행들에 들어 있는 Research의 값은 0, 1입니다. 0의 갯수와 1의 갯수를 프린트해주세요.

    r_zero, r_one = (df.loc[df["CGPA"] > df["CGPA"].quantile(0.75), "Research"].value_counts().loc[[0,1]].tolist())
    #가장 바깥에서는 리스트를 언패킹하고 있음
    #tolist는 series를 list로 바꿈
    #df.loc으로 어떤 행을 볼건지 조건
    #df.loc으로 어떤 열을 볼건지 조건
    #그렇게 추출된 부분 dataframe에서 ununiq한 값을 count
    #value_counts()의 결과물(Series)의 어떤 행들을 볼건지 정해줌[0,1]
    #그렇게 추출된 데이터를 리스트로 바꾸고 언패킹함
    print('Number of occurrences of 0 in Research column:', r_zero)
    print('Number of occurrences of 1 in Research column:', r_one)


if __name__ == "__main__":
    main()