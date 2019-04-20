from flask import Flask, render_template
import pymysql
app = Flask(__name__)

north = 1000
south = 1200
n_latest = 0
s_latest = 0
length = 0


class Database:
    def __init__(self):
        host = "uwbhacks.mysql.database.azure.com"
        user = "hacksadmin@uwbhacks"
        password = "UWBHacks**"
        db = "uwbhacks"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_utilization(self):
        self.cur.execute("SELECT * FROM utilization")
        result = self.cur.fetchall()
        return result


@app.route('/')
def utilization():
    def db_query():
        db = Database()
        util = db.list_utilization()
        return util
    res = db_query()
    return render_template("index.html", result=res)


if __name__ == '__main__':
    app.run()