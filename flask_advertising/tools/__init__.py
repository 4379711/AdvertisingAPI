# -*- coding: utf-8 -*-

from flask import g

from flask_advertising.settings import ALL_TOKEN


def get_token(profile, country):
    key_str = str(profile) + str(country)
    access_token = ALL_TOKEN.get(key_str, '')
    return access_token


def add_token():
    token = g.current_object.access_token
    profile = g.current_object.profile_id
    country = g.current_object.region
    key_str = str(profile) + str(country)
    ALL_TOKEN.update({key_str: token})
