# CloudWatch investigations API Reference

## Welcome

CloudWatch investigations API Reference
CloudWatch investigations
API Version 2018-05-10
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
## Actions

CloudWatch investigations CloudWatch investigations API Reference
CloudWatch investigations: CloudWatch investigations API Reference
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
Amazon's trademarks and trade dress may not be used in connection with any product or service 
that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any 
manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are 
the property of their respective owners, who may or may not be aﬃliated with, connected to, or 
sponsored by Amazon.
## CreateInvestigationGroup

## Request Syntax

CloudWatch investigations CloudWatch investigations API Reference
Table of Contents
Welcome ........................................................................................................................................... 1
Actions .............................................................................................................................................. 2
CreateInvestigationGroup ........................................................................................................................... 3
Request Syntax ........................................................................................................................................ 3
URI Request Parameters ........................................................................................................................ 4
Request Body ........................................................................................................................................... 4
Response Syntax ...................................................................................................................................... 7
Response Elements ................................................................................................................................. 8
Errors .......................................................................................................................................................... 8
Examples ................................................................................................................................................... 9
See Also .................................................................................................................................................. 10
DeleteInvestigationGroup ......................................................................................................................... 11
Request Syntax ...................................................................................................................................... 11
URI Request Parameters ...................................................................................................................... 11
Request Body ......................................................................................................................................... 11
Response Syntax ................................................................................................................................... 11
Response Elements ............................................................................................................................... 11
Errors ....................................................................................................................................................... 11
See Also .................................................................................................................................................. 12
DeleteInvestigationGroupPolicy .............................................................................................................. 14
Request Syntax ...................................................................................................................................... 14
URI Request Parameters ...................................................................................................................... 14
Request Body ......................................................................................................................................... 14
Response Syntax ................................................................................................................................... 14
Response Elements ............................................................................................................................... 14
Errors ....................................................................................................................................................... 14
See Also .................................................................................................................................................. 15
GetInvestigationGroup .............................................................................................................................. 17
Request Syntax ...................................................................................................................................... 17
URI Request Parameters ...................................................................................................................... 17
Request Body ......................................................................................................................................... 17
Response Syntax ................................................................................................................................... 17
Response Elements ............................................................................................................................... 18
Errors ....................................................................................................................................................... 21
API Version 2018-05-10 iii
## URI Request Parameters

## Request Body

CloudWatch investigations CloudWatch investigations API Reference
See Also .................................................................................................................................................. 22
GetInvestigationGroupPolicy .................................................................................................................... 23
Request Syntax ...................................................................................................................................... 23
URI Request Parameters ...................................................................................................................... 23
Request Body ......................................................................................................................................... 23
Response Syntax ................................................................................................................................... 23
Response Elements ............................................................................................................................... 24
Errors ....................................................................................................................................................... 24
See Also .................................................................................................................................................. 25
ListInvestigationGroups ............................................................................................................................. 27
Request Syntax ...................................................................................................................................... 27
URI Request Parameters ...................................................................................................................... 27
Request Body ......................................................................................................................................... 27
Response Syntax ................................................................................................................................... 27
Response Elements ............................................................................................................................... 28
Errors ....................................................................................................................................................... 28
See Also .................................................................................................................................................. 29
ListTagsForResource ................................................................................................................................... 31
Request Syntax ...................................................................................................................................... 31
URI Request Parameters ...................................................................................................................... 31
Request Body ......................................................................................................................................... 31
Response Syntax ................................................................................................................................... 31
Response Elements ............................................................................................................................... 32
Errors ....................................................................................................................................................... 32
See Also .................................................................................................................................................. 33
PutInvestigationGroupPolicy .................................................................................................................... 34
Request Syntax ...................................................................................................................................... 34
URI Request Parameters ...................................................................................................................... 34
Request Body ......................................................................................................................................... 35
Response Syntax ................................................................................................................................... 35
Response Elements ............................................................................................................................... 35
Errors ....................................................................................................................................................... 36
See Also .................................................................................................................................................. 37
TagResource ................................................................................................................................................. 38
Request Syntax ...................................................................................................................................... 38
URI Request Parameters ...................................................................................................................... 38
API Version 2018-05-10 iv
CloudWatch investigations CloudWatch investigations API Reference
Request Body ......................................................................................................................................... 38
Response Syntax ................................................................................................................................... 39
Response Elements ............................................................................................................................... 39
Errors ....................................................................................................................................................... 39
See Also .................................................................................................................................................. 40
UntagResource ............................................................................................................................................ 41
Request Syntax ...................................................................................................................................... 41
URI Request Parameters ...................................................................................................................... 41
Request Body ......................................................................................................................................... 41
Response Syntax ................................................................................................................................... 41
Response Elements ............................................................................................................................... 42
Errors ....................................................................................................................................................... 42
See Also .................................................................................................................................................. 43
UpdateInvestigationGroup ........................................................................................................................ 44
Request Syntax ...................................................................................................................................... 44
URI Request Parameters ...................................................................................................................... 44
Request Body ......................................................................................................................................... 45
Response Syntax ................................................................................................................................... 47
Response Elements ............................................................................................................................... 47
Errors ....................................................................................................................................................... 47
See Also .................................................................................................................................................. 48
Data Types ..................................................................................................................................... 49
CrossAccountConﬁguration ...................................................................................................................... 50
Contents .................................................................................................................................................. 50
See Also .................................................................................................................................................. 50
EncryptionConﬁguration ........................................................................................................................... 51
Contents .................................................................................................................................................. 51
See Also .................................................................................................................................................. 51
ListInvestigationGroupsModel ................................................................................................................. 52
Contents .................................................................................................................................................. 52
See Also .................................................................................................................................................. 52
Common Parameters ..................................................................................................................... 53
Common Error Types ..................................................................................................................... 56
API Version 2018-05-10 v
CloudWatch investigations CloudWatch investigations API Reference
Welcome
The CloudWatch investigations feature is a generative AI-powered assistant that can help you 
respond to incidents in your system. It uses generative AI to scan your system's telemetry and 
quickly surface suggestions that might be related to your issue. These suggestions include metrics, 
logs, deployment events, and root-cause hypotheses.
You can use API actions to create, manage, and delete investigation groups and investigation group 
policies. To start and manage investigations, you must use the CloudWatch console.
This document was last published on April 2, 2026.
API Version 2018-05-10 1
## Response Syntax

CloudWatch investigations CloudWatch investigations API Reference
Actions
The following actions are supported:
• CreateInvestigationGroup
• DeleteInvestigationGroup
• DeleteInvestigationGroupPolicy
• GetInvestigationGroup
• GetInvestigationGroupPolicy
• ListInvestigationGroups
• ListTagsForResource
• PutInvestigationGroupPolicy
• TagResource
• UntagResource
• UpdateInvestigationGroup
API Version 2018-05-10 2
## Response Elements

## Errors

CloudWatch investigations CloudWatch investigations API Reference
CreateInvestigationGroup
Creates an investigation group in your account. Creating an investigation group is a one-time setup 
task for each Region in your account. It is a necessary task to be able to perform investigations.
Settings in the investigation group help you centrally manage the common properties of your 
investigations, such as the following:
• Who can access the investigations
• Whether investigation data is encrypted with a customer managed AWS Key Management 
Service key.
• How long investigations and their data are retained by default.
Currently, you can have one investigation group in each Region in your account. Each investigation 
in a Region is a part of the investigation group in that Region
To create an investigation group and set up CloudWatch investigations, you must be signed in to 
an IAM principal that has either the AIOpsConsoleAdminPolicy or the AdministratorAccess
IAM policy attached, or to an account that has similar permissions.
Important
You can conﬁgure CloudWatch alarms to start investigations and add 
events to investigations. If you create your investigation group with
CreateInvestigationGroup and you want to enable alarms to do this, you must use
PutInvestigationGroupPolicy to create a resource policy that grants this permission 
to CloudWatch alarms.
For more information about conﬁguring CloudWatch alarms, see Using Amazon 
CloudWatch alarms
Request Syntax
POST /investigationGroups HTTP/1.1
Content-type: application/json
{ 
   "chatbotNotificationChannel": {  
CreateInvestigationGroup API Version 2018-05-10 3
## Examples

CloudWatch investigations CloudWatch investigations API Reference
      "string" : [ "string" ] 
   }, 
   "crossAccountConfigurations": [  
      {  
         "sourceRoleArn": "string" 
      } 
   ], 
   "encryptionConfiguration": {  
      "kmsKeyId": "string", 
      "type": "string" 
   }, 
   "isCloudTrailEventHistoryEnabled": boolean, 
   "name": "string", 
   "retentionInDays": number, 
   "roleArn": "string", 
   "tagKeyBoundaries": [ "string" ], 
   "tags": {  
      "string" : "string"  
   }
}
URI Request Parameters
The request does not use any URI parameters.
Request Body
The request accepts the following data in JSON format.
chatbotNotiﬁcationChannel
Use this structure to integrate CloudWatch investigations with chat applications. This structure 
is a string array. For the ﬁrst string, specify the ARN of an Amazon SNS topic. For the array of 
strings, specify the ARNs of one or more chat applications conﬁgurations that you want to 
associate with that topic. For more information about these conﬁguration ARNs, see Getting 
started with Amazon Q in chat applications and Resource type deﬁned by AWS Chatbot.
Type: String to array of strings map
Key Length Constraints: Minimum length of 20. Maximum length of 2048.
Key Pattern: arn:.*
URI Request Parameters API Version 2018-05-10 4
## See Also

CloudWatch investigations CloudWatch investigations API Reference
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: arn:.*
Required: No
crossAccountConﬁgurations
List of sourceRoleArn values that have been conﬁgured for cross-account access.
Type: Array of CrossAccountConﬁguration objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No
encryptionConﬁguration
Use this structure if you want to use a customer managed AWS KMS key to encrypt your 
investigation data. If you omit this parameter, CloudWatch investigations will use an AWS key to 
encrypt the data. For more information, see Encryption of investigation data.
Type: EncryptionConﬁguration object
Required: No
isCloudTrailEventHistoryEnabled
Specify true to enable CloudWatch investigations to have access to change events that are 
recorded by CloudTrail. The default is true.
Type: Boolean
Required: No
name
Provides a name for the investigation group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Request Body API Version 2018-05-10 5
## DeleteInvestigationGroup

## Request Syntax

## URI Request Parameters

## Request Body

## Response Syntax

## Response Elements

## Errors

CloudWatch investigations CloudWatch investigations API Reference
Pattern: [\-_A-Za-z0-9\[\]\(\)\{\}\.: ]+
Required: Yes
retentionInDays
Specify how long that investigation data is kept. For more information, see Operational 
investigation data retention.
If you omit this parameter, the default of 90 days is used.
Type: Long
Valid Range: Minimum value of 7. Maximum value of 90.
Required: No
roleArn
Specify the ARN of the IAM role that CloudWatch investigations will use when it gathers 
investigation data. The permissions in this role determine which of your resources that 
CloudWatch investigations will have access to during investigations.
For more information, see How to control what data CloudWatch investigations has access to 
during investigations.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: arn:.*
Required: Yes
tagKeyBoundaries
Enter the existing custom tag keys for custom applications in your system. Resource tags help 
CloudWatch investigations narrow the search space when it is unable to discover deﬁnite 
relationships between resources. For example, to discover that an Amazon ECS service depends 
on an Amazon RDS database, CloudWatch investigations can discover this relationship 
using data sources such as X-Ray and CloudWatch Application Signals. However, if you 
haven't deployed these features, CloudWatch investigations will attempt to identify possible 
relationships. Tag boundaries can be used to narrow the resources that will be discovered by 
CloudWatch investigations in these cases.
Request Body API Version 2018-05-10 6
## See Also

CloudWatch investigations CloudWatch investigations API Reference
You don't need to enter tags created by myApplications or CloudFormation, because 
CloudWatch investigations can automatically detect those tags.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: ([\p{L}\p{Z}\p{N}_.:/=+\-@]+)
Required: No
tags
A list of key-value pairs to associate with the investigation group. You can associate as many 
as 50 tags with an investigation group. To be able to associate tags when you create the 
investigation group, you must have the cloudwatch:TagResource permission.
Tags can help you organize and categorize your resources. You can also use them to scope user 
permissions by granting a user permission to access or change only resources with certain tag 
values.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: ([\p{L}\p{Z}\p{N}_.:/=+\-@]+)
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: ([\p{L}\p{Z}\p{N}_.:/=+\-@]*)
Required: No
Response Syntax
HTTP/1.1 201
Content-type: application/json
{ 
   "arn": "string"
}
Response Syntax API Version 2018-05-10 7
CloudWatch investigations CloudWatch investigations API Reference
Response Elements
If the action is successful, the service sends back an HTTP 201 response.
The following data is returned in JSON format by the service.
arn
The ARN of the investigation group that you just created.
Type: String
Pattern: arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:
[0-9]{12}:investigation-group\/[A-Za-z0-9]{16}
Errors
For information about the errors that are common to all actions, see Common Error Types.
AccessDeniedException
You don't have suﬃcient permissions to perform this action.
HTTP Status Code: 403
ConﬂictException
This operation couldn't be completed because of a conﬂict in resource states.
HTTP Status Code: 409
ForbiddenException
Access id denied for this operation, or this operation is not valid for the speciﬁed resource.
HTTP Status Code: 403
InternalServerException
An internal server error occurred. You can try again later.
HTTP Status Code: 500
ResourceNotFoundException
The speciﬁed resource doesn't exist.
Response Elements API Version 2018-05-10 8
## DeleteInvestigationGroupPolicy

## Request Syntax

## URI Request Parameters

## Request Body

## Response Syntax

## Response Elements

## Errors

CloudWatch investigations CloudWatch investigations API Reference
HTTP Status Code: 404
ServiceQuotaExceededException
This request exceeds a service quota.
quotaCode
This quota that was exceeded.
resourceId
The resource that caused the quota exception.
resourceType
The type of resource that caused the quota exception.
serviceCode
This name of the service associated with the error.
HTTP Status Code: 402
ThrottlingException
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429
ValidationException
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400
Examples
Example
The following example creates an investigation group.
Sample Request
{ 
    "name:": "TestInvestigationGroup", 
Examples API Version 2018-05-10 9
## See Also

CloudWatch investigations CloudWatch investigations API Reference
    "roleArn": "arn:aws:iam::123456789012:role/AdminNew", 
    "retentionInDays": 30
}
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-05-10 10
CloudWatch investigations CloudWatch investigations API Reference
DeleteInvestigationGroup
Deletes the speciﬁed investigation group from your account. You can currently have one 
investigation group per Region in your account. After you delete an investigation group, you can 
later create a new investigation group in the same Region.
Request Syntax
DELETE /investigationGroups/identifier HTTP/1.1
URI Request Parameters
The request uses the following URI parameters.
identiﬁer
Specify either the name or the ARN of the investigation group that you want to delete.
Pattern: (?:[\-_A-Za-z0-9]{1,512}|arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-
iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]
{16})
Required: Yes
Request Body
The request does not have a request body.
Response Syntax
HTTP/1.1 200
Response Elements
If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.
Errors
For information about the errors that are common to all actions, see Common Error Types.
DeleteInvestigationGroup API Version 2018-05-10 11
## GetInvestigationGroup

## Request Syntax

## URI Request Parameters

## Request Body

## Response Syntax

CloudWatch investigations CloudWatch investigations API Reference
AccessDeniedException
You don't have suﬃcient permissions to perform this action.
HTTP Status Code: 403
ConﬂictException
This operation couldn't be completed because of a conﬂict in resource states.
HTTP Status Code: 409
ForbiddenException
Access id denied for this operation, or this operation is not valid for the speciﬁed resource.
HTTP Status Code: 403
InternalServerException
An internal server error occurred. You can try again later.
HTTP Status Code: 500
ResourceNotFoundException
The speciﬁed resource doesn't exist.
HTTP Status Code: 404
ThrottlingException
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429
ValidationException
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
See Also API Version 2018-05-10 12
## Response Elements

CloudWatch investigations CloudWatch investigations API Reference
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-05-10 13
CloudWatch investigations CloudWatch investigations API Reference
DeleteInvestigationGroupPolicy
Removes the IAM resource policy from being associated with the investigation group that you 
specify.
Request Syntax
DELETE /investigationGroups/identifier/policy HTTP/1.1
URI Request Parameters
The request uses the following URI parameters.
identiﬁer
Specify either the name or the ARN of the investigation group that you want to remove the 
policy from.
Pattern: (?:[\-_A-Za-z0-9]{1,512}|arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-
iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]
{16})
Required: Yes
Request Body
The request does not have a request body.
Response Syntax
HTTP/1.1 200
Response Elements
If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.
Errors
For information about the errors that are common to all actions, see Common Error Types.
DeleteInvestigationGroupPolicy API Version 2018-05-10 14
CloudWatch investigations CloudWatch investigations API Reference
AccessDeniedException
You don't have suﬃcient permissions to perform this action.
HTTP Status Code: 403
ConﬂictException
This operation couldn't be completed because of a conﬂict in resource states.
HTTP Status Code: 409
ForbiddenException
Access id denied for this operation, or this operation is not valid for the speciﬁed resource.
HTTP Status Code: 403
InternalServerException
An internal server error occurred. You can try again later.
HTTP Status Code: 500
ResourceNotFoundException
The speciﬁed resource doesn't exist.
HTTP Status Code: 404
ThrottlingException
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429
ValidationException
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
See Also API Version 2018-05-10 15
## Errors

CloudWatch investigations CloudWatch investigations API Reference
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-05-10 16
CloudWatch investigations CloudWatch investigations API Reference
GetInvestigationGroup
Returns the conﬁguration information for the speciﬁed investigation group.
Request Syntax
GET /investigationGroups/identifier HTTP/1.1
URI Request Parameters
The request uses the following URI parameters.
identiﬁer
Specify either the name or the ARN of the investigation group that you want to view. This is 
used to set the name of the investigation group.
Pattern: (?:[\-_A-Za-z0-9]{1,512}|arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-
iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]
{16})
Required: Yes
Request Body
The request does not have a request body.
Response Syntax
HTTP/1.1 200
Content-type: application/json
{ 
   "arn": "string", 
   "chatbotNotificationChannel": {  
      "string" : [ "string" ] 
   }, 
   "createdAt": number, 
   "createdBy": "string", 
   "crossAccountConfigurations": [  
GetInvestigationGroup API Version 2018-05-10 17
CloudWatch investigations CloudWatch investigations API Reference
      {  
         "sourceRoleArn": "string" 
      } 
   ], 
   "encryptionConfiguration": {  
      "kmsKeyId": "string", 
      "type": "string" 
   }, 
   "isCloudTrailEventHistoryEnabled": boolean, 
   "lastModifiedAt": number, 
   "lastModifiedBy": "string", 
   "name": "string", 
   "retentionInDays": number, 
   "roleArn": "string", 
   "tagKeyBoundaries": [ "string" ]
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
arn
The Amazon Resource Name (ARN) of the investigation group.
Type: String
Pattern: arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:
[0-9]{12}:investigation-group\/[A-Za-z0-9]{16}
chatbotNotiﬁcationChannel
This structure is a string array. The ﬁrst string is the ARN of a Amazon SNS topic. The array of 
strings display the ARNs of chat applications conﬁgurations that are associated with that topic. 
For more information about these conﬁguration ARNs, see Getting started with Amazon Q in 
chat applications and Resource type deﬁned by AWS Chatbot.
Type: String to array of strings map
Key Length Constraints: Minimum length of 20. Maximum length of 2048.
Key Pattern: arn:.*
Response Elements API Version 2018-05-10 18
CloudWatch investigations CloudWatch investigations API Reference
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: arn:.*
createdAt
The date and time that the investigation group was created.
Type: Long
createdBy
The name of the user who created the investigation group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: [\-_\/A-Za-z0-9:\.]+
crossAccountConﬁgurations
Lists the AWSAccountId of the accounts conﬁgured for cross-account access and the results of 
the last scan performed on each account.
Type: Array of CrossAccountConﬁguration objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
encryptionConﬁguration
Speciﬁes the customer managed AWS KMS key that the investigation group uses to encrypt 
data, if there is one. If not, the investigation group uses an AWS key to encrypt the data.
Type: EncryptionConﬁguration object
isCloudTrailEventHistoryEnabled
Speciﬁes whether CloudWatch investigationshas access to change events that are recorded by 
CloudTrail.
Type: Boolean
lastModiﬁedAt
The date and time that the investigation group was most recently modiﬁed.
Response Elements API Version 2018-05-10 19
CloudWatch investigations CloudWatch investigations API Reference
Type: Long
lastModiﬁedBy
The name of the user who created the investigation group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: [\-_\/A-Za-z0-9:\.]+
name
The name of the investigation group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: [\-_A-Za-z0-9\[\]\(\)\{\}\.: ]+
retentionInDays
Speciﬁes how long that investigation data is kept.
Type: Long
Valid Range: Minimum value of 7. Maximum value of 90.
roleArn
The ARN of the IAM role that the investigation group uses for permissions to gather data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: arn:.*
tagKeyBoundaries
Displays the custom tag keys for custom applications in your system that you have speciﬁed in 
the investigation group. Resource tags help CloudWatch investigations narrow the search space 
when it is unable to discover deﬁnite relationships between resources.
Type: Array of strings
Response Elements API Version 2018-05-10 20
CloudWatch investigations CloudWatch investigations API Reference
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: ([\p{L}\p{Z}\p{N}_.:/=+\-@]+)
Errors
For information about the errors that are common to all actions, see Common Error Types.
AccessDeniedException
You don't have suﬃcient permissions to perform this action.
HTTP Status Code: 403
ConﬂictException
This operation couldn't be completed because of a conﬂict in resource states.
HTTP Status Code: 409
ForbiddenException
Access id denied for this operation, or this operation is not valid for the speciﬁed resource.
HTTP Status Code: 403
InternalServerException
An internal server error occurred. You can try again later.
HTTP Status Code: 500
ResourceNotFoundException
The speciﬁed resource doesn't exist.
HTTP Status Code: 404
ThrottlingException
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429
ValidationException
This operation or its parameters aren't formatted correctly.
Errors API Version 2018-05-10 21
CloudWatch investigations CloudWatch investigations API Reference
HTTP Status Code: 400
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-05-10 22
CloudWatch investigations CloudWatch investigations API Reference
GetInvestigationGroupPolicy
Returns the JSON of the IAM resource policy associated with the speciﬁed 
investigation group in a string. For example, {\"Version\":\"2012-10-17\",
\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service
\":\"aiops.alarms.cloudwatch.amazonaws.com\"},\"Action\":
[\"aiops:CreateInvestigation\",\"aiops:CreateInvestigationEvent\"],
\"Resource\":\"*\",\"Condition\":{\"StringEquals\":{\"aws:SourceAccount\":
\"111122223333\"},\"ArnLike\":{\"aws:SourceArn\":\"arn:aws:cloudwatch:us-
east-1:111122223333:alarm:*\"}}}]}.
Request Syntax
GET /investigationGroups/identifier/policy HTTP/1.1
URI Request Parameters
The request uses the following URI parameters.
identiﬁer
Specify either the name or the ARN of the investigation group that you want to view the policy 
of.
Pattern: (?:[\-_A-Za-z0-9]{1,512}|arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-
iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]
{16})
Required: Yes
Request Body
The request does not have a request body.
Response Syntax
HTTP/1.1 200
Content-type: application/json
GetInvestigationGroupPolicy API Version 2018-05-10 23
CloudWatch investigations CloudWatch investigations API Reference
{ 
   "investigationGroupArn": "string", 
   "policy": "string"
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
investigationGroupArn
The Amazon Resource Name (ARN) of the investigation group that you want to view the policy 
of.
Type: String
Pattern: arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:
[0-9]{12}:investigation-group\/[A-Za-z0-9]{16}
policy
The policy, in JSON format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: [\u0009\u000A\u000D\u0020-\u00FF]+
Errors
For information about the errors that are common to all actions, see Common Error Types.
AccessDeniedException
You don't have suﬃcient permissions to perform this action.
HTTP Status Code: 403
Response Elements API Version 2018-05-10 24
CloudWatch investigations CloudWatch investigations API Reference
ConﬂictException
This operation couldn't be completed because of a conﬂict in resource states.
HTTP Status Code: 409
ForbiddenException
Access id denied for this operation, or this operation is not valid for the speciﬁed resource.
HTTP Status Code: 403
InternalServerException
An internal server error occurred. You can try again later.
HTTP Status Code: 500
ResourceNotFoundException
The speciﬁed resource doesn't exist.
HTTP Status Code: 404
ThrottlingException
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429
ValidationException
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
See Also API Version 2018-05-10 25
CloudWatch investigations CloudWatch investigations API Reference
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-05-10 26
CloudWatch investigations CloudWatch investigations API Reference
ListInvestigationGroups
Returns the ARN and name of each investigation group in the account.
Request Syntax
GET /investigationGroups?maxResults=maxResults&nextToken=nextToken HTTP/1.1
URI Request Parameters
The request uses the following URI parameters.
maxResults
The maximum number of results to return in one operation. If you omit this parameter, the 
default of 50 is used.
Valid Range: Minimum value of 1. Maximum value of 50.
nextToken
Include this value, if it was returned by the previous operation, to get the next set of service 
operations.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Request Body
The request does not have a request body.
Response Syntax
HTTP/1.1 200
Content-type: application/json
{ 
   "investigationGroups": [  
      {  
         "arn": "string", 
         "name": "string" 
      } 
ListInvestigationGroups API Version 2018-05-10 27
CloudWatch investigations CloudWatch investigations API Reference
   ], 
   "nextToken": "string"
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
investigationGroups
An array of structures, where each structure contains the information about one investigation 
group in the account.
Type: Array of ListInvestigationGroupsModel objects
nextToken
Include this value in your next use of this operation to get the next set of service operations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Errors
For information about the errors that are common to all actions, see Common Error Types.
AccessDeniedException
You don't have suﬃcient permissions to perform this action.
HTTP Status Code: 403
ConﬂictException
This operation couldn't be completed because of a conﬂict in resource states.
HTTP Status Code: 409
ForbiddenException
Access id denied for this operation, or this operation is not valid for the speciﬁed resource.
Response Elements API Version 2018-05-10 28
CloudWatch investigations CloudWatch investigations API Reference
HTTP Status Code: 403
InternalServerException
An internal server error occurred. You can try again later.
HTTP Status Code: 500
ResourceNotFoundException
The speciﬁed resource doesn't exist.
HTTP Status Code: 404
ThrottlingException
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429
ValidationException
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-05-10 29
CloudWatch investigations CloudWatch investigations API Reference
See Also API Version 2018-05-10 30
CloudWatch investigations CloudWatch investigations API Reference
ListTagsForResource
Displays the tags associated with a CloudWatch investigations resource. Currently, investigation 
groups support tagging.
Request Syntax
GET /tags/resourceArn HTTP/1.1
URI Request Parameters
The request uses the following URI parameters.
resourceArn
The ARN of the CloudWatch investigations resource that you want to view tags for. You can use 
the ListInvestigationGroups operation to ﬁnd the ARNs of investigation groups.
The ARN format for an investigation group is arn:aws:aiops:Region:account-
id:investigation-group:investigation-group-id .
Required: Yes
Request Body
The request does not have a request body.
Response Syntax
HTTP/1.1 200
Content-type: application/json
{ 
   "tags": {  
      "string" : "string"  
   }
}
ListTagsForResource API Version 2018-05-10 31
CloudWatch investigations CloudWatch investigations API Reference
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
tags
The list of tag keys and values associated with the resource you speciﬁed.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: ([\p{L}\p{Z}\p{N}_.:/=+\-@]+)
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: ([\p{L}\p{Z}\p{N}_.:/=+\-@]*)
Errors
For information about the errors that are common to all actions, see Common Error Types.
AccessDeniedException
You don't have suﬃcient permissions to perform this action.
HTTP Status Code: 403
ConﬂictException
This operation couldn't be completed because of a conﬂict in resource states.
HTTP Status Code: 409
ForbiddenException
Access id denied for this operation, or this operation is not valid for the speciﬁed resource.
HTTP Status Code: 403
InternalServerException
An internal server error occurred. You can try again later.
Response Elements API Version 2018-05-10 32
CloudWatch investigations CloudWatch investigations API Reference
HTTP Status Code: 500
ResourceNotFoundException
The speciﬁed resource doesn't exist.
HTTP Status Code: 404
ThrottlingException
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429
ValidationException
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-05-10 33
CloudWatch investigations CloudWatch investigations API Reference
PutInvestigationGroupPolicy
Creates an IAM resource policy and assigns it to the speciﬁed investigation group.
If you create your investigation group with CreateInvestigationGroup and you want to enable 
CloudWatch alarms to create investigations and add events to investigations, you must use this 
operation to create a policy similar to this example.
{ "Version": "2008-10-17", "Statement": [ { "Effect": "Allow", "Principal": 
{ "Service": "aiops.alarms.cloudwatch.amazonaws.com" }, "Action": 
[ "aiops:CreateInvestigation", "aiops:CreateInvestigationEvent" ], 
"Resource": "*", "Condition": { "StringEquals": { "aws:SourceAccount": 
"account-id" }, "ArnLike": { "aws:SourceArn": 
"arn:aws:cloudwatch::123456789012:alarm:*" } } } ] }
Request Syntax
POST /investigationGroups/identifier/policy HTTP/1.1
Content-type: application/json
{ 
   "policy": "string"
}
URI Request Parameters
The request uses the following URI parameters.
identiﬁer
Specify either the name or the ARN of the investigation group that you want to assign the 
policy to.
Pattern: (?:[\-_A-Za-z0-9]{1,512}|arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-
iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]
{16})
Required: Yes
PutInvestigationGroupPolicy API Version 2018-05-10 34
CloudWatch investigations CloudWatch investigations API Reference
Request Body
The request accepts the following data in JSON format.
policy
The policy, in JSON format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: [\u0009\u000A\u000D\u0020-\u00FF]+
Required: Yes
Response Syntax
HTTP/1.1 200
Content-type: application/json
{ 
   "investigationGroupArn": "string"
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
investigationGroupArn
The ARN of the investigation group that will use this policy.
Type: String
Pattern: arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:
[0-9]{12}:investigation-group\/[A-Za-z0-9]{16}
Request Body API Version 2018-05-10 35
CloudWatch investigations CloudWatch investigations API Reference
Errors
For information about the errors that are common to all actions, see Common Error Types.
AccessDeniedException
You don't have suﬃcient permissions to perform this action.
HTTP Status Code: 403
ConﬂictException
This operation couldn't be completed because of a conﬂict in resource states.
HTTP Status Code: 409
ForbiddenException
Access id denied for this operation, or this operation is not valid for the speciﬁed resource.
HTTP Status Code: 403
InternalServerException
An internal server error occurred. You can try again later.
HTTP Status Code: 500
ResourceNotFoundException
The speciﬁed resource doesn't exist.
HTTP Status Code: 404
ThrottlingException
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429
ValidationException
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400
Errors API Version 2018-05-10 36
CloudWatch investigations CloudWatch investigations API Reference
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-05-10 37
CloudWatch investigations CloudWatch investigations API Reference
TagResource
Assigns one or more tags (key-value pairs) to the speciﬁed resource.
Tags can help you organize and categorize your resources. You can also use them to scope user 
permissions by granting a user permission to access or change only resources with certain tag 
values.
Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.
You can associate as many as 50 tags with a resource.
Request Syntax
POST /tags/resourceArn HTTP/1.1
Content-type: application/json
{ 
   "tags": {  
      "string" : "string"  
   }
}
URI Request Parameters
The request uses the following URI parameters.
resourceArn
The Amazon Resource Name (ARN) of the resource that you want to apply the tags to. You can 
use the ListInvestigationGroups operation to ﬁnd the ARNs of investigation groups.
Required: Yes
Request Body
The request accepts the following data in JSON format.
tags
The list of key-value pairs to associate with the resource.
TagResource API Version 2018-05-10 38
CloudWatch investigations CloudWatch investigations API Reference
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: ([\p{L}\p{Z}\p{N}_.:/=+\-@]+)
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: ([\p{L}\p{Z}\p{N}_.:/=+\-@]*)
Required: Yes
Response Syntax
HTTP/1.1 200
Response Elements
If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.
Errors
For information about the errors that are common to all actions, see Common Error Types.
AccessDeniedException
You don't have suﬃcient permissions to perform this action.
HTTP Status Code: 403
ConﬂictException
This operation couldn't be completed because of a conﬂict in resource states.
HTTP Status Code: 409
ForbiddenException
Access id denied for this operation, or this operation is not valid for the speciﬁed resource.
HTTP Status Code: 403
Response Syntax API Version 2018-05-10 39
CloudWatch investigations CloudWatch investigations API Reference
InternalServerException
An internal server error occurred. You can try again later.
HTTP Status Code: 500
ResourceNotFoundException
The speciﬁed resource doesn't exist.
HTTP Status Code: 404
ThrottlingException
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429
ValidationException
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-05-10 40
CloudWatch investigations CloudWatch investigations API Reference
UntagResource
Removes one or more tags from the speciﬁed resource.
Request Syntax
DELETE /tags/resourceArn?tagKeys=tagKeys HTTP/1.1
URI Request Parameters
The request uses the following URI parameters.
resourceArn
The Amazon Resource Name (ARN) of the resource that you want to remove the tags from. You 
can use theListInvestigationGroups operation to ﬁnd the ARNs of investigation groups.
Required: Yes
tagKeys
The list of tag keys to remove from the resource.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: ([\p{L}\p{Z}\p{N}_.:/=+\-@]+)
Required: Yes
Request Body
The request does not have a request body.
Response Syntax
HTTP/1.1 200
UntagResource API Version 2018-05-10 41
CloudWatch investigations CloudWatch investigations API Reference
Response Elements
If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.
Errors
For information about the errors that are common to all actions, see Common Error Types.
AccessDeniedException
You don't have suﬃcient permissions to perform this action.
HTTP Status Code: 403
ConﬂictException
This operation couldn't be completed because of a conﬂict in resource states.
HTTP Status Code: 409
ForbiddenException
Access id denied for this operation, or this operation is not valid for the speciﬁed resource.
HTTP Status Code: 403
InternalServerException
An internal server error occurred. You can try again later.
HTTP Status Code: 500
ResourceNotFoundException
The speciﬁed resource doesn't exist.
HTTP Status Code: 404
ThrottlingException
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429
ValidationException
This operation or its parameters aren't formatted correctly.
Response Elements API Version 2018-05-10 42
CloudWatch investigations CloudWatch investigations API Reference
HTTP Status Code: 400
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-05-10 43
CloudWatch investigations CloudWatch investigations API Reference
UpdateInvestigationGroup
Updates the conﬁguration of the speciﬁed investigation group.
Request Syntax
PATCH /investigationGroups/identifier HTTP/1.1
Content-type: application/json
{ 
   "chatbotNotificationChannel": {  
      "string" : [ "string" ] 
   }, 
   "crossAccountConfigurations": [  
      {  
         "sourceRoleArn": "string" 
      } 
   ], 
   "encryptionConfiguration": {  
      "kmsKeyId": "string", 
      "type": "string" 
   }, 
   "isCloudTrailEventHistoryEnabled": boolean, 
   "roleArn": "string", 
   "tagKeyBoundaries": [ "string" ]
}
URI Request Parameters
The request uses the following URI parameters.
identiﬁer
Specify either the name or the ARN of the investigation group that you want to modify.
Pattern: (?:[\-_A-Za-z0-9]{1,512}|arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-
iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]
{16})
Required: Yes
UpdateInvestigationGroup API Version 2018-05-10 44
CloudWatch investigations CloudWatch investigations API Reference
Request Body
The request accepts the following data in JSON format.
chatbotNotiﬁcationChannel
Use this structure to integrate CloudWatch investigations with chat applications. This structure 
is a string array. For the ﬁrst string, specify the ARN of an Amazon SNS topic. For the array of 
strings, specify the ARNs of one or more chat applications conﬁgurations that you want to 
associate with that topic. For more information about these conﬁguration ARNs, see Getting 
started with Amazon Q in chat applications and Resource type deﬁned by AWS Chatbot.
Type: String to array of strings map
Key Length Constraints: Minimum length of 20. Maximum length of 2048.
Key Pattern: arn:.*
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: arn:.*
Required: No
crossAccountConﬁgurations
Used to conﬁgure cross-account access for an investigation group. It allows the investigation 
group to access resources in other accounts.
Type: Array of CrossAccountConﬁguration objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No
encryptionConﬁguration
Use this structure if you want to use a customer managed AWS KMS key to encrypt your 
investigation data. If you omit this parameter, CloudWatch investigations will use an AWS key to 
encrypt the data. For more information, see Encryption of investigation data.
Type: EncryptionConﬁguration object
Request Body API Version 2018-05-10 45
CloudWatch investigations CloudWatch investigations API Reference
Required: No
isCloudTrailEventHistoryEnabled
Specify true to enable CloudWatch investigations to have access to change events that are 
recorded by CloudTrail. The default is true.
Type: Boolean
Required: No
roleArn
Specify this ﬁeld if you want to change the IAM role that CloudWatch investigations will use 
when it gathers investigation data. To do so, specify the ARN of the new role.
The permissions in this role determine which of your resources that CloudWatch investigations 
will have access to during investigations.
For more information, see How to control what data CloudWatch investigations has access to 
during investigations.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: arn:.*
Required: No
tagKeyBoundaries
Enter the existing custom tag keys for custom applications in your system. Resource tags help 
CloudWatch investigations narrow the search space when it is unable to discover deﬁnite 
relationships between resources. For example, to discover that an Amazon ECS service depends 
on an Amazon RDS database, CloudWatch investigations can discover this relationship 
using data sources such as X-Ray and CloudWatch Application Signals. However, if you 
haven't deployed these features, CloudWatch investigations will attempt to identify possible 
relationships. Tag boundaries can be used to narrow the resources that will be discovered by 
CloudWatch investigations in these cases.
You don't need to enter tags created by myApplications or CloudFormation, because 
CloudWatch investigations can automatically detect those tags.
Request Body API Version 2018-05-10 46
CloudWatch investigations CloudWatch investigations API Reference
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: ([\p{L}\p{Z}\p{N}_.:/=+\-@]+)
Required: No
Response Syntax
HTTP/1.1 200
Response Elements
If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.
Errors
For information about the errors that are common to all actions, see Common Error Types.
AccessDeniedException
You don't have suﬃcient permissions to perform this action.
HTTP Status Code: 403
ConﬂictException
This operation couldn't be completed because of a conﬂict in resource states.
HTTP Status Code: 409
ForbiddenException
Access id denied for this operation, or this operation is not valid for the speciﬁed resource.
HTTP Status Code: 403
InternalServerException
An internal server error occurred. You can try again later.
HTTP Status Code: 500
Response Syntax API Version 2018-05-10 47
CloudWatch investigations CloudWatch investigations API Reference
ResourceNotFoundException
The speciﬁed resource doesn't exist.
HTTP Status Code: 404
ThrottlingException
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429
ValidationException
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-05-10 48
CloudWatch investigations CloudWatch investigations API Reference
Data Types
The AWS AI Ops API contains several data types that various actions use. This section describes 
each data type in detail.
Note
The order of each element in a data type structure is not guaranteed. Applications should 
not assume a particular order.
The following data types are supported:
• CrossAccountConﬁguration
• EncryptionConﬁguration
• ListInvestigationGroupsModel
API Version 2018-05-10 49
CloudWatch investigations CloudWatch investigations API Reference
CrossAccountConﬁguration
This structure contains information about the cross-account conﬁguration in the account.
Contents
sourceRoleArn
The ARN of an existing role which will be used to do investigations on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: arn:.*
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
CrossAccountConﬁguration API Version 2018-05-10 50
CloudWatch investigations CloudWatch investigations API Reference
EncryptionConﬁguration
Use this structure to specify a customer managed AWS KMS key to use to encrypt investigation 
data.
Contents
kmsKeyId
If the investigation group uses a customer managed key for encryption, this ﬁeld displays the ID 
of that key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: arn:.*
Required: No
type
Displays whether investigation data is encrypted by a customer managed key or an AWS owned 
key.
Type: String
Valid Values: AWS_OWNED_KEY | CUSTOMER_MANAGED_KMS_KEY
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
EncryptionConﬁguration API Version 2018-05-10 51
CloudWatch investigations CloudWatch investigations API Reference
ListInvestigationGroupsModel
This structure contains information about one investigation group in the account.
Contents
arn
The Amazon Resource Name (ARN) of the investigation group.
Type: String
Pattern: arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:
[0-9]{12}:investigation-group\/[A-Za-z0-9]{16}
Required: No
name
The name of the investigation group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: [\-_A-Za-z0-9\[\]\(\)\{\}\.: ]+
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
ListInvestigationGroupsModel API Version 2018-05-10 52
CloudWatch investigations CloudWatch investigations API Reference
Common Parameters
The following list contains the parameters that all actions use for signing Signature Version 4 
requests with a query string. Any action-speciﬁc parameters are listed in the topic for that action. 
For more information about Signature Version 4, see Signing AWS API requests in the IAM User 
Guide.
X-Amz-Algorithm
The hash algorithm that you used to create the request signature.
Condition: Specify this parameter when you include authentication information in a query 
string instead of in the HTTP authorization header.
Type: string
Valid Values: AWS4-HMAC-SHA256
Required: Conditional
X-Amz-Credential
The credential scope value, which is a string that includes your access key, the date, the region 
you are targeting, the service you are requesting, and a termination string ("aws4_request"). 
The value is expressed in the following format: access_key/YYYYMMDD/region/service/
aws4_request.
For more information, see Create a signed AWS API request in the IAM User Guide.
Condition: Specify this parameter when you include authentication information in a query 
string instead of in the HTTP authorization header.
Type: string
Required: Conditional
X-Amz-Date
The date that is used to create the signature. The format must be ISO 8601 basic format 
(YYYYMMDD'T'HHMMSS'Z'). For example, the following date time is a valid X-Amz-Date value:
20120325T120000Z.
API Version 2018-05-10 53
CloudWatch investigations CloudWatch investigations API Reference
Condition: X-Amz-Date is optional for all requests; it can be used to override the date used for 
signing requests. If the Date header is speciﬁed in the ISO 8601 basic format, X-Amz-Date is not 
required. When X-Amz-Date is used, it always overrides the value of the Date header. For more 
information, see Elements of an AWS API request signature in the IAM User Guide.
Type: string
Required: Conditional
X-Amz-Security-Token
The temporary security token that was obtained through a call to AWS Security Token Service 
(AWS STS). For a list of services that support temporary security credentials from AWS STS, see
AWS services that work with IAM in the IAM User Guide.
Condition: If you're using temporary security credentials from AWS STS, you must include the 
security token.
Type: string
Required: Conditional
X-Amz-Signature
Speciﬁes the hex-encoded signature that was calculated from the string to sign and the derived 
signing key.
Condition: Specify this parameter when you include authentication information in a query 
string instead of in the HTTP authorization header.
Type: string
Required: Conditional
X-Amz-SignedHeaders
Speciﬁes all the HTTP headers that were included as part of the canonical request. For more 
information about specifying signed headers, see Create a signed AWS API request in the IAM 
User Guide.
Condition: Specify this parameter when you include authentication information in a query 
string instead of in the HTTP authorization header.
Type: string
API Version 2018-05-10 54
CloudWatch investigations CloudWatch investigations API Reference
Required: Conditional
API Version 2018-05-10 55
CloudWatch investigations CloudWatch investigations API Reference
Common Error Types
This section lists common error types that this AWS service may return. Not all services return all 
error types listed here. For errors speciﬁc to an API action for this service, see the topic for that API 
action.
AccessDeniedException
You don't have permission to perform this action. Verify that your IAM policy includes the 
required permissions.
HTTP Status Code: 403
ExpiredTokenException
The security token included in the request has expired. Request a new security token and try 
again.
HTTP Status Code: 403
IncompleteSignature
The request signature doesn't conform to AWS standards. Verify that you're using valid AWS 
credentials and that your request is properly formatted. If you're using an SDK, ensure it's up to 
date.
HTTP Status Code: 403
InternalFailure
The request can't be processed right now because of an internal server issue. Try again later. If 
the problem persists, contact AWS Support.
HTTP Status Code: 500
MalformedHttpRequestException
The request body can't be processed. This typically happens when the request body can't be 
decompressed using the speciﬁed content encoding algorithm. Verify that the content encoding 
header matches the compression format used.
HTTP Status Code: 400
API Version 2018-05-10 56
CloudWatch investigations CloudWatch investigations API Reference
NotAuthorized
You don't have permissions to perform this action. Verify that your IAM policy includes the 
required permissions.
HTTP Status Code: 401
OptInRequired
Your AWS account needs a subscription for this service. Verify that you've enabled the service in 
your account.
HTTP Status Code: 403
RequestAbortedException
The request was aborted before a response could be returned. This typically happens when the 
client closes the connection.
HTTP Status Code: 400
RequestEntityTooLargeException
The request entity is too large. Reduce the size of the request body and try again.
HTTP Status Code: 413
RequestTimeoutException
The request timed out. The server didn't receive the complete request within the expected time 
frame. Try again.
HTTP Status Code: 408
ServiceUnavailable
The service is temporarily unavailable. Try again later.
HTTP Status Code: 503
ThrottlingException
Your request rate is too high. The AWS SDKs automatically retry requests that receive this 
exception. Reduce the frequency of requests.
HTTP Status Code: 400
API Version 2018-05-10 57
CloudWatch investigations CloudWatch investigations API Reference
UnknownOperationException
The action or operation isn't recognized. Verify that the action name is spelled correctly and 
that it's supported by the API version you're using.
HTTP Status Code: 404
UnrecognizedClientException
The X.509 certiﬁcate or AWS access key ID you provided doesn't exist in our records. Verify that 
you're using valid credentials and that they haven't expired.
HTTP Status Code: 403
ValidationError
The input doesn't meet the required format or constraints. Check that all required parameters 
are included and that values are valid.
HTTP Status Code: 400
API Version 2018-05-10 58
