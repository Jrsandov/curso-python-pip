import requests


url = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
    r=requests.get(url)
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category["name"]) 
