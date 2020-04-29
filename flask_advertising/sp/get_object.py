# -*- coding: utf-8 -*-
from flask_advertising.settings import SANDBOX
from . import bp_campaigns, bp_productAds, bp_bid, bp_keywords, bp_targets, bp_ad_group, bp_reports, bp_entitySnapshots
from flask import g
from Advertising.SponsoredProducts.sp_api import *


@bp_campaigns.before_request
def get_object():
    g.current_object = Campaigns(g.client_id,
                                 g.client_secret,
                                 g.access_token,
                                 g.refresh_token,
                                 g.country,
                                 profile_id=g.profile,
                                 sandbox=SANDBOX)


@bp_ad_group.before_request
def get_object():
    g.current_object = AdGroups(g.client_id,
                                g.client_secret,
                                g.access_token,
                                g.refresh_token,
                                g.country,
                                profile_id=g.profile,
                                sandbox=SANDBOX)


@bp_productAds.before_request
def get_object():
    g.current_object = ProductAds(g.client_id,
                                  g.client_secret,
                                  g.access_token,
                                  g.refresh_token,
                                  g.country,
                                  profile_id=g.profile,
                                  sandbox=SANDBOX)


@bp_bid.before_request
def get_object():
    g.current_object = Bid(g.client_id,
                           g.client_secret,
                           g.access_token,
                           g.refresh_token,
                           g.country,
                           profile_id=g.profile,
                           sandbox=SANDBOX)


@bp_keywords.before_request
def get_object():
    g.current_object = Keywords(g.client_id,
                                g.client_secret,
                                g.access_token,
                                g.refresh_token,
                                g.country,
                                profile_id=g.profile,
                                sandbox=SANDBOX)


@bp_targets.before_request
def get_object():
    g.current_object = Targets(g.client_id,
                               g.client_secret,
                               g.access_token,
                               g.refresh_token,
                               g.country,
                               profile_id=g.profile,
                               sandbox=SANDBOX)


@bp_entitySnapshots.before_request
def get_object():
    g.current_object = EntitySnapshots(g.client_id,
                                       g.client_secret,
                                       g.access_token,
                                       g.refresh_token,
                                       g.country,
                                       profile_id=g.profile,
                                       sandbox=SANDBOX)


@bp_reports.before_request
def get_object():
    g.current_object = Reports(g.client_id,
                               g.client_secret,
                               g.access_token,
                               g.refresh_token,
                               g.country,
                               profile_id=g.profile,
                               sandbox=SANDBOX)
