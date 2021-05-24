from model.group import Group


def test_edit_first_group(app):
    old_groups = app.group.get_groups_list()
    if app.group.count() == 0:
        app.group.create_group(Group(name='test', header="testtest", footer="test1"))
        old_groups = app.group.get_groups_list()
    app.group.edit_first(Group(name='Olya edit name'))
    new_groups = app.group.get_groups_list()
    # проверяем, что кол-во групп в списке не изменилось
    assert len(old_groups) == len(new_groups)