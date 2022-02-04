# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from mydatamyconsent.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from mydatamyconsent.model.application_user import ApplicationUser
from mydatamyconsent.model.bank_account_type import BankAccountType
from mydatamyconsent.model.category_icon_font_family import CategoryIconFontFamily
from mydatamyconsent.model.country import Country
from mydatamyconsent.model.country_state import CountryState
from mydatamyconsent.model.data_consent import DataConsent
from mydatamyconsent.model.data_consent_details_dto import DataConsentDetailsDto
from mydatamyconsent.model.data_consent_identifier import DataConsentIdentifier
from mydatamyconsent.model.data_consent_request_model import DataConsentRequestModel
from mydatamyconsent.model.data_consent_requested_account_dto import DataConsentRequestedAccountDto
from mydatamyconsent.model.data_consent_requested_document import DataConsentRequestedDocument
from mydatamyconsent.model.data_consent_requested_document_dto import DataConsentRequestedDocumentDto
from mydatamyconsent.model.data_consent_requested_fa_dto import DataConsentRequestedFaDto
from mydatamyconsent.model.data_consent_requested_financial_account import DataConsentRequestedFinancialAccount
from mydatamyconsent.model.data_consent_requester_dto import DataConsentRequesterDto
from mydatamyconsent.model.data_consent_rfa_filter import DataConsentRfaFilter
from mydatamyconsent.model.data_consent_rfa_filter_dto import DataConsentRfaFilterDto
from mydatamyconsent.model.data_consent_status import DataConsentStatus
from mydatamyconsent.model.data_fetch_frequency_unit import DataFetchFrequencyUnit
from mydatamyconsent.model.data_fetch_type import DataFetchType
from mydatamyconsent.model.data_life_unit import DataLifeUnit
from mydatamyconsent.model.data_processing_agreement import DataProcessingAgreement
from mydatamyconsent.model.data_processing_agreement_paginated_list import DataProcessingAgreementPaginatedList
from mydatamyconsent.model.data_protection_officer import DataProtectionOfficer
from mydatamyconsent.model.data_provider import DataProvider
from mydatamyconsent.model.data_provider_paginated_list import DataProviderPaginatedList
from mydatamyconsent.model.document_issue_request import DocumentIssueRequest
from mydatamyconsent.model.document_provider_category import DocumentProviderCategory
from mydatamyconsent.model.file_type import FileType
from mydatamyconsent.model.filter_type import FilterType
from mydatamyconsent.model.financial_account_types import FinancialAccountTypes
from mydatamyconsent.model.gender import Gender
from mydatamyconsent.model.identification_strategy import IdentificationStrategy
from mydatamyconsent.model.identifier import Identifier
from mydatamyconsent.model.identifier_string_key_value_pair import IdentifierStringKeyValuePair
from mydatamyconsent.model.identity_claim import IdentityClaim
from mydatamyconsent.model.json_schema import JsonSchema
from mydatamyconsent.model.operator import Operator
from mydatamyconsent.model.organization import Organization
from mydatamyconsent.model.organization_address import OrganizationAddress
from mydatamyconsent.model.organization_address_type import OrganizationAddressType
from mydatamyconsent.model.organization_category import OrganizationCategory
from mydatamyconsent.model.organization_financial_account import OrganizationFinancialAccount
from mydatamyconsent.model.organization_kyo_document import OrganizationKyoDocument
from mydatamyconsent.model.organization_meta_data import OrganizationMetaData
from mydatamyconsent.model.organization_status import OrganizationStatus
from mydatamyconsent.model.organization_type import OrganizationType
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.proof_document_type import ProofDocumentType
from mydatamyconsent.model.push_uri_request import PushUriRequest
from mydatamyconsent.model.push_uri_response import PushUriResponse
from mydatamyconsent.model.receiver import Receiver
from mydatamyconsent.model.receiver_type import ReceiverType
from mydatamyconsent.model.refresh_token import RefreshToken
from mydatamyconsent.model.rejection import Rejection
from mydatamyconsent.model.suggested_account_dto import SuggestedAccountDto
from mydatamyconsent.model.theme import Theme
from mydatamyconsent.model.uri_details import UriDetails