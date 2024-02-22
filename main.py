from fastapi import FastAPI, HTTPException, Query
import requests
from oauth import get_access_token
from dotenv import load_dotenv
import os

load_dotenv()


app = FastAPI()

@app.get("/charity/search/")
async def search_charity(query: str = Query(...), limit: int = Query(100), offset: int = Query(0)):
    try:
        client_id = os.environ.get("CLIENT_ID")
        client_secret = os.environ.get("CLIENT_SECRET")
        access_token = get_access_token(client_id, client_secret)
        print(access_token, "*********Token***********")

        response = requests.get(
            f"https://api.ebay.com/commerce/charity/v1/charity_org?q={query}&limit={limit}&offset={offset}",
            headers={
                "X-EBAY-C-MARKETPLACE-ID": "EBAY_US",
                "Authorization": f'Bearer {access_token}' 
            },
        )

        response.raise_for_status()

        data = response.json()

        if "charityOrgs" not in data:
            raise KeyError("charityOrgs key not found in response")
        
        charities = []
        for charity in data["charityOrgs"]:
            if "name" not in charity or "logoImage" not in charity:
                raise KeyError("Required keys not found for charity")
            
            charity_data = {
                "name": charity["name"],
                "logoImage": charity["logoImage"].get("imageUrl", None)
            }
            charities.append(charity_data)

        result = {
            'charities': charities
        }

        if "total" in data and data["total"] > 10:
            result["total"] = data["total"]
            result["href"] = data["href"]
            result["next"] = data["next"]
            result["limit"] = data["limit"]
            result["offset"] = data["offset"]

        return result


    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Error connecting to the API")
    except KeyError as e:
        raise HTTPException(status_code=500, detail=f"Error parsing response: {e}")
