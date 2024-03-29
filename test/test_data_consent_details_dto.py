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
from com.mydatamyconsent.model.data_consent_requested_account_dto import DataConsentRequestedAccountDto
from com.mydatamyconsent.model.data_consent_requested_document import DataConsentRequestedDocument
from com.mydatamyconsent.model.data_consent_requested_document_dto import DataConsentRequestedDocumentDto
from com.mydatamyconsent.model.data_consent_requester_dto import DataConsentRequesterDto
from com.mydatamyconsent.model.data_consent_status import DataConsentStatus
from com.mydatamyconsent.model.data_fetch_frequency_unit import DataFetchFrequencyUnit
from com.mydatamyconsent.model.data_fetch_type import DataFetchType
from com.mydatamyconsent.model.data_life_unit import DataLifeUnit
from com.mydatamyconsent.model.json_schema import JsonSchema
globals()['DataConsentRequestedAccountDto'] = DataConsentRequestedAccountDto
globals()['DataConsentRequestedDocument'] = DataConsentRequestedDocument
globals()['DataConsentRequestedDocumentDto'] = DataConsentRequestedDocumentDto
globals()['DataConsentRequesterDto'] = DataConsentRequesterDto
globals()['DataConsentStatus'] = DataConsentStatus
globals()['DataFetchFrequencyUnit'] = DataFetchFrequencyUnit
globals()['DataFetchType'] = DataFetchType
globals()['DataLifeUnit'] = DataLifeUnit
globals()['JsonSchema'] = JsonSchema
from com.mydatamyconsent.model.data_consent_details_dto import DataConsentDetailsDto


class TestDataConsentDetailsDto(unittest.TestCase):
    """DataConsentDetailsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDataConsentDetailsDto(self):
        """Test DataConsentDetailsDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DataConsentDetailsDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
