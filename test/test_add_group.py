# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups_list()
    app.group.create_group(Group(name='test', header="testtest", footer="test1"))
    new_groups = app.group.get_groups_list()
    #проверяем, что новый список групп стал длиннее
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_groups_list()
    app.group.create_group(Group(name='', header="", footer=""))
    new_groups = app.group.get_groups_list()
    # проверяем, что новый список групп стал длиннее
    assert len(old_groups) + 1 == len(new_groups)


