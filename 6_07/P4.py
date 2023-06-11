#request 모듈 사용
import requests

def download(url, file_name):
    size = 0
    with open(file_name, "wb") as file:   # open in binary mode
        response = requests.get(url)               # get request
        size += file.write(response.content)      # write to file
    return size


url = "https://en.wikipedia.org/wiki/File:Google_2015_logo.svg"
size = download(url,"iml.svg")
print(size)