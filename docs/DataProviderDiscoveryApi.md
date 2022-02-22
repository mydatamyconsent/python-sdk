# mydatamyconsent.DataProviderDiscoveryApi

All URIs are relative to *https://api.mydatamyconsent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_provider_by_id**](DataProviderDiscoveryApi.md#get_data_provider_by_id) | **GET** /v1/data-providers/{providerId} | Get a Data Provider details based on provider id.
[**get_data_providers**](DataProviderDiscoveryApi.md#get_data_providers) | **GET** /v1/data-providers | Discover all data providers in My Data My Consent by country and filters.


# **get_data_provider_by_id**
> DataProvider get_data_provider_by_id(provider_id)

Get a Data Provider details based on provider id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_provider_discovery_api
from mydatamyconsent.model.data_provider import DataProvider
from mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_provider_discovery_api.DataProviderDiscoveryApi(api_client)
    provider_id = "providerId_example" # str | Provider id.

    # example passing only required values which don't have defaults set
    try:
        # Get a Data Provider details based on provider id.
        api_response = api_instance.get_data_provider_by_id(provider_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProviderDiscoveryApi->get_data_provider_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id. |

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
**200** | Success |  -  |
**500** | Server Error |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_providers**
> DataProviderPaginatedList get_data_providers()

Discover all data providers in My Data My Consent by country and filters.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_provider_discovery_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.data_provider_paginated_list import DataProviderPaginatedList
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_provider_discovery_api.DataProviderDiscoveryApi(api_client)
    account_type = "accountType_example" # str | Account type. (optional)
    document_type = "documentType_example" # str | Document type. (optional)
    organization_category = "organizationCategory_example" # str | Organization category. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25
    country = "IN" # str | ISO2 Country code. (optional) if omitted the server will use the default value of "IN"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Discover all data providers in My Data My Consent by country and filters.
        api_response = api_instance.get_data_providers(account_type=account_type, document_type=document_type, organization_category=organization_category, page_no=page_no, page_size=page_size, country=country)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProviderDiscoveryApi->get_data_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_type** | **str**| Account type. | [optional]
 **document_type** | **str**| Document type. | [optional]
 **organization_category** | **str**| Organization category. | [optional]
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25
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
**200** | Success |  -  |
**500** | Server Error |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

