# -*- coding:utf-8 -*-
__author__ = 'BlackIce'
import sqlite3


def create_db():
    """
    创建数据库
    :return:
    """
    conn = sqlite3.connect("output\\sign_in.db")
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE sign_in_table
    (name text, login text, logout text, ip add, week day)''')
    # Save (commit) the changes
    conn.commit()
    conn.close()


def write_db(data):
    conn = sqlite3.connect("output\\sign_in.db")
    c = conn.cursor()
    c.execute("INSERT INTO sign_in_table VALUES (?,?,?,?,?)", data)
