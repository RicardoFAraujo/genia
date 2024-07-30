import instaloader
import os
import requests

def get_instagram_profile_info(username):
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        full_name = profile.full_name
        followers = profile.followers
        profile_pic_url = profile.profile_pic_url
        return full_name, followers, profile_pic_url
    except instaloader.exceptions.ProfileNotExistsException:
        return "Profile not found", None, None
    except Exception as e:
        return str(e), None, None

def download_profile_pic(url, username):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            static_path = os.path.join('static', 'src')
            if not os.path.exists(static_path):
                os.makedirs(static_path)
            file_path = os.path.join(static_path, f'{username}.jpg')
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return file_path
        else:
            return None
    except Exception as e:
        return None
