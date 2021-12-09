from lxml import html
from lxml import etree
from lxml.html import fromstring
from io import StringIO
import requests

#test website

response = requests.get("https://ethanmorganumich.github.io/source/blog")
baseDomain = "https://ethanmorganumich.github.io"
if not response:
    print("FAIL")
    exit(1)

webpage = html.fromstring(response.content)
links = webpage.xpath('//a/@href')
print(links)

for link in links:
    if link[0] == "/":
        response = requests.get(baseDomain + link)
    else:
        response = requests.get(link)

    if not response:
        print("error loading:", response.url)
        exit(1)
    print("loaded", response.url)

    tree = fromstring(response.content)
    print(tree.findtext('.//h1'))

    #validate html
    # if not etree.parse(response.text, etree.HTMLParser(recover=False)):
    #     exit(1)

