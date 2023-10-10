from instagrapi import Client
from pathlib import Path

def main():
    # クライアントのインスタンスを作成
    cl = Client()
    
    # Check if session file exists
    session_file = Path('session_settings.json')
    if session_file.exists():
        # Load session settings from file
        settings = cl.load_settings(session_file)
        cl.set_settings(settings)
        print("セッションでログインしたよ")
    else:
        # Perform login if session file doesn't exist
        cl.login(username='agmpmpdpwp', password='Kamekiti1192')
        # Get and dump session settings to file
        settings = cl.get_settings()
        cl.dump_settings(session_file)
        print("新しくログインしたよ")
    
    # ユーザー情報を取得
    user_info = cl.user_info(cl.user_id)
    print("ユーザー情報:", user_info)
    
    # フォロワーを取得
    followers = cl.user_followers(cl.user_id)
    print("フォロワー:")
    for follower in followers:
        print(follower)
    
    # フォローを取得
    following = cl.user_following(cl.user_id)

    for user_id in following:
        user_info = cl.user_info(user_id)
        print(user_info)

if __name__ == "__main__":
    main()
