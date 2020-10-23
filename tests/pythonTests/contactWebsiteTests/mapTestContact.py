# Imports Selenium python module
from selenium import webdriver


class MapTestContact:
    def __init__(self, driver: webdriver.Chrome):

        print("")

        # Find map by id
        googleMap = driver.find_element_by_id("googleMaps")
        # If not true, returns error
        print(googleMap.get_attribute("src"))