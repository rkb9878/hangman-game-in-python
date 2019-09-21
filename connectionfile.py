from pymysql import *
class connectionfile:
    def connect(self):
        conn=Connect('127.0.0.1','root','','hangman')
        return conn