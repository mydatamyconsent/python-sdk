# DataConsentRequestDetails

DataConsentRequestResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Consent request id | 
**title** | **str** | Consent request title. | 
**description** | **str** | Consent request description. | 
**status** | [**DataConsentStatus**](DataConsentStatus.md) |  | 
**created_at_utc** | **datetime** | Request creation datetime in UTC timezone | 
**expires_at_utc** | **datetime** | Request expiration datetime in UTC timezone | 
**template_id** | **str, none_type** | Consent request template id | [optional] 
**consent_id** | **str, none_type** | Data Consent id | [optional] 
**purpose** | **str, none_type** | Consent request purpose. | [optional] 
**transaction_id** | **str, none_type** | Transaction id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


