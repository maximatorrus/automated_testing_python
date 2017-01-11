# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app, db, data_users, check_ui):
    user = data_users
    old_users = db.get_user_list()
    app.user.create(user)
    new_users = db.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)
