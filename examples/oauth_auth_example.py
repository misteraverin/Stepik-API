# Run with Python 3
import requests
from requests.auth import HTTPBasicAuth

# 1. Get your keys at https://stepic.org/oauth2/applications/
# (client type = confidential, authorization grant type = client credentials)
client_id = "..."
client_secret = "..."

# 2. Get a token
resp = requests.post('https://stepic.org/oauth2/token/',
                     data={'grant_type': 'client_credentials'},
                     auth=HTTPBasicAuth(client_id, client_secret))
token = resp.json().get('access_token', None)
if not token:
    print('Unable to authorize with provided credentials')
    exit(1)

# 3. Call API (https://stepic.org/api/docs/) using this token.
api_url = 'https://stepic.org/api/courses/67'
course = requests.get(api_url,
                      headers={'Authorization': 'Bearer ' + token}).json()
print(course)
