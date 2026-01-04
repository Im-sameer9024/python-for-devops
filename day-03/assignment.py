import requests
import json

class APIClient:

    def __init__(self, base_url, headers=None, params=None):
        self.base_url = base_url
        self.headers = headers or {}
        self.params = params or {}

    def fetch_data(self):
        try:
            response = requests.get(
                url=self.base_url,
                headers=self.headers,
                params=self.params,
                timeout=5
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            return None

    def extract_data(self, data):
        """
        Handles different API response structures safely
        """
        if not data:
            return []

        if isinstance(data.get("data"), list):
            return data["data"]

        if isinstance(data.get("data", {}).get("data"), list):
            return data["data"]["data"]

        return []

    def save_data(self, filename, data):
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Data saved to {filename} successfully.")
        except IOError as e:
            print(f"File Error: {e}")


api_url = "https://api.freeapi.app/api/v1/public/books"

headers = {
    "accept": "application/json"
}

query_params = {
    "page": 1,
    "limit": 10,
    "query": "science"
}

client = APIClient(api_url, headers, query_params)

response = client.fetch_data()
books = client.extract_data(response)
client.save_data("books.json", books)
