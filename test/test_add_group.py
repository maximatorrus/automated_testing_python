# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="group2", header="logo2", footer="comment2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


#def test_empty_group(app):
#    app.group.create(Group(name="", header="", footer=""))
