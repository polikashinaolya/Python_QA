
from random import randrange
import re


def test_contact_page_home_vs_edit(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_info_from_home_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.all_address == clear_whitespace(contact_from_edit_page.all_address)
    assert contact_from_home_page.all_email == contact_from_edit_page.all_email
    assert contact_from_home_page.all_phones == clear_characters(contact_from_edit_page.all_phones)


def clear_whitespace(something):
    return re.sub("\s+", " ", something)


def clear_characters(something):
    return re.sub("[-(!) ]", "", something)
