# mydatamyconsent.DataConsentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_consents_consent_id_accounts_account_id_get**](DataConsentsApi.md#v1_consents_consent_id_accounts_account_id_get) | **GET** /v1/consents/{consentId}/accounts/{accountId} | Get consented financial account details.
[**v1_consents_consent_id_accounts_account_id_insights_get**](DataConsentsApi.md#v1_consents_consent_id_accounts_account_id_insights_get) | **GET** /v1/consents/{consentId}/accounts/{accountId}/insights | Get consented financial account insights.
[**v1_consents_consent_id_accounts_account_id_transactions_get**](DataConsentsApi.md#v1_consents_consent_id_accounts_account_id_transactions_get) | **GET** /v1/consents/{consentId}/accounts/{accountId}/transactions | Get consented financial account transactions.
[**v1_consents_consent_id_accounts_get**](DataConsentsApi.md#v1_consents_consent_id_accounts_get) | **GET** /v1/consents/{consentId}/accounts | Get all accounts in a consent.
[**v1_consents_consent_id_documents_document_id_analysis_get**](DataConsentsApi.md#v1_consents_consent_id_documents_document_id_analysis_get) | **GET** /v1/consents/{consentId}/documents/{documentId}/analysis | Get analysis of a consented document.
[**v1_consents_consent_id_documents_document_id_download_get**](DataConsentsApi.md#v1_consents_consent_id_documents_document_id_download_get) | **GET** /v1/consents/{consentId}/documents/{documentId}/download | Download a consented document.
[**v1_consents_consent_id_documents_document_id_get**](DataConsentsApi.md#v1_consents_consent_id_documents_document_id_get) | **GET** /v1/consents/{consentId}/documents/{documentId} | Get consented document details.
[**v1_consents_consent_id_documents_get**](DataConsentsApi.md#v1_consents_consent_id_documents_get) | **GET** /v1/consents/{consentId}/documents | Get all documents in a consent.
[**v1_consents_consent_id_get**](DataConsentsApi.md#v1_consents_consent_id_get) | **GET** /v1/consents/{consentId} | Get consent details by consent id.
[**v1_consents_get**](DataConsentsApi.md#v1_consents_get) | **GET** /v1/consents | Get all consents filtered by status and time.


# **v1_consents_consent_id_accounts_account_id_get**
> dict v1_consents_consent_id_accounts_account_id_get(consent_id, account_id)

Get consented financial account details.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
        # Get consented financial account details.
        api_response = api_instance.v1_consents_consent_id_accounts_account_id_get(consent_id, account_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_consent_id_accounts_account_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **account_id** | **str**|  |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_consent_id_accounts_account_id_insights_get**
> dict v1_consents_consent_id_accounts_account_id_insights_get(consent_id, account_id)

Get consented financial account insights.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
        # Get consented financial account insights.
        api_response = api_instance.v1_consents_consent_id_accounts_account_id_insights_get(consent_id, account_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_consent_id_accounts_account_id_insights_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **account_id** | **str**|  |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_consent_id_accounts_account_id_transactions_get**
> dict v1_consents_consent_id_accounts_account_id_transactions_get(consent_id, account_id)

Get consented financial account transactions.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    from_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    to_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get consented financial account transactions.
        api_response = api_instance.v1_consents_consent_id_accounts_account_id_transactions_get(consent_id, account_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_consent_id_accounts_account_id_transactions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get consented financial account transactions.
        api_response = api_instance.v1_consents_consent_id_accounts_account_id_transactions_get(consent_id, account_id, filters=filters, from_date=from_date, to_date=to_date)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_consent_id_accounts_account_id_transactions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **account_id** | **str**|  |
 **filters** | **str**|  | [optional]
 **from_date** | **datetime**|  | [optional]
 **to_date** | **datetime**|  | [optional]

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_consent_id_accounts_get**
> dict v1_consents_consent_id_accounts_get(consent_id)

Get all accounts in a consent.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
        # Get all accounts in a consent.
        api_response = api_instance.v1_consents_consent_id_accounts_get(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_consent_id_accounts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_consent_id_documents_document_id_analysis_get**
> dict v1_consents_consent_id_documents_document_id_analysis_get(consent_id, document_id)

Get analysis of a consented document.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    document_id = "documentId_example" # str | Document Id.

    # example passing only required values which don't have defaults set
    try:
        # Get analysis of a consented document.
        api_response = api_instance.v1_consents_consent_id_documents_document_id_analysis_get(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_consent_id_documents_document_id_analysis_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **document_id** | **str**| Document Id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_consent_id_documents_document_id_download_get**
> dict v1_consents_consent_id_documents_document_id_download_get(consent_id, document_id)

Download a consented document.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    document_id = "documentId_example" # str | Document Id.

    # example passing only required values which don't have defaults set
    try:
        # Download a consented document.
        api_response = api_instance.v1_consents_consent_id_documents_document_id_download_get(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_consent_id_documents_document_id_download_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **document_id** | **str**| Document Id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_consent_id_documents_document_id_get**
> dict v1_consents_consent_id_documents_document_id_get(consent_id, document_id)

Get consented document details.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    document_id = "documentId_example" # str | Document Id.

    # example passing only required values which don't have defaults set
    try:
        # Get consented document details.
        api_response = api_instance.v1_consents_consent_id_documents_document_id_get(consent_id, document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_consent_id_documents_document_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |
 **document_id** | **str**| Document Id. |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_consent_id_documents_get**
> dict v1_consents_consent_id_documents_get(consent_id)

Get all documents in a consent.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
        # Get all documents in a consent.
        api_response = api_instance.v1_consents_consent_id_documents_get(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_consent_id_documents_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_consent_id_get**
> dict v1_consents_consent_id_get(consent_id)

Get consent details by consent id.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
        # Get consent details by consent id.
        api_response = api_instance.v1_consents_consent_id_get(consent_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_consent_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  |

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_consents_get**
> dict v1_consents_get()

Get all consents filtered by status and time.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consents_api
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
    status = DataConsentStatus("Pending") # DataConsentStatus | MyDataMyConsent.Domain.Entities.ConsentAggregate.Enums.DataConsentStatus. (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | System.DateTime. (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | till dateSystem.DateTime. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all consents filtered by status and time.
        api_response = api_instance.v1_consents_get(status=status, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentsApi->v1_consents_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **DataConsentStatus**| MyDataMyConsent.Domain.Entities.ConsentAggregate.Enums.DataConsentStatus. | [optional]
 **start_date** | **datetime**| System.DateTime. | [optional]
 **end_date** | **datetime**| till dateSystem.DateTime. | [optional]

### Return type

**dict**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

