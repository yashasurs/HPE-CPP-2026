# Command Line Reference

## Welcome

Command Line Reference
Amazon CloudWatch
API Version 2010-08-01
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
## Set up the command line interface

Amazon CloudWatch Command Line Reference
Amazon CloudWatch: Command Line Reference
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
Amazon's trademarks and trade dress may not be used in connection with any product or service 
that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any 
manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are 
the property of their respective owners, who may or may not be aﬃliated with, connected to, or 
sponsored by Amazon.
## Command line interface reference

## mon-cmd

## Description

Amazon CloudWatch Command Line Reference
Table of Contents
Welcome ........................................................................................................................................... 1
Set up the command line interface ............................................................................................... 2
Command line interface reference ................................................................................................. 3
mon-cmd ........................................................................................................................................................ 3
Description ................................................................................................................................................ 3
Syntax ........................................................................................................................................................ 4
Output ....................................................................................................................................................... 4
Examples ................................................................................................................................................... 4
Related Topics .......................................................................................................................................... 5
mon-delete-alarms ....................................................................................................................................... 5
Description ................................................................................................................................................ 5
Syntax ........................................................................................................................................................ 5
Options ...................................................................................................................................................... 5
Common options ..................................................................................................................................... 6
Output ..................................................................................................................................................... 11
Examples ................................................................................................................................................. 11
Related topics ........................................................................................................................................ 11
mon-describe-alarm-history .................................................................................................................... 12
Description .............................................................................................................................................. 12
Syntax ...................................................................................................................................................... 12
Options .................................................................................................................................................... 12
Common options .................................................................................................................................. 13
Output ..................................................................................................................................................... 18
Examples ................................................................................................................................................. 19
Related topics ........................................................................................................................................ 19
mon-describe-alarms ................................................................................................................................. 20
Description .............................................................................................................................................. 20
Syntax ...................................................................................................................................................... 20
Options .................................................................................................................................................... 20
Common options .................................................................................................................................. 21
Output ..................................................................................................................................................... 26
Examples ................................................................................................................................................. 27
Related topics ........................................................................................................................................ 28
mon-describe-alarms-for-metric ............................................................................................................. 28
API Version 2010-08-01 iii
## Syntax

## Output

## Examples

Amazon CloudWatch Command Line Reference
Description .............................................................................................................................................. 28
Syntax ...................................................................................................................................................... 28
Options .................................................................................................................................................... 29
Common options .................................................................................................................................. 33
Output ..................................................................................................................................................... 38
Examples ................................................................................................................................................. 39
Related topics ........................................................................................................................................ 39
mon-disable-alarm-actions ...................................................................................................................... 39
Description .............................................................................................................................................. 39
Syntax ...................................................................................................................................................... 40
Options .................................................................................................................................................... 40
Common options .................................................................................................................................. 40
Output ..................................................................................................................................................... 45
Examples ................................................................................................................................................. 46
Related topics ........................................................................................................................................ 46
mon-enable-alarm-actions ....................................................................................................................... 46
Description .............................................................................................................................................. 46
Syntax ...................................................................................................................................................... 46
Options .................................................................................................................................................... 47
Common options .................................................................................................................................. 47
Output ..................................................................................................................................................... 52
Examples ................................................................................................................................................. 52
Related topics ........................................................................................................................................ 52
mon-get-stats .............................................................................................................................................. 52
Description .............................................................................................................................................. 52
Syntax ...................................................................................................................................................... 53
Options .................................................................................................................................................... 53
Common options .................................................................................................................................. 58
Output ..................................................................................................................................................... 63
Examples ................................................................................................................................................. 63
Related topics ........................................................................................................................................ 64
mon-list-metrics ......................................................................................................................................... 65
Description .............................................................................................................................................. 65
Syntax ...................................................................................................................................................... 65
Options .................................................................................................................................................... 65
Common options .................................................................................................................................. 67
API Version 2010-08-01 iv
## Related Topics

## mon-delete-alarms

## Description

## Syntax

## Options

Amazon CloudWatch Command Line Reference
Output ..................................................................................................................................................... 72
Examples ................................................................................................................................................. 72
Related topics ........................................................................................................................................ 73
mon-put-data .............................................................................................................................................. 73
Description .............................................................................................................................................. 73
Syntax ...................................................................................................................................................... 74
Options .................................................................................................................................................... 74
Common options .................................................................................................................................. 78
Output ..................................................................................................................................................... 83
Examples ................................................................................................................................................. 84
Related topics ........................................................................................................................................ 84
mon-put-metric-alarm .............................................................................................................................. 85
Description .............................................................................................................................................. 85
Syntax ...................................................................................................................................................... 85
Options .................................................................................................................................................... 85
Common options .................................................................................................................................. 94
Output ..................................................................................................................................................... 99
Examples ............................................................................................................................................... 100
Related topics ...................................................................................................................................... 100
mon-set-alarm-state ............................................................................................................................... 100
Description ........................................................................................................................................... 100
Syntax .................................................................................................................................................... 101
Options ................................................................................................................................................. 101
Common options ................................................................................................................................ 102
Output ................................................................................................................................................... 107
Examples ............................................................................................................................................... 107
Related topics ...................................................................................................................................... 107
mon-version .............................................................................................................................................. 107
Description ........................................................................................................................................... 107
Syntax .................................................................................................................................................... 107
Output ................................................................................................................................................... 108
Examples ............................................................................................................................................... 108
Related topics ...................................................................................................................................... 108
Document history ........................................................................................................................ 109
API Version 2010-08-01 v
## Common options

Amazon CloudWatch Command Line Reference
Welcome
As of November 7, 2017, we are no longer supporting the CloudWatch command line interface 
with new functionality. It is not available for download. The CloudWatch CLI reference 
documentation is still available.
We encourage customers to use the AWS Command Line Interface. The AWS CLI includes all 
existing and new CloudWatch commands, and is the only command line interface being updated. 
For information about installing the AWS CLI, see Installing the AWS Command Line Interface. For 
information about CloudWatch commands in the AWS CLI, see cloudwatch.
API Version 2010-08-01 1
Amazon CloudWatch Command Line Reference
Set up the command line interface
As of November 7, 2017, we are no longer supporting the CloudWatch command line interface 
with new functionality. It is not available for download. The CloudWatch CLI reference 
documentation is still available.
We encourage customers to use the AWS Command Line Interface. The AWS CLI includes all 
existing and new CloudWatch commands, and is the only command line interface being updated. 
For information about installing the AWS CLI, see Installing the AWS Command Line Interface. For 
information about CloudWatch commands in the AWS CLI, see cloudwatch.
API Version 2010-08-01 2
Amazon CloudWatch Command Line Reference
Amazon CloudWatch command line interface reference
AWS provides two sets of command line tools that each support CloudWatch. This section 
describes the CloudWatch command line interface (CLI).
As of November 7, 2017, we are no longer supporting this CloudWatch command line interface 
with new functionality and it is no longer available for download. We encourage customers to 
use the AWS Command Line Interface to control and automate CloudWatch on Windows, Mac, 
and Linux. We also oﬀer the AWS Tools for Windows PowerShell if you prefer to script in the 
PowerShell environment.
Commands
• mon-cmd
• mon-delete-alarms
• mon-describe-alarm-history
• mon-describe-alarms
• mon-describe-alarms-for-metric
• mon-disable-alarm-actions
• mon-enable-alarm-actions
• mon-get-stats
• mon-list-metrics
• mon-put-data
• mon-put-metric-alarm
• mon-set-alarm-state
• mon-version
mon-cmd
Description
Lists all the other CloudWatch commands. For help on a speciﬁc command, use the following 
command:
commandname --help
mon-cmd API Version 2010-08-01 3
Amazon CloudWatch Command Line Reference
Syntax
mon-cmd
Output
This command lists all of the Amazon CloudWatch commands in a table.
The Amazon CloudWatch CLI displays errors on stderr.
Examples
Example Request
This example lists all of the Amazon CloudWatch commands.
mon-cmd 
Command Name                       Description                                          
    
------------                       -----------                                          
    
help                                
mon-delete-alarms                  Delete alarms.                                       
     
mon-describe-alarm-history         Show the history of alarm transitions and actions 
 taken.                                  
mon-describe-alarms                List alarms and show detailed alarm configuration.   
                                
mon-describe-alarms-for-metric     Show alarms for a given metric.    
mon-disable-alarm-actions          Disable all actions for a given alarm.               
     
mon-enable-alarm-actions           Enable all actions for a given alarm.                
     
mon-get-stats                      Get metric statistics.                               
     
mon-list-metrics                   List user's metrics.   
mon-put-data                       Put metric data.
mon-put-metric-alarm               Create a new alarm or update an existing one.        
     
mon-set-alarm-state                Manually set the state of an alarm.                  
     
mon-version                        Prints the version of the CLI tool and API.
Syntax API Version 2010-08-01 4
Amazon CloudWatch Command Line Reference
For help on a specific command, type '<commandname> --help'
Related Topics
Download
• Set up the command line interface
Related Command
• mon-version Command
mon-delete-alarms
Description
Deletes the speciﬁed alarms.
Syntax
mon-delete-alarms [AlarmNames [AlarmNames ...]] [Common Options]
Options
Name Description
AlarmNames  AlarmNames The names of the alarms to delete, separated by a 
space. You can also set this value using --alarm-n 
ame .
Type: Argument
Valid values: The name of the alarm, which must 
between 1 and 255 characters in length.
Default: n/a
Required: Yes
Related Topics API Version 2010-08-01 5
## Output

## Examples

## Related topics

Amazon CloudWatch Command Line Reference
Name Description
-f, --force Deletes the alarms without prompting you for 
conﬁrmation. By default, the mon-delete-alarms
command prompts you for conﬁrmation before 
deleting alarms.
Type: Flag
Valid values: n/a
Default: You are prompted before deleting each alarm.
Required: No
Common options
Name Description
--aws-credential-file  VALUE The location of the ﬁle with your AWS credentia 
ls. You can set this value using the environment 
variable AWS_CREDENTIAL_FILE . If you deﬁne the 
environment variable or you provide the path to the 
credential ﬁle, the ﬁle must exist or the request fails. 
All CloudWatch requests must be signed using your 
access key ID and secret access key.
Type: String
Valid values: A valid path to a ﬁle containing your 
access key ID and secret access key.
Default: Uses the environment variable AWS_CREDE 
NTIAL_FILE , if set.
-C, --ec2-cert-file-path
VALUE
The location of your EC2 certiﬁcate ﬁle for signing 
requests. You can use the environment variable
EC2_CERT to specify this value.
Common options API Version 2010-08-01 6
## mon-describe-alarm-history

## Description

## Syntax

## Options

Amazon CloudWatch Command Line Reference
Name Description
Type: String
Valid values: A valid ﬁle path to the PEM ﬁle 
provided by Amazon EC2 or AWS Identity and Access 
Management.
Default: Uses the environment variable EC2_CERT, if 
set.
--connection-timeout  VALUE The connection timeout value, in seconds.
Type: Integer
Valid values: Any positive number.
Default: 30
--delimiter  VALUE The delimiter to use when displaying delimited (long) 
results.
Type: String
Valid values: Any string.
Default: Comma (,)
--headers If you are displaying tabular or delimited results, 
include the column headers. If you are showing XML 
results, return the HTTP headers from the service 
request, if applicable.
Type: Flag
Valid values: When present, shows headers.
Default: The --headers  option is oﬀ by default.
Common options API Version 2010-08-01 7
## Common options

Amazon CloudWatch Command Line Reference
Name Description
-I, --access-key-id  VALUE The access key ID that will be used, in conjunction with 
the secret key, to sign the request. This must be used 
in conjunction with --secret-key, otherwise the option 
is ignored. All requests to CloudWatch must be signed, 
otherwise the request is rejected.
Type: String
Valid values: A valid access key ID.
Default: None
-K, --ec2-private-key-file-
path  VALUE
The private key that will be used to sign the request. 
Using public/private keys causes the CLI to use SOAP. 
The request is signed with a public certiﬁcate and 
private key. This parameter must be used in conjuncti 
on with EC2_CERT, otherwise the value is ignored. 
The value of the environment variable EC2_PRIVA 
TE_KEY  will be used if it is set, and this option is 
not speciﬁed. This option is ignored if the environme 
nt variable AWS_CREDENTIAL_FILE  is set, or --
aws-credentials-file  is used. All requests to 
CloudWatch must be signed, otherwise the request is 
rejected.
Type: String
Valid values: The path to a valid ASN.1 private key.
Default: None
Common options API Version 2010-08-01 8
Amazon CloudWatch Command Line Reference
Name Description
--region VALUE The region requests are directed to. You can use the 
environment variable EC2_REGION  to specify the 
value. The region is used to create the URL used to 
call CloudWatch, and must be a valid Amazon Web 
Services (AWS) region.
Type: String
Valid values: Any AWS region, for example, us-east-1.
Default: us-east-1, unless the EC2_REGION
environment variable is set.
S, --secret-key  VALUE The secret access key that will be used to sign the 
request, in conjunction with an access key ID. This 
parameter must be used in conjunction with --
access-key-id , otherwise this option is ignored.
Type: String
Valid values: Your access key ID.
Default: None
--show-empty-fields Shows empty ﬁelds using (nil) as a placeholder to 
indicate that this data was not requested.
Type: Flag
Valid values: None
Default: Empty ﬁelds are not shown by default.
Common options API Version 2010-08-01 9
Amazon CloudWatch Command Line Reference
Name Description
--show-request Displays the URL the CLI uses to call AWS.
Type: Flag
Valid values: None
Default: false
--show-table, --show-long, 
--show-xml, --quiet
Speciﬁes how the results are displayed: in a table, 
delimited (long), XML, or no output (quiet). The --
show-table  display shows a subset of the data in 
ﬁxed column-width form; --show-long  shows all 
of the returned values delimited by a character; --
show-xml  is the raw return from the service; and --
quiet suppresses all standard output. All options are 
mutually exclusive, with the priority --show-table ,
--show-long , --show-xml , and --quiet.
Type: Flag
Valid values: None
Default: --show-table
-U, --url VALUE The URL used to contact CloudWatch. You can set 
this value using the environment variable AWS_CLOUD 
WATCH_URL . This value is used in conjunction with
--region to create the expected URL. This option 
overrides the URL for the service call.
Type: String
Valid values: A valid HTTP or HTTPS URL.
Default: Uses the value speciﬁed in AWS_CLOUD 
WATCH_URL , if set.
Common options API Version 2010-08-01 10
Amazon CloudWatch Command Line Reference
Output
This command deletes an alarm.
The Amazon CloudWatch CLI displays errors on stderr.
Examples
Example request
This example deletes the alarm named my-alarm.
mon-delete-alarms --alarm-name my-alarm 
Example request
This example deletes multiple alarms.
mon-delete-alarms --alarm-name my-alarm1 my-alarm2 my-alarm3 
Related topics
Download
• Set up the command line interface
Related action
• DeleteAlarms
Related commands
• mon-put-metric-alarm
• mon-disable-alarm-actions
• mon-enable-alarm-actions
Output API Version 2010-08-01 11
Amazon CloudWatch Command Line Reference
mon-describe-alarm-history
Description
Retrieves the history for the speciﬁed alarm. You can ﬁlter alarms by date range or item type. If 
you don't specify an alarm name, Amazon CloudWatch returns histories for all of your alarms.
Note
Amazon CloudWatch retains the history of active and deleted alarms for two weeks.
Syntax
mon-describe-alarm-history [AlarmNames [AlarmNames ...]] [--end-date value] 
[--history-item-type value] [--start-date value] [Common Options]
Options
Name Description
AlarmName  AlarmNames The names of the alarms, separated by spaces. If you 
don't specify an alarm name, this command returns 
the histories of all your alarms. You can also set this 
value using --alarm-name .
Type: Argument
Valid values: Any string between 1 and 255 characters 
in length.
Default: n/a
Required: No
--end-date  VALUE The end of the date range for history.
Type: Date
Valid values: Date in YYYY-MM-DD format.
mon-describe-alarm-history API Version 2010-08-01 12
## Output

Amazon CloudWatch Command Line Reference
Name Description
Default: The current date.
Required: No
--history-item-type  VALUE The type of history items to retrieve. By default, all 
types are returned.
Type: Enumeration
Valid values: ConﬁgurationUpdate, StateUpdate, or 
Action
Default: All types are returned.
Required: No
--start-date  VALUE The start of the date range for history. By default it 
extends to all available history.
Type: Date
Valid values: Date in YYYY-MM-DD format.
Default: All available history.
Required: No
Common options
Name Description
--aws-credential-file  VALUE The location of the ﬁle with your AWS credentia 
ls. You can set this value using the environment 
variable AWS_CREDENTIAL_FILE . If you deﬁne the 
environment variable or you provide the path to the 
credential ﬁle, the ﬁle must exist or the request fails. 
All CloudWatch requests must be signed using your 
access key ID and secret access key.
Common options API Version 2010-08-01 13
## Examples

## Related topics

Amazon CloudWatch Command Line Reference
Name Description
Type: String
Valid values: A valid path to a ﬁle containing your 
access key ID and secret access key.
Default: Uses the environment variable AWS_CREDE 
NTIAL_FILE , if set.
-C, --ec2-cert-file-path
VALUE
The location of your EC2 certiﬁcate ﬁle for signing 
requests. You can use the environment variable
EC2_CERT to specify this value.
Type: String
Valid values: A valid ﬁle path to the PEM ﬁle 
provided by Amazon EC2 or AWS Identity and Access 
Management.
Default: Uses the environment variable EC2_CERT, if 
set.
--connection-timeout  VALUE The connection timeout value, in seconds.
Type: Integer
Valid values: Any positive number.
Default: 30
--delimiter  VALUE The delimiter to use when displaying delimited (long) 
results.
Type: String
Valid values: Any string.
Default: Comma (,)
Common options API Version 2010-08-01 14
## mon-describe-alarms

## Description

## Syntax

## Options

Amazon CloudWatch Command Line Reference
Name Description
--headers If you are displaying tabular or delimited results, 
include the column headers. If you are showing XML 
results, return the HTTP headers from the service 
request, if applicable.
Type: Flag
Valid values: When present, shows headers.
Default: The --headers  option is oﬀ by default.
-I, --access-key-id  VALUE The access key ID that will be used, in conjunction with 
the secret key, to sign the request. This must be used 
in conjunction with --secret-key, otherwise the option 
is ignored. All requests to CloudWatch must be signed, 
otherwise the request is rejected.
Type: String
Valid values: A valid access key ID.
Default: None
Common options API Version 2010-08-01 15
## Common options

Amazon CloudWatch Command Line Reference
Name Description
-K, --ec2-private-key-file-
path  VALUE
The private key that will be used to sign the request. 
Using public/private keys causes the CLI to use SOAP. 
The request is signed with a public certiﬁcate and 
private key. This parameter must be used in conjuncti 
on with EC2_CERT, otherwise the value is ignored. 
The value of the environment variable EC2_PRIVA 
TE_KEY  will be used if it is set, and this option is 
not speciﬁed. This option is ignored if the environme 
nt variable AWS_CREDENTIAL_FILE  is set, or --
aws-credentials-file  is used. All requests to 
CloudWatch must be signed, otherwise the request is 
rejected.
Type: String
Valid values: The path to a valid ASN.1 private key.
Default: None
--region VALUE The region requests are directed to. You can use the 
environment variable EC2_REGION  to specify the 
value. The region is used to create the URL used to 
call CloudWatch, and must be a valid Amazon Web 
Services (AWS) region.
Type: String
Valid values: Any AWS region, for example, us-east-1.
Default: us-east-1, unless the EC2_REGION
environment variable is set.
Common options API Version 2010-08-01 16
Amazon CloudWatch Command Line Reference
Name Description
S, --secret-key  VALUE The secret access key that will be used to sign the 
request, in conjunction with an access key ID. This 
parameter must be used in conjunction with --
access-key-id , otherwise this option is ignored.
Type: String
Valid values: Your access key ID.
Default: None
--show-empty-fields Shows empty ﬁelds using (nil) as a placeholder to 
indicate that this data was not requested.
Type: Flag
Valid values: None
Default: Empty ﬁelds are not shown by default.
--show-request Displays the URL the CLI uses to call AWS.
Type: Flag
Valid values: None
Default: false
Common options API Version 2010-08-01 17
Amazon CloudWatch Command Line Reference
Name Description
--show-table, --show-long, 
--show-xml, --quiet
Speciﬁes how the results are displayed: in a table, 
delimited (long), XML, or no output (quiet). The --
show-table  display shows a subset of the data in 
ﬁxed column-width form; --show-long  shows all 
of the returned values delimited by a character; --
show-xml  is the raw return from the service; and --
quiet suppresses all standard output. All options are 
mutually exclusive, with the priority --show-table ,
--show-long , --show-xml , and --quiet.
Type: Flag
Valid values: None
Default: --show-table
-U, --url VALUE The URL used to contact CloudWatch. You can set 
this value using the environment variable AWS_CLOUD 
WATCH_URL . This value is used in conjunction with
--region to create the expected URL. This option 
overrides the URL for the service call.
Type: String
Valid values: A valid HTTP or HTTPS URL.
Default: Uses the value speciﬁed in AWS_CLOUD 
WATCH_URL , if set.
Output
This command returns a table that contains the following:
• ALARM - The alarm name.
• TIMESTAMP - The timestamp.
• TYPE - The type of event, one of ConﬁgurationUpdate, StateUpdate and Action.
Output API Version 2010-08-01 18
Amazon CloudWatch Command Line Reference
• SUMMARY - A human-readable summary of history event.
• DATA - Detailed data about the event in machine-readable JSON format. This column appears 
only in the --show-long view.
The Amazon CloudWatch CLI displays errors on stderr.
Examples
Example request
This example describes all history items for the alarm my-alarm.
mon-describe-alarm-history--alarm-name my-alarm --headers
This is an example output of this command.
ALARM     TIMESTAMP                 TYPE                 SUMMARY
my-alarm  2013-05-07T18:46:16.121Z  Action               Published a notification to 
 arn:aws:sns:...
my-alarm  2013-05-07T18:46:16.118Z  StateUpdate          Alarm updated from 
 INSUFFICIENT_DATA to OK
my-alarm  2013-05-07T18:46:07.362Z  ConfigurationUpdate  Alarm "my-alarm" created
Related topics
Download
• Set up the command line interface
Related action
• DescribeAlarmHistory
Related commands
• mon-describe-alarms
• mon-describe-alarms-for-metric
Examples API Version 2010-08-01 19
Amazon CloudWatch Command Line Reference
mon-describe-alarms
Description
Gets information on the speciﬁed alarms. If you don't specify an alarm name, this command 
returns information about all of your alarms. You can retrieve alarms by using only the alarm name 
preﬁx, the alarm state, or an action preﬁx.
Syntax
mon-describe-alarms [AlarmNames [AlarmNames ...]] [--action-prefix value] 
[--alarm-name-prefix value] [--state-value value] [Common Options]
Options
Name Description
AlarmNames  AlarmNames The names of the alarms. You can also set this value 
using --alarm-name . You can specify this option 
multiple times.
Type: Argument
Valid values: An existing alarm name, otherwise no 
response is returned.
Default: n/a, displays all alarms by default.
Required: No
--action-prefix  VALUE Preﬁx of action names.
Type: Argument
Valid values: The preﬁx of an existing action name, in 
ARN format.
Default: n/a, display the ﬁrst action by default.
Required: No
mon-describe-alarms API Version 2010-08-01 20
## Output

Amazon CloudWatch Command Line Reference
Name Description
--alarm-name-prefix  VALUE Preﬁx of alarm names.
Type: Argument
Valid values: The preﬁx of an existing alarm name.
Default: n/a
Required: No
--state-value  VALUE The state of the alarm.
Type: Enumeration
Valid values: OK, ALARM, or INSUFFICIENT_DATA
Default: All alarm states.
Required: No
Common options
Name Description
--aws-credential-file  VALUE The location of the ﬁle with your AWS credentia 
ls. You can set this value using the environment 
variable AWS_CREDENTIAL_FILE . If you deﬁne the 
environment variable or you provide the path to the 
credential ﬁle, the ﬁle must exist or the request fails. 
All CloudWatch requests must be signed using your 
access key ID and secret access key.
Type: String
Valid values: A valid path to a ﬁle containing your 
access key ID and secret access key.
Common options API Version 2010-08-01 21
## Examples

Amazon CloudWatch Command Line Reference
Name Description
Default: Uses the environment variable AWS_CREDE 
NTIAL_FILE , if set.
-C, --ec2-cert-file-path
VALUE
The location of your EC2 certiﬁcate ﬁle for signing 
requests. You can use the environment variable
EC2_CERT to specify this value.
Type: String
Valid values: A valid ﬁle path to the PEM ﬁle 
provided by Amazon EC2 or AWS Identity and Access 
Management.
Default: Uses the environment variable EC2_CERT, if 
set.
--connection-timeout  VALUE The connection timeout value, in seconds.
Type: Integer
Valid values: Any positive number.
Default: 30
--delimiter  VALUE The delimiter to use when displaying delimited (long) 
results.
Type: String
Valid values: Any string.
Default: Comma (,)
Common options API Version 2010-08-01 22
## Related topics

## mon-describe-alarms-for-metric

Amazon CloudWatch Command Line Reference
Name Description
--headers If you are displaying tabular or delimited results, 
include the column headers. If you are showing XML 
results, return the HTTP headers from the service 
request, if applicable.
Type: Flag
Valid values: When present, shows headers.
Default: The --headers  option is oﬀ by default.
-I, --access-key-id  VALUE The access key ID that will be used, in conjunction with 
the secret key, to sign the request. This must be used 
in conjunction with --secret-key, otherwise the option 
is ignored. All requests to CloudWatch must be signed, 
otherwise the request is rejected.
Type: String
Valid values: A valid access key ID.
Default: None
Common options API Version 2010-08-01 23
Amazon CloudWatch Command Line Reference
Name Description
-K, --ec2-private-key-file-
path  VALUE
The private key that will be used to sign the request. 
Using public/private keys causes the CLI to use SOAP. 
The request is signed with a public certiﬁcate and 
private key. This parameter must be used in conjuncti 
on with EC2_CERT, otherwise the value is ignored. 
The value of the environment variable EC2_PRIVA 
TE_KEY  will be used if it is set, and this option is 
not speciﬁed. This option is ignored if the environme 
nt variable AWS_CREDENTIAL_FILE  is set, or --
aws-credentials-file  is used. All requests to 
CloudWatch must be signed, otherwise the request is 
rejected.
Type: String
Valid values: The path to a valid ASN.1 private key.
Default: None
--region VALUE The region requests are directed to. You can use the 
environment variable EC2_REGION  to specify the 
value. The region is used to create the URL used to 
call CloudWatch, and must be a valid Amazon Web 
Services (AWS) region.
Type: String
Valid values: Any AWS region, for example, us-east-1.
Default: us-east-1, unless the EC2_REGION
environment variable is set.
Common options API Version 2010-08-01 24
Amazon CloudWatch Command Line Reference
Name Description
S, --secret-key  VALUE The secret access key that will be used to sign the 
request, in conjunction with an access key ID. This 
parameter must be used in conjunction with --
access-key-id , otherwise this option is ignored.
Type: String
Valid values: Your access key ID.
Default: None
--show-empty-fields Shows empty ﬁelds using (nil) as a placeholder to 
indicate that this data was not requested.
Type: Flag
Valid values: None
Default: Empty ﬁelds are not shown by default.
--show-request Displays the URL the CLI uses to call AWS.
Type: Flag
Valid values: None
Default: false
Common options API Version 2010-08-01 25
Amazon CloudWatch Command Line Reference
Name Description
--show-table, --show-long, 
--show-xml, --quiet
Speciﬁes how the results are displayed: in a table, 
delimited (long), XML, or no output (quiet). The --
show-table  display shows a subset of the data in 
ﬁxed column-width form; --show-long  shows all 
of the returned values delimited by a character; --
show-xml  is the raw return from the service; and --
quiet suppresses all standard output. All options are 
mutually exclusive, with the priority --show-table ,
--show-long , --show-xml , and --quiet.
Type: Flag
Valid values: None
Default: --show-table
-U, --url VALUE The URL used to contact CloudWatch. You can set 
this value using the environment variable AWS_CLOUD 
WATCH_URL . This value is used in conjunction with
--region to create the expected URL. This option 
overrides the URL for the service call.
Type: String
Valid values: A valid HTTP or HTTPS URL.
Default: Uses the value speciﬁed in AWS_CLOUD 
WATCH_URL , if set.
Output
This command returns a table that contains the following:
• ALARM - Alarm name.
• DESCRIPTION - The alarm description. This column appears only in the --show-long view.
• STATE - The alarm state.
Output API Version 2010-08-01 26
Amazon CloudWatch Command Line Reference
• STATE_REASON - A human-readable reason for state. This column appears only in the --show-
long view.
• STATE_REASON_DATA - A machine-readable reason for state (JSON format). This column 
appears only in the --show-long view.
• ENABLED - Enables or disables actions. This column appears only in the --show-long view.
• OK_ACTIONS - The action to execute on OK status. This column appears only in the --show-long 
view.
• ALARM_ACTIONS - The action to execute on ALARM status.
• INSUFFICIENT_DATA_ACTIONS - The action to execute on INSUFFICIENT_DATA status. This 
column appears only in the --show-long view.
• NAMESPACE - A namespace for the metric.
• METRIC_NAME - The name of the metric.
• DIMENSIONS - The metric dimensions. This column appears only in the --show-long view.
• PERIOD - The period.
• STATISTIC - The statistic (Average, Minimum, Maximum, Sum, SampleCount).
• EXTENDEDSTATISTIC - The percentile statistic.
• UNIT - The unit. This column appears only in the --show-long view.
• EVAL_PERIODS - The number of periods to evaluate the metric.
• COMPARISON - The comparison operator.
• THRESHOLD - The threshold.
The Amazon CloudWatch CLI displays errors on stderr.
Examples
Example request
This example describes all of your alarms whose name starts with my-alarm.
mon-describe-alarms --alarm-name-prefix my-alarm --headers
This is an example output of this command.
Examples API Version 2010-08-01 27
Amazon CloudWatch Command Line Reference
ALARM      STATE ALARM_ACTIONS  NAMESPACE  METRIC_NAME    PERIOD  STATISTIC  
 EVAL_PERIODS  COMPARISON            THRESHOLD
my-alarm1  OK    arn:aws:sns:.. AWS/EC2    CPUUtilization 60      Average    3          
    GreaterThanThreshold  100.0
my-alarm2  OK    arn:aws:sns:.. AWS/EC2    CPUUtilization 60      Average    5          
    
GreaterThanThreshold  80o.0
Related topics
Download
• Set up the command line interface
Related action
• DescribeAlarms
Related commands
• mon-describe-alarm-history
• mon-describe-alarms-for-metric
mon-describe-alarms-for-metric
Description
Gets information about the alarms associated with the speciﬁed metric.
Syntax
mon-describe-alarms-for-metric --metric-name value --namespace value [--
dimensions "key1=value1,key2=value2..."] [--period value] [--statistic
value] [--extendedstatistic value] [--unit value] [Common Options]
Related topics API Version 2010-08-01 28
Amazon CloudWatch Command Line Reference
Options
Name Description
--dimensions  - "key1=val 
ue1,key2=value2...
The dimensions associated with the metric. You can 
specify dimensions two ways and the formats can be 
combined or used interchangeably:
• One option per dimension: --dimensions "key1=val 
ue1" --dimensions "key2=value2"
• All in one option: --dimensions "key1=value1,key2= 
value2"
Type: Map
Valid values: A string of the format name=value, where 
the key is the name of the dimension, and the value 
is the dimension's value. The dimension names, and 
values must be an ANSI string between 1 and 250 
characters long. A maximum of 10 dimensions are 
allowed.
Default: n/a
Required: No
--metric-name  VALUE The name of the metric whose associated alarms you 
want to search for.
Type: Argument
Valid values: A valid metric name between 1 and 255 
characters in length.
Default: n/a
Required: Yes
Options API Version 2010-08-01 29
Amazon CloudWatch Command Line Reference
Name Description
--namespace  VALUE The namespace of the metric associated with the 
alarm. For more information about namespaces, see
AWS Namespaces.
Type: String
Valid values: A valid namespace between 1 and 250 
characters in length.
Default: n/a
Required: Yes
--period VALUE The period to ﬁlter the alarms by. Only alarms that 
evaluate metrics at this period will be included in the 
results. If this isn't speciﬁed alarms on any period will 
be included .
Type: Argument
Valid values: A number, in seconds that is a multiple of 
60 seconds.
Default: n/a
Required: No
--statistic  VALUE The statistic to ﬁlter alarms by. Only alarms on the 
speciﬁed statistic will be included. If this parameter 
isn't speciﬁed, alarms on any statistic are included.
Type: Enumeration
Valid values: SampleCount, Average, Sum, Minimum or 
Maximum
Default: n/a
Required: No
Options API Version 2010-08-01 30
Amazon CloudWatch Command Line Reference
Name Description
--extendedstatistic  VALUE The percentile statistic to ﬁlter alarms by. Only alarms 
on the speciﬁed statistic are included. If this parameter 
isn't speciﬁed, alarms on any statistic are included.
Type: String
Valid values: Any percentile, with up to two decimal 
places (for example, p95.45).
Default: n/a
Required: No
Options API Version 2010-08-01 31
Amazon CloudWatch Command Line Reference
Name Description
--unit VALUE The unit to ﬁlter the alarms by. Only alarms on the 
speciﬁed statistics will be included. If this isn't speciﬁed 
than alarms on any units will be included. If the alarm 
doesn't have a unit speciﬁed than the only way to 
search for the alarm is to omit this option.
Type: Enumeration
Valid values: One of the following:
• Seconds
• Microseconds
• Milliseconds
• Bytes
• Kilobytes
• Megabytes
• Gigabytes
• Terabytes
• Bits
• Kilobits
• Megabits
• Gigabits
• Terabits
• Percent
• Count
• Bytes/Second
• Kilobytes/Second
• Megabytes/Second
• Gigabytes/Second
• Terabytes/Second
• Bits/Second
Options API Version 2010-08-01 32
Amazon CloudWatch Command Line Reference
Name Description
• Kilobits/Second
• Megabits/Second
• Gigabits/Second
• Terabits/Second
• Count/Second
• None
Default: n/a
Required: No
Common options
Name Description
--aws-credential-file  VALUE The location of the ﬁle with your AWS credentia 
ls. You can set this value using the environment 
variable AWS_CREDENTIAL_FILE . If you deﬁne the 
environment variable or you provide the path to the 
credential ﬁle, the ﬁle must exist or the request fails. 
All CloudWatch requests must be signed using your 
access key ID and secret access key.
Type: String
Valid values: A valid path to a ﬁle containing your 
access key ID and secret access key.
Default: Uses the environment variable AWS_CREDE 
NTIAL_FILE , if set.
-C, --ec2-cert-file-path
VALUE
The location of your EC2 certiﬁcate ﬁle for signing 
requests. You can use the environment variable
EC2_CERT to specify this value.
Common options API Version 2010-08-01 33
Amazon CloudWatch Command Line Reference
Name Description
Type: String
Valid values: A valid ﬁle path to the PEM ﬁle 
provided by Amazon EC2 or AWS Identity and Access 
Management.
Default: Uses the environment variable EC2_CERT, if 
set.
--connection-timeout  VALUE The connection timeout value, in seconds.
Type: Integer
Valid values: Any positive number.
Default: 30
--delimiter  VALUE The delimiter to use when displaying delimited (long) 
results.
Type: String
Valid values: Any string.
Default: Comma (,)
--headers If you are displaying tabular or delimited results, 
include the column headers. If you are showing XML 
results, return the HTTP headers from the service 
request, if applicable.
Type: Flag
Valid values: When present, shows headers.
Default: The --headers  option is oﬀ by default.
Common options API Version 2010-08-01 34
Amazon CloudWatch Command Line Reference
Name Description
-I, --access-key-id  VALUE The access key ID that will be used, in conjunction with 
the secret key, to sign the request. This must be used 
in conjunction with --secret-key, otherwise the option 
is ignored. All requests to CloudWatch must be signed, 
otherwise the request is rejected.
Type: String
Valid values: A valid access key ID.
Default: None
-K, --ec2-private-key-file-
path  VALUE
The private key that will be used to sign the request. 
Using public/private keys causes the CLI to use SOAP. 
The request is signed with a public certiﬁcate and 
private key. This parameter must be used in conjuncti 
on with EC2_CERT, otherwise the value is ignored. 
The value of the environment variable EC2_PRIVA 
TE_KEY  will be used if it is set, and this option is 
not speciﬁed. This option is ignored if the environme 
nt variable AWS_CREDENTIAL_FILE  is set, or --
aws-credentials-file  is used. All requests to 
CloudWatch must be signed, otherwise the request is 
rejected.
Type: String
Valid values: The path to a valid ASN.1 private key.
Default: None
Common options API Version 2010-08-01 35
Amazon CloudWatch Command Line Reference
Name Description
--region VALUE The region requests are directed to. You can use the 
environment variable EC2_REGION  to specify the 
value. The region is used to create the URL used to 
call CloudWatch, and must be a valid Amazon Web 
Services (AWS) region.
Type: String
Valid values: Any AWS region, for example, us-east-1.
Default: us-east-1, unless the EC2_REGION
environment variable is set.
S, --secret-key  VALUE The secret access key that will be used to sign the 
request, in conjunction with an access key ID. This 
parameter must be used in conjunction with --
access-key-id , otherwise this option is ignored.
Type: String
Valid values: Your access key ID.
Default: None
--show-empty-fields Shows empty ﬁelds using (nil) as a placeholder to 
indicate that this data was not requested.
Type: Flag
Valid values: None
Default: Empty ﬁelds are not shown by default.
Common options API Version 2010-08-01 36
Amazon CloudWatch Command Line Reference
Name Description
--show-request Displays the URL the CLI uses to call AWS.
Type: Flag
Valid values: None
Default: false
--show-table, --show-long, 
--show-xml, --quiet
Speciﬁes how the results are displayed: in a table, 
delimited (long), XML, or no output (quiet). The --
show-table  display shows a subset of the data in 
ﬁxed column-width form; --show-long  shows all 
of the returned values delimited by a character; --
show-xml  is the raw return from the service; and --
quiet suppresses all standard output. All options are 
mutually exclusive, with the priority --show-table ,
--show-long , --show-xml , and --quiet.
Type: Flag
Valid values: None
Default: --show-table
-U, --url VALUE The URL used to contact CloudWatch. You can set 
this value using the environment variable AWS_CLOUD 
WATCH_URL . This value is used in conjunction with
--region to create the expected URL. This option 
overrides the URL for the service call.
Type: String
Valid values: A valid HTTP or HTTPS URL.
Default: Uses the value speciﬁed in AWS_CLOUD 
WATCH_URL , if set.
Common options API Version 2010-08-01 37
Amazon CloudWatch Command Line Reference
Output
This command returns a table that contains the following:
• ALARM - Alarm name.
• DESCRIPTION - The alarm description. This column appears only in the --show-long view.
• STATE - The alarm state.
• STATE_REASON - A human-readable reason for state. This column appears only in the --show-
long view.
• STATE_REASON_DATA - A machine-readable reason for state (JSON format). This column 
appears only in the --show-long view.
• ENABLED - Enables or disables actions. This column appears only in the --show-long view.
• OK_ACTIONS - The action to execute on OK status. This column appears only in the --show-long 
view.
• ALARM_ACTIONS - The action to execute on ALARM status.
• INSUFFICIENT_DATA_ACTIONS - The action to execute on INSUFFICIENT_DATA status. This 
column appears only in the --show-long view.
• NAMESPACE - A namespace for the metric.
• METRIC_NAME - The name of the metric.
• DIMENSIONS - The metric dimensions. This column appears only in the --show-long view.
• PERIOD - The period.
• STATISTIC - The statistic (Average, Minimum, Maximum, Sum, SampleCount).
• EXTENDEDSTATISTIC - The percentile statistic.
• UNIT - The unit. This column appears only in the --show-long view.
• EVAL_PERIODS - The number of periods to evaluate the metric.
• COMPARISON - The comparison operator.
• THRESHOLD - The threshold.
The Amazon CloudWatch CLI displays errors on stderr.
Output API Version 2010-08-01 38
Amazon CloudWatch Command Line Reference
Examples
Example request
This example describes an alarm for a given metric.
mon-describe-alarms-for-metric--metric-name CPUUtilization --namespace AWS/EC2  --
dimensions InstanceId=i-abcdef 
This is an example output of this command.
ALARM    STATE ALARM_ACTIONS  NAMESPACE  METRIC_NAME    PERIOD  STATISTIC  EVAL_PERIODS 
  COMPARISON            THRESHOLD
my-alarm1  OK    arn:aws:sns:.. AWS/EC2    CPUUtilization 60      Average    3          
    GreaterThanThreshold  100.0
my-alarm2  OK    arn:aws:sns:.. AWS/EC2    CPUUtilization 60      Average    5          
    GreaterThanThreshold  80.0
Related topics
Download
• Set up the command line interface
Related action
• DescribeAlarmForMetric
Related commands
• mon-describe-alarm-history
• mon-describe-alarms
mon-disable-alarm-actions
Description
Disables all actions for the speciﬁed alarms.
Examples API Version 2010-08-01 39
Amazon CloudWatch Command Line Reference
Syntax
mon-disable-alarm-actions [AlarmNames [AlarmNames ...]] [Common Options]
Options
Name Description
AlarmNames  AlarmNames The names of the alarms. You can also set this value 
using --alarm-name .
Type: Argument
Valid values: A valid list of alarm names.
Default: n/a
Required: Yes
Common options
Name Description
--aws-credential-file  VALUE The location of the ﬁle with your AWS credentia 
ls. You can set this value using the environment 
variable AWS_CREDENTIAL_FILE . If you deﬁne the 
environment variable or you provide the path to the 
credential ﬁle, the ﬁle must exist or the request fails. 
All CloudWatch requests must be signed using your 
access key ID and secret access key.
Type: String
Valid values: A valid path to a ﬁle containing your 
access key ID and secret access key.
Default: Uses the environment variable AWS_CREDE 
NTIAL_FILE , if set.
Syntax API Version 2010-08-01 40
Amazon CloudWatch Command Line Reference
Name Description
-C, --ec2-cert-file-path
VALUE
The location of your EC2 certiﬁcate ﬁle for signing 
requests. You can use the environment variable
EC2_CERT to specify this value.
Type: String
Valid values: A valid ﬁle path to the PEM ﬁle 
provided by Amazon EC2 or AWS Identity and Access 
Management.
Default: Uses the environment variable EC2_CERT, if 
set.
--connection-timeout  VALUE The connection timeout value, in seconds.
Type: Integer
Valid values: Any positive number.
Default: 30
--delimiter  VALUE The delimiter to use when displaying delimited (long) 
results.
Type: String
Valid values: Any string.
Default: Comma (,)
Common options API Version 2010-08-01 41
Amazon CloudWatch Command Line Reference
Name Description
--headers If you are displaying tabular or delimited results, 
include the column headers. If you are showing XML 
results, return the HTTP headers from the service 
request, if applicable.
Type: Flag
Valid values: When present, shows headers.
Default: The --headers  option is oﬀ by default.
-I, --access-key-id  VALUE The access key ID that will be used, in conjunction with 
the secret key, to sign the request. This must be used 
in conjunction with --secret-key, otherwise the option 
is ignored. All requests to CloudWatch must be signed, 
otherwise the request is rejected.
Type: String
Valid values: A valid access key ID.
Default: None
Common options API Version 2010-08-01 42
Amazon CloudWatch Command Line Reference
Name Description
-K, --ec2-private-key-file-
path  VALUE
The private key that will be used to sign the request. 
Using public/private keys causes the CLI to use SOAP. 
The request is signed with a public certiﬁcate and 
private key. This parameter must be used in conjuncti 
on with EC2_CERT, otherwise the value is ignored. 
The value of the environment variable EC2_PRIVA 
TE_KEY  will be used if it is set, and this option is 
not speciﬁed. This option is ignored if the environme 
nt variable AWS_CREDENTIAL_FILE  is set, or --
aws-credentials-file  is used. All requests to 
CloudWatch must be signed, otherwise the request is 
rejected.
Type: String
Valid values: The path to a valid ASN.1 private key.
Default: None
--region VALUE The region requests are directed to. You can use the 
environment variable EC2_REGION  to specify the 
value. The region is used to create the URL used to 
call CloudWatch, and must be a valid Amazon Web 
Services (AWS) region.
Type: String
Valid values: Any AWS region, for example, us-east-1.
Default: us-east-1, unless the EC2_REGION
environment variable is set.
Common options API Version 2010-08-01 43
Amazon CloudWatch Command Line Reference
Name Description
S, --secret-key  VALUE The secret access key that will be used to sign the 
request, in conjunction with an access key ID. This 
parameter must be used in conjunction with --
access-key-id , otherwise this option is ignored.
Type: String
Valid values: Your access key ID.
Default: None
--show-empty-fields Shows empty ﬁelds using (nil) as a placeholder to 
indicate that this data was not requested.
Type: Flag
Valid values: None
Default: Empty ﬁelds are not shown by default.
--show-request Displays the URL the CLI uses to call AWS.
Type: Flag
Valid values: None
Default: false
Common options API Version 2010-08-01 44
Amazon CloudWatch Command Line Reference
Name Description
--show-table, --show-long, 
--show-xml, --quiet
Speciﬁes how the results are displayed: in a table, 
delimited (long), XML, or no output (quiet). The --
show-table  display shows a subset of the data in 
ﬁxed column-width form; --show-long  shows all 
of the returned values delimited by a character; --
show-xml  is the raw return from the service; and --
quiet suppresses all standard output. All options are 
mutually exclusive, with the priority --show-table ,
--show-long , --show-xml , and --quiet.
Type: Flag
Valid values: None
Default: --show-table
-U, --url VALUE The URL used to contact CloudWatch. You can set 
this value using the environment variable AWS_CLOUD 
WATCH_URL . This value is used in conjunction with
--region to create the expected URL. This option 
overrides the URL for the service call.
Type: String
Valid values: A valid HTTP or HTTPS URL.
Default: Uses the value speciﬁed in AWS_CLOUD 
WATCH_URL , if set.
Output
This command disables alarm actions for the speciﬁed alarms.
The Amazon CloudWatch CLI displays errors on stderr.
Output API Version 2010-08-01 45
Amazon CloudWatch Command Line Reference
Examples
Example request
This example disables all actions for an alarm called my-alarm.
mon-disable-alarm-actions --alarm-name my-alarm
Related topics
Download
• Set up the command line interface
Related action
• DisableAlarmActions
Related commands
• mon-enable-alarm-actions
• mon-delete-alarms
mon-enable-alarm-actions
Description
Enables all actions for the speciﬁed alarms.
Syntax
mon-enable-alarm-actions [AlarmNames [AlarmNames ...]] [Common Options]
Examples API Version 2010-08-01 46
Amazon CloudWatch Command Line Reference
Options
Name Description
AlarmNames  AlarmNames The names of the alarms. You can also set this value 
using --alarm-name .
Type: Argument
Valid values: A valid list of alarm names.
Default: n/a
Required: Yes
Common options
Name Description
--aws-credential-file  VALUE The location of the ﬁle with your AWS credentia 
ls. You can set this value using the environment 
variable AWS_CREDENTIAL_FILE . If you deﬁne the 
environment variable or you provide the path to the 
credential ﬁle, the ﬁle must exist or the request fails. 
All CloudWatch requests must be signed using your 
access key ID and secret access key.
Type: String
Valid values: A valid path to a ﬁle containing your 
access key ID and secret access key.
Default: Uses the environment variable AWS_CREDE 
NTIAL_FILE , if set.
-C, --ec2-cert-file-path
VALUE
The location of your EC2 certiﬁcate ﬁle for signing 
requests. You can use the environment variable
EC2_CERT to specify this value.
Options API Version 2010-08-01 47
Amazon CloudWatch Command Line Reference
Name Description
Type: String
Valid values: A valid ﬁle path to the PEM ﬁle 
provided by Amazon EC2 or AWS Identity and Access 
Management.
Default: Uses the environment variable EC2_CERT, if 
set.
--connection-timeout  VALUE The connection timeout value, in seconds.
Type: Integer
Valid values: Any positive number.
Default: 30
--delimiter  VALUE The delimiter to use when displaying delimited (long) 
results.
Type: String
Valid values: Any string.
Default: Comma (,)
--headers If you are displaying tabular or delimited results, 
include the column headers. If you are showing XML 
results, return the HTTP headers from the service 
request, if applicable.
Type: Flag
Valid values: When present, shows headers.
Default: The --headers  option is oﬀ by default.
Common options API Version 2010-08-01 48
Amazon CloudWatch Command Line Reference
Name Description
-I, --access-key-id  VALUE The access key ID that will be used, in conjunction with 
the secret key, to sign the request. This must be used 
in conjunction with --secret-key, otherwise the option 
is ignored. All requests to CloudWatch must be signed, 
otherwise the request is rejected.
Type: String
Valid values: A valid access key ID.
Default: None
-K, --ec2-private-key-file-
path  VALUE
The private key that will be used to sign the request. 
Using public/private keys causes the CLI to use SOAP. 
The request is signed with a public certiﬁcate and 
private key. This parameter must be used in conjuncti 
on with EC2_CERT, otherwise the value is ignored. 
The value of the environment variable EC2_PRIVA 
TE_KEY  will be used if it is set, and this option is 
not speciﬁed. This option is ignored if the environme 
nt variable AWS_CREDENTIAL_FILE  is set, or --
aws-credentials-file  is used. All requests to 
CloudWatch must be signed, otherwise the request is 
rejected.
Type: String
Valid values: The path to a valid ASN.1 private key.
Default: None
Common options API Version 2010-08-01 49
Amazon CloudWatch Command Line Reference
Name Description
--region VALUE The region requests are directed to. You can use the 
environment variable EC2_REGION  to specify the 
value. The region is used to create the URL used to 
call CloudWatch, and must be a valid Amazon Web 
Services (AWS) region.
Type: String
Valid values: Any AWS region, for example, us-east-1.
Default: us-east-1, unless the EC2_REGION
environment variable is set.
S, --secret-key  VALUE The secret access key that will be used to sign the 
request, in conjunction with an access key ID. This 
parameter must be used in conjunction with --
access-key-id , otherwise this option is ignored.
Type: String
Valid values: Your access key ID.
Default: None
--show-empty-fields Shows empty ﬁelds using (nil) as a placeholder to 
indicate that this data was not requested.
Type: Flag
Valid values: None
Default: Empty ﬁelds are not shown by default.
Common options API Version 2010-08-01 50
Amazon CloudWatch Command Line Reference
Name Description
--show-request Displays the URL the CLI uses to call AWS.
Type: Flag
Valid values: None
Default: false
--show-table, --show-long, 
--show-xml, --quiet
Speciﬁes how the results are displayed: in a table, 
delimited (long), XML, or no output (quiet). The --
show-table  display shows a subset of the data in 
ﬁxed column-width form; --show-long  shows all 
of the returned values delimited by a character; --
show-xml  is the raw return from the service; and --
quiet suppresses all standard output. All options are 
mutually exclusive, with the priority --show-table ,
--show-long , --show-xml , and --quiet.
Type: Flag
Valid values: None
Default: --show-table
-U, --url VALUE The URL used to contact CloudWatch. You can set 
this value using the environment variable AWS_CLOUD 
WATCH_URL . This value is used in conjunction with
--region to create the expected URL. This option 
overrides the URL for the service call.
Type: String
Valid values: A valid HTTP or HTTPS URL.
Default: Uses the value speciﬁed in AWS_CLOUD 
WATCH_URL , if set.
Common options API Version 2010-08-01 51
Amazon CloudWatch Command Line Reference
Output
This command enables alarm actions for the speciﬁed alarms.
The Amazon CloudWatch CLI displays errors on stderr.
Examples
Example request
This example enables all actions for the alarm named my-alarm.
mon-enable-alarm-actions --alarm-name my-alarm
Related topics
Download
• Set up the command line interface
Related action
• EnableAlarmActions
Related commands
• mon-disable-alarm-actions
• mon-delete-alarms
mon-get-stats
Description
Gets time-series data for the speciﬁed statistics.
Output API Version 2010-08-01 52
Amazon CloudWatch Command Line Reference
Note
When you create a new metric using the mon-put-data command, it can take up to two 
minutes before you can retrieve statistics on the new metric using the mon-get-stats
command. However, it can take up to ﬁfteen minutes before the new metric appears in the 
list of metrics retrieved using the mon-list-metrics command.
Syntax
mon-get-stats MetricName --namespace value --statistics value[,value...] 
[--dimensions "key1=value1,key2=value2..." ] [--end-time value] [--period
value] [--start-time value] [--unit value] [Common Options]
Options
Name Description
MetricName The name of the metric. You can also set this value 
using --metric-name .
Type: Argument
Valid values: Any valid metric name between 1 and 255 
characters.
Default: n/a
Required: Yes
--dimensions  "key1=val 
ue1,key2=value2..."
The dimensions of the metric. You can specify 
dimensions two ways and the formats can be combined 
or used interchangeably:
• One option per dimension: --dimensions "key1=val 
ue1" --dimensions "key2=value2"
• All in one option: --dimensions "key1=value1,key2= 
value2"
Syntax API Version 2010-08-01 53
Amazon CloudWatch Command Line Reference
Name Description
Type: Map
Valid values: A string of the format name=value, where 
the key is the name of the dimension, and the value 
is the dimension's value. The dimension names, and 
values must be an ANSI string between 1 and 250 
characters long. A maximum of 10 dimensions are 
allowed.
Default: n/a
Required: No
--end-time  VALUE The latest allowed timestamp for returned data points. 
The ending time is exclusive. Timestamps are speciﬁed 
using ISO8601 combined format. For example the date 
and time July 30th, 2013 at 12:30:00 PST would be 
represented as 2013-07-30T12:30:00-07:00, or in UTC: 
2013-07-30T19:30:00Z. The highest resolution that 
can be returned by CloudWatch is 1 minute, as such all 
timestamps are rounded down to the nearest minute.
Type: Argument
Valid values: A valid timestamp represented in ISO8601 
format with time zone oﬀset, or UTC indicator.
Default: The current date/time.
Required: No
Options API Version 2010-08-01 54
Amazon CloudWatch Command Line Reference
Name Description
-n, --namespace  VALUE The namespace of the metric. For more information 
about namespaces, see AWS Namespaces.
Type: String
Valid values: A valid namespace between 1 and 250 
characters in length.
Default: n/a
Required: Yes
--period VALUE The granularity, in seconds, to retrieve statistics for. 
The period must be at least 60 seconds and must be a 
multiple of 60.
Type: Argument
Valid values: A number, in seconds that is a multiple of 
60 seconds.
Default: 60 seconds.
Required: No
-s, --statistics  VALUE1,VA 
LUE2,VALUE3...
The statistics to be returned for the speciﬁed metric.
Type: Enumeration
Valid values: Average, Sum, Maximum, or Minimum
Default: n/a
Required: Yes
Options API Version 2010-08-01 55
Amazon CloudWatch Command Line Reference
Name Description
--start-time  VALUE The ﬁrst allowed timestamp for returned data points. 
The starting time is inclusive. Timestamps are speciﬁed 
using ISO8601 combined format. For example the date 
and time July 30th, 2013 at 12:30:00 PST would be 
represented as 2013-07-30T12:30:00-07:00, or in UTC: 
2013-07-30T19:30:00Z. The highest resolution that 
can be returned by CloudWatch is 1 minute, as such all 
timestamps are rounded down to the nearest minute.
Type: Argument
Valid values: A valid timestamp represented in ISO8601 
format with time zone oﬀset, or UTC indicator.
Default: One hour before the current time.
Required: No
Options API Version 2010-08-01 56
Amazon CloudWatch Command Line Reference
Name Description
--unit VALUE The unit to retrieve the metrics for. Metrics may be 
reported in multiple units, this retrieve a speciﬁc unit 
for a given metric. Not requesting a unit will result in all 
units being returned. If the metric is only ever reported 
with one unit this will have no eﬀect.
Type: Enumeration
Valid values: One of the following:
• Seconds
• Microseconds
• Milliseconds
• Bytes
• Kilobytes
• Megabytes
• Gigabytes
• Terabytes
• Bits
• Kilobits
• Megabits
• Gigabits
• Terabits
• Percent
• Count
• Bytes/Second
• Kilobytes/Second
• Megabytes/Second
• Gigabytes/Second
• Terabytes/Second
• Bits/Second
Options API Version 2010-08-01 57
Amazon CloudWatch Command Line Reference
Name Description
• Kilobits/Second
• Megabits/Second
• Gigabits/Second
• Terabits/Second
• Count/Second
• None
Default: n/a
Required: No
Common options
Name Description
--aws-credential-file  VALUE The location of the ﬁle with your AWS credentia 
ls. You can set this value using the environment 
variable AWS_CREDENTIAL_FILE . If you deﬁne the 
environment variable or you provide the path to the 
credential ﬁle, the ﬁle must exist or the request fails. 
All CloudWatch requests must be signed using your 
access key ID and secret access key.
Type: String
Valid values: A valid path to a ﬁle containing your 
access key ID and secret access key.
Default: Uses the environment variable AWS_CREDE 
NTIAL_FILE , if set.
-C, --ec2-cert-file-path
VALUE
The location of your EC2 certiﬁcate ﬁle for signing 
requests. You can use the environment variable
EC2_CERT to specify this value.
Common options API Version 2010-08-01 58
Amazon CloudWatch Command Line Reference
Name Description
Type: String
Valid values: A valid ﬁle path to the PEM ﬁle 
provided by Amazon EC2 or AWS Identity and Access 
Management.
Default: Uses the environment variable EC2_CERT, if 
set.
--connection-timeout  VALUE The connection timeout value, in seconds.
Type: Integer
Valid values: Any positive number.
Default: 30
--delimiter  VALUE The delimiter to use when displaying delimited (long) 
results.
Type: String
Valid values: Any string.
Default: Comma (,)
--headers If you are displaying tabular or delimited results, 
include the column headers. If you are showing XML 
results, return the HTTP headers from the service 
request, if applicable.
Type: Flag
Valid values: When present, shows headers.
Default: The --headers  option is oﬀ by default.
Common options API Version 2010-08-01 59
Amazon CloudWatch Command Line Reference
Name Description
-I, --access-key-id  VALUE The access key ID that will be used, in conjunction with 
the secret key, to sign the request. This must be used 
in conjunction with --secret-key, otherwise the option 
is ignored. All requests to CloudWatch must be signed, 
otherwise the request is rejected.
Type: String
Valid values: A valid access key ID.
Default: None
-K, --ec2-private-key-file-
path  VALUE
The private key that will be used to sign the request. 
Using public/private keys causes the CLI to use SOAP. 
The request is signed with a public certiﬁcate and 
private key. This parameter must be used in conjuncti 
on with EC2_CERT, otherwise the value is ignored. 
The value of the environment variable EC2_PRIVA 
TE_KEY  will be used if it is set, and this option is 
not speciﬁed. This option is ignored if the environme 
nt variable AWS_CREDENTIAL_FILE  is set, or --
aws-credentials-file  is used. All requests to 
CloudWatch must be signed, otherwise the request is 
rejected.
Type: String
Valid values: The path to a valid ASN.1 private key.
Default: None
Common options API Version 2010-08-01 60
Amazon CloudWatch Command Line Reference
Name Description
--region VALUE The region requests are directed to. You can use the 
environment variable EC2_REGION  to specify the 
value. The region is used to create the URL used to 
call CloudWatch, and must be a valid Amazon Web 
Services (AWS) region.
Type: String
Valid values: Any AWS region, for example, us-east-1.
Default: us-east-1, unless the EC2_REGION
environment variable is set.
S, --secret-key  VALUE The secret access key that will be used to sign the 
request, in conjunction with an access key ID. This 
parameter must be used in conjunction with --
access-key-id , otherwise this option is ignored.
Type: String
Valid values: Your access key ID.
Default: None
--show-empty-fields Shows empty ﬁelds using (nil) as a placeholder to 
indicate that this data was not requested.
Type: Flag
Valid values: None
Default: Empty ﬁelds are not shown by default.
Common options API Version 2010-08-01 61
Amazon CloudWatch Command Line Reference
Name Description
--show-request Displays the URL the CLI uses to call AWS.
Type: Flag
Valid values: None
Default: false
--show-table, --show-long, 
--show-xml, --quiet
Speciﬁes how the results are displayed: in a table, 
delimited (long), XML, or no output (quiet). The --
show-table  display shows a subset of the data in 
ﬁxed column-width form; --show-long  shows all 
of the returned values delimited by a character; --
show-xml  is the raw return from the service; and --
quiet suppresses all standard output. All options are 
mutually exclusive, with the priority --show-table ,
--show-long , --show-xml , and --quiet.
Type: Flag
Valid values: None
Default: --show-table
-U, --url VALUE The URL used to contact CloudWatch. You can set 
this value using the environment variable AWS_CLOUD 
WATCH_URL . This value is used in conjunction with
--region to create the expected URL. This option 
overrides the URL for the service call.
Type: String
Valid values: A valid HTTP or HTTPS URL.
Default: Uses the value speciﬁed in AWS_CLOUD 
WATCH_URL , if set.
Common options API Version 2010-08-01 62
Amazon CloudWatch Command Line Reference
Output
This command returns a table that contains the following:
• Time - The time the metrics were taken.
• SampleCount - No description available for this column.
• Average - The average value.
• Sum - The sum of values.
• Minimum - The minimum observed value.
• Maximum - The maximum observed value.
• Unit - The unit of the metric.
The Amazon CloudWatch CLI displays errors on stderr.
Examples
Example request
This example returns the average, minimum, and maximum CPU utilization for EC2 instance i-
c07704a9, at 1 hour resolution.
mon-get-stats CPUUtilization --start-time 2013-02-14T23:00:00.000Z --end-time 
 2013-03-14T23:00:00.000Z --period 3600 --statistics "Average,Minimum,Maximum" --
namespace "AWS/EC2" --dimensions "InstanceId=i-c07704a9"
This is an example of an output of the Samples and Average metrics at one minute resolution.
Time                 Samples  Average  Unit    
2013-05-19 00:03:00  2.0      0.19     Percent
2013-05-19 00:04:00  2.0      0        Percent
2013-05-19 00:05:00  2.0      0        Percent
2013-05-19 00:06:00  2.0      0        Percent
2013-05-19 00:07:00  2.0      0        Percent
2013-05-19 00:08:00  2.0      0        Percent
2013-05-19 00:09:00  2.0      0        Percent
2013-05-19 00:10:00  2.0      0        Percent
2013-05-19 00:11:00  2.0      0        Percent
Output API Version 2010-08-01 63
Amazon CloudWatch Command Line Reference
2013-05-19 00:12:00  2.0      0.195    Percent
2013-05-19 00:13:00  2.0      0.215    Percent
...
Example request
This example returns CPU utilization across your EC2 ﬂeet.
mon-get-stats CPUUtilization --start-time 2013-02-14T23:00:00.000Z --end-time 
 2013-03-14T23:00:00.000Z --period 3600 --statistics "Average,Minimum,Maximum" --
namespace "AWS/EC2"
Example request
This example returns the average, minimum, and maximum request count made to the test stack of 
MyService for a particular user, at 1 hour resolution.
mon-get-stats RequestCount --start-time 2013-11-24T23:00:00.000Z --end-time 
 2013-11-25T23:00:00.000Z --period 3600 --statistics "Average,Minimum,Maximum" --
namespace "MyService" --dimensions "User=SomeUser,Stack=Test"
Example request
This example shows RequestCount statistics across all of "MyService".
mon-get-stats RequestCount --start-time 2013-11-24T23:00:00.000Z 
 --end-time 2013-11-25T23:00:00.000Z --period 3600 --statistics 
 "Average,Minimum,Maximum,SampleCount" --namespace "MyService" 
Related topics
Download
• Set up the command line interface
Related action
• GetMetricStatistics
Related topics API Version 2010-08-01 64
Amazon CloudWatch Command Line Reference
Related commands
• mon-list-metrics
• mon-describe-alarms
mon-list-metrics
Description
Lists the names, namespaces, and dimensions of the metrics associated with your AWS account. 
You can ﬁlter metrics using any combination of metric name, namespace, or dimensions. If you do 
not specify a ﬁlter, all possible matches for the attribute are returned.
Note
The mon-list-metrics command can take up to ﬁfteen minutes to report new metric names, 
namespaces, and dimensions added by calls to mon-put-data. The data points put by
mon-put-data, or other methods will be available by mon-get-statistics in less than 
ﬁve minutes.
Syntax
mon-list-metrics [--dimensions "key1=value1,key2=value2..."] [--metric-name
value] [--namespace value] [Common Options]
Options
Name Description
-d, --dimensions "key1=val 
ue1,key2=value2..."
The dimensions of the metric to retrieve. You can 
specify dimensions two ways and the formats can be 
combined or used interchangeably:
• One option per dimension: --dimensions "key1=val 
ue1" --dimensions "key2=value2"
mon-list-metrics API Version 2010-08-01 65
Amazon CloudWatch Command Line Reference
Name Description
• All in one option: --dimensions "key1=value1,key2= 
value2"
If no dimensions are speciﬁed, no ﬁltering of 
dimensions will be done. Any other requested ﬁlters 
will still be applied. To be included in the result a 
metric must contain all speciﬁed dimensions, although 
the metric may contain additional dimensions beyond 
the requested metrics.
Type: Map
Valid values: A string of the format name=value, where 
the key is the name of the dimension, and the value 
is the dimension's value. The dimension names, and 
values must be an ANSI string between 1 and 250 
characters long. A maximum of 10 dimensions are 
allowed.
Default: n/a
Required: No
-m, --metric-name  VALUE The name of the metric. To be included in the results, 
the metric name must match the requested metric 
name exactly. If no metric name is speciﬁed no 
ﬁltering is done. Any other requested ﬁlters are 
applied.
Type: Simple
Valid values: Any valid metric name between 1 and 
250 characters in length.
Default: n/a
Required: No
Options API Version 2010-08-01 66
Amazon CloudWatch Command Line Reference
Name Description
-n, --namespace   VALUE The namespace to use to ﬁlter metrics. For more 
information about namespaces, see AWS Namespaces.
Type: String
Valid values: A valid namespace between 1 and 250 
characters in length.
Default: n/a
Required: No
Common options
Name Description
--aws-credential-file  VALUE The location of the ﬁle with your AWS credentia 
ls. You can set this value using the environment 
variable AWS_CREDENTIAL_FILE . If you deﬁne the 
environment variable or you provide the path to the 
credential ﬁle, the ﬁle must exist or the request fails. 
All CloudWatch requests must be signed using your 
access key ID and secret access key.
Type: String
Valid values: A valid path to a ﬁle containing your 
access key ID and secret access key.
Default: Uses the environment variable AWS_CREDE 
NTIAL_FILE , if set.
-C, --ec2-cert-file-path
VALUE
The location of your EC2 certiﬁcate ﬁle for signing 
requests. You can use the environment variable
EC2_CERT to specify this value.
Common options API Version 2010-08-01 67
Amazon CloudWatch Command Line Reference
Name Description
Type: String
Valid values: A valid ﬁle path to the PEM ﬁle 
provided by Amazon EC2 or AWS Identity and Access 
Management.
Default: Uses the environment variable EC2_CERT, if 
set.
--connection-timeout  VALUE The connection timeout value, in seconds.
Type: Integer
Valid values: Any positive number.
Default: 30
--delimiter  VALUE The delimiter to use when displaying delimited (long) 
results.
Type: String
Valid values: Any string.
Default: Comma (,)
--headers If you are displaying tabular or delimited results, 
include the column headers. If you are showing XML 
results, return the HTTP headers from the service 
request, if applicable.
Type: Flag
Valid values: When present, shows headers.
Default: The --headers  option is oﬀ by default.
Common options API Version 2010-08-01 68
Amazon CloudWatch Command Line Reference
Name Description
-I, --access-key-id  VALUE The access key ID that will be used, in conjunction with 
the secret key, to sign the request. This must be used 
in conjunction with --secret-key, otherwise the option 
is ignored. All requests to CloudWatch must be signed, 
otherwise the request is rejected.
Type: String
Valid values: A valid access key ID.
Default: None
-K, --ec2-private-key-file-
path  VALUE
The private key that will be used to sign the request. 
Using public/private keys causes the CLI to use SOAP. 
The request is signed with a public certiﬁcate and 
private key. This parameter must be used in conjuncti 
on with EC2_CERT, otherwise the value is ignored. 
The value of the environment variable EC2_PRIVA 
TE_KEY  will be used if it is set, and this option is 
not speciﬁed. This option is ignored if the environme 
nt variable AWS_CREDENTIAL_FILE  is set, or --
aws-credentials-file  is used. All requests to 
CloudWatch must be signed, otherwise the request is 
rejected.
Type: String
Valid values: The path to a valid ASN.1 private key.
Default: None
Common options API Version 2010-08-01 69
Amazon CloudWatch Command Line Reference
Name Description
--region VALUE The region requests are directed to. You can use the 
environment variable EC2_REGION  to specify the 
value. The region is used to create the URL used to 
call CloudWatch, and must be a valid Amazon Web 
Services (AWS) region.
Type: String
Valid values: Any AWS region, for example, us-east-1.
Default: us-east-1, unless the EC2_REGION
environment variable is set.
S, --secret-key  VALUE The secret access key that will be used to sign the 
request, in conjunction with an access key ID. This 
parameter must be used in conjunction with --
access-key-id , otherwise this option is ignored.
Type: String
Valid values: Your access key ID.
Default: None
--show-empty-fields Shows empty ﬁelds using (nil) as a placeholder to 
indicate that this data was not requested.
Type: Flag
Valid values: None
Default: Empty ﬁelds are not shown by default.
Common options API Version 2010-08-01 70
Amazon CloudWatch Command Line Reference
Name Description
--show-request Displays the URL the CLI uses to call AWS.
Type: Flag
Valid values: None
Default: false
--show-table, --show-long, 
--show-xml, --quiet
Speciﬁes how the results are displayed: in a table, 
delimited (long), XML, or no output (quiet). The --
show-table  display shows a subset of the data in 
ﬁxed column-width form; --show-long  shows all 
of the returned values delimited by a character; --
show-xml  is the raw return from the service; and --
quiet suppresses all standard output. All options are 
mutually exclusive, with the priority --show-table ,
--show-long , --show-xml , and --quiet.
Type: Flag
Valid values: None
Default: --show-table
-U, --url VALUE The URL used to contact CloudWatch. You can set 
this value using the environment variable AWS_CLOUD 
WATCH_URL . This value is used in conjunction with
--region to create the expected URL. This option 
overrides the URL for the service call.
Type: String
Valid values: A valid HTTP or HTTPS URL.
Default: Uses the value speciﬁed in AWS_CLOUD 
WATCH_URL , if set.
Common options API Version 2010-08-01 71
Amazon CloudWatch Command Line Reference
Output
This command returns a table that contains the following:
• Metric Name - The name of the metric attached to this metric.
• Namespace - The namespace associated with this metric.
• Dimensions - The dimension names and values associated with this metric.
The Amazon CloudWatch CLI displays errors on stderr.
Examples
Example request
This example returns a list of all your metrics.
mon-list-metrics 
This is an example of an output of a call to 'mon-list-metrics'.
Metric Name                 Namespace  Dimensions
CPUUtilization               AWS/EC2    {InstanceId=i-e7e48a8e}
CPUUtilization               AWS/EC2    {InstanceId=i-231d744a}
CPUUtilization               AWS/EC2    {InstanceId=i-22016e4b}
CPUUtilization               AWS/EC2    {InstanceId=i-b0345cd9}
CPUUtilization               AWS/EC2    {InstanceId=i-539dff3a}
CPUUtilization               AWS/EC2    {InstanceId=i-af3544c6}
CPUUtilization               AWS/EC2    {InstanceId=i-d4f29ebd}
CPUUtilization               AWS/EC2    {ImageId=ami-de4daab7}
...
Example request
This example lists your metrics with the speciﬁed name.
mon-list-metrics --metric-name RequestCount
Example request
This example lists your metrics that belong to the speciﬁed namespace.
Output API Version 2010-08-01 72
Amazon CloudWatch Command Line Reference
mon-list-metrics --namespace MyService
Example request
This example lists your metrics with the speciﬁed dimension names and values.
mon-list-metrics --dimensions "User=SomeUser,Stack=Test"
Related topics
Download
• Set up the command line interface
Related action
• ListMetrics
Related command
• mon-describe-alarms
mon-put-data
Description
Adds metric data points to the speciﬁed metric. This call will put time-series data, for either the 
raw value or valid statistic values of a given metric name. It supports the input of a single data 
point at a time.
Note
When you create a new metric using the mon-put-data command, it can take up to two 
minutes before you can retrieve statistics on the new metric using the mon-get-stats
command. However, it can take up to ﬁfteen minutes before the new metric appears in the 
list of metrics retrieved using the mon-list-metrics command.
Related topics API Version 2010-08-01 73
Amazon CloudWatch Command Line Reference
Syntax
mon-put-data --metric-name value[--namespace value [--
dimensions "key1=value1,key2=value2..."] [--statisticValues 
"key1=value1,key2=value2..."] [--timestamp value] [--unit value] [--value
value] [Common Options]
Options
Name Description
-d, --dimensions "key1=value1,key2= 
value2..."
The dimensions that uniquely identify the metric data. 
You can specify dimensions two ways and the formats 
can be combined or used interchangeably:
• One option per dimension: --dimensions "key1=val 
ue1" --dimensions "key2=value2"
• All in one option: --dimensions "key1=value1,key2= 
value2"
Type: Map
Valid values: A string of the format name=value, where 
the key is the name of the dimension, and the value 
is the dimension's value. The dimension names, and 
values must be an ANSI string between 1 and 250 
characters long. A maximum of 10 dimensions are 
allowed.
Default: n/a
Required: No
-m, --metric-name  VALUE1,VA 
LUE2,VALUE3...
The name of the metric.
Type: String
Valid values: Any valid metric name between 1 and 250 
characters.
Syntax API Version 2010-08-01 74
Amazon CloudWatch Command Line Reference
Name Description
Default: n/a
Required: Yes
n, --namespace  VALUE The namespace of the metric. For more information 
about namespaces, see AWS Namespaces.
Type: String
Valid values: An ANSI string between 1 and 250 
characters in length.
Default: n/a
Required: Yes
-s, --statistic  Values 
"key1=value1,key2= 
value2..."
The statistics to store for the speciﬁed timestamp and 
metric. This option is exclusive with --value. At least 
one of --statisticValue  or --value must be 
speciﬁed.
Type: Map
Valid values: A string containing all double values for 
all statistic names: SampleCount, Sum, Maximum, and 
Minimum. All these values must be a value between 
1E-130 and 1E130.
Default: n/a
Required: Yes
Options API Version 2010-08-01 75
Amazon CloudWatch Command Line Reference
Name Description
-t, --timestamp  VALUE The timestamp of the data point or observation for 
the metric to record. Timestamps are speciﬁed using 
ISO8601 combined format. For example the date 
and time July 30th, 2013 at 12:30:00 PST would be 
represented as 2013-07-30T12:30:00-07:00, or in UTC: 
2013-07-30T19:30:00Z.
Type: Simple
Valid values: A valid timestamp represented in ISO8601 
format with time zone oﬀset, or UTC indicator.
Default: The current UTC time.
Required: No
Options API Version 2010-08-01 76
Amazon CloudWatch Command Line Reference
Name Description
-u, --unit VALUE The unit for the metric.
Type: Enumeration
Valid values: One of the following:
• Seconds
• Microseconds
• Milliseconds
• Bytes
• Kilobytes
• Megabytes
• Gigabytes
• Terabytes
• Bits
• Kilobits
• Megabits
• Gigabits
• Terabits
• Percent
• Count
• Bytes/Second
• Kilobytes/Second
• Megabytes/Second
• Gigabytes/Second
• Terabytes/Second
• Bits/Second
• Kilobits/Second
• Megabits/Second
• Gigabits/Second
• Terabits/Second
Options API Version 2010-08-01 77
Amazon CloudWatch Command Line Reference
Name Description
• Count/Second
• None
Default: n/a
Required: No
-v, --value VALUE A single value to be recorded. The value is translate 
d to a statistic set of the form: SampleCount=1, 
Sum=VALUE, Minimum=VALUE, Maximum=VALUE. This 
option is exclusive of --statisticValues .
Type: Simple
Valid values: All values must be a number between 
1E-130 and 1E130.
Default: n/a
Required: Yes
Common options
Name Description
--aws-credential-file  VALUE The location of the ﬁle with your AWS credentia 
ls. You can set this value using the environment 
variable AWS_CREDENTIAL_FILE . If you deﬁne the 
environment variable or you provide the path to the 
credential ﬁle, the ﬁle must exist or the request fails. 
All CloudWatch requests must be signed using your 
access key ID and secret access key.
Type: String
Common options API Version 2010-08-01 78
Amazon CloudWatch Command Line Reference
Name Description
Valid values: A valid path to a ﬁle containing your 
access key ID and secret access key.
Default: Uses the environment variable AWS_CREDE 
NTIAL_FILE , if set.
-C, --ec2-cert-file-path
VALUE
The location of your EC2 certiﬁcate ﬁle for signing 
requests. You can use the environment variable
EC2_CERT to specify this value.
Type: String
Valid values: A valid ﬁle path to the PEM ﬁle 
provided by Amazon EC2 or AWS Identity and Access 
Management.
Default: Uses the environment variable EC2_CERT, if 
set.
--connection-timeout  VALUE The connection timeout value, in seconds.
Type: Integer
Valid values: Any positive number.
Default: 30
--delimiter  VALUE The delimiter to use when displaying delimited (long) 
results.
Type: String
Valid values: Any string.
Default: Comma (,)
Common options API Version 2010-08-01 79
Amazon CloudWatch Command Line Reference
Name Description
--headers If you are displaying tabular or delimited results, 
include the column headers. If you are showing XML 
results, return the HTTP headers from the service 
request, if applicable.
Type: Flag
Valid values: When present, shows headers.
Default: The --headers  option is oﬀ by default.
-I, --access-key-id  VALUE The access key ID that will be used, in conjunction with 
the secret key, to sign the request. This must be used 
in conjunction with --secret-key, otherwise the option 
is ignored. All requests to CloudWatch must be signed, 
otherwise the request is rejected.
Type: String
Valid values: A valid access key ID.
Default: None
Common options API Version 2010-08-01 80
Amazon CloudWatch Command Line Reference
Name Description
-K, --ec2-private-key-file-
path  VALUE
The private key that will be used to sign the request. 
Using public/private keys causes the CLI to use SOAP. 
The request is signed with a public certiﬁcate and 
private key. This parameter must be used in conjuncti 
on with EC2_CERT, otherwise the value is ignored. 
The value of the environment variable EC2_PRIVA 
TE_KEY  will be used if it is set, and this option is 
not speciﬁed. This option is ignored if the environme 
nt variable AWS_CREDENTIAL_FILE  is set, or --
aws-credentials-file  is used. All requests to 
CloudWatch must be signed, otherwise the request is 
rejected.
Type: String
Valid values: The path to a valid ASN.1 private key.
Default: None
--region VALUE The region requests are directed to. You can use the 
environment variable EC2_REGION  to specify the 
value. The region is used to create the URL used to 
call CloudWatch, and must be a valid Amazon Web 
Services (AWS) region.
Type: String
Valid values: Any AWS region, for example, us-east-1.
Default: us-east-1, unless the EC2_REGION
environment variable is set.
Common options API Version 2010-08-01 81
Amazon CloudWatch Command Line Reference
Name Description
S, --secret-key  VALUE The secret access key that will be used to sign the 
request, in conjunction with an access key ID. This 
parameter must be used in conjunction with --
access-key-id , otherwise this option is ignored.
Type: String
Valid values: Your access key ID.
Default: None
--show-empty-fields Shows empty ﬁelds using (nil) as a placeholder to 
indicate that this data was not requested.
Type: Flag
Valid values: None
Default: Empty ﬁelds are not shown by default.
--show-request Displays the URL the CLI uses to call AWS.
Type: Flag
Valid values: None
Default: false
Common options API Version 2010-08-01 82
Amazon CloudWatch Command Line Reference
Name Description
--show-table, --show-long, 
--show-xml, --quiet
Speciﬁes how the results are displayed: in a table, 
delimited (long), XML, or no output (quiet). The --
show-table  display shows a subset of the data in 
ﬁxed column-width form; --show-long  shows all 
of the returned values delimited by a character; --
show-xml  is the raw return from the service; and --
quiet suppresses all standard output. All options are 
mutually exclusive, with the priority --show-table ,
--show-long , --show-xml , and --quiet.
Type: Flag
Valid values: None
Default: --show-table
-U, --url VALUE The URL used to contact CloudWatch. You can set 
this value using the environment variable AWS_CLOUD 
WATCH_URL . This value is used in conjunction with
--region to create the expected URL. This option 
overrides the URL for the service call.
Type: String
Valid values: A valid HTTP or HTTPS URL.
Default: Uses the value speciﬁed in AWS_CLOUD 
WATCH_URL , if set.
Output
This command adds metric data points to a metric.
The Amazon CloudWatch CLI displays errors on stderr.
Output API Version 2010-08-01 83
Amazon CloudWatch Command Line Reference
Examples
Example request
This example puts statistic data for RequestCount in the MyService namespace. The metric 
contains no dimensions and so represents the overall RequestCount across the entire service. The 
measurement is a pre-aggregated statisticValue representing ﬁve earlier measurements whose 
maximum was 70, whose minimum was 30, and whose sum was 250.
mon-put-data --metric-name RequestCount --namespace "MyService" 
 --timestamp 2013-11-25T00:00:00.000Z --statisticValues 
 "Sum=250,Minimum=30,Maximum=70,SampleCount=5"
Example request
This example puts user-speciﬁc RequestCount test data in the MyService namespace. The user 
and stack name are stored as dimensions in order to distinguish this metric from the service-wide 
metric in the example above.
mon-put-data --metric-name RequestCount --namespace "MyService" --dimensions 
 "User=SomeUser,Stack=Test" --timestamp 2013-11-25T00:00:00.000Z --value 50
Related topics
Download
• Set up the command line interface
Related action
• PutMetricData
Related command
• mon-put-metric-alarm
Examples API Version 2010-08-01 84
Amazon CloudWatch Command Line Reference
mon-put-metric-alarm
Description
Creates or updates an alarm and associates it with the speciﬁed CloudWatch metric. You can also 
use this command to associate one or more Amazon Simple Notiﬁcation Service (Amazon SNS) 
resources with an alarm.
When this operation creates an alarm, the alarm state is immediately set to INSUFFICIENT_DATA. 
The alarm is evaluated and its StateValue is set appropriately. Any actions associated with the 
StateValue is then executed.
Note
When updating an existing alarm, StateValue is left unchanged.
Syntax
mon-put-metric-alarm AlarmName --comparison-operator value --evaluation-
periods value --metric-name value --namespace value --period value [--
statistic value] [--extendedstatistic value] --threshold value [--
actions-enabled value] [--alarm-actions value[,value...] ] [--alarm-
description value] [--dimensions "key1=value1,key2=value2..."] [--ok-
actions value[,value...] ] [--unit value] [--insufficient-data-actions
value[,value...]] [Common Options]
Options
Name Description
AlarmName The name of the alarm to update or create. The name 
must be unique within your AWS account. You can also 
set this value using --alarm-name .
Type: Argument
Valid values: A UTF-8 string.
mon-put-metric-alarm API Version 2010-08-01 85
Amazon CloudWatch Command Line Reference
Name Description
Default: n/a
Required: Yes
--actions-enabled  VALUE Indicates whether actions should be executed when 
the alarm changes state.
Type: Boolean
Valid values: True or False
Default: True
Required: No
Options API Version 2010-08-01 86
Amazon CloudWatch Command Line Reference
Name Description
--alarm-actions  VALUE1,VA 
LUE2,VALUE3...
The actions (up to ﬁve) to execute when this alarm 
transitions into an ALARM state from any other 
state. Each action is speciﬁed as an Amazon Resource 
Name (ARN). Using alarm actions, you can publish 
to an Amazon SNS topic, activate an Amazon EC2 
Auto Scaling policy, or stop, terminate, or recover an 
Amazon EC2 instance.
Note
If you are using an AWS Identity and Access 
Management (IAM) account to create or 
modify an alarm, you must have the following 
Amazon EC2 permissions:
• ec2:DescribeInstanceStatus  and
ec2:DescribeInstances  for all alarms 
on Amazon EC2 instance status metrics.
• ec2:StopInstances  for alarms with stop 
actions.
• ec2:TerminateInstances  for alarms 
with terminate actions.
• ec2:DescribeInstanceRecover 
yAttribute , and ec2:Recov 
erInstances  for alarms with recover 
actions.
If you have read/write permissions for Amazon 
CloudWatch but not for Amazon EC2, you can 
still create an alarm but the stop or terminate 
actions won’t be performed on the Amazon 
EC2 instance. However, if you are later granted 
permission to use the associated Amazon EC2 
APIs, the alarm actions you created earlier will 
Options API Version 2010-08-01 87
Amazon CloudWatch Command Line Reference
Name Description
be performed. For more information about 
IAM permissions, see Permissions and Policies
in IAM User Guide.
If you are using an IAM role (for example, an 
Amazon EC2 instance proﬁle), you cannot stop 
or terminate the instance using alarm actions. 
However, you can still see the alarm state and 
perform any other actions such as Amazon 
SNS notiﬁcations or Amazon EC2 Auto Scaling 
policies.
If you are using temporary security credentials 
granted using the AWS Security Token Service 
(AWS STS), you cannot stop or terminate an 
Amazon EC2 instance using alarm actions.
Type: String
Valid values: An ARN for an Amazon SNS topic, an 
Auto Scaling policy, or an ARN to stop, terminate, or 
recover an Amazon EC2 instance.
Default: n/a
Required: No
--alarm-description  VALUE The description of the alarm.
Type: String
Valid values: Any Unicode string between 1 and 255 
characters in length.
Default: n/a
Required: No
Options API Version 2010-08-01 88
Amazon CloudWatch Command Line Reference
Name Description
--comparison-operator  VALUE The comparison operator used to compare a data 
point to the threshold.
Type: Enumeration
Valid values: one of GreaterThanOrEqualToThresho 
ld, GreaterThanThreshold, LessThanThreshold, or 
LessThanOrEqualToThreshold
Default: n/a
Required: Yes
--dimensions  "key1=val 
ue1,key2=value2..."
The dimensions of the metric to create that you want 
to create an alarm for. You can specify dimensions 
two ways and the formats can be combined or used 
interchangeably:
• One option per dimension: --dimensions "key1=val 
ue1" --dimensions "key2=value2"
• All in one option: --dimensions "key1=value1,key2= 
value2"
Type: Map
Valid values: A string of the format name=value, 
where the key is the name of the dimension, and the 
value is the dimension's value. The dimension names, 
and values must be an ANSI string between 1 and 250 
characters long. A maximum of 10 dimensions are 
allowed.
Default: n/a
Required: No
Options API Version 2010-08-01 89
Amazon CloudWatch Command Line Reference
Name Description
--evaluation-periods  VALUE The number of consecutive periods for which the 
value of the metric is compared to the threshold to 
determine alarm status.
Type: Integer
Valid values: A number greater than zero.
Default: n/a
Required: Yes
--metric-name  VALUE The name of the metric on which to alarm.
Type: Argument
Valid values: An ANSI string between 1 and 250 
characters in length.
Default: n/a
Required: Yes
--namespace  VALUE The namespace of the metric on which to alarm. 
For more information about namespaces, see AWS 
Namespaces.
Type: String
Valid values: An ANSI string between 1 and 250 
characters in length.
Default: n/a
Required: Yes
Options API Version 2010-08-01 90
Amazon CloudWatch Command Line Reference
Name Description
--ok-actions  VALUE1,VA 
LUE2,VALUE3...
The actions (up to ﬁve) to execute when this alarm 
transitions into an OK state from any other state. 
Each action is speciﬁed as an Amazon Resource Name 
(ARN).
Type: String
Valid values: A valid ARN identiﬁer.
Default: n/a
Required: No
--period VALUE The period of metric on which to alarm (in seconds).
Type: Argument
Valid values: A number, in seconds that is a multiple of 
60 seconds.
Default: n/a
Required: Yes
--statistic  VALUE The statistic of the metric on which to alarm.
Type: Enumeration
Valid values: SampleCount, Average, Sum, Minimum, 
or Maximum
Default: n/a
Required: You must specify --statistic or --extende 
dstatistic.
Options API Version 2010-08-01 91
Amazon CloudWatch Command Line Reference
Name Description
--extendedstatistic  VALUE The percentile statistic of the metric on which to 
alarm.
Type: String
Valid values: Any percentile, with up to two decimal 
places (for example, p95.45).
Default: n/a
Required: You must specify --statistic or --extende 
dstatistic.
--threshold  VALUE The threshold that data points are compared with to 
determine the alarm state.
Type: Double
Valid values: A double value. All values must be a 
number between 1E-130 and 1E130.
Default: n/a
Required: Yes
Options API Version 2010-08-01 92
Amazon CloudWatch Command Line Reference
Name Description
--unit VALUE The unit of the metric on which to alarm.
Type: Enumeration
Valid values: One of the following:
• Seconds
• Microseconds
• Milliseconds
• Bytes
• Kilobytes
• Megabytes
• Gigabytes
• Terabytes
• Bits
• Kilobits
• Megabits
• Gigabits
• Terabits
• Percent
• Count
• Bytes/Second
• Kilobytes/Second
• Megabytes/Second
• Gigabytes/Second
• Terabytes/Second
• Bits/Second
• Kilobits/Second
• Megabits/Second
• Gigabits/Second
• Terabits/Second
Options API Version 2010-08-01 93
Amazon CloudWatch Command Line Reference
Name Description
• Count/Second
• None
Default: n/a
Required: No
--insufficient-data-actions
 VALUE1,VALUE2,VALUE3...
The actions (up to ﬁve) to execute when this alarm 
transitions into an INSUFFICIENT_DATA state from 
any other state. Each action is speciﬁed as an Amazon 
Resource Name (ARN).
Type: String
Valid values: A valid ARN identiﬁer.
Default: n/a
Required: No
Common options
Name Description
--aws-credential-file  VALUE The location of the ﬁle with your AWS credentia 
ls. You can set this value using the environment 
variable AWS_CREDENTIAL_FILE . If you deﬁne the 
environment variable or you provide the path to the 
credential ﬁle, the ﬁle must exist or the request fails. 
All CloudWatch requests must be signed using your 
access key ID and secret access key.
Type: String
Valid values: A valid path to a ﬁle containing your 
access key ID and secret access key.
Common options API Version 2010-08-01 94
Amazon CloudWatch Command Line Reference
Name Description
Default: Uses the environment variable AWS_CREDE 
NTIAL_FILE , if set.
-C, --ec2-cert-file-path
VALUE
The location of your EC2 certiﬁcate ﬁle for signing 
requests. You can use the environment variable
EC2_CERT to specify this value.
Type: String
Valid values: A valid ﬁle path to the PEM ﬁle 
provided by Amazon EC2 or AWS Identity and Access 
Management.
Default: Uses the environment variable EC2_CERT, if 
set.
--connection-timeout  VALUE The connection timeout value, in seconds.
Type: Integer
Valid values: Any positive number.
Default: 30
--delimiter  VALUE The delimiter to use when displaying delimited (long) 
results.
Type: String
Valid values: Any string.
Default: Comma (,)
Common options API Version 2010-08-01 95
Amazon CloudWatch Command Line Reference
Name Description
--headers If you are displaying tabular or delimited results, 
include the column headers. If you are showing XML 
results, return the HTTP headers from the service 
request, if applicable.
Type: Flag
Valid values: When present, shows headers.
Default: The --headers  option is oﬀ by default.
-I, --access-key-id  VALUE The access key ID that will be used, in conjunction with 
the secret key, to sign the request. This must be used 
in conjunction with --secret-key, otherwise the option 
is ignored. All requests to CloudWatch must be signed, 
otherwise the request is rejected.
Type: String
Valid values: A valid access key ID.
Default: None
Common options API Version 2010-08-01 96
Amazon CloudWatch Command Line Reference
Name Description
-K, --ec2-private-key-file-
path  VALUE
The private key that will be used to sign the request. 
Using public/private keys causes the CLI to use SOAP. 
The request is signed with a public certiﬁcate and 
private key. This parameter must be used in conjuncti 
on with EC2_CERT, otherwise the value is ignored. 
The value of the environment variable EC2_PRIVA 
TE_KEY  will be used if it is set, and this option is 
not speciﬁed. This option is ignored if the environme 
nt variable AWS_CREDENTIAL_FILE  is set, or --
aws-credentials-file  is used. All requests to 
CloudWatch must be signed, otherwise the request is 
rejected.
Type: String
Valid values: The path to a valid ASN.1 private key.
Default: None
--region VALUE The region requests are directed to. You can use the 
environment variable EC2_REGION  to specify the 
value. The region is used to create the URL used to 
call CloudWatch, and must be a valid Amazon Web 
Services (AWS) region.
Type: String
Valid values: Any AWS region, for example, us-east-1.
Default: us-east-1, unless the EC2_REGION
environment variable is set.
Common options API Version 2010-08-01 97
Amazon CloudWatch Command Line Reference
Name Description
S, --secret-key  VALUE The secret access key that will be used to sign the 
request, in conjunction with an access key ID. This 
parameter must be used in conjunction with --
access-key-id , otherwise this option is ignored.
Type: String
Valid values: Your access key ID.
Default: None
--show-empty-fields Shows empty ﬁelds using (nil) as a placeholder to 
indicate that this data was not requested.
Type: Flag
Valid values: None
Default: Empty ﬁelds are not shown by default.
--show-request Displays the URL the CLI uses to call AWS.
Type: Flag
Valid values: None
Default: false
Common options API Version 2010-08-01 98
Amazon CloudWatch Command Line Reference
Name Description
--show-table, --show-long, 
--show-xml, --quiet
Speciﬁes how the results are displayed: in a table, 
delimited (long), XML, or no output (quiet). The --
show-table  display shows a subset of the data in 
ﬁxed column-width form; --show-long  shows all 
of the returned values delimited by a character; --
show-xml  is the raw return from the service; and --
quiet suppresses all standard output. All options are 
mutually exclusive, with the priority --show-table ,
--show-long , --show-xml , and --quiet.
Type: Flag
Valid values: None
Default: --show-table
-U, --url VALUE The URL used to contact CloudWatch. You can set 
this value using the environment variable AWS_CLOUD 
WATCH_URL . This value is used in conjunction with
--region to create the expected URL. This option 
overrides the URL for the service call.
Type: String
Valid values: A valid HTTP or HTTPS URL.
Default: Uses the value speciﬁed in AWS_CLOUD 
WATCH_URL , if set.
Output
This command creates or updates an alarm associated with the speciﬁed metric.
The Amazon CloudWatch CLI displays errors on stderr.
Output API Version 2010-08-01 99
Amazon CloudWatch Command Line Reference
Examples
Example request
This example creates an alarm that publishes a message to a topic when CPU utilization of an EC2 
instances exceeds 90 percent for three consecutive one minute periods.
mon-put-metric-alarm --alarm-name my-alarm --alarm-description "some desc" \
--metric-name CPUUtilization --namespace AWS/EC2 --statistic Average  --period 60 --
threshold 90 \
--comparison-operator GreaterThanThreshold  --dimensions InstanceId=i-abcdef --
evaluation-periods 3  \
--unit Percent --alarm-actions arn:aws:sns:us-east-1:1234567890:my-topic
Related topics
Download
• Set up the command line interface
Related action
• PutMetricAlarm
Related command
• mon-put-data
mon-set-alarm-state
Description
Temporarily changes the alarm state of the speciﬁed alarm. On the next period, the alarm is set to 
its true state.
Examples API Version 2010-08-01 100
Amazon CloudWatch Command Line Reference
Syntax
mon-set-alarm-state AlarmName --state-reason value --state-value value [--
state-reason-data value] [Common Options]
Options
Name Description
AlarmName The name of the alarm. You can also set this value 
using --alarm-name .
Type: Argument
Valid values: A UTF-8 string.
Default: n/a
Required: Yes
--state-reason  VALUE The reason why this alarm was set to this state (human 
readable).
Type: String
Valid values: A UTF-8 string between 1 and 1023 
characters.
Default: n/a
Required: Yes
--state-reason-data  VALUE The reason why this alarm was set to this state. This 
data is intended to be machine-readable JSON.
Type: String
Valid values: A valid machine-readable JSON string 
between 1 and 4000 characters.
Default: n/a
Syntax API Version 2010-08-01 101
Amazon CloudWatch Command Line Reference
Name Description
Required: No
--state-value   VALUE The state the alarm should be set to.
Type: Enumeration
Valid values: ALARM, OK or INSUFFICIENT_DATA
Default: n/a
Required: Yes
Common options
Name Description
--aws-credential-file  VALUE The location of the ﬁle with your AWS credentia 
ls. You can set this value using the environment 
variable AWS_CREDENTIAL_FILE . If you deﬁne the 
environment variable or you provide the path to the 
credential ﬁle, the ﬁle must exist or the request fails. 
All CloudWatch requests must be signed using your 
access key ID and secret access key.
Type: String
Valid values: A valid path to a ﬁle containing your 
access key ID and secret access key.
Default: Uses the environment variable AWS_CREDE 
NTIAL_FILE , if set.
-C, --ec2-cert-file-path
VALUE
The location of your EC2 certiﬁcate ﬁle for signing 
requests. You can use the environment variable
EC2_CERT to specify this value.
Type: String
Common options API Version 2010-08-01 102
Amazon CloudWatch Command Line Reference
Name Description
Valid values: A valid ﬁle path to the PEM ﬁle 
provided by Amazon EC2 or AWS Identity and Access 
Management.
Default: Uses the environment variable EC2_CERT, if 
set.
--connection-timeout  VALUE The connection timeout value, in seconds.
Type: Integer
Valid values: Any positive number.
Default: 30
--delimiter  VALUE The delimiter to use when displaying delimited (long) 
results.
Type: String
Valid values: Any string.
Default: Comma (,)
--headers If you are displaying tabular or delimited results, 
include the column headers. If you are showing XML 
results, return the HTTP headers from the service 
request, if applicable.
Type: Flag
Valid values: When present, shows headers.
Default: The --headers  option is oﬀ by default.
Common options API Version 2010-08-01 103
Amazon CloudWatch Command Line Reference
Name Description
-I, --access-key-id  VALUE The access key ID that will be used, in conjunction with 
the secret key, to sign the request. This must be used 
in conjunction with --secret-key, otherwise the option 
is ignored. All requests to CloudWatch must be signed, 
otherwise the request is rejected.
Type: String
Valid values: A valid access key ID.
Default: None
-K, --ec2-private-key-file-
path  VALUE
The private key that will be used to sign the request. 
Using public/private keys causes the CLI to use SOAP. 
The request is signed with a public certiﬁcate and 
private key. This parameter must be used in conjuncti 
on with EC2_CERT, otherwise the value is ignored. 
The value of the environment variable EC2_PRIVA 
TE_KEY  will be used if it is set, and this option is 
not speciﬁed. This option is ignored if the environme 
nt variable AWS_CREDENTIAL_FILE  is set, or --
aws-credentials-file  is used. All requests to 
CloudWatch must be signed, otherwise the request is 
rejected.
Type: String
Valid values: The path to a valid ASN.1 private key.
Default: None
Common options API Version 2010-08-01 104
Amazon CloudWatch Command Line Reference
Name Description
--region VALUE The region requests are directed to. You can use the 
environment variable EC2_REGION  to specify the 
value. The region is used to create the URL used to 
call CloudWatch, and must be a valid Amazon Web 
Services (AWS) region.
Type: String
Valid values: Any AWS region, for example, us-east-1.
Default: us-east-1, unless the EC2_REGION
environment variable is set.
S, --secret-key  VALUE The secret access key that will be used to sign the 
request, in conjunction with an access key ID. This 
parameter must be used in conjunction with --
access-key-id , otherwise this option is ignored.
Type: String
Valid values: Your access key ID.
Default: None
--show-empty-fields Shows empty ﬁelds using (nil) as a placeholder to 
indicate that this data was not requested.
Type: Flag
Valid values: None
Default: Empty ﬁelds are not shown by default.
Common options API Version 2010-08-01 105
Amazon CloudWatch Command Line Reference
Name Description
--show-request Displays the URL the CLI uses to call AWS.
Type: Flag
Valid values: None
Default: false
--show-table, --show-long, 
--show-xml, --quiet
Speciﬁes how the results are displayed: in a table, 
delimited (long), XML, or no output (quiet). The --
show-table  display shows a subset of the data in 
ﬁxed column-width form; --show-long  shows all 
of the returned values delimited by a character; --
show-xml  is the raw return from the service; and --
quiet suppresses all standard output. All options are 
mutually exclusive, with the priority --show-table ,
--show-long , --show-xml , and --quiet.
Type: Flag
Valid values: None
Default: --show-table
-U, --url VALUE The URL used to contact CloudWatch. You can set 
this value using the environment variable AWS_CLOUD 
WATCH_URL . This value is used in conjunction with
--region to create the expected URL. This option 
overrides the URL for the service call.
Type: String
Valid values: A valid HTTP or HTTPS URL.
Default: Uses the value speciﬁed in AWS_CLOUD 
WATCH_URL , if set.
Common options API Version 2010-08-01 106
Amazon CloudWatch Command Line Reference
Output
This command temporarily changes an alarm's state and displays OK-Set alarm state value
when the request is successful.
The Amazon CloudWatch CLI displays errors on stderr.
Examples
Example request
This example sets the state of the alarm named my-alarm to OK.
mon-set-alarm-state --alarm-name my-alarm --state OK
Related topics
Download
• Set up the command line interface
Related action
• SetAlarmState
Related command
• mon-describe-alarms
mon-version
Description
Prints the version number of the CLI and API for CloudWatch.
Syntax
mon-version
Output API Version 2010-08-01 107
Amazon CloudWatch Command Line Reference
Output
This command displays the version of the CloudWatch CLI and API.
The Amazon CloudWatch CLI displays errors on stderr.
Examples
Example request
This example shows the CLI and API version.
mon-version
The following is example output.
Amazon CloudWatch CLI version 1.0.12.1 (API 2010-08-01)
Related topics
Download
• Set up the command line interface
Related Command (see --extendedstatistic parameter)
• mon-cmd
Output API Version 2010-08-01 108
Amazon CloudWatch Command Line Reference
Document history
The following table describes the important changes to the Amazon CloudWatch CLI Reference. 
This documentation is associated with the 2010-08-01 release of CloudWatch. This guide was last 
updated on 7 November 2017.
Change Description Release date
Moved the 
Amazon 
CloudWatch CLI 
content from 
the Amazon 
CloudWatch 
User Guide to 
this new guide
Moved the Amazon CloudWatch CLI content 
from the Amazon CloudWatch User Guide to 
this new guide. Updated the examples in the 
Amazon CloudSearch Developer Guide to use 
the AWS CLI, which is a cross-service CLI with a 
simpliﬁed installation, uniﬁed conﬁguration, and 
consistent command line syntax. The AWS CLI is 
supported on Linux/Unix, Windows, and Mac. The 
CLI examples in this guide have been updated to 
use the new AWS CLI.
For information about how to install and 
conﬁgure the new AWS CLI, see Getting Set Up 
with the AWS Command Line Interface in the AWS 
Command Line Interface User Guide.
28 February 2014
The CloudWatc 
h CLI is being 
retired.
As of November 7, 2017, we are no longer 
supporting the CloudWatch command line 
interface with new functionality. It is not available 
for download.
7 November 2017
API Version 2010-08-01 109
