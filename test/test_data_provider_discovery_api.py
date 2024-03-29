"""
    My Data My Consent - Developer API

    Unleashing the power of data consent by establishing trust. The Platform Core Developer API defines a set of capabilities that can be used to request, issue, manage and update data, documents and credentials by organizations. The API can be used to request, manage and update Decentralised Identifiers, Financial Data, Health Data issue Documents, Credentials directly or using OpenID Connect flows, and verify Messages signed with DIDs and much more.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@mydatamyconsent.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import com.mydatamyconsent
from com.mydatamyconsent.api.data_provider_discovery_api import DataProviderDiscoveryApi  # noqa: E501


class TestDataProviderDiscoveryApi(unittest.TestCase):
    """DataProviderDiscoveryApi unit test stubs"""

    def setUp(self):
        self.api = DataProviderDiscoveryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_data_providers_get(self):
        """Test case for v1_data_providers_get

        Discover all data providers in My Data My Consent by country and filters.  # noqa: E501
        """
        pass

    def test_v1_data_providers_provider_id_get(self):
        """Test case for v1_data_providers_provider_id_get

        Get a Data Provider details.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
