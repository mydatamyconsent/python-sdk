# mydatamyconsent.DocumentsApi

All URIs are relative to *https://api.mydatamyconsent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_issued_document_by_id**](DocumentsApi.md#get_issued_document_by_id) | **GET** /v1/documents/issued/{documentId} | Get issued document.
[**get_issued_documents**](DocumentsApi.md#get_issued_documents) | **GET** /v1/documents/issued | Get paginated list of issued documents of given document type.
[**get_registered_document_types**](DocumentsApi.md#get_registered_document_types) | **GET** /v1/documents/types | Get paginated list of registered document types.
[**issue_document_to_individual**](DocumentsApi.md#issue_document_to_individual) | **POST** /v1/documents/issue/individual | Issue a new document to an individual user.
[**issue_document_to_organization**](DocumentsApi.md#issue_document_to_organization) | **POST** /v1/documents/issue/organization | Issue a new document to an organization.
[**upload_document_for_individual**](DocumentsApi.md#upload_document_for_individual) | **POST** /v1/documents/issue/individual/upload/{issueRequestId} | Upload a document for issuance request of individual.
[**upload_document_for_organization**](DocumentsApi.md#upload_document_for_organization) | **POST** /v1/documents/issue/organization/upload/{issueRequestId} | Upload a document for issuance request of organization.


# **get_issued_document_by_id**
> IssuedDocumentDetails get_issued_document_by_id(document_id)

Get issued document.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
from mydatamyconsent.model.issued_document_details import IssuedDocumentDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    document_id = "documentId_example" # str | Document id.

    # example passing only required values which don't have defaults set
    try:
        # Get issued document.
        api_response = api_instance.get_issued_document_by_id(document_id)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->get_issued_document_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document id. |

### Return type

[**IssuedDocumentDetails**](IssuedDocumentDetails.md)

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

# **get_issued_documents**
> IssuedDocumentPaginatedList get_issued_documents()

Get paginated list of issued documents of given document type.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
from mydatamyconsent.model.issued_document_paginated_list import IssuedDocumentPaginatedList
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    document_type_id = "documentTypeId_example" # str | Document type id. (optional)
    from_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | From DateTime in UTC timezone. (optional)
    to_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | To DateTime in UTC timezone. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get paginated list of issued documents of given document type.
        api_response = api_instance.get_issued_documents(document_type_id=document_type_id, from_date_time=from_date_time, to_date_time=to_date_time, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->get_issued_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_type_id** | **str**| Document type id. | [optional]
 **from_date_time** | **datetime**| From DateTime in UTC timezone. | [optional]
 **to_date_time** | **datetime**| To DateTime in UTC timezone. | [optional]
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25

### Return type

[**IssuedDocumentPaginatedList**](IssuedDocumentPaginatedList.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registered_document_types**
> DocumentTypePaginatedList get_registered_document_types()

Get paginated list of registered document types.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
from mydatamyconsent.model.supported_entity_type import SupportedEntityType
from mydatamyconsent.model.document_type_paginated_list import DocumentTypePaginatedList
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    supported_entity_type = SupportedEntityType("Individual") # SupportedEntityType | Supported entity type. (optional)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get paginated list of registered document types.
        api_response = api_instance.get_registered_document_types(supported_entity_type=supported_entity_type, page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->get_registered_document_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supported_entity_type** | **SupportedEntityType**| Supported entity type. | [optional]
 **page_no** | **int**| Page number. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Number of items to return. | [optional] if omitted the server will use the default value of 25

### Return type

[**DocumentTypePaginatedList**](DocumentTypePaginatedList.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_document_to_individual**
> DocumentIssueRequestDetails issue_document_to_individual(document_issue_request)

Issue a new document to an individual user.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
from mydatamyconsent.model.document_issue_request_details import DocumentIssueRequestDetails
from mydatamyconsent.model.document_issue_request import DocumentIssueRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    document_issue_request = DocumentIssueRequest(
        document_type_id="document_type_id_example",
        identifier="GJ05FG67866586.",
        description="description_example",
        receiver=DocumentReceiver(
            country_iso2_code="country_iso2_code_example",
            identifiers=[
                StringStringKeyValuePair(
                    key="key_example",
                    value="value_example",
                ),
            ],
            identification_strategy=IdentificationStrategy("MatchAtLeastOneIdentifier"),
        ),
        issued_at_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
        valid_from_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expires_at_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
        payment_request=PaymentRequest(
            identifier="identifier_example",
            amount="amount_example",
            currency_code="currency_code_example",
            payment_url="payment_url_example",
            description="description_example",
            due_by_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        metadata={
            "key": "key_example",
        },
    ) # DocumentIssueRequest | Document issue request payload

    # example passing only required values which don't have defaults set
    try:
        # Issue a new document to an individual user.
        api_response = api_instance.issue_document_to_individual(document_issue_request)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->issue_document_to_individual: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_issue_request** | [**DocumentIssueRequest**](DocumentIssueRequest.md)| Document issue request payload |

### Return type

[**DocumentIssueRequestDetails**](DocumentIssueRequestDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_document_to_organization**
> DocumentIssueRequestDetails issue_document_to_organization(document_issue_request)

Issue a new document to an organization.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
from mydatamyconsent.model.document_issue_request_details import DocumentIssueRequestDetails
from mydatamyconsent.model.document_issue_request import DocumentIssueRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    document_issue_request = DocumentIssueRequest(
        document_type_id="document_type_id_example",
        identifier="GJ05FG67866586.",
        description="description_example",
        receiver=DocumentReceiver(
            country_iso2_code="country_iso2_code_example",
            identifiers=[
                StringStringKeyValuePair(
                    key="key_example",
                    value="value_example",
                ),
            ],
            identification_strategy=IdentificationStrategy("MatchAtLeastOneIdentifier"),
        ),
        issued_at_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
        valid_from_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expires_at_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
        payment_request=PaymentRequest(
            identifier="identifier_example",
            amount="amount_example",
            currency_code="currency_code_example",
            payment_url="payment_url_example",
            description="description_example",
            due_by_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        metadata={
            "key": "key_example",
        },
    ) # DocumentIssueRequest | Document issue request payload

    # example passing only required values which don't have defaults set
    try:
        # Issue a new document to an organization.
        api_response = api_instance.issue_document_to_organization(document_issue_request)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->issue_document_to_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_issue_request** | [**DocumentIssueRequest**](DocumentIssueRequest.md)| Document issue request payload |

### Return type

[**DocumentIssueRequestDetails**](DocumentIssueRequestDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document_for_individual**
> upload_document_for_individual(issue_request_id, form_file)

Upload a document for issuance request of individual.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    issue_request_id = "issueRequestId_example" # str | Document issue request id.
    form_file = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # Upload a document for issuance request of individual.
        api_instance.upload_document_for_individual(issue_request_id, form_file)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->upload_document_for_individual: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_request_id** | **str**| Document issue request id. |
 **form_file** | **file_type**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document_for_organization**
> upload_document_for_organization(issue_request_id, form_file)

Upload a document for issuance request of organization.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
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
    api_instance = documents_api.DocumentsApi(api_client)
    issue_request_id = "issueRequestId_example" # str | Document issue request id System.Guid.
    form_file = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # Upload a document for issuance request of organization.
        api_instance.upload_document_for_organization(issue_request_id, form_file)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->upload_document_for_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_request_id** | **str**| Document issue request id System.Guid. |
 **form_file** | **file_type**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

