__author__ = 'sagarpatel'

from bs4 import BeautifulSoup
import urllib.request

fixed_url = "http://music-torrent.net"
page = urllib.request.urlopen(fixed_url)
soup = BeautifulSoup(page.read() ,"html.parser")
file_out = open("music_index.txt", "w")

for i in range(2, 90):
    all_a = soup.find_all("a", {"class":"release-thumbnail"})
    for a in all_a:
        file_out.write(fixed_url + a["href"] + "\n")
    page = urllib.request.urlopen(fixed_url + "/" + str(i))
    soup = BeautifulSoup(page.read(),"html.parser")
