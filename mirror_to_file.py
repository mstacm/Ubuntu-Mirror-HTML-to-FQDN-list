from bs4 import BeautifulSoup
from urlparse import urlparse
import urllib

RELEASE_URL = "https://launchpad.net/ubuntu/+cdmirrors"
ARCHIVE_URL = "https://launchpad.net/ubuntu/+archivemirrors"

f = urllib.urlopen( RELEASE_URL )
rawHtml = f.read()

soup = BeautifulSoup(rawHtml)
mirrorTable = soup.find(id='mirrors_list')

mirrorList = set()

for link in mirrorTable.find_all('a'):
  fqdn = urlparse(link.get('href'))[1]
  mirrorList.add(fqdn)

with open('ubuntu_mirror_list.url', 'w') as f:
  for fqdn in mirrorList:
    f.write(fqdn + "\n")

#with open('ubuntu_archive_list.url', 'w') as f:
#  for fqdn in archiveList:
#    f.write(fqdn + '\n')

