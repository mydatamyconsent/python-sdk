# DataConsentDetailsDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**requester** | [**DataConsentRequesterDto**](DataConsentRequesterDto.md) |  | [optional] 
**location** | **str, none_type** |  | [optional] 
**personal_info_requested** | **bool** |  | [optional] 
**documents** | **int** |  | [optional] 
**financial_accounts** | **int** |  | [optional] 
**transaction_id** | **str, none_type** |  | [optional] 
**ip_address** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**purpose_code** | **str, none_type** |  | [optional] 
**purpose_link** | **str, none_type** |  | [optional] 
**agreement_id** | **str, none_type** |  | [optional] 
**data_life_unit** | [**DataLifeUnit**](DataLifeUnit.md) |  | [optional] 
**data_life_value** | **int** |  | [optional] 
**data_fetch_frequency_unit** | [**DataFetchFrequencyUnit**](DataFetchFrequencyUnit.md) |  | [optional] 
**data_fetch_frequency_unit_value** | **int** |  | [optional] 
**data_fetch_type** | [**DataFetchType**](DataFetchType.md) |  | [optional] 
**status** | [**DataConsentStatus**](DataConsentStatus.md) |  | [optional] 
**approved_at_utc** | **datetime, none_type** |  | [optional] 
**rejected_at_utc** | **datetime, none_type** |  | [optional] 
**expires_at_utc** | **datetime** |  | [optional] 
**requested_at_utc** | **datetime** |  | [optional] 
**requested_financial_accounts** | [**[DataConsentRequestedAccountDto], none_type**](DataConsentRequestedAccountDto.md) |  | [optional] 
**requested_documents** | [**[DataConsentRequestedDocumentDto], none_type**](DataConsentRequestedDocumentDto.md) |  | [optional] 
**requested_health_data** | [**[DataConsentRequestedDocument], none_type**](DataConsentRequestedDocument.md) |  | [optional] 
**requested_identity_details** | [**JsonSchema**](JsonSchema.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


