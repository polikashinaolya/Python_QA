# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Olya", middlename="asddas", lastname="fsdas", nickname="bnbdas",
                                   title="asdcvas", company="asdzxas", address="asqwdas", phone_home="123",
                                   phone_mobile="234", phone_work="345", fax="456", email="q@mail.ru",
                                   email2="s@", email3="3@", homepage="aerwe", address2="assdfsdfs",
                                   phone2="asdsdfdfas", notes="asqwqdas", bday="1", bmonth="January",
                                   byear="1001", aday="2", amonth="February", ayear="2002"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contacts_list()
    # проверяем, что длина списка групп стала короче
    assert len(old_contacts) - 1 == app.contact.count()
    # проверяем, что список контактов, измененный через программу совпадает со списком, изменненым через браузер
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
