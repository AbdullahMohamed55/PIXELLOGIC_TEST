from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SIGNUP_BUTTON = (By.CLASS_NAME, "signupbtn")
    SIGNEDUP = (By.TAG_NAME,"h3")
    FIRSTNAME = "firstname"
    LASTNAME = "lastname"
    PASSWORD = "password"
    PHONE = "phone"
    EMAIL = "email"
    CONFIRMPASSWORD = "confirmpassword"
    Error = "alert"

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass