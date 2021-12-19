# mydatamyconsent.DocumentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issue_document**](DocumentsApi.md#issue_document) | **POST** /v1/documents/issue | Issue a new document.
[**v1_documents_issued_document_id_get**](DocumentsApi.md#v1_documents_issued_document_id_get) | **GET** /v1/documents/issued/{documentId} | Get issued document.
[**v1_documents_issued_get**](DocumentsApi.md#v1_documents_issued_get) | **GET** /v1/documents/issued | Get issued documents.
[**v1_documents_types_get**](DocumentsApi.md#v1_documents_types_get) | **GET** /v1/documents/types | Get registered document types.


# **issue_document**
> bool issue_document()

Issue a new document.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
from mydatamyconsent.model.document_issue_request import DocumentIssueRequest
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
    document_issue_request = DocumentIssueRequest(
        document_type_id="document_type_id_example",
        identifier="identifier_example",
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
        expires_at_utc="expires_at_utc_example",
        base64_pdf_document="base64_pdf_document_example",
        metadata=None,
    ) # DocumentIssueRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Issue a new document.
        api_response = api_instance.issue_document(document_issue_request=document_issue_request)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->issue_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_issue_request** | [**DocumentIssueRequest**](DocumentIssueRequest.md)|  | [optional]

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
**500** | Server Error |  -  |
**200** | Success |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_documents_issued_document_id_get**
> v1_documents_issued_document_id_get(document_id)

Get issued document.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
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
        api_instance.v1_documents_issued_document_id_get(document_id)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->v1_documents_issued_document_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document id. |

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_documents_issued_get**
> v1_documents_issued_get()

Get issued documents.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
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
        api_instance.v1_documents_issued_get(document_type_id=document_type_id, from_date_time=from_date_time, to_date_time=to_date_time, page_size=page_size, page_no=page_no)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->v1_documents_issued_get: %s\n" % e)
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

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_documents_types_get**
> v1_documents_types_get()

Get registered document types.

### Example

```python
import time
import mydatamyconsent
from mydatamyconsent.api import documents_api
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
    page_size = 1 # int |  (optional)
    page_no = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get registered document types.
        api_instance.v1_documents_types_get(page_size=page_size, page_no=page_no)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DocumentsApi->v1_documents_types_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**|  | [optional]
 **page_no** | **int**|  | [optional]

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

