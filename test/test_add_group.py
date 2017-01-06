# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="group2", header="logo2", footer="comment2"))
    app.session.logout()


#def test_empty_group(app):
 #   app.group.create(Group(name="", header="", footer=""))
