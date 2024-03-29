# IssuedDocumentDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document Id. | 
**identifier** | **str** | Document Identifier. | 
**document_type** | **str** | Document type name. | 
**issued_to** | **str** | User name. | 
**issued_at_utc** | **datetime** | Issued datetime in UTC timezone. | 
**receiver** | [**DocumentReceiver**](DocumentReceiver.md) |  | 
**digital_signatures** | [**[DocumentDigitalSignature]**](DocumentDigitalSignature.md) | Digital signatures. | 
**expires_at_utc** | **datetime, none_type** | Expires datetime in UTC timezone. | [optional] 
**accepted_at_utc** | **datetime, none_type** | Accepted datetime in UTC timezone. | [optional] 
**metadata** | **{str: (str,)}, none_type** | Metadata. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


