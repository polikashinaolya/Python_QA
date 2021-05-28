from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    group_cache = None

    def open_groups_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith('/group.php') and len(driver.find_elements_by_name("new")) > 0):
            driver.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def create_group(self, group):
        self.open_groups_page()
        driver = self.app.driver
        # init new group
        driver.find_element_by_name("new").click()
        self.fill_form_group(group)
        # submit create group
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_form_group(self, group):
        driver = self.app.driver
        self.change_form_field("group_name", group.name)
        self.change_form_field("group_header", group.header)
        self.change_form_field("group_footer", group.footer)

    def change_form_field(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_first(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("edit").click()
        self.fill_form_group(group)
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))

    def get_groups_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_groups_page()
            self.group_cache = []
            for element in driver.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
