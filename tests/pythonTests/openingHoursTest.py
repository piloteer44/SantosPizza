# Imports Selenium python module
from selenium import webdriver


class OpeningHoursTest:
    def __init__(self, driver: webdriver.Chrome):

        print("")
        
        # Find opening hours list by id
        openingHours = driver.find_elements_by_id("openingHours")
        # For loop that loops through all the items in the list and prints them
        for item in openingHours:
            print(item.text)
        