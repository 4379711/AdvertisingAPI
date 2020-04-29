# -*- coding:utf-8 -*-

import json

from . import bp_campaigns, bp_productAds, bp_bid, bp_keywords, bp_targets, bp_reports, bp_entitySnapshots, bp_ad_group
from flask import request, g, jsonify


@bp_campaigns.route("/get_campaign", methods=['POST'])
def get_campaign():
    params_data = request.get_json()
    campaign_id = params_data.get("campaign_id")
    response = g.current_object.get_campaign(campaign_id)
    return jsonify(response.json()), response.status_code


@bp_campaigns.route("/get_campaign_ex", methods=['POST'])
def get_campaign_ex():
    params_data = request.get_json() or {}
    campaign_id = params_data.get("campaign_id")
    response = g.current_object.get_campaign_ex(campaign_id)
    return jsonify(response.json()), response.status_code


@bp_campaigns.route("/create_campaigns", methods=['POST'])
def create_campaigns():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.create_campaigns(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.create_campaigns(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_campaigns.route("/update_campaigns", methods=['POST'])
def update_campaigns():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.update_campaigns(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.update_campaigns(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_campaigns.route("/archive_campaign", methods=['POST'])
def archive_campaign():
    params_data = request.get_json() or {}
    campaign_id = params_data.get("campaign_id")
    response = g.current_object.archive_campaign(campaign_id=campaign_id)
    return jsonify(response.json()), response.status_code


@bp_campaigns.route("/list_campaigns", methods=['POST'])
def list_campaigns():
    params_data = request.get_json() or {}

    startIndex = params_data.get("startIndex")
    count = params_data.get("count")
    stateFilter = params_data.get("stateFilter")
    name = params_data.get("name")
    portfolioIdFilter = params_data.get("portfolioIdFilter")
    campaignIdFilter = params_data.get("campaignIdFilter")
    response = g.current_object.list_campaigns(startIndex=startIndex, count=count,
                                               stateFilter=stateFilter, name=name,
                                               portfolioIdFilter=portfolioIdFilter,
                                               campaignIdFilter=campaignIdFilter)

    return jsonify(response.json()), response.status_code


@bp_campaigns.route("/list_campaigns_ex", methods=['POST'])
def list_campaigns_ex():
    params_data = request.get_json() or {}
    startIndex = params_data.get("startIndex")
    count = params_data.get("count")
    stateFilter = params_data.get("stateFilter")
    name = params_data.get("name")
    campaignIdFilter = params_data.get("campaignIdFilter")
    response = g.current_object.list_campaigns_ex(startIndex=startIndex, count=count,
                                                  stateFilter=stateFilter, name=name,
                                                  campaignIdFilter=campaignIdFilter)
    return jsonify(response.json()), response.status_code


@bp_ad_group.route("/get_ad_group", methods=['POST'])
def get_ad_group():
    params_data = request.get_json() or {}
    ad_group_id = params_data.get("ad_group_id")
    response = g.current_object.get_ad_group(ad_group_id=ad_group_id)
    return jsonify(response.json()), response.status_code


@bp_ad_group.route("/get_ad_group_ex", methods=['POST'])
def get_ad_group_ex():
    params_data = request.get_json() or {}
    ad_group_id = params_data.get("ad_group_id")
    response = g.current_object.get_ad_group_ex(ad_group_id=ad_group_id)
    return jsonify(response.json()), response.status_code


@bp_ad_group.route("/create_ad_groups", methods=['POST'])
def create_ad_groups():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.create_ad_groups(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.create_ad_groups(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_ad_group.route("/update_ad_groups", methods=['POST'])
def update_ad_groups():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.update_ad_groups(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.update_ad_groups(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_ad_group.route("/archive_ad_group", methods=['POST'])
def archive_ad_group():
    params_data = request.get_json() or {}
    ad_group_id = params_data.get("ad_group_id")
    response = g.current_object.archive_ad_group(ad_group_id=ad_group_id)
    return jsonify(response.json()), response.status_code


@bp_ad_group.route("/list_ad_groups", methods=['POST'])
def list_ad_groups():
    params_data = request.get_json() or {}
    campaign_id = params_data.get("campaign_id")
    name = params_data.get("name")
    state = params_data.get("state")
    default_bid = params_data.get("default_bid")
    all_data_list = params_data.get("all_data_list")
    response = g.current_object.list_ad_groups(campaign_id=campaign_id, name=name,
                                               state=state, default_bid=default_bid,
                                               all_data_list=all_data_list)
    return jsonify(response.json()), response.status_code


@bp_ad_group.route("/list_ad_groups_ex", methods=['POST'])
def list_ad_groups_ex():
    params_data = request.get_json() or {}
    startIndex = params_data.get("startIndex")
    count = params_data.get("count")
    stateFilter = params_data.get("stateFilter")
    name = params_data.get("name")
    adGroupIdFilter = params_data.get("adGroupIdFilter")
    campaignIdFilter = params_data.get("campaignIdFilter")
    response = g.current_object.list_ad_groups_ex(startIndex=startIndex, name=name,
                                                  count=count, stateFilter=stateFilter,
                                                  adGroupIdFilter=adGroupIdFilter, campaignIdFilter=campaignIdFilter)
    return jsonify(response.json()), response.status_code


@bp_productAds.route("/get_product_ad", methods=['POST'])
def get_product_ad():
    params_data = request.get_json() or {}
    ad_id = params_data.get("ad_id")
    response = g.current_object.get_product_ad(ad_id=ad_id)
    return jsonify(response.json()), response.status_code


@bp_productAds.route("/get_product_ad_ex", methods=['POST'])
def get_product_ad_ex():
    params_data = request.get_json() or {}
    ad_id = params_data.get("ad_id")
    response = g.current_object.get_product_ad_ex(ad_id=ad_id)
    return jsonify(response.json()), response.status_code


@bp_productAds.route("/create_product_ad", methods=['POST'])
def create_product_ad():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.create_product_ad(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.create_product_ad(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_productAds.route("/update_product_ad", methods=['POST'])
def update_product_ad():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.update_product_ad(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.update_product_ad(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_productAds.route("/archive_product_ad", methods=['POST'])
def archive_product_ad():
    params_data = request.get_json() or {}
    ad_id = params_data.get("ad_id")
    response = g.current_object.update_product_ad(ad_id=ad_id)
    return jsonify(response.json()), response.status_code


@bp_productAds.route("/list_product_ads", methods=['POST'])
def list_product_ads():
    params_data = request.get_json() or {}
    startIndex = params_data.get("startIndex")
    count = params_data.get("count")
    sku = params_data.get("sku")
    asin = params_data.get("asin")
    stateFilter = params_data.get("stateFilter")
    adGroupIdFilter = params_data.get("adGroupIdFilter")
    campaignIdFilter = params_data.get("campaignIdFilter")
    response = g.current_object.list_product_ads(startIndex=startIndex, count=count,
                                                 sku=sku, asin=asin, stateFilter=stateFilter,
                                                 adGroupIdFilter=adGroupIdFilter, campaignIdFilter=campaignIdFilter
                                                 )
    return jsonify(response.json()), response.status_code


@bp_productAds.route("/list_product_ads_ex", methods=['POST'])
def list_product_ads_ex():
    params_data = request.get_json() or {}
    startIndex = params_data.get("startIndex")
    count = params_data.get("count")
    sku = params_data.get("sku")
    asin = params_data.get("asin")
    stateFilter = params_data.get("stateFilter")
    adGroupIdFilter = params_data.get("adGroupIdFilter")
    campaignIdFilter = params_data.get("campaignIdFilter")
    response = g.current_object.list_product_ads_ex(startIndex=startIndex, count=count,
                                                    sku=sku, asin=asin, stateFilter=stateFilter,
                                                    adGroupIdFilter=adGroupIdFilter, campaignIdFilter=campaignIdFilter
                                                    )
    return jsonify(response.json()), response.status_code


@bp_bid.route("/get_bid_recommendations_for_ad_groups", methods=['POST'])
def get_bid_recommendations_for_ad_groups():
    params_data = request.get_json() or {}
    ad_group_id = params_data.get(" ad_group_id")
    response = g.current_object.get_bid_recommendations_for_ad_groups(ad_group_id=ad_group_id)
    return jsonify(response.json()), response.status_code


@bp_bid.route("/get_bid_recommendations_for_keywords", methods=['POST'])
def get_bid_recommendations_for_keywords():
    params_data = request.get_json() or {}
    keyword_id = params_data.get("keyword_id")
    response = g.current_object.get_bid_recommendations_for_keywords(keyword_id=keyword_id)
    return jsonify(response.json()), response.status_code


@bp_bid.route("/create_keywords_bid_recommendations", methods=['POST'])
def create_keywords_bid_recommendations():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.create_keywords_bid_recommendations(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.create_keywords_bid_recommendations(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_bid.route("/get_bid_recommendations", methods=['POST'])
def get_bid_recommendations():
    params_data = request.get_json() or {}
    ad_group = params_data.get("ad_group_id")
    match_type = params_data.get("match_type")
    match_value = params_data.get("g.current_object")
    response = g.current_object.get_bid_recommendations(ad_group=ad_group,
                                                        match_type=match_type,
                                                        match_value=match_value)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/get_biddable_keyword", methods=['POST'])
def get_biddable_keyword():
    params_data = request.get_json() or {}
    keyword_id = params_data.get(" keyword_id")
    response = g.current_object.get_biddable_keyword(keyword_id=keyword_id)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/get_biddable_keyword_ex", methods=['POST'])
def get_biddable_keyword_ex():
    params_data = request.get_json() or {}
    keyword_id = params_data.get(" keyword_id")
    response = g.current_object.get_biddable_keyword_ex(keyword_id=keyword_id)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/create_biddable_keyword", methods=['POST'])
def create_biddable_keywords():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.create_biddable_keywords(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.create_biddable_keywords(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_keywords.route("/update_biddable_keywords", methods=['POST'])
def update_biddable_keywords():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.update_biddable_keywords(**all_data)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/archived_biddable_keyword", methods=['POST'])
def archived_biddable_keyword():
    params_data = request.get_json() or {}
    keyword_id = params_data.get(" keyword_id")
    response = g.current_object.archived_biddable_keyword(keyword_id=keyword_id)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/list_biddable_keywords", methods=['POST'])
def list_biddable_keywords():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.list_biddable_keywords(**all_data)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/list_biddable_keywords_ex", methods=['POST'])
def list_biddable_keywords_ex():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.list_biddable_keywords_ex(**all_data)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/get_negative_keyword", methods=['POST'])
def get_negative_keyword():
    params_data = request.get_json() or {}
    keyword_id = params_data.get("keyword_id")
    response = g.current_object.get_negative_keyword(keyword_id=keyword_id)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/get_negative_keyword_ex", methods=['POST'])
def get_negative_keyword_ex():
    params_data = request.get_json() or {}
    keyword_id = params_data.get("keyword_id")
    response = g.current_object.get_negative_keyword_ex(keyword_id=keyword_id)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/create_negative_keywords", methods=['POST'])
def create_negative_keywords():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.create_negative_keywords(**all_data)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/update_negative_keywords", methods=['POST'])
def update_negative_keywords():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.update_negative_keywords(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.update_negative_keywords(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_keywords.route("/archive_negative_keyword", methods=['POST'])
def archive_negative_keyword():
    params_data = request.get_json() or {}
    keyword_id = params_data.get("keyword_id")
    response = g.current_object.archive_negative_keyword(keyword_id=keyword_id)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/list_negative_keywords", methods=['POST'])
def list_negative_keywords():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.list_negative_keywords(**all_data)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/list_negative_keywords_ex", methods=['POST'])
def list_negative_keywords_ex():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.list_negative_keywords_ex(**all_data)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/get_campaign_negative_keyword", methods=['POST'])
def get_campaign_negative_keyword():
    params_data = request.get_json() or {}
    keyword_id = params_data.get("keyword_id")
    response = g.current_object.get_campaign_negative_keyword(keyword_id=keyword_id)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/get_campaign_negative_keyword_ex", methods=['POST'])
def get_campaign_negative_keyword_ex():
    params_data = request.get_json() or {}
    keyword_id = params_data.get("keyword_id")
    response = g.current_object.get_campaign_negative_keyword_ex(keyword_id=keyword_id)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/create_campaign_negative_keywords", methods=['POST'])
def create_campaign_negative_keywords():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.create_campaign_negative_keywords(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.create_campaign_negative_keywords(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_keywords.route("/update_campaign_negative_keywords", methods=['POST'])
def update_campaign_negative_keywords():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.update_campaign_negative_keywords(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.update_campaign_negative_keywords(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_keywords.route("/delete_campaign_negative_keyword", methods=['POST'])
def delete_campaign_negative_keyword():
    params_data = request.get_json() or {}
    keyword_id = params_data.get(" keyword_id")
    response = g.current_object.update_campaign_negative_keywords(keyword_id=keyword_id)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/list_campaign_negative_keywords", methods=['POST'])
def list_campaign_negative_keywords():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.list_campaign_negative_keywords(**all_data)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/list_campaign_negative_keywords_ex", methods=['POST'])
def list_campaign_negative_keywords_ex():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.list_campaign_negative_keywords_ex(**all_data)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/get_ad_group_suggested_keywords", methods=['POST'])
def get_ad_group_suggested_keywords():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.get_ad_group_suggested_keywords(**all_data)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/get_ad_group_suggested_keywords_ex", methods=['POST'])
def get_ad_group_suggested_keywords_ex():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.get_ad_group_suggested_keywords_ex(**all_data)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/get_asin_suggested_keywords", methods=['POST'])
def get_asin_suggested_keywords():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.get_asin_suggested_keywords(**all_data)
    return jsonify(response.json()), response.status_code


@bp_keywords.route("/bulk_get_asin_suggested_keywords", methods=['POST'])
def bulk_get_asin_suggested_keywords():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.bulk_get_asin_suggested_keywords(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.bulk_get_asin_suggested_keywords(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_targets.route("/get_targeting_clause", methods=['POST'])
def get_targeting_clause():
    params_data = request.get_json() or {}
    target_id = params_data.get(" target_id")
    response = g.current_object.get_targeting_clause(target_id=target_id)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/get_targeting_clause_ex", methods=['POST'])
def get_targeting_clause_ex():
    params_data = request.get_json() or {}
    target_id = params_data.get(" target_id")
    response = g.current_object.get_targeting_clause_ex(target_id=target_id)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/list_targeting_clause", methods=['POST'])
def list_targeting_clause():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.list_targeting_clause(**all_data)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/list_targeting_clause_ex", methods=['POST'])
def list_targeting_clause_ex():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.list_targeting_clause_ex(**all_data)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/create_targeting_clause", methods=['POST'])
def create_targeting_clause():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.create_targeting_clause(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.create_targeting_clause(all_data_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_targets.route("/update_targeting_clause", methods=['POST'])
def update_targeting_clause():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.update_targeting_clause(**all_data)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/delete_targeting_clause", methods=['POST'])
def delete_targeting_clause():
    params_data = request.get_json() or {}
    target_id = params_data.get(" target_id")
    response = g.current_object.delete_targeting_clause(target_id=target_id)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/create_target_recommendations", methods=['POST'])
def create_target_recommendations():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.create_target_recommendations(**all_data)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/get_targeting_categories", methods=['POST'])
def get_targeting_categories():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.get_targeting_categories(**all_data)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/get_brand_recommendations", methods=['POST'])
def get_brand_recommendations():
    params_data = request.get_json() or {}
    all_data = dict(params_data)
    response = g.current_object.get_brand_recommendations(**all_data)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/get_negative_targeting_clause", methods=['POST'])
def get_negative_targeting_clause():
    params_data = request.get_json() or {}
    target_id = params_data.get("target_id")
    response = g.current_object.get_negative_targeting_clause(target_id=target_id)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/get_negative_targeting_clause_ex", methods=['POST'])
def get_negative_targeting_clause_ex():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    target_id = params_data.get("target_id")
    response = g.current_object.get_negative_targeting_clause_ex(target_id=target_id)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/create_negative_targeting_clauses", methods=['POST'])
def create_negative_targeting_clauses():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    response = g.current_object.create_negative_targeting_clauses(**params_data)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/update_negative_targeting_clauses", methods=['POST'])
def update_negative_targeting_clauses():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    response = g.current_object.update_negative_targeting_clauses(**params_data)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/list_negative_targeting_clauses", methods=['POST'])
def list_negative_targeting_clauses():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    response = g.current_object.list_negative_targeting_clauses(**params_data)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/list_negative_targeting_clauses_ex", methods=['POST'])
def list_negative_targeting_clauses_ex():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    response = g.current_object.list_negative_targeting_clauses(**params_data)
    return jsonify(response.json()), response.status_code


@bp_targets.route("/delete_negative_targeting_clause", methods=['POST'])
def delete_negative_targeting_clause():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    target_id = params_data.get("target_id")
    response = g.current_object.delete_negative_targeting_clause(target_id=target_id)
    return jsonify(response.json()), response.status_code


@bp_reports.route("/request_report", methods=['POST'])
def request_report():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    if isinstance(params_data, dict):
        response = g.current_object.request_report(**params_data)
        return jsonify(response.json()), response.status_code
    elif isinstance(params_data, list):
        response = g.current_object.request_report(metrics_list=params_data)
        return jsonify(response.json()), response.status_code


@bp_reports.route("/get_report", methods=['POST'])
def get_report():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    report_id = params_data.get("report_id")
    response = g.current_object.get_report(report_id=report_id)
    return jsonify(response.json()), response.status_code


@bp_entitySnapshots.route("/request_snapshot", methods=['POST'])
def request_snapshot():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    record_type = params_data.get("record_type")
    state_filter = params_data.get("state_filter")
    response = g.current_object.request_snapshot(record_type=record_type, state_filter=state_filter)
    return jsonify(response.json()), response.status_code


@bp_entitySnapshots.route("/get_snapshot_by_id", methods=['POST'])
def get_snapshot_by_id():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    snapshot_id = params_data.get(" snapshot_id")
    response = g.current_object.get_snapshot_by_id(snapshot_id=snapshot_id)
    return jsonify(response.json()), response.status_code


@bp_entitySnapshots.route("/download_snapshot_file", methods=['POST'])
def download_snapshot_file():
    params_data = request.get_data()
    params_data = json.loads(params_data.decode())
    url = params_data.get("url")
    response = g.current_object.download_snapshot_file(url=url)
    return jsonify(response.json()), response.status_code
