from model.group import Group


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first(Group(name='test', header="testtest", footer="test1"))
    app.session.logout()
