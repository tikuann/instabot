from django.shortcuts import render
from myapp.services import instagram_api

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

        context = {
            'user_info': user_info_dict,
            'followers_info': followers_info_dict,
            'following_info': following_info_dict,
        }
        print(context)
    return render(request, 'login_and_user_info.html', context)
