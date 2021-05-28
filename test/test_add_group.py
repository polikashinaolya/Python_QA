# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups_list()
    group_test = Group(name='test', header="testtest", footer="test1")
    app.group.create_group(group_test)
    new_groups = app.group.get_groups_list()
    #проверяем, что новый список групп стал длиннее
    assert len(old_groups) + 1 == len(new_groups)
    #проверяем, что списки групп, добавленные программно и через браузер, совпадают
    old_groups.append(group_test)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




def test_add_empty_group(app):
    old_groups = app.group.get_groups_list()
    group_test = Group(name='test', header="testtest", footer="test1")
    app.group.create_group(group_test)
    new_groups = app.group.get_groups_list()
    #проверяем, что новый список групп стал длиннее
    assert len(old_groups) + 1 == app.group.count()
    # проверяем, что списки групп, добавленные программно и через браузер, совпадают
    old_groups.append(group_test)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


