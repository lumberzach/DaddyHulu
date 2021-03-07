# Daddyhulu
# Takes input URL and plays video


# Imports
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


# Chrome Options to save passwords to each platform
options = Options()


# Path to chrome profile
options.add_argument("user-data-dir=C:\\Users\\Boxca\\AppData\\Local\\Google\\Chrome\\profiletwo")
#options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(r"C:\Users\Boxca\Downloads\Drivers\chromedriver_win32 (1)\chromedriver.exe",
                          options=options)

# Play Function
def play(url):
    print(url)
    driver.get(url)
    time.sleep(3)
    try:
        driver.find_element_by_class_name('ytp-ad-skip-button-container')
        print("We've got an ad, lets skip it")
        time.sleep(3.5)
        driver.find_element_by_class_name('ytp-ad-skip-button-container').click()
    except NoSuchElementException:
        print("No ad, keep playing")
    actions = ActionChains(driver)
    actions.send_keys('f')
    actions.perform()



# Main Script
while True:
    url = input("What do you want to watch?\n")
    play(url)
    time.sleep(0)

