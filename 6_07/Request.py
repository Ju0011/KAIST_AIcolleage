import requests

response = requests.get("https://google.com")

print(response.status_code) #200이 떠야 성공

print(response.text)