# -*- coding: utf-8 -*-
from flask import Blueprint

bp_campaigns = Blueprint("campaigns", __name__, url_prefix='/sp/campaigns/')
bp_ad_group = Blueprint("adGroups", __name__, url_prefix='/sp/adGroups/')
bp_productAds = Blueprint("productAds", __name__, url_prefix='/sp/productAds/')
bp_bid = Blueprint("bid", __name__, url_prefix='/sp/bid/')
bp_keywords = Blueprint("keywords", __name__, url_prefix='/sp/keywords/')
bp_targets = Blueprint("targets", __name__, url_prefix='/sp/targets/')
bp_reports = Blueprint("reports", __name__, url_prefix='/sp/reports/')
bp_entitySnapshots = Blueprint("entitySnapshots", __name__, url_prefix='/sp/entitySnapshots/')

from .views import *
from .get_object import *
