import requests

class InternetArchiveMetadataAPI:
    BASE_URL = 'https://archive.org/metadata/TheAdventuresOfTomSawyer_201303'

    def __init__(self, identifier):
        self.identifier = identifier

    def get_metadata(self):
        url = f"{self.BASE_URL}{self.identifier}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data.get('title'), data.get('subject'))
        else:
            return None

api = InternetArchiveMetadataAPI('TheAdventuresOfTomSawyer_201303')
metadata = api.get_metadata()

if metadata:
    print(f"Name: {metadata[0]}")
    print(f"Subject: {metadata[1]}")
else:
    print("Metadata not found.")
