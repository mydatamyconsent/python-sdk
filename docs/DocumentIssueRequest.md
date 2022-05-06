# DocumentIssueRequest

Document Issue Request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type_id** | **str** | Document type id. | 
**identifier** | **str** | Document identifier. | 
**description** | **str** | Document description. | 
**receiver** | [**DocumentReceiver**](DocumentReceiver.md) |  | 
**issued_at_utc** | **datetime** | Datetime of issue in UTC timezone. | 
**valid_from_utc** | **datetime** | Valid from datetime in UTC timezone. | 
**expires_at_utc** | **datetime, none_type** | Datetime of expiry in UTC timezone. | [optional] 
**payment_request** | [**PaymentRequest**](PaymentRequest.md) |  | [optional] 
**metadata** | **{str: (str,)}, none_type** | Metadata. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


