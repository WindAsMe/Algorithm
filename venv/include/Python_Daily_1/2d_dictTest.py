# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-5-13 下午4:47
# File     :2d_dictTest.py
# Location:/Home/PycharmProjects/..


def add_dict(peoples, name, phone, addr):
    # 2D dictionary
    # Add member
    if name in peoples:
        # Name exist in peoples
        # Modified addr and phone by name
        peoples[name].update({'addr': addr, 'phone': phone})
    else:
        # Name disappear in peoples
        # Directly insert
        peoples.update({name: ({'addr': addr, 'phone': phone})})


def get_dict(peoples):
    # 2D dictionary get all member
    # In dictionary, NO CERTAIN ORDER!!!!
    # Different with list
    pond = ['phone', 'addr']
    # 通过item迭代
    for key, value in peoples.items():
        print('name:', key)
        i = 0
        for key_2, value_2 in value.items():
            print(pond[i], value_2)
            i += 1


def get_index(peoples, need_find, mark):
    # Get index
    # Input name
    if mark == 'n':
        i = 0
        for key, value in peoples.items():
            i += 1
            if key == need_find:
                print("下标是:", i)
    # Input address
    if mark == 'a':
        for key, value in peoples.items():
            if need_find == value['addr']:
                print("姓名为:", key)
    # Input telephone
    if mark == 'p':
        for key, value in peoples.items():
            if need_find == value['phone']:
                print("姓名为:", key)


def get_name(peoples, name):
    # Get name->information
    for key, value in peoples.items():
        if name == key:
            # peoples[name] == key
            print('Address:', peoples[name]['addr'])
            print('phone:', peoples[name]['phone'])

# Batch Inserts
# If lists have same length:
# Combination
# Or print ERROR
def batch_dict(peoples, names, addrs, phones):
    # list长度一致
    if len(names) == len(addrs) == len(phones):
        i = 0
        for name in names:
            # name 在people字典中
            if name in peoples:
                peoples[name].update({'addr': addrs[i], 'phone': phones[i]})
                i += 1
            else:
                peoples.update({name: ({'addr': addrs[i], 'phone': phones[i]})})
                i += 1

    else:
        print("error")


def init(peoples):
    # Initial dictionary
    peoples['Alice'] = {'addr': 'avenue', 'phone': '1231'}
    peoples['Beth'] = {'addr': 'London', 'phone': '2213'}
    peoples['Cecil'] = {'addr': 'America', 'phone': '3313'}


# people = {
#   'Alice': {
#       'addr': 'avenue',
#       'phone': '1231'
#   },
#   'Beth': {
#       'addr': 'London',
#       'phone': '2213'
#   },
#   'Cecil': {
#       'addr': 'America',
#       'phone': '3313'
#   }



