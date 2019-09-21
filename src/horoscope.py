#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# this makes the Firefox browser run in background
opts = webdriver.FirefoxOptions()
opts.add_argument('--headless')
driver = webdriver.Firefox(options=opts)

# opts = Options()
# opts.headless = True
# driver = webdriver.Firefox(options=opts)

# this makes the Chrome browser run in background
# opts = webdriver.ChromeOptions()
# opts.add_argument('--headless')
# driver = webdriver.Chrome(options=opts)

sign = input("Enter the horoscope: ")
driver.get("https://thehimalayantimes.com/category/horoscopes/{}".format(sign))

horoscope = driver.find_element_by_class_name("col-sm-9").text
print(horoscope)
