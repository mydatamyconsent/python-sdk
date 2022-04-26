# DataConsentRequest

Data consent request details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Data consent request id. | 
**title** | **str** | Data consent title. | 
**description** | **str** | Data consent description. | 
**collectables** | [**[CollectibleTypes]**](CollectibleTypes.md) | List of supported collectables. | 
**receiver** | [**ConsentRequestReceiver**](ConsentRequestReceiver.md) |  | 
**status** | [**DataConsentStatus**](DataConsentStatus.md) |  | 
**created_at_utc** | **datetime** | Request creation datetime in UTC timezone. | 
**expires_at_utc** | **datetime** | Request expiration datetime in UTC timezone. | 
**template_id** | **str, none_type** | Data consent template id. | [optional] 
**consent_id** | **str, none_type** | Data consent id. | [optional] 
**purpose** | **str, none_type** | Data consent purpose. | [optional] 
**data_life** | [**Life**](Life.md) |  | [optional] 
**approved_at_utc** | **datetime, none_type** | Request approval datetime in UTC timezone. | [optional] 
**data_access_expires_at_utc** | **datetime, none_type** | Data access expiration datetime in UTC timezone. | [optional] 
**rejected_at_utc** | **datetime, none_type** | Request rejection datetime in UTC timezone. | [optional] 
**revoked_at_utc** | **datetime, none_type** | Request revocation datetime in UTC timezone. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


