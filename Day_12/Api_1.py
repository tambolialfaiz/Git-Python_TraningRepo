import requests

url = 'https://24pullrequests.com/users/andrew.json'
response = requests.get(url)
data = response.json()
nickname = data['nickname']
repo_name = data['pull_requests'][0]['repo_name']

print(f"Nickname: {nickname}")
print(f"Repo name: {repo_name}") 