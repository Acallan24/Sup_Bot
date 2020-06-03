# =============================================================================
# Created By  : Rahul Kashyap
# Created Date: Wednesday June 3 2020
# =============================================================================
"""Python Script for Automation checkout though supreme"""
# =============================================================================
# Imports
# =============================================================================
from selenium import webdriver
import time

#start the chrome web diriver
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

driver = get_driver()
driver.get("https://www.supremenewyork.com/mobile#categories/Tops/Sweaters") #product page #sample product page

#get the product name 
time.sleep(2)
#filter for producst
catalog = driver.find_elements_by_class_name('name')

mylist = []
var = '****insert full product name here****' #this is the product that the bot is going to filter an search for within the page
for innterHTML in catalog:
    listd = str(innterHTML.get_attribute("innerText"))
    #print(listd)
    mylist.append(listd)
index = mylist.index(var)
index += 1
    
#Adding item to cart till the checkout process
time.sleep(2)
final_Xpath = f'/html/body/div[2]/div[2]/div/ul/li[{index}]'
def click_onXpath(filter):
    #final product click
    filter = driver.find_element_by_xpath(filter)
    filter.click()
click_onXpath(final_Xpath)

time.sleep(2)
add_to_cart = driver.find_element_by_xpath('//span[@class="cart-button"]') 
add_to_cart.click()

time.sleep(2)
driver.get('https://www.supremenewyork.com/shop/cart') #starting checkout

checkout_now = driver.find_element_by_xpath('//a[text()="checkout now"]')
checkout_now.click()


time.sleep(2)
#final send keys function
def send_keys():
    #Name
    name_input = driver.find_element_by_xpath('//input[@id="order_billing_name"]')
    name_input.send_keys("****insert name here****")  

    #email
    name_input = driver.find_element_by_xpath('//input[@id="order_email"]')
    name_input.send_keys("****insert email here****")

    #tel
    name_input = driver.find_element_by_xpath('//input[@id="order_tel"]')
    name_input.send_keys("****insert number here****")

    #address
    address_input = driver.find_element_by_xpath('//input[@id="bo"]')
    address_input.send_keys('****insert address here****')

    #apt
    apt_input = driver.find_element_by_xpath('//input[@id="oba3"]')
    apt_input.send_keys('****insert apartment here****')

    #zip
    zipa_input = driver.find_element_by_xpath('//input[@id="order_billing_zip"]')
    zipa_input.send_keys('****insert zip here****')

    #city
    city_input = driver.find_element_by_xpath('//input[@id="order_billing_city"]')
    city_input.send_keys('****insert city here****')

    #card number
    city_input = driver.find_element_by_xpath('//input[@id="rnsnckrn"]') 
    city_input.send_keys('****insert card number here****')

    #cvv
    city_input = driver.find_element_by_xpath('//input[@id="orcer"]') 
    city_input.send_keys('****insert cvv here****')

    # for the experation date and year follow the same foemat for "agree to rules" below, cpying the full xpath or filtering 

    #agree to rules
    rule_agree = driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/p[2]/label/div/ins')
    rule_agree.click()
send_keys()



