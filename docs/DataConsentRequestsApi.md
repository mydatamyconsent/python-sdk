# com.mydatamyconsent.DataConsentRequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_consent_request**](DataConsentRequestsApi.md#cancel_consent_request) | **DELETE** /v1/consent-requests/{requestId}/cancel | Cancel a Consent Request by ID.
[**create_request**](DataConsentRequestsApi.md#create_request) | **POST** /v1/consent-requests | Create a consent request.
[**get_all_consent_requests**](DataConsentRequestsApi.md#get_all_consent_requests) | **GET** /v1/consent-requests | Get all Consent Requests.
[**get_consent_request_by_id**](DataConsentRequestsApi.md#get_consent_request_by_id) | **GET** /v1/consent-requests/{requestId} | Get a Consent Request by ID.


# **cancel_consent_request**
> cancel_consent_request(request_id)

Cancel a Consent Request by ID.

.

### Example

```python
import time
import com.mydatamyconsent
from com.mydatamyconsent.api import data_consent_requests_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = com.mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with com.mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    request_id = "requestId_example" # str | consent request id.

    # example passing only required values which don't have defaults set
    try:
        # Cancel a Consent Request by ID.
        api_instance.cancel_consent_request(request_id)
    except com.mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->cancel_consent_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| consent request id. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_request**
> DataConsent create_request()

Create a consent request.

### Example

```python
import time
import com.mydatamyconsent
from com.mydatamyconsent.api import data_consent_requests_api
from com.mydatamyconsent.model.data_consent import DataConsent
from com.mydatamyconsent.model.data_consent_request_model import DataConsentRequestModel
from com.mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = com.mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with com.mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    data_consent_request_model = DataConsentRequestModel(
        organization_id="organization_id_example",
        transaction_id="transaction_id_example",
        identifiers={
            "key": "key_example",
        },
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expiry_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        description="description_example",
        purpose_code="purpose_code_example",
        purpose_link="purpose_link_example",
        data_life_unit=DataLifeUnit("Month"),
        data_life_value=1,
        data_fetch_frequency_unit=DataFetchFrequencyUnit("Hourly"),
        data_fetch_frequency_unit_value=1,
        data_fetch_type=DataFetchType("Onetime"),
        agreement_id="agreement_id_example",
        identity_claims=[
            IdentityClaim("Email"),
        ],
        financial_accounts=[
            DataConsentRequestedFaDto(
                drn="drn_example",
                from_datetime=dateutil_parser('1970-01-01T00:00:00.00Z'),
                to_datetime=dateutil_parser('1970-01-01T00:00:00.00Z'),
                provider_id="provider_id_example",
                account_type=FinancialAccountTypes("SavingsBankAccount"),
                account_identifier="account_identifier_example",
                filters=[
                    DataConsentRfaFilterDto(
                        filter_type=FilterType("TransactionType"),
                        operator=Operator("EqualTo"),
                        value="value_example",
                    ),
                ],
            ),
        ],
        documents=[
            DataConsentRequestedDocumentDto(
                drn="drn_example",
                from_datetime=dateutil_parser('1970-01-01T00:00:00.00Z'),
                to_datetime=dateutil_parser('1970-01-01T00:00:00.00Z'),
                provider_id="provider_id_example",
                document_type_id="document_type_id_example",
                document_identifier="document_identifier_example",
            ),
        ],
    ) # DataConsentRequestModel | MyDataMyConsent.Models.Consents.DataConsentRequestModel. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a consent request.
        api_response = api_instance.create_request(data_consent_request_model=data_consent_request_model)
        pprint(api_response)
    except com.mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->create_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_consent_request_model** | [**DataConsentRequestModel**](DataConsentRequestModel.md)| MyDataMyConsent.Models.Consents.DataConsentRequestModel. | [optional]

### Return type

[**DataConsent**](DataConsent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_consent_requests**
> dict get_all_consent_requests()

Get all Consent Requests.

### Example

```python
import time
import com.mydatamyconsent
from com.mydatamyconsent.api import data_consent_requests_api
from com.mydatamyconsent.model.data_consent_status import DataConsentStatus
from com.mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = com.mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with com.mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    status = DataConsentStatus("Pending") # DataConsentStatus |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all Consent Requests.
        api_response = api_instance.get_all_consent_requests(status=status)
        pprint(api_response)
    except com.mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_all_consent_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **DataConsentStatus**|  | [optional]

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

# **get_consent_request_by_id**
> DataConsentDetailsDto get_consent_request_by_id(request_id)

Get a Consent Request by ID.

### Example

```python
import time
import com.mydatamyconsent
from com.mydatamyconsent.api import data_consent_requests_api
from com.mydatamyconsent.model.data_consent_details_dto import DataConsentDetailsDto
from com.mydatamyconsent.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = com.mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with com.mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_consent_requests_api.DataConsentRequestsApi(api_client)
    request_id = "requestId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a Consent Request by ID.
        api_response = api_instance.get_consent_request_by_id(request_id)
        pprint(api_response)
    except com.mydatamyconsent.ApiException as e:
        print("Exception when calling DataConsentRequestsApi->get_consent_request_by_id: %s\n" % e)
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
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

