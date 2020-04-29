# -*- coding: utf-8 -*-
import gzip
import json

from Advertising.Account import SbClient
from Advertising.utils import MyTypeAssert


class Brands(SbClient):

    def get_brands(self):
        interface = 'brands'
        return self.make_request(interface)


class Campaigns(SbClient):

    def get_campaign(self, **params):

        interface = 'sb/campaigns/'

        data = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'stateFilter': params.get('stateFilter'),
            'name': params.get('name'),
            'portfolioIdFilter': params.get('portfolioIdFilter'),
            'campaignIdFilter': params.get('campaignIdFilter'),
        }
        data.update(params)
        return self.make_request(interface, payload=data)

    def get_campaign_ex(self, campaign_id):
        interface = 'sb/campaigns/{campaign_id}'.format(campaign_id=campaign_id)
        return self.make_request(interface)

    def create_campaigns(self, budget, name, brand_entityid, portfolio_id,
                         state, budget_type, start_date, end_date,
                         bid_multiplier, bid_optimization, creative, landing_page,
                         all_data_list=None, **params):
        '''
        :param budget:
        :param name:
        :param brand_entityid:
        :param portfolio_id:
        :param state:
        :param budget_type:
        :param start_date:
        :param end_date:
        :param bid_multiplier:
        :param bid_optimization:
        :param creative: {
              "brandName": "string",
              "brandLogoAssetID": "string",
              "headline": "string",
              "asins": [
                "string"
              ],
              "shouldOptimizeAsins": false
        }
        :param landing_page:
        :param all_data_list:
        :param params: must have one of [
        {
            "keywords": [{
            "keywordText": "string",
            "matchType": one of [broad, exact, phrase],
            "bid": 0
            }],
            "negativeKeywords": [{
            "keywordText": "string",
            "matchType": one of [negativeExact, negativePhrase]
            }]
        },
        {
            "expressions": [{
                "expression": {
                      "type": one of [asinCategorySameAs, asinBrandSameAs, asinPriceLessThan, asinPriceBetween,
                            asinPriceGreaterThan, asinReviewRatingLessThan, asinReviewRatingBetween,
                            asinReviewRatingGreaterThan, asinSameAs],
                      "value": "string"
                },
                "matchType": one of ['broad', 'exact', 'phrase'],
                "bid": 0
            }],
            "negativeExpressions": [{
                "expression": {
                      "type": one of ['asinBrandSameAs', 'asinSameAs'],
                      "value": "string"
                },
                "matchType": one of ['negativeExact', 'negativePhrase'],
                "bid": 0
            }]
        }]
        :return:
        '''
        interface = 'sb/campaigns'
        if all_data_list is not None:
            MyTypeAssert.other_assert(all_data_list, types=list)
            return self.make_request(interface, method='POST', payload=all_data_list)
        MyTypeAssert.number_assert(budget)
        MyTypeAssert.number_assert(portfolio_id)
        assert len(start_date) == 8
        assert len(end_date) == 8
        assert budget_type in ["lifetime", "daily"]
        assert state in ["enabled", "paused", "archived"]
        assert bid_optimization in [True, False]
        assert -99 <= bid_multiplier <= 99
        MyTypeAssert.other_assert(creative, types=dict)
        MyTypeAssert.other_assert(landing_page, types=dict)

        data = [{
            "name": name,
            "budget": budget,
            "budgetType": budget_type,
            "startDate": start_date,
            "endDate": end_date,
            "state": state,
            "brandEntityId": brand_entityid,
            "bidOptimization": bid_optimization,
            "bidMultiplier": bid_multiplier,
            "portfolioId": portfolio_id,
            'creative': creative,
        }]
        data[0].update(params)
        return self.make_request(interface, method='POST', payload=data)

    def update_campaigns(self, campaign_id, all_data_list=None, **params):
        '''

        :param campaign_id:
        :param portfolio_id:
        :param all_data_list:
        :param params: must some of {
                "name": "string",
                "budget": 0,
                "endDate": "string",
                "state": "enabled",
                "bidOptimization": true,
                "bidMultiplier": 0,
                "portfolioId": 0,
        }
        :return:
        '''
        interface = 'sb/campaigns'
        if all_data_list is not None:
            MyTypeAssert.other_assert(all_data_list, types=list)
            return self.make_request(interface, method='PUT', payload=all_data_list)
        MyTypeAssert.number_assert(campaign_id)

        data = [{
            "campaignId": campaign_id,
        }]
        data[0].update(params)

        return self.make_request(interface, method='PUT', payload=data)

    def archive_campaign(self, campaign_id):
        MyTypeAssert.number_assert(campaign_id)
        interface = 'sb/campaigns/{campaign_id}'.format(campaign_id=campaign_id)
        return self.make_request(interface, method='DELETE')


class AdGroups(SbClient):

    def get_ad_group(self, **params):
        interface = 'sb/adGroups/'

        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'name': params.get('name'),
            'adGroupIdFilter': params.get('adGroupIdFilter'),
            'campaignIdFilter': params.get('campaignIdFilter'),
        }
        return self.make_request(interface, payload=payload)

    def get_ad_group_ex(self, ad_group_id):
        MyTypeAssert.number_assert(ad_group_id)
        interface = 'sb/adGroups/{}'.format(ad_group_id)
        return self.make_request(interface)


class Bid(SbClient):

    def __init__(self, *args, **kwargs):
        super(Bid, self).__init__(*args, **kwargs)
        self.sandbox_header = {'BIDDING_CONTROLS_ON': 'yes'} if self.sandbox else {}

    def get_bid_recommendations(self, campaign_id, targets, keywords):
        '''
            0. A list of keywords or targeting expressions for which to generate bid recommendations
            1. Note that if a value is specified for the campaignId field,
            the past performance data for the campaign may be use to create bid recommendations
        :param campaign_id:
        :param targets: [
            [
              {
                "type": one of [asinCategorySameAs, asinBrandSameAs, asinPriceLessThan, asinPriceBetween,
                asinPriceGreaterThan, asinReviewRatingLessThan,
                asinReviewRatingBetween, asinReviewRatingGreaterThan, asinSameAs]
                "value": "string"
              }
            ]
        ]
        :param keywords: [
            {
              "matchType": one of [broad, exact, phrase]
              "keywordText": "string"
            }
        ]
        :return:
        '''
        MyTypeAssert.number_assert(campaign_id)
        MyTypeAssert.other_assert(targets, types=list)
        MyTypeAssert.other_assert(keywords, types=list)
        interface = 'sb/recommendations/bids'
        data = {
            'campaignId': campaign_id,
            'targets': targets,
            'keywords': keywords,
        }

        return self.make_request(interface, headers=self.sandbox_header, method='POST', payload=data)


class Keywords(SbClient):

    def get_keyword_ex(self, keyword_id):
        MyTypeAssert.number_assert(keyword_id)
        interface = 'sb/keywords/{}'.format(keyword_id)
        return self.make_request(interface)

    def get_keyword(self, **params):
        interface = 'sb/keywords'

        data = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'matchTypeFilter': params.get('matchTypeFilter'),
            'keywordText': params.get('keywordText'),
            'stateFilter': params.get('stateFilter'),
            'campaignIdFilter': params.get('campaignIdFilter'),
            'adGroupIdFilter': params.get('adGroupIdFilter'),
            'keywordIdFilter': params.get('keywordIdFilter'),
        }
        return self.make_request(interface=interface, payload=data)

    def create_keywords(self, ad_group_id, campaign_id,
                        keyword_text, match_type,
                        all_data_list=None,
                        **params):
        interface = 'sb/keywords'

        if all_data_list is not None:
            return self.make_request(interface, method='POST', payload=all_data_list)
        MyTypeAssert.number_assert(ad_group_id, campaign_id)
        # assert state in ["enabled", "paused", "archived"]
        assert match_type in ["exact", "phrase", "broad"]

        payload = [{
            'adGroupId': ad_group_id,
            'campaignId': campaign_id,
            'keywordText': keyword_text,
            'matchType': match_type,
            # 'state': state
        }]
        payload[0].update(params)
        return self.make_request(interface, method='POST', payload=payload)

    def update_keywords(self, keyword_id, adgroup_id, campaign_id,
                        all_data_list=None, **params):
        # you can only update the bid amount, or archive them.

        interface = 'sb/keywords'
        if all_data_list is not None:
            return self.make_request(interface, method='PUT', payload=all_data_list)
        MyTypeAssert.number_assert(keyword_id)
        data = [{
            'keywordId': keyword_id,
            'adGroupId': adgroup_id,
            'campaignId': campaign_id,
        }]
        data[0].update(params)

        return self.make_request(interface, method='PUT', payload=data)

    def archived_keyword(self, keyword_id):
        MyTypeAssert.number_assert(keyword_id)
        interface = 'sb/keywords/{}'.format(keyword_id)
        return self.make_request(interface, method='DELETE')

    def get_negative_keyword(self, keyword_id):
        MyTypeAssert.number_assert(keyword_id)
        interface = 'sb/negativeKeywords/{}'.format(keyword_id)
        return self.make_request(interface)

    def create_negative_keywords(self, ad_group_id, campaign_id,
                                 keyword_text, match_type,
                                 all_data_list=None, **params):
        interface = 'sb/negativeKeywords'

        if all_data_list is not None:
            return self.make_request(interface, method='POST', payload=all_data_list)
        MyTypeAssert.number_assert(ad_group_id, campaign_id)

        assert match_type in ["negativeExact", "negativePhrase"]

        payload = [{
            'adGroupId': ad_group_id,
            'campaignId': campaign_id,
            'keywordText': keyword_text,
            'matchType': match_type,
        }]
        payload[0].update(params)

        return self.make_request(interface, method='POST', payload=payload)

    def update_negative_keywords(self, keyword_id, adgroup_id, campaign_id, state,
                                 all_data_list=None, **params):
        interface = 'sb/negativeKeywords'

        if all_data_list is not None:
            return self.make_request(interface, method='PUT', payload=all_data_list)
        MyTypeAssert.number_assert(keyword_id, adgroup_id)
        assert state in ['enabled', 'pending', 'archived', 'draft']
        data = [{
            'keywordId': keyword_id,
            'adGroupId': adgroup_id,
            'campaignId': campaign_id,
            'state': state,
        }]
        data[0].update(params)
        return self.make_request(interface, method='PUT', payload=data)

    def archive_negative_keyword(self, keyword_id):
        MyTypeAssert.number_assert(keyword_id)
        interface = 'sb/negativeKeywords/{}'.format(keyword_id)
        return self.make_request(interface, method='DELETE')

    def get_recommendations_keywords(self, **params):

        '''

        :param params: one of [{'asins':[], 'maxNumSuggestions': int},{'url':[], 'maxNumSuggestions': int}]
        :return: [{
            "recommendationId": "addKeyword",
            "value": "string",
            "matchType": "broad"
        }]
        '''

        interface = 'sb/recommendations/keyword'
        payload = {
            'asins': params.get('asins'),
            'maxNumSuggestions': params.get('maxNumSuggestions'),
            'url': params.get('url'),
        }
        return self.make_request(interface, method='POST', payload=payload)


class Targets(SbClient):

    def get_targeting_clause(self, target_id):
        interface = 'sb/targets/{}'.format(target_id)
        return self.make_request(interface)

    def list_targeting_clause(self, next_token, max_results, filters, **params):

        '''
        Gets a list of product targets associated with the client identifier passed in the authorization header,
        filtered by specified criteria.
        :param next_token: string
        :param max_results: int [1, 100]
        :param filters: one of [
            {
              "filterType": "TARGETING_STATE",
              "values": one of ["ENABLED", 'PAUSED', 'PENDING', 'ARCHIVED', 'DRAFT']
            },
            {
              "filterType": "CAMPAIGN_ID",
              "values": ["string"]
            },
            {
              "filterType": "AD_GROUP_ID",
              "values": [0]
            }
        ]
        :param params:
        :return:
        '''

        interface = 'sb/targets/list'
        payload = {
            'nextToken': next_token,
            'maxResults': max_results,
            'filters': filters,
        }
        return self.make_request(interface, method='POST', payload=payload)

    def create_targeting_clause(self, targets, all_data_list=None, **params):
        '''

        :param targets: [
            {
              "adGroupId": 0,
              "campaignId": 0,
              "expressions": {
                "type": one of ["asinCategorySameAs", asinBrandSameAs, asinPriceLessThan, asinPriceBetween,
    asinPriceGreaterThan, asinReviewRatingLessThan, asinReviewRatingBetween, asinReviewRatingGreaterThan, asinSameAs ]
                "value": "string"
              },
              "bid": 0
            }
        ]
        :param all_data_list:
        :param params:
        :return:
        '''

        interface = 'sb/targets'
        if all_data_list is not None:
            return self.make_request(interface, method='POST', payload=all_data_list)
        MyTypeAssert.other_assert(targets, types=list)
        data = [{
            'targets': targets,
        }]
        data[0].update(params)

        return self.make_request(interface, method='POST', payload=data)

    def update_targeting_clause(self, target_id, adgroup_id, campaign_id, state,
                                all_data_list=None, **params):
        interface = 'sb/targets'
        if all_data_list is not None:
            return self.make_request(interface=interface, payload=all_data_list)
        MyTypeAssert.number_assert(target_id, adgroup_id, campaign_id)
        assert state in ['enabled', 'paused', 'pending', 'archived', 'draft']
        data = [{
            'targetId': target_id,
            'adGroupId': adgroup_id,
            'campaignId': campaign_id,
            'state': state,
        }]
        data[0].update(params)
        return self.make_request(interface, method='PUT', payload=data)

    def delete_targeting_clause(self, target_id):
        interface = 'sb/targets/{}'.format(target_id)
        return self.make_request(interface, method='DELETE')

    def get_target_ex(self, target_ids):
        interface = 'sb/targets/batchGet'
        MyTypeAssert.other_assert(target_ids, types=list)
        payload = {
            'targetIds': target_ids
        }
        return self.make_request(interface, method='POST', payload=payload)

    def list_negative_targeting_clause(self, next_token, max_results, filters):

        '''

        :param next_token:
        :param max_results:
        :param filters:  one of [
            {
              "filterType": "STATE",
              "values": [
                ENABLED, PAUSED, PENDING, ARCHIVED, DRAFT
              ]
            },
            {
              "filterType": "CAMPAIGN_ID",
              "values": [
                "string"
              ]
            },
            {
              "filterType": "AD_GROUP_ID",
              "values": [
                "string"
              ]
            }
        ]
        :return:
        '''

        interface = 'sb/negativeTargets/list'
        MyTypeAssert.other_assert(filters, types=list)
        data = {
            'nextToken': next_token,
            'maxResults': max_results,
            'filters': filters,
        }
        return self.make_request(interface=interface, method='POST', payload=data)

    def create_negative_targeting_clauses(self, negative_targets):
        '''

        :param negative_targets:  [
            {
              "adGroupId": 0,
              "campaignId": 0,
              "expressions": {
                "type": "asinBrandSameAs", "asinSameAs"
                "value": "string"
              }
            }
        ]
        :return:
        '''
        interface = 'sb/negativeTargets'
        MyTypeAssert.other_assert(negative_targets, types=list)

        data = {
            'negativeTargets': negative_targets,
        }

        return self.make_request(interface, method='POST', payload=data)

    def update_negative_targeting_clauses(self, negative_targets):
        '''

        :param negative_targets: [
            {
              "targetId": 0,
              "adGroupId": 0,
              "state": enabled, enabled, paused, pending, archived, draft
            }
        ]
        :return:
        '''
        interface = 'sb/negativeTargets'
        MyTypeAssert.other_assert(negative_targets, types=list)
        data = {
            'negativeTargets': negative_targets
        }

        return self.make_request(interface, method='PUT', payload=data)

    def get_negative_targeting_clauses(self, negative_targetid):
        interface = 'sb/negativeTargets/{}'.format(negative_targetid)
        return self.make_request(interface)

    def delete_negative_targeting_clause(self, negative_targetid):
        interface = 'sb/negativeTargets/{}'.format(negative_targetid)
        return self.make_request(interface=interface, method='DELETE')

    def get_negative_targeting_by_id(self, target_id):
        interface = 'sb/negativeTargets/batchGet'
        MyTypeAssert.other_assert(target_id, types=list)
        data = {
            'targetIds': target_id,
        }
        return self.make_request(interface=interface, method='POST', payload=data)

    #     Targeting recommendations
    def get_recommendations_target_product_list(self, next_token, max_results, filters):
        '''

        :param next_token:
        :param max_results:
        :param filters: [
            {
              "filterType": "ASINS",
              "values": ["string"]
            }
        ]
        :return: Gets a list of recommended products for targeting.
        '''
        interface = 'sb/recommendations/targets/product/list'
        MyTypeAssert.other_assert(filters, types=list)
        data = {
            'nextToken': next_token,
            'maxResults': max_results,
            'filters': filters,
        }
        return self.make_request(interface=interface, method='POST', payload=data)

    def get_recommendations_target_category_list(self, asins):
        '''

        :param asins: A list of asins ["string"]
        :return: Gets a list of recommended categories for targeting.
        '''
        interface = 'sb/recommendations/targets/category'
        MyTypeAssert.other_assert(asins, types=list)
        data = {
            'asins': asins
        }
        return self.make_request(interface=interface, method='POST', payload=data)

    def get_recommendations_target_brand_list(self, **params):
        '''

        :param params: one of [{'categoryId': int}, {'keyword': string}]
        :return:
        '''
        interface = 'sb/recommendations/targets/brand'
        payload = {
            'categoryId': params.get('categoryId'),
            'keyword': params.get('keyword')
        }
        return self.make_request(interface=interface, method='POST', payload=payload)


class Drafts(SbClient):

    def get_drafts_campaign_list(self, **params):
        interface = 'sb/drafts/campaigns'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'name': params.get('name'),
            'draftCampaignIdFilter': params.get('draftCampaignIdFilter'),
            'portfolioIdFilter': params.get('portfolioIdFilter')
        }
        return self.make_request(interface=interface, payload=payload)

    def get_drafts_campaigns_by_id(self, draft_campaigns_id):
        interface = 'sb/drafts/campaigns/{}'.format(draft_campaigns_id)
        return self.make_request(interface=interface)

    def create_drafts_campaigns(self, name, budget: (int, float), budget_type, start_date,
                                brand_entityid, bid_optimization, bid_multiplier,
                                portfolio_id, creative, landing_page,
                                all_data_list=None, **params):
        '''

        :param name:
        :param budget:
        :param budget_type:
        :param start_date:
        :param brand_entityid:
        :param bid_optimization:
        :param bid_multiplier:
        :param portfolio_id:
        :param creative: {
          "brandName": "string",
          "brandLogoAssetID": "string",
          "headline": "string",
          "asins": ["string"],
          "shouldOptimizeAsins": false
        }
        :param landing_page:  {
          "asins": [
            "string"
          ],
          "url": "string"
        }
        :param all_data_list: max 10
        :param params: one of [{
            "keywords": [{
                "keywordText": "string",
                "matchType": one of [broad, exact, phrase]
                "bid": 0
            }],
            "negativeKeywords": [{
                "keywordText": "string",
                "matchType": one of [negativeExact, negativePhrase]
            }]},
            {
                "targets": [{
                    "expressions": [{
                        "type": one of [ asinCategorySameAs, asinBrandSameAs, asinPriceLessThan, asinPriceBetween,
                            asinPriceGreaterThan, asinReviewRatingLessThan, asinReviewRatingBetween,
                            asinReviewRatingGreaterThan, asinSameAs],
                        "value": "string"
                    }],
                    "bid": 0
                }],
                "negativeTargets": [{
                    "expressions": [{
                        "type": same as "targets" expressions type,
                        "value": "string"
                    }]
                }]
            }
        ]
        :return:
        '''
        interface = 'sb/drafts/campaigns'
        if all_data_list is not None:
            return self.make_request(interface=interface, method='POST', payload=all_data_list)
        assert budget_type in ['lifetime', 'daily']
        assert bid_optimization in [True, False]
        assert len(start_date) == 8
        MyTypeAssert.other_assert(creative, types=dict)
        MyTypeAssert.other_assert(landing_page, types=dict)
        data = [{
            "name": name,
            "budget": budget,
            "budgetType": budget_type,
            "startDate": start_date,
            "brandEntityId": brand_entityid,
            "bidOptimization": bid_optimization,
            "bidMultiplier": bid_multiplier,
            "portfolioId": portfolio_id,
            "creative": creative,
            "landingPage": landing_page,
        }]
        data[0].update(params)
        return self.make_request(interface=interface, method='POST', payload=data)

    def update_drafts_campaigns(self, all_data_list=None, **params):
        '''

        :param all_data_list: max 10
        :param params:
        :return:
        '''
        interface = 'sb/drafts/campaigns'
        if all_data_list is not None:
            MyTypeAssert.other_assert(all_data_list, types=list)
            return self.make_request(interface=interface, method='PUT', payload=all_data_list)

        data = [{
            "name": params.get('name'),
            "budget": params.get('budget'),
            "budgetType": params.get('budgetType'),
            "startDate": params.get('startDate'),
            "endDate": params.get('endDate'),
            "brandEntityId": params.get('brandEntityId'),
            "bidOptimization": params.get('bidOptimization'),
            "bidMultiplier": params.get('bidMultiplier'),
            "portfolioId": params.get('portfolioId'),
            "creative": params.get('creative'),
            "landingPage": params.get('landingPage'),
        }]
        data[0].update(params)
        return self.make_request(interface=interface, method='PUT', payload=data)

    def delete_drafts_campaigns_by_id(self, draft_campaigns_id):
        interface = 'sb/drafts/campaigns/{}'.format(draft_campaigns_id)
        return self.make_request(interface=interface, method='DELETE')

    def submit_drafts_campaigns(self, draft_id):
        '''
        Submits one or more existing draft campaigns to the moderation approval queue.
        :param draft_id: list of draft id,  Maximum length is 10 draft campaign identifiers
        :return:
        '''
        interface = 'sb/drafts/campaigns/submit'
        MyTypeAssert.other_assert(draft_id, types=list)
        assert len(draft_id) <= 10
        data = {
            'draftId': draft_id
        }
        return self.make_request(interface=interface, method='POST', payload=data)


class Reports(SbClient):

    def request_report(self, record_type, report_date, metrics_list, segment=None):
        assert record_type in ['Campaign', 'Ad groups', 'Keyword', 'Search Term', 'Target']
        interface = 'v2/hsa/{}/report'.format(record_type)
        MyTypeAssert.other_assert(metrics_list, types=list)

        # report_date must format YYYYMMDD . and not older than 60 days .
        assert len(report_date) == 8
        payload = {
            'reportDate': report_date,
            'metrics': ','.join(metrics_list)
        }
        if segment:
            payload['segment'] = segment

        return self.make_request(interface, method='POST', payload=payload)

    def get_report(self, report_id):
        # The ReportResponse will contain a report status code.When the report has completed,
        # the location field will provide a redirect URL for the gzipped file containing the report.
        interface = 'v2/reports/{}'.format(report_id)
        resp = self.make_request(interface)
        if resp.status_code == 200:
            json_file = gzip.decompress(resp.content)
            result = json.loads(json_file)
            return result
        return resp

    def download_reports(self, report_id):
        interface = 'v2/reports/{}/download'.format(report_id)
        return self.make_request(interface=interface)


class Moderation(SbClient):

    def get_moderation_by_id(self, campaign_id):
        '''

        :param campaign_id: int
        :return: Gets the moderation result for a campaign specified by identifier.
        '''
        interface = 'sb/moderation/campaigns/{}'.format(campaign_id)
        return self.make_request(interface)


class Landing(SbClient):

    def get_landing_page_asins(self, page_url):
        '''

        :param page_url:  string
        :return: Gets ASIN information for a specified address.
        '''
        interface = 'pageAsins/{}'.format(page_url)
        return self.make_request(interface=interface)


class Stores(SbClient):

    def get_assets(self, brand_entityid, media_type):
        '''

        :param brand_entityid: string
        :param media_type: string
        :return: Gets a list of assets associated with a specified brand entity identifier.
        '''
        interface = 'stores/assets'
        assert media_type in ['brandLogo', 'image', 'video', 'backgroundVideo']

        data = {
            'brandEntityId': brand_entityid,
            'mediaType': media_type,
        }
        return self.make_request(interface=interface, payload=data)

    def create_assets(self, content_disposition, content_type, asset_info, asset):
        '''
        Creates a new image asset.
        :param content_disposition: The name of the image file.
        :param content_type: The image format type, one of ['PNG', 'JPEG', 'GIF']
        :param asset_info: {
          brandEntityId: "12345678", optional
          mediaType: {
            "brandLogo", must this value
          }
        }
        :param asset: The binary data for the image. File size must be smaller than 1MB, 400*400px
        :return:
        '''
        interface = 'stores/assets'
        assert content_type in ['PNG', 'JPEG', 'GIF']

        headers = {
            'Content-Disposition': content_disposition,
            'Content-Type': content_type,
        }

        data = {
            'assetInfo': asset_info,
            'asset': asset,
        }

        return self.make_request(interface=interface, method='POST', headers=headers, payload=data)


class EntitySnapshots(SbClient):

    def request_snapshot(self, record_type, state_filter):
        assert record_type in ["campaigns", "keywords", ]
        assert state_filter in ['enabled', 'paused', 'archived']
        interface = 'v2/hsa/{}/snapshot'.format(record_type)
        data = {
            'stateFilter': state_filter
        }
        return self.make_request(interface, method='POST', payload=data)

    def get_snapshot_by_id(self, snapshot_id):
        interface = 'v2/hsa/snapshots/{}'.format(snapshot_id)
        return self.make_request(interface)

    def download_snapshot_file(self, url):
        return self.make_request(url=url)