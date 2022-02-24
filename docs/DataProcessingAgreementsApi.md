# mydatamyconsent.DataProcessingAgreementsApi

All URIs are relative to *https://api.mydatamyconsent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_processing_agreement**](DataProcessingAgreementsApi.md#create_data_processing_agreement) | **POST** /v1/data-agreements | Create a data processing agreement.
[**delete_data_processing_agreement_by_id**](DataProcessingAgreementsApi.md#delete_data_processing_agreement_by_id) | **DELETE** /v1/data-agreements/{id} | Delete a data processing agreement. This will not delete a published or a agreement in use with consents.
[**get_data_processing_agreement_by_id**](DataProcessingAgreementsApi.md#get_data_processing_agreement_by_id) | **GET** /v1/data-agreements/{id} | Get data processing agreement by id.
[**get_data_processing_agreements**](DataProcessingAgreementsApi.md#get_data_processing_agreements) | **GET** /v1/data-agreements | Get all data processing agreements.
[**terminate_data_processing_agreement_by_id**](DataProcessingAgreementsApi.md#terminate_data_processing_agreement_by_id) | **PUT** /v1/data-agreements/{id}/terminate | Terminate a data processing agreement.
[**update_data_processing_agreement**](DataProcessingAgreementsApi.md#update_data_processing_agreement) | **PUT** /v1/data-agreements/{id} | Update a data processing agreement.


# **create_data_processing_agreement**
> DataProcessingAgreementDto create_data_processing_agreement()

Create a data processing agreement.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
from mydatamyconsent.model.create_data_processing_agreement_request_model import CreateDataProcessingAgreementRequestModel
from mydatamyconsent.model.data_processing_agreement_dto import DataProcessingAgreementDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_processing_agreements_api.DataProcessingAgreementsApi(api_client)
    create_data_processing_agreement_request_model = CreateDataProcessingAgreementRequestModel(
        version="version_example",
        body="body_example",
        attachment_url="attachment_url_example",
    ) # CreateDataProcessingAgreementRequestModel | Create data processing agreement MyDataMyConsent.Models.DataProcessingAgreements.CreateDataProcessingAgreementRequestModel. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a data processing agreement.
        api_response = api_instance.create_data_processing_agreement(create_data_processing_agreement_request_model=create_data_processing_agreement_request_model)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->create_data_processing_agreement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_data_processing_agreement_request_model** | [**CreateDataProcessingAgreementRequestModel**](CreateDataProcessingAgreementRequestModel.md)| Create data processing agreement MyDataMyConsent.Models.DataProcessingAgreements.CreateDataProcessingAgreementRequestModel. | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_processing_agreement_by_id**
> delete_data_processing_agreement_by_id(id)

Delete a data processing agreement. This will not delete a published or a agreement in use with consents.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_processing_agreements_api.DataProcessingAgreementsApi(api_client)
    id = "id_example" # str | Agreement id.

    # example passing only required values which don't have defaults set
    try:
        # Delete a data processing agreement. This will not delete a published or a agreement in use with consents.
        api_instance.delete_data_processing_agreement_by_id(id)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->delete_data_processing_agreement_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Agreement id. |

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
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_processing_agreement_by_id**
> DataProcessingAgreementDto get_data_processing_agreement_by_id(id)

Get data processing agreement by id.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
from mydatamyconsent.model.data_processing_agreement_dto import DataProcessingAgreementDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_processing_agreements_api.DataProcessingAgreementsApi(api_client)
    id = "id_example" # str | Agreement id.

    # example passing only required values which don't have defaults set
    try:
        # Get data processing agreement by id.
        api_response = api_instance.get_data_processing_agreement_by_id(id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->get_data_processing_agreement_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Agreement id. |

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
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_processing_agreements**
> DataProcessingAgreementDtoPaginatedList get_data_processing_agreements()

Get all data processing agreements.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
from mydatamyconsent.model.data_processing_agreement_dto_paginated_list import DataProcessingAgreementDtoPaginatedList
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
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
        api_response = api_instance.get_data_processing_agreements(page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->get_data_processing_agreements: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_data_processing_agreement_by_id**
> terminate_data_processing_agreement_by_id(id)

Terminate a data processing agreement.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_processing_agreements_api.DataProcessingAgreementsApi(api_client)
    id = "id_example" # str | Agreement id.

    # example passing only required values which don't have defaults set
    try:
        # Terminate a data processing agreement.
        api_instance.terminate_data_processing_agreement_by_id(id)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->terminate_data_processing_agreement_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Agreement id. |

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
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_processing_agreement**
> DataProcessingAgreementDto update_data_processing_agreement(id)

Update a data processing agreement.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import data_processing_agreements_api
from mydatamyconsent.model.update_data_processing_agreement_request_model import UpdateDataProcessingAgreementRequestModel
from mydatamyconsent.model.data_processing_agreement_dto import DataProcessingAgreementDto
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_processing_agreements_api.DataProcessingAgreementsApi(api_client)
    id = "id_example" # str | Agreement id.
    update_data_processing_agreement_request_model = UpdateDataProcessingAgreementRequestModel(
        version="version_example",
        body="body_example",
        attachment_url="attachment_url_example",
    ) # UpdateDataProcessingAgreementRequestModel | Updated data processing agreement MyDataMyConsent.Models.DataProcessingAgreements.UpdateDataProcessingAgreementRequestModel. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a data processing agreement.
        api_response = api_instance.update_data_processing_agreement(id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->update_data_processing_agreement: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a data processing agreement.
        api_response = api_instance.update_data_processing_agreement(id, update_data_processing_agreement_request_model=update_data_processing_agreement_request_model)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DataProcessingAgreementsApi->update_data_processing_agreement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Agreement id. |
 **update_data_processing_agreement_request_model** | [**UpdateDataProcessingAgreementRequestModel**](UpdateDataProcessingAgreementRequestModel.md)| Updated data processing agreement MyDataMyConsent.Models.DataProcessingAgreements.UpdateDataProcessingAgreementRequestModel. | [optional]

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
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

