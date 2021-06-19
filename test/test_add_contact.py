# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact_test = json_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact_test)
    # проверяем, что новый список групп стал длиннее
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    # проверяем, что списки контактов, добавленные программно и через браузер, совпадают
    old_contacts.append(contact_test)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
