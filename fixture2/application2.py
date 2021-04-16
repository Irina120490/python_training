from selenium import webdriver
from fixture2.session2 import SessionHelper2
from fixture2.contact import Contact

class Application2:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session2 = SessionHelper2(self)
        self.contact = Contact(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

