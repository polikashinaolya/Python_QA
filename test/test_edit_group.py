from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='test', header="testtest", footer="test1"))
    app.group.edit_first(Group(name='new', header="newnew", footer="new1"))