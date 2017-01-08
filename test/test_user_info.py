import re
from random import randrange


def test_all_info(app):
    users = app.user.get_user_list()
    index = randrange(len(users))
    user_from_home_page = app.user.get_user_list()[index]
    user_from_edit_page = app.user.get_user_info_from_edit_page(index)
    assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.firstname == user_from_edit_page.firstname
    assert user_from_home_page.lastname == user_from_edit_page.lastname
    assert user_from_home_page.address == user_from_edit_page.address


def test_phones_on_user_view_page(app):
    user_from_view_page = app.user.get_user_from_view_page(0)
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_view_page.telephone == user_from_edit_page.telephone
    assert user_from_view_page.mobile == user_from_edit_page.mobile
    assert user_from_view_page.work == user_from_edit_page.work
    assert user_from_view_page.secondaryphone == user_from_edit_page.secondaryphone


def clear(str):
    return re.sub("[() -]", "", str)


def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [user.telephone, user.mobile, user.work,
                                                            user.secondaryphone]))))


def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [user.email_, user.email2, user.email3])))
