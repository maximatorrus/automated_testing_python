# -*- coding: utf-8 -*-
from model.user import User
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    User(firstname=firstname, lastname=lastname, address=address, telephone=telephone, email_=email_)
    for firstname in ["", random_string("firstname", 10)]
    for lastname in ["", random_string("lastname", 10)]
    for address in ["", random_string("address", 10)]
    for telephone in ["", random_string("telephone", 10)]
    for email_ in ["", random_string("email_", 10)]
    ]


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, user):
    old_users = app.user.get_user_list()
    app.user.create(user)
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
