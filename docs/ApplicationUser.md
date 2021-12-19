# ApplicationUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_name** | **str, none_type** |  | [optional] 
**normalized_user_name** | **str, none_type** |  | [optional] 
**email** | **str, none_type** |  | [optional] 
**normalized_email** | **str, none_type** |  | [optional] 
**email_confirmed** | **bool** |  | [optional] 
**password_hash** | **str, none_type** |  | [optional] 
**security_stamp** | **str, none_type** |  | [optional] 
**concurrency_stamp** | **str, none_type** |  | [optional] 
**phone_number** | **str, none_type** |  | [optional] 
**phone_number_confirmed** | **bool** |  | [optional] 
**two_factor_enabled** | **bool** |  | [optional] 
**lockout_end** | **datetime, none_type** |  | [optional] 
**lockout_enabled** | **bool** |  | [optional] 
**access_failed_count** | **int** |  | [optional] 
**first_name** | **str, none_type** |  | [optional] 
**middle_name** | **str, none_type** |  | [optional] 
**last_name** | **str, none_type** |  | [optional] 
**full_name** | **str, none_type** |  | [optional] [readonly] 
**gender** | [**Gender**](Gender.md) |  | [optional] 
**date_of_birth** | **datetime** |  | [optional] 
**country_id** | **str** |  | [optional] 
**post_code** | **str, none_type** |  | [optional] 
**referred_by** | **str, none_type** |  | [optional] 
**language** | **str, none_type** |  | [optional] 
**theme** | [**Theme**](Theme.md) |  | [optional] 
**designation** | **str, none_type** |  | [optional] 
**is_marked_for_deletion** | **bool** |  | [optional] 
**hard_delete_date** | **datetime, none_type** |  | [optional] 
**security_pin** | **str, none_type** |  | [optional] 
**photo_url** | **str, none_type** |  | [optional] 
**referral_code** | **str, none_type** |  | [optional] 
**recovery_token** | **str, none_type** |  | [optional] 
**digi_locker_last_sync_date** | **datetime, none_type** |  | [optional] 
**refresh_tokens** | [**[RefreshToken], none_type**](RefreshToken.md) |  | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**referred_by_user** | [**ApplicationUser**](ApplicationUser.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


