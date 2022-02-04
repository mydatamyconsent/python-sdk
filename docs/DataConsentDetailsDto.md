# DataConsentDetailsDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | [**DataConsentStatus**](DataConsentStatus.md) |  | [optional] 
**approved_at_utc** | **datetime, none_type** |  | [optional] 
**rejected_at_utc** | **datetime, none_type** |  | [optional] 
**expires_at_utc** | **datetime** |  | [optional] 
**requested_at_utc** | **datetime** |  | [optional] 
**requester** | [**DataConsentRequesterDto**](DataConsentRequesterDto.md) |  | [optional] 
**consent_details** | [**GetConsentTemplateDetailsDto**](GetConsentTemplateDetailsDto.md) |  | [optional] 
**identifiers** | [**[DataConsentIdentifier], none_type**](DataConsentIdentifier.md) |  | [optional] 
**approved_documents** | [**[DataConsentRequestedDocument], none_type**](DataConsentRequestedDocument.md) |  | [optional] 
**approved_financials** | [**[DataConsentRequestedFinancialAccount], none_type**](DataConsentRequestedFinancialAccount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


