# Imports Selenium python module
from selenium import webdriver


class InfoTestContact:
    def __init__(self, driver: webdriver.Chrome):

        print("")

        # Find address by id
        text = driver.find_element_by_id("address").text
        # If not true, returns error
        assert "Fjällgatan 32H" in text
        print(text)

        # Find zipcode by id
        text = driver.find_element_by_id("zipCode").text
        # If not true, returns error
        assert "981 39 KIRUNA" in text
        print(text)

        print("")

        # Find email by id
        text = driver.find_element_by_id("email")
        # Write email href
        print(text.get_attribute("href"))

        print("")

        # Find phone number by id
        address = driver.find_element_by_id("phoneNumber")
        # Write mobile href
        print(address.get_attribute("href"))
