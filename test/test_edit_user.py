from model.user import User


def test_edit_first_user(app):
    app.user.edit_first(User(firstname="Second", middlename="Middle2", lastname="Last2", nickname="Nickname2",
                         title="Title2", company="Company2", address="Address", telephone="telephone", mobile="mobile2",
                         work="work2", fax="fax2", email_="email12", email2="email22", email3="email32",
                         homepage="homepage", byear="1991", ayear="2000",
                         bday="//div[@id='content']/form/select[1]//option[14]",
                         bmonth="//div[@id='content']/form/select[2]//option[7]",
                         aday="//div[@id='content']/form/select[3]//option[15]",
                         amonth="//div[@id='content']/form/select[4]//option[6]"))
