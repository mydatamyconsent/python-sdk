# mydatamyconsent.DataConsentsApi

All URIs are relative to *https://api.mydatamyconsent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_consented_document_by_id**](DataConsentsApi.md#download_consented_document_by_id) | **GET** /v1/consents/individuals/{consentId}/documents/{documentId}/download | Download a individuals consented document.
[**download_org_consented_document_by_id**](DataConsentsApi.md#download_org_consented_document_by_id) | **GET** /v1/consents/organizations/{consentId}/documents/{documentId}/download | Download a organizations consented document.
[**get_all_consented_documents**](DataConsentsApi.md#get_all_consented_documents) | **GET** /v1/consents/individuals/{consentId}/documents | Get the individual documents based on ConsentId.
[**get_all_consented_financial_accounts**](DataConsentsApi.md#get_all_consented_financial_accounts) | **GET** /v1/consents/individuals/{consentId}/financial-accounts | Get all individual consented financial accounts.
[**get_all_organization_consented_documents**](DataConsentsApi.md#get_all_organization_consented_documents) | **GET** /v1/consents/organizations/{consentId}/documents | Get the organization documents based on ConsentId.
[**get_consent_details_by_id**](DataConsentsApi.md#get_consent_details_by_id) | **GET** /v1/consents/individuals/{consentId} | Get all individuals consent details by consent id.
[**get_consent_financial_accounts**](DataConsentsApi.md#get_consent_financial_accounts) | **GET** /v1/consents/organizations/{consentId}/financial-accounts | Get all organizational consented financial accounts.
[**get_consented_account_by_id**](DataConsentsApi.md#get_consented_account_by_id) | **GET** /v1/consents/individuals/{consentId}/financial-accounts/{accountId} | Get individual consented financial account details based on account id.
[**get_consented_document_by_id**](DataConsentsApi.md#get_consented_document_by_id) | **GET** /v1/consents/individuals/{consentId}/documents/{documentId} | Get individuals consent document based on document id.
[**get_consented_financial_account**](DataConsentsApi.md#get_consented_financial_account) | **GET** /v1/consents/organizations/{consentId}/financial-accounts/{accountId} | Get organization consented financial account details based on account id.
[**get_consented_financial_account_transactions**](DataConsentsApi.md#get_consented_financial_account_transactions) | **GET** /v1/consents/individuals/{consentId}/financial-accounts/{accountId}/transactions | Get individual consented financial account transactions of an individual based on accountId.
[**get_consents_for_organizations**](DataConsentsApi.md#get_consents_for_organizations) | **GET** /v1/consents/organizations | Get the list of data consents sent for organizations.
[**get_consents_sent_to_individuals**](DataConsentsApi.md#get_consents_sent_to_individuals) | **GET** /v1/consents/individuals | Get the list of Consents Sent to Individuals.
[**get_org_consented_account_transactions**](DataConsentsApi.md#get_org_consented_account_transactions) | **GET** /v1/consents/organizations/{consentId}/financial-accounts/{accountId}/transactions | Get organization consented financial account transactions of an individual based on accountId.
[**get_organization_consent_details_by_id**](DataConsentsApi.md#get_organization_consent_details_by_id) | **GET** /v1/consents/organizations/{consentId} | Get all organization consent details by consent id.
[**get_organization_consented_document_by_id**](DataConsentsApi.md#get_organization_consented_document_by_id) | **GET** /v1/consents/organizations/{consentId}/documents/{documentId} | Get organization consent document based on document id.


# **download_consented_document_by_id**
> UserDocumentDownload download_consented_document_by_id(consent_id, document_id)

Download a individuals consented document.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.user_document_download import UserDocumentDownload
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.
    document_id = "documentId_example" # str | Document id.

    # example passing only required values which don't have defaults set
    try:
        # Download a individuals consented document.
        api_response = api_instance.download_consented_document_by_id(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->download_consented_document_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |
 **document_id** | **str**| Document id. |

### Return type

[**UserDocumentDownload**](UserDocumentDownload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_org_consented_document_by_id**
> OrganizationDocumentDownloadDto download_org_consented_document_by_id(consent_id, document_id)

Download a organizations consented document.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.organization_document_download_dto import OrganizationDocumentDownloadDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.
    document_id = "documentId_example" # str | Document id.

    # example passing only required values which don't have defaults set
    try:
        # Download a organizations consented document.
        api_response = api_instance.download_org_consented_document_by_id(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->download_org_consented_document_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |
 **document_id** | **str**| Document id. |

### Return type

[**OrganizationDocumentDownloadDto**](OrganizationDocumentDownloadDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_consented_documents**
> DataConsentDocumentsDto get_all_consented_documents(consent_id)

Get the individual documents based on ConsentId.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_documents_dto import DataConsentDocumentsDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.

    # example passing only required values which don't have defaults set
    try:
        # Get the individual documents based on ConsentId.
        api_response = api_instance.get_all_consented_documents(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_all_consented_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |

### Return type

[**DataConsentDocumentsDto**](DataConsentDocumentsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_consented_financial_accounts**
> DataConsentFinancialsDto get_all_consented_financial_accounts(consent_id)

Get all individual consented financial accounts.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_financials_dto import DataConsentFinancialsDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.

    # example passing only required values which don't have defaults set
    try:
        # Get all individual consented financial accounts.
        api_response = api_instance.get_all_consented_financial_accounts(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_all_consented_financial_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |

### Return type

[**DataConsentFinancialsDto**](DataConsentFinancialsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_organization_consented_documents**
> DataConsentDocumentsDto get_all_organization_consented_documents(consent_id)

Get the organization documents based on ConsentId.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_documents_dto import DataConsentDocumentsDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.

    # example passing only required values which don't have defaults set
    try:
        # Get the organization documents based on ConsentId.
        api_response = api_instance.get_all_organization_consented_documents(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_all_organization_consented_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |

### Return type

[**DataConsentDocumentsDto**](DataConsentDocumentsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_details_by_id**
> DataConsentDetailsDto get_consent_details_by_id(consent_id)

Get all individuals consent details by consent id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_details_dto import DataConsentDetailsDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.

    # example passing only required values which don't have defaults set
    try:
        # Get all individuals consent details by consent id.
        api_response = api_instance.get_consent_details_by_id(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consent_details_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |

### Return type

[**DataConsentDetailsDto**](DataConsentDetailsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_financial_accounts**
> DataConsentFinancialsDto get_consent_financial_accounts(consent_id)

Get all organizational consented financial accounts.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_financials_dto import DataConsentFinancialsDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.

    # example passing only required values which don't have defaults set
    try:
        # Get all organizational consented financial accounts.
        api_response = api_instance.get_consent_financial_accounts(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consent_financial_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |

### Return type

[**DataConsentFinancialsDto**](DataConsentFinancialsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consented_account_by_id**
> FinancialAccount get_consented_account_by_id(consent_id, account_id)

Get individual consented financial account details based on account id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.financial_account import FinancialAccount
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.
    account_id = "accountId_example" # str | Account id.

    # example passing only required values which don't have defaults set
    try:
        # Get individual consented financial account details based on account id.
        api_response = api_instance.get_consented_account_by_id(consent_id, account_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consented_account_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |
 **account_id** | **str**| Account id. |

### Return type

[**FinancialAccount**](FinancialAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consented_document_by_id**
> UserDocumentDetails get_consented_document_by_id(consent_id, document_id)

Get individuals consent document based on document id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.user_document_details import UserDocumentDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.
    document_id = "documentId_example" # str | Document Id.

    # example passing only required values which don't have defaults set
    try:
        # Get individuals consent document based on document id.
        api_response = api_instance.get_consented_document_by_id(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consented_document_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |
 **document_id** | **str**| Document Id. |

### Return type

[**UserDocumentDetails**](UserDocumentDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consented_financial_account**
> OrganizationFinancialAccountDto get_consented_financial_account(consent_id, account_id)

Get organization consented financial account details based on account id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.organization_financial_account_dto import OrganizationFinancialAccountDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.
    account_id = "accountId_example" # str | Account id.

    # example passing only required values which don't have defaults set
    try:
        # Get organization consented financial account details based on account id.
        api_response = api_instance.get_consented_financial_account(consent_id, account_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consented_financial_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |
 **account_id** | **str**| Account id. |

### Return type

[**OrganizationFinancialAccountDto**](OrganizationFinancialAccountDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consented_financial_account_transactions**
> UserAccountFinancialTransactionsDtoPaginatedList get_consented_financial_account_transactions(consent_id, account_id)

Get individual consented financial account transactions of an individual based on accountId.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.user_account_financial_transactions_dto_paginated_list import UserAccountFinancialTransactionsDtoPaginatedList
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.
    account_id = "accountId_example" # str | Account id.
    filters = "filters_example" # str | Filters. (optional)
    from_date_time_utc = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | From date time in utc timezone. (optional)
    to_date_time_utc = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Til date time in utc timezone. (optional)
    page_no = 10 # int | Page number. (optional) if omitted the server will use the default value of 10
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get individual consented financial account transactions of an individual based on accountId.
        api_response = api_instance.get_consented_financial_account_transactions(consent_id, account_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consented_financial_account_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get individual consented financial account transactions of an individual based on accountId.
        api_response = api_instance.get_consented_financial_account_transactions(consent_id, account_id, filters=filters, from_date_time_utc=from_date_time_utc, to_date_time_utc=to_date_time_utc, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consented_financial_account_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |
 **account_id** | **str**| Account id. |
 **filters** | **str**| Filters. | [optional]
 **from_date_time_utc** | **datetime**| From date time in utc timezone. | [optional]
 **to_date_time_utc** | **datetime**| Til date time in utc timezone. | [optional]
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 10
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25

### Return type

[**UserAccountFinancialTransactionsDtoPaginatedList**](UserAccountFinancialTransactionsDtoPaginatedList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consents_for_organizations**
> OrganizationDataConsentInfoDtoPaginatedList get_consents_for_organizations()

Get the list of data consents sent for organizations.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.organization_data_consent_info_dto_paginated_list import OrganizationDataConsentInfoDtoPaginatedList
from mydatamyconsent.model.data_consent_status import DataConsentStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    status = DataConsentStatus("Pending") # DataConsentStatus | Data consent status MyDataMyConsent.Domain.Entities.ConsentAggregate.Enums.DataConsentStatus. (optional)
    _from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | From date time in utc timezone. (optional)
    to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Til date time in utc timezone. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of data consents sent for organizations.
        api_response = api_instance.get_consents_for_organizations(status=status, _from=_from, to=to, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consents_for_organizations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **DataConsentStatus**| Data consent status MyDataMyConsent.Domain.Entities.ConsentAggregate.Enums.DataConsentStatus. | [optional]
 **_from** | **datetime**| From date time in utc timezone. | [optional]
 **to** | **datetime**| Til date time in utc timezone. | [optional]
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25

### Return type

[**OrganizationDataConsentInfoDtoPaginatedList**](OrganizationDataConsentInfoDtoPaginatedList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consents_sent_to_individuals**
> UserDataConsentInfoDtoPaginatedList get_consents_sent_to_individuals()

Get the list of Consents Sent to Individuals.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.user_data_consent_info_dto_paginated_list import UserDataConsentInfoDtoPaginatedList
from mydatamyconsent.model.data_consent_status import DataConsentStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    status = DataConsentStatus("Pending") # DataConsentStatus | Data consent status MyDataMyConsent.Domain.Entities.ConsentAggregate.Enums.DataConsentStatus. (optional)
    _from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | From date time in utc timezone. (optional)
    to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Til date time in utc timezone. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of Consents Sent to Individuals.
        api_response = api_instance.get_consents_sent_to_individuals(status=status, _from=_from, to=to, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consents_sent_to_individuals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **DataConsentStatus**| Data consent status MyDataMyConsent.Domain.Entities.ConsentAggregate.Enums.DataConsentStatus. | [optional]
 **_from** | **datetime**| From date time in utc timezone. | [optional]
 **to** | **datetime**| Til date time in utc timezone. | [optional]
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25

### Return type

[**UserDataConsentInfoDtoPaginatedList**](UserDataConsentInfoDtoPaginatedList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_consented_account_transactions**
> OrganizationFinancialTransactionsDtoPaginatedList get_org_consented_account_transactions(consent_id, account_id)

Get organization consented financial account transactions of an individual based on accountId.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.organization_financial_transactions_dto_paginated_list import OrganizationFinancialTransactionsDtoPaginatedList
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.
    account_id = "accountId_example" # str | Account id.
    filters = "filters_example" # str | Filters. (optional)
    from_date_time_utc = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | From date time in utc timezone. (optional)
    to_date_time_utc = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Til date time in utc timezone. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get organization consented financial account transactions of an individual based on accountId.
        api_response = api_instance.get_org_consented_account_transactions(consent_id, account_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_org_consented_account_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get organization consented financial account transactions of an individual based on accountId.
        api_response = api_instance.get_org_consented_account_transactions(consent_id, account_id, filters=filters, from_date_time_utc=from_date_time_utc, to_date_time_utc=to_date_time_utc, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_org_consented_account_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |
 **account_id** | **str**| Account id. |
 **filters** | **str**| Filters. | [optional]
 **from_date_time_utc** | **datetime**| From date time in utc timezone. | [optional]
 **to_date_time_utc** | **datetime**| Til date time in utc timezone. | [optional]
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25

### Return type

[**OrganizationFinancialTransactionsDtoPaginatedList**](OrganizationFinancialTransactionsDtoPaginatedList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_consent_details_by_id**
> DataConsentDetailsDto get_organization_consent_details_by_id(consent_id)

Get all organization consent details by consent id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_details_dto import DataConsentDetailsDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.

    # example passing only required values which don't have defaults set
    try:
        # Get all organization consent details by consent id.
        api_response = api_instance.get_organization_consent_details_by_id(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_organization_consent_details_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |

### Return type

[**DataConsentDetailsDto**](DataConsentDetailsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_consented_document_by_id**
> OrganizationDocumentDetails get_organization_consented_document_by_id(consent_id, document_id)

Get organization consent document based on document id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.organization_document_details import OrganizationDocumentDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | Consent id.
    document_id = "documentId_example" # str | Document Id.

    # example passing only required values which don't have defaults set
    try:
        # Get organization consent document based on document id.
        api_response = api_instance.get_organization_consented_document_by_id(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_organization_consented_document_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Consent id. |
 **document_id** | **str**| Document Id. |

### Return type

[**OrganizationDocumentDetails**](OrganizationDocumentDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

