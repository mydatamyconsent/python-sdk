"""
    My Data My Consent - Developer API

    Unleashing the power of data consent by establishing trust. The Platform Core Developer API defines a set of capabilities that can be used to request, issue, manage and update data, documents and credentials by organizations. The API can be used to request, manage and update Decentralised Identifiers, Financial Data, Health Data issue Documents, Credentials directly or using OpenID Connect flows, and verify Messages signed with DIDs and much more.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@mydatamyconsent.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import com.mydatamyconsent
from com.mydatamyconsent.model.filter_type import FilterType
from com.mydatamyconsent.model.operator import Operator
globals()['FilterType'] = FilterType
globals()['Operator'] = Operator
from com.mydatamyconsent.model.data_consent_rfa_filter_dto import DataConsentRfaFilterDto


class TestDataConsentRfaFilterDto(unittest.TestCase):
    """DataConsentRfaFilterDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDataConsentRfaFilterDto(self):
        """Test DataConsentRfaFilterDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DataConsentRfaFilterDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
