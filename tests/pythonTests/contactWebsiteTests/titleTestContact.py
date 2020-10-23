# Imports Selenium python module
from selenium import webdriver


class TitleTestContact:
    def __init__(self, driver: webdriver.Chrome):

        print("")

        # Find the title by id
        title = driver.find_element_by_id("titleTextTest").text
        # If not true, returns error
        assert "PIZZERIA SANTOS" in title
        print(title)
