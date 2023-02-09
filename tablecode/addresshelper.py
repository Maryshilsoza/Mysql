from addressdao import addressdao
import csv

class addresshelper:

    def insertaddresslist(self):
        print('address list insert')

        company = addressdao()

        #addresscategory1 = ['active']
        #addresscategory2 = ['dissolved']
        #addresslist =[addresscategory1,addresscategory2]
        addresslist = self.readaddresscsv()

        for addresscategory in addresslist:
            company.insertaddress(addresscategory)

        company.selectaddresslist()


    def readaddresscsv(self):

        print('program started')

        f = open('address.csv','r')

        csvfile = csv.reader(f)

        return csvfile

com = addresshelper()
com.insertaddresslist()
