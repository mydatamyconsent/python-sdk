"""
    My Data My Consent - Developer API

    Unleashing the power of data consent by establishing trust. The Platform Core Developer API defines a set of capabilities that can be used to request, issue, manage and update data, documents and credentials by organizations. The API can be used to request, manage and update Decentralised Identifiers, Financial Data, Health Data issue Documents, Credentials directly or using OpenID Connect flows, and verify Messages signed with DIDs and much more.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@mydatamyconsent.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import com.mydatamyconsent
from com.mydatamyconsent.api.data_consents_api import DataConsentsApi  # noqa: E501


class TestDataConsentsApi(unittest.TestCase):
    """DataConsentsApi unit test stubs"""

    def setUp(self):
        self.api = DataConsentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_consents_consent_id_accounts_account_id_get(self):
        """Test case for v1_consents_consent_id_accounts_account_id_get

        Get consented financial account details.  # noqa: E501
        """
        pass

    def test_v1_consents_consent_id_accounts_account_id_insights_get(self):
        """Test case for v1_consents_consent_id_accounts_account_id_insights_get

        Get consented financial account insights.  # noqa: E501
        """
        pass

    def test_v1_consents_consent_id_accounts_account_id_transactions_get(self):
        """Test case for v1_consents_consent_id_accounts_account_id_transactions_get

        Get consented financial account transactions.  # noqa: E501
        """
        pass

    def test_v1_consents_consent_id_accounts_get(self):
        """Test case for v1_consents_consent_id_accounts_get

        Get all accounts in a consent.  # noqa: E501
        """
        pass

    def test_v1_consents_consent_id_documents_document_id_analysis_get(self):
        """Test case for v1_consents_consent_id_documents_document_id_analysis_get

        Get analysis of a consented document.  # noqa: E501
        """
        pass

    def test_v1_consents_consent_id_documents_document_id_download_get(self):
        """Test case for v1_consents_consent_id_documents_document_id_download_get

        Download a consented document.  # noqa: E501
        """
        pass

    def test_v1_consents_consent_id_documents_document_id_get(self):
        """Test case for v1_consents_consent_id_documents_document_id_get

        Get consented document details.  # noqa: E501
        """
        pass

    def test_v1_consents_consent_id_documents_get(self):
        """Test case for v1_consents_consent_id_documents_get

        Get all documents in a consent.  # noqa: E501
        """
        pass

    def test_v1_consents_consent_id_get(self):
        """Test case for v1_consents_consent_id_get

        Get consent details by consent id.  # noqa: E501
        """
        pass

    def test_v1_consents_get(self):
        """Test case for v1_consents_get

        Get all consents filtered by status and time.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
