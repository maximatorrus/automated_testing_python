# -*- coding: utf-8 -*-
from model.user import User
import pytest
import random
import string


def test_add_user(app, json_users):
    user = json_users
    old_users = app.user.get_user_list()
    app.user.create(user)
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
