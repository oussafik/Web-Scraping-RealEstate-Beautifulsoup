import pymysql

class Dbconnect(object):
    def __init__(self):
        self.dbconection = pymysql.connect(host='localhost',port=3308, user='root',passwd='', db='realestate')
        self.dbcursor = self.dbconection.cursor()

    def commit_db(self):
        self.dbconection.commit()

    def close_db(self):
        self.dbcursor.close()
        self.dbconection.close()



