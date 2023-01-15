import feedparser
import urllib.request
from os.path import join, isfile

URL = "https://dl.dropboxusercontent.com/s/puqlz6qnlk6ixos/rss.xml"
DOWNLOAD_FOLDER = "/home/mfuchs/Music/Podcasts/Sanft_und_Sorgfaeltig"

NewsFeed = feedparser.parse(URL)

for idx, entry in enumerate(NewsFeed.entries):
    link = entry["links"][0]["href"]
    filename = link.split("/")[-1]
    download_path = join(DOWNLOAD_FOLDER, filename)
    print(f"Downloading {filename} ({idx}/{len(NewsFeed.entries)}) ...")
    if isfile(download_path):
        continue
    # urllib.request.urlretrieve(link, download_path)
