# Imports Selenium python module
from selenium import webdriver


class TitleTest:
    def __init__(self, driver: webdriver.Chrome):

        print("")

        # Find title by id
        titleText = driver.find_element_by_id("titleTextTest").text
        # If not true, returns error
        assert "PIZZERIA SANTOS" in titleText
        print(titleText)

        # Find title image by id
        titleImage = driver.find_element_by_id("titleImageTest")
        # Find title image by style property
        print(titleImage.value_of_css_property("background-image"))
        
        # Find title phone number by id
        titlePhoneNumber = driver.find_element_by_id("titlePhoneNumberTest").text
        # If not true, returns error
        assert "0630-555-555" in titlePhoneNumber
        print(titlePhoneNumber)

        # Find title address by id
        titleAddress = driver.find_element_by_id("titleAddressTest").text
        # If not true, returns error
        assert "Fjällgatan 32H" in titleAddress
        print(titleAddress)
