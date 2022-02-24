# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from mydatamyconsent.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from mydatamyconsent.model.activity import Activity
from mydatamyconsent.model.approved_consent_request import ApprovedConsentRequest
from mydatamyconsent.model.bank_account_type import BankAccountType
from mydatamyconsent.model.create_data_processing_agreement_request_model import CreateDataProcessingAgreementRequestModel
from mydatamyconsent.model.create_individual_data_consent_request import CreateIndividualDataConsentRequest
from mydatamyconsent.model.create_organization_data_consent_request import CreateOrganizationDataConsentRequest
from mydatamyconsent.model.data_consent_details_dto import DataConsentDetailsDto
from mydatamyconsent.model.data_consent_documents_dto import DataConsentDocumentsDto
from mydatamyconsent.model.data_consent_financials_dto import DataConsentFinancialsDto
from mydatamyconsent.model.data_consent_requested_document import DataConsentRequestedDocument
from mydatamyconsent.model.data_consent_requested_financial_account import DataConsentRequestedFinancialAccount
from mydatamyconsent.model.data_consent_status import DataConsentStatus
from mydatamyconsent.model.data_processing_agreement_dto import DataProcessingAgreementDto
from mydatamyconsent.model.data_processing_agreement_dto_paginated_list import DataProcessingAgreementDtoPaginatedList
from mydatamyconsent.model.data_protection_officer import DataProtectionOfficer
from mydatamyconsent.model.data_provider import DataProvider
from mydatamyconsent.model.data_provider_paginated_list import DataProviderPaginatedList
from mydatamyconsent.model.digital_signature import DigitalSignature
from mydatamyconsent.model.document import Document
from mydatamyconsent.model.document_category_type import DocumentCategoryType
from mydatamyconsent.model.document_issue_request import DocumentIssueRequest
from mydatamyconsent.model.document_issue_request_details import DocumentIssueRequestDetails
from mydatamyconsent.model.document_issue_request_status import DocumentIssueRequestStatus
from mydatamyconsent.model.document_receiver import DocumentReceiver
from mydatamyconsent.model.document_sub_category_type import DocumentSubCategoryType
from mydatamyconsent.model.document_type import DocumentType
from mydatamyconsent.model.document_type_paginated_list import DocumentTypePaginatedList
from mydatamyconsent.model.documents_required import DocumentsRequired
from mydatamyconsent.model.file_type import FileType
from mydatamyconsent.model.financial import Financial
from mydatamyconsent.model.financial_account import FinancialAccount
from mydatamyconsent.model.financial_account_details_required import FinancialAccountDetailsRequired
from mydatamyconsent.model.financial_accounts import FinancialAccounts
from mydatamyconsent.model.identification_strategy import IdentificationStrategy
from mydatamyconsent.model.identifier import Identifier
from mydatamyconsent.model.individual_data_consent_request_response import IndividualDataConsentRequestResponse
from mydatamyconsent.model.issued_document import IssuedDocument
from mydatamyconsent.model.issued_document_paginated_list import IssuedDocumentPaginatedList
from mydatamyconsent.model.json_schema import JsonSchema
from mydatamyconsent.model.life import Life
from mydatamyconsent.model.organization_data_consent_info_dto import OrganizationDataConsentInfoDto
from mydatamyconsent.model.organization_data_consent_info_dto_paginated_list import OrganizationDataConsentInfoDtoPaginatedList
from mydatamyconsent.model.organization_data_consent_request_response import OrganizationDataConsentRequestResponse
from mydatamyconsent.model.organization_document_details_dto import OrganizationDocumentDetailsDto
from mydatamyconsent.model.organization_document_download_dto import OrganizationDocumentDownloadDto
from mydatamyconsent.model.organization_financial_account_dto import OrganizationFinancialAccountDto
from mydatamyconsent.model.organization_financial_transactions_dto import OrganizationFinancialTransactionsDto
from mydatamyconsent.model.organization_financial_transactions_dto_paginated_list import OrganizationFinancialTransactionsDtoPaginatedList
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.push_uri_request import PushUriRequest
from mydatamyconsent.model.push_uri_response import PushUriResponse
from mydatamyconsent.model.receiver import Receiver
from mydatamyconsent.model.receiver_type import ReceiverType
from mydatamyconsent.model.shared_with import SharedWith
from mydatamyconsent.model.string_string_key_value_pair import StringStringKeyValuePair
from mydatamyconsent.model.supported_entity_type import SupportedEntityType
from mydatamyconsent.model.supported_identifier import SupportedIdentifier
from mydatamyconsent.model.update_data_processing_agreement_request_model import UpdateDataProcessingAgreementRequestModel
from mydatamyconsent.model.uri_details import UriDetails
from mydatamyconsent.model.user_account_financial_transactions_dto import UserAccountFinancialTransactionsDto
from mydatamyconsent.model.user_account_financial_transactions_dto_paginated_list import UserAccountFinancialTransactionsDtoPaginatedList
from mydatamyconsent.model.user_data_consent_info_dto import UserDataConsentInfoDto
from mydatamyconsent.model.user_data_consent_info_dto_paginated_list import UserDataConsentInfoDtoPaginatedList
from mydatamyconsent.model.user_document_details_dto import UserDocumentDetailsDto
from mydatamyconsent.model.user_document_download_dto import UserDocumentDownloadDto
