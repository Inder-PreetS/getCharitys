import requests
import base64
import time


access_token = None
expiry_time = None

def get_access_token(client_id, client_secret):
    global access_token
    global expiry_time
    
    if access_token and expiry_time and expiry_time > time.time():
        print("Using cached access token")
        return access_token
    
    try:
        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        url = 'https://api.ebay.com/identity/v1/oauth2/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {encoded_credentials}'
        }

        payload = {
            'grant_type': 'client_credentials',
            'scope': 'https://api.ebay.com/oauth/api_scope'
        }

        response = requests.post(url, headers=headers, data=payload)

        response.raise_for_status()

        response_data = response.json()
        access_token = response_data['access_token']
        expires_in = response_data['expires_in']

        expiry_time = time.time() + expires_in

        print("New access token obtained")
        return access_token
    except requests.RequestException as e:
        print("Failed to obtain access token:", e)
        raise
    except KeyError as e:
        print("Error parsing response JSON:", e)
        raise
    except Exception as e:
        print("An unexpected error occurred:", e)
        raise
