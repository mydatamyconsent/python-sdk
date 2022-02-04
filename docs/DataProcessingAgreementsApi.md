# mydatamyconsent.DataProcessingAgreementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_data_agreements_get**](DataProcessingAgreementsApi.md#v1_data_agreements_get) | **GET** /v1/data-agreements | Get all data processing agreements.
[**v1_data_agreements_id_delete**](DataProcessingAgreementsApi.md#v1_data_agreements_id_delete) | **DELETE** /v1/data-agreements/{id} | Delete a data processing agreement. This will not delete a published or a agreement in use with consents.
[**v1_data_agreements_id_get**](DataProcessingAgreementsApi.md#v1_data_agreements_id_get) | **GET** /v1/data-agreements/{id} | Get data processing agreement by Id.
[**v1_data_agreements_id_put**](DataProcessingAgreementsApi.md#v1_data_agreements_id_put) | **PUT** /v1/data-agreements/{id} | Update a data processing agreement.
[**v1_data_agreements_id_terminate_put**](DataProcessingAgreementsApi.md#v1_data_agreements_id_terminate_put) | **PUT** /v1/data-agreements/{id}/terminate | Terminate a data processing agreement.
[**v1_data_agreements_post**](DataProcessingAgreementsApi.md#v1_data_agreements_post) | **POST** /v1/data-agreements | Create a data processing agreement.


# **v1_data_agreements_get**
> DataProcessingAgreementDtoPaginatedList v1_data_agreements_get()

Get all data processing agreements.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.data_processing_agreement_dto_paginated_list import DataProcessingAgreementDtoPaginatedList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_processing_agreements_api.DataProcessingAgreementsApi(api_client)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all data processing agreements.
        api_response = api_instance.v1_data_agreements_get(page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->v1_data_agreements_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25

### Return type

[**DataProcessingAgreementDtoPaginatedList**](DataProcessingAgreementDtoPaginatedList.md)

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

# **v1_data_agreements_id_delete**
> v1_data_agreements_id_delete(id)

Delete a data processing agreement. This will not delete a published or a agreement in use with consents.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
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
    api_instance = data_processing_agreements_api.DataProcessingAgreementsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a data processing agreement. This will not delete a published or a agreement in use with consents.
        api_instance.v1_data_agreements_id_delete(id)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->v1_data_agreements_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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
**204** | Success |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_data_agreements_id_get**
> DataProcessingAgreementDto v1_data_agreements_id_get(id)

Get data processing agreement by Id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.data_processing_agreement_dto import DataProcessingAgreementDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_processing_agreements_api.DataProcessingAgreementsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get data processing agreement by Id.
        api_response = api_instance.v1_data_agreements_id_get(id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->v1_data_agreements_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DataProcessingAgreementDto**](DataProcessingAgreementDto.md)

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

# **v1_data_agreements_id_put**
> DataProcessingAgreementDto v1_data_agreements_id_put(id)

Update a data processing agreement.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.update_data_processing_agreement_request_model import UpdateDataProcessingAgreementRequestModel
from mydatamyconsent.model.data_processing_agreement_dto import DataProcessingAgreementDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_processing_agreements_api.DataProcessingAgreementsApi(api_client)
    id = "id_example" # str | 
    update_data_processing_agreement_request_model = UpdateDataProcessingAgreementRequestModel(
        version="version_example",
        body="body_example",
        attachment_url="attachment_url_example",
    ) # UpdateDataProcessingAgreementRequestModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a data processing agreement.
        api_response = api_instance.v1_data_agreements_id_put(id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->v1_data_agreements_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a data processing agreement.
        api_response = api_instance.v1_data_agreements_id_put(id, update_data_processing_agreement_request_model=update_data_processing_agreement_request_model)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->v1_data_agreements_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **update_data_processing_agreement_request_model** | [**UpdateDataProcessingAgreementRequestModel**](UpdateDataProcessingAgreementRequestModel.md)|  | [optional]

### Return type

[**DataProcessingAgreementDto**](DataProcessingAgreementDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_data_agreements_id_terminate_put**
> v1_data_agreements_id_terminate_put(id)

Terminate a data processing agreement.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
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
    api_instance = data_processing_agreements_api.DataProcessingAgreementsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Terminate a data processing agreement.
        api_instance.v1_data_agreements_id_terminate_put(id)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->v1_data_agreements_id_terminate_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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
**204** | Success |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_data_agreements_post**
> DataProcessingAgreementDto v1_data_agreements_post()

Create a data processing agreement.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
from mydatamyconsent.model.create_data_processing_agreement_request_model import CreateDataProcessingAgreementRequestModel
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.data_processing_agreement_dto import DataProcessingAgreementDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_processing_agreements_api.DataProcessingAgreementsApi(api_client)
    create_data_processing_agreement_request_model = CreateDataProcessingAgreementRequestModel(
        version="version_example",
        body="body_example",
        attachment_url="attachment_url_example",
    ) # CreateDataProcessingAgreementRequestModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a data processing agreement.
        api_response = api_instance.v1_data_agreements_post(create_data_processing_agreement_request_model=create_data_processing_agreement_request_model)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->v1_data_agreements_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_data_processing_agreement_request_model** | [**CreateDataProcessingAgreementRequestModel**](CreateDataProcessingAgreementRequestModel.md)|  | [optional]

### Return type

[**DataProcessingAgreementDto**](DataProcessingAgreementDto.md)

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

