# myapp/services/instagram_api.py

from instagrapi import Client
from pathlib import Path

def login_and_get_info(username="agmpmpdpwp", password="Kamekiti1192"):
    cl = Client()
    
    session_file = Path('session_settings.json')
    if session_file.exists():
        settings = cl.load_settings(session_file)
        cl.set_settings(settings)
        print("セッションでログインする")
    else:
        cl.login(username=username, password=password)
        settings = cl.get_settings()
        cl.dump_settings(session_file)
        print("新規でログインする")

    user_info = cl.user_info(cl.user_id)
    
    # フォロワーを取得
    followers = cl.user_followers(cl.user_id)
    
    for user_id in followers:
        followers = cl.user_info(user_id)
    
    # フォローを取得
    following_data = cl.user_following(cl.user_id)

    for user_id in following_data:
        following = cl.user_info(user_id)
    
    return {'user_info': user_info, 'followers': followers, 'following': following}

# if __name__ == "__main__":
#     # For testing purposes, use your actual username and password here
#     test_username = "agmpmpdpwp"
#     test_password = "Kamekiti1192"
#     login_and_get_info(test_username, test_password)
