from selenium import webdriver
from parsel import Selector
from time import sleep
import parameters
profile_link='https://www.linkedin.com/in/shymaa-alsayed-47115218b/'

def scrape_data(profile_link):

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(r"D:\chromewebdriver\chromedriver.exe",options=options)

    #login using webdriver
    driver.get('https://www.linkedin.com')

    username = driver.find_element('id','session_key')
    username.send_keys(parameters.linkedin_username)
    sleep(0.5)

    password = driver.find_element('id','session_password')
    password.send_keys(parameters.linkedin_password)
    sleep(0.5)

    sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
    sign_in_button.click()
    sleep(0.5)


    driver.get(profile_link) #change profile_url here.
    sel = Selector(text=driver.page_source)

    name = sel.xpath('//h1/text()').extract_first()
    split_name=name.lower().split()

    company = sel.xpath('//*[starts-with(@class,"pv-top-card-v2-section__entity-name pv-top-card-v2-section__company-name")] / text()').extract_first()
    print(company)
    return split_name[0], split_name[1]

fname,lname=scrape_data('https://www.linkedin.com/in/shymaa-alsayed-47115218b/')
print(fname)
print(lname)
"""input_file = open('input_file.txt', 'w')
input_file.write(split_name[0])
input_file.write("\n")
input_file.write(split_name[1])
print(name)"""

