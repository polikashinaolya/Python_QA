from model.group import Group
from random import randrange


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='test', header="testtest", footer="test1"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    # проверяем, что новый список групп стал короче
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
