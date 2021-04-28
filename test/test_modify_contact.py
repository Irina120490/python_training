
from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Seckin"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="Setiner"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)