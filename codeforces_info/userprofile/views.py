import requests
from django.shortcuts import render

def get_codeforces_details(username):
    url = f'https://codeforces.com/api/user.info?handles={username}'
    
    response = requests.get(url)
    data = response.json()
    
    motivational_quotes = {
        "Pupil": "Keep pushing, you're just starting!",
        "Specialist": "You're getting better, keep it up!",
        "Expert": "Great job! Keep challenging yourself!",
        "Candidate Master": "You're almost at the top, amazing!",
        "Master": "You're a top contender!",
        "International Master": "Impressive! You're among the best!",
        "Grandmaster": "Incredible! You are one of the elite!",
        "International Grandmaster": "You're a legend in the making!",
        "Legendary Grandmaster": "You're one of the greatest, keep dominating!"
    }
    
    if data['status'] == 'OK':
        user = data['result'][0]
        
        rank = user.get('rank', 'N/A')
        rating = user.get('rating', 'N/A')
        max_rating = user.get('maxRating', 'N/A')
        country = user.get('country', 'N/A')
        contribution = user.get('contribution', 'N/A')
        avatar = user.get('avatar', '')  # Profile picture URL
        handle = user.get('handle', 'N/A')  # The username/handle
        
        motivational_message = motivational_quotes.get(rank, "Keep improving, you're doing great!")
        
        return {
            "rank": rank,
            "rating": rating,
            "max_rating": max_rating,
            "country": country,
            "contribution": contribution,
            "avatar": avatar,
            "handle": handle,  # Add the handle here
            "motivational_message": motivational_message
        }
    else:
        return None


def home(request):
    details1 = None
    details2 = None
    error = None
    
    if request.method == 'POST':
        username1 = request.POST.get('username1')
        username2 = request.POST.get('username2')
        
        if username1 and username2:
            details1 = get_codeforces_details(username1)
            details2 = get_codeforces_details(username2)
            
            if not details1 or not details2:
                error = 'One or both users not found or error in fetching data'
    
    return render(request, 'userprofile/home.html', {'details1': details1, 'details2': details2, 'error': error})
