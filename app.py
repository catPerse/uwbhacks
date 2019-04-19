from flask import Flask
import pymysql
app = Flask(__name__)


class Database:
    def __init__(self):
        host = "uwbhacks.mysql.database.azure.com"
        user = "hacksadmin@uwbhacks"
        password = "UWBHacks**"
        db = "uwbhacks"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
