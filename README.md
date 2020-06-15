# PIXELLOGIC_TEST
This a selenium automation of testing a sign up forum of phptravel.net/

## Prerequisites 
you need to install selenium

```
$ pip install selenium
```
then run hte automation script

```
$ python main.py
```
## Hierarcchy 
The could is Fully **OOP** and the hierarchy is as below :
1) ``` main.py``` 
I used **Unit testing** to test the signup forum also after each successful sign up the webdriver will log into the account to make sure it logs in correctly. 
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



## Notes
1) Each test case that failed **the Web Driver** took a screen shot of browser window and save it in the folder with its name the number of the test case
2) Change the path of the webdriver to the corresponding one on your system in ``` main.py ``` 
<div align="center">
  <img src="https://i.imgur.com/o6Stc4j.png">
</div>

3) Regarding the **HTTP interceptor** I couldn't find a way to do it in python in selenium I was at a point I couldn't use another frame work because I had done a lot already.
