
from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Seckin"))
    app.contact.modify_first_contact(Contact(firstname="Setiner"))
