# import requests
#
# class GitHubEventsAPI:
#     BASE_URL = 'https://api.github.com/events'
#
#     def __init__(self):
#         self.headers = {'User-Agent': 'GitHubEventsAPI'}
#
#     def get_events(self):
#         response = requests.get(self.BASE_URL, headers=self.headers)
#         return response.json()
#
# api = GitHubEventsAPI()
# events = api.get_events()
# print(events)
