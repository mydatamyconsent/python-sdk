# DocumentIssueRequestDetails

Document issue request details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document issue request Id. | 
**document_type_id** | **str** | Document type Id. | 
**type_name** | **str** | Document type name. | 
**identifier** | **str** | Document identifier. | 
**status** | [**DocumentIssueRequestStatus**](DocumentIssueRequestStatus.md) |  | 
**description** | **str** | Document description. | 
**receiver** | **bool, date, datetime, dict, float, int, list, str, none_type** | Document receiver details. | 
**issued_at_utc** | **datetime** | Datetime of issue in UTC timezone. | 
**valid_from_utc** | **datetime** | Valid from datetime in UTC timezone. | 
**created_at_utc** | **datetime** | Creation datetime of issue request in UTC timezone. | 
**expires_at_utc** | **datetime, none_type** | Datetime of expiry in UTC timezone. | [optional] 
**meta_data** | **bool, date, datetime, dict, float, int, list, str, none_type** | Metadata. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


