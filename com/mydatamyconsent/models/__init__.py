# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from com.mydatamyconsent.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from com.mydatamyconsent.model.application_user import ApplicationUser
from com.mydatamyconsent.model.bank_account_type import BankAccountType
from com.mydatamyconsent.model.category_icon_font_family import CategoryIconFontFamily
from com.mydatamyconsent.model.country import Country
from com.mydatamyconsent.model.country_state import CountryState
from com.mydatamyconsent.model.data_consent import DataConsent
from com.mydatamyconsent.model.data_consent_details_dto import DataConsentDetailsDto
from com.mydatamyconsent.model.data_consent_identifier import DataConsentIdentifier
from com.mydatamyconsent.model.data_consent_request_model import DataConsentRequestModel
from com.mydatamyconsent.model.data_consent_requested_account_dto import DataConsentRequestedAccountDto
from com.mydatamyconsent.model.data_consent_requested_document import DataConsentRequestedDocument
from com.mydatamyconsent.model.data_consent_requested_document_dto import DataConsentRequestedDocumentDto
from com.mydatamyconsent.model.data_consent_requested_fa_dto import DataConsentRequestedFaDto
from com.mydatamyconsent.model.data_consent_requested_financial_account import DataConsentRequestedFinancialAccount
from com.mydatamyconsent.model.data_consent_requester_dto import DataConsentRequesterDto
from com.mydatamyconsent.model.data_consent_rfa_filter import DataConsentRfaFilter
from com.mydatamyconsent.model.data_consent_rfa_filter_dto import DataConsentRfaFilterDto
from com.mydatamyconsent.model.data_consent_status import DataConsentStatus
from com.mydatamyconsent.model.data_fetch_frequency_unit import DataFetchFrequencyUnit
from com.mydatamyconsent.model.data_fetch_type import DataFetchType
from com.mydatamyconsent.model.data_life_unit import DataLifeUnit
from com.mydatamyconsent.model.data_processing_agreement import DataProcessingAgreement
from com.mydatamyconsent.model.data_processing_agreement_paginated_list import DataProcessingAgreementPaginatedList
from com.mydatamyconsent.model.data_protection_officer import DataProtectionOfficer
from com.mydatamyconsent.model.data_provider import DataProvider
from com.mydatamyconsent.model.data_provider_paginated_list import DataProviderPaginatedList
from com.mydatamyconsent.model.document_issue_request import DocumentIssueRequest
from com.mydatamyconsent.model.document_provider_category import DocumentProviderCategory
from com.mydatamyconsent.model.file_type import FileType
from com.mydatamyconsent.model.filter_type import FilterType
from com.mydatamyconsent.model.financial_account_types import FinancialAccountTypes
from com.mydatamyconsent.model.gender import Gender
from com.mydatamyconsent.model.identification_strategy import IdentificationStrategy
from com.mydatamyconsent.model.identifier import Identifier
from com.mydatamyconsent.model.identifier_string_key_value_pair import IdentifierStringKeyValuePair
from com.mydatamyconsent.model.identity_claim import IdentityClaim
from com.mydatamyconsent.model.json_schema import JsonSchema
from com.mydatamyconsent.model.operator import Operator
from com.mydatamyconsent.model.organization import Organization
from com.mydatamyconsent.model.organization_address import OrganizationAddress
from com.mydatamyconsent.model.organization_address_type import OrganizationAddressType
from com.mydatamyconsent.model.organization_category import OrganizationCategory
from com.mydatamyconsent.model.organization_financial_account import OrganizationFinancialAccount
from com.mydatamyconsent.model.organization_kyo_document import OrganizationKyoDocument
from com.mydatamyconsent.model.organization_meta_data import OrganizationMetaData
from com.mydatamyconsent.model.organization_status import OrganizationStatus
from com.mydatamyconsent.model.organization_type import OrganizationType
from com.mydatamyconsent.model.problem_details import ProblemDetails
from com.mydatamyconsent.model.proof_document_type import ProofDocumentType
from com.mydatamyconsent.model.push_uri_request import PushUriRequest
from com.mydatamyconsent.model.push_uri_response import PushUriResponse
from com.mydatamyconsent.model.receiver import Receiver
from com.mydatamyconsent.model.receiver_type import ReceiverType
from com.mydatamyconsent.model.refresh_token import RefreshToken
from com.mydatamyconsent.model.rejection import Rejection
from com.mydatamyconsent.model.suggested_account_dto import SuggestedAccountDto
from com.mydatamyconsent.model.theme import Theme
from com.mydatamyconsent.model.uri_details import UriDetails
