from urllib.request import urlopen
from urllib.request import urlretrieve
import urllib.error
import xml.etree.ElementTree as et

def resOpts(avt):
    print('\nChoose Avatar Resolution: \n')
    print('1. Full Res (184 x 184)')
    print('2. Medium Res (64 x 64)')
    print('3. Small Res (32 x 32)')
    res = int(input('\nEnter a number: '))

    if res == 1:
        avt = avt.find('avatarFull').text
    elif res ==2:
        avt = avt.find('avatarMedium').text
    elif res == 3:
        avt = avt.find('avatarIcon').text
    else:
        print('\nWrong Option')
        exit()
    return avt

def printProg(text):
    print("  │")
    print(f"  │─ {text}")

try:
    profile = input('\nEnter Steam Profile Link: ')
    url = profile + '?xml=1'
    url = urlopen(url)
    avatar = et.fromstring(url.read())
    steamId = avatar.find('steamID').text
    filename = avatar.find('steamID64').text + '.jpg'
    avatar = resOpts(avatar)
    print('\nSteamID: ' + steamId)
    printProg('Getting Avatar Link')
    printProg('Downloading')
    urlretrieve(avatar,filename)
    printProg('Download Complete')
except et.ParseError:
    print('\nCannot Parse Account Information')
except (urllib.error.URLError,urllib.error.HTTPError):
    print('\nConnection Error or Please Check Your URL')
except urllib.error.ContentTooShortError:
    print('\nDownload Failed')
except AttributeError:
    print('\nAccount Not Found')