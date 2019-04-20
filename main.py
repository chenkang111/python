
#coding=utf-8
import urllib
from bs4 import  BeautifulSoup

def getHtml(url):
  # urllib.addheaders('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36')
   response = urllib.urlopen(url)
   print response
   soup =BeautifulSoup(response,'html.parser')
   return response



if __name__ == '__main__':
    getHtml('https://www.meipai.com/')



