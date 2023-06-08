import requests

url = "https://en.wikipedia.org/wiki/File:Google_2015_logo.svg"
response = requests.get(url)

name = 'im1.svg'
size = 0

with open(name, "wb") as file:   # open in binary mode
    size += file.write(response.content)      # write to file

print(size)