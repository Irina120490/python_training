
from model.contact import Contact

def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Eng", middlename="Seckin", nickname="Ool"))
    app.session.logout()