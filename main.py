import unittest
from selenium import webdriver
import page
import time 
import csv
import random
import string 
import sys
import os


class PHP_Travel_SignUp(unittest.TestCase):
    """A sample test class to show how page object works"""
    # PATH of the webdriver
    PATH = '/home/abdo/Documents/pixellogic/chromedriver'
    def setUp(self):
        
            
            # PATH = '/home/abdo/Documents/pixellogic/chromedriver'
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("https://www.phptravels.net/register")
        # load test cases from csv
        ############# TO DO #################


    def restart(self):
        
        # this restart the browser everytime it crashes 
        self.driver.close()
       
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("https://www.phptravels.net/register")


    def login(self,usr,pswd):
        self.driver.close()
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get('https://www.phptravels.net/login')
        user = self.driver.find_element_by_name('username')
        user.send_keys(usr)
        passw = self.driver.find_element_by_name('password')
        passw.send_keys(pswd)
        signup = self.driver.find_element_by_class_name('loginbtn')
        signup.click()
        time.sleep(3)
        if self.driver.title == "Login":
            return False
        else: 
            return True
    def generateRandomEmail(self):
        # Generating random emails to test with 

        extensions = ['com','net','org','gov']
        domains = ['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier']

        winext = extensions[random.randint(0,len(extensions)-1)]
        windom = domains[random.randint(0,len(domains)-1)]

        acclen = random.randint(1,20)

        winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

        finale = winacc + "@" + windom + "." + winext
        return finale

    def test_search_in_python_org(self):
        """
        Testing the sign up forum 

        """

        #Load the main page. In this case the home page of Python.org.
        report = []
        with open('testcase.csv') as csv_file:
            self.csv_reader = csv.reader(csv_file, delimiter=',')
            # IF ANYTHING CRASHES THE BROWSER WILL RESTART AND EVERTHING IS THE REPORT
            try:
                for i,row in enumerate(self.csv_reader):
                    
                    main_page = page.MainPage(self.driver)
                    if i == 0:
                        row.append('ouptut')
                        row.append('reason')
                        report.append(row)
                        continue;
                   
                    main_page.forumElement = row[0:6]
                    

                    main_page.click_sign_up()
                    time.sleep(3)
                    # if signed up  this what we want ?

                    result = main_page.is_signed_up()
                    if result == 'SignedUp':
                        if not self.login(row[3],row[4]):
                            result = "failed to login"
                            # print('login status ','nailed it' )

                    if (result == "SignedUp" and row[-1]=="NotSignUp") or ((result !='SignedUp' and row[-1]=='SignUp')):
                        row.append("Failed")
                        row.append(result)
                        report.append(row)
                        self.driver.save_screenshot("failedScreenshots/"+str(i)+".png")
                    elif (result != "SignedUp" and row[-1]=="NotSignUp") or (result == "SignedUp" and row[-1]=="SignUp"):
                        row.append('Passed')
                        row.append(result)
                        report.append(row)
                    self.restart()
            except Exception as e:
                print(e)                
                self.restart()

                # print(result,"  ",row[-2])
            
        # print(report)
        with open('report.csv','w') as csv_file:
            self.writer = csv.writer(csv_file, delimiter=',')
            self.writer.writerows(report)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":

    unittest.main()