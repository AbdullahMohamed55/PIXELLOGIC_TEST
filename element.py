from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        for element,val in zip(self.locator,value): 
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_name(element))
            driver.find_element_by_name(element).clear()
            driver.find_element_by_name(element).send_keys(val)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")