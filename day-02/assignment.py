import requests

api_url = "https://jsonplaceholder.typicode.com/todos"


response = requests.get(api_url)

all_titles = []

for todo in response.json():
    all_titles.append(todo["title"])
    
print(all_titles)



