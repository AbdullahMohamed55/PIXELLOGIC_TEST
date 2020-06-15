from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SetForumElements(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = [MainPageLocators.FIRSTNAME,
                MainPageLocators.LASTNAME,
                MainPageLocators.PHONE,
                MainPageLocators.EMAIL,
                MainPageLocators.PASSWORD,
                MainPageLocators.CONFIRMPASSWORD]


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    forumElement = SetForumElements()
    def login(self,usr,pswd):
        
        self.driver.get('https://www.phptravels.net/login')
        user = self.driver.find_element_by_name('username')
        user.send_keys(usr)
        passw = self.driver.find_element_by_name('password')
        passw.send_keys(pswd)
        time.sleep(2)

    def is_signed_up(self):
        """Verifies that user signed up correctly checking Hi in h3 """
        
        # print(*MainPageLocators.SIGNEDUP)
        # element = WebDriverWait(self.driver,10).until(
        # EC.presence_of_element_located(MainPageLocators.SIGNEDUP))
        element = self.driver.find_element(*MainPageLocators.SIGNEDUP)
        try:
            element = self.driver.find_element(*MainPageLocators.SIGNEDUP)
            if self.driver.title == 'My Account':
                # Check if login correct
                return "SignedUp"
            else:
                return self.checkErrorType()
        except: 
            return self.checkErrorType()
    

    def click_sign_up(self):
        """Triggers the sign up"""
       
        element = self.driver.find_element(*MainPageLocators.SIGNUP_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    def checkErrorType(self):
        try:
            element= self.driver.find_element_by_class_name(MainPageLocators.Error)
        except:
            return "Fill out the missing cell"
        return element.text

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source