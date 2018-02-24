import sqlite3
from MWMFlask.Main import app
from MWMFlask.utils.database.schema import schema as schema
from MWMFlask.utils.database.schema import test_users as users

database_uri = app.config["DATABASE_URI"]

db = sqlite3.connect(database_uri, check_same_thread=False)


def execute_query(qry, params=None):
    if params:
        cur = db.cursor()
        try:
            cur.execute(qry, params)
            db.commit()
        except sqlite3.Error as e:
            db.rollback()
            print("MySql Transaction error:\n" + str(e))
            return e
    else:
        cur = db.cursor()
        try:
            cur.execute(qry)
            db.commit()
        except sqlite3.Error as e:
            db.rollback()
            print("MySql Transaction error:\n" + str(e))
            return e


def get_rs(qry, params=None):
    if params:
        cur = db.cursor()
        try:
            cur.execute(qry, params)
            rs = cur.fetchall()
            if len(rs) == 1:
                rs = rs[0]
            db.commit()
            return rs
        except sqlite3.Error as e:
            db.rollback()
            print("MySql Transaction error:\n" + str(e))
            return e
    else:
        cur = db.cursor()
        try:
            cur.execute(qry)
            rs = cur.fetchall()
            db.commit()
            return rs
        except sqlite3.Error as e:
            db.rollback()
            print("MySql Transaction error:\n" + str(e))
            return e


def init_db():
    for qry in schema:
        execute_query(qry)


def load_db():
    for qry in users:
        execute_query(qry)


if __name__ == '__main__':
    init_db()
