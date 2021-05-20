from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from time import sleep


class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            #self.driver.current_url() ПРИ ТАКОМ ВАРИАНТЕ НЕ РАБОТАЕТ ПРОВЕРКА, БРАУЗЕР БРОСАЕТСЯ
            self.driver.get("http://localhost/addressbook/")
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()
