import requests

from config import UNSPLASH_ACCESS_KEY

def test_squirrel_api():
    print("connecting to Unsplash")
    
    url = f"https://api.unsplash.com/photos/random?query=squirrel&client_id={UNSPLASH_ACCESS_KEY}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            image_url = data['urls']['regular']
            photographer = data['user']['name']
            description = data.get('alt_description', 'a cute squirrel')
            
            print("Success! Squirrel located.")
            print(f"Photographer: {photographer}")
            print(f"Description: {description}")
            print(f"Link: {image_url}")
            
        else:
            print(f"Failed with Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_squirrel_api()