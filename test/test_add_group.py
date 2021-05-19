# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create_group(Group(name='test', header="testtest", footer="test1"))


def test_add_empty_group(app):
    app.group.create_group(Group(name='', header="", footer=""))


