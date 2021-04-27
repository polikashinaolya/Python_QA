# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact_str
from time import sleep


class Add_Contact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_new_cont(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, username="admin", password="secret")
        self.open_create_contact_page(driver)
        self.contact_fill_form_str(driver, Contact_str(firstname="Olya", middlename= "asddas", lastname="fsdas", nickname="bnbdas",
                                                       title="asdcvas", company="asdzxas", address="asqwdas", home="123",
                                                       mobile="234", work="345", fax="456", email="q@mail.ru",
                                                       email2="s@", email3="3@", homepage="aerwe", address2="assdfsdfs",
                                                       phone2="asdsdfdfas", notes="asqwqdas"))
        self.contact_fill_form_bday(driver)
        #self.contact_fill_form_picture()
        sleep(5)
        self.confirm_add_contact(driver)
        sleep(5)
        self.finish_add_contact(driver)

    def finish_add_contact(self, driver):
        #return home page
        driver.find_element_by_link_text("home page").click()
        #logout
        driver.find_element_by_link_text("Logout").click()

    def confirm_add_contact(self, driver):
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def contact_fill_form_bday(self, driver):
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("1")
        driver.find_element_by_xpath("//option[@value='1']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("January")
        driver.find_element_by_xpath("//option[@value='January']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1001")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("2")
        driver.find_element_by_xpath("(//option[@value='2'])[2]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("February")
        driver.find_element_by_xpath("(//option[@value='February'])[2]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("2002")

    def contact_fill_form_str(self, driver, Contact_str):
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(Contact_str.firstname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(Contact_str.middlename)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(Contact_str.lastname)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(Contact_str.nickname)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(Contact_str.title)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(Contact_str.company)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(Contact_str.address)
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(Contact_str.home)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(Contact_str.mobile)
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(Contact_str.work)
        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(Contact_str.fax)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(Contact_str.email)
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(Contact_str.email2)
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(Contact_str.email3)
        driver.find_element_by_name("homepage").click()
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(Contact_str.homepage)
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(Contact_str.address2)
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(Contact_str.phone2)
        driver.find_element_by_name("notes").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(Contact_str.notes)

    def contact_fill_form_picture(self, driver):
        driver = self.driver
        driver.get("http://localhost/addressbook/edit.php")
        driver.find_element_by_name("photo").click()
        driver.find_element_by_name("photo").clear()
        driver.find_element_by_name("photo").send_keys("C:\\fakepath\\2020-01-20_18-35-30.png")


    def open_create_contact_page(self, driver):
        driver.find_element_by_link_text("add new").click()

    def open_homepage(self, driver):
        driver.get("http://localhost/addressbook/")

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
