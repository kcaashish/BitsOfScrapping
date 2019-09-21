from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/")


while True:
    quoteDiv = driver.find_elements_by_class_name("quote")

    for quote in quoteDiv:
        text = quote.find_element_by_class_name("text").text
        author = quote.find_element_by_class_name("author").text
        print("***********************************************")
        print("Quote: " + text)
        print("Author: " + author)
        print("################################################")

    try:
        nextBtn = driver.find_element_by_css_selector("li.next > a")
        nextBtn.click()
    except NoSuchElementException:
        print("No more pages!")
        break


driver.quit()






