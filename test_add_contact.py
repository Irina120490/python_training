# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact_two(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd, Contact (firstname="Anna", middlename="Morozova", nickname="Ann",
                             company="Yandex", address="Rubin st.", home="122222", mobile="123333",
                             work="124444", fax="124563", email="Anna@mail.ru", email2="An@mail.ru",
                             bday="12", bmonth="March", byear="1993", address2="kjgekg", phone2="654321",
                             notes="rtyui"))
        self.logout(wd)
    
    def test_add_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd, Contact (firstname="Jonn", middlename="Smith", nickname="Jo", company="Google",
                             address="Baker st.", home="1234567", mobile="1234565", work="1234545",
                             fax="1234758", email="Jonn@mail.ru", email2="Jo@mail.ru", bday="1", bmonth="January",
                             byear="1999", address2="asdfgh", phone2="123456", notes="jkl"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_the_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def add_new_contact(self, wd, contactsgroup):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contactsgroup.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contactsgroup.middlename)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contactsgroup.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contactsgroup.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contactsgroup.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contactsgroup.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contactsgroup.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contactsgroup.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contactsgroup.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contactsgroup.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contactsgroup.email2)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contactsgroup.bday)
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contactsgroup.bmonth)
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contactsgroup.byear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contactsgroup.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contactsgroup.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contactsgroup.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
