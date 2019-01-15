#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      :
# @File      : __init__.py.py
# @Time      : 2019/1/09 17:06
# @software  : PyCharm

from weather import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # uid = db.Column(db.String(30), n)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<City {}>'.format(self.name)
