# mydatamyconsent.DataConsentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_consents_individuals_consent_id_accounts_account_id_get**](DataConsentsApi.md#v1_consents_individuals_consent_id_accounts_account_id_get) | **GET** /v1/consents/individuals/{consentId}/accounts/{accountId} | Get individual consented financial account details based on account id.
[**v1_consents_individuals_consent_id_accounts_account_id_transactions_get**](DataConsentsApi.md#v1_consents_individuals_consent_id_accounts_account_id_transactions_get) | **GET** /v1/consents/individuals/{consentId}/accounts/{accountId}/transactions | Get consented financial account transactions of an individual based on accountId.
[**v1_consents_individuals_consent_id_accounts_get**](DataConsentsApi.md#v1_consents_individuals_consent_id_accounts_get) | **GET** /v1/consents/individuals/{consentId}/accounts | Get all individual financial accounts in a consent.
[**v1_consents_individuals_consent_id_documents_document_id_download_get**](DataConsentsApi.md#v1_consents_individuals_consent_id_documents_document_id_download_get) | **GET** /v1/consents/individuals/{consentId}/documents/{documentId}/download | Download a individuals consented document.
[**v1_consents_individuals_consent_id_documents_document_id_get**](DataConsentsApi.md#v1_consents_individuals_consent_id_documents_document_id_get) | **GET** /v1/consents/individuals/{consentId}/documents/{documentId} | Get individuals consent document based on document id.
[**v1_consents_individuals_consent_id_documents_get**](DataConsentsApi.md#v1_consents_individuals_consent_id_documents_get) | **GET** /v1/consents/individuals/{consentId}/documents | Get the individual documents based on ConsentId.
[**v1_consents_individuals_consent_id_get**](DataConsentsApi.md#v1_consents_individuals_consent_id_get) | **GET** /v1/consents/individuals/{consentId} | Get individuals consent details by consent id.
[**v1_consents_individuals_get**](DataConsentsApi.md#v1_consents_individuals_get) | **GET** /v1/consents/individuals | Get the list of Consents Sent to Individuals.
[**v1_consents_organizations_consent_id_accounts_account_id_get**](DataConsentsApi.md#v1_consents_organizations_consent_id_accounts_account_id_get) | **GET** /v1/consents/organizations/{consentId}/accounts/{accountId} | Get orgnization consented financial account details based on account id.
[**v1_consents_organizations_consent_id_accounts_account_id_transactions_get**](DataConsentsApi.md#v1_consents_organizations_consent_id_accounts_account_id_transactions_get) | **GET** /v1/consents/organizations/{consentId}/accounts/{accountId}/transactions | Get consented financial account transactions of an organization based on accountId.
[**v1_consents_organizations_consent_id_accounts_get**](DataConsentsApi.md#v1_consents_organizations_consent_id_accounts_get) | **GET** /v1/consents/organizations/{consentId}/accounts | Get all organizational financial accounts in a consent.
[**v1_consents_organizations_consent_id_documents_document_id_download_get**](DataConsentsApi.md#v1_consents_organizations_consent_id_documents_document_id_download_get) | **GET** /v1/consents/organizations/{consentId}/documents/{documentId}/download | Download organizations consented document.
[**v1_consents_organizations_consent_id_documents_document_id_get**](DataConsentsApi.md#v1_consents_organizations_consent_id_documents_document_id_get) | **GET** /v1/consents/organizations/{consentId}/documents/{documentId} | Get organizations consent document based on document id.
[**v1_consents_organizations_consent_id_documents_get**](DataConsentsApi.md#v1_consents_organizations_consent_id_documents_get) | **GET** /v1/consents/organizations/{consentId}/documents | Get the organizations documents based on ConsentId.
[**v1_consents_organizations_consent_id_get**](DataConsentsApi.md#v1_consents_organizations_consent_id_get) | **GET** /v1/consents/organizations/{consentId} | Get organizations consent details by consent id.
[**v1_consents_organizations_get**](DataConsentsApi.md#v1_consents_organizations_get) | **GET** /v1/consents/organizations | Get the list of data consents sent for organizations.


# **v1_consents_individuals_consent_id_accounts_account_id_get**
> FinancialAccount v1_consents_individuals_consent_id_accounts_account_id_get(consent_id, account_id)

Get individual consented financial account details based on account id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.financial_account import FinancialAccount
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 
    account_id = "accountId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get individual consented financial account details based on account id.
        api_response = api_instance.v1_consents_individuals_consent_id_accounts_account_id_get(consent_id, account_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_individuals_consent_id_accounts_account_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **account_id** | **str**|  |

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_individuals_consent_id_accounts_account_id_transactions_get**
> UserAccountFinancialTransactionsDtoPaginatedList v1_consents_individuals_consent_id_accounts_account_id_transactions_get(consent_id, account_id)

Get consented financial account transactions of an individual based on accountId.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.user_account_financial_transactions_dto_paginated_list import UserAccountFinancialTransactionsDtoPaginatedList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 
    account_id = "accountId_example" # str | 
    filters = "filters_example" # str |  (optional)
    page_no = 1 # int |  (optional)
    page_size = 1 # int |  (optional)
    from_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    to_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get consented financial account transactions of an individual based on accountId.
        api_response = api_instance.v1_consents_individuals_consent_id_accounts_account_id_transactions_get(consent_id, account_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_individuals_consent_id_accounts_account_id_transactions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get consented financial account transactions of an individual based on accountId.
        api_response = api_instance.v1_consents_individuals_consent_id_accounts_account_id_transactions_get(consent_id, account_id, filters=filters, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_individuals_consent_id_accounts_account_id_transactions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **account_id** | **str**|  |
 **filters** | **str**|  | [optional]
 **page_no** | **int**|  | [optional]
 **page_size** | **int**|  | [optional]
 **from_date** | **datetime**|  | [optional]
 **to_date** | **datetime**|  | [optional]

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_individuals_consent_id_accounts_get**
> DataConsentFinancialsDto v1_consents_individuals_consent_id_accounts_get(consent_id)

Get all individual financial accounts in a consent.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_financials_dto import DataConsentFinancialsDto
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get all individual financial accounts in a consent.
        api_response = api_instance.v1_consents_individuals_consent_id_accounts_get(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_individuals_consent_id_accounts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_individuals_consent_id_documents_document_id_download_get**
> UserDocumentDownloadDto v1_consents_individuals_consent_id_documents_document_id_download_get(consent_id, document_id)

Download a individuals consented document.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.user_document_download_dto import UserDocumentDownloadDto
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | consentId.
    document_id = "documentId_example" # str | documentId.

    # example passing only required values which don't have defaults set
    try:
        # Download a individuals consented document.
        api_response = api_instance.v1_consents_individuals_consent_id_documents_document_id_download_get(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_individuals_consent_id_documents_document_id_download_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| consentId. |
 **document_id** | **str**| documentId. |

### Return type

[**UserDocumentDownloadDto**](UserDocumentDownloadDto.md)

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_individuals_consent_id_documents_document_id_get**
> UserDocumentDetailsDto v1_consents_individuals_consent_id_documents_document_id_get(consent_id, document_id)

Get individuals consent document based on document id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.user_document_details_dto import UserDocumentDetailsDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 
    document_id = "documentId_example" # str | Document Id.

    # example passing only required values which don't have defaults set
    try:
        # Get individuals consent document based on document id.
        api_response = api_instance.v1_consents_individuals_consent_id_documents_document_id_get(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_individuals_consent_id_documents_document_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **document_id** | **str**| Document Id. |

### Return type

[**UserDocumentDetailsDto**](UserDocumentDetailsDto.md)

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_individuals_consent_id_documents_get**
> DataConsentDocumentsDto v1_consents_individuals_consent_id_documents_get(consent_id)

Get the individual documents based on ConsentId.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_documents_dto import DataConsentDocumentsDto
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the individual documents based on ConsentId.
        api_response = api_instance.v1_consents_individuals_consent_id_documents_get(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_individuals_consent_id_documents_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_individuals_consent_id_get**
> DataConsentDetailsDto v1_consents_individuals_consent_id_get(consent_id)

Get individuals consent details by consent id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_details_dto import DataConsentDetailsDto
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get individuals consent details by consent id.
        api_response = api_instance.v1_consents_individuals_consent_id_get(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_individuals_consent_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_individuals_get**
> UserDataConsentInfoDtoPaginatedList v1_consents_individuals_get()

Get the list of Consents Sent to Individuals.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.user_data_consent_info_dto_paginated_list import UserDataConsentInfoDtoPaginatedList
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.data_consent_status import DataConsentStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    page_no = 1 # int |  (optional)
    page_size = 1 # int |  (optional)
    status = DataConsentStatus("Pending") # DataConsentStatus |  (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of Consents Sent to Individuals.
        api_response = api_instance.v1_consents_individuals_get(page_no=page_no, page_size=page_size, status=status, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_individuals_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_no** | **int**|  | [optional]
 **page_size** | **int**|  | [optional]
 **status** | **DataConsentStatus**|  | [optional]
 **start_date** | **datetime**|  | [optional]
 **end_date** | **datetime**|  | [optional]

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_organizations_consent_id_accounts_account_id_get**
> OrganizationFinancialAccountDto v1_consents_organizations_consent_id_accounts_account_id_get(consent_id, account_id)

Get orgnization consented financial account details based on account id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.organization_financial_account_dto import OrganizationFinancialAccountDto
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 
    account_id = "accountId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get orgnization consented financial account details based on account id.
        api_response = api_instance.v1_consents_organizations_consent_id_accounts_account_id_get(consent_id, account_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_organizations_consent_id_accounts_account_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **account_id** | **str**|  |

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_organizations_consent_id_accounts_account_id_transactions_get**
> OrganizationFinancialTransactionsDtoPaginatedList v1_consents_organizations_consent_id_accounts_account_id_transactions_get(consent_id, account_id)

Get consented financial account transactions of an organization based on accountId.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.organization_financial_transactions_dto_paginated_list import OrganizationFinancialTransactionsDtoPaginatedList
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 
    account_id = "accountId_example" # str | 
    filters = "filters_example" # str |  (optional)
    page_no = 1 # int |  (optional)
    page_size = 1 # int |  (optional)
    from_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    to_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get consented financial account transactions of an organization based on accountId.
        api_response = api_instance.v1_consents_organizations_consent_id_accounts_account_id_transactions_get(consent_id, account_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_organizations_consent_id_accounts_account_id_transactions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get consented financial account transactions of an organization based on accountId.
        api_response = api_instance.v1_consents_organizations_consent_id_accounts_account_id_transactions_get(consent_id, account_id, filters=filters, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_organizations_consent_id_accounts_account_id_transactions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **account_id** | **str**|  |
 **filters** | **str**|  | [optional]
 **page_no** | **int**|  | [optional]
 **page_size** | **int**|  | [optional]
 **from_date** | **datetime**|  | [optional]
 **to_date** | **datetime**|  | [optional]

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_organizations_consent_id_accounts_get**
> DataConsentFinancialsDto v1_consents_organizations_consent_id_accounts_get(consent_id)

Get all organizational financial accounts in a consent.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_financials_dto import DataConsentFinancialsDto
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get all organizational financial accounts in a consent.
        api_response = api_instance.v1_consents_organizations_consent_id_accounts_get(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_organizations_consent_id_accounts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_organizations_consent_id_documents_document_id_download_get**
> OrganizationDocumentDownloadDto v1_consents_organizations_consent_id_documents_document_id_download_get(consent_id, document_id)

Download organizations consented document.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.organization_document_download_dto import OrganizationDocumentDownloadDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 
    document_id = "documentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Download organizations consented document.
        api_response = api_instance.v1_consents_organizations_consent_id_documents_document_id_download_get(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_organizations_consent_id_documents_document_id_download_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **document_id** | **str**|  |

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_organizations_consent_id_documents_document_id_get**
> OrganizationDocumentDetailsDto v1_consents_organizations_consent_id_documents_document_id_get(consent_id, document_id)

Get organizations consent document based on document id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.organization_document_details_dto import OrganizationDocumentDetailsDto
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 
    document_id = "documentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get organizations consent document based on document id.
        api_response = api_instance.v1_consents_organizations_consent_id_documents_document_id_get(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_organizations_consent_id_documents_document_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **document_id** | **str**|  |

### Return type

[**OrganizationDocumentDetailsDto**](OrganizationDocumentDetailsDto.md)

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_organizations_consent_id_documents_get**
> DataConsentDocumentsDto v1_consents_organizations_consent_id_documents_get(consent_id)

Get the organizations documents based on ConsentId.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_documents_dto import DataConsentDocumentsDto
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the organizations documents based on ConsentId.
        api_response = api_instance.v1_consents_organizations_consent_id_documents_get(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_organizations_consent_id_documents_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_organizations_consent_id_get**
> DataConsentDetailsDto v1_consents_organizations_consent_id_get(consent_id)

Get organizations consent details by consent id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.data_consent_details_dto import DataConsentDetailsDto
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    consent_id = "consentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get organizations consent details by consent id.
        api_response = api_instance.v1_consents_organizations_consent_id_get(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_organizations_consent_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_organizations_get**
> OrganizationDataConsentInfoDtoPaginatedList v1_consents_organizations_get()

Get the list of data consents sent for organizations.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
from mydatamyconsent.model.organization_data_consent_info_dto_paginated_list import OrganizationDataConsentInfoDtoPaginatedList
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.data_consent_status import DataConsentStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consents_api.DataConsentsApi(api_client)
    page_no = 1 # int |  (optional)
    page_size = 1 # int |  (optional)
    status = DataConsentStatus("Pending") # DataConsentStatus |  (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of data consents sent for organizations.
        api_response = api_instance.v1_consents_organizations_get(page_no=page_no, page_size=page_size, status=status, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_organizations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_no** | **int**|  | [optional]
 **page_size** | **int**|  | [optional]
 **status** | **DataConsentStatus**|  | [optional]
 **start_date** | **datetime**|  | [optional]
 **end_date** | **datetime**|  | [optional]

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

