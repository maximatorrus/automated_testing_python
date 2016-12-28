# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from user import User

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_user(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.open_add_new_page(wd)
        self.add_new_user(wd, User(firstname="First", middlename="Middle", lastname="Last", nickname="Nickname",
                          title="Title", company="Company", address="Address", telephone="telephone", mobile="mobile",
                          work="work", fax="fax", email_="email1", email2="email2", email3="email3",
                          homepage="homepage", byear="1991", ayear="2000",
                          bday="//div[@id='content']/form/select[1]//option[14]",
                          bmonth="//div[@id='content']/form/select[2]//option[7]",
                          aday="//div[@id='content']/form/select[3]//option[15]",
                          amonth="//div[@id='content']/form/select[4]//option[6]"))
        self.logout(wd)

    def test_add__empty_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.open_add_new_page(wd)
        self.add_new_user(wd, User(firstname="", middlename="", lastname="", nickname="",
                                   title="", company="", address="", telephone="",
                                   mobile="",
                                   work="", fax="", email_="", email2="", email3="",
                                   homepage="", byear="", ayear="",
                                   bday="//div[@id='content']/form/select[1]//option[1]",
                                   bmonth="//div[@id='content']/form/select[2]//option[1]",
                                   aday="//div[@id='content']/form/select[3]//option[1]",
                                   amonth="//div[@id='content']/form/select[4]//option[1]"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys("\\undefined")

    def add_new_user(self, wd, user):
        # adв new user
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % user.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("%s" % user.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % user.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("%s" % user.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("%s" % user.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("%s" % user.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % user.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("%s" % user.telephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("%s" % user.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("%s" % user.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("%s" % user.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("%s" % user.email_)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("%s" % user.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("%s" % user.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("%s" % user.homepage)
        # birthday & anniversary
        if not wd.find_element_by_xpath("%s" % user.bday).is_selected():
            wd.find_element_by_xpath(user.bday).click()
        if not wd.find_element_by_xpath("%s" % user.bmonth).is_selected():
            wd.find_element_by_xpath(user.bmonth).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("%s" % user.byear)
        if not wd.find_element_by_xpath("%s" % user.aday).is_selected():
            wd.find_element_by_xpath(user.aday).click()
        if not wd.find_element_by_xpath("%s" % user.amonth).is_selected():
            wd.find_element_by_xpath(user.amonth).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("%s" % user.ayear)
        # submit of add user
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_add_new_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, user_name, password):
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % user_name)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
