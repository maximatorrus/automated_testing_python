from model.group import Group


def test_edit_first_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.edit_first(Group(name="foo"))
    app.session.logout()
