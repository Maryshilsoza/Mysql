import mysql.connector

class dbconnection:

    def getconnection(self):

        #create the connection
        dbconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yuwarani@97",
        database="project",
        )


        return dbconnection



#db=dbconnection()
#db.getconnection()
#print(db)
