from model.group import Group


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name='new', header="newnew", footer="new1"))
    app.session.logout()