# -*- coding: utf-8 -*-


"""

"""
import requests
import json
import time
from selenium import webdriver


"""
    Replace websiteURL with website you want the bot to
    get the item
    MUST BE A SHOPIFY WEBSITE
"""

websiteURL = 'https://bdgastore.com'

def availabilityCheck():
    
    r = requests.get(websiteURL + '/products.json')
    products = json.loads((r.text))['products']
    
    for product in products:
        print(product['title'])
        productname = product['title']
        
        
        # Replace quote with name of Item you want from that website
        if productname == 'TIRED T-SHIRT':
        
            producturl = websiteURL + '/products/' + product['handle']
            print('Item Found')
            return producturl
        else:
            return False
        
def buyProduct(url):
    driver = webdriver.Chrome(executable_path=r'/Users/adrianolguin/Desktop/chromedriver')
    driver.get(str(url))
    
    """
    The code below only works for the bdgastore website as it is 
    currently hardcoded
   
    """
    
    #close pop up if it shows
    try:
        driver.find_element_by_xpath('//div[@class="mc-closeModal"]').click()
        time.sleep(3)
    except:
        print('No pop up window shown (:')
    
    #click size M
    driver.find_element_by_xpath('//div[@data-value="M"]').click()
    
    #click add to cart
    driver.find_element_by_xpath('//button[@class="button full"]').click()
    time.sleep(3)
    
    
    
    """
    This following code WILL work for any Shopify website when checking out
    as all Shopify websites have the same check out procedure
    
    """
    
    #click check out
    driver.find_element_by_xpath('//input[@value="Check Out"]').click()
    time.sleep(3)
    
    #enter email
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('myemail@gmail.com')
    time.sleep(0.25)
    
    #enter First Name
    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys('Luis')
    time.sleep(0.25)
    
    #enter Last Name
    driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys('Hernandez')
    time.sleep(0.25)
    
    #enter Street
    driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys('MY STREET ADDRESS')
    time.sleep(0.25)
    
    #enter City
    driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys('Norwalk')
    time.sleep(0.25)
    
    #enter Zip
    driver.find_element_by_xpath('//input[@placeholder="ZIP code"]').send_keys('90650')
    time.sleep(0.25)
    
    #enter phone
    driver.find_element_by_xpath('//input[@data-backup="phone"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//input[@data-backup="phone"]').send_keys('562')
    time.sleep(1)
    driver.find_element_by_xpath('//input[@data-backup="phone"]').send_keys('1234567')
    time.sleep(0.25)
    driver.find_element_by_xpath('//input[@data-backup="phone"]').send_keys(u'\ue007')
    
    
while True:
    
    myUrl = availabilityCheck()
    if myUrl!=False:
        buyProduct(myUrl)
        break
    else:
        print('Product not available')