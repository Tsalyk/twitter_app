import requests, json
from hidden import oauth


def parse_data(nickname: str) -> dict:
    """
    Parses json file and returns a dict
    where key is a name of friend
    and value is a location
    """
    base_url = "https://api.twitter.com/"
    bearer_token = oauth()["bearer_token"]
    search_url = f"{base_url}1.1/friends/list.json"

    search_headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    search_params = {
        "screen_name": nickname,
        "count": 50
    }

    response = requests.get(search_url,
                            headers=search_headers,
                            params=search_params)

    data = response.json()
    user_dict = {}

    for user in data["users"]:
        user_dict[user["name"]] = user["location"]

    return user_dict