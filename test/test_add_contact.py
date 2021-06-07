# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import string
import random


def random_strint(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join([random.choice(symbol) for i in range(random.randrange(maxlen))])


def random_month():
    return random.choice(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                          'September', 'October', 'November', 'December'])


def random_phone_number():
    symbol_for_phone_number = string.digits + '+' + ' ' + '-'
    return ''.join([random.choice(symbol_for_phone_number) for i in range(16)])


testdata = [
    Contact(firstname=random_strint('firstname', 10), middlename=random_strint('', 10),
            lastname=random_strint('lastname', 10), nickname=random_strint('', 10), title=random_strint('', 10),
            company=random_strint('company', 10), address=random_strint('', 10), phone_home=random_phone_number(),
            phone_mobile=random_phone_number(), phone_work=random_phone_number(), fax=random_phone_number(),
            email=random_strint('email', 10), email2=random_strint('', 10), email3=random_strint('', 10),
            homepage=random_strint('', 10), address2=random_strint('', 10), phone2=random_phone_number(),
            notes=random_strint('', 10), bday=random.choice(range(31)), bmonth=random_month(),
            byear=random.choice(range(3000)), aday=random.choice(range(31)), amonth=random_month(),
            ayear=random.choice(range(3000)))
            for i in range(5)
            ]


@pytest.mark.parametrize("contact_test", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact_test):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact_test)
    # проверяем, что новый список групп стал длиннее
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    # проверяем, что списки контактов, добавленные программно и через браузер, совпадают
    old_contacts.append(contact_test)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
