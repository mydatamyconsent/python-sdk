# DataConsent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_id** | **str, none_type** |  | [optional] 
**organization_id** | **str, none_type** |  | [optional] 
**requested_by_org_id** | **str** |  | [optional] 
**transaction_id** | **str, none_type** |  | [optional] 
**start_date_time** | **datetime, none_type** |  | [optional] 
**expiry_date_time** | **datetime** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**purpose_code** | **str, none_type** |  | [optional] 
**purpose_link** | **str, none_type** |  | [optional] 
**location** | **str, none_type** |  | [optional] 
**agreement_id** | **str** |  | [optional] 
**data_life_unit** | [**DataLifeUnit**](DataLifeUnit.md) |  | [optional] 
**data_life_value** | **int** |  | [optional] 
**data_fetch_frequency_unit** | [**DataFetchFrequencyUnit**](DataFetchFrequencyUnit.md) |  | [optional] 
**data_fetch_frequency_unit_value** | **int** |  | [optional] 
**data_fetch_type** | [**DataFetchType**](DataFetchType.md) |  | [optional] 
**status** | [**DataConsentStatus**](DataConsentStatus.md) |  | [optional] 
**created_at_utc** | **datetime** |  | [optional] 
**approved_at_utc** | **datetime, none_type** |  | [optional] 
**rejected_at_utc** | **datetime, none_type** |  | [optional] 
**user** | [**ApplicationUser**](ApplicationUser.md) |  | [optional] 
**organization** | [**Organization**](Organization.md) |  | [optional] 
**requested_by_org** | [**Organization**](Organization.md) |  | [optional] 
**agreement** | [**DataProcessingAgreement**](DataProcessingAgreement.md) |  | [optional] 
**identity_claims** | [**[IdentityClaim], none_type**](IdentityClaim.md) |  | [optional] 
**identifiers** | [**[DataConsentIdentifier], none_type**](DataConsentIdentifier.md) |  | [optional] 
**requested_financial_accounts** | [**[DataConsentRequestedFinancialAccount], none_type**](DataConsentRequestedFinancialAccount.md) |  | [optional] 
**requested_documents** | [**[DataConsentRequestedDocument], none_type**](DataConsentRequestedDocument.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


