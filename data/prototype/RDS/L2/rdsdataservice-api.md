# API Reference

## Welcome

API Reference
RDS Data API
API Version 2018-08-01
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
## Actions

RDS Data API API Reference
RDS Data API: API Reference
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
Amazon's trademarks and trade dress may not be used in connection with any product or service 
that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any 
manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are 
the property of their respective owners, who may or may not be aﬃliated with, connected to, or 
sponsored by Amazon.
## BatchExecuteStatement

## Request Syntax

RDS Data API API Reference
Table of Contents
Welcome ........................................................................................................................................... 1
Actions .............................................................................................................................................. 2
BatchExecuteStatement .............................................................................................................................. 3
Request Syntax ........................................................................................................................................ 3
URI Request Parameters ........................................................................................................................ 4
Request Body ........................................................................................................................................... 4
Response Syntax ...................................................................................................................................... 6
Response Elements ................................................................................................................................. 6
Errors .......................................................................................................................................................... 7
See Also ..................................................................................................................................................... 9
BeginTransaction ........................................................................................................................................ 10
Request Syntax ...................................................................................................................................... 10
URI Request Parameters ...................................................................................................................... 10
Request Body ......................................................................................................................................... 10
Response Syntax ................................................................................................................................... 11
Response Elements ............................................................................................................................... 12
Errors ....................................................................................................................................................... 12
See Also .................................................................................................................................................. 14
CommitTransaction .................................................................................................................................... 16
Request Syntax ...................................................................................................................................... 16
URI Request Parameters ...................................................................................................................... 16
Request Body ......................................................................................................................................... 16
Response Syntax ................................................................................................................................... 17
Response Elements ............................................................................................................................... 17
Errors ....................................................................................................................................................... 17
See Also .................................................................................................................................................. 20
ExecuteSql .................................................................................................................................................... 21
Request Syntax ...................................................................................................................................... 21
URI Request Parameters ...................................................................................................................... 21
Request Body ......................................................................................................................................... 21
Response Syntax ................................................................................................................................... 23
Response Elements ............................................................................................................................... 24
Errors ....................................................................................................................................................... 24
See Also .................................................................................................................................................. 25
API Version 2018-08-01 iii
## URI Request Parameters

## Request Body

RDS Data API API Reference
ExecuteStatement ...................................................................................................................................... 26
Request Syntax ...................................................................................................................................... 26
URI Request Parameters ...................................................................................................................... 27
Request Body ......................................................................................................................................... 27
Response Syntax ................................................................................................................................... 30
Response Elements ............................................................................................................................... 31
Errors ....................................................................................................................................................... 32
See Also .................................................................................................................................................. 35
RollbackTransaction ................................................................................................................................... 36
Request Syntax ...................................................................................................................................... 36
URI Request Parameters ...................................................................................................................... 36
Request Body ......................................................................................................................................... 36
Response Syntax ................................................................................................................................... 37
Response Elements ............................................................................................................................... 37
Errors ....................................................................................................................................................... 37
See Also .................................................................................................................................................. 40
Data Types ..................................................................................................................................... 41
ArrayValue .................................................................................................................................................... 42
Contents .................................................................................................................................................. 42
See Also .................................................................................................................................................. 43
ColumnMetadata ........................................................................................................................................ 44
Contents .................................................................................................................................................. 44
See Also .................................................................................................................................................. 46
Field ............................................................................................................................................................... 47
Contents .................................................................................................................................................. 47
See Also .................................................................................................................................................. 48
Record ........................................................................................................................................................... 49
Contents .................................................................................................................................................. 49
See Also .................................................................................................................................................. 49
ResultFrame ................................................................................................................................................. 50
Contents .................................................................................................................................................. 50
See Also .................................................................................................................................................. 50
ResultSetMetadata ..................................................................................................................................... 51
Contents .................................................................................................................................................. 51
See Also .................................................................................................................................................. 51
ResultSetOptions ........................................................................................................................................ 52
API Version 2018-08-01 iv
RDS Data API API Reference
Contents .................................................................................................................................................. 52
See Also .................................................................................................................................................. 52
SqlParameter ............................................................................................................................................... 54
Contents .................................................................................................................................................. 54
See Also .................................................................................................................................................. 55
SqlStatementResult ................................................................................................................................... 56
Contents .................................................................................................................................................. 56
See Also .................................................................................................................................................. 56
StructValue .................................................................................................................................................. 57
Contents .................................................................................................................................................. 57
See Also .................................................................................................................................................. 57
UpdateResult ............................................................................................................................................... 58
Contents .................................................................................................................................................. 58
See Also .................................................................................................................................................. 58
Value ............................................................................................................................................................. 59
Contents .................................................................................................................................................. 59
See Also .................................................................................................................................................. 61
API Version 2018-08-01 v
## Response Syntax

## Response Elements

RDS Data API API Reference
Welcome
Amazon RDS provides an HTTP endpoint to run SQL statements on an Amazon Aurora DB cluster. 
To run these statements, you use the RDS Data API (Data API).
Data API is available with the following types of Aurora databases:
• Aurora PostgreSQL - Serverless v2, provisioned, and Serverless v1
• Aurora MySQL - Serverless v2, provisioned, and Serverless v1
For more information about the Data API, see Using RDS Data API in the Amazon Aurora User 
Guide.
This document was last published on April 2, 2026.
API Version 2018-08-01 1
## Errors

RDS Data API API Reference
Actions
The following actions are supported:
• BatchExecuteStatement
• BeginTransaction
• CommitTransaction
• ExecuteSql
• ExecuteStatement
• RollbackTransaction
API Version 2018-08-01 2
RDS Data API API Reference
BatchExecuteStatement
Runs a batch SQL statement over an array of data.
You can run bulk update and insert operations for multiple records using a DML statement with 
diﬀerent parameter sets. Bulk operations can provide a signiﬁcant performance improvement over 
individual insert and update operations.
Note
If a call isn't part of a transaction because it doesn't include the transactionID
parameter, changes that result from the call are committed automatically.
There isn't a ﬁxed upper limit on the number of parameter sets. However, the maximum 
size of the HTTP request submitted through the Data API is 4 MiB. If the request exceeds 
this limit, the Data API returns an error and doesn't process the request. This 4-MiB limit 
includes the size of the HTTP headers and the JSON notation in the request. Thus, the 
number of parameter sets that you can include depends on a combination of factors, such 
as the size of the SQL statement and the size of each parameter set.
The response size limit is 1 MiB. If the call returns more than 1 MiB of response data, the 
call is terminated.
Request Syntax
POST /BatchExecute HTTP/1.1
Content-type: application/json
{ 
   "database": "string", 
   "parameterSets": [  
      [  
         {  
            "name": "string", 
            "typeHint": "string", 
            "value": { ... } 
         } 
      ] 
   ], 
   "resourceArn": "string", 
   "schema": "string", 
BatchExecuteStatement API Version 2018-08-01 3
## See Also

RDS Data API API Reference
   "secretArn": "string", 
   "sql": "string", 
   "transactionId": "string"
}
URI Request Parameters
The request does not use any URI parameters.
Request Body
The request accepts the following data in JSON format.
database
The name of the database.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No
parameterSets
The parameter set for the batch operation.
The SQL statement is executed as many times as the number of parameter sets provided. To 
execute a SQL statement with no parameters, use one of the following options:
• Specify one or more empty parameter sets.
• Use the ExecuteStatement operation instead of the BatchExecuteStatement operation.
Note
Array parameters are not supported.
Type: Array of arrays of SqlParameter objects
Required: No
URI Request Parameters API Version 2018-08-01 4
## BeginTransaction

## Request Syntax

## URI Request Parameters

## Request Body

RDS Data API API Reference
resourceArn
The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
schema
The name of the database schema.
Note
Currently, the schema parameter isn't supported.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No
secretArn
The ARN of the secret that enables access to the DB cluster. Enter the database user name and 
password for the credentials in the secret.
For information about creating the secret, see Create a database secret.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
sql
The SQL statement to run. Don't include a semicolon (;) at the end of the SQL statement.
Type: String
Request Body API Version 2018-08-01 5
## Response Syntax

RDS Data API API Reference
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: Yes
transactionId
The identiﬁer of a transaction that was started by using the BeginTransaction operation. 
Specify the transaction ID of the transaction that you want to include the SQL statement in.
If the SQL statement is not part of a transaction, don't set this parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 192.
Required: No
Response Syntax
HTTP/1.1 200
Content-type: application/json
{ 
   "updateResults": [  
      {  
         "generatedFields": [  
            { ... } 
         ] 
      } 
   ]
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
updateResults
The execution results of each batch entry.
Type: Array of UpdateResult objects
Response Syntax API Version 2018-08-01 6
## Response Elements

## Errors

RDS Data API API Reference
Errors
AccessDeniedException
You don't have suﬃcient access to perform this action.
HTTP Status Code: 403
BadRequestException
There is an error in the call or in a SQL statement. (This error only appears in calls from Aurora 
Serverless v1 databases.)
message
The error message returned by this BadRequestException error.
HTTP Status Code: 400
DatabaseErrorException
There was an error in processing the SQL statement.
HTTP Status Code: 400
DatabaseNotFoundException
The DB cluster doesn't have a DB instance.
HTTP Status Code: 404
DatabaseResumingException
A request was cancelled because the Aurora Serverless v2 DB instance was paused. The Data API 
request automatically resumes the DB instance. Wait a few seconds and try again.
HTTP Status Code: 400
DatabaseUnavailableException
The writer instance in the DB cluster isn't available.
HTTP Status Code: 504
ForbiddenException
There are insuﬃcient privileges to make the call.
Errors API Version 2018-08-01 7
RDS Data API API Reference
message
The error message returned by this ForbiddenException error.
HTTP Status Code: 403
HttpEndpointNotEnabledException
The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster.
HTTP Status Code: 400
InternalServerErrorException
An internal error occurred.
HTTP Status Code: 500
InvalidResourceStateException
The resource is in an invalid state.
HTTP Status Code: 400
InvalidSecretException
The Secrets Manager secret used with the request isn't valid.
HTTP Status Code: 400
SecretsErrorException
There was a problem with the Secrets Manager secret used with the request, caused by one of 
the following conditions:
• RDS Data API timed out retrieving the secret.
• The secret provided wasn't found.
• The secret couldn't be decrypted.
HTTP Status Code: 400
ServiceUnavailableError
The service speciﬁed by the resourceArn parameter isn't available.
HTTP Status Code: 503
Errors API Version 2018-08-01 8
## See Also

RDS Data API API Reference
StatementTimeoutException
The execution of the SQL statement timed out.
dbConnectionId
The database connection ID that executed the SQL statement.
message
The error message returned by this StatementTimeoutException error.
HTTP Status Code: 400
TransactionNotFoundException
The transaction ID wasn't found.
HTTP Status Code: 404
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
See Also API Version 2018-08-01 9
RDS Data API API Reference
BeginTransaction
Starts a SQL transaction.
Note
A transaction can run for a maximum of 24 hours. A transaction is terminated and rolled 
back automatically after 24 hours.
A transaction times out if no calls use its transaction ID in three minutes. If a transaction 
times out before it's committed, it's rolled back automatically.
For Aurora MySQL, DDL statements inside a transaction cause an implicit commit. We 
recommend that you run each MySQL DDL statement in a separate ExecuteStatement
call with continueAfterTimeout enabled.
Request Syntax
POST /BeginTransaction HTTP/1.1
Content-type: application/json
{ 
   "database": "string", 
   "resourceArn": "string", 
   "schema": "string", 
   "secretArn": "string"
}
URI Request Parameters
The request does not use any URI parameters.
Request Body
The request accepts the following data in JSON format.
database
The name of the database.
Type: String
BeginTransaction API Version 2018-08-01 10
## CommitTransaction

## Request Syntax

## URI Request Parameters

## Request Body

RDS Data API API Reference
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No
resourceArn
The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
schema
The name of the database schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No
secretArn
The name or ARN of the secret that enables access to the DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
Response Syntax
HTTP/1.1 200
Content-type: application/json
{ 
   "transactionId": "string"
}
Response Syntax API Version 2018-08-01 11
## Response Syntax

## Response Elements

## Errors

RDS Data API API Reference
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
transactionId
The transaction ID of the transaction started by the call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 192.
Errors
AccessDeniedException
You don't have suﬃcient access to perform this action.
HTTP Status Code: 403
BadRequestException
There is an error in the call or in a SQL statement. (This error only appears in calls from Aurora 
Serverless v1 databases.)
message
The error message returned by this BadRequestException error.
HTTP Status Code: 400
DatabaseErrorException
There was an error in processing the SQL statement.
HTTP Status Code: 400
DatabaseNotFoundException
The DB cluster doesn't have a DB instance.
HTTP Status Code: 404
Response Elements API Version 2018-08-01 12
RDS Data API API Reference
DatabaseResumingException
A request was cancelled because the Aurora Serverless v2 DB instance was paused. The Data API 
request automatically resumes the DB instance. Wait a few seconds and try again.
HTTP Status Code: 400
DatabaseUnavailableException
The writer instance in the DB cluster isn't available.
HTTP Status Code: 504
ForbiddenException
There are insuﬃcient privileges to make the call.
message
The error message returned by this ForbiddenException error.
HTTP Status Code: 403
HttpEndpointNotEnabledException
The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster.
HTTP Status Code: 400
InternalServerErrorException
An internal error occurred.
HTTP Status Code: 500
InvalidResourceStateException
The resource is in an invalid state.
HTTP Status Code: 400
InvalidSecretException
The Secrets Manager secret used with the request isn't valid.
HTTP Status Code: 400
Errors API Version 2018-08-01 13
RDS Data API API Reference
SecretsErrorException
There was a problem with the Secrets Manager secret used with the request, caused by one of 
the following conditions:
• RDS Data API timed out retrieving the secret.
• The secret provided wasn't found.
• The secret couldn't be decrypted.
HTTP Status Code: 400
ServiceUnavailableError
The service speciﬁed by the resourceArn parameter isn't available.
HTTP Status Code: 503
StatementTimeoutException
The execution of the SQL statement timed out.
dbConnectionId
The database connection ID that executed the SQL statement.
message
The error message returned by this StatementTimeoutException error.
HTTP Status Code: 400
TransactionNotFoundException
The transaction ID wasn't found.
HTTP Status Code: 404
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
See Also API Version 2018-08-01 14
## See Also

RDS Data API API Reference
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-08-01 15
## ExecuteSql

## Request Syntax

## URI Request Parameters

## Request Body

RDS Data API API Reference
CommitTransaction
Ends a SQL transaction started with the BeginTransaction operation and commits the changes.
Request Syntax
POST /CommitTransaction HTTP/1.1
Content-type: application/json
{ 
   "resourceArn": "string", 
   "secretArn": "string", 
   "transactionId": "string"
}
URI Request Parameters
The request does not use any URI parameters.
Request Body
The request accepts the following data in JSON format.
resourceArn
The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
secretArn
The name or ARN of the secret that enables access to the DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
CommitTransaction API Version 2018-08-01 16
RDS Data API API Reference
transactionId
The identiﬁer of the transaction to end and commit.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 192.
Required: Yes
Response Syntax
HTTP/1.1 200
Content-type: application/json
{ 
   "transactionStatus": "string"
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
transactionStatus
The status of the commit operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Errors
AccessDeniedException
You don't have suﬃcient access to perform this action.
HTTP Status Code: 403
Response Syntax API Version 2018-08-01 17
## Response Syntax

RDS Data API API Reference
BadRequestException
There is an error in the call or in a SQL statement. (This error only appears in calls from Aurora 
Serverless v1 databases.)
message
The error message returned by this BadRequestException error.
HTTP Status Code: 400
DatabaseErrorException
There was an error in processing the SQL statement.
HTTP Status Code: 400
DatabaseNotFoundException
The DB cluster doesn't have a DB instance.
HTTP Status Code: 404
DatabaseUnavailableException
The writer instance in the DB cluster isn't available.
HTTP Status Code: 504
ForbiddenException
There are insuﬃcient privileges to make the call.
message
The error message returned by this ForbiddenException error.
HTTP Status Code: 403
HttpEndpointNotEnabledException
The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster.
HTTP Status Code: 400
InternalServerErrorException
An internal error occurred.
Errors API Version 2018-08-01 18
## Response Elements

## Errors

RDS Data API API Reference
HTTP Status Code: 500
InvalidResourceStateException
The resource is in an invalid state.
HTTP Status Code: 400
InvalidSecretException
The Secrets Manager secret used with the request isn't valid.
HTTP Status Code: 400
NotFoundException
The resourceArn, secretArn, or transactionId value can't be found.
message
The error message returned by this NotFoundException error.
HTTP Status Code: 404
SecretsErrorException
There was a problem with the Secrets Manager secret used with the request, caused by one of 
the following conditions:
• RDS Data API timed out retrieving the secret.
• The secret provided wasn't found.
• The secret couldn't be decrypted.
HTTP Status Code: 400
ServiceUnavailableError
The service speciﬁed by the resourceArn parameter isn't available.
HTTP Status Code: 503
StatementTimeoutException
The execution of the SQL statement timed out.
dbConnectionId
The database connection ID that executed the SQL statement.
Errors API Version 2018-08-01 19
## See Also

RDS Data API API Reference
message
The error message returned by this StatementTimeoutException error.
HTTP Status Code: 400
TransactionNotFoundException
The transaction ID wasn't found.
HTTP Status Code: 404
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
See Also API Version 2018-08-01 20
RDS Data API API Reference
ExecuteSql
Runs one or more SQL statements.
Note
This operation isn't supported for Aurora Serverless v2 and provisioned DB 
clusters. For Aurora Serverless v1 DB clusters, the operation is deprecated. Use the
BatchExecuteStatement or ExecuteStatement operation.
Request Syntax
POST /ExecuteSql HTTP/1.1
Content-type: application/json
{ 
   "awsSecretStoreArn": "string", 
   "database": "string", 
   "dbClusterOrInstanceArn": "string", 
   "schema": "string", 
   "sqlStatements": "string"
}
URI Request Parameters
The request does not use any URI parameters.
Request Body
The request accepts the following data in JSON format.
awsSecretStoreArn
The Amazon Resource Name (ARN) of the secret that enables access to the DB cluster. Enter the 
database user name and password for the credentials in the secret.
For information about creating the secret, see Create a database secret.
Type: String
ExecuteSql API Version 2018-08-01 21
RDS Data API API Reference
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
database
The name of the database.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No
dbClusterOrInstanceArn
The ARN of the Aurora Serverless DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
schema
The name of the database schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No
sqlStatements
One or more SQL statements to run on the DB cluster.
You can separate SQL statements from each other with a semicolon (;). Any valid SQL statement 
is permitted, including data deﬁnition, data manipulation, and commit statements.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: Yes
Request Body API Version 2018-08-01 22
RDS Data API API Reference
Response Syntax
HTTP/1.1 200
Content-type: application/json
{ 
   "sqlStatementResults": [  
      {  
         "numberOfRecordsUpdated": number, 
         "resultFrame": {  
            "records": [  
               {  
                  "values": [  
                     { ... } 
                  ] 
               } 
            ], 
            "resultSetMetadata": {  
               "columnCount": number, 
               "columnMetadata": [  
                  {  
                     "arrayBaseColumnType": number, 
                     "isAutoIncrement": boolean, 
                     "isCaseSensitive": boolean, 
                     "isCurrency": boolean, 
                     "isSigned": boolean, 
                     "label": "string", 
                     "name": "string", 
                     "nullable": number, 
                     "precision": number, 
                     "scale": number, 
                     "schemaName": "string", 
                     "tableName": "string", 
                     "type": number, 
                     "typeName": "string" 
                  } 
               ] 
            } 
         } 
      } 
   ]
}
Response Syntax API Version 2018-08-01 23
RDS Data API API Reference
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
sqlStatementResults
The results of the SQL statement or statements.
Type: Array of SqlStatementResult objects
Errors
AccessDeniedException
You don't have suﬃcient access to perform this action.
HTTP Status Code: 403
BadRequestException
There is an error in the call or in a SQL statement. (This error only appears in calls from Aurora 
Serverless v1 databases.)
message
The error message returned by this BadRequestException error.
HTTP Status Code: 400
ForbiddenException
There are insuﬃcient privileges to make the call.
message
The error message returned by this ForbiddenException error.
HTTP Status Code: 403
InternalServerErrorException
An internal error occurred.
HTTP Status Code: 500
Response Elements API Version 2018-08-01 24
RDS Data API API Reference
ServiceUnavailableError
The service speciﬁed by the resourceArn parameter isn't available.
HTTP Status Code: 503
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
See Also API Version 2018-08-01 25
RDS Data API API Reference
ExecuteStatement
Runs a SQL statement against a database.
Note
If a call isn't part of a transaction because it doesn't include the transactionID
parameter, changes that result from the call are committed automatically.
If the binary response data from the database is more than 1 MB, the call is terminated.
Request Syntax
POST /Execute HTTP/1.1
Content-type: application/json
{ 
   "continueAfterTimeout": boolean, 
   "database": "string", 
   "formatRecordsAs": "string", 
   "includeResultMetadata": boolean, 
   "parameters": [  
      {  
         "name": "string", 
         "typeHint": "string", 
         "value": { ... } 
      } 
   ], 
   "resourceArn": "string", 
   "resultSetOptions": {  
      "decimalReturnType": "string", 
      "longReturnType": "string" 
   }, 
   "schema": "string", 
   "secretArn": "string", 
   "sql": "string", 
   "transactionId": "string"
}
ExecuteStatement API Version 2018-08-01 26
RDS Data API API Reference
URI Request Parameters
The request does not use any URI parameters.
Request Body
The request accepts the following data in JSON format.
continueAfterTimeout
A value that indicates whether to continue running the statement after the call times out. By 
default, the statement stops running when the call times out.
Note
For DDL statements, we recommend continuing to run the statement after the call 
times out. When a DDL statement terminates before it is ﬁnished running, it can result 
in errors and possibly corrupted data structures.
Type: Boolean
Required: No
database
The name of the database.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No
formatRecordsAs
A value that indicates whether to format the result set as a single JSON string. This 
parameter only applies to SELECT statements and is ignored for other types of statements. 
Allowed values are NONE and JSON. The default value is NONE. The result is returned in the
formattedRecords ﬁeld.
For usage information about the JSON format for result sets, see Using the Data API in the
Amazon Aurora User Guide.
URI Request Parameters API Version 2018-08-01 27
RDS Data API API Reference
Type: String
Valid Values: NONE | JSON
Required: No
includeResultMetadata
A value that indicates whether to include metadata in the results.
Type: Boolean
Required: No
parameters
The parameters for the SQL statement.
Note
Array parameters are not supported.
Type: Array of SqlParameter objects
Required: No
resourceArn
The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
resultSetOptions
Options that control how the result set is returned.
Type: ResultSetOptions object
Required: No
Request Body API Version 2018-08-01 28
RDS Data API API Reference
schema
The name of the database schema.
Note
Currently, the schema parameter isn't supported.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No
secretArn
The ARN of the secret that enables access to the DB cluster. Enter the database user name and 
password for the credentials in the secret.
For information about creating the secret, see Create a database secret.
Note
When you use the CLI on Linux to reference a secret created in the RDS console, the 
ARN might include special characters like rds!cluster. If you enclose the ARN in 
double quotes, the ! character might trigger a shell expansion error, such as -bash: !
cluster: event not found. To avoid this, escape the exclamation mark (\!) in the 
ARN or enclose the entire ARN in single quotes (') instead of double quotes.
Alternatively, disable shell history expansion by running set +H before you execute the 
command.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
sql
The SQL statement to run.
Request Body API Version 2018-08-01 29
RDS Data API API Reference
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: Yes
transactionId
The identiﬁer of a transaction that was started by using the BeginTransaction operation. 
Specify the transaction ID of the transaction that you want to include the SQL statement in.
If the SQL statement is not part of a transaction, don't set this parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 192.
Required: No
Response Syntax
HTTP/1.1 200
Content-type: application/json
{ 
   "columnMetadata": [  
      {  
         "arrayBaseColumnType": number, 
         "isAutoIncrement": boolean, 
         "isCaseSensitive": boolean, 
         "isCurrency": boolean, 
         "isSigned": boolean, 
         "label": "string", 
         "name": "string", 
         "nullable": number, 
         "precision": number, 
         "scale": number, 
         "schemaName": "string", 
         "tableName": "string", 
         "type": number, 
         "typeName": "string" 
      } 
   ], 
   "formattedRecords": "string", 
Response Syntax API Version 2018-08-01 30
RDS Data API API Reference
   "generatedFields": [  
      { ... } 
   ], 
   "numberOfRecordsUpdated": number, 
   "records": [  
      [  
         { ... } 
      ] 
   ]
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
columnMetadata
Metadata for the columns included in the results. This ﬁeld is blank if the formatRecordsAs
parameter is set to JSON.
Type: Array of ColumnMetadata objects
formattedRecords
A string value that represents the result set of a SELECT statement in JSON format. This value 
is only present when the formatRecordsAs parameter is set to JSON.
The size limit for this ﬁeld is currently 10 MB. If the JSON-formatted string representing the 
result set requires more than 10 MB, the call returns an error.
Type: String
generatedFields
Values for ﬁelds generated during a DML request.
Note
The generatedFields data isn't supported by Aurora PostgreSQL. To get the values 
of generated ﬁelds, use the RETURNING clause. For more information, see Returning 
Data From Modiﬁed Rows in the PostgreSQL documentation.
Response Elements API Version 2018-08-01 31
RDS Data API API Reference
Type: Array of Field objects
numberOfRecordsUpdated
The number of records updated by the request.
Type: Long
records
The records returned by the SQL statement. This ﬁeld is blank if the formatRecordsAs
parameter is set to JSON.
Type: Array of arrays of Field objects
Errors
AccessDeniedException
You don't have suﬃcient access to perform this action.
HTTP Status Code: 403
BadRequestException
There is an error in the call or in a SQL statement. (This error only appears in calls from Aurora 
Serverless v1 databases.)
message
The error message returned by this BadRequestException error.
HTTP Status Code: 400
DatabaseErrorException
There was an error in processing the SQL statement.
HTTP Status Code: 400
DatabaseNotFoundException
The DB cluster doesn't have a DB instance.
HTTP Status Code: 404
Errors API Version 2018-08-01 32
RDS Data API API Reference
DatabaseResumingException
A request was cancelled because the Aurora Serverless v2 DB instance was paused. The Data API 
request automatically resumes the DB instance. Wait a few seconds and try again.
HTTP Status Code: 400
DatabaseUnavailableException
The writer instance in the DB cluster isn't available.
HTTP Status Code: 504
ForbiddenException
There are insuﬃcient privileges to make the call.
message
The error message returned by this ForbiddenException error.
HTTP Status Code: 403
HttpEndpointNotEnabledException
The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster.
HTTP Status Code: 400
InternalServerErrorException
An internal error occurred.
HTTP Status Code: 500
InvalidResourceStateException
The resource is in an invalid state.
HTTP Status Code: 400
InvalidSecretException
The Secrets Manager secret used with the request isn't valid.
HTTP Status Code: 400
Errors API Version 2018-08-01 33
RDS Data API API Reference
SecretsErrorException
There was a problem with the Secrets Manager secret used with the request, caused by one of 
the following conditions:
• RDS Data API timed out retrieving the secret.
• The secret provided wasn't found.
• The secret couldn't be decrypted.
HTTP Status Code: 400
ServiceUnavailableError
The service speciﬁed by the resourceArn parameter isn't available.
HTTP Status Code: 503
StatementTimeoutException
The execution of the SQL statement timed out.
dbConnectionId
The database connection ID that executed the SQL statement.
message
The error message returned by this StatementTimeoutException error.
HTTP Status Code: 400
TransactionNotFoundException
The transaction ID wasn't found.
HTTP Status Code: 404
UnsupportedResultException
There was a problem with the result because of one of the following conditions:
• It contained an unsupported data type.
• It contained a multidimensional array.
• The size was too large.
HTTP Status Code: 400
Errors API Version 2018-08-01 34
RDS Data API API Reference
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
See Also API Version 2018-08-01 35
RDS Data API API Reference
RollbackTransaction
Performs a rollback of a transaction. Rolling back a transaction cancels its changes.
Request Syntax
POST /RollbackTransaction HTTP/1.1
Content-type: application/json
{ 
   "resourceArn": "string", 
   "secretArn": "string", 
   "transactionId": "string"
}
URI Request Parameters
The request does not use any URI parameters.
Request Body
The request accepts the following data in JSON format.
resourceArn
The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
secretArn
The name or ARN of the secret that enables access to the DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes
RollbackTransaction API Version 2018-08-01 36
RDS Data API API Reference
transactionId
The identiﬁer of the transaction to roll back.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 192.
Required: Yes
Response Syntax
HTTP/1.1 200
Content-type: application/json
{ 
   "transactionStatus": "string"
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
transactionStatus
The status of the rollback operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Errors
AccessDeniedException
You don't have suﬃcient access to perform this action.
HTTP Status Code: 403
Response Syntax API Version 2018-08-01 37
RDS Data API API Reference
BadRequestException
There is an error in the call or in a SQL statement. (This error only appears in calls from Aurora 
Serverless v1 databases.)
message
The error message returned by this BadRequestException error.
HTTP Status Code: 400
DatabaseErrorException
There was an error in processing the SQL statement.
HTTP Status Code: 400
DatabaseNotFoundException
The DB cluster doesn't have a DB instance.
HTTP Status Code: 404
DatabaseUnavailableException
The writer instance in the DB cluster isn't available.
HTTP Status Code: 504
ForbiddenException
There are insuﬃcient privileges to make the call.
message
The error message returned by this ForbiddenException error.
HTTP Status Code: 403
HttpEndpointNotEnabledException
The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster.
HTTP Status Code: 400
InternalServerErrorException
An internal error occurred.
Errors API Version 2018-08-01 38
RDS Data API API Reference
HTTP Status Code: 500
InvalidResourceStateException
The resource is in an invalid state.
HTTP Status Code: 400
InvalidSecretException
The Secrets Manager secret used with the request isn't valid.
HTTP Status Code: 400
NotFoundException
The resourceArn, secretArn, or transactionId value can't be found.
message
The error message returned by this NotFoundException error.
HTTP Status Code: 404
SecretsErrorException
There was a problem with the Secrets Manager secret used with the request, caused by one of 
the following conditions:
• RDS Data API timed out retrieving the secret.
• The secret provided wasn't found.
• The secret couldn't be decrypted.
HTTP Status Code: 400
ServiceUnavailableError
The service speciﬁed by the resourceArn parameter isn't available.
HTTP Status Code: 503
StatementTimeoutException
The execution of the SQL statement timed out.
dbConnectionId
The database connection ID that executed the SQL statement.
Errors API Version 2018-08-01 39
RDS Data API API Reference
message
The error message returned by this StatementTimeoutException error.
HTTP Status Code: 400
TransactionNotFoundException
The transaction ID wasn't found.
HTTP Status Code: 404
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
See Also API Version 2018-08-01 40
RDS Data API API Reference
Data Types
The AWS RDS DataService API contains several data types that various actions use. This section 
describes each data type in detail.
Note
The order of each element in a data type structure is not guaranteed. Applications should 
not assume a particular order.
The following data types are supported:
• ArrayValue
• ColumnMetadata
• Field
• Record
• ResultFrame
• ResultSetMetadata
• ResultSetOptions
• SqlParameter
• SqlStatementResult
• StructValue
• UpdateResult
• Value
API Version 2018-08-01 41
RDS Data API API Reference
ArrayValue
Contains an array.
Contents
Important
This data type is a UNION, so only one of the following members can be speciﬁed when 
used or returned.
arrayValues
An array of arrays.
Type: Array of ArrayValue objects
Required: No
booleanValues
An array of Boolean values.
Type: Array of booleans
Required: No
doubleValues
An array of ﬂoating-point numbers.
Type: Array of doubles
Required: No
longValues
An array of integers.
Type: Array of longs
Required: No
ArrayValue API Version 2018-08-01 42
RDS Data API API Reference
stringValues
An array of strings.
Type: Array of strings
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-08-01 43
RDS Data API API Reference
ColumnMetadata
Contains the metadata for a column.
Contents
arrayBaseColumnType
The type of the column.
Type: Integer
Required: No
isAutoIncrement
A value that indicates whether the column increments automatically.
Type: Boolean
Required: No
isCaseSensitive
A value that indicates whether the column is case-sensitive.
Type: Boolean
Required: No
isCurrency
A value that indicates whether the column contains currency values.
Type: Boolean
Required: No
isSigned
A value that indicates whether an integer column is signed.
Type: Boolean
Required: No
ColumnMetadata API Version 2018-08-01 44
RDS Data API API Reference
label
The label for the column.
Type: String
Required: No
name
The name of the column.
Type: String
Required: No
nullable
A value that indicates whether the column is nullable.
Type: Integer
Required: No
precision
The precision value of a decimal number column.
Type: Integer
Required: No
scale
The scale value of a decimal number column.
Type: Integer
Required: No
schemaName
The name of the schema that owns the table that includes the column.
Type: String
Required: No
Contents API Version 2018-08-01 45
RDS Data API API Reference
tableName
The name of the table that includes the column.
Type: String
Required: No
type
The type of the column.
Type: Integer
Required: No
typeName
The database-speciﬁc data type of the column.
Type: String
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-08-01 46
RDS Data API API Reference
Field
Contains a value.
Contents
Important
This data type is a UNION, so only one of the following members can be speciﬁed when 
used or returned.
arrayValue
An array of values.
Type: ArrayValue object
Note: This object is a Union. Only one member of this object can be speciﬁed or returned.
Required: No
blobValue
A value of BLOB data type.
Type: Base64-encoded binary data object
Required: No
booleanValue
A value of Boolean data type.
Type: Boolean
Required: No
doubleValue
A value of double data type.
Type: Double
Field API Version 2018-08-01 47
RDS Data API API Reference
Required: No
isNull
A NULL value.
Type: Boolean
Required: No
longValue
A value of long data type.
Type: Long
Required: No
stringValue
A value of string data type.
Type: String
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-08-01 48
RDS Data API API Reference
Record
A record returned by a call.
Note
This data structure is only used with the deprecated ExecuteSql operation. Use the
BatchExecuteStatement or ExecuteStatement operation instead.
Contents
values
The values returned in the record.
Type: Array of Value objects
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
Record API Version 2018-08-01 49
RDS Data API API Reference
ResultFrame
The result set returned by a SQL statement.
Note
This data structure is only used with the deprecated ExecuteSql operation. Use the
BatchExecuteStatement or ExecuteStatement operation instead.
Contents
records
The records in the result set.
Type: Array of Record objects
Required: No
resultSetMetadata
The result-set metadata in the result set.
Type: ResultSetMetadata object
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
ResultFrame API Version 2018-08-01 50
RDS Data API API Reference
ResultSetMetadata
The metadata of the result set returned by a SQL statement.
Contents
columnCount
The number of columns in the result set.
Type: Long
Required: No
columnMetadata
The metadata of the columns in the result set.
Type: Array of ColumnMetadata objects
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
ResultSetMetadata API Version 2018-08-01 51
RDS Data API API Reference
ResultSetOptions
Options that control how the result set is returned.
Contents
decimalReturnType
A value that indicates how a ﬁeld of DECIMAL type is represented in the response. The 
value of STRING, the default, speciﬁes that it is converted to a String value. The value of
DOUBLE_OR_LONG speciﬁes that it is converted to a Long value if its scale is 0, or to a Double 
value otherwise.
Note
Conversion to Double or Long can result in roundoﬀ errors due to precision loss. We 
recommend converting to String, especially when working with currency values.
Type: String
Valid Values: STRING | DOUBLE_OR_LONG
Required: No
longReturnType
A value that indicates how a ﬁeld of LONG type is represented. Allowed values are LONG and
STRING. The default is LONG. Specify STRING if the length or precision of numeric values might 
cause truncation or rounding errors.
Type: String
Valid Values: STRING | LONG
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
ResultSetOptions API Version 2018-08-01 52
RDS Data API API Reference
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-08-01 53
RDS Data API API Reference
SqlParameter
A parameter used in a SQL statement.
Contents
name
The name of the parameter.
Type: String
Required: No
typeHint
A hint that speciﬁes the correct object type for data type mapping. Possible values are as 
follows:
• DATE - The corresponding String parameter value is sent as an object of DATE type to the 
database. The accepted format is YYYY-MM-DD.
• DECIMAL - The corresponding String parameter value is sent as an object of DECIMAL type 
to the database.
• JSON - The corresponding String parameter value is sent as an object of JSON type to the 
database.
• TIME - The corresponding String parameter value is sent as an object of TIME type to the 
database. The accepted format is HH:MM:SS[.FFF].
• TIMESTAMP - The corresponding String parameter value is sent as an object of TIMESTAMP
type to the database. The accepted format is YYYY-MM-DD HH:MM:SS[.FFF].
• UUID - The corresponding String parameter value is sent as an object of UUID type to the 
database.
Type: String
Valid Values: JSON | UUID | TIMESTAMP | DATE | TIME | DECIMAL
Required: No
value
The value of the parameter.
SqlParameter API Version 2018-08-01 54
RDS Data API API Reference
Type: Field object
Note: This object is a Union. Only one member of this object can be speciﬁed or returned.
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-08-01 55
RDS Data API API Reference
SqlStatementResult
The result of a SQL statement.
Note
This data structure is only used with the deprecated ExecuteSql operation. Use the
BatchExecuteStatement or ExecuteStatement operation instead.
Contents
numberOfRecordsUpdated
The number of records updated by a SQL statement.
Type: Long
Required: No
resultFrame
The result set of the SQL statement.
Type: ResultFrame object
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
SqlStatementResult API Version 2018-08-01 56
RDS Data API API Reference
StructValue
A structure value returned by a call.
Note
This data structure is only used with the deprecated ExecuteSql operation. Use the
BatchExecuteStatement or ExecuteStatement operation instead.
Contents
attributes
The attributes returned in the record.
Type: Array of Value objects
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
StructValue API Version 2018-08-01 57
RDS Data API API Reference
UpdateResult
The response elements represent the results of an update.
Contents
generatedFields
Values for ﬁelds generated during the request.
Type: Array of Field objects
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
UpdateResult API Version 2018-08-01 58
RDS Data API API Reference
Value
Contains the value of a column.
Note
This data structure is only used with the deprecated ExecuteSql operation. Use the
BatchExecuteStatement or ExecuteStatement operation instead.
Contents
Important
This data type is a UNION, so only one of the following members can be speciﬁed when 
used or returned.
arrayValues
An array of column values.
Type: Array of Value objects
Required: No
bigIntValue
A value for a column of big integer data type.
Type: Long
Required: No
bitValue
A value for a column of BIT data type.
Type: Boolean
Required: No
Value API Version 2018-08-01 59
RDS Data API API Reference
blobValue
A value for a column of BLOB data type.
Type: Base64-encoded binary data object
Required: No
doubleValue
A value for a column of double data type.
Type: Double
Required: No
intValue
A value for a column of integer data type.
Type: Integer
Required: No
isNull
A NULL value.
Type: Boolean
Required: No
realValue
A value for a column of real data type.
Type: Float
Required: No
stringValue
A value for a column of string data type.
Type: String
Required: No
Contents API Version 2018-08-01 60
RDS Data API API Reference
structValue
A value for a column of STRUCT data type.
Type: StructValue object
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-08-01 61
