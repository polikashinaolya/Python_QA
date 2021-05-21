from time import sleep
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_homepage(self):
        driver = self.app.driver
        driver.get("http://localhost/addressbook/")

    def login(self, username, password):
        driver = self.app.driver
        self.open_homepage()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()
        sleep(15)

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in(driver):
            self.logout()

    def is_logged_in(self, driver):
        driver = self.app.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def ensure_login(self, username, password):
        driver = self.app.driver
        if self.is_logged_in(username):
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        driver = self.app.driver
        return driver.find_element_by_css_selector('form[name="logout"] b').text == '(%s)' % username