#!/usr/bin/env  python3
class AddrBookEntry(object):
    'address book entry class'
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print("Created instance for:",self.name,self.phone)

    def updatePhone(self,newph):
        self.phone = newph
        print("Updated hpne# for :",self.name)

john = AddrBookEntry('John Doe','408-555-1212')
print(john.name,john.phone)
john.updatePhone('19921024433')

class EmpAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry calss'
    def __init__(self,nm,ph,id,em):
        AddrBookEntry.__init__(self,nm,ph)
        self.empid = id
        self.email = em
    def updateEmail(self,newem):
        self.email = newem
        print("Updated e-mail address for:",self.name)

joy = EmpAddrBookEntry('John Gree','508-555-1212','tm','999@11.com')
print(joy.name,joy.phone,joy.empid,joy.email)
joy.updateEmail('444@126.com')