import requests
import shutil

class Steam(object):

    def is_connected(self):
        url='https://www.google.com/'
        try:
            _ = requests.get(url, timeout=5)
            return True
        except requests.ConnectionError:
            print("\nNo Internet Connection.")
        return False

    def download_avatar(self, session, filename, avatar_url):
        avatar = session.get(avatar_url, stream=True)
        avatar.raw.decode_content = True
        with open(filename, "wb+") as f:
            shutil.copyfileobj(avatar.raw, f)
            del avatar
            f.close()


    def print_resolutions(self):
        print('\nChoose Avatar Resolution: \n')
        print('1. Full Res (184 x 184)')
        print('2. Medium Res (64 x 64)')
        print('3. Small Res (32 x 32)')