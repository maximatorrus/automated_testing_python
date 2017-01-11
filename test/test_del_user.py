from model.user import User
import random


def test_delete_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.create(User(firstname="First", middlename="Middle", lastname="Last"))
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.delete_user_by_id(user.id)
    assert len(old_users) - 1 == len(db.get_user_list())
    old_users.remove(user)
    new_users = db.get_user_list()
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)

