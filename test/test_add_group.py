# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
    group_test = json_groups
    old_groups = app.group.get_groups_list()
    app.group.create_group(group_test)
    # проверяем, что новый список групп стал длиннее
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    #проверяем, что списки групп, добавленные программно и через браузер, совпадают
    old_groups.append(group_test)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


