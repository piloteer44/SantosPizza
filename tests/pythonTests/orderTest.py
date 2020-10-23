from selenium import webdriver


def setValueAndCheck(self, value: int, driver: webdriver.Chrome):
    # Change the value of the input element to a valid zip-code
    driver.execute_script(
        "arguments[0].setAttribute('value', arguments[1])", self.inputElement, value)
    self.confirmButton.click()
    # Checks if input value outputs the correct message
    if driver.find_element_by_id("orderStatus").text != "Vi levererar inte till dig":
        print("Zip Code test succeeded with: " + str(value))
        return True
    else:
        print("Zip Code test didn't succeed with: " + str(value))
        return False


class OrderTest:
    def __init__(self, driver: webdriver.Chrome):
        print("")
        # Find order button by id
        orderButton = driver.find_element_by_id("orderButton")
        assert orderButton.text == "UTKÖRNING"
        print(orderButton.text)
        # Find order overlay by id
        overlay = driver.find_element_by_id("orderOverlay")
        assert overlay
        orderButton.click()
        assert overlay.get_attribute("data-state") == "visible"

        # Find input by id
        self.inputElement = driver.find_element_by_id("orderInput")
        # Find confirm button by id
        self.confirmButton = driver.find_element_by_id("orderConfirmButton")
        # Sets value of input to a zip code
        assert setValueAndCheck(self, "98139", driver) == True
        assert setValueAndCheck(self, "89488", driver) == False
