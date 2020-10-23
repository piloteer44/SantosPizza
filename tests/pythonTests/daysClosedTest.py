# Imports Selenium python module
from selenium import webdriver


class DaysClosedTest:

    def checkOrderClosedDates(self, month: int, date: int, expectedOrder: list):
        # Executes the JS reordering script with a custom month and date
        self.driver.execute_script(
            "reorderListByClosestDate(new Date(2020," + str(month - 1) + "," + str(date) + "))")
        # Gets the current sorted order from the classes closedDate
        websiteOrder = list(map(
            lambda date: date.text, self.driver.find_elements_by_class_name("closedDate")))
        # Asserts that the expected order and the website order is the same
        assert expectedOrder == websiteOrder
        print(str(date) + "/" + str(month) + " " + str(websiteOrder))

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

        print("")

        # Runs the function checkOrderClosedDates that reorders the list with the specified date and checks if it's sorted correctly
        self.checkOrderClosedDates(12, 24, ['24 december', '25 december',
                                            '26 december', '6 januari', '1 maj'])

        self.checkOrderClosedDates(12, 25, ['25 december', '26 december',
                                            '6 januari', '1 maj', '24 december'])

        self.checkOrderClosedDates(12, 26, ['26 december', '6 januari',
                                            '1 maj', '24 december', '25 december'])

        self.checkOrderClosedDates(12, 27, ['6 januari', '1 maj',
                                            '24 december', '25 december', '26 december'])

        self.checkOrderClosedDates(1, 6, ['6 januari', '1 maj',
                                          '24 december', '25 december', '26 december'])

        self.checkOrderClosedDates(1, 7, ['1 maj', '24 december',
                                          '25 december', '26 december', '6 januari'])

        self.checkOrderClosedDates(5, 1, ['1 maj', '24 december',
                                          '25 december', '26 december', '6 januari'])

        self.checkOrderClosedDates(5, 2, ['24 december', '25 december',
                                          '26 december', '6 januari', '1 maj'])
