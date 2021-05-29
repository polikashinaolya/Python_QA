from model.group import Group
from random import randrange

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='test', header="testtest", footer="test1"))
    old_groups = app.group.get_groups_list()
    group_test = Group(name='Olya edit name')
    group_test.id = old_groups[0].id
    index = randrange(len(old_groups))
    app.group.edit_by_index(index, group_test)
    # проверяем, что кол-во групп в списке не изменилось
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    # проверяем, что списки групп, измененные программно и через браузер, совпадают
    old_groups[0] = group_test
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
