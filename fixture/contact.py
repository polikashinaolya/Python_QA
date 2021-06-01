from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    contact_cache = None
   
    def open_create_contact_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith('addressbook/edit.php') and len(driver.find_elements_by_css_selector('input[name="photo"]')) > 0):
            driver.find_element_by_link_text("add new").click()

    def open_contact_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith('/addressbook/') and len(driver.find_elements_by_name("Send e-Mail")) > 0):
            driver.find_element_by_css_selector('div#nav a[href="./"]').click()

    def fill_form_contact(self, contact):
        self.change_field_form_string("firstname", contact.firstname)
        self.change_field_form_string("middlename", contact.middlename)
        self.change_field_form_string("lastname", contact.lastname)
        self.change_field_form_string("nickname", contact.nickname)
        self.change_field_form_string("title", contact.title)
        self.change_field_form_string("company", contact.company)
        self.change_field_form_string("address", contact.address)
        self.change_field_form_string("home", contact.phone_home)
        self.change_field_form_string("mobile", contact.phone_mobile)
        self.change_field_form_string("work", contact.phone_work)
        self.change_field_form_string("fax", contact.fax)
        self.change_field_form_string("email", contact.email)
        self.change_field_form_string("email2", contact.email2)
        self.change_field_form_string("email3", contact.email3)
        self.change_field_form_string("homepage", contact.homepage)
        self.change_field_form_string("address2", contact.address2)
        self.change_field_form_string("phone2", contact.phone2)
        self.change_field_form_string("notes", contact.notes)
        # добавляем даты
        self.change_field_form_date("bday", contact.bday)
        self.change_field_form_date("bmonth", contact.bmonth)
        self.change_field_form_string("byear", contact.byear)
        #добавлякм вторые даты
        self.change_field_form_date("aday", contact.aday)
        self.change_field_form_date("amonth", contact.amonth)
        self.change_field_form_string("ayear", contact.ayear)

    def change_field_form_string(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def change_field_form_date(self, field_name, date):
        driver = self.app.driver
        if date is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).send_keys(date)

    def create(self, contact):
        self.open_create_contact_page()
        self.fill_form_contact(contact)
        self.confirm_add_contact()
        self.return_to_home_page()
        self.contact_cache = None

    def confirm_add_contact(self):
        driver = self.app.driver
        driver.find_element_by_css_selector('input[type="submit"]').click()

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        driver = self.app.driver
        self.open_contact_page()
        driver.find_elements_by_css_selector('input[name="selected[]"]')[index].click()
        driver.find_element_by_css_selector('input[value="Delete"]').click()
        driver.switch_to_alert().accept()
        self.contact_cache = None
        print('был удален контакт с индексом %s' % index)

    def edit_first(self, contact):
        self.edit_by_index(0, contact)

    def edit_by_index(self, index, contact):
        driver = self.app.driver
        self.open_edit_page_by_index(index)
        self.fill_form_contact(contact)
        driver.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None
        print('был отредактирован контакт с индексом %s' % index)

    def open_edit_page_by_index(self, index):
        driver = self.app.driver
        self.open_contact_page()
        driver.find_elements_by_css_selector('img[title="Edit"]')[index].click()

    def count(self):
        driver = self.app.driver
        self.open_contact_page()
        return len(driver.find_elements_by_css_selector('input[name="selected[]"]'))

    def get_contacts_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_contact_page()
            self.contact_cache = []
            for index in range(self.count()):
                self.contact_cache.append(Contact(id=self.get_contact_info_from_home_page(index).id,
                                                  lastname=self.get_contact_info_from_home_page(index).lastname,
                                                  firstname=self.get_contact_info_from_home_page(index).firstname))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_edit_page_by_index(index)
        id = driver.find_element_by_name("id").get_attribute('value')
        firstname = driver.find_element_by_name("firstname").get_attribute('value')
        lastname = driver.find_element_by_name("lastname").get_attribute('value')
        address = driver.find_element_by_name("address").get_attribute('value')
        email = driver.find_element_by_name("email").get_attribute('value')
        email2 = driver.find_element_by_name("email2").get_attribute('value')
        email3 = driver.find_element_by_name("email3").get_attribute('value')
        phone_home = driver.find_element_by_name("home").get_attribute('value')
        phone_mobile = driver.find_element_by_name("mobile").get_attribute('value')
        phone_work = driver.find_element_by_name("work").get_attribute('value')
        phone2 = driver.find_element_by_name("phone2").get_attribute('value')
        all_email = ''.join([email,  email2,  email3])
        all_phones = ''.join([phone_home,  phone_mobile, phone_work, phone2])
        return Contact(id=id, firstname=firstname, lastname=lastname, all_address=address, all_email=all_email, all_phones=all_phones)

    def get_contact_info_from_home_page(self, index):
        driver = self.app.driver
        self.open_contact_page()
        contact_info = driver.find_elements_by_css_selector('table#maintable tr[name="entry"]')[index]
        id = contact_info.find_element_by_name("selected[]").get_attribute('value')
        [lastname, firstname,  all_address, all_email, all_phones] = map(lambda x: re.sub("\n", '', x),
        [contact_info.find_elements_by_css_selector('td')[1].text,
        contact_info.find_elements_by_css_selector('td')[2].text,
        contact_info.find_elements_by_css_selector('td')[3].text,
        contact_info.find_elements_by_css_selector('td')[4].text,
        contact_info.find_elements_by_css_selector('td')[5].text])
        return Contact(id=id, firstname=firstname, lastname=lastname, all_address=all_address, all_email=all_email,
                       all_phones=all_phones)