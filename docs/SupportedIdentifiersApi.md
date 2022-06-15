# mydatamyconsent.SupportedIdentifiersApi

All URIs are relative to *https://api.mydatamyconsent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_supported_identifiers**](SupportedIdentifiersApi.md#get_all_supported_identifiers) | **GET** /v1/supported-identifiers/{countryIso2Code} | Get all supported identifiers by country.


# **get_all_supported_identifiers**
> SupportedIdentifier get_all_supported_identifiers(country_iso2_code)

Get all supported identifiers by country.

Get all supported identifiers by country.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import supported_identifiers_api
from mydatamyconsent.model.error import Error
from mydatamyconsent.model.supported_identifier import SupportedIdentifier
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = supported_identifiers_api.SupportedIdentifiersApi(api_client)
    country_iso2_code = "countryIso2Code_example" # str | Country ISO 2 code.

    # example passing only required values which don't have defaults set
    try:
        # Get all supported identifiers by country.
        api_response = api_instance.get_all_supported_identifiers(country_iso2_code)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling SupportedIdentifiersApi->get_all_supported_identifiers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_iso2_code** | **str**| Country ISO 2 code. |

### Return type

[**SupportedIdentifier**](SupportedIdentifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

