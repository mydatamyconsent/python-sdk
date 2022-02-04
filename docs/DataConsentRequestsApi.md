# mydatamyconsent.DataConsentRequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_consent_request**](DataConsentRequestsApi.md#cancel_consent_request) | **DELETE** /v1/consent-requests/{requestId}/cancel | Revoke / Cancel the ConsentRequest based on Id.
[**create_request**](DataConsentRequestsApi.md#create_request) | **POST** /v1/consent-requests | Create a consent request.
[**get_all_consent_requests_to_individuals**](DataConsentRequestsApi.md#get_all_consent_requests_to_individuals) | **GET** /v1/consent-requests/individuals | Get all Consent Requests sent to Individuals.
[**get_all_consent_requests_to_organizations**](DataConsentRequestsApi.md#get_all_consent_requests_to_organizations) | **GET** /v1/consent-requests/organizations | Get All Consent Requests sent to Organizations
[**get_individual_consent_request_by_id**](DataConsentRequestsApi.md#get_individual_consent_request_by_id) | **GET** /v1/consent-requests/individuals/{requestId} | Get a Consent Request by ID.
[**get_organization_consent_request_by_id**](DataConsentRequestsApi.md#get_organization_consent_request_by_id) | **GET** /v1/consent-requests/organizations/{requestId} | Get a OrganizationConsent Request by Id


# **cancel_consent_request**
> bool cancel_consent_request(request_id)

Revoke / Cancel the ConsentRequest based on Id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
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
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    request_id = "requestId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke / Cancel the ConsentRequest based on Id.
        api_response = api_instance.cancel_consent_request(request_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->cancel_consent_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  |

### Return type

**bool**

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

# **create_request**
> bool create_request()

Create a consent request.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.data_consent_request_model import DataConsentRequestModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    data_consent_request_model = DataConsentRequestModel(
        consent_template_id="consent_template_id_example",
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expiry_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        receiver=Receiver(
            type=ReceiverType("Individual"),
            identifiers=[
                IdentifierStringKeyValuePair(
                    key=Identifier("Email"),
                    value="value_example",
                ),
            ],
            identification_strategy=IdentificationStrategy("MatchAtLeastOneIdentifier"),
        ),
    ) # DataConsentRequestModel | MyDataMyConsent.Models.Consents.DataConsentRequestModel. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a consent request.
        api_response = api_instance.create_request(data_consent_request_model=data_consent_request_model)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->create_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_consent_request_model** | [**DataConsentRequestModel**](DataConsentRequestModel.md)| MyDataMyConsent.Models.Consents.DataConsentRequestModel. | [optional]

### Return type

**bool**

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
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_consent_requests_to_individuals**
> dict get_all_consent_requests_to_individuals()

Get all Consent Requests sent to Individuals.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
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
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    page_no = 1 # int |  (optional)
    page_size = 1 # int |  (optional)
    status = DataConsentStatus("Pending") # DataConsentStatus |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all Consent Requests sent to Individuals.
        api_response = api_instance.get_all_consent_requests_to_individuals(page_no=page_no, page_size=page_size, status=status)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_all_consent_requests_to_individuals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_no** | **int**|  | [optional]
 **page_size** | **int**|  | [optional]
 **status** | **DataConsentStatus**|  | [optional]

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
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_consent_requests_to_organizations**
> dict get_all_consent_requests_to_organizations()

Get All Consent Requests sent to Organizations

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
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
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    page_no = 1 # int |  (optional)
    page_size = 1 # int |  (optional)
    status = DataConsentStatus("Pending") # DataConsentStatus |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get All Consent Requests sent to Organizations
        api_response = api_instance.get_all_consent_requests_to_organizations(page_no=page_no, page_size=page_size, status=status)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_all_consent_requests_to_organizations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_no** | **int**|  | [optional]
 **page_size** | **int**|  | [optional]
 **status** | **DataConsentStatus**|  | [optional]

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
**500** | Server Error |  -  |
**0** | Error |  -  |

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
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    request_id = "requestId_example" # str | 

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
 **request_id** | **str**|  |

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

# **get_organization_consent_request_by_id**
> DataConsentDetailsDto get_organization_consent_request_by_id(request_id)

Get a OrganizationConsent Request by Id

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_consent_requests_api
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
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    request_id = "requestId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a OrganizationConsent Request by Id
        api_response = api_instance.get_organization_consent_request_by_id(request_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_organization_consent_request_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  |

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

