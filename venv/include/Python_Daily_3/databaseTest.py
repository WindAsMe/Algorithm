# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :databaseTest.py
# Location:/Home/PycharmProjects/..

import pymysql


# Insert a user
def employee_insert(db):
    cursor = db.cursor()
    firstName = input('输入用户姓:')
    lastName = input('输入用户名:')
    age = input('输入用户年龄:')
    sex = input('输入用户性别:')
    try:
        cursor.execute('INSERT INTO employee(first_name,last_name, age, sex)VALUES ("%s", "%s", "%s", "%s")' % \
                   (firstName, lastName, age, sex))
        db.commit()
    except:
        db.rollback()


# Find a/many user(s)
def employee_find(db):
    cursor = db.cursor()
    name = input('输入用户名:')
    # sql combination
    sql = "SELECT * FROM employee " \
          "WHERE first_name = '%s'" % name
    # print(sql)

    try:
        # print(name)
        cursor.execute(sql)
        # Find all result
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            print("fname=", fname, "lname=", lname,
                  "age=", age, "sex=", sex)
    except:
        print("Error: unable to fecth data")


# Update a/many user(s)
def employee_update(db):
    cursor = db.cursor()
    name = input('输入修改后用户名:')
    sql = "UPDATE employee " \
          "SET first_name = '%s'" \
          "WHERE sex = 'M' " % name
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


# Delete a/many user(s)
def employee_delete(db):
    cursor = db.cursor()
    name = input('需要删除的用户名:')
    sql = "DELETE FROM employee " \
          "WHERE first_name = '%s'" % name
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


if __name__ == '__main__':
    db = pymysql.connect("localhost", "root", "change123", "TESTDB", charset='utf8')
    mark = input('输入功能(1.插入, 2.查询, 3.修改, 4.删除)')
    if mark == '1':
        employee_insert(db)
    elif mark == '2':
        employee_find(db)
    elif mark == '3':
        employee_update(db)
    elif mark == '4':
        employee_delete(db)
    db.close()
