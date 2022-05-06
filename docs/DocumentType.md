# DocumentType

Issuable Document Type details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document Type Identifier. | 
**category_type** | [**DocumentCategoryType**](DocumentCategoryType.md) |  | 
**sub_category_type** | [**DocumentSubCategoryType**](DocumentSubCategoryType.md) |  | 
**name** | **str** | Document Type Name. eg: Driving License. | 
**slug** | **str** | Document Type Unique Slug. eg: \&quot;in.gov.gj.transport.dl\&quot;. | 
**logo_url** | **str** | Logo URL of document type. | 
**supported_entity_types** | [**[SupportedEntityType]**](SupportedEntityType.md) | Supported entity types. eg: Individual, Organization. | 
**added_by** | **str** | Name of the document type creator. | 
**payable_amount** | **float** | Payable amount if document is chargeable. eg: 10.25. | 
**description** | **str, none_type** | Document Type description. eg: Gujarat State Driving License. | [optional] 
**search_service_name** | **str, none_type** | Document search repository service name. | [optional] 
**repository_service_name** | **str, none_type** | Document repository service name. | [optional] 
**payable_amount_currency** | **str, none_type** | Payable amount currency. eg: INR, USD etc.,. | [optional] 
**approved_at_utc** | **datetime, none_type** | DateTime of approval in UTC timezone. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


