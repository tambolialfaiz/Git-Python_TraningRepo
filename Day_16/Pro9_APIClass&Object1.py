#Nyno ugle

import requests

class API:
    gitHubLink = 'https://api.github.com/events'

    def __init__(self):
        self.headers = {'User-Agent': 'GitHubEventsAPI'}

    def GetData(self, event_type=None):
        params = {'type': event_type} if event_type else None
        response = requests.get(self.gitHubLink, headers=self.headers, params=params)
        events = response.json()
        return [(event['type'], event['actor']['login'], event['repo']['name'],event['repo']['url']) for event in events]

api = API()
events = api.GetData(event_type='PushEvent')
for event in events:
    print(f"Type: {event[0]}\nLogin: {event[1]}\nname: {event[2]}\nURL:{event[3]}\n")
