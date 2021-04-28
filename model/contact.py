
class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, company=None, address=None, home=None,
                 mobile=None, work=None, fax=None, email=None, email2=None, bday=None, bmonth=None, byear=None,
                 address2=None, phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname