# PIXELLOGIC_TEST
This a selenium automation of testing a sign up forum of phptravel.net/

## How to run  
you need to install selenium

```
$ pip install selenium
```
then run the automation script

```
$ python main.py
```
## Hierarchy 
The code is **OOP** and the Hierarchy is as below :
1) ``` main.py``` 
I used **Python's testing framework** to test the signup forum also after each successful sign up the webdriver will log into the account to make sure it logs in correctly. 
Also Restarting the browser when error occur or crashes due to failures and other exceptions.

2) ``` page.py ```
The page object pattern intends creating an object for each web page. By following this technique a layer of separation between the test code and technical implementation is created.

3) ``` elements.py ```
This class handles where getting and setting values to boxes of the forums.

4) ``` locators.py```
Separating the locator strings from the place where they are being used. In this snippet, locators of the same page belong to same class. So **No hard coded elements**
<div align="center">
  <img src="https://i.imgur.com/BQ1gW0J.png">
</div>

## Testcases 
All the test cases are in file **testcase.csv**
where each row is like this :
<div align="center">
  <img src="https://i.imgur.com/SBH9Io6.png">
</div>
the smaple input and the expected output that we compare against.

## Report
The report as same as the Testcase file added to that the **actual output** and **reason** colomn.
<div align="center">
  <img src="https://i.imgur.com/xvzUTzh.png">
</div>
Each test case that failed **the Web Driver** took a screen shot of browser window and save it to Failedscreenhots folder with its name the number of the test case

## Notes
1) Change the path of the webdriver to the corresponding one on your system in ``` main.py ``` 
<div align="center">
  <img src="https://i.imgur.com/o6Stc4j.png">
</div>

2) Regarding the **HTTP interceptor** It's not supported in selenium python I was at a point I couldn't use another frame work because I had done a lot already.
