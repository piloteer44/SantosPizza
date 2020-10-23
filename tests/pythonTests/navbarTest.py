# Imports Selenium python module
from selenium import webdriver


class NavbarTest:
    def __init__(self, driver: webdriver.Chrome):

        print("")
 
        # Find the navbar by id
        navbarTest = driver.find_element_by_class_name("navbar")
        # Find navbar children and find href attribute
        for item in navbarTest.find_elements_by_xpath(".//*"):
            print(item.get_attribute("href"))

