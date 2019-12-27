import requests
import json
from selenium import webdriver
import time

def checkStock():
    r = requests.get('https://featuresneakerboutique.com/products.json')
    products = json.loads((r.text))['products']
    
    for product in products:
        productName = product['title']
        
        if productName == 'Asics Gel-Kayano 5 OG - White/White':
            productUrl = 'https://featuresneakerboutique.com/products/' + product['handle']
            print('found item')
            return productUrl
    else :
        return False

def buyProduct():
    driver = webdriver.Chrome(executable_path='./chromedriver 2')
    
    driver.get(str())
    
    # get size
    driver.find_element_by_xpath('//div[@data-value="9"]').click()
    # add to cart
    driver.find_element_by_xpath('//button[@id="AddToCart"]').click()
    time.sleep(3)
    # checkout need a lil arrow
    driver.find_element_by_xpath('//button[@Value="Check Out "]').click()
    time.sleep(3)
    
    
    # checkout info Email
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('email@email.com')
    time.sleep(1)
    # first name
    driver.find_element_by_xpath('//button[@Value="First Name"]').send_keys('john')
    time.sleep(1)
    # last name
    driver.find_element_by_xpath('//button[@Value="Last Name"]').send_keys('smith')
    time.sleep(1)
    # street
    driver.find_element_by_xpath('//button[@Value="Address"]').send_keys('addresssss')
    time.sleep(1)
    # city
    driver.find_element_by_xpath('//button[@Value="City"]').send_keys('big city')
    time.sleep(1)
    # zip
    driver.find_element_by_xpath('//button[@Value="zip"]').send_keys('10289')
    time.sleep(1)


while True:
    myurl = checkStock()
    if myurl != False:
        buyProduct(myurl)
        break
    else:
        print('none')