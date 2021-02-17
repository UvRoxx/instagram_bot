from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException

DRIVER_PATH = "/Users/utkarshvarma/Dropbox/My Mac (UTKARSHs-MacBook-Pro.local)/Documents/Development/chromedriver"
LOGIN_URL = "https://www.instagram.com/"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(DRIVER_PATH)

    def login(self, user_id: str, password: str):
        self.driver.get(LOGIN_URL)
        sleep(4)
        login_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_input.send_keys(user_id)
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        print("LOGIN DONE")
        sleep(10)
        dismiss_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        dismiss_button.click()

    def find_followers(self, account_name):
        sleep(5)
        try:
            search_box = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
            search_box.send_keys(account_name)
            search_box.send_keys(Keys.ENTER)
            sleep(4)
            search_box.send_keys(Keys.ENTER)
            search_box.send_keys(Keys.ENTER)
            sleep(4)


        except:
            print("Exception Pass")

    def start_following(self):
        followers_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        sleep(4)
        buttons = self.driver.find_elements_by_tag_name("button")
        i = 0
        while True:
            for button in buttons:
                try:
                    if str(button.text) == "Follow":
                        try:
                            i += 1
                            button.click()
                            sleep(2)
                            print("Follow Done")
                            if i == 5:
                                self.driver.refresh()
                                self.start_following()
                            sleep(3)

                        except:
                            print("Exception While Hittting Follow")
                            pass
                except:
                    sleep(5)
                    print("Exception after ")
                    pass
            self.driver.refresh()
            self.start_following()
