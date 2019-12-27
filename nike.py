import requests
from bs4 import BeautifulSoup as bs
import random

session = requests.session()
# user agent
headers = {}
session.headers.update(headers)


def getSizesInStock():
    global session
    # link to shoe
    endpoint = 'https://www.nike.com/t/air-jordan-4-retro-wntr-shoe-9L34P1/CQ9597-401'
    response = session.get(endpoint)
    
    soup  = bs(response.text, "html.parser")
    
    div = soup.find("form", { "id":"buyTools" })
    
    allSizes = div.find_all("label")
    
    sizes = []
    
    for size in allSizes:
        sizeId = size['id']
        sizes.append(sizeId.split('__')[1])
    return sizes

print(getSizesInStock())