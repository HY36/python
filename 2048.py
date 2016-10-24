import requests
from bs4 import BeautifulSoup

url = 'http://cos.name/2016/09/r-and-parallel-computing/'

html = requests.get(url).text

bsObj = BeautifulSoup(html, "lxml")

title = bsObj.find('h1')
