from lxml import html
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