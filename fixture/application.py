from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from time import sleep


class Application:
    def __init__(self, browser, baseUrl):
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.baseUrl = baseUrl

    def is_valid(self):
        try:
            #self.driver.current_url()
            self.driver.get("http://localhost/addressbook/")
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()
