from steam import Steam
import xml.etree.ElementTree as et
import requests

class Avatar(object):
    def __init__(self):
        self.stm = Steam()
        if self.stm.is_connected():
            self.get_avatar()

    def get_avatar(self):
        url = input('\nEnter Steam Profile Link: ')
        url = url + '?xml=1'
        with requests.Session() as s:
            try:
                r = s.get(url)
                xml = et.fromstring(r.text)
                steamId = xml.find('steamID').text
                filename = xml.find('steamID64').text + '.jpg'
                avatar = self.print_resolutions(xml)
                print(f'\nSteamID: {steamId}')
                self.printProg('Getting Avatar Link')
                self.printProg('Downloading')
                self.stm.download_avatar(s, filename, avatar)
                self.printProg("Download Complete")
            except AttributeError:
                print('\nAccount Not Found')
            except et.ParseError:
                print('\nCannot Parse Account Information')
            except Exception as e:
                print(f'\nAn Error Occured: {e}')
            

    def print_resolutions(self, xml):
        self.stm.print_resolutions()
        
        try:
            res = int(input('\nEnter a number: '))
        except ValueError:
            print("Not a number")
            exit()

        if res == 1:
            avt = xml.find('avatarFull').text
        elif res ==2:
            avt = xml.find('avatarMedium').text
        elif res == 3:
            avt = xml.find('avatarIcon').text
        else:
            print('\nWrong Option')
            exit()
        return avt

    def printProg(self, text):
        print("  │")
        print(f"  │─ {text}")

Avatar()