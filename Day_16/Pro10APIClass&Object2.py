# ALfaiz Tamboli

import requests

class API_2:
    APILink = 'https://24pullrequests.com/users/'

    def __init__(self, username):
        self.username = username

    def fatchData(self):
        url = f"{self.APILink}{self.username}.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['nickname'], data['pull_requests'][0]['repo_name'])
        else:
            return None

api = API_2('andrew')
user_info = api.fatchData()

if user_info:
    print(f"Nickname: {user_info[0]}")
    print(f"Repo Name: {user_info[1]}")
else:
    print("User not found.")
