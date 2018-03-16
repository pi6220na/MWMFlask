import sqlite3
from MWMFlask.Main import app
from MWMFlask.utils.database.schema import schema as schema
from MWMFlask.utils.database.schema import test_users as users
from MWMFlask.models.places import type_strings

database_uri = app.config["DATABASE_URI"]

db = sqlite3.connect(database_uri, check_same_thread=False)


def execute_query(qry, params=None, custom_functions=None):
    if params:
        if custom_functions is not None:
            for f in custom_functions:
                db.create_function(f[0], f[1], f[2])
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


def get_rs(qry, params=None, custom_functions=None):
    if params:
        if custom_functions is not None:
            for f in custom_functions:
                db.create_function(f[0], f[1], f[2])
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
    type_qry = "INSERT INTO place_types (place_type) VALUES (?)"
    for t in type_strings:
        execute_query(type_qry, (t,))
