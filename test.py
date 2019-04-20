from flask import Flask, render_template
import pymysql
app = Flask(__name__)

north = 1000
south = 1200



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

    def north(self):
        self.cur.execute("SELECT North_util FROM utilization ORDER BY Datetime DESC LIMIT 1")
        result = self.cur.fetchall()
        return result
    # @staticmethod
    # def db_length(self):
    #     db = Database()
    #     length = len(db.list_utilization())
    #     return length

    def south(self):
        self.cur.execute("SELECT South_util FROM utilization ORDER BY Datetime DESC LIMIT 1")
        result = self.cur.fetchall()
        return result


@app.route('/')
def utilization():
    def db_query():
        db = Database()
        util = db.list_utilization()
        north1 = db.north()
        south1 = db.south()
        return util, north1, south1
    res, sorted_north, sorted_south = db_query()
    print(sorted_north[0])
    return render_template("index.html", result=res, north=sorted_north,
                           south=sorted_south, n_percent=(north - sorted_north[0].get('North_util'))/north*100,
                           s_percent=(south - sorted_south[0].get('South_util'))/south*100)


if __name__ == '__main__':
    app.run()