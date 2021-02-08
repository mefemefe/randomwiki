from bs4 import BeautifulSoup as bs
import urllib.request
wiki = urllib.request.urlopen("https://en.wikipedia.org/wiki/Special:Random")
wiki = bs(wiki, "html.parser")
link = wiki.find("link", rel="canonical", href=True)

print(wiki.title.string)
print(link['href'])
