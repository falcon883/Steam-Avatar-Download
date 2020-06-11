from bs4 import BeautifulSoup
import requests
import shutil

def is_Connected():
    url='https://www.google.com/'
    try:
        _ = requests.get(url, timeout=5)
        return True
    except requests.ConnectionError:
        print("\nNo Internet Connection.")
    return False

def resOpts(link):
    print('\nChoose Avatar Resolution: \n')
    print('1. Full Res (184 x 184)')
    print('2. Medium Res (64 x 64)')
    print('3. Small Res (32 x 32)')
    resolution = int(input('\nEnter a Number: '))

    if resolution == 1:
        pass
    elif resolution == 2:
        link = link.replace('_full','_medium')
    elif resolution == 3:
        link = link.replace('_full','')
    else:
        print('\nWrong Option.')
        exit()
    return link

if is_Connected():
    url = input("\nEnter Steam Profile URL: ")

    try:
        r = requests.get(url)
    except requests.RequestException as re:
        #print(re)
        print('\nError Connecting To Steam')
        exit()

    if r.status_code == 200:
        try:
            avatar_link = BeautifulSoup(r.content,'html.parser')
            avatar_img = avatar_link.find('link',{'rel':'image_src'})['href']
            filename = url.split('/')[4] + '.jpg'
            avatar_img = resOpts(avatar_img)
            avatar = requests.get(avatar_img,stream=True)
            Ifile = open(filename,'wb+')
            avatar.raw.decode_content = True
            shutil.copyfileobj(avatar.raw,Ifile)
            print('\nDownload Complete')
            del avatar
        except TypeError as t:
            #print(t)
            print('\nAccount Not Found or Cannot Access The Avatar')
        except Exception as ex:
            #print(ex)
            print('\nError Downloading Avatar')
    
