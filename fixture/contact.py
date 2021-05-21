
class ContactHelper:
    def __init__(self, app):
        self.app = app
   
    def open_create_contact_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def open_contact_page(self):
        driver = self.app.driver
        if driver.current_url is not 'http://localhost/addressbook/':
            driver.find_element_by_css_selector('div#nav a[href="./"]')

    def fill_form_contact(self, contact):
        driver = self.app.driver
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
        driver = self.app.driver
        self.open_create_contact_page()
        self.fill_form_contact(contact)
        self.confirm_add_contact()
        self.return_to_home_page()

    def confirm_add_contact(self):
        driver = self.app.driver
        driver.find_element_by_css_selector('input[type="submit"]').click()

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()

    def delete_first(self):
        driver = self.app.driver
        self.open_contact_page()
        driver.find_element_by_css_selector('input[name="selected[]"]').click()
        driver.find_element_by_css_selector('input[value="Delete"]').click()
        driver.switch_to_alert().accept()

    def edit_first(self, contact):
        driver = self.app.driver
        self.open_contact_page()
        driver.find_element_by_css_selector('img[title="Edit"]').click()
        self.fill_form_contact(contact)
        driver.find_element_by_name("update").click()
        self.return_to_home_page()

    def count(self):
        driver = self.app.driver
        return len(driver.find_elements_by_css_selector('input[name="selected[]"]'))



