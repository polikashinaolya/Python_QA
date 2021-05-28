from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='test', header="testtest", footer="test1"))
    old_groups = app.group.get_groups_list()
    app.group.delete_first()
    new_groups = app.group.get_groups_list()
    # проверяем, что новый список групп стал короче
    assert len(old_groups) - 1 == app.group.count()
    old_groups[0:1] = []
    assert old_groups == new_groups
