import requests

def user_info(username):
    url = f'https://codeforces.com/api/user.info?handles={username}'
    
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK':
        user = data['result'][0]
        
        # Extracting details
        rank = user.get('rank', 'N/A')
        rating = user.get('rating', 'N/A')
        max_rating = user.get('maxRating', 'N/A')
        country = user.get('country', 'N/A')
        contribution = user.get('contribution', 'N/A')
        
        # Displaying the information
        print(f"Username: {username}")
        print(f"Rank: {rank}")
        print(f"Rating: {rating}")
        print(f"Max Rating: {max_rating}")
        print(f"Country: {country}")
        print(f"Contribution: {contribution}")
    else:
        print(f"Error: {data['comment']}")

# Input username
username = input("Enter your Codeforces username: ")
user_info(username)
