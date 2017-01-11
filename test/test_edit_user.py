from model.user import User
import random


def test_edit_first_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.create(User(firstname="First", lastname="Last"))
    old_users = db.get_user_list()
    user = random.choice(old_users)
    old_users.remove(user)
    edit_user = User(firstname="Second", lastname="Second")
    edit_user.id = user.id
    old_users.append(edit_user)
    app.user.edit_user_by_id(user.id, edit_user)
    new_users = db.get_user_list()
    assert len(old_users) == len(new_users)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
    if check_ui:
        assert sorted(old_users, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)
