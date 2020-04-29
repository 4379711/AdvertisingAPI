# -*- coding:utf-8 -*-

from flask import Flask
from jinja2.utils import import_string

blueprints = (
    'flask_advertising.sp:bp_campaigns',
    'flask_advertising.sp:bp_productAds',
    'flask_advertising.sp:bp_bid',
    'flask_advertising.sp:bp_keywords',
    'flask_advertising.sp:bp_targets',
    'flask_advertising.sp:bp_reports',
    'flask_advertising.sp:bp_entitySnapshots',
    'flask_advertising.sp:bp_ad_group',

    'flask_advertising.pre_request:bp_pre_request',
)


def create_app():
    app = Flask(__name__)
    # app.config.from_object(config)

    # # Load extensions
    # mail.init_app(app)
    # db.init_app(app)

    # Load blueprints
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)

    return app


if __name__ == '__main__':
    application = create_app()
    application.run(host='0.0.0.0', port=4379, debug=False)
