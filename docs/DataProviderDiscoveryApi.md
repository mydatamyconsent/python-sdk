# com.mydatamyconsent.DataProviderDiscoveryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_data_providers_get**](DataProviderDiscoveryApi.md#v1_data_providers_get) | **GET** /v1/data-providers | Discover all data providers in My Data My Consent by country and filters.
[**v1_data_providers_provider_id_get**](DataProviderDiscoveryApi.md#v1_data_providers_provider_id_get) | **GET** /v1/data-providers/{providerId} | Get a Data Provider details.


# **v1_data_providers_get**
> DataProviderPaginatedList v1_data_providers_get()

Discover all data providers in My Data My Consent by country and filters.

.

### Example

```python
import time
import com.mydatamyconsent
from com.mydatamyconsent.api import data_provider_discovery_api
from com.mydatamyconsent.model.data_provider_paginated_list import DataProviderPaginatedList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = com.mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with com.mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_provider_discovery_api.DataProviderDiscoveryApi(api_client)
    account_type = "accountType_example" # str | Account type. (optional)
    document_type = "documentType_example" # str | Document type. (optional)
    organization_category = "organizationCategory_example" # str | Organization category. (optional)
    page_no = 1 # int | Page number. (optional)
    page_size = 1 # int | Page size. (optional)
    country = "IN" # str | ISO2 Country code. (optional) if omitted the server will use the default value of "IN"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Discover all data providers in My Data My Consent by country and filters.
        api_response = api_instance.v1_data_providers_get(account_type=account_type, document_type=document_type, organization_category=organization_category, page_no=page_no, page_size=page_size, country=country)
        pprint(api_response)
    except com.mydatamyconsent.ApiException as e:
        print("Exception when calling DataProviderDiscoveryApi->v1_data_providers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_type** | **str**| Account type. | [optional]
 **document_type** | **str**| Document type. | [optional]
 **organization_category** | **str**| Organization category. | [optional]
 **page_no** | **int**| Page number. | [optional]
 **page_size** | **int**| Page size. | [optional]
 **country** | **str**| ISO2 Country code. | [optional] if omitted the server will use the default value of "IN"

### Return type

[**DataProviderPaginatedList**](DataProviderPaginatedList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**401** | Unauthorized. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_data_providers_provider_id_get**
> DataProvider v1_data_providers_provider_id_get(provider_id)

Get a Data Provider details.

.

### Example

```python
import time
import com.mydatamyconsent
from com.mydatamyconsent.api import data_provider_discovery_api
from com.mydatamyconsent.model.data_provider import DataProvider
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = com.mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with com.mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_provider_discovery_api.DataProviderDiscoveryApi(api_client)
    provider_id = "providerId_example" # str | Provider Id.

    # example passing only required values which don't have defaults set
    try:
        # Get a Data Provider details.
        api_response = api_instance.v1_data_providers_provider_id_get(provider_id)
        pprint(api_response)
    except com.mydatamyconsent.ApiException as e:
        print("Exception when calling DataProviderDiscoveryApi->v1_data_providers_provider_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider Id. |

### Return type

[**DataProvider**](DataProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**401** | Unauthorized. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

