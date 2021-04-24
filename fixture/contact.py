
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add_new").click()
        self.fill_contact_form(contact, wd)
        wd.find_element_by_name("submit").click()
        self.return_to_the_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("contact_firstname", contact.firstname)
        self.change_field_value("contact_middlename", contact.middlename)
        self.change_field_value("contact_nickname", contact.nickname)
        self.change_field_value("contact_company", contact.company)
        self.change_field_value("contact_address", contact.address)
        self.change_field_value("contact_home", contact.home)
        self.change_field_value("contact_mobile", contact.mobile)
        self.change_field_value("contact_work", contact.work)
        self.change_field_value("contact_fax", contact.fax)
        self.change_field_value("contact_email", contact.email)
        self.change_field_value("contact_email2", contact.email2)
        self.change_field_value("contact_bday", contact.bday)
        self.change_field_value("contact_bmonth", contact.bmonth)
        self.change_field_value("contact_byear", contact.byear)
        self.change_field_value("contact_address2", contact.address2)
        self.change_field_value("contact_phone2", contact.phone2)
        self.change_field_value("contact_notes", contact.notes)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_the_home_page()

    def return_to_the_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()