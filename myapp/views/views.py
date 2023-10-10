from django.shortcuts import render
from myapp.services import instagram_api
import base64
import requests

def login_and_user_info(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = instagram_api.login_and_get_info(username, password)
        user_info = data['user_info']
        followers_info = data['followers']
        following_info = data['following']
        
        user_info_dict = user_info.__dict__
        followers_info_dict = following_info.__dict__
        following_info_dict = followers_info.__dict__
        
        # 自分のアイコンエンコード
        profile_pic_url = user_info_dict.get('profile_pic_url')
        if profile_pic_url:
            response = requests.get(profile_pic_url)
            img_data = response.content
            base64_encoded = base64.b64encode(img_data).decode('utf-8')
            user_info_dict['profile_pic_url'] = f"data:image/jpeg;base64,{base64_encoded}"
            
        #フォロワーのアイコンエンコード
        profile_pic_url = followers_info_dict.get('profile_pic_url')
        if profile_pic_url:
            response = requests.get(profile_pic_url)
            img_data = response.content
            base64_encoded = base64.b64encode(img_data).decode('utf-8')
            followers_info_dict['profile_pic_url'] = f"data:image/jpeg;base64,{base64_encoded}"
            
        #フォロー中のアイコンエンコード  
        profile_pic_url = following_info_dict.get('profile_pic_url')
        if profile_pic_url:
            response = requests.get(profile_pic_url)
            img_data = response.content
            base64_encoded = base64.b64encode(img_data).decode('utf-8')
            following_info_dict['profile_pic_url'] = f"data:image/jpeg;base64,{base64_encoded}"

        context = {
            'user_info': user_info_dict,
            'followers_info': followers_info_dict,
            'following_info': following_info_dict,
        }
    return render(request, 'login_and_user_info.html', context)
