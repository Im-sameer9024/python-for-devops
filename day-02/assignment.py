import requests
import json

api_url = "https://api.freeapi.app/api/v1/public/randomusers"

class DataFetcher:

     def __init__(self, url,filename):
          self.url = url
          self.filename = filename

     def fetch_data(self):
          try:
               response = requests.get(url=self.url)
               response.raise_for_status()
               return response.json()
          except requests.exceptions.RequestException as e:
               print(f"An error occurred: {e}")
               return None
     
     def save_data(self,data):
          try:
               with open(self.filename,'w') as file:
                    json.dump(data,file,indent=4)
                    print("Data saved successfully.")
          except IOError as e:
               print(f"An error occurred while saving data: {e}")
    
if __name__ == "__main__":

     fetcher = DataFetcher(api_url, 'random_user.json')
     response_data = fetcher.fetch_data()

     if response_data:
         users = response_data['data']['data']
         fetcher.save_data(users)
     else:
          print("Failed to fetch data.")