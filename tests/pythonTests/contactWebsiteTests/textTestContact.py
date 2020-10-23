# Imports Selenium python module
from selenium import webdriver


class TextTestContact:
    def __init__(self, driver: webdriver.Chrome):

        print("")

        # Find the text by id
        text = driver.find_element_by_id("welcomeText").text
        # If not true, returns error
        assert "HITTA HIT TILL OSS!" in text
        print(text)
