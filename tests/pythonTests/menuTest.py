# Imports Selenium python module
from selenium import webdriver


class MenuTest:
    def __init__(self, driver: webdriver.Chrome):
     
        print("")

        # Find menu by id
        menu = driver.find_elements_by_id("menu")
        # For loop that loops through all the items in the list and prints them
        for item in menu:
            print(item.text)
