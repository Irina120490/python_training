
from model.contact import Contact

def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(firstname="Anf", middlename="MEdhdk", nickname="And",
                                     company="Gjdm", address="Volkova st.", home="0000", mobile="11111",
                                     work="22222", fax="33333", email="Opth@mail.ru", email2="gmdlf@mail.ru",
                                     bday="15", bmonth="April", byear="1995", address2="vlfllfl", phone2="99999",
                                     notes="rflkl"))
    app.session.logout()
