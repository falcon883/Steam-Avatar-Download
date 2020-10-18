from bs4 import BeautifulSoup
from steam import Steam
import requests

class Avatar(object):

    def __init__(self):
        self.stm = Steam()
        if self.stm.is_connected():
            self.get_avatar()    

    def get_avatar(self):
        url = input("\nEnter Steam Profile URL: ")

        try:
            with requests.Session() as s:
                r = s.get(url)
                if r.status_code == 200:
                    bs = BeautifulSoup(r.content,'html5lib')
                    avatar = bs.find('link',{'rel':'image_src'})['href']
                    filename = url.split('/')[4] + '.jpg'
                    avatar = self.print_resolutions(avatar)
                    self.stm.download_avatar(s, filename, avatar)
        except requests.RequestException:
            print('\nError Connecting To Steam')
        except TypeError:
            print('\nAccount Not Found or Cannot Access The Avatar')
        except Exception:
            print('\nError Downloading Avatar')

    def print_resolutions(self, link):
        self.stm.print_resolutions()
        try:
            resolution = int(input('\nEnter a Number: '))
            if resolution == 1:
                pass
            elif resolution == 2:
                link = link.replace('_full','_medium')
            elif resolution == 3:
                link = link.replace('_full','')
            else:
                print("Invalid Input. Defaulting to Full Res")
            return link
        except ValueError:
            print("Not a number")
            exit()

Avatar()