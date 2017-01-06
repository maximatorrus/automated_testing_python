from model.user import User


def test_delete_first_user(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="First", middlename="Middle", lastname="Last", nickname="Nickname",
                             title="Title", company="Company", address="Address", telephone="telephone",
                             mobile="mobile",
                             work="work", fax="fax", email_="email1", email2="email2", email3="email3",
                             homepage="homepage", byear="1991", ayear="2000",
                             bday="//div[@id='content']/form/select[1]//option[14]",
                             bmonth="//div[@id='content']/form/select[2]//option[7]",
                             aday="//div[@id='content']/form/select[3]//option[15]",
                             amonth="//div[@id='content']/form/select[4]//option[6]"))
    app.user.delete_first()
