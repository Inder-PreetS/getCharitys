from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
import requests

def search_charity_orgs(query, limit=20):
    try:
        # Define your client credentials and OAuth scopes
        client_id = 'YOUR_CLIENT_ID'
        client_secret = 'YOUR_CLIENT_SECRET'
        scopes = ['https://api.ebay.com/oauth/api_scope']
        
        # Authenticate using the client credentials grant flow
        client = BackendApplicationClient(client_id=client_id)
        oauth = OAuth2Session(client=client)
        token_url = 'https://api.ebay.com/identity/v1/oauth2/token'
        token = oauth.fetch_token(token_url=token_url, auth=HTTPBasicAuth(client_id, client_secret), scope=scopes)
        
        # Specify the endpoint for searching charitable organizations
        endpoint = 'https://api.ebay.com/commerce/charity/v1/charity_org'
        
        # Specify query parameters
        params = {
            'q': query,
            'limit': limit
        }
        
        # Specify headers including the marketplace ID and access token
        headers = {
            'X-EBAY-C-MARKETPLACE-ID': 'EBAY_US',  # Change to 'EBAY_GB' for the UK marketplace
            'Authorization': f"Bearer {token['access_token']}"
            # Add any other headers as needed
        }
        
        # Make the authenticated API request
        response = oauth.get(endpoint, params=params, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract and return the name and logo for each organization
            orgs_data = [{'name': org['name'], 'logo': org['logoImage']['imageUrl']} for org in data['charityOrgs']]
            return orgs_data
        else:
            # If the request was not successful, raise an exception
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors
        print("Error connecting to the API:", e)
    except Exception as e:
        # Handle any other unexpected errors
        print("An error occurred:", e)

# Example usage
search_query = "red cross"
charity_orgs_data = search_charity_orgs(search_query)
if charity_orgs_data:
    print("Number of charity organizations retrieved:", len(charity_orgs_data))
    # Print or process the data as needed
    for org in charity_orgs_data:
        print("Name:", org['name'])
        print("Logo:", org['logo'])
