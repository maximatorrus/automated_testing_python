# -*- coding: utf-8 -*-
import pytest
from application import Application
from user import User


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    # app.open_home_page()
    app.login(user_name="admin", password="secret")
    app.open_add_new_page()
    app.add_new_user(User(firstname="First", middlename="Middle", lastname="Last", nickname="Nickname",
                      title="Title", company="Company", address="Address", telephone="telephone", mobile="mobile",
                      work="work", fax="fax", email_="email1", email2="email2", email3="email3",
                      homepage="homepage", byear="1991", ayear="2000",
                      bday="//div[@id='content']/form/select[1]//option[14]",
                      bmonth="//div[@id='content']/form/select[2]//option[7]",
                      aday="//div[@id='content']/form/select[3]//option[15]",
                      amonth="//div[@id='content']/form/select[4]//option[6]"))
    app.logout()


def test_add__empty_user(app):
    # app.open_home_page()
    app.login(user_name="admin", password="secret")
    app.open_add_new_page()
    app.add_new_user(User(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", telephone="",
                               mobile="",
                               work="", fax="", email_="", email2="", email3="",
                               homepage="", byear="", ayear="",
                               bday="//div[@id='content']/form/select[1]//option[1]",
                               bmonth="//div[@id='content']/form/select[2]//option[1]",
                               aday="//div[@id='content']/form/select[3]//option[1]",
                               amonth="//div[@id='content']/form/select[4]//option[1]"))
    app.logout()
