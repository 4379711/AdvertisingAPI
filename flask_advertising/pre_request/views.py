# -*- coding: utf-8 -*-

from flask_advertising.tools import get_token, add_token
from . import bp_pre_request
from flask import request, g
from flask import jsonify


@bp_pre_request.route('/help', methods=['POST', 'GET'])
def index():
    return jsonify(message="Here is the advertising API .If you have any questions, please see the documentation!")


@bp_pre_request.before_app_request
def pre_request_():
    _headers = dict(request.headers)
    required_parameters = ('Client-Id', 'Client-Secret', 'Refresh-Token', 'Profile-Id')
    for key_ in required_parameters:
        if key_ not in _headers.keys():
            return jsonify(message=f'You must put {key_} in headers !'), 800

    g.client_id = _headers.get('Client-Id')
    g.client_secret = _headers.get('Client-Secret')
    g.refresh_token = _headers.get('Refresh-Token')
    g.profile = _headers.get('Profile-Id')
    g.country = _headers.get('Country', 'US')
    # g.access_token = _headers.get('Access-Token', '')
    g.access_token = get_token(g.profile, g.country)


@bp_pre_request.app_errorhandler(Exception)
def error_(error):
    if isinstance(error, AttributeError):
        error = 'May be missing parameters !'
        return f"An error occurred !\n{error}", 801
    return f"An error occurred !\n{error}", 802


@bp_pre_request.teardown_app_request
def update_token(resp):
    add_token()
    return resp
