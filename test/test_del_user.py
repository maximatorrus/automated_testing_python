
def test_delete_first_user(app):
    app.session.login(user_name="admin", password="secret")
    app.user.delete_first()
    app.session.logout()
