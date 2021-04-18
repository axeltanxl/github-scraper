import requests
import webbrowser
from bs4 import BeautifulSoup as bs

github_user = input('Input Github username: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt' : 'Avatar'})
webbrowser.open(profile_image['src'])