import mysql.connector
from DBConnection import dbconnection

class addressdao:

    def insertaddress(self,address):

        dbconn = dbconnection().getconnection()
        print(dbconn)

        cursor = dbconn.cursor()

        statement = '''insert into address(address_name) values(%s)'''

        cursor.execute(statement,address)

        dbconn.commit()

        cursor.close()

        dbconn.close()

    def selectaddresslist(self):

        dbconn = dbconnection().getconnection()
        print(dbconn)

        cursor = dbconn.cursor()

        statement = '''select * from address'''

        cursor.execute(statement)

        result = cursor.fetchall()
        print(result)

        cursor.close()

        dbconn.close()

#address = ['active']
#com = addressdao()
#com.insertaddress()
#com.selectaddresslist()
