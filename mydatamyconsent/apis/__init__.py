
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from mydatamyconsent.api.data_consent_requests_api import DataConsentRequestsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from mydatamyconsent.api.data_consent_requests_api import DataConsentRequestsApi
from mydatamyconsent.api.data_consents_api import DataConsentsApi
from mydatamyconsent.api.data_processing_agreements_api import DataProcessingAgreementsApi
from mydatamyconsent.api.data_provider_discovery_api import DataProviderDiscoveryApi
from mydatamyconsent.api.digi_locker_compat_issuer_api import DigiLockerCompatIssuerApi
from mydatamyconsent.api.documents_api import DocumentsApi
from mydatamyconsent.api.supported_identifiers_api import SupportedIdentifiersApi
