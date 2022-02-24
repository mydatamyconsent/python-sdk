# mydatamyconsent.DataConsentRequestsApi

All URIs are relative to *https://api.mydatamyconsent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_individual_data_consent_request**](DataConsentRequestsApi.md#cancel_individual_data_consent_request) | **PUT** /v1/consent-requests/individual/{requestId}/cancel | Cancel the individual data consent request based on Id.
[**cancel_organization_data_consent_request**](DataConsentRequestsApi.md#cancel_organization_data_consent_request) | **PUT** /v1/consent-requests/organization/{requestId}/cancel | Cancel the Organization data consent request based on Id.
[**create_individual_data_consent_request**](DataConsentRequestsApi.md#create_individual_data_consent_request) | **POST** /v1/consent-requests/individual | Create a individual data consent request.
[**create_organization_data_consent_request**](DataConsentRequestsApi.md#create_organization_data_consent_request) | **POST** /v1/consent-requests/organization | Create a organization data consent request.
[**get_all_consent_requests_to_individuals**](DataConsentRequestsApi.md#get_all_consent_requests_to_individuals) | **GET** /v1/consent-requests/individuals | Get all Consent Requests sent to Individuals.
[**get_all_consent_requests_to_organizations**](DataConsentRequestsApi.md#get_all_consent_requests_to_organizations) | **GET** /v1/consent-requests/organizations | Get All Consent Requests sent to Organizations.
[**get_individual_consent_request_by_id**](DataConsentRequestsApi.md#get_individual_consent_request_by_id) | **GET** /v1/consent-requests/individuals/{requestId} | Get a Consent Request by ID.
[**get_organization_consent_request_by_id**](DataConsentRequestsApi.md#get_organization_consent_request_by_id) | **GET** /v1/consent-requests/organizations/{requestId} | Get a OrganizationConsent Request by Id.


# **cancel_individual_data_consent_request**
> IndividualDataConsentRequestResponse cancel_individual_data_consent_request(request_id)

Cancel the individual data consent request based on Id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.individual_data_consent_request_response import IndividualDataConsentRequestResponse
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
        # Cancel the individual data consent request based on Id.
        api_response = api_instance.cancel_individual_data_consent_request(request_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->cancel_individual_data_consent_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Individual consent request id. |

### Return type

[**IndividualDataConsentRequestResponse**](IndividualDataConsentRequestResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_organization_data_consent_request**
> OrganizationDataConsentRequestResponse cancel_organization_data_consent_request(request_id)

Cancel the Organization data consent request based on Id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.organization_data_consent_request_response import OrganizationDataConsentRequestResponse
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
        # Cancel the Organization data consent request based on Id.
        api_response = api_instance.cancel_organization_data_consent_request(request_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->cancel_organization_data_consent_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Organization consent request id. |

### Return type

[**OrganizationDataConsentRequestResponse**](OrganizationDataConsentRequestResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_individual_data_consent_request**
> IndividualDataConsentRequestResponse create_individual_data_consent_request(create_individual_data_consent_request)

Create a individual data consent request.

Create a individual data consent request.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.create_individual_data_consent_request import CreateIndividualDataConsentRequest
from mydatamyconsent.model.individual_data_consent_request_response import IndividualDataConsentRequestResponse
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
    create_individual_data_consent_request = CreateIndividualDataConsentRequest(
        consent_template_id="consent_template_id_example",
        receiver=Receiver(
            type=ReceiverType("Individual"),
            identifiers=[
                StringStringKeyValuePair(
                    key="key_example",
                    value="value_example",
                ),
            ],
            identification_strategy=IdentificationStrategy("MatchAtLeastOneIdentifier"),
        ),
    ) # CreateIndividualDataConsentRequest | The Individual data consent request payload

    # example passing only required values which don't have defaults set
    try:
        # Create a individual data consent request.
        api_response = api_instance.create_individual_data_consent_request(create_individual_data_consent_request)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->create_individual_data_consent_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_individual_data_consent_request** | [**CreateIndividualDataConsentRequest**](CreateIndividualDataConsentRequest.md)| The Individual data consent request payload |

### Return type

[**IndividualDataConsentRequestResponse**](IndividualDataConsentRequestResponse.md)

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
> OrganizationDataConsentRequestResponse create_organization_data_consent_request(create_organization_data_consent_request)

Create a organization data consent request.

Create a organization data consent request.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.organization_data_consent_request_response import OrganizationDataConsentRequestResponse
from mydatamyconsent.model.create_organization_data_consent_request import CreateOrganizationDataConsentRequest
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
    create_organization_data_consent_request = CreateOrganizationDataConsentRequest(
        consent_template_id="consent_template_id_example",
        receiver=Receiver(
            type=ReceiverType("Individual"),
            identifiers=[
                StringStringKeyValuePair(
                    key="key_example",
                    value="value_example",
                ),
            ],
            identification_strategy=IdentificationStrategy("MatchAtLeastOneIdentifier"),
        ),
    ) # CreateOrganizationDataConsentRequest | M:MyDataMyConsent.DeveloperApi.Controllers.DataConsentRequestsController.CreateOrganizationDataConsentRequest(MyDataMyConsent.DeveloperApi.Models.CreateOrganizationDataConsentRequest).

    # example passing only required values which don't have defaults set
    try:
        # Create a organization data consent request.
        api_response = api_instance.create_organization_data_consent_request(create_organization_data_consent_request)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->create_organization_data_consent_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_data_consent_request** | [**CreateOrganizationDataConsentRequest**](CreateOrganizationDataConsentRequest.md)| M:MyDataMyConsent.DeveloperApi.Controllers.DataConsentRequestsController.CreateOrganizationDataConsentRequest(MyDataMyConsent.DeveloperApi.Models.CreateOrganizationDataConsentRequest). |

### Return type

[**OrganizationDataConsentRequestResponse**](OrganizationDataConsentRequestResponse.md)

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
> UserDataConsentInfoDtoPaginatedList get_all_consent_requests_to_individuals()

Get all Consent Requests sent to Individuals.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
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
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    status = DataConsentStatus("Pending") # DataConsentStatus | Data consent status. (optional)
    start_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Start date time. (optional)
    end_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | End date time. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all Consent Requests sent to Individuals.
        api_response = api_instance.get_all_consent_requests_to_individuals(status=status, start_date_time=start_date_time, end_date_time=end_date_time, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_all_consent_requests_to_individuals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **DataConsentStatus**| Data consent status. | [optional]
 **start_date_time** | **datetime**| Start date time. | [optional]
 **end_date_time** | **datetime**| End date time. | [optional]
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

# **get_all_consent_requests_to_organizations**
> OrganizationDataConsentInfoDtoPaginatedList get_all_consent_requests_to_organizations()

Get All Consent Requests sent to Organizations.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
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
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    status = DataConsentStatus("Pending") # DataConsentStatus | Data consent status. (optional)
    start_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Start date time. (optional)
    end_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | End date time. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get All Consent Requests sent to Organizations.
        api_response = api_instance.get_all_consent_requests_to_organizations(status=status, start_date_time=start_date_time, end_date_time=end_date_time, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_all_consent_requests_to_organizations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **DataConsentStatus**| Data consent status. | [optional]
 **start_date_time** | **datetime**| Start date time. | [optional]
 **end_date_time** | **datetime**| End date time. | [optional]
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

# **get_individual_consent_request_by_id**
> DataConsentDetailsDto get_individual_consent_request_by_id(request_id)

Get a Consent Request by ID.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
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
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    request_id = "requestId_example" # str | Individual consent request id.

    # example passing only required values which don't have defaults set
    try:
        # Get a Consent Request by ID.
        api_response = api_instance.get_individual_consent_request_by_id(request_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_individual_consent_request_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Individual consent request id. |

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

# **get_organization_consent_request_by_id**
> DataConsentDetailsDto get_organization_consent_request_by_id(request_id)

Get a OrganizationConsent Request by Id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
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

