# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :shelveTest.py
# Location:/Home/PycharmProjects/..

import sys
import shelve


def store_person(db):
    """
    save person to database
    :param db: database
    :return:
    """
    pid = input('Enter id:')
    person = {'name': input('Enter name:'), 'age': input('Enter age:')}
    db[pid] = person

    
def find_person(db):
    field = input("Find person ID:")
    print("find out:", db[field])


if __name__ == '__main__':
    database = shelve.open('file.bat')
    while True:
        try:
            mark = input('Function:')
            if mark == '1':
                store_person(database)
            elif mark == '2':
                find_person(database)
            else:
                raise IOError
        finally:
            database.close()

