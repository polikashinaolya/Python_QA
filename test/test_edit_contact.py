# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Olya", middlename="asddas", lastname="fsdas", nickname="bnbdas",
                                   title="asdcvas", company="asdzxas", address="asqwdas", phone_home="123",
                                   phone_mobile="234", phone_work="345", fax="456", email="q@mail.ru",
                                   email2="s@", email3="3@", homepage="aerwe", address2="assdfsdfs",
                                   phone2="asdsdfdfas", notes="asqwqdas", bday="1", bmonth="January",
                                   byear="1001", aday="2", amonth="February", ayear="2002"))
    old_contacts = app.contact.get_contacts_list()
    contacts_test = Contact(firstname="Olya edit name", phone_home="000000", bday="20", amonth="November")
    contacts_test.id = old_contacts[0].id
    index = randrange(len(old_contacts))
    app.contact.edit_by_index(index, contacts_test)
    new_contacts = app.contact.get_contacts_list()
    # проверяем, что длина списка групп не изменилась
    assert len(old_contacts) == app.contact.count()
    # проверяем, что списки групп, измененные программно и через браузер, совпадают
    old_contacts[0] = contacts_test
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)