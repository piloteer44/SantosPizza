# Imports Selenium python module
from selenium import webdriver


class PicturesTest:
    def __init__(self, driver: webdriver.Chrome):

        print("")

        # Find pizza images by class name
        imagesTest = driver.find_elements_by_class_name("pizzaPictures")
        # For loop that loops through all the items in the div and prints their source
        for item in imagesTest:
             print(item.get_attribute("src"))