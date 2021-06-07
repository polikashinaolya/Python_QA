# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import string
import random


def random_strint(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + ' '*10  #пока убрала string.punctuation чтобы тесты не падали
    return prefix + ''.join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Group(name='', header='', footer='')] + [
    Group(name=random_strint('name', 10), header=random_strint('header', 20), footer=random_strint('footer', 20))
    for i in range(5)
]


@pytest.mark.parametrize("group_test", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group_test):
    old_groups = app.group.get_groups_list()
    app.group.create_group(group_test)
    # проверяем, что новый список групп стал длиннее
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    #проверяем, что списки групп, добавленные программно и через браузер, совпадают
    old_groups.append(group_test)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


