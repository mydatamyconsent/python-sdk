# OrganizationDataConsent

Organization data consent details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approver** | **str** | Name of consent approver organization. | 
**id** | **str** | Data consent id. | 
**title** | **str** | Consent title. | 
**description** | **str** | Consent description. | 
**status** | [**DataConsentStatus**](DataConsentStatus.md) |  | 
**approved_at_utc** | **datetime** | Consent approval datetime in UTC timezone. | 
**data_access_expires_at_utc** | **datetime** | Data access expiration datetime in UTC timezone. | 
**template_id** | **str, none_type** | Consent template id. | [optional] 
**purpose** | **str, none_type** | Consent purpose. | [optional] 
**transaction_id** | **str, none_type** | Transaction id. | [optional] 
**revoked_at_utc** | **datetime, none_type** | Consent revocation datetime in UTC timezone. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


