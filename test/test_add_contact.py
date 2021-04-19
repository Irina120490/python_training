# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact_two(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact(Contact(firstname="Anna", middlename="Morozova", nickname="Ann",
                                     company="Yandex", address="Rubin st.", home="122222", mobile="123333",
                                     work="124444", fax="124563", email="Anna@mail.ru", email2="An@mail.ru",
                                     bday="12", bmonth="March", byear="1993", address2="kjgekg", phone2="654321",
                                     notes="rtyui"))
    app.session.logout

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact(Contact(firstname="Jonn", middlename="Smith", nickname="Jo", company="Google",
                                     address="Baker st.", home="1234567", mobile="1234565", work="1234545",
                                     fax="1234758", email="Jonn@mail.ru", email2="Jo@mail.ru", bday="1",
                                     bmonth="January", byear="1999", address2="asdfgh", phone2="123456", notes="jkl"))
    app.session.logout
