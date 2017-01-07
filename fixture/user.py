from model.user import User


class UserHelper:
    def __init__(self, app):
        self.app = app

    def open_new_users_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_users_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and
                        len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img")) > 0):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys("%s" % text)

    def change_sel_value(self, field_name):
        wd = self.app.wd
        if field_name is not None:
            if not wd.find_element_by_xpath("%s" % field_name).is_selected():
                wd.find_element_by_xpath(field_name).click()

    def initialize_user(self, user):
        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("middlename", user.middlename)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("nickname", user.nickname)
        self.change_field_value("title", user.title)
        self.change_field_value("company", user.company)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.telephone)
        self.change_field_value("mobile", user.mobile)
        self.change_field_value("work", user.work)
        self.change_field_value("fax", user.fax)
        self.change_field_value("email", user.email_)
        self.change_field_value("email2", user.email2)
        self.change_field_value("email3", user.email3)
        self.change_field_value("homepage", user.homepage)
        # birthday & anniversary
        self.change_sel_value(user.bday)
        self.change_sel_value(user.bmonth)
        self.change_field_value("byear", user.byear)
        self.change_sel_value(user.aday)
        self.change_sel_value(user.amonth)
        self.change_field_value("ayear", user.ayear)

    def create(self, user):
        wd = self.app.wd
        self.open_new_users_page()
        # add new user
        self.initialize_user(user)
        # submit of add user
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.user_cache = None

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_user(self):
        self.select_user_by_index(0)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.open_users_page()
        self.select_user_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.user_cache = None

    def delete_first(self):
        self.delete_user_by_index(0)

    def edit_user_by_index(self, index, user):
        wd = self.app.wd
        self.open_users_page()
        self.select_user_by_index(index)
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.initialize_user(user)
        # submit updating
        wd.find_element_by_name("update").click()
        self.user_cache = None

    def edit_first(self, user):
        self.edit_user_by_index(0, user)

    def count(self):
        wd = self.app.wd
        self.open_users_page()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_users_page()
            self.user_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.user_cache.append(User(firstname=firstname, lastname=lastname, id=id))
        return list(self.user_cache)
