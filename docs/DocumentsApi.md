# mydatamyconsent.DocumentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_issued_document_by_id**](DocumentsApi.md#get_issued_document_by_id) | **GET** /v1/documents/issued/{documentId} | Get issued document.
[**get_issued_documents**](DocumentsApi.md#get_issued_documents) | **GET** /v1/documents/issued | Get issued documents.
[**get_registered_document_types**](DocumentsApi.md#get_registered_document_types) | **GET** /v1/documents/types | Get registered document types.
[**issue_document**](DocumentsApi.md#issue_document) | **POST** /v1/documents/issue | Issue a new document.


# **get_issued_document_by_id**
> IssuedDocument get_issued_document_by_id(document_id)

Get issued document.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.issued_document import IssuedDocument
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
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

[**IssuedDocument**](IssuedDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Server Error |  -  |
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issued_documents**
> IssuedDocumentPaginatedList get_issued_documents()

Get issued documents.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
from mydatamyconsent.model.issued_document_paginated_list import IssuedDocumentPaginatedList
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
    api_instance = documents_api.DocumentsApi(api_client)
    document_type_id = "documentTypeId_example" # str |  (optional)
    from_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    to_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    page_no = 1 # int |  (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get issued documents.
        api_response = api_instance.get_issued_documents(document_type_id=document_type_id, from_date_time=from_date_time, to_date_time=to_date_time, page_size=page_size, page_no=page_no)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->get_issued_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_type_id** | **str**|  | [optional]
 **from_date_time** | **datetime**|  | [optional]
 **to_date_time** | **datetime**|  | [optional]
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **page_no** | **int**|  | [optional] if omitted the server will use the default value of 1

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
**500** | Server Error |  -  |
**200** | Success |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registered_document_types**
> DocumentTypePaginatedList get_registered_document_types()

Get registered document types.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.document_type_paginated_list import DocumentTypePaginatedList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    page_no = 1 # int | Page number. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Number of items to return. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get registered document types.
        api_response = api_instance.get_registered_document_types(page_no=page_no, page_size=page_size)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->get_registered_document_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**500** | Server Error |  -  |
**200** | Success |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_document**
> IssuedDocument issue_document(document_issue_request)

Issue a new document.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
from mydatamyconsent.model.document_issue_request import DocumentIssueRequest
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.issued_document import IssuedDocument
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    document_issue_request = DocumentIssueRequest(
        document_type_id="document_type_id_example",
        document_identifier="document_identifier_example",
        name="name_example",
        description="description_example",
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
        expires_at_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
        base64_pdf_document="base64_pdf_document_example",
        metadata=None,
    ) # DocumentIssueRequest | Document issue request MyDataMyConsent.Models.Documents.DocumentIssueRequest.

    # example passing only required values which don't have defaults set
    try:
        # Issue a new document.
        api_response = api_instance.issue_document(document_issue_request)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->issue_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_issue_request** | [**DocumentIssueRequest**](DocumentIssueRequest.md)| Document issue request MyDataMyConsent.Models.Documents.DocumentIssueRequest. |

### Return type

[**IssuedDocument**](IssuedDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Server Error |  -  |
**200** | Success |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

