# API Reference

## Welcome

API Reference
Amazon RDS Performance Insights
API Version 2018-02-27
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
## Actions

Amazon RDS Performance Insights API Reference
Amazon RDS Performance Insights: API Reference
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
Amazon's trademarks and trade dress may not be used in connection with any product or service 
that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any 
manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are 
the property of their respective owners, who may or may not be aﬃliated with, connected to, or 
sponsored by Amazon.
## CreatePerformanceAnalysisReport

## Request Syntax

## Request Parameters

Amazon RDS Performance Insights API Reference
Table of Contents
Welcome ........................................................................................................................................... 1
Actions .............................................................................................................................................. 2
CreatePerformanceAnalysisReport ............................................................................................................ 3
Request Syntax ........................................................................................................................................ 3
Request Parameters ................................................................................................................................ 3
Response Syntax ...................................................................................................................................... 4
Response Elements ................................................................................................................................. 5
Errors .......................................................................................................................................................... 5
Examples ................................................................................................................................................... 5
See Also ..................................................................................................................................................... 7
DeletePerformanceAnalysisReport ............................................................................................................ 8
Request Syntax ........................................................................................................................................ 8
Request Parameters ................................................................................................................................ 8
Response Elements ................................................................................................................................. 9
Errors .......................................................................................................................................................... 9
Examples ................................................................................................................................................. 10
See Also .................................................................................................................................................. 10
DescribeDimensionKeys ............................................................................................................................. 12
Request Syntax ...................................................................................................................................... 12
Request Parameters .............................................................................................................................. 12
Response Syntax ................................................................................................................................... 17
Response Elements ............................................................................................................................... 17
Errors ....................................................................................................................................................... 18
Examples ................................................................................................................................................. 19
See Also .................................................................................................................................................. 21
GetDimensionKeyDetails ........................................................................................................................... 23
Request Syntax ...................................................................................................................................... 23
Request Parameters .............................................................................................................................. 23
Response Syntax ................................................................................................................................... 25
Response Elements ............................................................................................................................... 26
Errors ....................................................................................................................................................... 26
Examples ................................................................................................................................................. 26
See Also .................................................................................................................................................. 29
GetPerformanceAnalysisReport ............................................................................................................... 31
API Version 2018-02-27 iii
## Response Syntax

Amazon RDS Performance Insights API Reference
Request Syntax ...................................................................................................................................... 31
Request Parameters .............................................................................................................................. 31
Response Syntax ................................................................................................................................... 33
Response Elements ............................................................................................................................... 34
Errors ....................................................................................................................................................... 34
Examples ................................................................................................................................................. 35
See Also .................................................................................................................................................. 37
GetResourceMetadata ................................................................................................................................ 38
Request Syntax ...................................................................................................................................... 38
Request Parameters .............................................................................................................................. 38
Response Syntax ................................................................................................................................... 39
Response Elements ............................................................................................................................... 39
Errors ....................................................................................................................................................... 40
Examples ................................................................................................................................................. 40
See Also .................................................................................................................................................. 41
GetResourceMetrics .................................................................................................................................... 43
Request Syntax ...................................................................................................................................... 43
Request Parameters .............................................................................................................................. 43
Response Syntax ................................................................................................................................... 46
Response Elements ............................................................................................................................... 47
Errors ....................................................................................................................................................... 48
Examples ................................................................................................................................................. 49
See Also .................................................................................................................................................. 51
ListAvailableResourceDimensions ........................................................................................................... 52
Request Syntax ...................................................................................................................................... 52
Request Parameters .............................................................................................................................. 52
Response Syntax ................................................................................................................................... 54
Response Elements ............................................................................................................................... 55
Errors ....................................................................................................................................................... 55
Examples ................................................................................................................................................. 56
See Also .................................................................................................................................................. 57
ListAvailableResourceMetrics ................................................................................................................... 59
Request Syntax ...................................................................................................................................... 59
Request Parameters .............................................................................................................................. 59
Response Syntax ................................................................................................................................... 61
Response Elements ............................................................................................................................... 61
API Version 2018-02-27 iv
## Response Elements

## Errors

## Examples

Amazon RDS Performance Insights API Reference
Errors ....................................................................................................................................................... 62
Examples ................................................................................................................................................. 62
See Also .................................................................................................................................................. 63
ListPerformanceAnalysisReports ............................................................................................................. 65
Request Syntax ...................................................................................................................................... 65
Request Parameters .............................................................................................................................. 65
Response Syntax ................................................................................................................................... 67
Response Elements ............................................................................................................................... 67
Errors ....................................................................................................................................................... 68
Examples ................................................................................................................................................. 68
See Also .................................................................................................................................................. 70
ListTagsForResource ................................................................................................................................... 72
Request Syntax ...................................................................................................................................... 72
Request Parameters .............................................................................................................................. 72
Response Syntax ................................................................................................................................... 73
Response Elements ............................................................................................................................... 73
Errors ....................................................................................................................................................... 73
Examples ................................................................................................................................................. 74
See Also .................................................................................................................................................. 75
TagResource ................................................................................................................................................. 76
Request Syntax ...................................................................................................................................... 76
Request Parameters .............................................................................................................................. 76
Response Elements ............................................................................................................................... 77
Errors ....................................................................................................................................................... 77
Examples ................................................................................................................................................. 78
See Also .................................................................................................................................................. 79
UntagResource ............................................................................................................................................ 80
Request Syntax ...................................................................................................................................... 80
Request Parameters .............................................................................................................................. 80
Response Elements ............................................................................................................................... 81
Errors ....................................................................................................................................................... 81
Examples ................................................................................................................................................. 82
See Also .................................................................................................................................................. 83
Data Types ..................................................................................................................................... 84
AnalysisReport ............................................................................................................................................ 86
Contents .................................................................................................................................................. 86
API Version 2018-02-27 v
Amazon RDS Performance Insights API Reference
See Also .................................................................................................................................................. 88
AnalysisReportSummary ........................................................................................................................... 89
Contents .................................................................................................................................................. 89
See Also .................................................................................................................................................. 90
Data ............................................................................................................................................................... 91
Contents .................................................................................................................................................. 91
See Also .................................................................................................................................................. 91
DataPoint ..................................................................................................................................................... 92
Contents .................................................................................................................................................. 92
See Also .................................................................................................................................................. 92
DimensionDetail .......................................................................................................................................... 93
Contents .................................................................................................................................................. 93
See Also .................................................................................................................................................. 93
DimensionGroup ......................................................................................................................................... 94
Contents .................................................................................................................................................. 94
See Also .................................................................................................................................................. 98
DimensionGroupDetail .............................................................................................................................. 99
Contents .................................................................................................................................................. 99
See Also .................................................................................................................................................. 99
DimensionKeyDescription ....................................................................................................................... 100
Contents ............................................................................................................................................... 100
See Also ................................................................................................................................................ 101
DimensionKeyDetail ................................................................................................................................. 102
Contents ............................................................................................................................................... 102
See Also ................................................................................................................................................ 103
FeatureMetadata ...................................................................................................................................... 104
Contents ............................................................................................................................................... 104
See Also ................................................................................................................................................ 104
Insight ......................................................................................................................................................... 106
Contents ............................................................................................................................................... 106
See Also ................................................................................................................................................ 108
MetricDimensionGroups .......................................................................................................................... 109
Contents ............................................................................................................................................... 109
See Also ................................................................................................................................................ 109
MetricKeyDataPoints ............................................................................................................................... 110
Contents ............................................................................................................................................... 110
API Version 2018-02-27 vi
## See Also

Amazon RDS Performance Insights API Reference
See Also ................................................................................................................................................ 110
MetricQuery ............................................................................................................................................... 111
Contents ............................................................................................................................................... 111
See Also ................................................................................................................................................ 112
PerformanceInsightsMetric .................................................................................................................... 114
Contents ............................................................................................................................................... 114
See Also ................................................................................................................................................ 115
Recommendation ..................................................................................................................................... 116
Contents ............................................................................................................................................... 116
See Also ................................................................................................................................................ 116
ResponsePartitionKey .............................................................................................................................. 118
Contents ............................................................................................................................................... 118
See Also ................................................................................................................................................ 118
ResponseResourceMetric ........................................................................................................................ 119
Contents ............................................................................................................................................... 119
See Also ................................................................................................................................................ 120
ResponseResourceMetricKey .................................................................................................................. 121
Contents ............................................................................................................................................... 121
See Also ................................................................................................................................................ 122
Tag ............................................................................................................................................................... 123
Contents ............................................................................................................................................... 123
See Also ................................................................................................................................................ 124
Common Parameters ................................................................................................................... 125
Common Error Types ................................................................................................................... 128
API Version 2018-02-27 vii
## DeletePerformanceAnalysisReport

## Request Syntax

## Request Parameters

Amazon RDS Performance Insights API Reference
Welcome
Amazon RDS Performance Insights enables you to monitor and explore diﬀerent dimensions of 
database load based on data captured from a running DB instance. The guide provides detailed 
information about Performance Insights data types, parameters and errors.
When Performance Insights is enabled, the Amazon RDS Performance Insights API provides 
visibility into the performance of your DB instance. Amazon CloudWatch provides the authoritative 
source for AWS service-vended monitoring metrics. Performance Insights oﬀers a domain-speciﬁc 
view of DB load.
DB load is measured as average active sessions. Performance Insights provides the data to API 
consumers as a two-dimensional time-series dataset. The time dimension provides DB load data for 
each time point in the queried time range. Each time point decomposes overall load in relation to 
the requested dimensions, measured at that time point. Examples include SQL, Wait event, User, 
and Host.
• To learn more about Performance Insights and Amazon Aurora DB instances, go to the   Amazon 
Aurora User Guide .
• To learn more about Performance Insights and Amazon RDS DB instances, go to the   Amazon 
RDS User Guide .
• To learn more about Performance Insights and Amazon DocumentDB clusters, go to the  
Amazon DocumentDB Developer Guide .
This document was last published on April 2, 2026.
API Version 2018-02-27 1
## Response Elements

## Errors

Amazon RDS Performance Insights API Reference
Actions
The following actions are supported:
• CreatePerformanceAnalysisReport
• DeletePerformanceAnalysisReport
• DescribeDimensionKeys
• GetDimensionKeyDetails
• GetPerformanceAnalysisReport
• GetResourceMetadata
• GetResourceMetrics
• ListAvailableResourceDimensions
• ListAvailableResourceMetrics
• ListPerformanceAnalysisReports
• ListTagsForResource
• TagResource
• UntagResource
API Version 2018-02-27 2
## Examples

## See Also

Amazon RDS Performance Insights API Reference
CreatePerformanceAnalysisReport
Creates a new performance analysis report for a speciﬁc time period for the DB instance.
Request Syntax
{ 
   "EndTime": number, 
   "Identifier": "string", 
   "ServiceType": "string", 
   "StartTime": number, 
   "Tags": [  
      {  
         "Key": "string", 
         "Value": "string" 
      } 
   ]
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
EndTime
The end time deﬁned for the analysis report.
Type: Timestamp
Required: Yes
Identiﬁer
An immutable, AWS Region-unique identiﬁer for a data source. Performance Insights gathers 
metrics from this data source.
CreatePerformanceAnalysisReport API Version 2018-02-27 3
Amazon RDS Performance Insights API Reference
To use an Amazon RDS instance as a data source, you specify its DbiResourceId value. For 
example, specify db-ADECBTYHKTSAUMUZQYPDS2GW4A.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-]+$
Required: Yes
ServiceType
The AWS service for which Performance Insights will return metrics. Valid value is RDS.
Type: String
Valid Values: RDS | DOCDB
Required: Yes
StartTime
The start time deﬁned for the analysis report.
Type: Timestamp
Required: Yes
Tags
The metadata assigned to the analysis report consisting of a key-value pair.
Type: Array of Tag objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No
Response Syntax
{ 
   "AnalysisReportId": "string"
}
Response Syntax API Version 2018-02-27 4
## DescribeDimensionKeys

## Request Syntax

## Request Parameters

Amazon RDS Performance Insights API Reference
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
AnalysisReportId
A unique identiﬁer for the created analysis report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: report-[0-9a-f]{17}
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
HTTP Status Code: 400
Examples
Create a performance analysis report
The following example creates a performance analysis report for the speciﬁed time period and 
adds the speciﬁed tag to the report.
Response Elements API Version 2018-02-27 5
Amazon RDS Performance Insights API Reference
Sample Request
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.CreatePerformanceAnalysisReport
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{ 
    "ServiceType": "RDS", 
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
    "StartTime": 1689280091, 
    "EndTime": 1689282071, 
    "Tags": [{ 
        "Key": "Name", 
        "Value": "MyName" 
    }]
}
Sample Response
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive
{ 
    "AnalysisReportId": "report-01234567890abcdef"
} 
                 
Examples API Version 2018-02-27 6
Amazon RDS Performance Insights API Reference
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
See Also API Version 2018-02-27 7
Amazon RDS Performance Insights API Reference
DeletePerformanceAnalysisReport
Deletes a performance analysis report.
Request Syntax
{ 
   "AnalysisReportId": "string", 
   "Identifier": "string", 
   "ServiceType": "string"
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
AnalysisReportId
The unique identiﬁer of the analysis report for deletion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: report-[0-9a-f]{17}
Required: Yes
Identiﬁer
An immutable identiﬁer for a data source that is unique for an AWS Region. Performance 
Insights gathers metrics from this data source. In the console, the identiﬁer is shown 
as ResourceID. When you call DescribeDBInstances, the identiﬁer is returned as
DbiResourceId.
DeletePerformanceAnalysisReport API Version 2018-02-27 8
Amazon RDS Performance Insights API Reference
To use a DB instance as a data source, specify its DbiResourceId value. For example, specify
db-ABCDEFGHIJKLMNOPQRSTU1VW2X.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-]+$
Required: Yes
ServiceType
The AWS service for which Performance Insights will return metrics. Valid value is RDS.
Type: String
Valid Values: RDS | DOCDB
Required: Yes
Response Elements
If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
HTTP Status Code: 400
Response Elements API Version 2018-02-27 9
## Response Syntax

## Response Elements

Amazon RDS Performance Insights API Reference
Examples
Delete a perfornamce analysis report
The following example deletes the performance analysis report report-01234567890abcdef.
Sample Request
                    POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.GetPerformanceAnalysisReport
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{ 
    "AnalysisReportId": "report-01234567890abcdef", 
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
    "ServiceType": "RDS"
} 
                 
Sample Response
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive 
                 
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
Examples API Version 2018-02-27 10
## Errors

Amazon RDS Performance Insights API Reference
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
See Also API Version 2018-02-27 11
## Examples

Amazon RDS Performance Insights API Reference
DescribeDimensionKeys
For a speciﬁc time period, retrieve the top N dimension keys for a metric.
Note
Each response element returns a maximum of 500 bytes. For larger elements, such as SQL 
statements, only the ﬁrst 500 bytes are returned.
Request Syntax
{ 
   "AdditionalMetrics": [ "string" ], 
   "EndTime": number, 
   "Filter": {  
      "string" : "string"  
   }, 
   "GroupBy": {  
      "Dimensions": [ "string" ], 
      "Group": "string", 
      "Limit": number
   }, 
   "Identifier": "string", 
   "MaxResults": number, 
   "Metric": "string", 
   "NextToken": "string", 
   "PartitionBy": {  
      "Dimensions": [ "string" ], 
      "Group": "string", 
      "Limit": number
   }, 
   "PeriodInSeconds": number, 
   "ServiceType": "string", 
   "StartTime": number
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
DescribeDimensionKeys API Version 2018-02-27 12
Amazon RDS Performance Insights API Reference
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
EndTime
The date and time specifying the end of the requested time series data. The value speciﬁed is
exclusive, which means that data points less than (but not equal to) EndTime are returned.
The value for EndTime must be later than the value for StartTime.
Type: Timestamp
Required: Yes
GroupBy
A speciﬁcation for how to aggregate the data points from a query result. You must specify a 
valid dimension group. Performance Insights returns all dimensions within this group, unless 
you provide the names of speciﬁc dimensions within this group. You can also request that 
Performance Insights return a limited number of values for a dimension.
Type: DimensionGroup object
Required: Yes
Identiﬁer
An immutable, AWS Region-unique identiﬁer for a data source. Performance Insights gathers 
metrics from this data source.
To use an Amazon RDS instance as a data source, you specify its DbiResourceId value. For 
example, specify db-FAIHNTYBKTGAUSUZQYPDS2GW4A.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-]+$
Required: Yes
Request Parameters API Version 2018-02-27 13
## See Also

Amazon RDS Performance Insights API Reference
Metric
The name of a Performance Insights metric to be measured.
Valid values for Metric are:
• db.load.avg - A scaled representation of the number of active sessions for the database 
engine.
• db.sampledload.avg - The raw number of active sessions for the database engine.
If the number of active sessions is less than an internal Performance Insights threshold,
db.load.avg and db.sampledload.avg are the same value. If the number of active sessions 
is greater than the internal threshold, Performance Insights samples the active sessions, with
db.load.avg showing the scaled values, db.sampledload.avg showing the raw values, 
and db.sampledload.avg less than db.load.avg. For most use cases, you can query
db.load.avg only.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: Yes
ServiceType
The AWS service for which Performance Insights will return metrics. Valid values are as follows:
• RDS
• DOCDB
Type: String
Valid Values: RDS | DOCDB
Required: Yes
StartTime
The date and time specifying the beginning of the requested time series data. You must specify 
a StartTime within the past 7 days. The value speciﬁed is inclusive, which means that data 
points equal to or greater than StartTime are returned.
The value for StartTime must be earlier than the value for EndTime.
Request Parameters API Version 2018-02-27 14
Amazon RDS Performance Insights API Reference
Type: Timestamp
Required: Yes
AdditionalMetrics
Additional metrics for the top N dimension keys. If the speciﬁed dimension group in the
GroupBy parameter is db.sql_tokenized, you can specify per-SQL metrics to get the values 
for the top N SQL digests. The response syntax is as follows: "AdditionalMetrics" : 
{ "string" : "string" }.
The only supported statistic function is .avg.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-_\.:/*)( ]+$
Required: No
Filter
One or more ﬁlters to apply in the request. Restrictions:
• Any number of ﬁlters by the same dimension, as speciﬁed in the GroupBy or Partition
parameters.
• A single ﬁlter for any other dimension in this dimension group.
Note
The db.sql.db_id ﬁlter isn't available for RDS for SQL Server DB instances.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: ^[a-zA-Z0-9-_\.:/*)( ]+$
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: .*\S.*
Request Parameters API Version 2018-02-27 15
## GetDimensionKeyDetails

## Request Syntax

## Request Parameters

Amazon RDS Performance Insights API Reference
Required: No
MaxResults
The maximum number of items to return in the response. If more items exist than the speciﬁed
MaxRecords value, a pagination token is included in the response so that the remaining results 
can be retrieved.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No
NextToken
An optional pagination token provided by a previous request. If this parameter is speciﬁed, the 
response includes only records beyond the token, up to the value speciﬁed by MaxRecords.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: ^[a-zA-Z0-9_=-]+$
Required: No
PartitionBy
For each dimension speciﬁed in GroupBy, specify a secondary dimension to further subdivide 
the partition keys in the response.
Type: DimensionGroup object
Required: No
PeriodInSeconds
The granularity, in seconds, of the data points returned from Performance Insights. A period can 
be as short as one second, or as long as one day (86400 seconds). Valid values are:
• 1 (one second)
• 60 (one minute)
• 300 (ﬁve minutes)
• 3600 (one hour)
Request Parameters API Version 2018-02-27 16
Amazon RDS Performance Insights API Reference
• 86400 (twenty-four hours)
If you don't specify PeriodInSeconds, then Performance Insights chooses a value for you, 
with a goal of returning roughly 100-200 data points in the response.
Type: Integer
Required: No
Response Syntax
{ 
   "AlignedEndTime": number, 
   "AlignedStartTime": number, 
   "Keys": [  
      {  
         "AdditionalMetrics": {  
            "string" : number 
         }, 
         "Dimensions": {  
            "string" : "string"  
         }, 
         "Partitions": [ number ], 
         "Total": number
      } 
   ], 
   "NextToken": "string", 
   "PartitionKeys": [  
      {  
         "Dimensions": {  
            "string" : "string"  
         } 
      } 
   ]
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
Response Syntax API Version 2018-02-27 17
## Response Syntax

Amazon RDS Performance Insights API Reference
AlignedEndTime
The end time for the returned dimension keys, after alignment to a granular boundary (as 
speciﬁed by PeriodInSeconds). AlignedEndTime will be greater than or equal to the value 
of the user-speciﬁed Endtime.
Type: Timestamp
AlignedStartTime
The start time for the returned dimension keys, after alignment to a granular boundary (as 
speciﬁed by PeriodInSeconds). AlignedStartTime will be less than or equal to the value of 
the user-speciﬁed StartTime.
Type: Timestamp
Keys
The dimension keys that were requested.
Type: Array of DimensionKeyDescription objects
NextToken
A pagination token that indicates the response didn’t return all available records because
MaxRecords was speciﬁed in the previous request. To get the remaining records, specify
NextToken in a separate request with this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: ^[a-zA-Z0-9_=-]+$
PartitionKeys
If PartitionBy was present in the request, PartitionKeys contains the breakdown of 
dimension keys by the speciﬁed partitions.
Type: Array of ResponsePartitionKey objects
Errors
For information about the errors that are common to all actions, see Common Error Types.
Errors API Version 2018-02-27 18
## Response Elements

## Errors

## Examples

Amazon RDS Performance Insights API Reference
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
HTTP Status Code: 400
Examples
Retrieve top dimension keys
The following example retrieves the top 10 dimension keys for metrics db.load.avg,
db.sql_tokenized.stats.calls_per_sec.avg, and db.sql_tokenized.statement
over a speciﬁc 5-minute time range. The request returns the metrics in dimension groups
db.sql_tokenized.id and db.sql_tokenized.statement. For both of these dimension 
groups, the request subdivides the partition keys by db.user.id and db.user.name.
Sample Request
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.DescribeDimensionKeys
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>  
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{ 
Examples API Version 2018-02-27 19
Amazon RDS Performance Insights API Reference
   "ServiceType": "RDS", 
   "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
   "StartTime": 1603915200, 
   "EndTime": 1603918800, 
   "PeriodInSeconds": 300, 
   "Metric": "db.load.avg", 
   "GroupBy": {  
      "Dimensions": [ "db.sql_tokenized.id", "db.sql_tokenized.statement" ], 
      "Group": "db.sql_tokenized", 
      "Limit": 5 
   }, 
   "Filter": {  
      "db.user.name" : "example-user"  
   }, 
   "PartitionBy": {  
      "Dimensions": [ "db.user.id", "db.user.name" ], 
      "Group": "db.user", 
      "Limit": 5 
   }, 
   "MaxResults": 10, 
   "AdditionalMetrics": [ 
      "db.sql_tokenized.stats.calls_per_sec.avg", 
      "db.sql_tokenized.stats.rows_per_sec.avg" 
   ]
}
Sample Response
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>  
Content-Length: <PayloadSizeBytes>
Connection: keep-alive
{ 
   "AlignedEndTime": 1.6244895E9, 
   "AlignedStartTime": 1.6244889E9, 
   "Keys": [  
      {  
         "Dimensions": {  
            "db.sql_tokenized.id" : "12A345BCDE67F8G9H012I3IJKI4J5675K8L912M", 
Examples API Version 2018-02-27 20
Amazon RDS Performance Insights API Reference
            "db.sql_tokenized.statement" : "INSERT INTO pgbench_history (tid, bid, aid, 
 delta, mtime) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP);" 
         }, 
         "Partitions": [ 2.1333333333333333 ], 
         "Total": 2.1333333333333333, 
         "AdditionalMetrics" : { 
            "db.sql_tokenized.stats.calls_per_sec.avg": 1.0, 
            "db.sql_tokenized.stats.rows_per_sec.avg": 3.0 
         } 
      }, 
      ...... 
   ], 
   "PartitionKeys": [  
     { 
        "Dimensions": { 
          "db.user.name": "example-user", 
          "db.user.id": "A12B3456C7D8E890F123F45G67HIJ8K9LM0N1O2" 
        } 
     } 
   ]
}
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
See Also API Version 2018-02-27 21
## See Also

Amazon RDS Performance Insights API Reference
See Also API Version 2018-02-27 22
Amazon RDS Performance Insights API Reference
GetDimensionKeyDetails
Get the attributes of the speciﬁed dimension group for a DB instance or data source. For 
example, if you specify a SQL ID, GetDimensionKeyDetails retrieves the full text of the 
dimension db.sql.statement associated with this ID. This operation is useful because
GetResourceMetrics and DescribeDimensionKeys don't support retrieval of large SQL 
statement text, lock snapshots, and execution plans.
Request Syntax
{ 
   "Group": "string", 
   "GroupIdentifier": "string", 
   "Identifier": "string", 
   "RequestedDimensions": [ "string" ], 
   "ServiceType": "string"
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
Group
The name of the dimension group. Performance Insights searches the speciﬁed group for the 
dimension group ID. The following group name values are valid:
• db.execution_plan (Amazon RDS and Aurora only)
• db.lock_snapshot (Aurora only)
• db.query (Amazon DocumentDB only)
• db.sql (Amazon RDS and Aurora only)
Type: String
GetDimensionKeyDetails API Version 2018-02-27 23
## GetPerformanceAnalysisReport

Amazon RDS Performance Insights API Reference
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: Yes
GroupIdentiﬁer
The ID of the dimension group from which to retrieve dimension details. For dimension group
db.sql, the group ID is db.sql.id. The following group ID values are valid:
• db.execution_plan.id for dimension group db.execution_plan (Aurora and RDS only)
• db.sql.id for dimension group db.sql (Aurora and RDS only)
• db.query.id for dimension group db.query (DocumentDB only)
• For the dimension group db.lock_snapshot, the GroupIdentifier is the epoch 
timestamp when Performance Insights captured the snapshot, in seconds. You can retrieve 
this value with the GetResourceMetrics operation for a 1 second period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: Yes
Identiﬁer
The ID for a data source from which to gather dimension data. This ID must be immutable 
and unique within an AWS Region. When a DB instance is the data source, specify its
DbiResourceId value. For example, specify db-ABCDEFGHIJKLMNOPQRSTU1VW2X.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-]+$
Required: Yes
ServiceType
The AWS service for which Performance Insights returns data. The only valid value is RDS.
Type: String
Request Parameters API Version 2018-02-27 24
Amazon RDS Performance Insights API Reference
Valid Values: RDS | DOCDB
Required: Yes
RequestedDimensions
A list of dimensions to retrieve the detail data for within the given dimension group. If you don't 
specify this parameter, Performance Insights returns all dimension data within the speciﬁed 
dimension group. Specify dimension names for the following dimension groups:
• db.execution_plan - Specify the dimension name db.execution_plan.raw_plan or 
the short dimension name raw_plan (Amazon RDS and Aurora only)
• db.lock_snapshot - Specify the dimension name db.lock_snapshot.lock_trees or 
the short dimension name lock_trees. (Aurora only)
• db.sql - Specify either the full dimension name db.sql.statement or the short 
dimension name statement (Aurora and RDS only).
• db.query - Specify either the full dimension name db.query.statement or the short 
dimension name statement (DocumentDB only).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-_\.:/*)( ]+$
Required: No
Response Syntax
{ 
   "Dimensions": [  
      {  
         "Dimension": "string", 
         "Status": "string", 
         "Value": "string" 
      } 
   ]
}
Response Syntax API Version 2018-02-27 25
Amazon RDS Performance Insights API Reference
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
Dimensions
The details for the requested dimensions.
Type: Array of DimensionKeyDetail objects
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
HTTP Status Code: 400
Examples
Retrieve the full SQL text for a query
The following example requests the full text for the SQL query with the ID example-
group-identifier, which is a placeholder for a SQL ID that you retrieved by calling
GetResourceMetrics or DescribeDimensionKeys. Because the dimension details are 
available, the response shows the full SQL text.
Response Elements API Version 2018-02-27 26
Amazon RDS Performance Insights API Reference
Sample Request
{ 
    "ServiceType":"RDS", 
    "Identifier":"db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
    "Group": "db.sql", 
    "GroupIdentifier": "example-group-identifier", 
    "RequestedDimensions": ["statement"]
}
Sample Response
{ 
    "Dimensions":[ 
    { 
        "Value": "SELECT e.last_name, d.department_name FROM employees e, departments d 
 WHERE e.department_id=d.department_id", 
        "Dimension": "db.sql.statement", 
        "Status": "AVAILABLE" 
    }, 
    ... 
    ]
}
Retrieve locking data for a database at a point in time
The following example requests locking data at the epoch timestamp 1730231303. You can 
retrieve the epoch timestamp with the GetResourceMetrics operation for a 1 second period.
Note that Performance Insights uses the comma-separated values format for the response. Each 
column value is enclosed in double quotation marks (" ") and separated by a comma. Each line is 
separated by a new line. The ﬁrst line in the response describes the column names, and each of the 
following lines represents session data from a blocking or blocked session. The value level is the 
level of the session in the blocking tree hierarchy. For example, the session at level 0 is blocking the 
sessions at level 1.
Sample Request
{ 
    "ServiceType":"RDS", 
    "Identifier":"db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
Examples API Version 2018-02-27 27
Amazon RDS Performance Insights API Reference
    "Group": "db.lock_snapshot", 
    "GroupIdentifier": "1730231303", 
    "RequestedDimensions": ["lock_trees"]
}
Sample Response
{ 
    "Dimensions":[ 
    { 
        "Value": "\"level\",\"blocked_sessions_count\",\"pid\",\"session_id
\",\"blocking_mode\",\"waiting_mode\",\"last_query_executed\",\"application
\",\"blocking_txn_start_time\",\"waiting_start_time\",\"session_start_time
\",\"state\",\"wait_event_type\",\"wait_event\",\"last_query_exec_time\",
\"user\",\"host\",\"port\",\"client_address\",\"granted\",\"waiting_tuple\",
\"waiting_page\",\"waiting_transaction_id\",\"waiting_relation\",\"waiting_object_id
\",\"waiting_database_id\",\"waiting_database_name\",\"waiting_locktype\",
\"blocking_time_(In_Seconds)\"\n\"0\",\"4\",\"28599\",\"63bcb300.6fb7\",\"\",\"\",
\"update sbtest1 set id = 200000 where id=1;\",\"psql\",\"\",\"\",\"1672533380000\",
\"idle in transaction\",\"Client\",\"ClientRead\",\"1672533380000\",\"postgres\",\"\",
\"37444\",\"34.222.155.102\",\"t\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"42\"\n
\"1\",\"3\",\"30877\",\"63bcbc21.789d\",\"ExclusiveLock\",\"ShareLock\",\"update 
 sbtest1 set id=20000 where id=1;\",\"psql\",\"1672533380000\",\"1672535758000\",
\"1672535758000\",\"active\",\"Lock\",\"transactionid\",\"1672535758000\",\"postgres
\",\"\",\"35064\",\"34.222.155.102\",\"f\",\"\",\"\",\"569470\",\"\",\"\",\"\",
\"sbtest\",\"transactionid\",\"2430\"\n\"2\",\"2\",\"30937\",\"63bcbc5c.78d9\",
\"AccessExclusiveLock\",\"AccessExclusiveLock\",\"update sbtest1 set id = 200000 where 
 id=1;\",\"psql\",\"1672535758000\",\"1672533370000\",\"1672533370000\",\"active\",
\"Lock\",\"tuple\",\"1672533370000\",\"postgres\",\"\",\"37398\",\"34.222.155.102\",
\"f\",\"1\",\"0\",\"\",\"16946\",\"\",\"16839\",\"sbtest\",\"tuple\",\"2470\"\n
\"3\",\"1\",\"31029\",\"63bcbcbf.7935\",\"AccessExclusiveLock\",\"AccessExclusiveLock
\",\"update sbtest1 set id = 200000 where id=1;\",\"psql\",\"1672533370000\",
\"1672533330000\",\"1672533330000\",\"active\",\"Lock\",\"tuple\",\"1672533330000\",
\"postgres\",\"\",\"36266\",\"34.222.155.102\",\"f\",\"1\",\"0\",\"\",\"16946\",\"\",
\"16839\",\"sbtest\",\"tuple\",\"2440\"\n\"4\",\"0\",\"31062\",\"63bcbcd8.7956\",
\"AccessExclusiveLock\",\"AccessExclusiveLock\",\"update sbtest1 set id = 200000 where 
 id=1;\",\"psql\",\"1672533330000\",\"1672533360000\",\"1672533360000\",\"active\",
\"Lock\",\"tuple\",\"1672533360000\",\"postgres\",\"\",\"56694\",\"34.222.155.102\",\"f
\",\"1\",\"0\",\"\",\"16946\",\"\",\"16839\",\"sbtest\",\"tuple\",\"\"\n", 
        "Dimension": "db.lock_snapshot", 
        "Status": "AVAILABLE" 
    }, 
    ... 
Examples API Version 2018-02-27 28
Amazon RDS Performance Insights API Reference
    ]
}
Retrieve execution plans for a database
The following example requests execution plans for a database, where the plan ID is 435345209.
Sample Request
{ 
      "ServiceType": "RDS", 
      "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
      "GroupIdentifier": "435345209", 
      "Group": "db.execution_plan", 
      "RequestedDimensions": ["raw_plan"]
}
Sample Response
{ 
      "Dimensions":[ 
      { 
         "Value": "Update on orders  (cost=0.43..8.46 rows=0 width=0)\n  ->  Index Scan 
 using orders_pk on orders  (cost=0.43..8.46 rows=1 width=14)\n        Index Cond: 
 (order_id = 200)" 
         "Dimension": "db.execution_plan.raw_plan", 
         "Status": "AVAILABLE", 
      } 
      ]
}
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
See Also API Version 2018-02-27 29
Amazon RDS Performance Insights API Reference
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 30
Amazon RDS Performance Insights API Reference
GetPerformanceAnalysisReport
Retrieves the report including the report ID, status, time details, and the insights with 
recommendations. The report status can be RUNNING, SUCCEEDED, or FAILED. The insights include 
the description and recommendation ﬁelds.
Request Syntax
{ 
   "AcceptLanguage": "string", 
   "AnalysisReportId": "string", 
   "Identifier": "string", 
   "ServiceType": "string", 
   "TextFormat": "string"
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
AnalysisReportId
A unique identiﬁer of the created analysis report. For example, report-12345678901234567
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: report-[0-9a-f]{17}
Required: Yes
Identiﬁer
An immutable identiﬁer for a data source that is unique for an AWS Region. Performance 
Insights gathers metrics from this data source. In the console, the identiﬁer is shown 
GetPerformanceAnalysisReport API Version 2018-02-27 31
Amazon RDS Performance Insights API Reference
as ResourceID. When you call DescribeDBInstances, the identiﬁer is returned as
DbiResourceId.
To use a DB instance as a data source, specify its DbiResourceId value. For example, specify
db-ABCDEFGHIJKLMNOPQRSTU1VW2X.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-]+$
Required: Yes
ServiceType
The AWS service for which Performance Insights will return metrics. Valid value is RDS.
Type: String
Valid Values: RDS | DOCDB
Required: Yes
AcceptLanguage
The text language in the report. The default language is EN_US (English).
Type: String
Valid Values: EN_US
Required: No
TextFormat
Indicates the text format in the report. The options are PLAIN_TEXT or MARKDOWN. The default 
value is plain text.
Type: String
Valid Values: PLAIN_TEXT | MARKDOWN
Required: No
Request Parameters API Version 2018-02-27 32
Amazon RDS Performance Insights API Reference
Response Syntax
{ 
   "AnalysisReport": {  
      "AnalysisReportId": "string", 
      "CreateTime": number, 
      "EndTime": number, 
      "Identifier": "string", 
      "Insights": [  
         {  
            "BaselineData": [  
               {  
                  "PerformanceInsightsMetric": {  
                     "Dimensions": {  
                        "string" : "string"  
                     }, 
                     "DisplayName": "string", 
                     "Filter": {  
                        "string" : "string"  
                     }, 
                     "Metric": "string", 
                     "Value": number
                  } 
               } 
            ], 
            "Context": "string", 
            "Description": "string", 
            "EndTime": number, 
            "InsightData": [  
               {  
                  "PerformanceInsightsMetric": {  
                     "Dimensions": {  
                        "string" : "string"  
                     }, 
                     "DisplayName": "string", 
                     "Filter": {  
                        "string" : "string"  
                     }, 
                     "Metric": "string", 
                     "Value": number
                  } 
               } 
            ], 
Response Syntax API Version 2018-02-27 33
Amazon RDS Performance Insights API Reference
            "InsightId": "string", 
            "InsightType": "string", 
            "Recommendations": [  
               {  
                  "RecommendationDescription": "string", 
                  "RecommendationId": "string" 
               } 
            ], 
            "Severity": "string", 
            "StartTime": number, 
            "SupportingInsights": [  
               "Insight" 
            ] 
         } 
      ], 
      "ServiceType": "string", 
      "StartTime": number, 
      "Status": "string" 
   }
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
AnalysisReport
The summary of the performance analysis report created for a time period.
Type: AnalysisReport object
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
Response Elements API Version 2018-02-27 34
Amazon RDS Performance Insights API Reference
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
HTTP Status Code: 400
Examples
Retrieve a performance analysis report
The following example gets the report insights and other details for the report
report-01234567890abcdef.
Sample Request
                    POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.GetPerformanceAnalysisReport
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{ 
    "AnalysisReportId": "report-01234567890abcdef", 
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
    "ServiceType": "RDS"
} 
                 
Sample Response
Examples API Version 2018-02-27 35
Amazon RDS Performance Insights API Reference
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive
{ 
    "AnalysisReport": { 
        "AnalysisReportId": "report-01234567890abcdef", 
        "CreateTime": 1690906983.028, 
        "EndTime": 1690453065, 
        "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
        "Insights": [ 
            { 
                "BaselineData": [ 
                    { 
                        "PerformanceInsightsMetric": { 
                            "Dimensions": {}, 
                            "Metric": "db.load.avg", 
                            "Value": 0 
                        } 
                    } 
                ], 
                "Context": "CAUSAL", 
                "Description": "The database is idle, with no detectable load for the 
 time range.", 
                "EndTime": 1690453065, 
                "InsightData": [ 
                    { 
                        "PerformanceInsightsMetric": { 
                            "Dimensions": {}, 
                            "Metric": "db.load.avg", 
                            "Value": 0 
                        } 
                    } 
                ], 
                "InsightId": 
 "MURCX0xPQURfWkVSTwY8NIdQhkWEeU19Zybf8H636v470O8ID2uUn6uLWFp5MDAwMDAwMDAw", 
                "InsightType": "DB_LOAD_ZERO", 
                "Recommendations": [ 
                    { 
                        "RecommendationDescription": "Try creating an analysis report 
 for a different time range.", 
Examples API Version 2018-02-27 36
Amazon RDS Performance Insights API Reference
                        "RecommendationId": 
 "MVJlY29tbWVuZGF0aW9uREJfTE9BRF9aRVJPvXe8CGe_f-ZX2tY-
Em61aD6v2u9wcPi58j_zY28eKEwwMDAwMDAwMDA=" 
                    } 
                ], 
                "Severity": "LOW", 
                "StartTime": 1690009222, 
                "SupportingInsights": [] 
            } 
        ], 
        "ServiceType": "RDS", 
        "StartTime": 1690009222, 
        "Status": "SUCCEEDED" 
    }
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
See Also API Version 2018-02-27 37
Amazon RDS Performance Insights API Reference
GetResourceMetadata
Retrieve the metadata for diﬀerent features. For example, the metadata might indicate that a 
feature is turned on or oﬀ on a speciﬁc DB instance.
Request Syntax
{ 
   "Identifier": "string", 
   "ServiceType": "string"
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
Identiﬁer
An immutable identiﬁer for a data source that is unique for an AWS Region. Performance 
Insights gathers metrics from this data source. To use a DB instance as a data source, specify its
DbiResourceId value. For example, specify db-ABCDEFGHIJKLMNOPQRSTU1VW2X.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-]+$
Required: Yes
ServiceType
The AWS service for which Performance Insights returns metrics.
GetResourceMetadata API Version 2018-02-27 38
Amazon RDS Performance Insights API Reference
Type: String
Valid Values: RDS | DOCDB
Required: Yes
Response Syntax
{ 
   "Features": {  
      "string" : {  
         "Status": "string" 
      } 
   }, 
   "Identifier": "string"
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
Features
The metadata for diﬀerent features. For example, the metadata might indicate that a feature is 
turned on or oﬀ on a speciﬁc DB instance.
Type: String to FeatureMetadata object map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: .*\S.*
Identiﬁer
An immutable identiﬁer for a data source that is unique for an AWS Region. Performance 
Insights gathers metrics from this data source. To use a DB instance as a data source, specify its
DbiResourceId value. For example, specify db-ABCDEFGHIJKLMNOPQRSTU1VW2X.
Type: String
Response Syntax API Version 2018-02-27 39
Amazon RDS Performance Insights API Reference
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
HTTP Status Code: 400
Examples
Retrieve metadata for diﬀerent features
The following example requests all metadata for the database with the ID db-
ABC1DEFGHIJKL2MNOPQRSTUV3W. The response shows that SQL digest statistics are enabled.
Sample Request
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.GetResourceMetadata
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Errors API Version 2018-02-27 40
Amazon RDS Performance Insights API Reference
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{     
    "ServiceType": "RDS",     
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W"
}
Sample Response
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>  
Content-Length: <PayloadSizeBytes>
Connection: keep-alive
{     
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
    "Features":{ 
        "SQL_DIGEST_STATISTICS":{ 
            "Status": "ENABLED" 
        } 
    }
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
See Also API Version 2018-02-27 41
Amazon RDS Performance Insights API Reference
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 42
Amazon RDS Performance Insights API Reference
GetResourceMetrics
Retrieve Performance Insights metrics for a set of data sources over a time period. You can provide 
speciﬁc dimension groups and dimensions, and provide ﬁltering criteria for each group. You must 
specify an aggregate function for each metric.
Note
Each response element returns a maximum of 500 bytes. For larger elements, such as SQL 
statements, only the ﬁrst 500 bytes are returned.
Request Syntax
{ 
   "EndTime": number, 
   "Identifier": "string", 
   "MaxResults": number, 
   "MetricQueries": [  
      {  
         "Filter": {  
            "string" : "string"  
         }, 
         "GroupBy": {  
            "Dimensions": [ "string" ], 
            "Group": "string", 
            "Limit": number
         }, 
         "Metric": "string" 
      } 
   ], 
   "NextToken": "string", 
   "PeriodAlignment": "string", 
   "PeriodInSeconds": number, 
   "ServiceType": "string", 
   "StartTime": number
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
GetResourceMetrics API Version 2018-02-27 43
Amazon RDS Performance Insights API Reference
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
EndTime
The date and time specifying the end of the requested time series query range. The value 
speciﬁed is exclusive. Thus, the command returns data points less than (but not equal to)
EndTime.
The value for EndTime must be later than the value for StartTime.
Type: Timestamp
Required: Yes
Identiﬁer
An immutable identiﬁer for a data source that is unique for an AWS Region. Performance 
Insights gathers metrics from this data source. In the console, the identiﬁer is shown 
as ResourceID. When you call DescribeDBInstances, the identiﬁer is returned as
DbiResourceId.
To use a DB instance as a data source, specify its DbiResourceId value. For example, specify
db-ABCDEFGHIJKLMNOPQRSTU1VW2X.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-]+$
Required: Yes
MetricQueries
An array of one or more queries to perform. Each query must specify a Performance Insights 
metric and specify an aggregate function, and you can provide ﬁltering criteria. You must 
append the aggregate function to the metric. For example, to ﬁnd the average for the metric
db.load you must use db.load.avg. Valid values for aggregate functions include .avg,
.min, .max, and .sum.
Request Parameters API Version 2018-02-27 44
Amazon RDS Performance Insights API Reference
Type: Array of MetricQuery objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: Yes
ServiceType
The AWS service for which Performance Insights returns metrics. Valid values are as follows:
• RDS
• DOCDB
Type: String
Valid Values: RDS | DOCDB
Required: Yes
StartTime
The date and time specifying the beginning of the requested time series query range. You can't 
specify a StartTime that is earlier than 7 days ago. By default, Performance Insights has 7 
days of retention, but you can extend this range up to 2 years. The value speciﬁed is inclusive. 
Thus, the command returns data points equal to or greater than StartTime.
The value for StartTime must be earlier than the value for EndTime.
Type: Timestamp
Required: Yes
MaxResults
The maximum number of items to return in the response.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No
NextToken
An optional pagination token provided by a previous request. If this parameter is speciﬁed, the 
response includes only records beyond the token, up to the value speciﬁed by MaxRecords.
Request Parameters API Version 2018-02-27 45
Amazon RDS Performance Insights API Reference
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: ^[a-zA-Z0-9_=-]+$
Required: No
PeriodAlignment
The returned timestamp which is the start or end time of the time periods. The default value is
END_TIME.
Type: String
Valid Values: END_TIME | START_TIME
Required: No
PeriodInSeconds
The granularity, in seconds, of the data points returned from Performance Insights. A period can 
be as short as one second, or as long as one day (86400 seconds). Valid values are:
• 1 (one second)
• 60 (one minute)
• 300 (ﬁve minutes)
• 3600 (one hour)
• 86400 (twenty-four hours)
If you don't specify PeriodInSeconds, then Performance Insights will choose a value for you, 
with a goal of returning roughly 100-200 data points in the response.
Type: Integer
Required: No
Response Syntax
{ 
Response Syntax API Version 2018-02-27 46
Amazon RDS Performance Insights API Reference
   "AlignedEndTime": number, 
   "AlignedStartTime": number, 
   "Identifier": "string", 
   "MetricList": [  
      {  
         "DataPoints": [  
            {  
               "Timestamp": number, 
               "Value": number
            } 
         ], 
         "Key": {  
            "Dimensions": {  
               "string" : "string"  
            }, 
            "Metric": "string" 
         } 
      } 
   ], 
   "NextToken": "string"
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
AlignedEndTime
The end time for the returned metrics, after alignment to a granular boundary (as speciﬁed by
PeriodInSeconds). AlignedEndTime will be greater than or equal to the value of the user-
speciﬁed Endtime.
Type: Timestamp
AlignedStartTime
The start time for the returned metrics, after alignment to a granular boundary (as speciﬁed by
PeriodInSeconds). AlignedStartTime will be less than or equal to the value of the user-
speciﬁed StartTime.
Type: Timestamp
Response Elements API Version 2018-02-27 47
Amazon RDS Performance Insights API Reference
Identiﬁer
An immutable identiﬁer for a data source that is unique for an AWS Region. Performance 
Insights gathers metrics from this data source. In the console, the identiﬁer is shown 
as ResourceID. When you call DescribeDBInstances, the identiﬁer is returned as
DbiResourceId.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
MetricList
An array of metric results, where each array element contains all of the data points for a 
particular dimension.
Type: Array of MetricKeyDataPoints objects
NextToken
An optional pagination token provided by a previous request. If this parameter is speciﬁed, the 
response includes only records beyond the token, up to the value speciﬁed by MaxRecords.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: ^[a-zA-Z0-9_=-]+$
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
InvalidArgumentException
One of the arguments provided is invalid for this request.
Errors API Version 2018-02-27 48
Amazon RDS Performance Insights API Reference
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
HTTP Status Code: 400
Examples
Retrieve Data Points for All Dimensions Within a Group
The following example requests data points for the db.wait_event dimension group, and for the
db.wait_event.name dimension within that group. In the response, the relevant data points are 
grouped by the requested dimension (db.wait_event.name).
Sample Request
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.GetResourceMetrics
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>  
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{ 
    "ServiceType": "RDS", 
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
    "MetricQueries": [ 
        { 
            "Metric": "db.load.avg", 
            "GroupBy": { 
                "Group": "db.wait_event", 
                "Dimensions": ["db.wait_event.type"] 
            } 
        } 
    ], 
    "StartTime": 1527026400, 
Examples API Version 2018-02-27 49
Amazon RDS Performance Insights API Reference
    "EndTime": 1527080400, 
    "PeriodInSeconds": 300
}
Sample Response
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>  
Content-Length: <PayloadSizeBytes>
Connection: keep-alive
{ 
    "AlignedEndTime": 1.5270804E9, 
    "AlignedStartTime": 1.5270264E9, 
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
    "MetricList": [ 
        { 
            "Key": { 
                "Metric": "db.load.avg" 
            }, 
            "DataPoints": [ 
                { 
                    "Timestamp": 1527026700.0, 
                    "Value": 1.3533333333333333 
                }, 
                { 
                    "Timestamp": 1527027000.0, 
                    "Value": 0.88 
                }, 
                ... 
            ] 
        }, 
        { 
            "Key": { 
                "Metric": "db.load.avg", 
                "Dimensions": { 
                    "db.wait_event.name": "wait/synch/mutex/innodb/
aurora_lock_thread_slot_futex" 
                } 
            }, 
Examples API Version 2018-02-27 50
Amazon RDS Performance Insights API Reference
            "DataPoints": [ 
                { 
                    "Timestamp": 1527026700.0, 
                    "Value": 0.8566666666666667 
                }, 
                { 
                    "Timestamp": 1527027000.0, 
                    "Value": 0.8633333333333333 
                }, 
                ... 
            ], 
        }, 
        ... 
    ]
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
See Also API Version 2018-02-27 51
Amazon RDS Performance Insights API Reference
ListAvailableResourceDimensions
Retrieve the dimensions that can be queried for each speciﬁed metric type on a speciﬁed DB 
instance.
Request Syntax
{ 
   "AuthorizedActions": [ "string" ], 
   "Identifier": "string", 
   "MaxResults": number, 
   "Metrics": [ "string" ], 
   "NextToken": "string", 
   "ServiceType": "string"
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
Identiﬁer
An immutable identiﬁer for a data source that is unique within an AWS Region. 
Performance Insights gathers metrics from this data source. To use an Amazon RDS DB 
instance as a data source, specify its DbiResourceId value. For example, specify db-
ABCDEFGHIJKLMNOPQRSTU1VWZ.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-]+$
ListAvailableResourceDimensions API Version 2018-02-27 52
Amazon RDS Performance Insights API Reference
Required: Yes
Metrics
The types of metrics for which to retrieve dimensions. Valid values include db.load.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-_\.:/*)( ]+$
Required: Yes
ServiceType
The AWS service for which Performance Insights returns metrics.
Type: String
Valid Values: RDS | DOCDB
Required: Yes
AuthorizedActions
The actions to discover the dimensions you are authorized to access. If you specify multiple 
actions, then the response will contain the dimensions common for all the actions.
When you don't specify this request parameter or provide an empty list, the response contains 
all the available dimensions for the target database engine whether or not you are authorized 
to access them.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: DescribeDimensionKeys | GetDimensionKeyDetails | 
GetResourceMetrics
Required: No
Request Parameters API Version 2018-02-27 53
Amazon RDS Performance Insights API Reference
MaxResults
The maximum number of items to return in the response. If more items exist than the speciﬁed
MaxRecords value, a pagination token is included in the response so that the remaining results 
can be retrieved.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No
NextToken
An optional pagination token provided by a previous request. If this parameter is speciﬁed, the 
response includes only records beyond the token, up to the value speciﬁed by MaxRecords.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: ^[a-zA-Z0-9_=-]+$
Required: No
Response Syntax
{ 
   "MetricDimensions": [  
      {  
         "Groups": [  
            {  
               "Dimensions": [  
                  {  
                     "Identifier": "string" 
                  } 
               ], 
               "Group": "string" 
            } 
         ], 
         "Metric": "string" 
      } 
   ], 
Response Syntax API Version 2018-02-27 54
Amazon RDS Performance Insights API Reference
   "NextToken": "string"
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
MetricDimensions
The dimension information returned for requested metric types.
Type: Array of MetricDimensionGroups objects
NextToken
An optional pagination token provided by a previous request. If this parameter is speciﬁed, the 
response includes only records beyond the token, up to the value speciﬁed by MaxRecords.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: ^[a-zA-Z0-9_=-]+$
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
Response Elements API Version 2018-02-27 55
Amazon RDS Performance Insights API Reference
HTTP Status Code: 400
Examples
Retrieving dimensions for the metric type db.load
The following example retrieves the dimensions for the metric type db.load.
Sample Request
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.DescribeDimensionKeys
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>  
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{ 
    "ServiceType": "RDS",     
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
    "Metrics": ["db.load"]
}
Sample Response
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>  
Content-Length: <PayloadSizeBytes>
Connection: keep-alive
{     
    "MetricDimensions": [ 
        { 
            "Metric": "db.load", 
            "Groups": [ 
Examples API Version 2018-02-27 56
Amazon RDS Performance Insights API Reference
                { 
                    "Group": "db.user", 
                    "Dimensions": [ 
                        { 
                            "Identifier": "db.user.id" 
                        }, 
                        { 
                            "Identifier": "db.user.name" 
                        } 
                    ] 
                }, 
                { 
                    "Group": "db.sql_tokenized", 
                    "Dimensions": [ 
                        { 
                            "Identifier": "db.sql_tokenized.id" 
                        }, 
                        { 
                            "Identifier": "db.sql_tokenized.db_id" 
                        }, 
                        { 
                            "Identifier": "db.sql_tokenized.statement" 
                        } 
                    ]  
                }, 
                ... 
            ] 
        } 
    ]
}
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
See Also API Version 2018-02-27 57
Amazon RDS Performance Insights API Reference
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 58
Amazon RDS Performance Insights API Reference
ListAvailableResourceMetrics
Retrieve metrics of the speciﬁed types that can be queried for a speciﬁed DB instance.
Request Syntax
{ 
   "Identifier": "string", 
   "MaxResults": number, 
   "MetricTypes": [ "string" ], 
   "NextToken": "string", 
   "ServiceType": "string"
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
Identiﬁer
An immutable identiﬁer for a data source that is unique within an AWS Region. 
Performance Insights gathers metrics from this data source. To use an Amazon RDS DB 
instance as a data source, specify its DbiResourceId value. For example, specify db-
ABCDEFGHIJKLMNOPQRSTU1VWZ.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-]+$
Required: Yes
ListAvailableResourceMetrics API Version 2018-02-27 59
Amazon RDS Performance Insights API Reference
MetricTypes
The types of metrics to return in the response. Valid values in the array include the following:
• os (OS counter metrics) - All engines
• db (DB load metrics) - All engines except for Amazon DocumentDB
• db.sql.stats (per-SQL metrics) - All engines except for Amazon DocumentDB
• db.sql_tokenized.stats (per-SQL digest metrics) - All engines except for Amazon 
DocumentDB
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-_\.:/*)( ]+$
Required: Yes
ServiceType
The AWS service for which Performance Insights returns metrics.
Type: String
Valid Values: RDS | DOCDB
Required: Yes
MaxResults
The maximum number of items to return. If the MaxRecords value is less than the number of 
existing items, the response includes a pagination token.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No
NextToken
An optional pagination token provided by a previous request. If this parameter is speciﬁed, the 
response includes only records beyond the token, up to the value speciﬁed by MaxRecords.
Request Parameters API Version 2018-02-27 60
Amazon RDS Performance Insights API Reference
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: ^[a-zA-Z0-9_=-]+$
Required: No
Response Syntax
{ 
   "Metrics": [  
      {  
         "Description": "string", 
         "Metric": "string", 
         "Unit": "string" 
      } 
   ], 
   "NextToken": "string"
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
Metrics
An array of metrics available to query. Each array element contains the full name, description, 
and unit of the metric.
Type: Array of ResponseResourceMetric objects
NextToken
A pagination token that indicates the response didn’t return all available records because
MaxRecords was speciﬁed in the previous request. To get the remaining records, specify
NextToken in a separate request with this value.
Type: String
Response Syntax API Version 2018-02-27 61
Amazon RDS Performance Insights API Reference
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: ^[a-zA-Z0-9_=-]+$
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
HTTP Status Code: 400
Examples
List speciﬁed metrics
The following example requests the metrics for metric types os and db.
Sample Request
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.ListAvailableResourceMetrics
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Errors API Version 2018-02-27 62
Amazon RDS Performance Insights API Reference
Content-Length: <PayloadSizeBytes>
{ 
    "ServiceType": "RDS", 
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
    "MetricTypes": [ "os", "db" ]
}
Sample Response
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive
{     
    "Metrics": [         
        { 
            "Description": "The number of virtual CPUs for the DB instance", 
            "Metric": "os.general.numVCPUs", 
            "Unit": "vCPUs" 
        }, 
        ......, 
        { 
            "Description": "Time spent reading data file blocks by backends in this 
 instance", 
            "Metric": "db.IO.read_latency", 
            "Unit": "Milliseconds per block" 
        }, 
        ...... 
    ]
}
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS Command Line Interface V2
• AWS SDK for .NET V4
See Also API Version 2018-02-27 63
Amazon RDS Performance Insights API Reference
• AWS SDK for C++
• AWS SDK for Go v2
• AWS SDK for Java V2
• AWS SDK for JavaScript V3
• AWS SDK for Kotlin
• AWS SDK for PHP V3
• AWS SDK for Python
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 64
Amazon RDS Performance Insights API Reference
ListPerformanceAnalysisReports
Lists all the analysis reports created for the DB instance. The reports are sorted based on the start 
time of each report.
Request Syntax
{ 
   "Identifier": "string", 
   "ListTags": boolean, 
   "MaxResults": number, 
   "NextToken": "string", 
   "ServiceType": "string"
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
Identiﬁer
An immutable identiﬁer for a data source that is unique for an AWS Region. Performance 
Insights gathers metrics from this data source. In the console, the identiﬁer is shown 
as ResourceID. When you call DescribeDBInstances, the identiﬁer is returned as
DbiResourceId.
To use a DB instance as a data source, specify its DbiResourceId value. For example, specify
db-ABCDEFGHIJKLMNOPQRSTU1VW2X.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
ListPerformanceAnalysisReports API Version 2018-02-27 65
Amazon RDS Performance Insights API Reference
Pattern: ^[a-zA-Z0-9-]+$
Required: Yes
ServiceType
The AWS service for which Performance Insights returns metrics. Valid value is RDS.
Type: String
Valid Values: RDS | DOCDB
Required: Yes
ListTags
Speciﬁes whether or not to include the list of tags in the response.
Type: Boolean
Required: No
MaxResults
The maximum number of items to return in the response. If more items exist than the speciﬁed
MaxResults value, a pagination token is included in the response so that the remaining results 
can be retrieved.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No
NextToken
An optional pagination token provided by a previous request. If this parameter is speciﬁed, the 
response includes only records beyond the token, up to the value speciﬁed by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: ^[a-zA-Z0-9_=-]+$
Required: No
Request Parameters API Version 2018-02-27 66
Amazon RDS Performance Insights API Reference
Response Syntax
{ 
   "AnalysisReports": [  
      {  
         "AnalysisReportId": "string", 
         "CreateTime": number, 
         "EndTime": number, 
         "StartTime": number, 
         "Status": "string", 
         "Tags": [  
            {  
               "Key": "string", 
               "Value": "string" 
            } 
         ] 
      } 
   ], 
   "NextToken": "string"
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
AnalysisReports
List of reports including the report identiﬁer, start and end time, creation time, and status.
Type: Array of AnalysisReportSummary objects
NextToken
An optional pagination token provided by a previous request. If this parameter is speciﬁed, the 
response includes only records beyond the token, up to the value speciﬁed by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: ^[a-zA-Z0-9_=-]+$
Response Syntax API Version 2018-02-27 67
Amazon RDS Performance Insights API Reference
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
HTTP Status Code: 400
Examples
List of analysis reports for a DB instance
The following example lists all the analysis reports for the DB instance db-
ABC1DEFGHIJKL2MNOPQRSTUV3W along with tags for each report.
Sample Request
                    POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.ListPerformanceAnalysisReports
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Content-Length: <PayloadSizeBytes>
Errors API Version 2018-02-27 68
Amazon RDS Performance Insights API Reference
{ 
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W", 
    "ServiceType": "RDS", 
    "ListTags": true, 
    "MaxResults": 5
} 
                 
Sample Response
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive
{ 
    "AnalysisReports": [ 
        { 
            "AnalysisReportId": "report-01234567890abcdef", 
            "CreateTime": 1690561641.014, 
            "EndTime": 1689356407, 
            "StartTime": 1689161030, 
            "Status": "SUCCEEDED", 
            "Tags": [ 
                { 
                    "Key": "Name", 
                    "Value": "MyName1" 
                } 
            ] 
        }, 
        { 
            "AnalysisReportId": "report-01234567891abcdef", 
            "CreateTime": 1690487582.167, 
            "EndTime": 1689339840, 
            "StartTime": 1689176864, 
            "Status": "SUCCEEDED", 
            "Tags": [ 
                { 
                    "Key": "MyKey", 
                    "Value": "MyValue" 
Examples API Version 2018-02-27 69
Amazon RDS Performance Insights API Reference
                }, 
                { 
                    "Key": "Name", 
                    "Value": "MyName2" 
                } 
            ] 
        }, 
        { 
            "AnalysisReportId": "report-01234567892abcdef", 
            "CreateTime": 1690551889.941, 
            "EndTime": 1689324849, 
            "StartTime": 1689177272, 
            "Status": "SUCCEEDED", 
            "Tags": [ 
                { 
                    "Key": "Name", 
                    "Value": "" 
                } 
            ] 
        } 
    ]
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
See Also API Version 2018-02-27 70
Amazon RDS Performance Insights API Reference
See Also API Version 2018-02-27 71
Amazon RDS Performance Insights API Reference
ListTagsForResource
Retrieves all the metadata tags associated with Amazon RDS Performance Insights resource.
Request Syntax
{ 
   "ResourceARN": "string", 
   "ServiceType": "string"
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
ResourceARN
Lists all the tags for the Amazon RDS Performance Insights resource. This value is an Amazon 
Resource Name (ARN). For information about creating an ARN, see  Constructing an RDS 
Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: ^arn:.*:pi:.*$
Required: Yes
ServiceType
List the tags for the AWS service for which Performance Insights returns metrics. Valid value is
RDS.
ListTagsForResource API Version 2018-02-27 72
Amazon RDS Performance Insights API Reference
Type: String
Valid Values: RDS | DOCDB
Required: Yes
Response Syntax
{ 
   "Tags": [  
      {  
         "Key": "string", 
         "Value": "string" 
      } 
   ]
}
Response Elements
If the action is successful, the service sends back an HTTP 200 response.
The following data is returned in JSON format by the service.
Tags
The metadata assigned to an Amazon RDS resource consisting of a key-value pair.
Type: Array of Tag objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
Response Syntax API Version 2018-02-27 73
Amazon RDS Performance Insights API Reference
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
HTTP Status Code: 400
Examples
List tags for an analysis report
The following example lists all the tags for the report report-01234567890abcdef.
Sample Request
                    POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.ListTagsForResource
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{ 
    "ServiceType": "RDS", 
    "ResourceARN": "arn:aws:pi:us-west-2:123456789012:perf-reports/rds/db-
ABC1DEFGHIJKL2MNOPQRSTUV3W/report-01234567890abcdef"
} 
                 
Sample Response
Examples API Version 2018-02-27 74
Amazon RDS Performance Insights API Reference
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive
{ 
    "Tags": [ 
        { 
            "Key": "MyKey", 
            "Value": "MyValue" 
        }, 
        { 
            "Key": "Name", 
            "Value": "MyName" 
        } 
    ]
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
See Also API Version 2018-02-27 75
Amazon RDS Performance Insights API Reference
TagResource
Adds metadata tags to the Amazon RDS Performance Insights resource.
Request Syntax
{ 
   "ResourceARN": "string", 
   "ServiceType": "string", 
   "Tags": [  
      {  
         "Key": "string", 
         "Value": "string" 
      } 
   ]
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
ResourceARN
The Amazon RDS Performance Insights resource that the tags are added to. This value is an 
Amazon Resource Name (ARN). For information about creating an ARN, see  Constructing an 
RDS Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: ^arn:.*:pi:.*$
Required: Yes
TagResource API Version 2018-02-27 76
Amazon RDS Performance Insights API Reference
ServiceType
The AWS service for which Performance Insights returns metrics. Valid value is RDS.
Type: String
Valid Values: RDS | DOCDB
Required: Yes
Tags
The metadata assigned to an Amazon RDS resource consisting of a key-value pair.
Type: Array of Tag objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes
Response Elements
If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
HTTP Status Code: 400
Response Elements API Version 2018-02-27 77
Amazon RDS Performance Insights API Reference
Examples
Add tag to an analysis report
The following example adds a tag to the report report-01234567890abcdef.
Sample Request
                    POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.TagResource
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{ 
    "ServiceType": "RDS", 
    "ResourceARN": "arn:aws:pi:us-west-2:123456789012:perf-reports/rds/db-
ABC1DEFGHIJKL2MNOPQRSTUV3W/report-01234567890abcdef", 
    "Tags": [{ 
        "Key": "MyKey", 
        "Value": "MyValue" 
    }]
} 
                 
Sample Response
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive 
                 
Examples API Version 2018-02-27 78
Amazon RDS Performance Insights API Reference
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
See Also API Version 2018-02-27 79
Amazon RDS Performance Insights API Reference
UntagResource
Deletes the metadata tags from the Amazon RDS Performance Insights resource.
Request Syntax
{ 
   "ResourceARN": "string", 
   "ServiceType": "string", 
   "TagKeys": [ "string" ]
}
Request Parameters
For information about the parameters that are common to all actions, see Common Parameters.
The request accepts the following data in JSON format.
Note
In the following list, the required parameters are described ﬁrst.
ResourceARN
The Amazon RDS Performance Insights resource that the tags are added to. This value is an 
Amazon Resource Name (ARN). For information about creating an ARN, see  Constructing an 
RDS Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: ^arn:.*:pi:.*$
Required: Yes
ServiceType
List the tags for the AWS service for which Performance Insights returns metrics. Valid value is
RDS.
UntagResource API Version 2018-02-27 80
Amazon RDS Performance Insights API Reference
Type: String
Valid Values: RDS | DOCDB
Required: Yes
TagKeys
The metadata assigned to an Amazon RDS Performance Insights resource consisting of a key-
value pair.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: ^.*$
Required: Yes
Response Elements
If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.
Errors
For information about the errors that are common to all actions, see Common Error Types.
InternalServiceError
The request failed due to an unknown error.
HTTP Status Code: 500
InvalidArgumentException
One of the arguments provided is invalid for this request.
HTTP Status Code: 400
NotAuthorizedException
The user is not authorized to perform this request.
Response Elements API Version 2018-02-27 81
Amazon RDS Performance Insights API Reference
HTTP Status Code: 400
Examples
Delete tag from an analysis report
The following example deletes the tag MyKey from the report report-01234567890abcdef.
Sample Request
                    POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.UntagResource
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, 
 Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{ 
    "ServiceType": "RDS", 
    "ResourceARN": "arn:aws:pi:us-west-2:123456789012:perf-reports/rds/db-
ABC1DEFGHIJKL2MNOPQRSTUV3W/report-01234567890abcdef", 
    "Tags": ["MyKey"]
} 
                 
Sample Response
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive 
                 
Examples API Version 2018-02-27 82
Amazon RDS Performance Insights API Reference
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
See Also API Version 2018-02-27 83
Amazon RDS Performance Insights API Reference
Data Types
The Amazon RDS Performance Insights API contains several data types that various actions use. 
This section describes each data type in detail.
Note
The order of each element in a data type structure is not guaranteed. Applications should 
not assume a particular order.
The following data types are supported:
• AnalysisReport
• AnalysisReportSummary
• Data
• DataPoint
• DimensionDetail
• DimensionGroup
• DimensionGroupDetail
• DimensionKeyDescription
• DimensionKeyDetail
• FeatureMetadata
• Insight
• MetricDimensionGroups
• MetricKeyDataPoints
• MetricQuery
• PerformanceInsightsMetric
• Recommendation
• ResponsePartitionKey
• ResponseResourceMetric
• ResponseResourceMetricKey
• Tag
API Version 2018-02-27 84
Amazon RDS Performance Insights API Reference
API Version 2018-02-27 85
Amazon RDS Performance Insights API Reference
AnalysisReport
Retrieves the summary of the performance analysis report created for a time period.
Contents
Note
In the following list, the required parameters are described ﬁrst.
AnalysisReportId
The name of the analysis report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: report-[0-9a-f]{17}
Required: Yes
CreateTime
The time you created the analysis report.
Type: Timestamp
Required: No
EndTime
The analysis end time in the report.
Type: Timestamp
Required: No
Identiﬁer
The unique identiﬁer of the analysis report.
Type: String
AnalysisReport API Version 2018-02-27 86
Amazon RDS Performance Insights API Reference
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-]+$
Required: No
Insights
The list of identiﬁed insights in the analysis report.
Type: Array of Insight objects
Required: No
ServiceType
List the tags for the AWS service for which Performance Insights returns metrics. Valid values 
are as follows:
• RDS
• DOCDB
Type: String
Valid Values: RDS | DOCDB
Required: No
StartTime
The analysis start time in the report.
Type: Timestamp
Required: No
Status
The status of the created analysis report.
Type: String
Valid Values: RUNNING | SUCCEEDED | FAILED
Required: No
Contents API Version 2018-02-27 87
Amazon RDS Performance Insights API Reference
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 88
Amazon RDS Performance Insights API Reference
AnalysisReportSummary
Retrieves the details of the performance analysis report.
Contents
Note
In the following list, the required parameters are described ﬁrst.
AnalysisReportId
The name of the analysis report.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: No
CreateTime
The time you created the analysis report.
Type: Timestamp
Required: No
EndTime
The end time of the analysis in the report.
Type: Timestamp
Required: No
StartTime
The start time of the analysis in the report.
Type: Timestamp
AnalysisReportSummary API Version 2018-02-27 89
Amazon RDS Performance Insights API Reference
Required: No
Status
The status of the analysis report.
Type: String
Valid Values: RUNNING | SUCCEEDED | FAILED
Required: No
Tags
List of all the tags added to the analysis report.
Type: Array of Tag objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 90
Amazon RDS Performance Insights API Reference
Data
List of data objects which provide details about source metrics. This ﬁeld can be used to determine 
the PI metric to render for the insight. This data type also includes static values for the metrics for 
the Insight that were calculated and included in text and annotations on the DB load chart.
Contents
Note
In the following list, the required parameters are described ﬁrst.
PerformanceInsightsMetric
This ﬁeld determines the Performance Insights metric to render for the insight. The name ﬁeld 
refers to a Performance Insights metric.
Type: PerformanceInsightsMetric object
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
Data API Version 2018-02-27 91
Amazon RDS Performance Insights API Reference
DataPoint
A timestamp, and a single numerical value, which together represent a measurement at a 
particular point in time.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Timestamp
The time, in epoch format, associated with a particular Value.
Type: Timestamp
Required: Yes
Value
The actual value associated with a particular Timestamp.
Type: Double
Required: Yes
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
DataPoint API Version 2018-02-27 92
Amazon RDS Performance Insights API Reference
DimensionDetail
The information about a dimension.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Identiﬁer
The identiﬁer of a dimension.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
DimensionDetail API Version 2018-02-27 93
Amazon RDS Performance Insights API Reference
DimensionGroup
A logical grouping of Performance Insights metrics for a related subject area. For example, the
db.sql dimension group consists of the following dimensions:
• db.sql.id - The hash of a running SQL statement, generated by Performance Insights.
• db.sql.db_id - Either the SQL ID generated by the database engine, or a value generated by 
Performance Insights that begins with pi-.
• db.sql.statement - The full text of the SQL statement that is running, for example, SELECT 
* FROM employees.
• db.sql_tokenized.id - The hash of the SQL digest generated by Performance Insights.
Note
Each response element returns a maximum of 500 bytes. For larger elements, such as SQL 
statements, only the ﬁrst 500 bytes are returned.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Group
The name of the dimension group. Valid values are as follows:
• db - The name of the database to which the client is connected. The following values are 
permitted:
• Aurora PostgreSQL
• Amazon RDS PostgreSQL
• Aurora MySQL
• Amazon RDS MySQL
• Amazon RDS MariaDB
DimensionGroup API Version 2018-02-27 94
Amazon RDS Performance Insights API Reference
• Amazon DocumentDB
• db.application - The name of the application that is connected to the database. The 
following values are permitted:
• Aurora PostgreSQL
• Amazon RDS PostgreSQL
• Amazon DocumentDB
• db.blocking_sql - The SQL queries blocking the most DB load.
• db.blocking_session - The sessions blocking the most DB load.
• db.blocking_object - The object resources acquired by other sessions that are blocking 
the most DB load.
• db.host - The host name of the connected client (all engines).
• db.plans - The execution plans for the query (only Aurora PostgreSQL).
• db.query - The query that is currently running (only Amazon DocumentDB).
• db.query_tokenized - The digest query (only Amazon DocumentDB).
• db.session_type - The type of the current session (only Aurora PostgreSQL and RDS 
PostgreSQL).
• db.sql - The text of the SQL statement that is currently running (all engines except Amazon 
DocumentDB).
• db.sql_tokenized - The SQL digest (all engines except Amazon DocumentDB).
• db.user - The user logged in to the database (all engines except Amazon DocumentDB).
• db.wait_event - The event for which the database backend is waiting (all engines except 
Amazon DocumentDB).
• db.wait_event_type - The type of event for which the database backend is waiting (all 
engines except Amazon DocumentDB).
• db.wait_state - The event for which the database backend is waiting (only Amazon 
DocumentDB).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-_\.:/*)( ]+$
Required: Yes
Contents API Version 2018-02-27 95
Amazon RDS Performance Insights API Reference
Dimensions
A list of speciﬁc dimensions from a dimension group. If this parameter is not present, then it 
signiﬁes that all of the dimensions in the group were requested, or are present in the response.
Valid values for elements in the Dimensions array are:
• db.application.name - The name of the application that is connected to the database. 
Valid values are as follows:
• Aurora PostgreSQL
• Amazon RDS PostgreSQL
• Amazon DocumentDB
• db.blocking_sql.id - The ID for each of the SQL queries blocking the most DB load.
• db.blocking_sql.sql - The SQL text for each of the SQL queries blocking the most DB 
load.
• db.blocking_session.id - The ID for each of the sessions blocking the most DB load.
• db.blocking_object.id - The ID for each of the object resources acquired by other 
sessions that are blocking the most DB load.
• db.blocking_object.type - The object type for each of the object resources acquired by 
other sessions that are blocking the most DB load.
• db.blocking_object.value - The value for each of the object resources acquired by other 
sessions that are blocking the most DB load.
• db.host.id - The host ID of the connected client (all engines).
• db.host.name - The host name of the connected client (all engines).
• db.name - The name of the database to which the client is connected. Valid values are as 
follows:
• Aurora PostgreSQL
• Amazon RDS PostgreSQL
• Aurora MySQL
• Amazon RDS MySQL
• Amazon RDS MariaDB
• Amazon DocumentDB
• db.query.id - The query ID generated by Performance Insights (only Amazon 
DocumentDB).
Contents API Version 2018-02-27 96
Amazon RDS Performance Insights API Reference
• db.query.db_id - The query ID generated by the database (only Amazon DocumentDB).
• db.query.statement - The text of the query that is being run (only Amazon DocumentDB).
• db.query.tokenized_id
• db.query.tokenized.id - The query digest ID generated by Performance Insights (only 
Amazon DocumentDB).
• db.query.tokenized.db_id - The query digest ID generated by Performance Insights 
(only Amazon DocumentDB).
• db.query.tokenized.statement - The text of the query digest (only Amazon 
DocumentDB).
• db.session_type.name - The type of the current session (only Amazon DocumentDB).
• db.sql.id - The hash of the full, non-tokenized SQL statement generated by Performance 
Insights (all engines except Amazon DocumentDB).
• db.sql.db_id - Either the SQL ID generated by the database engine, or a value generated 
by Performance Insights that begins with pi- (all engines except Amazon DocumentDB).
• db.sql.statement - The full text of the SQL statement that is running, as in SELECT * 
FROM employees (all engines except Amazon DocumentDB)
• db.sql.tokenized_id - The hash of the SQL digest generated by Performance Insights 
(all engines except Amazon DocumentDB). The db.sql.tokenized_id dimension 
fetches the value of the db.sql_tokenized.id dimension. Amazon RDS returns
db.sql.tokenized_id from the db.sql dimension group.
• db.sql_tokenized.id - The hash of the SQL digest generated by Performance Insights 
(all engines except Amazon DocumentDB). In the console, db.sql_tokenized.id is called 
the Support ID because AWS Support can look at this data to help you troubleshoot database 
issues.
• db.sql_tokenized.db_id - Either the native database ID used to refer to the SQL 
statement, or a synthetic ID such as pi-2372568224 that Performance Insights generates if 
the native database ID isn't available (all engines except Amazon DocumentDB).
• db.sql_tokenized.statement - The text of the SQL digest, as in SELECT * FROM 
employees WHERE employee_id = ? (all engines except Amazon DocumentDB)
• db.user.id - The ID of the user logged in to the database (all engines except Amazon 
DocumentDB).
• db.user.name - The name of the user logged in to the database (all engines except Amazon 
DocumentDB).
Contents API Version 2018-02-27 97
Amazon RDS Performance Insights API Reference
• db.wait_event.name - The event for which the backend is waiting (all engines except 
Amazon DocumentDB).
• db.wait_event.type - The type of event for which the backend is waiting (all engines 
except Amazon DocumentDB).
• db.wait_event_type.name - The name of the event type for which the backend is waiting 
(all engines except Amazon DocumentDB).
• db.wait_state.name - The event for which the backend is waiting (only Amazon 
DocumentDB).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^[a-zA-Z0-9-_\.:/*)( ]+$
Required: No
Limit
The maximum number of items to fetch for this dimension group.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 98
Amazon RDS Performance Insights API Reference
DimensionGroupDetail
Information about dimensions within a dimension group.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Dimensions
The dimensions within a dimension group.
Type: Array of DimensionDetail objects
Required: No
Group
The name of the dimension group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
DimensionGroupDetail API Version 2018-02-27 99
Amazon RDS Performance Insights API Reference
DimensionKeyDescription
An object that includes the requested dimension key values and aggregated metric values within a 
dimension group.
Contents
Note
In the following list, the required parameters are described ﬁrst.
AdditionalMetrics
A map that contains the value for each additional metric.
Type: String to double map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: .*\S.*
Required: No
Dimensions
A map of name-value pairs for the dimensions in the group.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: .*\S.*
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: .*\S.*
Required: No
Partitions
If PartitionBy was speciﬁed, PartitionKeys contains the dimensions that were.
DimensionKeyDescription API Version 2018-02-27 100
Amazon RDS Performance Insights API Reference
Type: Array of doubles
Required: No
Total
The aggregated metric value for the dimensions, over the requested time range.
Type: Double
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 101
Amazon RDS Performance Insights API Reference
DimensionKeyDetail
An object that describes the details for a speciﬁed dimension.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Dimension
The full name of the dimension. The full name includes the group name and key name. The 
following values are valid:
• db.query.statement (Amazon DocumentDB)
• db.sql.statement (Amazon RDS and Aurora)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: No
Status
The status of the dimension detail data. Possible values include the following:
• AVAILABLE - The dimension detail data is ready to be retrieved.
• PROCESSING - The dimension detail data isn't ready to be retrieved because more processing 
time is required. If the requested detail data has the status PROCESSING, Performance 
Insights returns the truncated query.
• UNAVAILABLE - The dimension detail data could not be collected successfully.
Type: String
Valid Values: AVAILABLE | PROCESSING | UNAVAILABLE
Required: No
DimensionKeyDetail API Version 2018-02-27 102
Amazon RDS Performance Insights API Reference
Value
The value of the dimension detail data. Depending on the return status, this value is either the 
full or truncated SQL query for the following dimensions:
• db.query.statement (Amazon DocumentDB)
• db.sql.statement (Amazon RDS and Aurora)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 103
Amazon RDS Performance Insights API Reference
FeatureMetadata
The metadata for a feature. For example, the metadata might indicate that a feature is turned on 
or oﬀ on a speciﬁc DB instance.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Status
The status of the feature on the DB instance. Possible values include the following:
• ENABLED - The feature is enabled on the instance.
• DISABLED - The feature is disabled on the instance.
• UNSUPPORTED - The feature isn't supported on the instance.
• ENABLED_PENDING_REBOOT - The feature is enabled on the instance but requires a reboot to 
take eﬀect.
• DISABLED_PENDING_REBOOT - The feature is disabled on the instance but requires a reboot 
to take eﬀect.
• UNKNOWN - The feature status couldn't be determined.
Type: String
Valid Values: ENABLED | DISABLED | UNSUPPORTED | ENABLED_PENDING_REBOOT | 
DISABLED_PENDING_REBOOT | UNKNOWN
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
FeatureMetadata API Version 2018-02-27 104
Amazon RDS Performance Insights API Reference
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 105
Amazon RDS Performance Insights API Reference
Insight
Retrieves the list of performance issues which are identiﬁed.
Contents
Note
In the following list, the required parameters are described ﬁrst.
InsightId
The unique identiﬁer for the insight. For example, insight-12345678901234567.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: Yes
BaselineData
Metric names and values from the timeframe used as baseline to generate the insight.
Type: Array of Data objects
Required: No
Context
Indicates if the insight is causal or correlated insight.
Type: String
Valid Values: CAUSAL | CONTEXTUAL
Required: No
Description
Description of the insight. For example: A high severity Insight found between 
02:00 to 02:30, where there was an unusually high DB load 600x above 
baseline. Likely performance impact.
Insight API Version 2018-02-27 106
Amazon RDS Performance Insights API Reference
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8000.
Pattern: (.|\n)*
Required: No
EndTime
The end time of the insight. For example, 2018-10-30T00:00:00Z.
Type: Timestamp
Required: No
InsightData
List of data objects containing metrics and references from the time range while generating the 
insight.
Type: Array of Data objects
Required: No
InsightType
The type of insight. For example, HighDBLoad, HighCPU, or DominatingSQLs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: No
Recommendations
List of recommendations for the insight. For example, Investigate the following SQLs 
that contributed to 100% of the total DBLoad during that time period: 
sql-id.
Type: Array of Recommendation objects
Required: No
Contents API Version 2018-02-27 107
Amazon RDS Performance Insights API Reference
Severity
The severity of the insight. The values are: Low, Medium, or High.
Type: String
Valid Values: LOW | MEDIUM | HIGH
Required: No
StartTime
The start time of the insight. For example, 2018-10-30T00:00:00Z.
Type: Timestamp
Required: No
SupportingInsights
List of supporting insights that provide additional factors for the insight.
Type: Array of Insight objects
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 108
Amazon RDS Performance Insights API Reference
MetricDimensionGroups
The available dimension information for a metric type.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Groups
The available dimension groups for a metric type.
Type: Array of DimensionGroupDetail objects
Required: No
Metric
The metric type to which the dimension information belongs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
MetricDimensionGroups API Version 2018-02-27 109
Amazon RDS Performance Insights API Reference
MetricKeyDataPoints
A time-ordered series of data points, corresponding to a dimension of a Performance Insights 
metric.
Contents
Note
In the following list, the required parameters are described ﬁrst.
DataPoints
An array of timestamp-value pairs, representing measurements over a period of time.
Type: Array of DataPoint objects
Required: No
Key
The dimensions to which the data points apply.
Type: ResponseResourceMetricKey object
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
MetricKeyDataPoints API Version 2018-02-27 110
Amazon RDS Performance Insights API Reference
MetricQuery
A single query to be processed. You must provide the metric to query and append an aggregate 
function to the metric. For example, to ﬁnd the average for the metric db.load you must use
db.load.avg. Valid values for aggregate functions include .avg, .min, .max, and .sum. If no 
other parameters are speciﬁed, Performance Insights returns all data points for the speciﬁed 
metric. Optionally, you can request that the data points be aggregated by dimension group 
(GroupBy), and return only those data points that match your criteria (Filter).
Contents
Note
In the following list, the required parameters are described ﬁrst.
Metric
The name of a Performance Insights metric to be measured.
Valid values for Metric are:
• db.load.avg - A scaled representation of the number of active sessions for the database 
engine.
• db.sampledload.avg - The raw number of active sessions for the database engine.
• The counter metrics listed in Performance Insights operating system counters in the Amazon 
Aurora User Guide.
• The counter metrics listed in Performance Insights operating system counters in the Amazon 
RDS User Guide.
If the number of active sessions is less than an internal Performance Insights threshold,
db.load.avg and db.sampledload.avg are the same value. If the number of active sessions 
is greater than the internal threshold, Performance Insights samples the active sessions, with
db.load.avg showing the scaled values, db.sampledload.avg showing the raw values, 
and db.sampledload.avg less than db.load.avg. For most use cases, you can query
db.load.avg only.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
MetricQuery API Version 2018-02-27 111
Amazon RDS Performance Insights API Reference
Pattern: ^[a-zA-Z0-9-_\.:/*)( ]+$
Required: Yes
Filter
One or more ﬁlters to apply in the request. Restrictions:
• Any number of ﬁlters by the same dimension, as speciﬁed in the GroupBy parameter.
• A single ﬁlter for any other dimension in this dimension group.
Note
The db.sql.db_id ﬁlter isn't available for RDS for SQL Server DB instances.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: ^[a-zA-Z0-9-_\.:/*)( ]+$
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: .*\S.*
Required: No
GroupBy
A speciﬁcation for how to aggregate the data points from a query result. You must specify a 
valid dimension group. Performance Insights will return all of the dimensions within that group, 
unless you provide the names of speciﬁc dimensions within that group. You can also request 
that Performance Insights return a limited number of values for a dimension.
Type: DimensionGroup object
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
See Also API Version 2018-02-27 112
Amazon RDS Performance Insights API Reference
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 113
Amazon RDS Performance Insights API Reference
PerformanceInsightsMetric
This data type helps to determine Performance Insights metric to render for the insight.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Dimensions
A dimension map that contains the dimensions for this partition.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 2000.
Key Pattern: ^.*$
Value Length Constraints: Minimum length of 1. Maximum length of 2000.
Value Pattern: ^.*$
Required: No
DisplayName
The Performance Insights metric name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: ^.*$
Required: No
Filter
The ﬁlter for the Performance Insights metric.
Type: String to string map
PerformanceInsightsMetric API Version 2018-02-27 114
Amazon RDS Performance Insights API Reference
Key Length Constraints: Minimum length of 1. Maximum length of 2000.
Key Pattern: ^.*$
Value Length Constraints: Minimum length of 1. Maximum length of 2000.
Value Pattern: ^.*$
Required: No
Metric
The Performance Insights metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: ^.*$
Required: No
Value
The value of the metric. For example, 9 for db.load.avg.
Type: Double
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 115
Amazon RDS Performance Insights API Reference
Recommendation
The list of recommendations for the insight.
Contents
Note
In the following list, the required parameters are described ﬁrst.
RecommendationDescription
The recommendation details to help resolve the performance issue. For example, Investigate 
the following SQLs that contributed to 100% of the total DBLoad during 
that time period: sql-id
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8000.
Pattern: (.|\n)*
Required: No
RecommendationId
The unique identiﬁer for the recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
Recommendation API Version 2018-02-27 116
Amazon RDS Performance Insights API Reference
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 117
Amazon RDS Performance Insights API Reference
ResponsePartitionKey
If PartitionBy was speciﬁed in a DescribeDimensionKeys request, the dimensions are 
returned in an array. Each element in the array speciﬁes one dimension.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Dimensions
A dimension map that contains the dimensions for this partition.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: .*\S.*
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: .*\S.*
Required: Yes
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
ResponsePartitionKey API Version 2018-02-27 118
Amazon RDS Performance Insights API Reference
ResponseResourceMetric
An object that contains the full name, description, and unit of a metric.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Description
The description of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No
Metric
The full name of the metric.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: No
Unit
The unit of the metric.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: No
ResponseResourceMetric API Version 2018-02-27 119
Amazon RDS Performance Insights API Reference
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 120
Amazon RDS Performance Insights API Reference
ResponseResourceMetricKey
An object describing a Performance Insights metric and one or more dimensions for that metric.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Metric
The name of a Performance Insights metric to be measured.
Valid values for Metric are:
• db.load.avg - A scaled representation of the number of active sessions for the database 
engine.
• db.sampledload.avg - The raw number of active sessions for the database engine.
• The counter metrics listed in Performance Insights operating system counters in the Amazon 
Aurora User Guide.
• The counter metrics listed in Performance Insights operating system counters in the Amazon 
RDS User Guide.
If the number of active sessions is less than an internal Performance Insights threshold,
db.load.avg and db.sampledload.avg are the same value. If the number of active sessions 
is greater than the internal threshold, Performance Insights samples the active sessions, with
db.load.avg showing the scaled values, db.sampledload.avg showing the raw values, 
and db.sampledload.avg less than db.load.avg. For most use cases, you can query
db.load.avg only.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: .*\S.*
Required: Yes
ResponseResourceMetricKey API Version 2018-02-27 121
Amazon RDS Performance Insights API Reference
Dimensions
The valid dimensions for the metric.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: .*\S.*
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: .*\S.*
Required: No
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 122
Amazon RDS Performance Insights API Reference
Tag
Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
Contents
Note
In the following list, the required parameters are described ﬁrst.
Key
A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters 
in length and can't be preﬁxed with aws: or rds:. The string can only contain only the set of 
Unicode letters, digits, white-space, '_', '.', ':', '/', '=', '+', '-', '@' (Java regex: "^([\\p{L}\\p{Z}\
\p{N}_.:/=+\\-@]*)$").
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: ^.*$
Required: Yes
Value
A value is the optional value of the tag. The string value can be from 1 to 256 Unicode 
characters in length and can't be preﬁxed with aws: or rds:. The string can only contain only 
the set of Unicode letters, digits, white-space, '_', '.', ':', '/', '=', '+', '-', '@' (Java regex: "^([\\p{L}\
\p{Z}\\p{N}_.:/=+\\-@]*)$").
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: ^.*$
Required: Yes
Tag API Version 2018-02-27 123
Amazon RDS Performance Insights API Reference
See Also
For more information about using this API in one of the language-speciﬁc AWS SDKs, see the 
following:
• AWS SDK for C++
• AWS SDK for Java V2
• AWS SDK for Ruby V3
See Also API Version 2018-02-27 124
Amazon RDS Performance Insights API Reference
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
API Version 2018-02-27 125
Amazon RDS Performance Insights API Reference
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
API Version 2018-02-27 126
Amazon RDS Performance Insights API Reference
Required: Conditional
API Version 2018-02-27 127
Amazon RDS Performance Insights API Reference
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
API Version 2018-02-27 128
Amazon RDS Performance Insights API Reference
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
API Version 2018-02-27 129
Amazon RDS Performance Insights API Reference
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
API Version 2018-02-27 130
