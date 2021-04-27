# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group


class AddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(50)

    def test_add_new_group(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.create_group(driver, Group(name='test', header="testtest", footer="test1"))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def test_add_new_empty_group(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.create_group(driver, Group(name='', header="", footer=""))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def create_group(self, driver, group):
        # init new group
        driver.find_element_by_name("new").click()
        # fill form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit create group
        driver.find_element_by_name("submit").click()

    def open_groups_page(self, driver):
        driver.find_element_by_link_text("groups").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_homepage(self, driver):
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
