import elice_utils

from time import sleep
def merge(input_filenames, output_file):
    # 출력 파일을 쓰기 모드로 열어둡니다.
    with open(output_file, 'w') as out_file:
        # 입력 파일을 순회하며 내용을 출력 파일에 복사합니다.
        for file_name in input_filenames:
            with open(file_name, 'r') as in_file:
                out_file.write(in_file.read())
    pass

merge(['kaist1.txt', 'kaist2.txt', 'kaist3.txt'], 'output.txt')
#merge(['kaist1.txt', 'kaist2.txt', 'kaist3.txt'], './outputs/output.txt') #경로 지정해주면 경로에 결과물 만들어줌
sleep(0.5) # Wait 0.5 seconds before creating a download link.
elice_utils.send_file('output.txt')