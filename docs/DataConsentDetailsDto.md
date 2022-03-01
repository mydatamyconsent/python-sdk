# DataConsentDetailsDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**data_life** | [**Life**](Life.md) |  | [optional] 
**requested_by_org** | [**Requester**](Requester.md) |  | [optional] 
**status** | [**DataConsentStatus**](DataConsentStatus.md) |  | [optional] 
**approved_at_utc** | **datetime, none_type** |  | [optional] 
**rejected_at_utc** | **datetime, none_type** |  | [optional] 
**expires_at_utc** | **datetime** |  | [optional] 
**requested_at_utc** | **datetime** |  | [optional] 
**identifiers** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**documents** | [**[DataConsentDocumentDetailsDto], none_type**](DataConsentDocumentDetailsDto.md) |  | [optional] 
**financials** | **str, none_type** |  | [optional] 
**health_records** | **str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


