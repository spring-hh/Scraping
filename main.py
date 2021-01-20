from bs4 import BeautifulSoup
import requests

html = requests.get('https://git-scm.com')
soup = BeautifulSoup(html.text, 'lxml')

git_version = soup.findAll('span', {'class': 'version'})
print(git_version[0].text)