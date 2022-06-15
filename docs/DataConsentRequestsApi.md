# mydatamyconsent.DataConsentRequestsApi

All URIs are relative to *https://api.mydatamyconsent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_individual_data_consent_request**](DataConsentRequestsApi.md#cancel_individual_data_consent_request) | **PUT** /v1/consent-requests/individual/{requestId}/cancel | Cancel the individual data consent request by Id.
[**cancel_organization_data_consent_request**](DataConsentRequestsApi.md#cancel_organization_data_consent_request) | **PUT** /v1/consent-requests/organization/{requestId}/cancel | Cancel the organization data consent request by Id.
[**create_individual_data_consent_request**](DataConsentRequestsApi.md#create_individual_data_consent_request) | **POST** /v1/consent-requests/individual | Create data consent request for an individual.
[**create_organization_data_consent_request**](DataConsentRequestsApi.md#create_organization_data_consent_request) | **POST** /v1/consent-requests/organization | Create data consent request for an organization.
[**get_all_consent_requests_to_individuals**](DataConsentRequestsApi.md#get_all_consent_requests_to_individuals) | **GET** /v1/consent-requests/individuals | Get all Consent Requests sent to individuals.
[**get_all_consent_requests_to_organizations**](DataConsentRequestsApi.md#get_all_consent_requests_to_organizations) | **GET** /v1/consent-requests/organizations | Get all Consent Requests sent to organizations.
[**get_individual_consent_request_by_id**](DataConsentRequestsApi.md#get_individual_consent_request_by_id) | **GET** /v1/consent-requests/individuals/{requestId} | Get individual data consent request by id.
[**get_organization_consent_request_by_id**](DataConsentRequestsApi.md#get_organization_consent_request_by_id) | **GET** /v1/consent-requests/organizations/{requestId} | Get a OrganizationConsent Request by Id.


# **cancel_individual_data_consent_request**
> cancel_individual_data_consent_request(request_id)

Cancel the individual data consent request by Id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    request_id = "requestId_example" # str | Individual consent request id.

    # example passing only required values which don't have defaults set
    try:
        # Cancel the individual data consent request by Id.
        api_instance.cancel_individual_data_consent_request(request_id)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->cancel_individual_data_consent_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Individual consent request id. |

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
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_organization_data_consent_request**
> cancel_organization_data_consent_request(request_id)

Cancel the organization data consent request by Id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    request_id = "requestId_example" # str | Organization consent request id.

    # example passing only required values which don't have defaults set
    try:
        # Cancel the organization data consent request by Id.
        api_instance.cancel_organization_data_consent_request(request_id)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->cancel_organization_data_consent_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Organization consent request id. |

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
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_individual_data_consent_request**
> IndividualDataConsentRequestDetails create_individual_data_consent_request(create_data_consent_request)

Create data consent request for an individual.

Create data consent request for an individual.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.error import Error
from mydatamyconsent.model.individual_data_consent_request_details import IndividualDataConsentRequestDetails
from mydatamyconsent.model.create_data_consent_request import CreateDataConsentRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    create_data_consent_request = CreateDataConsentRequest(
        consent_template_id="consent_template_id_example",
        receiver=ConsentRequestReceiver(
            country_iso2_code="country_iso2_code_example",
            identifiers=[
                StringStringKeyValuePair(
                    key="key_example",
                    value="value_example",
                ),
            ],
            identification_strategy=IdentificationStrategy("MatchAtLeastOneIdentifier"),
        ),
    ) # CreateDataConsentRequest | The Individual data consent request payload

    # example passing only required values which don't have defaults set
    try:
        # Create data consent request for an individual.
        api_response = api_instance.create_individual_data_consent_request(create_data_consent_request)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->create_individual_data_consent_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_data_consent_request** | [**CreateDataConsentRequest**](CreateDataConsentRequest.md)| The Individual data consent request payload |

### Return type

[**IndividualDataConsentRequestDetails**](IndividualDataConsentRequestDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_data_consent_request**
> OrganizationDataConsentRequestDetails create_organization_data_consent_request(create_data_consent_request)

Create data consent request for an organization.

Create data consent request for an organization.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.organization_data_consent_request_details import OrganizationDataConsentRequestDetails
from mydatamyconsent.model.error import Error
from mydatamyconsent.model.create_data_consent_request import CreateDataConsentRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    create_data_consent_request = CreateDataConsentRequest(
        consent_template_id="consent_template_id_example",
        receiver=ConsentRequestReceiver(
            country_iso2_code="country_iso2_code_example",
            identifiers=[
                StringStringKeyValuePair(
                    key="key_example",
                    value="value_example",
                ),
            ],
            identification_strategy=IdentificationStrategy("MatchAtLeastOneIdentifier"),
        ),
    ) # CreateDataConsentRequest | The Organization data consent request payload

    # example passing only required values which don't have defaults set
    try:
        # Create data consent request for an organization.
        api_response = api_instance.create_organization_data_consent_request(create_data_consent_request)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->create_organization_data_consent_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_data_consent_request** | [**CreateDataConsentRequest**](CreateDataConsentRequest.md)| The Organization data consent request payload |

### Return type

[**OrganizationDataConsentRequestDetails**](OrganizationDataConsentRequestDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_consent_requests_to_individuals**
> IndividualDataConsentRequestDetailsPaginatedList get_all_consent_requests_to_individuals()

Get all Consent Requests sent to individuals.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.data_consent_status import DataConsentStatus
from mydatamyconsent.model.error import Error
from mydatamyconsent.model.individual_data_consent_request_details_paginated_list import IndividualDataConsentRequestDetailsPaginatedList
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    status = DataConsentStatus("Pending") # DataConsentStatus | Data consent status. (optional)
    start_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Start datetime in UTC timezone. (optional)
    end_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | End datetime in UTC timezone. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all Consent Requests sent to individuals.
        api_response = api_instance.get_all_consent_requests_to_individuals(status=status, start_date_time=start_date_time, end_date_time=end_date_time, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_all_consent_requests_to_individuals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **DataConsentStatus**| Data consent status. | [optional]
 **start_date_time** | **datetime**| Start datetime in UTC timezone. | [optional]
 **end_date_time** | **datetime**| End datetime in UTC timezone. | [optional]
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25

### Return type

[**IndividualDataConsentRequestDetailsPaginatedList**](IndividualDataConsentRequestDetailsPaginatedList.md)

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_consent_requests_to_organizations**
> OrganizationDataConsentRequestDetailsPaginatedList get_all_consent_requests_to_organizations()

Get all Consent Requests sent to organizations.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.organization_data_consent_request_details_paginated_list import OrganizationDataConsentRequestDetailsPaginatedList
from mydatamyconsent.model.data_consent_status import DataConsentStatus
from mydatamyconsent.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    status = DataConsentStatus("Pending") # DataConsentStatus | Data consent status. (optional)
    start_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Start datetime in UTC timezone. (optional)
    end_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | End datetime in UTC timezone. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all Consent Requests sent to organizations.
        api_response = api_instance.get_all_consent_requests_to_organizations(status=status, start_date_time=start_date_time, end_date_time=end_date_time, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_all_consent_requests_to_organizations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **DataConsentStatus**| Data consent status. | [optional]
 **start_date_time** | **datetime**| Start datetime in UTC timezone. | [optional]
 **end_date_time** | **datetime**| End datetime in UTC timezone. | [optional]
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25

### Return type

[**OrganizationDataConsentRequestDetailsPaginatedList**](OrganizationDataConsentRequestDetailsPaginatedList.md)

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_individual_consent_request_by_id**
> DataConsentRequest get_individual_consent_request_by_id(request_id)

Get individual data consent request by id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.error import Error
from mydatamyconsent.model.data_consent_request import DataConsentRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    request_id = "requestId_example" # str | Individual data consent request id.

    # example passing only required values which don't have defaults set
    try:
        # Get individual data consent request by id.
        api_response = api_instance.get_individual_consent_request_by_id(request_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_individual_consent_request_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Individual data consent request id. |

### Return type

[**DataConsentRequest**](DataConsentRequest.md)

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
**400** | Bad Request |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_consent_request_by_id**
> DataConsentRequest get_organization_consent_request_by_id(request_id)

Get a OrganizationConsent Request by Id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.error import Error
from mydatamyconsent.model.data_consent_request import DataConsentRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    request_id = "requestId_example" # str | Organization consent request id.

    # example passing only required values which don't have defaults set
    try:
        # Get a OrganizationConsent Request by Id.
        api_response = api_instance.get_organization_consent_request_by_id(request_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_organization_consent_request_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Organization consent request id. |

### Return type

[**DataConsentRequest**](DataConsentRequest.md)

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
**400** | Bad Request |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

