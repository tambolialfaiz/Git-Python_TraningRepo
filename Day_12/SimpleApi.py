# This is simple get API call to show the Status code.

import requests
response = requests.get("https://24pullrequests.com/users/andrew.json")
print(response)
