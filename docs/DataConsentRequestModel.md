# DataConsentRequestModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | [optional] 
**transaction_id** | **str, none_type** |  | [optional] 
**identifiers** | **{str: (str,)}, none_type** |  | [optional] 
**start_date_time** | **datetime, none_type** |  | [optional] 
**expiry_date_time** | **datetime** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**purpose_code** | **str, none_type** |  | [optional] 
**purpose_link** | **str, none_type** |  | [optional] 
**data_life_unit** | [**DataLifeUnit**](DataLifeUnit.md) |  | [optional] 
**data_life_value** | **int** |  | [optional] 
**data_fetch_frequency_unit** | [**DataFetchFrequencyUnit**](DataFetchFrequencyUnit.md) |  | [optional] 
**data_fetch_frequency_unit_value** | **int** |  | [optional] 
**data_fetch_type** | [**DataFetchType**](DataFetchType.md) |  | [optional] 
**agreement_id** | **str** |  | [optional] 
**identity_claims** | [**[IdentityClaim], none_type**](IdentityClaim.md) |  | [optional] 
**financial_accounts** | [**[DataConsentRequestedFaDto], none_type**](DataConsentRequestedFaDto.md) |  | [optional] 
**documents** | [**[DataConsentRequestedDocumentDto], none_type**](DataConsentRequestedDocumentDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


