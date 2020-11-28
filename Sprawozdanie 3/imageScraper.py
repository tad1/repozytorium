import requests
import sys
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class App:
    def __init__(self,url, limit = None):
        self.url = url
        self.limit = limit
        self.result = []
        self.loadWeb()
        self.find_images()

    def loadWeb(self):
        result = requests.get(self.url)
        self.soup = BeautifulSoup(result.content, 'lxml')
        
    def find_images(self):
        images = self.soup.find_all('img', limit= self.limit)

        for image in images:
            self.result.append(urljoin(self.url, image['src']))

    def print_res(self):
        for link in self.result:
            print(link)

    def save_to_file(self):
        f = open('image_links.txt', 'w+')
        for link in self.result:
            f.write(link+'\r')

def user_input():
    limit = None
    url = input("Type URL:\n>> ")
    limit = input("Limit of images:\n>>(None)")
    return url, limit

def main():
    limit = ''
    arg_num = len(sys.argv)

    #get sys arguments
    if arg_num == 1:
        #no arguments get input from user
        url, limit = user_input()
    elif arg_num > 1:
        url = sys.argv[1]    
        if arg_num > 2:
            limit = sys.argv[2]

    #check passed argument
    if not re.compile('//').search(url):
        url = 'https://' + url
    if limit.isnumeric and limit != '':
        limit = int(limit)
    else:
        limit = None

    app = App(url, limit)
    app.print_res()
    app.save_to_file()

main()
