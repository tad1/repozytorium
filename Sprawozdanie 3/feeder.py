import codecs
import requests
import re
import sys
import os
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import CData


def getRss(url):
    if not(url[0:8] == 'https://' or url[0:7] == 'http://'):

        url = "https://" + url
    if(url[len(url)-1] != "/"):
        url += "/"
    print("accesing " + url+" feed")
    result = requests.get(url + 'rss')
    if(not result):
        return result, "Website " + url + " don't support rss!"
    return result.content, ''


def rssToHTML(soup):
    items = soup('item')
    #create output html
    output_HTML = """<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><title>Feeder</title></head><body></body></html>"""
    output_HTML = BeautifulSoup(output_HTML, 'lxml')
    for item in items:
        #create new tags
        div = output_HTML.new_tag('article')
        date_tag = output_HTML.new_tag('span')
        desc = output_HTML.new_tag('h4')
        read_more = output_HTML.new_tag('a')

        
        link = item.find('_link').text

        #get and change date format
        date = item.find('pubdate')
        date = date.text.split(" ")
        date = date[:-1]
        date.insert(0,date[-1])
        date.pop()
        date = ' '.join(date)
        date_tag.append(date)
        date_tag['class'] = 'date'


        
        desc_str = str(item.find('description'))

        #remove parser error ']]>' from cdata
        desc_str = re.sub('\n]]&gt;', '', desc_str)


        read_more['class'] = 'rm_link'
        read_more['href'] = link
        read_more.string = "Read more >"

        #append everything into container and append it to document
        desc.append(BeautifulSoup(desc_str, 'lxml'))
        div.append(date_tag)
        div.append(item.find('title'))
        div.append(desc)
        div.append(read_more)
        div.find('title').name = 'h2'

        output_HTML.find('body').append(div)

    #Add CSS
    articles = output_HTML('article')
    body = output_HTML.find('body')
    head = output_HTML.find('head')
    font_rel = output_HTML.new_tag('link')

    #using Roboto font
    #<link href="https://fonts.googleapis.com/css2?family=Roboto&amp;display=swap" rel="stylesheet">
    font_rel['href']= 'https://fonts.googleapis.com/css2?family=Roboto&amp;display=swap'
    font_rel['rel'] = "stylesheet"
    head.append(font_rel)

    #in case when Roboto font don't work (getting offline)
    output_HTML.find('html')['style'] = 'font-family: Inter'

    body['style'] = 'font-family: Roboto'

    #add styling
    style = output_HTML.new_tag('style')
    style.string = """ article{text-align: center; width: 50%; margin-left: 25%; margin-top: 50px; box-shadow: 0 0 14px rgba(34, 44, 55, 0.1);}
    h2{font-weigth: 500; color: #002835; width: 90%; font-size: 1.5em; margin-left: 5%; margin-top: 0; margin-bottom: 0}
    h4{color: #455463; width: 80%; margin-left: 10%; font-weight: 400; margin-top: 1%}
    .rm_link{font-size: 1.125em; line-height: 1.5em; color: #2196f3;}
    .date{color: #9e9e9e; padding-top: 5px}
    """
    output_HTML.append(style)


    return output_HTML

def main():
    
    url = "https://blog.mozilla.org/"
    print(sys.argv)
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        _url = input("Type blog URL default: https://blog.mozilla.org/\n>>(https://blog.mozilla.org/) ")
        if not _url == '':
          url = _url
    src, message = getRss(url)
    if not src:
        print(message)
        input(">>Press ENTER to continue...")
        return
    print('feed accessed!')
    print('parsing rss...')

    #replace <link> with <_link> to prevent parser error
    src = re.sub(rb'<link>', b'<_link>', src)
    src = re.sub(rb'</link>', b'</_link>', src)
    soup = BeautifulSoup(src, features="lxml")
    rss = soup.find("rss")
    if rss['version'] != '2.0':
        print("Error: this rss version is not supported! Your version:", rss['version'] ,"Only 2.0!")

    html_doc = rssToHTML(soup)

    file = codecs.open('index.html', 'w', "utf-8")
    file.write(html_doc.prettify())
    file.close()
    #get path of created file
    path = "start " + os.getcwd() + "\\index.html"
    print("done.")
    os.system(path)



if __name__ == "__main__":
    main()