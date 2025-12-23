import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"



def get_all_posts(url):
    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as error:
        print(error)
        return None
    
def extract_titles(posts):
    
    titles = []
    
    if not isinstance(posts,list):
        return titles
    
    for post in posts:
        title = post.get("title")
        if title:
            titles.append(title)

    return titles

def main():
    
    posts = get_all_posts(API_URL)  
    
    if not posts:
        print("No posts found")
        return
    
    
    titles = extract_titles(posts)
    
    for index, title in enumerate(titles, start=1):
        print(f"{index}. {title}")


if __name__ == "__main__":
    main()
