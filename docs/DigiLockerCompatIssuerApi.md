# mydatamyconsent.DigiLockerCompatIssuerApi

All URIs are relative to *https://api.mydatamyconsent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**digilocker_compat_issue_document**](DigiLockerCompatIssuerApi.md#digilocker_compat_issue_document) | **POST** /issuer/issuedoc/1/xml | Digilocker Compatible endpoint to issue document.


# **digilocker_compat_issue_document**
> PushUriResponse digilocker_compat_issue_document()

Digilocker Compatible endpoint to issue document.

### Example


```python
import time
import mydatamyconsent
from mydatamyconsent.api import digi_locker_compat_issuer_api
from mydatamyconsent.model.push_uri_request import PushUriRequest
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.push_uri_response import PushUriResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.mydatamyconsent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mydatamyconsent.Configuration(
    host = "https://api.mydatamyconsent.com"
)


# Enter a context with an instance of the API client
with mydatamyconsent.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = digi_locker_compat_issuer_api.DigiLockerCompatIssuerApi(api_client)
    push_uri_request = PushUriRequest(
        uri_details=UriDetails(
            aadhaar="aadhaar_example",
            uri="uri_example",
            doc_type="doc_type_example",
            doc_name="doc_name_example",
            doc_id="doc_id_example",
            issued_on="issued_on_example",
            valid_from="valid_from_example",
            valid_to="valid_to_example",
            timestamp="timestamp_example",
            action="action_example",
        ),
        ns2="ns2_example",
        ver="ver_example",
        ts="ts_example",
        txn="txn_example",
        org_id="org_id_example",
        keyhash="keyhash_example",
    ) # PushUriRequest | Push uri request MyDataMyConsent.Models.DigiLocker.PushUriRequest. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Digilocker Compatible endpoint to issue document.
        api_response = api_instance.digilocker_compat_issue_document(push_uri_request=push_uri_request)
        pprint(api_response)
    except mydatamyconsent.ApiException as e:
        print("Exception when calling DigiLockerCompatIssuerApi->digilocker_compat_issue_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_uri_request** | [**PushUriRequest**](PushUriRequest.md)| Push uri request MyDataMyConsent.Models.DigiLocker.PushUriRequest. | [optional]

### Return type

[**PushUriResponse**](PushUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**404** | Not Found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

