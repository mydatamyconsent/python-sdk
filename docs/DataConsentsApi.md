# mydatamyconsent.DataConsentsApi

All URIs are relative to *https://api.mydatamyconsent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_consented_document_analysis**](DataConsentsApi.md#download_consented_document_analysis) | **GET** /v1/consents/{consentId}/documents/{documentId}/analysis | Get analysis of a consented document.
[**download_individual_consented_document_by_id**](DataConsentsApi.md#download_individual_consented_document_by_id) | **GET** /v1/consents/individuals/{consentId}/documents/{documentId}/download | Download individual consented document by document id.
[**download_organization_consented_document_by_id**](DataConsentsApi.md#download_organization_consented_document_by_id) | **GET** /v1/consents/organizations/{consentId}/documents/{documentId}/download | Download organization consent document based on document id.
[**get_all_consented_financial_accounts**](DataConsentsApi.md#get_all_consented_financial_accounts) | **GET** /v1/consents/individuals/{consentId}/financial-accounts | Get all individual consented financial accounts.
[**get_consent_financial_accounts**](DataConsentsApi.md#get_consent_financial_accounts) | **GET** /v1/consents/organizations/{consentId}/financial-accounts | Get all organizational consented financial accounts.
[**get_consented_account_by_id**](DataConsentsApi.md#get_consented_account_by_id) | **GET** /v1/consents/individuals/{consentId}/financial-accounts/{accountId} | Get individual consented financial account details based on account id.
[**get_consented_document_by_id**](DataConsentsApi.md#get_consented_document_by_id) | **GET** /v1/consents/individuals/{consentId}/documents/{documentId} | Get individual consented document by document id.
[**get_consented_financial_account**](DataConsentsApi.md#get_consented_financial_account) | **GET** /v1/consents/organizations/{consentId}/financial-accounts/{accountId} | Get organization consented financial account details based on account id.
[**get_consented_financial_account_insights**](DataConsentsApi.md#get_consented_financial_account_insights) | **GET** /v1/consents/{consentId}/financial-accounts/{accountId}/insights | Get consented financial account insights.
[**get_consented_financial_account_transactions**](DataConsentsApi.md#get_consented_financial_account_transactions) | **GET** /v1/consents/individuals/{consentId}/financial-accounts/{accountId}/transactions | Get individual consented financial account transactions of an individual based on accountId.
[**get_consents**](DataConsentsApi.md#get_consents) | **GET** /v1/consents/individuals | Get the paginated list of individual data consents.
[**get_individual_consented_documents**](DataConsentsApi.md#get_individual_consented_documents) | **GET** /v1/consents/individuals/{consentId}/documents | Get individual consented documents by consent id.
[**get_individual_data_consent_by_id**](DataConsentsApi.md#get_individual_data_consent_by_id) | **GET** /v1/consents/individuals/{consentId} | Get individuals data consent details by consent id.
[**get_org_consented_account_transactions**](DataConsentsApi.md#get_org_consented_account_transactions) | **GET** /v1/consents/organizations/{consentId}/financial-accounts/{accountId}/transactions | Get organization consented financial account transactions of an individual based on accountId.
[**get_organization_consented_document_by_id**](DataConsentsApi.md#get_organization_consented_document_by_id) | **GET** /v1/consents/organizations/{consentId}/documents/{documentId} | Get organization consent document based on document id.
[**get_organization_consented_documents**](DataConsentsApi.md#get_organization_consented_documents) | **GET** /v1/consents/organizations/{consentId}/documents | Get organization consented documents by consent id.
[**get_organization_data_consent_by_id**](DataConsentsApi.md#get_organization_data_consent_by_id) | **GET** /v1/consents/organizations/{consentId} | Get organizations data consent details by consent id.
[**get_organization_data_consents**](DataConsentsApi.md#get_organization_data_consents) | **GET** /v1/consents/organizations | Get the paginated list of organization data consents.


# **download_consented_document_analysis**
> dict download_consented_document_analysis(consent_id, document_id)

Get analysis of a consented document.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    consent_id = "consentId_example" # str | Data consent id.
    document_id = "documentId_example" # str | Consented document Id.

    # example passing only required values which don't have defaults set
    try:
        # Get analysis of a consented document.
        api_response = api_instance.download_consented_document_analysis(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->download_consented_document_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Data consent id. |
 **document_id** | **str**| Consented document Id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_individual_consented_document_by_id**
> dict download_individual_consented_document_by_id(consent_id, document_id)

Download individual consented document by document id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    consent_id = "consentId_example" # str | Individual data consent id.
    document_id = "documentId_example" # str | Consented document id.

    # example passing only required values which don't have defaults set
    try:
        # Download individual consented document by document id.
        api_response = api_instance.download_individual_consented_document_by_id(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->download_individual_consented_document_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Individual data consent id. |
 **document_id** | **str**| Consented document id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_organization_consented_document_by_id**
> dict download_organization_consented_document_by_id(consent_id, document_id)

Download organization consent document based on document id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    consent_id = "consentId_example" # str | Organization data consent id.
    document_id = "documentId_example" # str | Organization consented document Id.

    # example passing only required values which don't have defaults set
    try:
        # Download organization consent document based on document id.
        api_response = api_instance.download_organization_consented_document_by_id(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->download_organization_consented_document_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Organization data consent id. |
 **document_id** | **str**| Organization consented document Id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
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
> dict get_consented_document_by_id(consent_id, document_id)

Get individual consented document by document id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    consent_id = "consentId_example" # str | Individual data consent id.
    document_id = "documentId_example" # str | Consented document id.

    # example passing only required values which don't have defaults set
    try:
        # Get individual consented document by document id.
        api_response = api_instance.get_consented_document_by_id(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consented_document_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Individual data consent id. |
 **document_id** | **str**| Consented document id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
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

# **get_consented_financial_account_insights**
> get_consented_financial_account_insights(consent_id, account_id)

Get consented financial account insights.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    consent_id = "consentId_example" # str | 
    account_id = "accountId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get consented financial account insights.
        api_instance.get_consented_financial_account_insights(consent_id, account_id)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consented_financial_account_insights: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **account_id** | **str**|  |

### Return type

void (empty response body)

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

# **get_consents**
> dict get_consents()

Get the paginated list of individual data consents.

GetIndividualDataConsents

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    from_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | From datetime in UTC timezone. (optional)
    to_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | To datetime in UTC timezone. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the paginated list of individual data consents.
        api_response = api_instance.get_consents(status=status, from_date_time=from_date_time, to_date_time=to_date_time, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_consents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **DataConsentStatus**| Data consent status MyDataMyConsent.Domain.Entities.ConsentAggregate.Enums.DataConsentStatus. | [optional]
 **from_date_time** | **datetime**| From datetime in UTC timezone. | [optional]
 **to_date_time** | **datetime**| To datetime in UTC timezone. | [optional]
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_individual_consented_documents**
> dict get_individual_consented_documents(consent_id)

Get individual consented documents by consent id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    consent_id = "consentId_example" # str | Individual data consent id.

    # example passing only required values which don't have defaults set
    try:
        # Get individual consented documents by consent id.
        api_response = api_instance.get_individual_consented_documents(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_individual_consented_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Individual data consent id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_individual_data_consent_by_id**
> dict get_individual_data_consent_by_id(consent_id)

Get individuals data consent details by consent id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    consent_id = "consentId_example" # str | Individual data consent id.

    # example passing only required values which don't have defaults set
    try:
        # Get individuals data consent details by consent id.
        api_response = api_instance.get_individual_data_consent_by_id(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_individual_data_consent_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Individual data consent id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
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

# **get_organization_consented_document_by_id**
> dict get_organization_consented_document_by_id(consent_id, document_id)

Get organization consent document based on document id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    consent_id = "consentId_example" # str | Organization data consent id.
    document_id = "documentId_example" # str | Organization consented document Id.

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
 **consent_id** | **str**| Organization data consent id. |
 **document_id** | **str**| Organization consented document Id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_consented_documents**
> dict get_organization_consented_documents(consent_id)

Get organization consented documents by consent id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    consent_id = "consentId_example" # str | Organization data consent id.

    # example passing only required values which don't have defaults set
    try:
        # Get organization consented documents by consent id.
        api_response = api_instance.get_organization_consented_documents(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_organization_consented_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Organization data consent id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_data_consent_by_id**
> dict get_organization_data_consent_by_id(consent_id)

Get organizations data consent details by consent id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    consent_id = "consentId_example" # str | Organization data consent id.

    # example passing only required values which don't have defaults set
    try:
        # Get organizations data consent details by consent id.
        api_response = api_instance.get_organization_data_consent_by_id(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_organization_data_consent_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| Organization data consent id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_data_consents**
> dict get_organization_data_consents()

Get the paginated list of organization data consents.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    from_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | From datetime in UTC timezone. (optional)
    to_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | To datetime in UTC timezone. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the paginated list of organization data consents.
        api_response = api_instance.get_organization_data_consents(status=status, from_date_time=from_date_time, to_date_time=to_date_time, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->get_organization_data_consents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **DataConsentStatus**| Data consent status MyDataMyConsent.Domain.Entities.ConsentAggregate.Enums.DataConsentStatus. | [optional]
 **from_date_time** | **datetime**| From datetime in UTC timezone. | [optional]
 **to_date_time** | **datetime**| To datetime in UTC timezone. | [optional]
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

