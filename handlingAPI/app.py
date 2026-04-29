import requests

def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%252Cid%252Ccontent&page=1"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    

def main():
    try:
        fetch_random_jokes()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()