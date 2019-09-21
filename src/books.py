from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os

driver = webdriver.Chrome()
driver.get("http://books.toscrape.com/")

while True:
    articleDiv = driver.find_elements_by_xpath("//article[@class='product_pod']")

    for article in articleDiv:
        bookTitle = article.find_element_by_tag_name('h3 > a')

        # price = article.find_element_by_xpath("//div[@class='product_price']/p[1]").text
        # above code using xpath didn't work, so used css selector
        price = article.find_element_by_css_selector("div.product_price > p").text

        # got error using xpath, so used css selector instead
        rating = article.find_elements_by_css_selector("article.product_pod > p")[0]

        print("******************************************")
        print("BookTitle: " + bookTitle.get_attribute("title"))
        print("Price: " + price)
        print("Rating in Five: " + rating.get_attribute("class").split(" ")[1])
        print("##########################################")

    try:
        nextBtn = driver.find_element_by_xpath("//li[@class='next']/a")
        nextBtn.click()
    except NoSuchElementException:
        print("Reached the end page!")
        break

