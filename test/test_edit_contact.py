# -*- coding: utf-8 -*-

from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Olya", middlename="asddas", lastname="fsdas", nickname="bnbdas",
                                   title="asdcvas", company="asdzxas", address="asqwdas", phone_home="123",
                                   phone_mobile="234", phone_work="345", fax="456", email="q@mail.ru",
                                   email2="s@", email3="3@", homepage="aerwe", address2="assdfsdfs",
                                   phone2="asdsdfdfas", notes="asqwqdas", bday="1", bmonth="January",
                                   byear="1001", aday="2", amonth="February", ayear="2002"))
    app.contact.edit_first(Contact(firstname="MOlya", middlename="asddas", lastname="fsdas", nickname="bnbdas",
                               title="asdcvas", company="asdzxas", address="asqwdas", phone_home="123",
                               phone_mobile="234", phone_work="345", fax="456", email="q@mail.ru",
                               email2="s@", email3="3@", homepage="aerwe", address2="assdfsdfs",
                               phone2="asdsdfdfas", notes="asqwqdas", bday="3", bmonth="March",
                               byear="3003", aday="4", amonth="April", ayear="4004"))