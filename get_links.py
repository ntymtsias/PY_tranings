url = 'https://study.vsedetigenii.pro/wpm/start/'

login = ' Ochakovska'
password = 'Masha@2407'
# get all youtube links from the url above
import requests
from bs4 import BeautifulSoup
import re
import os
import subprocess
import sys

def get_youtube_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a', href=re.compile('youtube.com'))
    print(links)
    return links

def download_youtube_links(links):
    for link in links:
        url = link.get('href')
        print(url)
        subprocess.call(['youtube-dl', url])

#login to the site and get the links
def login(url):
    # url = 'https://study.vsedetigenii.pro/wpm/start/'
    session = requests.Session()
    login_data = {'log': login, 'pwd': password}
    r = session.post(url, data=login_data)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a', href=re.compile('youtube.com'))
    print(links)
    return links

def main():
    links = login(url)
    # download_youtube_links(links)

if __name__ == '__main__':
    main()
    