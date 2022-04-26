# DataConsentDocument

Data Consent document details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document id. | 
**name** | **str** | Document name. | 
**category** | **str** | Document category. | 
**identifier** | **str** | Document identifier. | 
**field_title** | **str** | Document field title. | 
**field_slug** | **str** | Document field slug. | 
**issued_at_utc** | **datetime** | Document issued at datetime in UTC timezone. | 
**issuer** | [**DataConsentDocumentIssuer**](DataConsentDocumentIssuer.md) |  | 
**digital_signatures** | [**[DocumentDigitalSignature]**](DocumentDigitalSignature.md) | Digital signatures. | 
**expires_at_utc** | **datetime, none_type** | Document expires at datetime in UTC timezone. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


