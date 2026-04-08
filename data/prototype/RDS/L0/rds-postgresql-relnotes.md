# Amazon RDS for PostgreSQL Release Notes

## RDS for PostgreSQL release notes

Amazon RDS for PostgreSQL Release Notes
Amazon Relational Database Service
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
## RDS for PostgreSQL release calendar

## RDS for PostgreSQL release calendar for major versions

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Amazon Relational Database Service: Amazon RDS for PostgreSQL 
Release Notes
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
Amazon's trademarks and trade dress may not be used in connection with any product or service 
that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any 
manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are 
the property of their respective owners, who may or may not be aﬃliated with, connected to, or 
sponsored by Amazon.
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Table of Contents
RDS for PostgreSQL release notes ................................................................................................. 1
RDS for PostgreSQL release calendar ............................................................................................ 2
RDS for PostgreSQL release calendar for major versions .................................................................... 2
RDS for PostgreSQL release calendar for minor versions .................................................................... 4
RDS for PostgreSQL release calendar for Extended Support versions .............................................. 7
RDS for PostgreSQL updates .......................................................................................................... 9
PostgreSQL 18 versions ............................................................................................................................ 10
PostgreSQL version 18.3 on Amazon RDS ...................................................................................... 10
PostgreSQL version 18.2 on Amazon RDS ...................................................................................... 10
PostgreSQL version 18.1 on Amazon RDS ...................................................................................... 11
PostgreSQL version 18.0 in the Amazon RDS Preview environment ......................................... 12
PostgreSQL version 18 RC1 in the Amazon RDS Preview environment ..................................... 13
PostgreSQL version 18 Beta 3 in the Amazon RDS Preview environment ................................ 14
PostgreSQL version 18 Beta 2 in the Amazon RDS Preview environment ................................ 15
PostgreSQL version 18 Beta 1 in the Amazon RDS Preview environment ................................ 17
PostgreSQL 17 versions ............................................................................................................................ 18
PostgreSQL version 17.9 on Amazon RDS ...................................................................................... 19
PostgreSQL version 17.8 on Amazon RDS ...................................................................................... 19
PostgreSQL version 17.7 on Amazon RDS ...................................................................................... 20
PostgreSQL version 17.6-R2 on Amazon RDS ................................................................................ 20
PostgreSQL version 17.6 on Amazon RDS ...................................................................................... 20
PostgreSQL version 17.5-R2 on Amazon RDS ................................................................................ 21
PostgreSQL version 17.5 on Amazon RDS ...................................................................................... 21
PostgreSQL version 17.4-R2 on Amazon RDS ................................................................................ 22
PostgreSQL version 17.4 on Amazon RDS ...................................................................................... 22
PostgreSQL version 17.3 on Amazon RDS ...................................................................................... 22
PostgreSQL version 17.2-R3 on Amazon RDS ................................................................................ 23
PostgreSQL version 17.2-R2 on Amazon RDS ................................................................................ 23
PostgreSQL version 17.2 on Amazon RDS ...................................................................................... 23
PostgreSQL version 17.1 on Amazon RDS ...................................................................................... 23
PostgreSQL version 17.0 in the Amazon RDS Preview environment ......................................... 25
PostgreSQL version 17 RC1 in the Amazon RDS Preview environment ..................................... 26
PostgreSQL version 17 Beta 3 in the Amazon RDS Preview environment ................................ 27
PostgreSQL version 17 Beta 2 in the Amazon RDS Preview environment ................................ 28
iii
## RDS for PostgreSQL release calendar for minor versions

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 17 Beta 1 in the Amazon RDS Preview environment ................................ 29
PostgreSQL 16 versions ............................................................................................................................ 29
PostgreSQL version 16.13 on Amazon RDS .................................................................................... 31
PostgreSQL version 16.12 on Amazon RDS .................................................................................... 31
PostgreSQL version 16.11 on Amazon RDS .................................................................................... 31
PostgreSQL version 16.10-R2 on Amazon RDS .............................................................................. 32
PostgreSQL version 16.10 on Amazon RDS .................................................................................... 32
PostgreSQL version 16.9-R2 on Amazon RDS ................................................................................ 33
PostgreSQL version 16.9 on Amazon RDS ...................................................................................... 33
PostgreSQL version 16.8-R2 on Amazon RDS ................................................................................ 33
PostgreSQL version 16.8 on Amazon RDS ...................................................................................... 34
PostgreSQL version 16.7 on Amazon RDS ...................................................................................... 34
PostgreSQL version 16.6-R3 on Amazon RDS ................................................................................ 35
PostgreSQL version 16.6-R2 on Amazon RDS ................................................................................ 35
PostgreSQL version 16.6 on Amazon RDS ...................................................................................... 35
PostgreSQL version 16.5 on Amazon RDS ...................................................................................... 35
PostgreSQL version 16.4-R3 on Amazon RDS ................................................................................ 36
PostgreSQL version 16.4-R2 on Amazon RDS ................................................................................ 36
PostgreSQL version 16.4 on Amazon RDS ...................................................................................... 36
PostgreSQL version 16.3-R4 on Amazon RDS ................................................................................ 37
PostgreSQL version 16.3-R3 on Amazon RDS ................................................................................ 37
PostgreSQL version 16.3-R2 on Amazon RDS ................................................................................ 37
PostgreSQL version 16.3 on Amazon RDS ...................................................................................... 38
PostgreSQL version 16.2-R3 on Amazon RDS ................................................................................ 38
PostgreSQL version 16.2-R2 on Amazon RDS ................................................................................ 39
PostgreSQL version 16.2 on Amazon RDS ...................................................................................... 39
PostgreSQL version 16.1-R2 on Amazon RDS ................................................................................ 40
PostgreSQL version 16.1 on Amazon RDS ...................................................................................... 41
PostgreSQL version 16.0 in the Amazon RDS Preview environment ......................................... 42
PostgreSQL version 16 RC1 in the Amazon RDS Preview environment ..................................... 42
PostgreSQL version 16 Beta 3 in the Amazon RDS Preview environment ................................ 43
PostgreSQL version 16 Beta 2 in the Amazon RDS Preview environment ................................ 44
PostgreSQL version 16 Beta 1 in the Amazon RDS Preview environment ................................ 45
PostgreSQL 15 versions (Some of these versions have reached the end of standard support or 
deprecated.) ................................................................................................................................................. 46
PostgreSQL version 15.17 on Amazon RDS .................................................................................... 47
iv
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 15.16 on Amazon RDS .................................................................................... 47
PostgreSQL version 15.15 on Amazon RDS .................................................................................... 48
PostgreSQL version 15.14-R2 on Amazon RDS .............................................................................. 48
PostgreSQL version 15.14 on Amazon RDS .................................................................................... 49
PostgreSQL version 15.13-R2 on Amazon RDS .............................................................................. 49
PostgreSQL version 15.13 on Amazon RDS .................................................................................... 49
PostgreSQL version 15.12-R2 on Amazon RDS .............................................................................. 50
PostgreSQL version 15.12 on Amazon RDS .................................................................................... 50
PostgreSQL version 15.11 on Amazon RDS .................................................................................... 50
PostgreSQL version 15.10-R3 on Amazon RDS .............................................................................. 51
PostgreSQL version 15.10-R2 on Amazon RDS .............................................................................. 51
PostgreSQL version 15.10 on Amazon RDS .................................................................................... 51
PostgreSQL version 15.9 on Amazon RDS ...................................................................................... 52
PostgreSQL version 15.8-R3 on Amazon RDS ................................................................................ 53
PostgreSQL version 15.8-R2 on Amazon RDS ................................................................................ 53
PostgreSQL version 15.8 on Amazon RDS ...................................................................................... 53
PostgreSQL version 15.7-R4 on Amazon RDS ................................................................................ 53
PostgreSQL version 15.7-R3 on Amazon RDS ................................................................................ 54
PostgreSQL version 15.7-R2 on Amazon RDS ................................................................................ 54
PostgreSQL version 15.7 on Amazon RDS ...................................................................................... 54
PostgreSQL version 15.6-R3 on Amazon RDS (This version has reached the end of 
standard support.) ................................................................................................................................ 55
PostgreSQL version 15.6-R2 on Amazon RDS (This version has reached the end of 
standard support.) ................................................................................................................................ 55
PostgreSQL version 15.6 on Amazon RDS (This version has reached the end of standard 
support.) .................................................................................................................................................. 56
PostgreSQL version 15.5-R2 on Amazon RDS (This version has reached the end of 
standard support.) ................................................................................................................................ 56
PostgreSQL version 15.5 on Amazon RDS (This version has reached the end of standard 
support.) .................................................................................................................................................. 57
PostgreSQL version 15.4-R3 on Amazon RDS (This version has reached the end of 
standard support.) ................................................................................................................................ 58
PostgreSQL version 15.4-R2 on Amazon RDS (This version has reached the end of 
standard support.) ................................................................................................................................ 59
PostgreSQL version 15.4 on Amazon RDS (This version has reached the end of standard 
support.) .................................................................................................................................................. 60
v
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 15.3-R2 on Amazon RDS (Deprecated) ........................................................ 60
PostgreSQL version 15.3 on Amazon RDS (Deprecated) .............................................................. 61
PostgreSQL version 15.2-R2 on Amazon RDS (Deprecated) ........................................................ 62
PostgreSQL version 15.2 on Amazon RDS (Deprecated) .............................................................. 62
PostgreSQL 14 versions ............................................................................................................................ 63
PostgreSQL version 14.22 on Amazon RDS .................................................................................... 65
PostgreSQL version 14.21 on Amazon RDS .................................................................................... 65
PostgreSQL version 14.20-R2 on Amazon RDS .............................................................................. 65
PostgreSQL version 14.20 on Amazon RDS .................................................................................... 66
PostgreSQL version 14.19-R2 on Amazon RDS .............................................................................. 66
PostgreSQL version 14.19 on Amazon RDS .................................................................................... 66
PostgreSQL version 14.18-R2 on Amazon RDS .............................................................................. 67
PostgreSQL version 14.18 on Amazon RDS .................................................................................... 67
PostgreSQL version 14.17-R2 on Amazon RDS .............................................................................. 67
PostgreSQL version 14.17 on Amazon RDS .................................................................................... 68
PostgreSQL version 14.16 on Amazon RDS .................................................................................... 68
PostgreSQL version 14.15-R3 on Amazon RDS .............................................................................. 69
PostgreSQL version 14.15-R2 on Amazon RDS .............................................................................. 69
PostgreSQL version 14.15 on Amazon RDS .................................................................................... 69
PostgreSQL version 14.14 on Amazon RDS .................................................................................... 69
PostgreSQL version 14.13-R3 on Amazon RDS .............................................................................. 70
PostgreSQL version 14.13-R2 on Amazon RDS .............................................................................. 70
PostgreSQL version 14.13 on Amazon RDS .................................................................................... 71
PostgreSQL version 14.12-R4 on Amazon RDS .............................................................................. 71
PostgreSQL version 14.12-R3 on Amazon RDS .............................................................................. 71
PostgreSQL version 14.12-R2 on Amazon RDS .............................................................................. 72
PostgreSQL version 14.12 on Amazon RDS .................................................................................... 72
PostgreSQL version 14.11-R4 on Amazon RDS .............................................................................. 73
PostgreSQL version 14.11-R3 on Amazon RDS .............................................................................. 73
PostgreSQL version 14.11-R2 on Amazon RDS .............................................................................. 74
PostgreSQL version 14.11 on Amazon RDS .................................................................................... 74
PostgreSQL version 14.10-R2 on Amazon RDS .............................................................................. 75
PostgreSQL version 14.10 on Amazon RDS .................................................................................... 76
PostgreSQL version 14.9-R2 on Amazon RDS ................................................................................ 77
PostgreSQL version 14.9 on Amazon RDS ...................................................................................... 77
PostgreSQL version 14.8-R2 on Amazon RDS (Deprecated) ........................................................ 78
vi
## RDS for PostgreSQL release calendar for Extended Support versions

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 14.8 on Amazon RDS (Deprecated) .............................................................. 78
PostgreSQL version 14.7 on Amazon RDS (Deprecated) .............................................................. 79
PostgreSQL version 14.6 on Amazon RDS (Deprecated) .............................................................. 79
PostgreSQL version 14.5 on Amazon RDS (Deprecated) .............................................................. 80
PostgreSQL version 14.4 on Amazon RDS (Deprecated) .............................................................. 81
PostgreSQL version 14.3 on Amazon RDS (Deprecated) .............................................................. 81
PostgreSQL version 14.2 on Amazon RDS (Deprecated) .............................................................. 82
PostgreSQL version 14.1 on Amazon RDS (Deprecated) .............................................................. 82
PostgreSQL 13 versions ............................................................................................................................ 83
PostgreSQL version 13.23-R2 on Amazon RDS .............................................................................. 84
PostgreSQL version 13.23 on Amazon RDS .................................................................................... 85
PostgreSQL version 13.22-R2 on Amazon RDS .............................................................................. 85
PostgreSQL version 13.22 on Amazon RDS .................................................................................... 85
PostgreSQL version 13.21-R2 on Amazon RDS .............................................................................. 85
PostgreSQL version 13.21 on Amazon RDS .................................................................................... 86
PostgreSQL version 13.20-R2 on Amazon RDS .............................................................................. 86
PostgreSQL version 13.20 on Amazon RDS .................................................................................... 87
PostgreSQL version 13.19 on Amazon RDS .................................................................................... 87
PostgreSQL version 13.18-R3 on Amazon RDS .............................................................................. 87
PostgreSQL version 13.18-R2 on Amazon RDS .............................................................................. 88
PostgreSQL version 13.18 on Amazon RDS .................................................................................... 88
PostgreSQL version 13.17 on Amazon RDS .................................................................................... 88
PostgreSQL version 13.16-R3 on Amazon RDS .............................................................................. 89
PostgreSQL version 13.16-R2 on Amazon RDS .............................................................................. 89
PostgreSQL version 13.16 on Amazon RDS .................................................................................... 89
PostgreSQL version 13.15-R4 on Amazon RDS .............................................................................. 90
PostgreSQL version 13.15-R3 on Amazon RDS .............................................................................. 90
PostgreSQL version 13.15-R2 on Amazon RDS .............................................................................. 90
PostgreSQL version 13.15 on Amazon RDS .................................................................................... 91
PostgreSQL version 13.14-R4 on Amazon RDS .............................................................................. 92
PostgreSQL version 13.14-R3 on Amazon RDS .............................................................................. 92
PostgreSQL version 13.14-R2 on Amazon RDS .............................................................................. 92
PostgreSQL version 13.14 on Amazon RDS .................................................................................... 93
PostgreSQL version 13.13-R2 on Amazon RDS .............................................................................. 93
PostgreSQL version 13.13 on Amazon RDS .................................................................................... 94
PostgreSQL version 13.12-R2 on Amazon RDS .............................................................................. 95
vii
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 13.12 on Amazon RDS .................................................................................... 95
PostgreSQL version 13.11-R2 on Amazon RDS .............................................................................. 96
PostgreSQL version 13.11 on Amazon RDS .................................................................................... 96
PostgreSQL version 13.10 on Amazon RDS (Deprecated) ............................................................ 97
PostgreSQL version 13.9 on Amazon RDS (Deprecated) .............................................................. 97
PostgreSQL version 13.8 on Amazon RDS (Deprecated) .............................................................. 98
PostgreSQL version 13.7 on Amazon RDS (Deprecated) .............................................................. 99
PostgreSQL version 13.6 on Amazon RDS (Deprecated) .............................................................. 99
PostgreSQL version 13.5 on Amazon RDS (Deprecated) .............................................................. 99
PostgreSQL version 13.4 on Amazon RDS (Deprecated) ............................................................ 100
PostgreSQL version 13.3 on Amazon RDS (Deprecated) ............................................................ 100
PostgreSQL version 13.2 on Amazon RDS (Deprecated) ............................................................ 101
PostgreSQL version 13.1 on Amazon RDS (Deprecated) ............................................................ 101
PostgreSQL 12 versions (Some of these versions have reached the end of standard support or 
deprecated.) ............................................................................................................................................... 102
PostgreSQL version 12.22-R3 on Amazon RDS (This version has reached the end of 
standard support.) .............................................................................................................................. 103
PostgreSQL version 12.22-R2 on Amazon RDS (This version has reached the end of 
standard support.) .............................................................................................................................. 103
PostgreSQL version 12.22 on Amazon RDS (This version has reached the end of standard 
support.) ............................................................................................................................................... 103
PostgreSQL version 12.21 on Amazon RDS (Deprecated) .......................................................... 103
PostgreSQL version 12.20-R3 on Amazon RDS (Deprecated) ................................................... 104
PostgreSQL version 12.20-R2 on Amazon RDS (Deprecated) ................................................... 105
PostgreSQL version 12.20 on Amazon RDS (Deprecated) .......................................................... 105
PostgreSQL version 12.19-R4 on Amazon RDS (Deprecated) ................................................... 105
PostgreSQL version 12.19-R3 on Amazon RDS (Deprecated) ................................................... 105
PostgreSQL version 12.19-R2 on Amazon RDS (Deprecated) ................................................... 106
PostgreSQL version 12.19 on Amazon RDS (Deprecated) .......................................................... 106
PostgreSQL version 12.18-R4 on Amazon RDS (Deprecated) ................................................... 107
PostgreSQL version 12.18-R3 on Amazon RDS (Deprecated) ................................................... 107
PostgreSQL version 12.18-R2 on Amazon RDS (Deprecated) ................................................... 108
PostgreSQL version 12.18 on Amazon RDS (Deprecated) .......................................................... 108
PostgreSQL version 12.17-R2 on Amazon RDS (Deprecated) ................................................... 109
PostgreSQL version 12.17 on Amazon RDS (Deprecated) .......................................................... 109
PostgreSQL version 12.16-R2 on Amazon RDS (Deprecated) ................................................... 110
viii
## RDS for PostgreSQL updates

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 12.16 on Amazon RDS (Deprecated) .......................................................... 111
PostgreSQL version 12.15 on Amazon RDS (Deprecated) .......................................................... 111
PostgreSQL version 12.14 on Amazon RDS (Deprecated) .......................................................... 112
PostgreSQL version 12.13 on Amazon RDS (Deprecated) .......................................................... 112
PostgreSQL version 12.12 on Amazon RDS (Deprecated) .......................................................... 113
PostgreSQL version 12.11 on Amazon RDS (Deprecated) .......................................................... 113
PostgreSQL version 12.10 on Amazon RDS (Deprecated) .......................................................... 114
PostgreSQL version 12.9 on Amazon RDS (Deprecated) ............................................................ 114
PostgreSQL version 12.8 on Amazon RDS (Deprecated) ............................................................ 114
PostgreSQL version 12.7 on Amazon RDS (Deprecated) ............................................................ 115
PostgreSQL version 12.6 on Amazon RDS (Deprecated) ............................................................ 115
PostgreSQL version 12.5 on Amazon RDS (Deprecated) ............................................................ 116
PostgreSQL version 12.4 on Amazon RDS (Deprecated) ............................................................ 116
PostgreSQL version 12.3 on Amazon RDS (Deprecated) ............................................................ 116
PostgreSQL version 12.2 on Amazon RDS (Deprecated) ............................................................ 117
PostgreSQL 11 versions (Some of these versions have reached the end of standard support or 
deprecated.) ............................................................................................................................................... 117
PostgreSQL version 11.22-R2 on Amazon RDS (This version has reached the end of 
standard support.) .............................................................................................................................. 118
PostgreSQL version 11.22 on Amazon RDS (This version has reached the end of standard 
support.) ............................................................................................................................................... 119
PostgreSQL version 11.21 on Amazon RDS (Deprecated) .......................................................... 119
PostgreSQL version 11.20 on Amazon RDS (Deprecated) .......................................................... 120
PostgreSQL version 11.19 on Amazon RDS (Deprecated) .......................................................... 121
PostgreSQL version 11.18 on Amazon RDS (Deprecated) .......................................................... 121
PostgreSQL version 11.17 on Amazon RDS (Deprecated) .......................................................... 122
PostgreSQL version 11.16 on Amazon RDS (Deprecated) .......................................................... 122
PostgreSQL version 11.15 on Amazon RDS (Deprecated) .......................................................... 122
PostgreSQL version 11.14 on Amazon RDS (Deprecated) .......................................................... 123
PostgreSQL version 11.13 on Amazon RDS (Deprecated) .......................................................... 123
PostgreSQL version 11.12 on Amazon RDS (Deprecated) .......................................................... 123
PostgreSQL version 11.11 on Amazon RDS (Deprecated) .......................................................... 124
PostgreSQL version 11.10 on Amazon RDS (Deprecated) .......................................................... 124
PostgreSQL version 11.9 on Amazon RDS (Deprecated) ............................................................ 124
PostgreSQL version 11.8 on Amazon RDS (Deprecated) ............................................................ 124
PostgreSQL version 11.7 on Amazon RDS (Deprecated) ............................................................ 125
ix
## PostgreSQL 18 versions

## PostgreSQL version 18.3 on Amazon RDS

## PostgreSQL version 18.2 on Amazon RDS

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 11.6 on Amazon RDS (Deprecated) ............................................................ 125
PostgreSQL version 11.5 on Amazon RDS (Deprecated) ............................................................ 125
PostgreSQL version 11.4 on Amazon RDS (Deprecated) ............................................................ 126
PostgreSQL version 11.2 on Amazon RDS (Deprecated) ............................................................ 126
PostgreSQL version 11.1 on Amazon RDS (Deprecated) ............................................................ 126
PostgreSQL 10 versions (Deprecated) ................................................................................................. 128
PostgreSQL version 10.23 on Amazon RDS (Deprecated) .......................................................... 129
PostgreSQL version 10.22 on Amazon RDS (Deprecated) .......................................................... 130
PostgreSQL version 10.21 on Amazon RDS (Deprecated) .......................................................... 130
PostgreSQL version 10.20 on Amazon RDS (Deprecated) .......................................................... 130
PostgreSQL version 10.19 on Amazon RDS (Deprecated) .......................................................... 131
PostgreSQL version 10.18 on Amazon RDS (Deprecated) .......................................................... 131
PostgreSQL version 10.17 on Amazon RDS (Deprecated) .......................................................... 131
PostgreSQL version 10.16 on Amazon RDS (Deprecated) .......................................................... 132
PostgreSQL version 10.15 on Amazon RDS (Deprecated) .......................................................... 132
PostgreSQL version 10.14 on Amazon RDS (Deprecated) .......................................................... 132
PostgreSQL version 10.13 on Amazon RDS (Deprecated) .......................................................... 132
PostgreSQL version 10.12 on Amazon RDS (Deprecated) .......................................................... 133
PostgreSQL version 10.11 on Amazon RDS (Deprecated) .......................................................... 133
PostgreSQL version 10.10 on Amazon RDS (Deprecated) .......................................................... 133
PostgreSQL version 10.9 on Amazon RDS (Deprecated) ............................................................ 133
PostgreSQL version 10.7 on Amazon RDS (Deprecated) ............................................................ 134
PostgreSQL version 10.6 on Amazon RDS (Deprecated) ............................................................ 134
PostgreSQL version 10.5 on Amazon RDS (Deprecated) ............................................................ 135
PostgreSQL version 10.4 on Amazon RDS (Deprecated) ............................................................ 135
PostgreSQL version 10.3 on Amazon RDS (Deprecated) ............................................................ 136
PostgreSQL version 10.1 on Amazon RDS (Deprecated) ............................................................ 137
PostgreSQL 9.6 versions (Deprecated) ................................................................................................ 138
PostgreSQL version 9.6.24 on Amazon RDS (Deprecated) ......................................................... 139
PostgreSQL version 9.6.23 on Amazon RDS (Deprecated) ......................................................... 139
PostgreSQL version 9.6.22 on Amazon RDS (Deprecated) ......................................................... 139
PostgreSQL version 9.6.21 on Amazon RDS (Deprecated) ......................................................... 140
PostgreSQL version 9.6.20 on Amazon RDS (Deprecated) ......................................................... 140
PostgreSQL version 9.6.19 on Amazon RDS (Deprecated) ......................................................... 140
PostgreSQL version 9.6.18 on Amazon RDS (Deprecated) ......................................................... 140
PostgreSQL version 9.6.17 on Amazon RDS (Deprecated) ......................................................... 141
x
## PostgreSQL version 18.1 on Amazon RDS

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 9.6.16 on Amazon RDS (Deprecated) ......................................................... 141
PostgreSQL version 9.6.15 on Amazon RDS (Deprecated) ......................................................... 141
PostgreSQL version 9.6.14 on Amazon RDS (Deprecated) ......................................................... 141
PostgreSQL version 9.6.12 on Amazon RDS (Deprecated) ......................................................... 141
PostgreSQL version 9.6.11 on Amazon RDS (Deprecated) ......................................................... 141
PostgreSQL version 9.6.10 on Amazon RDS (Deprecated) ......................................................... 142
PostgreSQL version 9.6.9 on Amazon RDS (Deprecated) ........................................................... 142
PostgreSQL version 9.6.8 on Amazon RDS (Deprecated) ........................................................... 143
PostgreSQL version 9.6.6 on Amazon RDS (Deprecated) ........................................................... 143
PostgreSQL version 9.6.5 on Amazon RDS (Deprecated) ........................................................... 144
PostgreSQL version 9.6.3 on Amazon RDS (Deprecated) ........................................................... 144
PostgreSQL version 9.6.2 on Amazon RDS (Deprecated) ........................................................... 145
PostgreSQL version 9.6.1 on Amazon RDS (Deprecated) ........................................................... 145
Deprecation of PostgreSQL 10 ............................................................................................................. 146
Deprecation of PostgreSQL 9.6 ............................................................................................................ 147
Amazon RDS Extended Support updates ................................................................................... 148
Amazon RDS Extended Support for PostgreSQL 12 ........................................................................ 148
Amazon RDS Extended Support version 12.22-RDS.20251114 ................................................ 148
Amazon RDS Extended Support version 12.22-RDS.20250814 ................................................ 148
Amazon RDS Extended Support version 12.22-RDS.20250508 ................................................ 149
Amazon RDS Extended Support version 12.22-RDS.20250220 ................................................ 149
Amazon RDS Extended Support for PostgreSQL 11 ........................................................................ 149
Amazon RDS Extended Support version 11.22-RDS.20251114 ................................................ 149
Amazon RDS Extended Support version 11.22-RDS.20250814 ................................................ 150
Amazon RDS Extended Support version 11.22-RDS.20250508 ................................................ 150
Amazon RDS Extended Support version 11.22-RDS.20250220 ................................................ 150
Amazon RDS Extended Support version 11.22-RDS.20241121 ................................................ 151
Amazon RDS Extended Support version 11.22-RDS.20240808 ................................................ 151
Amazon RDS Extended Support version 11.22-RDS.20240509 ................................................ 151
Amazon RDS Extended Support version 11.22-RDS.20240418 ................................................ 151
Extension versions ....................................................................................................................... 153
Extensions for PostgreSQL 18 .............................................................................................................. 154
Extensions for PostgreSQL 17 .............................................................................................................. 161
Extensions for PostgreSQL 16 .............................................................................................................. 168
Extensions for PostgreSQL 15 .............................................................................................................. 176
Extensions for PostgreSQL 14 .............................................................................................................. 183
xi
## PostgreSQL version 18.0 in the Amazon RDS Preview environment

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extensions for PostgreSQL 13 .............................................................................................................. 190
Extensions for PostgreSQL 12 .............................................................................................................. 197
Extensions for PostgreSQL 11 .............................................................................................................. 202
Extensions for PostgreSQL 10 .............................................................................................................. 207
Extensions for PostgreSQL 9.6 ............................................................................................................. 211
Document history ........................................................................................................................ 216
Earlier updates .......................................................................................................................................... 222
xii
## PostgreSQL version 18 RC1 in the Amazon RDS Preview environment

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Release notes for Amazon Relational Database Service 
(Amazon RDS) for PostgreSQL
The Amazon RDS for PostgreSQL release notes provide details about the PostgreSQL versions and 
extensions that are available for Amazon RDS.
Topics
• Release calendars for Amazon RDS for PostgreSQL
• Amazon RDS for PostgreSQL updates
• Amazon RDS Extended Support updates
• Extension versions for Amazon RDS for PostgreSQL
1
## PostgreSQL version 18 Beta 3 in the Amazon RDS Preview environment

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Release calendars for Amazon RDS for PostgreSQL
Release calendar for Amazon RDS for PostgreSQL major 
versions
RDS for PostgreSQL major versions are available under standard support at least until community 
end of life for the corresponding community version. You can continue running a major version 
past its RDS end of standard support date for a fee. For more information, see Using Amazon RDS 
Extended support and Amazon RDS pricing.
You can use the following dates to plan your testing and upgrade cycles.
Note
Dates with only a month and a year are approximate and are updated with an exact date 
when it's known.
You can also view information about support dates for major engine versions by using 
the AWS CLI or the RDS API. For more information, see Viewing support dates for engine 
versions in Amazon RDS Extended Support.
PostgreSQ 
L major 
version
Community 
release 
date
RDS 
release 
date
Community 
end of 
life date
RDS 
end of 
standard 
support 
date
RDS 
start of 
Extended 
Support 
year 1 
pricing
RDS 
start of 
Extended 
Support 
year 3 
pricing
RDS 
end of 
Extended 
Support 
date
PostgreSQ 
L 18
13 
November 
2025
14 
November 
2025
November 
2030
28 
February 
2031
1 March 
2032
1 March 
2033
28 
February 
2034
PostgreSQ 
L 17
14 
November 
2024
14 
November 
2024
November 
2029
28 
February 
2030
1 March 
2030
1 March 
2032
28 
February 
2033
RDS for PostgreSQL release calendar for major versions 2
## PostgreSQL version 18 Beta 2 in the Amazon RDS Preview environment

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQ 
L major 
version
Community 
release 
date
RDS 
release 
date
Community 
end of 
life date
RDS 
end of 
standard 
support 
date
RDS 
start of 
Extended 
Support 
year 1 
pricing
RDS 
start of 
Extended 
Support 
year 3 
pricing
RDS 
end of 
Extended 
Support 
date
PostgreSQ 
L 16
9 
November 
2023
20 
November 
2023
November 
2028
28 
February 
2029
1 March 
2029
1 March 
2031
29 
February 
2032
PostgreSQ 
L 15
13 
October 
2022
27 
February 
2023
November 
2027
29 
February 
2028
1 March 
2028
1 March 
2030
28 
February 
2031
PostgreSQ 
L 14
30 
September 
2021
3 
February 
2022
12 
November 
2026
28 
February 
2027
1 March 
2027
1 March 
2029
28 
February 
2030
PostgreSQ 
L 13
24 
September 
2020
24 
February 
2021
November 
2025
28 
February 
2026
1 March 
2026
1 March 
2028
28 
February 
2029
PostgreSQ 
L 12
3 
October 
2019
31 March 
2020
14 
November 
2024
28 
February 
2025
1 March 
2025
1 March 
2027
29 
February 
2028
PostgreSQ 
L 11
18 
October 
2018
13 March 
2019
9 
November 
2023
29 
February 
2024
1 April 
2024
1 April 
2026
31 March 
2027
PostgreSQ 
L 10
Deprecate 
d
5 
October 
2017
27 
February 
2018
10 
November 
2022
April 
2023
N/A N/A N/A
RDS for PostgreSQL release calendar for major versions 3
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQ 
L major 
version
Community 
release 
date
RDS 
release 
date
Community 
end of 
life date
RDS 
end of 
standard 
support 
date
RDS 
start of 
Extended 
Support 
year 1 
pricing
RDS 
start of 
Extended 
Support 
year 3 
pricing
RDS 
end of 
Extended 
Support 
date
PostgreSQ 
L 9.6
Deprecate 
d
26 
September 
2016
11 
November 
2016
11 
November 
2021
30 April 
2022
N/A N/A N/A
Release calendar for Amazon RDS for PostgreSQL minor 
versions
Amazon RDS currently supports the following minor versions of PostgreSQL.
Note
Minor versions can reach the end of standard support before the corresponding major 
versions. For example, minor version 14.9 will reach its end of standard support in March 
2025, while major version 14 will reach its end of standard support in February 2027. 
Amazon RDS will support additional 14.* minor versions that the PostgreSQL community 
releases between these dates.
Dates with only a month and a year are approximate, and will be updated with the exact 
date when it is known.
PostgreSQL minor 
engine version
Community release 
date
RDS release date RDS end of standard 
support date
18.1 13 November 2025 14 November 2022 March 2027
18.2** 12 February 2026 12 February 2026 March 2027
RDS for PostgreSQL release calendar for minor versions 4
## PostgreSQL version 18 Beta 1 in the Amazon RDS Preview environment

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL minor 
engine version
Community release 
date
RDS release date RDS end of standard 
support date
18.3 26 February 2026 27 February 2026 March 2027
17.9 26 February 2026 27 February 2026 March 2027
17.8** 12 February 2026 12 February 2026 March 2027
17.7 13 November 2025 13 November 2025 March 2027
17.6 14 August 2025 14 August 2025 September 2026
17.5 08 May 2025 08 May 2025 September 2026
17.4 20 February 2025 21 February 2025 May 2026
17.3** 13 February 2025 13 February 2025 May 2026
17.2 21 November 2024 21 November 2024 May 2026
17.1** 14 November 2024 14 November 2024 May 2026
16.13 26 February 2026 27 February 2026 March 2027
16.12** 12 February 2026 12 February 2026 March 2027
16.11 13 November 2025 13 November 2025 March 2027
16.10 14 August 2025 14 August 2025 September 2026
16.9 08 May 2025 08 May 2025 September 2026
16.8 20 February 2025 21 February 2025 May 2026
16.7** 13 February 2025 13 February 2025 May 2026
16.6 21 November 2024 21 November 2024 May 2026
16.5** 14 November 2024 14 November 2024 May 2026
15.17 26 February 2026 27 February 2026 March 2027
RDS for PostgreSQL release calendar for minor versions 5
## PostgreSQL 17 versions

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL minor 
engine version
Community release 
date
RDS release date RDS end of standard 
support date
15.16** 12 February 2026 12 February 2026 March 2027
15.15 13 November 2025 13 November 2025 March 2027
15.14 14 August 2025 14 August 2025 September 2026
15.13 08 May 2025 08 May 2025 September 2026
15.12 20 February 2025 21 February 2025 May 2026
15.11** 13 February 2025 13 February 2025 May 2026
15.10 21 November 2024 21 November 2024 May 2026
15.9** 14 November 2024 14 November 2024 May 2026
14.22 26 February 2026 27 February 2026 March 2027
14.21** 12 February 2026 12 February 2026 March 2027
14.20 13 November 2025 13 November 2025 February 2027
14.19 14 August 2025 14 August 2025 September 2026
14.18 08 May 2025 08 May 2025 September 2026
14.17 20 February 2025 21 February 2025 May 2026
14.16** 13 February 2025 13 February 2025 May 2026
14.15 21 November 2024 21 November 2024 May 2026
14.14** 14 November 2024 14 November 2024 May 2026
13.23* 13 November 2025 13 November 2025 28 February 2026
13.22 14 August 2025 14 August 2025 28 February 2026
13.21 08 May 2025 08 May 2025 28 February 2026
RDS for PostgreSQL release calendar for minor versions 6
## PostgreSQL version 17.9 on Amazon RDS

## PostgreSQL version 17.8 on Amazon RDS

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL minor 
engine version
Community release 
date
RDS release date RDS end of standard 
support date
13.20 20 February 2025 21 February 2025 28 February 2026
13.19** 13 February 2025 13 February 2025 28 February 2026
13.18 21 November 2024 21 November 2024 28 February 2026
13.17** 14 November 2024 14 November 2024 28 February 2026
12.22* 21 November 2024 21 November 2024 28 February 2025
11.22* 09 November 2023 17 November 2023 29 February 2024
* Amazon RDS Extended Support eligible minor engine version. For more information, see Using 
Amazon RDS Extended Support.
** RDS for PostgreSQL versions marked with this symbol will be set to NO_CREATE status. You 
won't be able to create new DB instances using these versions.
Release calendar for Amazon RDS Extended Support for RDS 
for PostgreSQL
Note
Amazon RDS will continue to release updates for the Extended Support engine versions. 
You can use the Extended Support release calendar to plan your testing and upgrade 
cycles.
Dates with only a month and a year are approximate, and will be updated with the exact 
date when it’s known.
Minor engine version Community release 
date
RDS release date RDS end of Extended 
Support date
12.22-rds.20250814* Not applicable 29 September 2025 30 September 2026
RDS for PostgreSQL release calendar for Extended Support versions 7
## PostgreSQL version 17.7 on Amazon RDS

## PostgreSQL version 17.6-R2 on Amazon RDS

## PostgreSQL version 17.6 on Amazon RDS

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Minor engine version Community release 
date
RDS release date RDS end of Extended 
Support date
12.22-rds.20250508* Not applicable 4 June 2025 30 September 2026
12.22-rds.20250220* Not applicable 3 April 2025 30 September 2026
11.22-rds.20250814* Not applicable 29 September 2025 30 September 2026
11.22-rds.20250508* Not applicable 4 June 2025 30 September 2026
11.22-rds.20250220* Not applicable 3 April 2025 30 September 2026
11.22-RDS.20241121 
*
Not applicable 12 December 2024 31 March 2026
11.22-RDS.20240808 
*
Not applicable 26 August 2024 30 September 2025
11.22-RDS.20240509 
*
Not applicable 10 June 2024 30 September 2025
11.22-RDS.20240418 
*
Not applicable 14 May 2024 30 September 2025
* PostgreSQL Community retired major version 11 and won't be releasing new minor versions. 
Amazon RDS released this minor version with critical security patches and bug ﬁxes for PostgreSQL 
databases that are covered under Amazon RDS Extended Support. For more information about 
these minor versions, see Amazon RDS Extended Support updates. For more information about 
Amazon RDS Extended Support, see Using Amazon RDS Extended Support.
RDS for PostgreSQL release calendar for Extended Support versions 8
## PostgreSQL version 17.5-R2 on Amazon RDS

## PostgreSQL version 17.5 on Amazon RDS

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Amazon RDS for PostgreSQL updates
Amazon RDS supports DB instances running several versions of PostgreSQL. You can specify any 
currently available PostgreSQL version when creating a new DB instance. You can specify the major 
version (such as PostgreSQL 10) and any available minor version for the speciﬁed major version. 
If no version is speciﬁed, Amazon RDS defaults to an available version, typically the most recent 
version. If a major version is speciﬁed but a minor version isn't, Amazon RDS defaults to a recent 
release of the major version that you speciﬁed.
To see a list of available versions, and also defaults for newly created DB instances, use the
describe-db-engine-versions AWS CLI command. For example, to display the default 
PostgreSQL engine version, use the following command.
aws rds describe-db-engine-versions --default-only --engine postgres
To learn more about versioning policy for RDS for PostgreSQL, see Amazon RDS FAQs. For more 
information about PostgreSQL versions, see Versioning Policy in the PostgreSQL documentation.
Topics
• PostgreSQL 18 versions
• PostgreSQL 17 versions
• PostgreSQL 16 versions
• PostgreSQL 15 versions (Some of these versions have reached the end of standard support or 
deprecated.)
• PostgreSQL 14 versions
• PostgreSQL 13 versions
• PostgreSQL 12 versions (Some of these versions have reached the end of standard support or 
deprecated.)
• PostgreSQL 11 versions (Some of these versions have reached the end of standard support or 
deprecated.)
• PostgreSQL 10 versions (Deprecated)
• PostgreSQL 9.6 versions (Deprecated)
• Deprecation of PostgreSQL 10
9
## PostgreSQL version 17.4-R2 on Amazon RDS

## PostgreSQL version 17.4 on Amazon RDS

## PostgreSQL version 17.3 on Amazon RDS

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Deprecation of PostgreSQL 9.6
PostgreSQL 18 versions
Minor versions
• PostgreSQL version 18.3 on Amazon RDS
• PostgreSQL version 18.2 on Amazon RDS
• PostgreSQL version 18.1 on Amazon RDS
• PostgreSQL version 18.0 in the Amazon RDS Preview environment
• PostgreSQL version 18 RC1 in the Amazon RDS Preview environment
• PostgreSQL version 18 Beta 3 in the Amazon RDS Preview environment
• PostgreSQL version 18 Beta 2 in the Amazon RDS Preview environment
• PostgreSQL version 18 Beta 1 in the Amazon RDS Preview environment
PostgreSQL version 18.3 on Amazon RDS
PostgreSQL version 18.3 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 18.3 release.
PostgreSQL version 18.2 on Amazon RDS
PostgreSQL version 18.2 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 18.2 release.
General enhancements
• Improved stability and reliability for database operations.
• Enhanced data collection capabilities.
• Advanced query performance monitoring: Introduced the pg_stat_monitor extension to provide 
comprehensive query performance insights and help identify performance bottlenecks.
This version also includes the following extension changes:
The following extension was added:
PostgreSQL 18 versions 10
## PostgreSQL version 17.2-R3 on Amazon RDS

## PostgreSQL version 17.2-R2 on Amazon RDS

## PostgreSQL version 17.2 on Amazon RDS

## PostgreSQL version 17.1 on Amazon RDS

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• pg_stat_monitor
• The pgactive extension was updated to version 2.1.7.
• The pglogical extension was updated to version 2.4.6.
• The pg_hint_plan extension was updated to version 1.6.2.
• The orafce extension was updated to version 4.16.3.
• The postgis extension was updated to version 3.6.1.
• The pg_bigm extension was updated to version 1.2-20250903.
• The pg_cron extension was updated to version 1.6.7.
• The hypopg extension was updated to version 1.4.2.
• The tds_fdw extension was updated to version 2.0.5.
• The pg_repack extension was updated to version 1.5.3.
• The pgvector extension was updated to version 0.8.1.
• The mysql_fdw extension was updated to version 2.9.3.
• The oracle_fdw extension was updated to version 2.8.0.
• The roaringbitmap extension was updated to version 1.1.0.
PostgreSQL version 18.1 on Amazon RDS
PostgreSQL 18 contains many new features and enhancements that can be seen in the following 
release documentation, PostgreSQL 18.
The following parameters were updated:
• track_cost_delay_timing default is set to on
• max_active_replication_origins default is set to 20.
• pclient_connection_check_interval default is set to 60000.
• log_connections was updated to reﬂect the new PostgreSQL 18 behavior. The old default 
value of 0 is equivalent to the new default empty value, and the old value of 1 is equivalent to 
specifying all three values of receipt, authentication, and authorization.
• autovacuum_worker_slots,io_workers,io_max_concurrency
The following extensions were added:
PostgreSQL version 18.1 on Amazon RDS 11
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• pgcollection
• roaringbitmap
This version also includes the following extension changes:
• The pgaudit updated to version 18.0
• The pg_cron updated to version 1.6.7
• The pgvector updated to version 0.8.1
• The pg_tle updated to version 1.5.2
• The mysql_fdw updated to version 2.9.3.
• The tds_fdw updated to version 2.0.5.
The following extension supported in RDS for PostgreSQL version 17 isn't supported for RDS for 
PostgreSQL version 18:
• postgis_topology
• plrust
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 18.
PostgreSQL version 18.0 in the Amazon RDS Preview environment
Note
The preview documentation for Amazon RDS PostgreSQL version 18 is subject to change.
PostgreSQL 18 contains many new features and enhancements that can be seen in the following 
release documentation, PostgreSQL 18.
The following extensions were added:
• pglogical
• postgis
• pgrouting
PostgreSQL version 18.0 in the Amazon RDS Preview environment 12
## PostgreSQL version 17.0 in the Amazon RDS Preview environment

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• h3-pg
This version also includes the following extension changes:
• The pg_bigm extension was updated to version v1.2-20250903
The following extension supported in RDS for PostgreSQL version 17 isn't supported for RDS for 
PostgreSQL version 18.0 in preview:
• pgAudit
• plrust
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 18.
PostgreSQL version 18 RC1 in the Amazon RDS Preview environment
PostgreSQL 18 RC1 contains many new features and enhancements that can be seen in the release 
documentation: PostgreSQL 18 RC1 Released!.
The following extensions were added:
• pg_hint_plan
• tds_fdw
• pg_transport
This version also includes the following extension changes:
• The hypopg extension was updated to version 1.4.2
• The pg_repack extension was updated to version 1.5.2
• The pgactive extension was updated to version 2.1.6
The following extensions that are supported in Amazon RDS PostgreSQL version 17 aren't 
supported for Amazon RDS PostgreSQL version 18 Beta 3 in preview:
• address_standardizer
• address_standardizer_data_us
PostgreSQL version 18 RC1 in the Amazon RDS Preview environment 13
## PostgreSQL version 17 RC1 in the Amazon RDS Preview environment

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• h3-pg
• pgAudit
• pglogical
• pgrouting
• plrust
• PostGIS
• postgis_raster
• postgis_tiger_geocoder
• postgis_topology
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 18.
PostgreSQL version 18 Beta 3 in the Amazon RDS Preview environment
PostgreSQL 18 Beta 3 contains many new features and enhancements that can be seen in the 
release documentation: PostgreSQL 18 Beta 3 Released!.
The following modiﬁable parameters were added:
• autovacuum_vacuum_max_threshold
• track_cost_delay_timing
• idle_replication_slot_timeout
• md5_password_warnings
• log_lock_failure
• restrict_nonsystem_relation_kind
• vacuum_truncate
• vacuum_max_eager_freeze_failure_rate
• enable_distinct_reordering
• enable_self_join_elimination
• max_active_replication_origins
• io_max_combine_limit
The following extensions were added:
PostgreSQL version 18 Beta 3 in the Amazon RDS Preview environment 14
## PostgreSQL version 17 Beta 3 in the Amazon RDS Preview environment

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• plv8
• pgactive
The following extensions that are supported in Amazon RDS PostgreSQL version 17 aren't 
supported for Amazon RDS PostgreSQL version 18 Beta 3 in preview:
• address_standardizer
• address_standardizer_data_us
• h3-pg
• pg_hint_plan
• pg_transport
• pgAudit
• pglogical
• pgrouting
• plrust
• PostGIS
• postgis_raster
• postgis_tiger_geocoder
• postgis_topology
• tds_fdw
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 18.
PostgreSQL version 18 Beta 2 in the Amazon RDS Preview environment
PostgreSQL 18 Beta 2 contains many new features and enhancements that can be seen in the 
release documentation: PostgreSQL 18 Beta 2 Released!.
The following loadable module was added in this release:
• pg_overexplain
The following extensions were added in this release:
PostgreSQL version 18 Beta 2 in the Amazon RDS Preview environment 15
## PostgreSQL version 17 Beta 2 in the Amazon RDS Preview environment

Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• pg_tap
• oracle_fdw
• pg_bigm
• pg_partman
• pg_proctab
• pg_repack
• pg_tle
• rdkit
The following extensions that are supported in Amazon RDS PostgreSQL version 17 aren't 
supported for Amazon RDS PostgreSQL version 18 Beta 2 in preview:
• address_standardizer
• address_standardizer_data_us
• h3-pg
• pg_hint_plan
• pg_transport
• pgactive
• pgAudit
• pglogical
• pgrouting
• plrust
• plv8
• PostGIS
• postgis_raster
• postgis_tiger_geocoder
• postgis_topology
• tds_fdw
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 18.
PostgreSQL version 18 Beta 2 in the Amazon RDS Preview environment 16
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 18 Beta 1 in the Amazon RDS Preview environment
PostgreSQL 18 Beta 1 contains many new features and enhancements that can be seen in the 
release documentation: PostgreSQL 18 Beta 1 Released!.
This release includes the following version updates:
• LLVM version updated to 20.1.1
• LZ4 version updated to 1.10.0
• Zstd version updated to 1.5.7
• Zlib version updated to 1.3.1
• AWS-LC version updated to AWS-LC FIPS 3.0
• Kerberos version updated to 1.21.3
• Perl version updated to 5.40.2
• ossp-uuid now uses the e2fs UUID implementation
The following extensions that are supported in Amazon RDS PostgreSQL version 17 aren't 
supported for Amazon RDS PostgreSQL version 18 Beta 1 in preview:
• address_standardizer
• address_standardizer_data_us
• h3-pg
• oracle_fdw
• pg_bigm
• pg_hint_plan
• pg_partman
• pg_proctab
• pg_repack
• pg_tle
• pg_transport
• pgactive
• pgAudit
• pglogical
PostgreSQL version 18 Beta 1 in the Amazon RDS Preview environment 17
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• pgrouting
• pgTAP
• plrust
• pltcl
• plv8
• PostGIS
• postgis_raster
• postgis_tiger_geocoder
• postgis_topology
• rdkit
• tds_fdw
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 18.
PostgreSQL 17 versions
Minor versions
• PostgreSQL version 17.9 on Amazon RDS
• PostgreSQL version 17.8 on Amazon RDS
• PostgreSQL version 17.7 on Amazon RDS
• PostgreSQL version 17.6-R2 on Amazon RDS
• PostgreSQL version 17.6 on Amazon RDS
• PostgreSQL version 17.5-R2 on Amazon RDS
• PostgreSQL version 17.5 on Amazon RDS
• PostgreSQL version 17.4-R2 on Amazon RDS
• PostgreSQL version 17.4 on Amazon RDS
• PostgreSQL version 17.3 on Amazon RDS
• PostgreSQL version 17.2-R3 on Amazon RDS
• PostgreSQL version 17.2-R2 on Amazon RDS
• PostgreSQL version 17.2 on Amazon RDS
PostgreSQL 17 versions 18
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• PostgreSQL version 17.1 on Amazon RDS
• PostgreSQL version 17.0 in the Amazon RDS Preview environment
• PostgreSQL version 17 RC1 in the Amazon RDS Preview environment
• PostgreSQL version 17 Beta 3 in the Amazon RDS Preview environment
• PostgreSQL version 17 Beta 2 in the Amazon RDS Preview environment
• PostgreSQL version 17 Beta 1 in the Amazon RDS Preview environment
PostgreSQL version 17.9 on Amazon RDS
PostgreSQL version 17.9 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 17.9 release.
PostgreSQL version 17.8 on Amazon RDS
PostgreSQL version 17.8 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 17.8 release.
General enhancements
• Improved stability and reliability for database operations.
• Enhanced data collection capabilities.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.7.
• The pglogical extension was updated to version 2.4.6.
• The pg_hint_plan extension was updated to version 1.7.1.
• The orafce extension was updated to version 4.16.3.
• The pg_bigm extension was updated to version 1.2-20250903.
• The pg_cron extension was updated to version 1.6.7.
• The hypopg extension was updated to version 1.4.2.
• The tds_fdw extension was updated to version 2.0.5.
• The pg_repack extension was updated to version 1.5.3.
• The pgvector extension was updated to version 0.8.1.
PostgreSQL version 17.9 on Amazon RDS 19
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The mysql_fdw extension was updated to version 2.9.3.
• The oracle_fdw extension was updated to version 2.8.0.
PostgreSQL version 17.7 on Amazon RDS
PostgreSQL version 17.7 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 17.7 release.
General enhancements
• The pgcollection extension is now available for RDS PostgreSQL version 15.15 and above(16.11 
and 17.7), providing a memory-optimized data type designed for high-performance use inside 
PL/pgSQL functions. A collection stores key-value pairs where each key is a unique text string 
(maximum 32,767 characters) and values can be any PostgreSQL type including composite types, 
with all elements in a collection required to be of the same type. Collections maintain entries 
in creation order and can hold an unlimited number of elements constrained only by available 
database memory, with a maximum persisted size of 1GB when stored as a table column..
This version also includes the following extension changes:
• The pg_tle extension was updated to version 1.5.2.
• The h3-pg extension was updated to version 4.2.3.
PostgreSQL version 17.6-R2 on Amazon RDS
PostgreSQL version 17.6-R2 is now available on Amazon RDS.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 17.6 on Amazon RDS
PostgreSQL version 17.6 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 17.6 release.
General enhancements
PostgreSQL version 17.7 on Amazon RDS 20
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Grant rds_superuser access to pg_wal_pause / pg_wal_replay functions to perform logical 
upgrades and veriﬁcation/validation.
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pg_repack extension was updated to version 1.5.2.
• The oracle_fdw extension was updated to version 2.8.0.
• The pgactive extension was updated to version 2.1.5.
PostgreSQL version 17.5-R2 on Amazon RDS
PostgreSQL version 17.5-R2 is now available on Amazon RDS.
General enhancements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 17.5 on Amazon RDS
PostgreSQL version 17.5 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 17.5 release.
General enhancements
• Fixed for the address_standardizer_data_us extension issue regarding ALTER EXTENSION 
UPDATE failure.
• Changed the Oracle client library version for the oracle_fdw extension on x86 to 19.26.0.0.0.
• Fixed the pgactive extension unable to upgrade issue due to incorrect extension upgrade 
scripts which causes replication to break after engine upgrade.
This version also includes the following extension changes:
PostgreSQL version 17.5-R2 on Amazon RDS 21
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pg_repack extension was updated to version 1.5.1.
• The pglogical extension was updated to version 2.4.5.
• The PgAudit extension was updated to version 17.1.
• The RDKit extension was updated to version 2024_09_6.
PostgreSQL version 17.4-R2 on Amazon RDS
PostgreSQL version 17.4-R2 is now available on Amazon RDS.
Fixes and improvements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 17.4 on Amazon RDS
PostgreSQL version 17.4 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 17.4 release.
PostgreSQL version 17.3 on Amazon RDS
PostgreSQL version 17.3 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 17.3 release.
New features and enhancements.
• In Blue/Green deployments, creating or modifying temporary objects is no longer classiﬁed as 
restricted DDL.
• The postgres_get_av_diag function has been updated to support radix tree optimization on 
PostgreSQL 17. Recommendations are now tailored to account for this new optimization feature.
• Resolved an issue where DVB returned duplicate rows during slow vacuum analysis.
• Resolved CVE RUSTSEC-2024-0421 by upgrading URL Rust crate to 2.5.4. For more information, 
see RUSTSEC-2024-0421.
PostgreSQL version 17.4-R2 on Amazon RDS 22
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Applied Promise.any error allocation ﬁx for V8 9.7.37, PLV8 3.1.10.
This version also includes the following extension changes:.
• The rds_tools extension was updated to 1.9.
• The orafce extension was updated to 4.14.0.
• The pg_cron extension was updated to 1.6.5.
• The rdkit extension was updated to 2024_09_3.
• The pg_active extension was updated to 2.1.4.
• The pg_partman extension was updated to 5.2.4.
• The prefix extension was updated to 1.2.10.
• The PostGIS extension was updated to 3.5.1.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 17.
PostgreSQL version 17.2-R3 on Amazon RDS
PostgreSQL version 17.2-R3 is now available on Amazon RDS.
General enhancements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
PostgreSQL version 17.2-R2 on Amazon RDS
PostgreSQL version 17.2-R2 is now available on Amazon RDS. This release contains ﬁx for PLV8
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 17.2.
PostgreSQL version 17.2 on Amazon RDS
PostgreSQL version 17.2 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 17.2 release.
PostgreSQL version 17.1 on Amazon RDS
PostgreSQL version 17.1 is now available on Amazon RDS. This release contains many new features 
and enhancements that can be seen in the following release documentation, PostgreSQL 17.1.
PostgreSQL version 17.2-R3 on Amazon RDS 23
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
New features
• Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some 
connection slots are reserved for the new rds_reserved role, which is granted to Amazon 
RDS administrative users. The number of reserved connection slots is determined by the
rds.rds_reserved_connections parameter. You may need to adjust the value of the
max_connections parameter to account for the number of Amazon RDS reserved connection 
slots.
The rds_reserved role is a new predeﬁned role created by Amazon RDS. Predeﬁned roles 
and their privileges can't be changed. You can't drop, rename, or modify privileges for these 
predeﬁned roles. Attempting to modify a predeﬁned role results in an error.
• Added vacuum blocker detection to improve autovacuum monitoring. For more information, see
Identify and resolve aggressive vacuum blockers in RDS for PostgreSQL
• Unblocked ALTER TEMP TABLE and DROP TEMP TABLE in Blue/Green replication.
• Added the rds_tools.pg_ls_multixactdir() function for pg_multixact to monitor the 
directory disk space usage.
• Added support for plrust version 1.2.7.
Updated features
• PostGIS was updated to version 3.5.0, and the following dependencies were updated:
• json-c was updated to version 0.18_20240915.
• GDAL was updated to version 3.9.3
• PROJ was updated to version 9.5.0
• PROJ_DATA was updated to version 1.19
• The orafce extension was updated to version 4.13.4.
• The pg_bigm extension was updated to version 1.2_20240606.
• The pg_proctab extension was updated to version 0.0.12.
• The pg_repack extension was updated to version 1.5.1.
• The pgrouting extension was updated to version 3.6.3.
• The pgvector extension was updated to version 0.8.0.
• The rdkit extension was updated to version 2024_09_2(4.6.1).
PostgreSQL version 17.1 on Amazon RDS 24
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The rds_tools extension was updated to version 1.8.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 17.
PostgreSQL version 17.0 in the Amazon RDS Preview environment
Note
The preview documentation for Amazon RDS PostgreSQL version 17 is subject to change.
PostgreSQL 17 contains many new features and enhancements that can be seen in the following 
release documentation, PostgreSQL 17.
New features
• GCC was upgraded to version 12.4.0
• Introduced a new Amazon RDS-speciﬁc parameter, rds.logical_slot_sync_dbname, to 
specify the dbname for the PostgreSQL version 17 logical slots synchronization and failover 
feature.For more information, see Managing logical slot synchronization for RDS for PostgreSQL.
This version also includes the following extension and dependency updates:
• The following PostGIS dependencies were updated:
• gdal was upgraded to version 3.9.2
• PROJ was upgraded to version 9.4.1
• PROJ_DATA was upgraded to version 1.18
• GEOS was upgraded to version 3.13.0
• The oracle_fdw extension was updated to version 2.7.0.
• The orafce extension was updated to version 4.12.0.
• The pg_buffercache extension was updated to version 1.5.
• The pg_cron extension was updated to version 1.6.4.
• The pg_stat_statements extension was updated to version 1.11.
• The pgaudit extension was updated to version 17.0.
PostgreSQL version 17.0 in the Amazon RDS Preview environment 25
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pgvector extension was updated to version 0.7.4.
• The plprofiler extension was updated to version 4.2.5.
• The rds_tools extension was updated to version 1.6.
• The tds_fdw extension was updated to version 2.0.4.
The following extension supported in RDS for PostgreSQL version 16 isn't supported for RDS for 
PostgreSQL version 17.0 in preview:
• plrust
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 17.
PostgreSQL version 17 RC1 in the Amazon RDS Preview environment
Note
The preview documentation for Amazon RDS for PostgreSQL version 17 is subject to 
change.
PostgreSQL 17 RC1 contains many new features and enhancements that can be seen in the 
following release documentation, PostgreSQL 17 RC1 Released!.
New features
• Performance Insights is supported in the preview environment.
New extensions
• The pg_logical extension was added.
This version also includes the following extension updates:
• The address_standardizer extension was updated to version 3.5.0alpha2.
• The address_standardizer_data_us extension was updated to version 3.5.0alpha2.
• The PostGIS extension was updated to version 3.5.0alpha2.
PostgreSQL version 17 RC1 in the Amazon RDS Preview environment 26
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The postgis_raster extension was updated to version 3.5.0alpha2.
• The postgis_tiger_geocoder extension was updated to version 3.5.0alpha2.
• The postgis_topology extension was updated to version 3.5.0alpha2.
The following extension supported in RDS for PostgreSQL version 16 isn't supported in RDS for 
PostgreSQL version 17 RC1 in preview:
• plrust
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 17.
PostgreSQL version 17 Beta 3 in the Amazon RDS Preview environment
Note
The preview documentation for Amazon RDS PostgreSQL version 17 is subject to change.
PostgreSQL 17 Beta 3 contains many new features and enhancements that can be seen in the 
following release documentation, PostgreSQL 17 Beta 3 Released!.
New features
• The t4g instance type is supported in the Preview environment.
• The wal_compression default value for TAZ cluster is now lz4 instead of zstd.
New extensions
• The pg_hint_plan extension was added.
• The plv8 extension was added.
• The rdkit extension was added.
This version also includes the following extension updates:
• The orafce extension was updated to version 4.10.3.
• The pg_cron extension was updated to version 1.6.3.
PostgreSQL version 17 Beta 3 in the Amazon RDS Preview environment 27
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pg_vector extension was updated to version 0.7.3.
The following extensions supported in Amazon RDS PostgreSQL version 16 aren't supported for 
Amazon RDS PostgreSQL version 17 Beta 3 in preview:
• pglogical
• plrust
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 17.
PostgreSQL version 17 Beta 2 in the Amazon RDS Preview environment
PostgreSQL 17 Beta 2 contains many new features and enhancements that can be seen in the 
following release documentation, PostgreSQL 17 Beta 2 Released!.
New extensions
• The h3-pg extension was added.
• The mysql_fdw extension was added.
• The pg_cron extension was added.
• The pgactive extension was added.
• The pgAudit extension was added.
• The pg_repack extension was added.
• The tds_fdw extension was added.
This version also includes the following extension update:
• The pgTAP extension was updated to version 1.3.3.
The following extensions supported in Amazon RDS PostgreSQL version 16 aren't supported for 
Amazon RDS PostgreSQL version 17 Beta 2 in preview:
• pg_hint_plan
• pglogical
• plrust
PostgreSQL version 17 Beta 2 in the Amazon RDS Preview environment 28
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• plv8
• rdkit
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 17.
PostgreSQL version 17 Beta 1 in the Amazon RDS Preview environment
PostgreSQL 17 Beta 1 contains many new features and enhancements that can be seen in the 
release documentation: PostgreSQL 17 Beta 1 Released!.
The following extensions supported in Amazon RDS PostgreSQL version 16 aren't supported for 
Amazon RDS PostgreSQL version 17 Beta 1 in preview:
• h3pg
• MySQL_FDW
• pg_cron
• pg_repack
• pgactive
• pgaudit
• pghintplan
• pglogical
• plrust
• plv8
• rdkit
• tds_fdw
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 17.
PostgreSQL 16 versions
Minor versions
• PostgreSQL version 16.13 on Amazon RDS
• PostgreSQL version 16.12 on Amazon RDS
PostgreSQL version 17 Beta 1 in the Amazon RDS Preview environment 29
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• PostgreSQL version 16.11 on Amazon RDS
• PostgreSQL version 16.10-R2 on Amazon RDS
• PostgreSQL version 16.10 on Amazon RDS
• PostgreSQL version 16.9-R2 on Amazon RDS
• PostgreSQL version 16.9 on Amazon RDS
• PostgreSQL version 16.8-R2 on Amazon RDS
• PostgreSQL version 16.8 on Amazon RDS
• PostgreSQL version 16.7 on Amazon RDS
• PostgreSQL version 16.6-R3 on Amazon RDS
• PostgreSQL version 16.6-R2 on Amazon RDS
• PostgreSQL version 16.6 on Amazon RDS
• PostgreSQL version 16.5 on Amazon RDS
• PostgreSQL version 16.4-R3 on Amazon RDS
• PostgreSQL version 16.4-R2 on Amazon RDS
• PostgreSQL version 16.4 on Amazon RDS
• PostgreSQL version 16.3-R4 on Amazon RDS
• PostgreSQL version 16.3-R3 on Amazon RDS
• PostgreSQL version 16.3-R2 on Amazon RDS
• PostgreSQL version 16.3 on Amazon RDS
• PostgreSQL version 16.2-R3 on Amazon RDS
• PostgreSQL version 16.2-R2 on Amazon RDS
• PostgreSQL version 16.2 on Amazon RDS
• PostgreSQL version 16.1-R2 on Amazon RDS
• PostgreSQL version 16.1 on Amazon RDS
• PostgreSQL version 16.0 in the Amazon RDS Preview environment
• PostgreSQL version 16 RC1 in the Amazon RDS Preview environment
• PostgreSQL version 16 Beta 3 in the Amazon RDS Preview environment
• PostgreSQL version 16 Beta 2 in the Amazon RDS Preview environment
• PostgreSQL version 16 Beta 1 in the Amazon RDS Preview environment
PostgreSQL 16 versions 30
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 16.13 on Amazon RDS
PostgreSQL version 16.13 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16.13 release.
PostgreSQL version 16.12 on Amazon RDS
PostgreSQL version 16.12 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16.12 release.
General enhancements
• Improved stability and reliability for database operations.
• Enhanced data collection capabilities.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.7.
• The pglogical extension was updated to version 2.4.6.
• The pg_hint_plan extension was updated to version 1.6.2.
• The orafce extension was updated to version 4.16.3.
• The pg_bigm extension was updated to version 1.2-20250903.
• The pg_cron extension was updated to version 1.6.7.
• The hypopg extension was updated to version 1.4.2.
• The tds_fdw extension was updated to version 2.0.5.
• The pg_repack extension was updated to version 1.5.3.
• The pgvector extension was updated to version 0.8.1.
• The mysql_fdw extension was updated to version 2.9.3.
• The oracle_fdw extension was updated to version 2.8.0.
PostgreSQL version 16.11 on Amazon RDS
PostgreSQL version 16.11 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16.11 release.
General enhancements
PostgreSQL version 16.13 on Amazon RDS 31
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pgcollection extension is now available for RDS PostgreSQL version 15.15 and above(16.11 
and 17.7), providing a memory-optimized data type designed for high-performance use inside 
PL/pgSQL functions. A collection stores key-value pairs where each key is a unique text string 
(maximum 32,767 characters) and values can be any PostgreSQL type including composite types, 
with all elements in a collection required to be of the same type. Collections maintain entries 
in creation order and can hold an unlimited number of elements constrained only by available 
database memory, with a maximum persisted size of 1GB when stored as a table column..
This version also includes the following extension changes:
• The pg_tle extension was updated to version 1.5.2.
• The h3-pg extension was updated to version 4.2.3.
PostgreSQL version 16.10-R2 on Amazon RDS
PostgreSQL version 16.10-R2 is now available on Amazon RDS.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 16.10 on Amazon RDS
PostgreSQL version 16.10 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16.10 release.
General enhancements
• Grant rds_superuser access to pg_wal_pause / pg_wal_replay functions to perform logical 
upgrades and veriﬁcation/validation.
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pg_repack extension was updated to version 1.5.2.
• The oracle_fdw extension was updated to version 2.8.0.
• The pgactive extension was updated to version 2.1.5.
PostgreSQL version 16.10-R2 on Amazon RDS 32
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 16.9-R2 on Amazon RDS
PostgreSQL version 16.9-R2 is now available on Amazon RDS.
General enhancements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 16.9 on Amazon RDS
PostgreSQL version 16.9 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16.9 release.
General enhancements
• Fixed for the address_standardizer_data_us extension issue regarding ALTER EXTENSION 
UPDATE failure.
• Changed the Oracle client library version on x86 to 19.26.0.0.0.
• Fixed the pgactive extension unable to upgrade issue due to incorrect extension upgrade 
scripts which causes replication to break after engine upgrade.
This version also includes the following extension changes:
• The pg_repack extension was updated to version 1.5.1.
• The pglogical extension was updated to version 2.4.5.
• The PgAudit extension was updated to version 16.1.
• The RDKit extension was updated to version 2024_09_6.
PostgreSQL version 16.8-R2 on Amazon RDS
PostgreSQL version 16.8-R2 is now available on Amazon RDS.
Fixes and improvements
PostgreSQL version 16.9-R2 on Amazon RDS 33
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 16.8 on Amazon RDS
PostgreSQL version 16.8 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16.8 release.
PostgreSQL version 16.7 on Amazon RDS
PostgreSQL version 16.7 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16.7 release.
New features and enhancements.
• In Blue/Green deployments, creating or modifying temporary objects is no longer classiﬁed as 
restricted DDL.
• Resolved an issue where DVB returned duplicate rows during slow vacuum analysis.
• Resolved CVE RUSTSEC-2024-0421 by upgrading URL Rust crate to 2.5.4. For more information, 
see RUSTSEC-2024-0421.
• Applied Promise.any error allocation ﬁx for V8 9.7.37, PLV8 3.1.10.
This version also includes the following extension changes:.
• The rds_tools extension was updated to 1.9.
• The orafce extension was updated to 4.14.0.
• The pg_cron extension was updated to 1.6.5.
• The rdkit extension was updated to 2024_09_3.
• The pg_active extension was updated to 2.1.4.
• The pg_partman extension was updated to 5.2.4.
• The prefix extension was updated to 1.2.10.
PostgreSQL version 16.8 on Amazon RDS 34
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16.6-R3 on Amazon RDS
PostgreSQL version 16.6-R3 is now available on Amazon RDS.
General enhancements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
PostgreSQL version 16.6-R2 on Amazon RDS
PostgreSQL version 16.6-R2 is now available on Amazon RDS. This release contains ﬁx for PLV8
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 16.6.
PostgreSQL version 16.6 on Amazon RDS
PostgreSQL version 16.6 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16.6 release.
PostgreSQL version 16.5 on Amazon RDS
PostgreSQL version 16.5 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in PostgreSQL 16.5.
New features
• Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some 
connection slots are reserved for the new rds_reserved role, which is granted to Amazon 
RDS administrative users. The number of reserved connection slots is determined by the
rds.rds_reserved_connections parameter . You may need to adjust the value of the
max_connections parameter to account for the number of Amazon RDS reserved connection 
slots.
The rds_reserved role is a new predeﬁned role created by Amazon RDS. Predeﬁned roles 
and their privileges can't be changed. You can't drop, rename, or modify privileges for these 
predeﬁned roles. Attempting to modify a predeﬁned role results in an error.
• Unblocked ALTER TEMP TABLE and DROP TEMP TABLE in Blue/Green replication.
PostgreSQL version 16.6-R3 on Amazon RDS 35
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Added the rds_tools.pg_ls_multixactdir() function for pg_multixact to monitor the 
directory disk space usage.
Updated features
• The oracle_fdw extension was updated to version 2.7.0.
• The orafce extension was updated to version 4.13.4.
• The pg_cron extension was updated to version 1.6.4.
• The pg_hint_plan extension was updated to version 1.6.1.
• The pgvector extension was updated to version 0.8.0.
• The plprofiler extension was updated to version 4.2.5.
• The PostGIS extension was updated to version 3.4.3.
• The rdkit extension was updated to version 4.6.1.
• The rds_tools extension was updated to version 1.7.
• The tds_fdw extension was updated to version 2.0.4.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16.4-R3 on Amazon RDS
PostgreSQL version 16.4-R3 is now available on Amazon RDS. This release contains ﬁxes for
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 16.4.
PostgreSQL version 16.4-R2 on Amazon RDS
PostgreSQL version 16.4-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 16.4 release.
PostgreSQL version 16.4 on Amazon RDS
PostgreSQL version 16.4 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16.4 release.
New features and enhancements
• Delegated extension role was added.
PostgreSQL version 16.4-R3 on Amazon RDS 36
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Fixed CVE-2024-7348 that prevents search path restrictions bypass through pattern-matching 
queries in information_schema.
This version also includes the following extension updates:
• The hypopg extension was updated to 1.4.1.
• The mysql_fdw extension was updated to 2.9.2.
• The orafce extension was updated to 4.10.3.
• The pg_cron extension was updated to 1.6.3.
• The pgTAP extension was updated to 1.3.3.
• The pgvector extension was updated to 0.7.3.
• The rdkit extension was updated to 4.5.0 (Release 2024_03_5).
• The wal2json extension was updated to 2.6.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16.3-R4 on Amazon RDS
PostgreSQL version 16.3-R4 is now available on Amazon RDS. This release contains ﬁxes for
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 16.3.
PostgreSQL version 16.3-R3 on Amazon RDS
PostgreSQL version 16.3-R3 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 16.3 release.
PostgreSQL version 16.3-R2 on Amazon RDS
PostgreSQL version 16.3-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 16.3 release.
New features and enhancements
• Includes support for four new crates in PL/Rust, including:
• regex
• serde
PostgreSQL version 16.3-R4 on Amazon RDS 37
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• serde_json
• url
• Fixed a security issue in pg_repack
• Fixed a performance issue in pgvector for index creation on halfvec data type
• Fixed a bug in aws_s3 causing import queries to occasionally get stuck and fail to terminate
PostgreSQL version 16.3 on Amazon RDS
PostgreSQL version 16.3 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16.3 release.
New features and enhancements
• The blue/green deployment switchover won’t be blocked by the REFRESH MATERIALIZED 
VIEW statement.
• Fixed the permission denial for the CREATE DATABASE WITH OWNER statement.
• Upgraded the aws_s3 extension to version 1.2 to support the export to S3 with the KMS 
customer managed key.
• Fixed a pgvector compatibility issue with some of the previous generations of DB instances, such 
as m4.
This version also includes the following extension updates:
• The aws_s3 extension was updated to 1.2.
• The orafce extension was updated to 4.9.4.
• The pg_partman extension was updated to 5.1.0.
• The pgvector extension was updated to 0.7.0.
• The postgis extension was updated to 3.4.2.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16.2-R3 on Amazon RDS
PostgreSQL version 16.2-R3 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 16.2 release.
PostgreSQL version 16.3 on Amazon RDS 38
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
New features and enhancements.
• Fixed a security issue in pg_repack
PostgreSQL version 16.2-R2 on Amazon RDS
PostgreSQL version 16.2-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 16.2 release.
New features and enhancements.
• Fixed a bug allowing the querying of the security invoker views as an unprivileged user.
• Fixed a bug preventing tds_fdw from connecting when TLS is enabled.
• Fixed a bug preventing upgrades to PostGIS version 3.4.1.
• Fixed an error with the aws_s3 extension when the Region was not provided.
This version also includes the following extension changes:.
• The pg_partman extension was updated to 5.0.1.
• The pg_tle extension was updated to 1.4.0.
• The pgactive extension was updated to 2.1.3.
• The pgtap extension was updated to 1.3.2.
• The pgvector extension was updated to 0.6.2.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16.2 on Amazon RDS
PostgreSQL version 16.2 on Amazon RDS
PostgreSQL version 16.2 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16.2 release..
New features and enhancements
• Added support for pg_log_standby_snapshot
PostgreSQL version 16.2-R2 on Amazon RDS 39
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Fixed the multisecond latency on the aws_lambda calls
• Fixed a bug preventing the termination of autovacuum
• Fixed a bug preventing the creation of the h3 extension
This version includes the following changes:
• The orafce extension was updated to version 4.9.0.
• The pg_repack extension was updated to version 1.5.0.
• The pgactive extension was updated to version 2.1.2.
• The pgvector extension was updated to 0.6.0.
• The plv8 extension was updated to 3.1.10.
• The PostGIS extension was updated to 3.4.1.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16.1-R2 on Amazon RDS
PostgreSQL version 16.1-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 16 release..
New features and enhancements
• Fixed a crash in CatalogCacheComputeHashValue with dblink_connect due to a Null or
invalid connection
• Supported the AWS SDK version of the aws_s3 extension
• Fixed the overﬂow in the pg_transport extension
• Removed the unsupported shared libraries from the engine binary
This version includes the following changes:
• The plrust extension was updated to version 1.2.7.
• The plv8 extension was updated to version 3.1.9.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16.1-R2 on Amazon RDS 40
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 16.1 on Amazon RDS
PostgreSQL version 16.1 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 16 release..
New features and enhancements
• The aws-lc now uses a FIPS version.
• Allow setting TLS 1.3 as the ssl_min_protocol_version and
ssl_max_protocol_version.
• The pgactive extension was added.
• The pglogical extension was added.
• By default, the default_toast_compression DB instance parameter is set to lz4.
• The rds.rds_superuser_reserved_connections parameter has been deprecated in RDS 
for PostgreSQL version 16. The reserved_connections parameter should be utilized to 
reserve the number of connection slots. The reserved_connections parameter sets the 
number of connection slots reserved for roles with the pg_use_reserved_connections
privileges. rds_superuser is a member of the pg_use_reserved_connections role by 
default. For more information, see the PostgreSQL documentation reserved connections.
This version includes the following changes:
• The hll extension was updated to version 2.1.8.
• The oracle_fdw extension was updated to version 2.6.0.
• The orafce extension was updated to version 4.6.1.
• The pg_cron extension was updated to version 1.6.1.
• The pg_partman extension was updated to version 5.0.0.
• The pgtap extension was updated to version 1.3.1.
• The pgvector extension was updated to version 0.5.1.
• The plprofiler extension was updated to version 4.2.4.
• The plrust extension was updated to version 1.2.6.
• The plv8 extension was updated to version 3.1.8.
• The rdkit extension was updated to version 4.4.0.
PostgreSQL version 16.1 on Amazon RDS 41
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16.0 in the Amazon RDS Preview environment
Note
The preview documentation for Amazon RDS PostgreSQL version 16.0 is subject to change.
Note
RDS for PostgreSQL versions 16 RC1, 16 Beta 3, 16 Beta 2, and 16 Beta 1 will not be 
supported after RDS for PostgreSQL version 16.0 is released in the Preview environment.
PostgreSQL version 16.0 is now available in the Amazon RDS Preview environment. PostgreSQL 
version 16 contains several improvements that are described in the PostgreSQL 16 release.
This version includes the following changes:
• The mysql_fdw extension was updated to version 2.9.1
• The pgrouting extension was updated to version 3.5.0
• The pgvector extension was updated to version 0.5.0
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16 RC1 in the Amazon RDS Preview environment
Note
The preview documentation for Amazon RDS PostgreSQL version 16 RC1 is subject to 
change.
PostgreSQL version 16 RC1 is now available in the Amazon RDS Preview environment. PostgreSQL 
version 16 RC1 contains several improvements that are described in the following PostgreSQL 
documentation: PostgreSQL 16 RC1 Released.
PostgreSQL version 16.0 in the Amazon RDS Preview environment 42
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
New extensions
• The pg_proctab extension was added.
• The rdkit extension was added.
• The hll extension was added.
• The pg_cron extension was added.
This version also includes the following change:
• The PostGIS extension was updated to version 3.4.0.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16 Beta 3 in the Amazon RDS Preview environment
Note
The preview documentation for Amazon RDS PostgreSQL version 16 beta 3 is subject to 
change.
PostgreSQL version 16 Beta 3 is now available in the Amazon RDS Preview environment. 
PostgreSQL version 16 Beta 3 contains several improvements that are described in the following 
PostgreSQL documentation: PostgreSQL 16 Beta 3 Released.
New extensions
• The h3-pg extension was added.
• The mysql_fdw extension was added.
• The oracle_fdw extension was added.
• The pg_bigm extension was added.
• The pg_hint_plan extension was added.
• The pgAudit extension was added.
• The plprofiler extension was added.
• The plrust extension was added.
PostgreSQL version 16 Beta 3 in the Amazon RDS Preview environment 43
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The plv8 extension was added.
This version also includes the following change:
• The pg_tle extension was updated to version 1.1.0.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16 Beta 2 in the Amazon RDS Preview environment
Note
The preview documentation for Amazon RDS PostgreSQL version 16 Beta 2 is subject to 
change.
PostgreSQL version 16 Beta 2 is now available in the Amazon RDS Preview environment. 
PostgreSQL version 16 Beta 2 contains several improvements that are described in the following 
PostgreSQL documentation: PostgreSQL 16 Beta 2 Released.
New extensions
• The aws_commons extension was added.
• The aws_lambda extension was added.
• The aws_s3 extension was added.
• The hypopg extension was added.
• The orafce extension was added.
This version also includes the following change:
• pgvector was updated to version 0.4.4
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL version 16 Beta 2 in the Amazon RDS Preview environment 44
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 16 Beta 1 in the Amazon RDS Preview environment
Note
The preview documentation for Amazon RDS PostgreSQL version 16 Beta 1 is subject to 
change.
PostgreSQL version 16 Beta 1 is now available in the Amazon RDS Preview environment. 
PostgreSQL version 16 Beta 1 contains several improvements that are described in the following 
PostgreSQL documentation: PostgreSQL 16 Beta 1 Released.
The following extensions supported in Amazon RDS PostgreSQL version 15 aren't supported for 
Amazon RDS PostgreSQL version 16 Beta 1 in preview:
• aws_commons
• aws_lambda
• aws_s3
• hll
• hypoPG
• mysql_fdw
• oracle_fdw
• orafce
• pg_bigm
• pg_cron
• pg_proctab
• pgaudit
• pghintplan
• pglogical
• plprofiler
• plrust
• plv8
• rdkit
PostgreSQL version 16 Beta 1 in the Amazon RDS Preview environment 45
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 16.
PostgreSQL 15 versions (Some of these versions have reached 
the end of standard support or deprecated.)
Minor versions
• PostgreSQL version 15.17 on Amazon RDS
• PostgreSQL version 15.16 on Amazon RDS
• PostgreSQL version 15.15 on Amazon RDS
• PostgreSQL version 15.14-R2 on Amazon RDS
• PostgreSQL version 15.14 on Amazon RDS
• PostgreSQL version 15.13-R2 on Amazon RDS
• PostgreSQL version 15.13 on Amazon RDS
• PostgreSQL version 15.12-R2 on Amazon RDS
• PostgreSQL version 15.12 on Amazon RDS
• PostgreSQL version 15.11 on Amazon RDS
• PostgreSQL version 15.10-R3 on Amazon RDS
• PostgreSQL version 15.10-R2 on Amazon RDS
• PostgreSQL version 15.10 on Amazon RDS
• PostgreSQL version 15.9 on Amazon RDS
• PostgreSQL version 15.8-R3 on Amazon RDS
• PostgreSQL version 15.8-R2 on Amazon RDS
• PostgreSQL version 15.8 on Amazon RDS
• PostgreSQL version 15.7-R4 on Amazon RDS
• PostgreSQL version 15.7-R3 on Amazon RDS
• PostgreSQL version 15.7-R2 on Amazon RDS
• PostgreSQL version 15.7 on Amazon RDS
• PostgreSQL version 15.6-R3 on Amazon RDS (This version has reached the end of standard 
support.)
• PostgreSQL version 15.6-R2 on Amazon RDS (This version has reached the end of standard 
support.)
PostgreSQL 15 versions (Some of these versions have reached the end of standard support or 
deprecated.)
46
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• PostgreSQL version 15.6 on Amazon RDS (This version has reached the end of standard support.)
• PostgreSQL version 15.5-R2 on Amazon RDS (This version has reached the end of standard 
support.)
• PostgreSQL version 15.5 on Amazon RDS (This version has reached the end of standard support.)
• PostgreSQL version 15.4-R3 on Amazon RDS (This version has reached the end of standard 
support.)
• PostgreSQL version 15.4-R2 on Amazon RDS (This version has reached the end of standard 
support.)
• PostgreSQL version 15.4 on Amazon RDS (This version has reached the end of standard support.)
• PostgreSQL version 15.3-R2 on Amazon RDS (Deprecated)
• PostgreSQL version 15.3 on Amazon RDS (Deprecated)
• PostgreSQL version 15.2-R2 on Amazon RDS (Deprecated)
• PostgreSQL version 15.2 on Amazon RDS (Deprecated)
PostgreSQL version 15.17 on Amazon RDS
PostgreSQL version 15.17 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.17 release.
PostgreSQL version 15.16 on Amazon RDS
PostgreSQL version 15.16 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.16 release.
General enhancements
• Improved stability and reliability for database operations.
• Enhanced data collection capabilities.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.7.
• The pglogical extension was updated to version 2.4.6.
• The pg_hint_plan extension was updated to version 1.5.3.
• The orafce extension was updated to version 4.16.3.
PostgreSQL version 15.17 on Amazon RDS 47
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pg_bigm extension was updated to version 1.2-20250903.
• The pg_cron extension was updated to version 1.6.7.
• The hypopg extension was updated to version 1.4.2.
• The tds_fdw extension was updated to version 2.0.5.
• The pg_repack extension was updated to version 1.5.3.
• The pgvector extension was updated to version 0.8.1.
• The mysql_fdw extension was updated to version 2.9.3.
• The oracle_fdw extension was updated to version 2.8.0.
PostgreSQL version 15.15 on Amazon RDS
PostgreSQL version 15.15 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.15 release.
General enhancements
• The pgcollection extension is now available for RDS PostgreSQL version 15.15 and above(16.11 
and 17.7), providing a memory-optimized data type designed for high-performance use inside 
PL/pgSQL functions. A collection stores key-value pairs where each key is a unique text string 
(maximum 32,767 characters) and values can be any PostgreSQL type including composite types, 
with all elements in a collection required to be of the same type. Collections maintain entries 
in creation order and can hold an unlimited number of elements constrained only by available 
database memory, with a maximum persisted size of 1GB when stored as a table column.
This version also includes the following extension changes:
• The pg_tle extension was updated to version 1.5.2.
• The h3-pg extension was updated to version 4.2.3.
PostgreSQL version 15.14-R2 on Amazon RDS
PostgreSQL version 15.14-R2 is now available on Amazon RDS.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 15.15 on Amazon RDS 48
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 15.14 on Amazon RDS
PostgreSQL version 15.14 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.14 release.
General enhancements
• Grant rds_superuser access to pg_wal_pause / pg_wal_replay functions to perform logical 
upgrades and veriﬁcation/validation.
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pg_repack extension was updated to version 1.5.2.
• The oracle_fdw extension was updated to version 2.8.0.
• The pgactive extension was updated to version 2.1.5.
PostgreSQL version 15.13-R2 on Amazon RDS
PostgreSQL version 15.13-R2 is now available on Amazon RDS.
General enhancements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 15.13 on Amazon RDS
PostgreSQL version 15.13 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.13 release.
General enhancements
• Fixed for the address_standardizer_data_us extension issue regarding ALTER EXTENSION 
UPDATE failure.
PostgreSQL version 15.14 on Amazon RDS 49
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Changed the Oracle client library version on x86 to 19.26.0.0.0.
• Fixed the pgactive extension unable to upgrade issue due to incorrect extension upgrade 
scripts which causes replication to break after engine upgrade.
This version also includes the following extension changes:
• The pg_repack extension was updated to version 1.5.1.
• The pglogical extension was updated to version 2.4.5.
• The PgAudit extension was updated to version 1.7.1.
• The RDKit extension was updated to version 2024_09_6.
PostgreSQL version 15.12-R2 on Amazon RDS
PostgreSQL version 15.12-R2 is now available on Amazon RDS.
Fixes and improvements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 15.12 on Amazon RDS
PostgreSQL version 15.12 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.12 release.
PostgreSQL version 15.11 on Amazon RDS
PostgreSQL version 15.11 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.11 release.
New features and enhancements.
• In Blue/Green deployments, creating or modifying temporary objects is no longer classiﬁed as 
restricted DDL.
PostgreSQL version 15.12-R2 on Amazon RDS 50
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Resolved an issue where DVB returned duplicate rows during slow vacuum analysis.
• Resolved CVE RUSTSEC-2024-0421 by upgrading URL Rust crate to 2.5.4. For more information, 
see RUSTSEC-2024-0421.
• Applied Promise.any error allocation ﬁx for V8 9.7.37, PLV8 3.1.10.
This version also includes the following extension changes:.
• The rds_tools extension was updated to 1.9.
• The orafce extension was updated to 4.14.0.
• The pg_cron extension was updated to 1.6.5.
• The rdkit extension was updated to 2024_09_3.
• The pg_active extension was updated to 2.1.4.
• The pg_partman extension was updated to 5.2.4.
• The prefix extension was updated to 1.2.10.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL version 15.10-R3 on Amazon RDS
PostgreSQL version 15.10-R3 is now available on Amazon RDS.
General enhancements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
PostgreSQL version 15.10-R2 on Amazon RDS
PostgreSQL version 15.10-R2 is now available on Amazon RDS. This release ﬁx for PLV8
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 
15.10.
PostgreSQL version 15.10 on Amazon RDS
PostgreSQL version 15.10 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.10 release.
PostgreSQL version 15.10-R3 on Amazon RDS 51
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 15.9 on Amazon RDS
PostgreSQL version 15.9 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in PostgreSQL 15.9.
New features
• Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some 
connection slots are reserved for the new rds_reserved role, which is granted to Amazon 
RDS administrative users. The number of reserved connection slots is determined by the
rds.rds_reserved_connections parameter . You may need to adjust the value of the
max_connections parameter to account for the number of Amazon RDS reserved connection 
slots.
The rds_reserved role is a new predeﬁned role created by Amazon RDS. Predeﬁned roles 
and their privileges can't be changed. You can't drop, rename, or modify privileges for these 
predeﬁned roles. Attempting to modify a predeﬁned role results in an error.
• Unblocked ALTER TEMP TABLE and DROP TEMP TABLE in Blue/Green replication.
• Added the rds_tools.pg_ls_multixactdir() function for pg_multixact to monitor the 
directory disk space usage.
Updated features
• The oracle_fdw extension was updated to version 2.7.0.
• The orafce extension was updated to version 4.13.4.
• The pg_cron extension was updated to version 1.6.4.
• The pg_hint_plan extension was updated to version 1.5.2.
• The pgvector extension was updated to version 0.8.0.
• The plprofiler extension was updated to version 4.2.5.
• The PostGIS extension was updated to version 3.4.3.
• The rdkit extension was updated to version 4.6.1.
• The rds_tools extension was updated to version 1.7.
• The tds_fdw extension was updated to version 2.0.4.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL version 15.9 on Amazon RDS 52
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 15.8-R3 on Amazon RDS
PostgreSQL version 15.8-R3 is now available on Amazon RDS. This release contains ﬁx for
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 15.8.
PostgreSQL version 15.8-R2 on Amazon RDS
PostgreSQL version 15.8-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 15.8 release.
PostgreSQL version 15.8 on Amazon RDS
PostgreSQL version 15.8 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.8 release.
New features and enhancements
• Delegated extension role was added.
This version also includes the following extension updates:
• The hypopg extension was updated to 1.4.1.
• The mysql_fdw extension was updated to 2.9.2.
• The orafce extension was updated to 4.10.3.
• The pg_cron extension was updated to 1.6.3.
• The pgTAP extension was updated to 1.3.3.
• The pgvector extension was updated to 0.7.3.
• The rdkit extension was updated to 4.5.0 (Release 2024_03_5).
• The wal2json extension was updated to 2.6.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL version 15.7-R4 on Amazon RDS
PostgreSQL version 15.7-R4 is now available on Amazon RDS. This release contains ﬁxes for
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 15.7.
PostgreSQL version 15.8-R3 on Amazon RDS 53
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 15.7-R3 on Amazon RDS
PostgreSQL version 15.7-R3 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 15.7 release.
PostgreSQL version 15.7-R2 on Amazon RDS
PostgreSQL version 15.7-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 15.7 release.
New features and enhancements
• Includes support for four new crates in PL/Rust, including:
• regex
• serde
• serde_json
• url
• Fixed a security issue in pg_repack
• Fixed a performance issue in pgvector for index creation on halfvec data type
• Fixed a bug in aws_s3 causing import queries to occasionally get stuck and fail to terminate
PostgreSQL version 15.7 on Amazon RDS
PostgreSQL version 15.7 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.7 release.
New features and enhancements
• The blue/green deployment switchover won’t be blocked by the REFRESH MATERIALIZED 
VIEW statement.
• Fixed the permission denial for the CREATE DATABASE WITH OWNER statement.
• Upgraded the aws_s3 extension to version 1.2 to support the export to S3 with the KMS 
customer managed key.
• Fixed a pgvector compatibility issue with some of the previous generations of DB instances, such 
as m4.
PostgreSQL version 15.7-R3 on Amazon RDS 54
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
This version also includes the following extension updates:
• The aws_s3 extension was updated to 1.2.
• The orafce extension was updated to 4.9.4.
• The pg_hint_plan extension was updated to 1.5.1.
• The pg_partman extension was updated to 5.1.0.
• The pgvector extension was updated to 0.7.0.
• The postgis extension was updated to 3.4.2.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL version 15.6-R3 on Amazon RDS (This version has reached 
the end of standard support.)
PostgreSQL version 15.6-R3 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 15.6 release.
New features and enhancements
• Fixed a security issue in pg_repack
PostgreSQL version 15.6-R2 on Amazon RDS (This version has reached 
the end of standard support.)
PostgreSQL version 15.6-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 15.6 release.
New features and enhancements.
• Fixed a bug allowing the querying of the security invoker views as an unprivileged user.
• Fixed a bug preventing upgrades to PostGIS version 3.4.1.
• Fixed an error with the aws_s3 extension when the Region was not provided.
This version also includes the following extension changes:
• The pg_partman extension was updated to version 5.0.1.
PostgreSQL version 15.6-R3 on Amazon RDS (This version has reached the end of standard support.) 55
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pg_tle extension was updated to version 1.4.0.
• The pgactive extension was updated to version 2.1.3.
• The pgtap extension was updated to version 1.3.2.
• The pgvector extension was updated to version 0.6.2.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL version 15.6 on Amazon RDS (This version has reached the 
end of standard support.)
PostgreSQL version 15.6 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.6 release.
New features and enhancements
• Fixed the multisecond latency on the aws_lambda calls
• Fixed a bug preventing the termination of autovacuum
This version includes the following changes:
• The orafce extension was updated to version 4.9.0.
• The pgactive extension was updated to version 2.1.2.
• The pgvector extension was updated to 0.6.0.
• The plv8 extension was updated to 3.1.10.
• The PostGIS extension was updated to 3.4.1.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL version 15.5-R2 on Amazon RDS (This version has reached 
the end of standard support.)
PostgreSQL version 15.5-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 15.5 release.
PostgreSQL version 15.6 on Amazon RDS (This version has reached the end of standard support.) 56
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
New features and enhancements
• Fixed a crash in CatalogCacheComputeHashValue with dblink_connect due to a Null or
invalid connection.
• Backported run_as_owner to RPG 15:
• Backported a security ﬁx for the logical replication apply worker that allows regular table 
owners to obtain privilege escalation to the subscription owner (an rds_superuser). The logical 
apply worker mitigates the risk by temporarily switching the role from the subscription owner 
to the table owner during logical apply.
In the cases of potential security breaches, the ﬁx will break your existing logical replication 
if any table in the subscription is owned by a regular user, and there are security-restricted 
operations attached to the table via triggers or default expressions. We recommend that you 
carefully examine the operations attached to the table if you notice the logical replication is 
broken after the upgrade. If all of the operations are as expected and you wish to revert the 
behavior of the logical replication so your application can continue, you can do so by setting 
the new parameter rds.run_logical_replication_as_subscription_owner to true. 
Be aware that by doing so your logical replication will be vulnerable to the aforementioned 
security risk again.
• Added rds.run_logical_replication_as_subscription_owner to the Amazon RDS 
parameter group.
• Supported the AWS SDK version of the aws_s3 extension.
• Fixed the overﬂow in the pg_transport extension.
• Removed the unsupported shared libraries from the engine binary.
This version includes the following changes:
• The plrust extension was updated to version 1.2.7.
• The plv8 extension was updated to version 3.1.9.
PostgreSQL version 15.5 on Amazon RDS (This version has reached the 
end of standard support.)
PostgreSQL version 15.5 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.5 release.
PostgreSQL version 15.5 on Amazon RDS (This version has reached the end of standard support.) 57
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
New features and enhancements
• Fixed a bug where pg_database_size() with an invalid OID causes a crash.
• Added support for the rds.enable_pgactive parameter in rdsutils to avoid the warning 
message.
• Exposed RDKit guc param rdkit.morgan_fp_size.
• Fixed the bug where setting TABLESPACE with DEFAULT option in CREATE or ALTER DATABASE
fails.
This version includes the following changes:
• The h3-pg extension was updated to version 4.1.3.
• The hll extension was updated to version 2.18.
• The oracle_fdw extension was updated to version 2.6.0.
• The orafce extension was updated to version 4.6.1.
• The pg_cron extension was updated to version 1.6.1.
• The pg_partman extension was updated to version 5.0.0.
• The pg_proctab extension was updated to version 0.0.10.
• The pgactive extension was updated to version 2.1.1.
• The pgtap extension was updated to version 1.3.1.
• The plprofiler extension was updated to version 4.2.4.
• The plrust extension was updated to version 1.2.6.
• The PostGIS extension was updated to version 3.4.0.
• The rdkit extension was updated to version 4.4.0.
PostgreSQL version 15.4-R3 on Amazon RDS (This version has reached 
the end of standard support.)
PostgreSQL version 15.4-R3 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 15.4 release.
This version includes the following changes:
• Bug and security ﬁxes for pgactive.
PostgreSQL version 15.4-R3 on Amazon RDS (This version has reached the end of standard support.) 58
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pgvector extension was updated to version 0.5.1.
PostgreSQL version 15.4-R2 on Amazon RDS (This version has reached 
the end of standard support.)
PostgreSQL version 15.4-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 15.4 release.
New features and enhancements
• Fixed a bug preventing database owners without the rds_superuser role from being able to 
create tables in the public schema.
• The pgactive extension was added.
• A new rds.cte_materialize_mode parameter was introduced which controls the 
materialization behavior of the query of a WITH clause, also known as a Common Table 
Expression. See WITH Queries for more information. The parameter values include the following:
• default: The WITH clause will be treated using the engine's default behavior.
• always: The full output of the query in the WITH clause will be materialized and the output 
reused in the outer query.
• never: The query in the WITH clause will be inlined with the outer query if possible. This 
parameter will also override the MATERIALIZED and NOT MATERIALIZED keywords supplied 
to the WITH clause.
This version also includes the following changes:
• The mysql_fdw extension was updated to version 2.9.1.
• The pgvector extension was updated to version 0.5.0.
• The plrust extension was updated to version 1.2.5.
• The plv8 extension was updated to version 3.1.8.
• The rdkit extension was updated to version 4.3.0.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL version 15.4-R2 on Amazon RDS (This version has reached the end of standard support.) 59
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 15.4 on Amazon RDS (This version has reached the 
end of standard support.)
PostgreSQL version 15.4 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.4 release.
New features and enhancements
• Fixed a bug preventing users with the rds_superuser role from creating schemas in databases 
owned by other users.
• Users with the rds_superuser role can now access toast tables in the pg_toast schema that 
are owned by other users.
• Fixed an issue where ALTER TABLE took a ShareLock and may cause deadlocks.
This version also includes the following changes:
• The hypopg extension was updated to version 1.4.0.
• The orafce extension was updated to version 4.3.0.
• The pg_tle extension was updated to version 1.1.1.
• The pglogical extension was updated to version 2.4.3.
• The plrust extension was updated to version 1.2.3.
• The PostGIS extension was updated to version 3.3.3.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL version 15.3-R2 on Amazon RDS (Deprecated)
PostgreSQL version 15.3-R2 is now available on Amazon RDS. This release contains logical 
replication for Multi-AZ DB clusters, improved plrust performance, and an update to pgvector.
New features and enhancements
• Improves the performance of plrust
• Fixed a Patroni 2.1.7 restart issue and instead enables replication slot from the disk
This version also includes the following changes:
PostgreSQL version 15.4 on Amazon RDS (This version has reached the end of standard support.) 60
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pgvector extension was updated to version 0.4.4.
• The plrust extension was updated to version 1.1.3.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL version 15.3 on Amazon RDS (Deprecated)
PostgreSQL version 15.3 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.3 release.
New features and enhancements
• Includes changes to allow rds-superuser to run the pg_stat_reset_slru function
• Fixed a security issue involving rds_sec_override which wasn't reset after the intended usage, 
allowing unauthorized access to restricted tables
• Added the hypopg extension at version 1.3.1
• You can use logical_seed_lsn to determine the LSN at which a snapshot is taken in order to 
establish logical replication connection between the source and the restored target database. 
You can then use logical replication to continuously stream the newer data recorded after 
the LSN and synchronize the changes from publisher to subscriber. Speciﬁcally, it allows the 
customer to create a logical slot on a source RDS database, take a snapshot, restore the snapshot 
to a new RDS instance (target), and use the value of logical_seed_lsn() from the target instance 
to advance the logical slot on the source instance in order to subscribe the target to the source.
This version also includes the following changes:
• compat-collation-for-glibc was updated to version 1.8.
• libgeos was updated to version 3.11.2.
• The pg_cron extension was updated to version 1.5.2.
• The pg_partman extension was updated to version 4.7.3.
• The pg_tle extension was updated to version 1.0.4.
• The plrust extension was updated to version 1.1.1.
• The plv8 extension was updated to version 3.1.6.
• The PostGIS extension was updated to version 3.3.2.
PostgreSQL version 15.3 on Amazon RDS (Deprecated) 61
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL version 15.2-R2 on Amazon RDS (Deprecated)
PostgreSQL version 15.2-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 15.2 release.
New extensions
• The pgvector extension was added.
• The plrust extension was added.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL version 15.2 on Amazon RDS (Deprecated)
PostgreSQL version 15.2 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 15.2 release.
New features and enhancements
• The archive library rds_archive is now used for archiving WAL ﬁles instead of
archive_command.
• The lz4 and zstd WAL compression methods are now supported.
• By default, the default_toast_compression DB instance parameter is set to lz4.
New extensions
• The pg_walinspect extension version 1.0 was added.
This version also includes the following changes:
• The btree_gist extension was updated to version 1.7.
• The hll extension was updated to version 2.17.
• The mysql_fdw extension was updated to version 2.9.0.
• The pageinspect extension was updated to version 1.11.
PostgreSQL version 15.2-R2 on Amazon RDS (Deprecated) 62
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pg_hint_plan extension was updated to version 1.5.0.
• The pg_repack extension was updated to version 1.4.8.
• The pg_stat_statements extension was updated to version 1.10.
• The pgaudit extension was updated to version 1.7.0.
• The pglogical extension was updated to version 2.4.2.
• The pgrouting extension was updated to version 3.4.1.
• The pllcoffee extension was updated to version 3.1.4.
• The plls extensionwas updated to version 3.1.4.
• The plprofiler extension was updated to version 4.2.1.
• The plv8 extension was updated to version 3.1.4.
• The PostGIS extension was updated to version 3.3.2.
• The tds_fdw extension was updated to version 2.0.3.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 15.
PostgreSQL 14 versions
Minor versions
• PostgreSQL version 14.22 on Amazon RDS
• PostgreSQL version 14.21 on Amazon RDS
• PostgreSQL version 14.20-R2 on Amazon RDS
• PostgreSQL version 14.20 on Amazon RDS
• PostgreSQL version 14.19-R2 on Amazon RDS
• PostgreSQL version 14.19 on Amazon RDS
• PostgreSQL version 14.18-R2 on Amazon RDS
• PostgreSQL version 14.18 on Amazon RDS
• PostgreSQL version 14.17-R2 on Amazon RDS
• PostgreSQL version 14.17 on Amazon RDS
• PostgreSQL version 14.16 on Amazon RDS
PostgreSQL 14 versions 63
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• PostgreSQL version 14.15-R3 on Amazon RDS
• PostgreSQL version 14.15-R2 on Amazon RDS
• PostgreSQL version 14.15 on Amazon RDS
• PostgreSQL version 14.14 on Amazon RDS
• PostgreSQL version 14.13-R3 on Amazon RDS
• PostgreSQL version 14.13-R2 on Amazon RDS
• PostgreSQL version 14.13 on Amazon RDS
• PostgreSQL version 14.12-R4 on Amazon RDS
• PostgreSQL version 14.12-R3 on Amazon RDS
• PostgreSQL version 14.12-R2 on Amazon RDS
• PostgreSQL version 14.12 on Amazon RDS
• PostgreSQL version 14.11-R4 on Amazon RDS
• PostgreSQL version 14.11-R3 on Amazon RDS
• PostgreSQL version 14.11-R2 on Amazon RDS
• PostgreSQL version 14.11 on Amazon RDS
• PostgreSQL version 14.10-R2 on Amazon RDS
• PostgreSQL version 14.10 on Amazon RDS
• PostgreSQL version 14.9-R2 on Amazon RDS
• PostgreSQL version 14.9 on Amazon RDS
• PostgreSQL version 14.8-R2 on Amazon RDS (Deprecated)
• PostgreSQL version 14.8 on Amazon RDS (Deprecated)
• PostgreSQL version 14.7 on Amazon RDS (Deprecated)
• PostgreSQL version 14.6 on Amazon RDS (Deprecated)
• PostgreSQL version 14.5 on Amazon RDS (Deprecated)
• PostgreSQL version 14.4 on Amazon RDS (Deprecated)
• PostgreSQL version 14.3 on Amazon RDS (Deprecated)
• PostgreSQL version 14.2 on Amazon RDS (Deprecated)
• PostgreSQL version 14.1 on Amazon RDS (Deprecated)
PostgreSQL 14 versions 64
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 14.22 on Amazon RDS
PostgreSQL version 14.22 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.22 release.
PostgreSQL version 14.21 on Amazon RDS
PostgreSQL version 14.21 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.21 release.
General enhancements
• Improved stability and reliability for database operations.
• Enhanced data collection capabilities.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.7.
• The pglogical extension was updated to version 2.4.6.
• The pg_hint_plan extension was updated to version 1.4.4.
• The orafce extension was updated to version 4.16.3.
• The pg_bigm extension was updated to version 1.2-20250903.
• The pg_cron extension was updated to version 1.6.7.
• The hypopg extension was updated to version 1.4.2.
• The tds_fdw extension was updated to version 2.0.5.
• The pg_repack extension was updated to version 1.5.3.
• The pgvector extension was updated to version 0.8.1.
• The mysql_fdw extension was updated to version 2.9.3.
• The oracle_fdw extension was updated to version 2.8.0.
PostgreSQL version 14.20-R2 on Amazon RDS
PostgreSQL version 14.20-R2 is now available on Amazon RDS.
This version also includes the following changes:
PostgreSQL version 14.22 on Amazon RDS 65
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Fixed an issue on the plv8 extension regarding CREATE EXTENSION failure on older version.
PostgreSQL version 14.20 on Amazon RDS
PostgreSQL version 14.20 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.20 release.
General enhancements
This version also includes the following extension changes:
• The pg_tle extension was updated to version 1.5.2.
• The h3-pg extension was updated to version 4.2.3.
PostgreSQL version 14.19-R2 on Amazon RDS
PostgreSQL version 14.19-R2 is now available on Amazon RDS.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 14.19 on Amazon RDS
PostgreSQL version 14.19 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.19 release.
General enhancements
• Grant rds_superuser access to pg_wal_pause / pg_wal_replay functions to perform logical 
upgrades and veriﬁcation/validation.
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pg_repack extension was updated to version 1.5.2.
• The oracle_fdw extension was updated to version 2.8.0.
• The pgactive extension was updated to version 2.1.5.
PostgreSQL version 14.20 on Amazon RDS 66
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 14.18-R2 on Amazon RDS
PostgreSQL version 14.18-R2 is now available on Amazon RDS.
General enhancements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 14.18 on Amazon RDS
PostgreSQL version 14.18 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.18 release.
General enhancements
• Fixed for the address_standardizer_data_us extension issue regarding ALTER EXTENSION 
UPDATE failure.
• Changed the Oracle client library version on x86 to 19.26.0.0.0.
• Fixed the pgactive extension unable to upgrade issue due to incorrect extension upgrade 
scripts which causes replication to break after engine upgrade.
This version also includes the following extension changes:
• The pg_repack extension was updated to version 1.5.1.
• The pglogical extension was updated to version 2.4.5.
• The PgAudit extension was updated to version 1.6.3.
• The RDKit extension was updated to version 2024_09_6.
PostgreSQL version 14.17-R2 on Amazon RDS
PostgreSQL version 14.17-R2 is now available on Amazon RDS.
Fixes and improvements
PostgreSQL version 14.18-R2 on Amazon RDS 67
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 14.17 on Amazon RDS
PostgreSQL version 14.17 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.17 release.
PostgreSQL version 14.16 on Amazon RDS
PostgreSQL version 14.16 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.16 release.
New features and enhancements.
• In Blue/Green deployments, creating or modifying temporary objects is no longer classiﬁed as 
restricted DDL.
• Resolved an issue where DVB returned duplicate rows during slow vacuum analysis.
• Resolved CVE RUSTSEC-2024-0421 by upgrading URL Rust crate to 2.5.4. For more information, 
see RUSTSEC-2024-0421.
• Applied Promise.any error allocation ﬁx for V8 9.7.37, PLV8 3.1.10.
This version also includes the following extension changes:.
• The rds_tools extension was updated to 1.9.
• The orafce extension was updated to 4.14.0.
• The pg_cron extension was updated to 1.6.5.
• The rdkit extension was updated to 2024_09_3.
• The pg_active extension was updated to 2.1.4.
• The pg_partman extension was updated to 5.2.4.
• The prefix extension was updated to 1.2.10.
PostgreSQL version 14.17 on Amazon RDS 68
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.15-R3 on Amazon RDS
PostgreSQL version 14.15-R3 is now available on Amazon RDS.
General enhancements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
PostgreSQL version 14.15-R2 on Amazon RDS
PostgreSQL version 14.15-R2 is now available on Amazon RDS. This release contains ﬁx for PLV8
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 
14.15.
PostgreSQL version 14.15 on Amazon RDS
PostgreSQL version 14.15 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.15 release.
PostgreSQL version 14.14 on Amazon RDS
PostgreSQL version 14.14 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in PostgreSQL 14.14.
New features
• Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some 
connection slots are reserved for the new rds_reserved role, which is granted to Amazon 
RDS administrative users. The number of reserved connection slots is determined by the
rds.rds_reserved_connections parameter . You may need to adjust the value of the
max_connections parameter to account for the number of Amazon RDS reserved connection 
slots.
The rds_reserved role is a new predeﬁned role created by Amazon RDS. Predeﬁned roles 
and their privileges can't be changed. You can't drop, rename, or modify privileges for these 
predeﬁned roles. Attempting to modify a predeﬁned role results in an error.
• Unblocked ALTER TEMP TABLE and DROP TEMP TABLE in Blue/Green replication.
PostgreSQL version 14.15-R3 on Amazon RDS 69
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Added the rds_tools.pg_ls_multixactdir() function for pg_multixact to monitor the 
directory disk space usage.
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
Updated features
• The oracle_fdw extension was updated to version 2.7.0.
• The orafce extension was updated to version 4.13.4.
• The pg_cron extension was updated to version 1.6.4.
• The pg_hint_plan extension was updated to version 1.4.3
• The pgvector extension was updated to version 0.8.0.
• The plprofiler extension was updated to version 4.2.5.
• The PostGIS extension was updated to version 3.4.3.
• The rdkit extension was updated to version 4.6.1.
• The rds_tools extension was updated to version 1.7.
• The tds_fdw extension was updated to version 2.0.4.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.13-R3 on Amazon RDS
PostgreSQL version 14.13-R3 is now available on Amazon RDS. This release contains ﬁxes for
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 
14.13.
PostgreSQL version 14.13-R2 on Amazon RDS
PostgreSQL version 14.13-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 14.13 release.
New features and enhancements
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
PostgreSQL version 14.13-R3 on Amazon RDS 70
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 14.13 on Amazon RDS
PostgreSQL version 14.13 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.13 release.
New features and enhancements
• Delegated extension role was added.
This version also includes the following extension updates:
• The hypopg extension was updated to 1.4.1.
• The mysql_fdw extension was updated to 2.9.2.
• The orafce extension was updated to 4.10.3.
• The pg_cron extension was updated to 1.6.3.
• The pgTAP extension was updated to 1.3.3.
• The pgvector extension was updated to 0.7.3.
• The rdkit extension was updated to 4.5.0 (Release 2024_03_5).
• The wal2json extension was updated to 2.6.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.12-R4 on Amazon RDS
PostgreSQL version 14.12-R4 is now available on Amazon RDS. This release contains ﬁxes for
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 
14.12.
PostgreSQL version 14.12-R3 on Amazon RDS
PostgreSQL version 14.12-R3 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 14.12 release.
New features and enhancements
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
PostgreSQL version 14.13 on Amazon RDS 71
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 14.12-R2 on Amazon RDS
PostgreSQL version 14.12-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 14.12 release.
New features and enhancements
• Includes support for four new crates in PL/Rust, including:
• regex
• serde
• serde_json
• url
• Fixed a security exploit issue in plv8
• Fixed a security issue in pg_repack
• Fixed a performance issue in pgvector for index creation on halfvec data type
• Fixed a bug in aws_s3 causing import queries to occasionally get stuck and fail to terminate
This version also includes the following extension changes:.
• The plv8 extension was updated to 3.1.10.
PostgreSQL version 14.12 on Amazon RDS
PostgreSQL version 14.12 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.12 release.
New features and enhancements
• The blue/green deployment switchover won’t be blocked by the REFRESH MATERIALIZED 
VIEW statement.
• Fixed the permission denial for the CREATE DATABASE WITH OWNER statement.
• Upgraded the aws_s3 extension to version 1.2 to support the export to S3 with the KMS 
customer managed key.
• Fixed a pgvector compatibility issue with some of the previous generations of DB instances, such 
as m4.
PostgreSQL version 14.12-R2 on Amazon RDS 72
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
This version also includes the following extension updates:
• The aws_s3 extension was updated to 1.2.
• The orafce extension was updated to 4.9.4.
• The pg_hint_plan extension was updated to 1.4.2.
• The pg_partman extension was updated to 5.1.0.
• The pgvector extension was updated to 0.7.0.
• The postgis extension was updated to 3.4.2.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.11-R4 on Amazon RDS
PostgreSQL version 14.11-R4 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 14.11 release.
New features and enhancements
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
PostgreSQL version 14.11-R3 on Amazon RDS
PostgreSQL version 14.11-R3 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 14.11 release.
New features and enhancements
• Fixed a security exploit issue in plv8
• Fixed a security issue in pg_repack
This version also includes the following extension change:
• The plv8 extension was updated to 3.1.10.
PostgreSQL version 14.11-R4 on Amazon RDS 73
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 14.11-R2 on Amazon RDS
PostgreSQL version 14.11-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 14.11 release.
New features and enhancements.
• Fixed a bug preventing upgrades to PostGIS version 3.4.1.
• Fixed an error with the aws_s3 extension when the Region was not provided.
This version also includes the following extension changes:
• The pg_partman extension was updated to version 5.0.1.
• The pg_tle extension was updated to version 1.4.0.
• The pgactive extension was updated to version 2.1.3.
• The pgtap extension was updated to version 1.3.2.
• The pgvector extension was updated to version 0.6.2.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.11 on Amazon RDS
PostgreSQL version 14.11 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.11 release..
New features and enhancements
• Fixed the multisecond latency on the aws_lambda calls
• Fixed a bug preventing the termination of autovacuum
This version includes the following changes:
• The orafce extension was updated to version 4.9.0.
• The pg_cron extension was updated to version 1.6.2.
• The pgactive extension was updated to version 2.1.2.
PostgreSQL version 14.11-R2 on Amazon RDS 74
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pgvector extension was updated to 0.6.0.
• The PostGIS extension was updated to 3.4.1.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.10-R2 on Amazon RDS
PostgreSQL version 14.10-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 14.10 release.
New features and enhancements
• Fixed a crash in CatalogCacheComputeHashValue with dblink_connect due to a Null or
invalid connection.
• Backported run_as_owner to RPG 14
• Backported a security ﬁx for the logical replication apply worker that allows regular table 
owners to obtain privilege escalation to the subscription owner (an rds_superuser). The logical 
apply worker mitigates the risk by temporarily switching the role from the subscription owner 
to the table owner during logical apply.
In the cases of potential security breaches, the ﬁx will break your existing logical replication 
if any table in the subscription is owned by a regular user, and there are security-restricted 
operations attached to the table via triggers or default expressions. We recommend that you 
carefully examine the operations attached to the table if you notice the logical replication is 
broken after the upgrade. If all of the operations are as expected and you wish to revert the 
behavior of the logical replication so your application can continue, you can do so by setting 
the new parameter rds.run_logical_replication_as_subscription_owner to true. 
Be aware that by doing so your logical replication will be vulnerable to the aforementioned 
security risk again.
• Added rds.run_logical_replication_as_subscription_owner to the Amazon RDS 
parameter group.
• Supported the AWS SDK version of the aws_s3 extension.
• Fixed the overﬂow in the pg_transport extension.
• Removed the unsupported shared libraries from the engine binary.
This version includes the following change:
PostgreSQL version 14.10-R2 on Amazon RDS 75
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The plrust extension was updated to version 1.2.7.
PostgreSQL version 14.10 on Amazon RDS
PostgreSQL version 14.10 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.10 release.
New features and enhancements
• Fixed a bug where pg_database_size() with an invalid OID causes a crash.
• Added support for the rds.enable_pgactive parameter in rdsutils to avoid the warning 
message.
• Exposed RDKit guc param rdkit.morgan_fp_size.
• Fixed the bug where setting TABLESPACE with DEFAULT option in CREATE or ALTER DATABASE
fails.
• Added the pgactive extension.
This version includes the following changes:
• The h3-pg extension was updated to version 4.1.3.
• The hll extension was updated to version 2.18
• The oracle_fdw extension was updated to version 2.6.0.
• The orafce extension was updated to version 4.6.1.
• The pg_cron extension was updated to version 1.6.1.
• The pg_partman extension was updated to version 5.0.0.
• The pg_proctab extension was updated to version 0.0.10.
• The pgtap extension was updated to version 1.3.1.
• The pgvector extension was updated to version 0.5.1.
• The plprofiler extension was updated to version 4.2.4.
• The plrust extension was updated to version 1.2.6.
• The PostGIS extension was updated to version 3.4.0.
• The rdkit extension was updated to version 4.4.0.
PostgreSQL version 14.10 on Amazon RDS 76
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 14.9-R2 on Amazon RDS
PostgreSQL version 14.9-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 14.9 release.
New features and enhancements
• A new rds.cte_materialize_mode parameter was introduced which controls the 
materialization behavior of the query of a WITH clause, also known as a Common Table 
Expression. See WITH Queries for more information. The parameter values include the following:
• default: The WITH clause will be treated using the engine's default behavior.
• always: The full output of the query in the WITH clause will be materialized and the output 
reused in the outer query.
• never: The query in the WITH clause will be inlined with the outer query if possible. This 
parameter will also override the MATERIALIZED and NOT MATERIALIZED keywords supplied 
to the WITH clause.
This version also includes the following changes:
• The pgvector extension was updated to version 0.5.0.
• The plrust extension was updated to version 1.2.5.
• The rdkit extension was updated to version 4.3.0.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.9 on Amazon RDS
PostgreSQL version 14.9 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.9 release.
New features and enhancements
• A bug was ﬁxed preventing users with the rds_superuser role from creating schemas in 
databases owned by other users.
• Users with the rds_superuser role can now access toast tables in the pg_toast schema that 
are owned by other users.
• Fixed an issue where ALTER TABLE took a ShareLock and may cause deadlocks.
PostgreSQL version 14.9-R2 on Amazon RDS 77
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
This version also includes the following changes:
• The hypopg extension was updated to version 1.4.0.
• The orafce extension was updated to version 4.3.0.
• The pg_tle extension was updated to version 1.1.1.
• The pglogical extension was updated to version 2.4.3.
• The plrust extension was added at version 1.2.3.
• The PostGIS extension was updated to version 3.3.3
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.8-R2 on Amazon RDS (Deprecated)
PostgreSQL version 14.8-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 14.8 release.
New features and enhancements
• Fixed a Patroni 2.1.7 restart issue and instead enables replication slot from the disk
This version also includes the following change:
• The pgvector extension was updated to version 0.4.4.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.8 on Amazon RDS (Deprecated)
PostgreSQL version 14.8 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.8 release.
New features and enhancements
• Includes changes to allow rds-superuser to run the pg_stat_reset_slru function
• Fixed a security issue involving rds_sec_override which wasn't reset after the intended usage, 
allowing unauthorized access to restricted tables
• Added extension hypopg version 1.3.1
PostgreSQL version 14.8-R2 on Amazon RDS (Deprecated) 78
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Added extension pgvector version 0.4.1
• You can use logical_seed_lsn to determine the LSN at which a snapshot is taken in order to 
establish logical replication connection between the source and the restored target database. 
You can then use logical replication to continuously stream the newer data recorded after 
the LSN and synchronize the changes from publisher to subscriber. Speciﬁcally, it allows the 
customer to create a logical slot on a source RDS database, take a snapshot, restore the snapshot 
to a new RDS instance (target), and use the value of logical_seed_lsn() from the target instance 
to advance the logical slot on the source instance in order to subscribe the target to the source.
This version also includes the following changes:
• compat-collation-for-glibc was updated to version 1.8.
• The pg_cron extension was updated to version 1.5.2.
• The pg_tle extension was updated to version 1.0.4.
• The pglogical extension was updated to version 2.4.2.
• The PostGIS extension was updated to version 3.3.2.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.7 on Amazon RDS (Deprecated)
PostgreSQL version 14.7 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.7 release.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.6 on Amazon RDS (Deprecated)
PostgreSQL version 14.6 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.6 release.
New features and enhancements
• PostgreSQL version 14.6 added support for the tcn ("triggered change notiﬁcation") 
extension which generates notiﬁcation events on table changes via a trigger function called
triggered_change_notification. The tcn extension is useful for applications using drivers 
PostgreSQL version 14.7 on Amazon RDS (Deprecated) 79
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
which support asynchronous notiﬁcation. This makes it possible to notify all clients if the 
contents of a table have been changed, enabling them to take appropriate action in near-real 
time, such as updating a table cache or information display.
However, such functionality should only be used with care as it makes all data changes on the 
table available to all clients (including unprivileged users) through the notiﬁcation events when 
they listen on the tcn channel. It is the user’s responsibility to avoid using tcn trigger on a table 
with sensitive data to avoid information leakage.
This version includes the following changes:
• The seg extension version 1.4 was added.
• The tcn extension version 1.0 was added.
• The orafce extension was updated to version 3.24.
• The pgaudit extension was updated to version 1.6.2.
• The pgtap extension was updated to version 1.2.0.
• The rdkit extension was updated to version 4.2.0.
• The PostGIS dependency GDAL was updated to version 3.4.3.
• The wal2json extension was updated to version 2.5.
• The aws_s3 extension was updated to version 1.1.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.5 on Amazon RDS (Deprecated)
PostgreSQL version 14.5 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.5 release.
This version includes the following changes:
• The PostGIS extension was updated to version 3.1.7.
• The pg_partman extension was updated to version 4.6.2.
• The pgrouting extension was updated to version 3.2.2.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.5 on Amazon RDS (Deprecated) 80
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 14.4 on Amazon RDS (Deprecated)
PostgreSQL version 14.4 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.4 release.
New features and enhancements
• While this release includes other ﬁxes, a noteworthy ﬁx included in this release is for CREATE 
INDEX CONCURRENTLY and REINDEX CONCURRENTLY that can potentially cause silent data 
corruption of indexes. Amazon RDS has made the ﬁx for the index corruption available since 
the release of Amazon RDS for PostgreSQL 14.3. This release does not include any RDS speciﬁc 
changes or extension version updates.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.3 on Amazon RDS (Deprecated)
PostgreSQL version 14.3 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 14.3 release.
New features and enhancements
• This release includes Amazon RDS collations designed to help with data migration from EBCDIC-
based systems. For more information, see RDS for PostgreSQL collations for EBCDIC and other 
mainframe migrations.
• This release includes a ﬁx that was made available in the  PostgreSQL out-of-cycle release June 
16, 2022 that resolves the CREATE INDEX CONCURRENTLY and REINDEX CONCURRENTLY
issue. The issue aﬀects all community PostgreSQL 14 versions prior to 14.4. For information 
about how to detect and remediate the issue, see PostgreSQL 14 out-of-cycle release June 16, 
2022.
• Users with the rds_superuser role can now create roles for users.
This version also includes the following changes:
• The pglogical extension was updated to version 2.4.1.
• The pg_hint_plan extension was updated to version 1.4.
• The postgresql-hllextension was updated to version 2.16.
PostgreSQL version 14.4 on Amazon RDS (Deprecated) 81
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.2 on Amazon RDS (Deprecated)
PostgreSQL version 14.2 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in PostgreSQL 14.2.
This version also includes the following changes:
• The mysql_fdw extension version 2.7.0 is added. For more information, see Working with MySQL 
databases by using the mysql_fdw extension.
• The tds_fdw extension version 2.0.2 is added. For more information, see Working with SQL 
Server databases by using the tds_fdw extension in the Amazon RDS User Guide.
• The pgaudit extension is updated to 1.6.1. For information about using this extension with RDS 
for PostgreSQL, see Logging at the session and object level with the pgaudit extension.
• The lo (large objects) module is updated to version 1.1.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 14.1 on Amazon RDS (Deprecated)
PostgreSQL version 14.1 is now available on Amazon RDS. This release contains several 
improvements that were announced in PostgreSQL 14.1.
This version also includes the following changes:
• The old_snapshot  extension 1.0 is added. If you set old_snapshot_threshold to a value, this 
extension lets you map transaction ID to a timestamp.
• The amcheck extension was updated to version 1.3.
• The btree_gist extension was updated to version 1.6.
• The cube extension was updated to version 1.5.
• The hstore extension was updated to version 1.8.
• The intarray extension was updated to version 1.5.
• The pageinspect extension was updated to version 1.9.
• The pg_cron extension was updated to version 1.4
PostgreSQL version 14.2 on Amazon RDS (Deprecated) 82
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pg_partman extension was updated to version 4.6.0.
• The pg_repack extension was updated to version 1.4.7.
• The pg_stat_statements extension was updated to version 1.9.
• The pg_trgm extension was updated to version 1.6.
• The pgaudit extension was updated to version 1.6.
• The pgrouting extension was updated to version 3.2.0.
• The postgres_fdw extension was updated to version 1.1.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL 13 versions
Minor versions
• PostgreSQL version 13.23-R2 on Amazon RDS
• PostgreSQL version 13.23 on Amazon RDS
• PostgreSQL version 13.22-R2 on Amazon RDS
• PostgreSQL version 13.22 on Amazon RDS
• PostgreSQL version 13.21-R2 on Amazon RDS
• PostgreSQL version 13.21 on Amazon RDS
• PostgreSQL version 13.20-R2 on Amazon RDS
• PostgreSQL version 13.20 on Amazon RDS
• PostgreSQL version 13.19 on Amazon RDS
• PostgreSQL version 13.18-R3 on Amazon RDS
• PostgreSQL version 13.18-R2 on Amazon RDS
• PostgreSQL version 13.18 on Amazon RDS
• PostgreSQL version 13.17 on Amazon RDS
• PostgreSQL version 13.16-R3 on Amazon RDS
• PostgreSQL version 13.16-R2 on Amazon RDS
• PostgreSQL version 13.16 on Amazon RDS
• PostgreSQL version 13.15-R4 on Amazon RDS
PostgreSQL 13 versions 83
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• PostgreSQL version 13.15-R3 on Amazon RDS
• PostgreSQL version 13.15-R2 on Amazon RDS
• PostgreSQL version 13.15 on Amazon RDS
• PostgreSQL version 13.14-R4 on Amazon RDS
• PostgreSQL version 13.14-R3 on Amazon RDS
• PostgreSQL version 13.14-R2 on Amazon RDS
• PostgreSQL version 13.14 on Amazon RDS
• PostgreSQL version 13.13-R2 on Amazon RDS
• PostgreSQL version 13.13 on Amazon RDS
• PostgreSQL version 13.12-R2 on Amazon RDS
• PostgreSQL version 13.12 on Amazon RDS
• PostgreSQL version 13.11-R2 on Amazon RDS
• PostgreSQL version 13.11 on Amazon RDS
• PostgreSQL version 13.10 on Amazon RDS (Deprecated)
• PostgreSQL version 13.9 on Amazon RDS (Deprecated)
• PostgreSQL version 13.8 on Amazon RDS (Deprecated)
• PostgreSQL version 13.7 on Amazon RDS (Deprecated)
• PostgreSQL version 13.6 on Amazon RDS (Deprecated)
• PostgreSQL version 13.5 on Amazon RDS (Deprecated)
• PostgreSQL version 13.4 on Amazon RDS (Deprecated)
• PostgreSQL version 13.3 on Amazon RDS (Deprecated)
• PostgreSQL version 13.2 on Amazon RDS (Deprecated)
• PostgreSQL version 13.1 on Amazon RDS (Deprecated)
PostgreSQL version 13.23-R2 on Amazon RDS
PostgreSQL version 13.23-R2 is now available on Amazon RDS.
This version also includes the following changes:
• Fixed an issue on the plv8 extension regarding CREATE EXTENSION failure on older version.
PostgreSQL version 13.23-R2 on Amazon RDS 84
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 13.23 on Amazon RDS
PostgreSQL version 13.23 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.23 release.
General enhancements
This version also includes the following extension changes:
• The pg_tle extension was updated to version 1.5.2.
• The h3-pg extension was updated to version 4.2.3.
PostgreSQL version 13.22-R2 on Amazon RDS
PostgreSQL version 13.22-R2 is now available on Amazon RDS.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 13.22 on Amazon RDS
PostgreSQL version 13.22 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.22 release.
General enhancements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pg_repack extension was updated to version 1.5.2.
• The oracle_fdw extension was updated to version 2.8.0.
• The pgactive extension was updated to version 2.1.5.
PostgreSQL version 13.21-R2 on Amazon RDS
PostgreSQL version 13.21-R2 is now available on Amazon RDS.
PostgreSQL version 13.23 on Amazon RDS 85
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
General enhancements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 13.21 on Amazon RDS
PostgreSQL version 13.21 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.21 release.
General enhancements
• Fixed for the address_standardizer_data_us extension issue regarding ALTER EXTENSION 
UPDATE failure.
• Changed the Oracle client library version on x86 to 19.26.0.0.0.
• Fixed the pgactive extension unable to upgrade issue due to incorrect extension upgrade 
scripts which causes replication to break after engine upgrade.
This version also includes the following extension changes:
• The pg_repack extension was updated to version 1.5.1.
• The pglogical extension was updated to version 2.4.5.
• The PgAudit extension was updated to version 1.5.3.
PostgreSQL version 13.20-R2 on Amazon RDS
PostgreSQL version 13.20-R2 is now available on Amazon RDS.
Fixes and Improvements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
This version also includes the following extension changes:
PostgreSQL version 13.21 on Amazon RDS 86
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pgactive extension was updated to version 2.1.6.
PostgreSQL version 13.20 on Amazon RDS
PostgreSQL version 13.20 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.20 release.
PostgreSQL version 13.19 on Amazon RDS
PostgreSQL version 13.19 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.19 release.
New features and enhancements.
• In Blue/Green deployments, creating or modifying temporary objects is no longer classiﬁed as 
restricted DDL.
• Resolved an issue where DVB returned duplicate rows during slow vacuum analysis.
• Resolved CVE RUSTSEC-2024-0421 by upgrading URL Rust crate to 2.5.4. For more information, 
see RUSTSEC-2024-0421.
• Applied Promise.any error allocation ﬁx for V8 9.7.37, PLV8 3.1.10.
This version also includes the following extension changes:.
• The rds_tools extension was updated to 1.9.
• The orafce extension was updated to 4.14.0.
• The pg_cron extension was updated to 1.6.5.
• The pg_active extension was updated to 2.1.4.
• The prefix extension was updated to 1.2.10.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.18-R3 on Amazon RDS
PostgreSQL version 13.18-R3 is now available on Amazon RDS.
General enhancements
PostgreSQL version 13.20 on Amazon RDS 87
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
PostgreSQL version 13.18-R2 on Amazon RDS
PostgreSQL version 13.18-R2 is now available on Amazon RDS. This release contains ﬁx for
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 
13.18.
PostgreSQL version 13.18 on Amazon RDS
PostgreSQL version 13.18 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.18 release.
PostgreSQL version 13.17 on Amazon RDS
PostgreSQL version 13.17 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.17 release.
New features
• Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some 
connection slots are reserved for the new rds_reserved role, which is granted to Amazon 
RDS administrative users. The number of reserved connection slots is determined by the
rds.rds_reserved_connections parameter . You may need to adjust the value of the
max_connections parameter to account for the number of Amazon RDS reserved connection 
slots.
The rds_reserved role is a new predeﬁned role created by Amazon RDS. Predeﬁned roles 
and their privileges can't be changed. You can't drop, rename, or modify privileges for these 
predeﬁned roles. Attempting to modify a predeﬁned role results in an error.
• Unblocked ALTER TEMP TABLE and DROP TEMP TABLE in Blue/Green replication.
• Added the rds_tools.pg_ls_multixactdir() function for pg_multixact to monitor the 
directory disk space usage.
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
Updated features
• The oracle_fdw extension was updated to version 2.7.0.
PostgreSQL version 13.18-R2 on Amazon RDS 88
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The orafce extension was updated to version 4.13.4.
• The pg_cron extension was updated to version 1.6.4.
• The pg_hint_plan extension was updated to version 1.3.10.
• The pgvector extension was updated to version 0.8.0.
• The plprofiler extension was updated to version 4.2.5.
• The PostGIS extension was updated to version 3.4.3.
• The rds_tools extension was updated to version 1.7.
• The tds_fdw extension was updated to version 2.0.4.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.16-R3 on Amazon RDS
PostgreSQL version 13.16-R3 is now available on Amazon RDS. This release contains ﬁxes for
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 
13.16.
PostgreSQL version 13.16-R2 on Amazon RDS
PostgreSQL version 13.16-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 13.16 release.
New features and enhancements
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
PostgreSQL version 13.16 on Amazon RDS
PostgreSQL version 13.16 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.16 release.
New features and enhancements
• Delegated extension role was added.
This version also includes the following extension updates:
PostgreSQL version 13.16-R3 on Amazon RDS 89
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The hypopg extension was updated to 1.4.1.
• The mysql_fdw extension was updated to 2.9.2.
• The orafce extension was updated to 4.10.3.
• The pg_cron extension was updated to 1.6.3.
• The pgTAP extension was updated to 1.3.3.
• The pgvector extension was updated to 0.7.3.
• The wal2json extension was updated to 2.6.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.15-R4 on Amazon RDS
PostgreSQL version 13.15-R4 is now available on Amazon RDS. This release contains ﬁxed for
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 
13.15.
PostgreSQL version 13.15-R3 on Amazon RDS
PostgreSQL version 13.15-R3 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 13.15 release.
New features and enhancements
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
PostgreSQL version 13.15-R2 on Amazon RDS
PostgreSQL version 13.15-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 13.15 release.
New features and enhancements
• Includes support for four new crates in PL/Rust, including:
• regex
• serde
• serde_json
PostgreSQL version 13.15-R4 on Amazon RDS 90
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• url
• Fixed a security exploit issue in plv8
• Fixed a security issue in pg_repack
• Fixed a performance issue in pgvector for index creation on halfvec data type
• Fixed a bug in aws_s3 causing import queries to occasionally get stuck and fail to terminate
• Fixed a performance issue in aws_s3 and aws_lambda
This version also includes the following extension change:
• The plv8 extension was updated to 3.1.10.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.15 on Amazon RDS
PostgreSQL version 13.15 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.15 release.
New features and enhancements
• The blue/green deployment switchover won’t be blocked by the REFRESH MATERIALIZED 
VIEW statement.
• Fixed the permission denial for the CREATE DATABASE WITH OWNER statement.
• Upgraded the aws_s3 extension to version 1.2 to support the export to S3 with the KMS 
customer managed key.
• Fixed a pgvector compatibility issue with some of the previous generations of DB instances, such 
as m4.
This version also includes the following extension updates:
• The aws_s3 extension was updated to 1.2.
• The orafce extension was updated to 4.9.4.
• The pg_hint_plan extension was updated to 1.3.9.
• The pgvector extension was updated to 0.7.0.
• The postgis extension was updated to 3.4.2.
PostgreSQL version 13.15 on Amazon RDS 91
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.14-R4 on Amazon RDS
PostgreSQL version 13.14-R4 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 13.14 release.
New features and enhancements
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
PostgreSQL version 13.14-R3 on Amazon RDS
PostgreSQL version 13.14-R3 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 13.14 release.
New features and enhancements
• Fixed a security exploit issue in plv8
• Fixed a security issue in pg_repack
This version also includes the following extension change:
• The plv8 extension was updated to 3.1.10.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.14-R2 on Amazon RDS
PostgreSQL version 13.14-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 13.14 release.
New features and enhancements
• Fixed a bug preventing upgrades to PostGIS version 3.4.1.
This version also includes the following extension changes:
• The pg_partman extension was updated to version 4.5.1.
PostgreSQL version 13.14-R4 on Amazon RDS 92
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pg_tle extension was updated to version 1.4.0.
• The pgactive extension was updated to version 2.1.3.
• The pgtap extension was updated to version 1.3.2.
• The pgvector extension was updated to version 0.6.2.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.14 on Amazon RDS
PostgreSQL version 13.14 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.14 release..
New features and enhancements
• Fixed the multisecond latency on the aws_lambda calls
• Fixed a bug preventing the termination of autovacuum
This version includes the following changes:
• The orafce extension was updated to version 4.9.0.
• The pg_cron extension was updated to version 1.6.2.
• The pgactive extension was updated to version 2.1.2.
• The pgvector extension was updated to 0.6.0.
• The PostGIS extension was updated to 3.4.1.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.13-R2 on Amazon RDS
PostgreSQL version 13.13-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 13.13 release.
New features and enhancements
• Fixed a crash in CatalogCacheComputeHashValue with dblink_connect due to a Null or
invalid connection.
• Backported run_as_owner to RPG 13:
PostgreSQL version 13.14 on Amazon RDS 93
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Backported a security ﬁx for the logical replication apply worker that allows regular table 
owners to obtain privilege escalation to the subscription owner (an rds_superuser). The logical 
apply worker mitigates the risk by temporarily switching the role from the subscription owner 
to the table owner during logical apply.
In the cases of potential security breaches, the ﬁx will break your existing logical replication 
if any table in the subscription is owned by a regular user, and there are security-restricted 
operations attached to the table via triggers or default expressions. We recommend that you 
carefully examine the operations attached to the table if you notice the logical replication is 
broken after the upgrade. If all of the operations are as expected and you wish to revert the 
behavior of the logical replication so your application can continue, you can do so by setting 
the new parameter rds.run_logical_replication_as_subscription_owner to true. 
Be aware that by doing so your logical replication will be vulnerable to the aforementioned 
security risk again.
• Added rds.run_logical_replication_as_subscription_owner to the Amazon RDS 
parameter group.
• Fixed the overﬂow in the pg_transport extension.
• Removed the unsupported shared libraries from the engine binary.
This version includes the following change:
• The plrust extension was updated to version 1.2.7.
PostgreSQL version 13.13 on Amazon RDS
PostgreSQL version 13.13 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.13 release.
New features and enhancements
• Fixed a bug where pg_database_size() with an invalid OID causes a crash.
• Added support for the rds.enable_pgactive parameter in rdsutils to avoid the warning 
message.
• Exposed RDKit guc param rdkit.morgan_fp_size.
• Fixed the bug where setting TABLESPACE with DEFAULT option in CREATE or ALTER DATABASE
fails.
PostgreSQL version 13.13 on Amazon RDS 94
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Added the pgactive extension.
This version includes the following changes:
• The h3-pg extension was updated to version 4.1.3.
• The hll extension was updated to version 2.18
• The oracle_fdw extension was updated to version 2.6.0.
• The orafce extension was updated to version 4.6.1.
• The pg_cron extension was updated to version 1.6.1.
• The pg_proctab extension was updated to version 0.0.10.
• The pgtap extension was updated to version 1.3.1.
• The pgvector extension was updated to version 0.5.1.
• The plprofiler extension was updated to version 4.2.4.
• The plrust extension was updated to version 1.2.6.
• The PostGIS extension was updated to version 3.4.0.
PostgreSQL version 13.12-R2 on Amazon RDS
PostgreSQL version 13.12-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 13.12 release.
This version includes the following change:
• The pgvector extension was updated to version 0.5.0.
• The plrust extension was updated to version 1.2.5.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.12 on Amazon RDS
PostgreSQL version 13.12 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.12 release.
PostgreSQL version 13.12-R2 on Amazon RDS 95
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
New features and enhancements
• A bug was ﬁxed preventing users with the rds_superuser role from creating schemas in 
databases owned by other users.
• Users with the rds_superuser role can now access toast tables in the pg_toast schema that 
are owned by other users.
• Fixed an issue where ALTER TABLE took a ShareLock and may cause deadlocks.
This version also includes the following changes:
• hypopg was updated to 1.4.0
• orafce was updated to 4.3.0
• pg_tle was added at version 1.1.1
• pglogical was updated to 2.4.3
• plrust was added at version 1.2.3
• PostGIS was updated to 3.3.3
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.11-R2 on Amazon RDS
PostgreSQL version 13.11-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 13.11 release.
This version also includes the following change:
• The pgvector extension was updated to version 0.4.4.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 14.
PostgreSQL version 13.11 on Amazon RDS
PostgreSQL version 13.11 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.11 release.
PostgreSQL version 13.11-R2 on Amazon RDS 96
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
New features and enhancements
• Includes changes to allow rds-superuser to run the pg_stat_reset_slru function
• Fixed a security issue involving rds_sec_override which wasn't reset after the intended usage, 
allowing unauthorized access to restricted tables
• Added extension hypopg version 1.3.1
• Added extension pgvector version 0.4.1
• You can use logical_seed_lsn to determine the LSN at which a snapshot is taken in order to 
establish logical replication connection between the source and the restored target database. 
You can then use logical replication to continuously stream the newer data recorded after 
the LSN and synchronize the changes from publisher to subscriber. Speciﬁcally, it allows the 
customer to create a logical slot on a source RDS database, take a snapshot, restore the snapshot 
to a new RDS instance (target), and use the value of logical_seed_lsn() from the target instance 
to advance the logical slot on the source instance in order to subscribe the target to the source.
This version also includes the following changes:
• compat-collation-for-glibc was updated to version 1.8
• libcompat was updated to version 1.8
• pg_cron was updated to version 1.5.2
• pglogical was updated to version 2.4.2
• PostGIS was updated to version 3.3.2
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.10 on Amazon RDS (Deprecated)
PostgreSQL version 13.10 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.10 release.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.9 on Amazon RDS (Deprecated)
PostgreSQL version 13.9 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 13.9 release.
PostgreSQL version 13.10 on Amazon RDS (Deprecated) 97
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
New features and enhancements
• PostgreSQL version 13.9 added support for the tcn ("triggered change notiﬁcation") 
extension which generates notiﬁcation events on table changes via a trigger function called
triggered_change_notification. The tcn extension is useful for applications using drivers 
which support asynchronous notiﬁcation. This makes it possible to notify all clients if the 
contents of a table have been changed, enabling them to take appropriate action in near-real 
time, such as updating a table cache or information display.
However, such functionality should only be used with care as it makes all data changes on the 
table available to all clients (including unprivileged users) through the notiﬁcation events when 
they listen on the tcn channel. It is the user’s responsibility to avoid using tcn trigger on a table 
with sensitive data to avoid information leakage.
This version includes the following changes:
• The seg extension version 1.3 is added.
• The tcn extension version 1.0 is added.
• The orafce extension is updated to 3.24.
• The pgaudit extension is updated to 1.5.2.
• The pgtap extension is updated to 1.2.0.
• The PostGIS dependency GDAL is updated to 3.4.3.
• The PostGIS dependency PROJ is updated to 8.0.1.
• The wal2json extension is updated to 2.5.
• The aws_s3 extension is updated to 1.1.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.8 on Amazon RDS (Deprecated)
PostgreSQL version 13.8 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in PostgreSQL 13.8.
This version includes the following changes:
• The PostGIS extension is updated to 3.1.7
PostgreSQL version 13.8 on Amazon RDS (Deprecated) 98
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pgRouting extension is updated to 3.1.4
For information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.7 on Amazon RDS (Deprecated)
PostgreSQL version 13.7 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in PostgreSQL 13.7.
This version also includes the following changes:
• The pglogical extension is updated to 2.4.1
For information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.6 on Amazon RDS (Deprecated)
PostgreSQL version 13.6 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in PostgreSQL 13.6.
This version also includes the following changes:
• The mysql_fdw extension version 2.7.0 is added. For more information, see Working with MySQL 
databases by using the mysql_fdw extension in the Amazon RDS User Guide.
• The tds_fdw extension version 2.0.2 is added. For more information, see Working with SQL 
Server databases by using the tds_fdw extension in the Amazon RDS User Guide.
• The pgaudit extension is updated to 1.5.1. For information about using this extension with RDS 
for PostgreSQL, see Logging at the session and object level with the pgaudit extension in the
Amazon RDS User Guide.
• The lo (large objects) module is updated to version 1.1.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.5 on Amazon RDS (Deprecated)
PostgreSQL version 13.5 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in PostgreSQL 13.5.
PostgreSQL version 13.7 on Amazon RDS (Deprecated) 99
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
This version also includes the following change:
• The pg_cron extension is updated to 1.4.1
For information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.4 on Amazon RDS (Deprecated)
PostgreSQL version 13.4 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in PostgreSQL 13.4.
This version also includes the following changes:
• The flow_control extension version 1.0 is added in this release.
• The spi module extensions reﬁnt, autoinc, inset_username, and moddatetime version 1.0 are 
added.
• The pgrouting extension is updated to version 3.1.3.
• The pglogical extension is updated to version 2.4.0.
• The PostGIS extension is updated to version 3.1.4, along with the following related extensions:
• address_standardizer
• address_standardizer_data_us
• PostGIS_raster
• PostGIS_tiger_geocoder
• PostGIS_topology
For information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.3 on Amazon RDS (Deprecated)
PostgreSQL version 13.3 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in PostgreSQL 13.3.
This version also includes the following changes:
• The oracle_fdw extension version 2.3.0 is added. For more information, see Working with Oracle 
databases by using the oracle_fdw extension in the Amazon RDS User Guide.
• The orafce extension is updated to version 3.15.
PostgreSQL version 13.4 on Amazon RDS (Deprecated) 100
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The pg_cron extension is updated to version 1.3.1.
• The  pg_partman extension is updated to version 4.5.1.
• The PostGIS extension is updated to version 3.0.3, along with the following related extensions:
• address_standardizer
• address_standardizer_data_us
• PostGIS_raster
• PostGIS_tiger_geocoder
• PostGIS_topology
For information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.2 on Amazon RDS (Deprecated)
PostgreSQL version 13.2 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in PostgreSQL 13.2.
This version also added the following new extensions:
• The aws_lambda extension version 1.0. For more information, see  Invoking an AWS Lambda 
function from an RDS for PostgreSQL DB instance in the Amazon RDS User Guide.
• The pg_bigm extension version 1.2.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.1 on Amazon RDS (Deprecated)
PostgreSQL version 13.1 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in PostgreSQL 13.0 and PostgreSQL 13.1.
This version added:
• The bool_plperl extension version 1.0.
• The rds_tools extension version 1.0. For more information, see  Checking for users with non-
SCRAM passwords .
For information on all extensions, see Extensions supported for RDS for PostgreSQL 13.
PostgreSQL version 13.2 on Amazon RDS (Deprecated) 101
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL 12 versions (Some of these versions have reached 
the end of standard support or deprecated.)
Minor versions
• PostgreSQL version 12.22-R3 on Amazon RDS (This version has reached the end of standard 
support.)
• PostgreSQL version 12.22-R2 on Amazon RDS (This version has reached the end of standard 
support.)
• PostgreSQL version 12.22 on Amazon RDS (This version has reached the end of standard 
support.)
• PostgreSQL version 12.21 on Amazon RDS (Deprecated)
• PostgreSQL version 12.20-R3 on Amazon RDS (Deprecated)
• PostgreSQL version 12.20-R2 on Amazon RDS (Deprecated)
• PostgreSQL version 12.20 on Amazon RDS (Deprecated)
• PostgreSQL version 12.19-R4 on Amazon RDS (Deprecated)
• PostgreSQL version 12.19-R3 on Amazon RDS (Deprecated)
• PostgreSQL version 12.19-R2 on Amazon RDS (Deprecated)
• PostgreSQL version 12.19 on Amazon RDS (Deprecated)
• PostgreSQL version 12.18-R4 on Amazon RDS (Deprecated)
• PostgreSQL version 12.18-R3 on Amazon RDS (Deprecated)
• PostgreSQL version 12.18-R2 on Amazon RDS (Deprecated)
• PostgreSQL version 12.18 on Amazon RDS (Deprecated)
• PostgreSQL version 12.17-R2 on Amazon RDS (Deprecated)
• PostgreSQL version 12.17 on Amazon RDS (Deprecated)
• PostgreSQL version 12.16-R2 on Amazon RDS (Deprecated)
• PostgreSQL version 12.16 on Amazon RDS (Deprecated)
• PostgreSQL version 12.15 on Amazon RDS (Deprecated)
• PostgreSQL version 12.14 on Amazon RDS (Deprecated)
• PostgreSQL version 12.13 on Amazon RDS (Deprecated)
• PostgreSQL version 12.12 on Amazon RDS (Deprecated)
• PostgreSQL version 12.11 on Amazon RDS (Deprecated)
PostgreSQL 12 versions (Some of these versions have reached the end of standard support or 
deprecated.)
102
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• PostgreSQL version 12.10 on Amazon RDS (Deprecated)
• PostgreSQL version 12.9 on Amazon RDS (Deprecated)
• PostgreSQL version 12.8 on Amazon RDS (Deprecated)
• PostgreSQL version 12.7 on Amazon RDS (Deprecated)
• PostgreSQL version 12.6 on Amazon RDS (Deprecated)
• PostgreSQL version 12.5 on Amazon RDS (Deprecated)
• PostgreSQL version 12.4 on Amazon RDS (Deprecated)
• PostgreSQL version 12.3 on Amazon RDS (Deprecated)
• PostgreSQL version 12.2 on Amazon RDS (Deprecated)
PostgreSQL version 12.22-R3 on Amazon RDS (This version has reached 
the end of standard support.)
PostgreSQL version 12.22-R3 is now available on Amazon RDS.
General enhancements
• Updated V8 engine to version 11.5.150.2 for the plv8 extension 3.1.10.
PostgreSQL version 12.22-R2 on Amazon RDS (This version has reached 
the end of standard support.)
PostgreSQL version 12.22-R2 is now available on Amazon RDS. This release contains several ﬁx for 
PLV8 CVE-2022-4174 for PostgreSQL announced in PostgreSQL 12.22.
PostgreSQL version 12.22 on Amazon RDS (This version has reached the 
end of standard support.)
PostgreSQL version 12.22 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 12.22 release.
PostgreSQL version 12.21 on Amazon RDS (Deprecated)
PostgreSQL version 12.21 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in PostgreSQL 12.21.
PostgreSQL version 12.22-R3 on Amazon RDS (This version has reached the end of standard support.) 103
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
New features
• Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some 
connection slots are reserved for the new rds_reserved role, which is granted to Amazon 
RDS administrative users. The number of reserved connection slots is determined by the
rds.rds_reserved_connections parameter . You may need to adjust the value of the
max_connections parameter to account for the number of Amazon RDS reserved connection 
slots.
The rds_reserved role is a new predeﬁned role created by Amazon RDS. Predeﬁned roles 
and their privileges can't be changed. You can't drop, rename, or modify privileges for these 
predeﬁned roles. Attempting to modify a predeﬁned role results in an error.
• Unblocked ALTER TEMP TABLE and DROP TEMP TABLE in Blue/Green replication.
• Added the rds_tools.pg_ls_multixactdir() function for pg_multixact to monitor the 
directory disk space usage.
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
Updated features
• The oracle_fdw extension was updated to version 2.7.0.
• The orafce extension was updated to version 4.13.4.
• The pg_cron extension was updated to version 1.6.4.
• The pg_hint_plan extension was updated to version 1.3.10.
• The pgvector extension was updated to version 0.7.4.
• The PostGIS extension was updated to version 3.4.3.
• The rds_tools extension was updated to version 1.7.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.20-R3 on Amazon RDS (Deprecated)
PostgreSQL version 12.20-R3 is now available on Amazon RDS. This release contains ﬁxes for
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 
12.20.
PostgreSQL version 12.20-R3 on Amazon RDS (Deprecated) 104
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 12.20-R2 on Amazon RDS (Deprecated)
PostgreSQL version 12.20-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 12.20 release.
New features and enhancements
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
PostgreSQL version 12.20 on Amazon RDS (Deprecated)
PostgreSQL version 12.20 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 12.20 release.
New features and enhancements
• Delegated extension role was added.
This version also includes the following extension updates:
• The orafce extension was updated to 4.10.3.
• The pg_cron extension was updated to 1.6.3.
• The pgTAP extension was updated to 1.3.3.
• The pgvector extension was updated to 0.7.3.
• The wal2json extension was updated to 2.6.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.19-R4 on Amazon RDS (Deprecated)
PostgreSQL version 12.19-R4 is now available on Amazon RDS. This release contains ﬁxes for
CVE-2022-4174 and Rust CVE RUSTSEC-2024-042 for PostgreSQL announced in PostgreSQL 
12.19.
PostgreSQL version 12.19-R3 on Amazon RDS (Deprecated)
PostgreSQL version 12.19-R3 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 12.19 release.
PostgreSQL version 12.20-R2 on Amazon RDS (Deprecated) 105
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
New features and enhancements
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
PostgreSQL version 12.19-R2 on Amazon RDS (Deprecated)
PostgreSQL version 12.19-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 12.19 release.
New features and enhancements
• Fixed a security exploit issue in plv8
• Fixed a security issue in pg_repack
• Fixed a performance issue in pgvector for index creation on halfvec data type
• Fixed a bug in aws_s3 causing import queries to occasionally get stuck and fail to terminate
• Fixed a performance issue in aws_s3 and aws_lambda
This version also includes the following extension change:
• The plv8 extension was updated to 3.1.10.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.19 on Amazon RDS (Deprecated)
PostgreSQL version 12.19 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 12.19 release.
New features and enhancements
• The blue/green deployment switchover won’t be blocked by the REFRESH MATERIALIZED 
VIEW statement.
• Fixed the permission denial for the CREATE DATABASE WITH OWNER statement.
• Upgraded the aws_s3 extension to version 1.2 to support the export to S3 with the KMS 
customer managed key.
• Fixed a pgvector compatibility issue with some of the previous generations of DB instances, such 
as m4.
PostgreSQL version 12.19-R2 on Amazon RDS (Deprecated) 106
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
This version also includes the following extension updates:
• The aws_s3 extension was updated to 1.2.
• The orafce extension was updated to 4.9.4.
• The pg_hint_plan extension was updated to 1.3.9.
• The pgvector extension was updated to 0.7.0.
• The postgis extension was updated to 3.4.2.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.18-R4 on Amazon RDS (Deprecated)
PostgreSQL version 12.18-R4 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 12.18 release.
New features and enhancements
• Fixed potential incompatibilities in the plv8 extension occurring after database upgrades.
PostgreSQL version 12.18-R3 on Amazon RDS (Deprecated)
PostgreSQL version 12.18-R3 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 12.18 release..
New features and enhancements
• Fixed a security exploit issue in plv8
• Fixed a security issue in pg_repack
This version also includes the following extension change:
• The plv8 extension was updated to 3.1.10.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.18-R4 on Amazon RDS (Deprecated) 107
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 12.18-R2 on Amazon RDS (Deprecated)
PostgreSQL version 12.18-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 12.18 release..
This version includes the following extension changes:
• The pg_partman extension was updated to version 5.0.1.
• The pgactive extension was updated to version 2.1.3.
• The pgtap extension was updated to version 1.3.2.
• The pgvector extension was updated to version 0.6.2.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.18 on Amazon RDS (Deprecated)
PostgreSQL version 12.18 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 12.18 release..
New features and enhancements
• Fixed the multisecond latency on the aws_lambda calls
• Fixed a bug preventing the termination of autovacuum
This version includes the following changes:
• The orafce extension was updated to version 4.9.0.
• The pg_cron extension was updated to version 1.6.2.
• The pgactive extension was updated to version 2.1.2.
• The pgvector extension was updated to 0.6.0.
• The PostGIS extension was updated to 3.4.1.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.18-R2 on Amazon RDS (Deprecated) 108
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 12.17-R2 on Amazon RDS (Deprecated)
PostgreSQL version 12.17-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 12.17 release.
New features and enhancements
• Fixed a crash in CatalogCacheComputeHashValue with dblink_connect due to a Null or
invalid connection.
• Backported run_as_owner to RPG 12:
• Backported a security ﬁx for the logical replication apply worker that allows regular table 
owners to obtain privilege escalation to the subscription owner (an rds_superuser). The logical 
apply worker mitigates the risk by temporarily switching the role from the subscription owner 
to the table owner during logical apply.
In the cases of potential security breaches, the ﬁx will break your existing logical replication 
if any table in the subscription is owned by a regular user, and there are security-restricted 
operations attached to the table via triggers or default expressions. We recommend that you 
carefully examine the operations attached to the table if you notice the logical replication is 
broken after the upgrade. If all of the operations are as expected and you wish to revert the 
behavior of the logical replication so your application can continue, you can do so by setting 
the new parameter rds.run_logical_replication_as_subscription_owner to true. 
Be aware that by doing so your logical replication will be vulnerable to the aforementioned 
security risk again.
• Added rds.run_logical_replication_as_subscription_owner to the Amazon RDS 
parameter group.
• Fixed the overﬂow in the pg_transport extension.
• Removed the unsupported shared libraries from the engine binary.
PostgreSQL version 12.17 on Amazon RDS (Deprecated)
PostgreSQL version 12.17 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 12.17 release.
New features and enhancements
• Fixed a bug where pg_database_size() with an invalid OID causes a crash.
PostgreSQL version 12.17-R2 on Amazon RDS (Deprecated) 109
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Added support for the rds.enable_pgactive parameter in rdsutils to avoid the warning 
message.
• Exposed RDKit guc param rdkit.morgan_fp_size.
• Fixed the bug where setting TABLESPACE with DEFAULT option in CREATE or ALTER DATABASE
fails.
• Added the pgactive extension.
This version includes the following changes:
• The hll extension was updated to version 2.18
• The oracle_fdw extension was updated to version 2.6.0.
• The orafce extension was updated to version 4.6.1.
• The pg_cron extension was updated to version 1.6.1.
• The pg_proctab extension was updated to version 0.0.10.
• The pgtap extension was updated to version 1.3.1.
• The pgvector extension was updated to version 0.5.1.
• The plprofiler extension was updated to version 4.2.4.
• The PostGIS extension was updated to version 3.4.0.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.16-R2 on Amazon RDS (Deprecated)
PostgreSQL version 12.16-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 12.16 release.
New features and enhancements
• The pgvector extension was added.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.16-R2 on Amazon RDS (Deprecated) 110
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 12.16 on Amazon RDS (Deprecated)
PostgreSQL version 12.16 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 12.16 release.
New features and enhancements
• A bug was ﬁxed preventing users with the rds_superuser role from creating schemas in 
databases owned by other users.
• Users with the rds_superuser role can now access toast tables in the pg_toast schema that 
are owned by other users.
• Fixed an issue where ALTER TABLE took a ShareLock and may cause deadlocks.
This version also includes the following changes:
• The orafce extension was updated to version 4.3.0.
• The pglogical extension was updated to version 2.4.3.
• The PostGIS extension was updated to version 3.3.3.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.15 on Amazon RDS (Deprecated)
PostgreSQL version 12.15 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 12.15 release.
New features and enhancements
• Fixed a security issue involving rds_sec_override which wasn't reset after the intended usage, 
allowing unauthorized access to restricted tables
• You can use logical_seed_lsn to determine the LSN at which a snapshot is taken in order to 
establish logical replication connection between the source and the restored target database. 
You can then use logical replication to continuously stream the newer data recorded after 
the LSN and synchronize the changes from publisher to subscriber. Speciﬁcally, it allows the 
customer to create a logical slot on a source RDS database, take a snapshot, restore the snapshot 
to a new RDS instance (target), and use the value of logical_seed_lsn() from the target instance 
to advance the logical slot on the source instance in order to subscribe the target to the source.
PostgreSQL version 12.16 on Amazon RDS (Deprecated) 111
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
This version also includes the following changes:
• compat-collation-for-glibc was updated to version 1.8
• pg_cron was updated to version 1.5.2
• pglogical was updated to version 2.4.2
• PostGIS was updated to version 3.3.2
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.14 on Amazon RDS (Deprecated)
PostgreSQL version 12.14 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 12.14 release.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.13 on Amazon RDS (Deprecated)
PostgreSQL version 12.13 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 12.13 release.
New features and enhancements
• PostgreSQL version 12.13 added support for the tcn ("triggered change notiﬁcation") 
extension which generates notiﬁcation events on table changes via a trigger function called
triggered_change_notification. The tcn extension is useful for applications using drivers 
which support asynchronous notiﬁcation. This makes it possible to notify all clients if the 
contents of a table have been changed, enabling them to take appropriate action in near-real 
time, such as updating a table cache or information display.
However, such functionality should only be used with care as it makes all data changes on the 
table available to all clients (including unprivileged users) through the notiﬁcation events when 
they listen on the tcn channel. It is the user’s responsibility to avoid using tcn trigger on a table 
with sensitive data to avoid information leakage.
This version includes the following changes:
• The seg extension version 1.3 is added.
PostgreSQL version 12.14 on Amazon RDS (Deprecated) 112
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The tcn extension version 1.0 is added.
• The orafce extension is updated to 3.24.
• The pgaudit extension is updated to 1.4.3.
• The pgtap extension is updated to 1.2.0.
• The PostGIS dependency GDAL is updated to 3.4.3.
• The PostGIS dependency PROJ is updated to 7.0.1.
• The wal2json extension is updated to 2.5.
• The aws_s3 extension is updated to 1.1.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.12 on Amazon RDS (Deprecated)
PostgreSQL version 12.12 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in PostgreSQL 12.12.
This version includes the following changes:
• The PostGIS extension is updated to 3.1.7
• The pgRouting extension is updated to 3.0.6
For information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.11 on Amazon RDS (Deprecated)
PostgreSQL version 12.11 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in PostgreSQL 12.11.
This version also includes the following changes:
• The pglogical extension is updated to 2.4.1.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.12 on Amazon RDS (Deprecated) 113
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 12.10 on Amazon RDS (Deprecated)
PostgreSQL version 12.10 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in 12.10.
This version also includes the following changes:
• The pgaudit extension is updated to 1.4.2. For information about using this extension with RDS 
for PostgreSQL, see Logging at the session and object level with the pgaudit extension.
• The lo (large objects) module is updated to version 1.1.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.9 on Amazon RDS (Deprecated)
PostgreSQL version 12.9 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in 12.9.
This version also includes the following changes:
• The pg_cron extension is updated to 1.4.1
• The pg_hint_plan extension is updated to 1.3.7.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.8 on Amazon RDS (Deprecated)
PostgreSQL version 12.8 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in 12.8.
This version also includes the following changes:
• The pgRouting extension is updated to version 3.0.5.
• The pglogical extension is updated to version 2.4.0.
• The PostGIS extension is updated to version 3.1.4, along with the following related extensions:
• address_standardizer
• address_standardizer_data_us
• PostGIS_raster
PostgreSQL version 12.10 on Amazon RDS (Deprecated) 114
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• PostGIS_tiger_geocoder
• PostGIS_topology
For information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.7 on Amazon RDS (Deprecated)
PostgreSQL version 12.7 is now available on Amazon RDS. PostgreSQL version 12.7 contains 
several improvements that were announced for PostgreSQL release 12.7.
This version also includes the following changes:
• The oracle_fdw extension version 2.3.0 is added. For more information, see Working with Oracle 
databases by using the oracle_fdw extension in the Amazon RDS User Guide.
• The orafce extension is updated to version 3.15.
• The pg_cron extension is updated to version 1.3.1.
• The pg_partman extension is updated to version 4.5.1.
• The PostGIS extension is updated to version 3.0.3, along with the following related extensions:
• address_standardizer
• address_standardizer_data_us
• PostGIS_raster
• PostGIS_tiger_geocoder
• PostGIS_topology
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.6 on Amazon RDS (Deprecated)
PostgreSQL version 12.6 is now available on Amazon RDS. PostgreSQL version 12.6 contains 
several improvements that were announced for PostgreSQL release 12.6.
This version also includes the following changes:
• The aws_lambda extension version 1.0 is added. For more information, see  Invoking an AWS 
Lambda function from an RDS for PostgreSQL DB instance in the Amazon RDS User Guide.
• The pg_bigm extension version 1.2 is added.
PostgreSQL version 12.7 on Amazon RDS (Deprecated) 115
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The PostGIS extension is updated to version 3.0.2.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.5 on Amazon RDS (Deprecated)
PostgreSQL version 12.5 is now available on Amazon RDS. PostgreSQL version 12.5 contains 
several improvements that were announced for PostgreSQL release 12.5.
This version also includes the following changes:
• Added the pg_partman extension version 4.4.0. For more information, see  Managing 
PostgreSQL partitions with the pg_partman extension in the Amazon RDS User Guide.
• Added the pg_cron extension version 1.3.0. For more information, see  Scheduling maintenance 
with the PostgreSQL pg_cron extension in the Amazon RDS User Guide.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.4 on Amazon RDS (Deprecated)
PostgreSQL version 12.4 is now available on Amazon RDS. PostgreSQL version 12.4 contains 
several improvements that were announced for PostgreSQL release 12.4.
This version also includes the following changes:
• Added the pg_proctab extension version 0.0.9
• Added the rdkit extension version 3.8
• Upgraded the aws_s3 extension to version 1.1.
• Upgraded the pglogical extension to version 2.3.2
• Upgraded the wal2json extension to version 2.3
For information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.3 on Amazon RDS (Deprecated)
PostgreSQL version 12.3 is now available on Amazon RDS. PostgreSQL version 12.3 contains 
several improvements that were announced for PostgreSQL release 12.3.
PostgreSQL version 12.5 on Amazon RDS (Deprecated) 116
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
This version also includes the following changes:
• Upgraded the pg_hint_plan extension to version 1.3.5.
• Upgraded the pglogical extension to version 2.3.1.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL version 12.2 on Amazon RDS (Deprecated)
PostgreSQL version 12.2 is now available on Amazon RDS. PostgreSQL version 12.2 contains 
several improvements that were announced for PostgreSQL releases 12.0, 12.1, and 12.2.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 12.
PostgreSQL 11 versions (Some of these versions have reached 
the end of standard support or deprecated.)
Minor versions
• PostgreSQL version 11.22-R2 on Amazon RDS (This version has reached the end of standard 
support.)
• PostgreSQL version 11.22 on Amazon RDS (This version has reached the end of standard 
support.)
• PostgreSQL version 11.21 on Amazon RDS (Deprecated)
• PostgreSQL version 11.20 on Amazon RDS (Deprecated)
• PostgreSQL version 11.19 on Amazon RDS (Deprecated)
• PostgreSQL version 11.18 on Amazon RDS (Deprecated)
• PostgreSQL version 11.17 on Amazon RDS (Deprecated)
• PostgreSQL version 11.16 on Amazon RDS (Deprecated)
• PostgreSQL version 11.15 on Amazon RDS (Deprecated)
• PostgreSQL version 11.14 on Amazon RDS (Deprecated)
• PostgreSQL version 11.13 on Amazon RDS (Deprecated)
• PostgreSQL version 11.12 on Amazon RDS (Deprecated)
• PostgreSQL version 11.11 on Amazon RDS (Deprecated)
• PostgreSQL version 11.10 on Amazon RDS (Deprecated)
PostgreSQL version 12.2 on Amazon RDS (Deprecated) 117
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• PostgreSQL version 11.9 on Amazon RDS (Deprecated)
• PostgreSQL version 11.8 on Amazon RDS (Deprecated)
• PostgreSQL version 11.7 on Amazon RDS (Deprecated)
• PostgreSQL version 11.6 on Amazon RDS (Deprecated)
• PostgreSQL version 11.5 on Amazon RDS (Deprecated)
• PostgreSQL version 11.4 on Amazon RDS (Deprecated)
• PostgreSQL version 11.2 on Amazon RDS (Deprecated)
• PostgreSQL version 11.1 on Amazon RDS (Deprecated)
PostgreSQL version 11.22-R2 on Amazon RDS (This version has reached 
the end of standard support.)
PostgreSQL version 11.22-R2 is now available on Amazon RDS. This release contains several ﬁxes 
and improvements for PostgreSQL announced in the PostgreSQL 11.22 release.
New features and enhancements
• Backported run_as_owner to RPG 11:
• Backported a security ﬁx for the logical replication apply worker that allows regular table 
owners to obtain privilege escalation to the subscription owner (an rds_superuser). The logical 
apply worker mitigates the risk by temporarily switching the role from the subscription owner 
to the table owner during logical apply.
In the cases of potential security breaches, the ﬁx will break your existing logical replication 
if any table in the subscription is owned by a regular user, and there are security-restricted 
operations attached to the table via triggers or default expressions. We recommend that you 
carefully examine the operations attached to the table if you notice the logical replication is 
broken after the upgrade. If all of the operations are as expected and you wish to revert the 
behavior of the logical replication so your application can continue, you can do so by setting 
the new parameter rds.run_logical_replication_as_subscription_owner to true. 
Be aware that by doing so your logical replication will be vulnerable to the aforementioned 
security risk again.
• Added rds.run_logical_replication_as_subscription_owner to the Amazon RDS 
parameter group.
• Fixed the overﬂow in the pg_transport extension.
PostgreSQL version 11.22-R2 on Amazon RDS (This version has reached the end of standard support.) 118
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Removed the unsupported shared libraries from the engine binary.
PostgreSQL version 11.22 on Amazon RDS (This version has reached the 
end of standard support.)
PostgreSQL version 11.22 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 11.22 release.
New features and enhancements
• Fixed a bug where pg_database_size() with an invalid OID causes a crash.
• Added support for the rds.enable_pgactive parameter in rdsutils to avoid the warning 
message.
• Exposed RDKit guc param rdkit.morgan_fp_size.
• Fixed the bug where setting TABLESPACE with DEFAULT option in CREATE or ALTER DATABASE
fails.
• Added the pgactive extension.
This version includes the following changes:
• The hll extension was updated to version 2.18
• The orafce extension was updated to version 4.6.1.
• The pg_proctab extension was updated to version 0.0.10.
• The pgtap extension was updated to version 1.3.1.
• The plprofiler extension was updated to version 4.2.4.
PostgreSQL version 11.21 on Amazon RDS (Deprecated)
PostgreSQL version 11.21 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 11.21 release.
New features and enhancements
• A bug was ﬁxed preventing users with the rds_superuser role from creating schemas in 
databases owned by other users.
PostgreSQL version 11.22 on Amazon RDS (This version has reached the end of standard support.) 119
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Users with the rds_superuser role can now access toast tables in the pg_toast schema that 
are owned by other users.
• Fixed an issue where ALTER TABLE took a ShareLock and may cause deadlocks.
This version also includes the following changes:
• The orafce extension was updated to version 4.3.0.
• The pglogical extension was updated to version 2.4.3.
• The PostGIS extension was updated to version 3.3.3.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.20 on Amazon RDS (Deprecated)
PostgreSQL version 11.20 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 11.20 release.
New features and enhancements
• Fixed a security issue involving rds_sec_override which wasn't reset after the intended usage, 
allowing unauthorized access to restricted tables
• You can use logical_seed_lsn to determine the LSN at which a snapshot is taken in order to 
establish logical replication connection between the source and the restored target database. 
You can then use logical replication to continuously stream the newer data recorded after 
the LSN and synchronize the changes from publisher to subscriber. Speciﬁcally, it allows the 
customer to create a logical slot on a source RDS database, take a snapshot, restore the snapshot 
to a new RDS instance (target), and use the value of logical_seed_lsn() from the target instance 
to advance the logical slot on the source instance in order to subscribe the target to the source.
This version also includes the following changes:
• compat-collation-for-glibc was updated to version 1.8
• pglogical was updated to version 2.4.2
• PostGIS was updated to version 3.3.2
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.20 on Amazon RDS (Deprecated) 120
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 11.19 on Amazon RDS (Deprecated)
PostgreSQL version 11.19 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 11.19 release.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.18 on Amazon RDS (Deprecated)
PostgreSQL version 11.18 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 11.18 release.
New features and enhancements
• PostgreSQL version 11.18 added support for the tcn ("triggered change notiﬁcation") 
extension which generates notiﬁcation events on table changes via a trigger function called
triggered_change_notification. The tcn extension is useful for applications using drivers 
which support asynchronous notiﬁcation. This makes it possible to notify all clients if the 
contents of a table have been changed, enabling them to take appropriate action in near-real 
time, such as updating a table cache or information display.
However, such functionality should only be used with care as it makes all data changes on the 
table available to all clients (including unprivileged users) through the notiﬁcation events when 
they listen on the tcn channel. It is the user’s responsibility to avoid using tcn trigger on a table 
with sensitive data to avoid information leakage.
This version includes the following changes:
• The seg extension version 1.3 is added.
• The tcn extension version 1.0 is added.
• The orafce extension is updated to 3.24.
• The pgaudit extension is updated to 1.3.4.
• The pgtap extension is updated to 1.2.0.
• The PostGIS dependency GDAL is updated to 3.4.3.
• The PostGIS dependency PROJ is updated to 7.0.1.
• The wal2json extension is updated to 2.5.
PostgreSQL version 11.19 on Amazon RDS (Deprecated) 121
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The aws_s3 extension is updated to 1.1.
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.17 on Amazon RDS (Deprecated)
PostgreSQL version 11.17 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in PostgreSQL 11.17.
This version includes the following change:
• The PostGIS extension is updated to 3.1.7
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.16 on Amazon RDS (Deprecated)
PostgreSQL version 11.16 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in PostgreSQL 11.16.
This version also includes the following changes:
• The pglogical extension is updated to 2.4.1.
• The aws_commons extension is updated to 1.2.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.15 on Amazon RDS (Deprecated)
PostgreSQL version 11.15 is now available on Amazon RDS. PostgreSQL version 11.15 contains 
several improvements that were announced for PostgreSQL release 11.15.
This version also includes the following changes:
• The pgaudit extension is updated to 1.3.3. For information about using this extension with RDS 
for PostgreSQL, see Logging at the session and object level with the pgaudit extension.
• The lo module is updated to version 1.1.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.17 on Amazon RDS (Deprecated) 122
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 11.14 on Amazon RDS (Deprecated)
PostgreSQL version 11.14 is now available on Amazon RDS. PostgreSQL version 11.14 contains 
several improvements that were announced for PostgreSQL release 11.14.
This version also includes the following change:
• The pg_hint_plan extension is updated to 1.3.7.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.13 on Amazon RDS (Deprecated)
PostgreSQL version 11.13 is now available on Amazon RDS. PostgreSQL version 11.13 contains 
several improvements that were announced for PostgreSQL release 11.13.
This version also includes the following changes:
• The pgrouting extension is updated to version 2.6.3.
• The pglogical extension is updated to version 2.4.0.
• The PostGIS extension is updated to version 3.1.4, along with the following related extensions:
• address_standardizer
• address_standardizer_data_us
• PostGIS_raster
• PostGIS_tiger_geocoder
• PostGIS_topology
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.12 on Amazon RDS (Deprecated)
PostgreSQL version 11.12 is now available on Amazon RDS. PostgreSQL version 11.12 contains 
several improvements that were announced for PostgreSQL release 11.12.
This version also includes the following change:
• The orafce extension is updated to version 3.15.
PostgreSQL version 11.14 on Amazon RDS (Deprecated) 123
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.11 on Amazon RDS (Deprecated)
PostgreSQL version 11.11 is now available on Amazon RDS. PostgreSQL version 11.11 contains 
several improvements that were announced for PostgreSQL release 11.11.
This version also added the following new extension:
• The pg_bigm extension version 1.2.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.10 on Amazon RDS (Deprecated)
PostgreSQL version 11.10 is now available on Amazon RDS. PostgreSQL version 11.10 contains 
several improvements that were announced for PostgreSQL release 11.10.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.9 on Amazon RDS (Deprecated)
PostgreSQL version 11.9 is now available on Amazon RDS. PostgreSQL version 11.9 contains 
several improvements that were announced for PostgreSQL release 11.9.
This version also includes the following changes:
• Added the aws_s3 extension version 1.1
• Added the pg_proctab extension version 0.0.9
• Upgraded the pgaudit extension to version 1.3.1
• Upgraded the pglogical extension to version 2.2.2
• Added the rdkit extension version 3.8
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.8 on Amazon RDS (Deprecated)
PostgreSQL version 11.8 contains several bug ﬁxes for issues in release 11.7. For more information 
on the ﬁxes in PostgreSQL 11.8, see the PostgreSQL 11.8 documentation.
PostgreSQL version 11.11 on Amazon RDS (Deprecated) 124
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
This version also includes the following change:
• Upgraded the pg_hint_plan extension to version 1.3.5.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.7 on Amazon RDS (Deprecated)
PostgreSQL version 11.7 contains several bug ﬁxes for issues in release 11.6. For more information 
on the ﬁxes in PostgreSQL 11.7, see the PostgreSQL 11.7 documentation.
PostgreSQL version 11.6 on Amazon RDS (Deprecated)
PostgreSQL version 11.6 contains several bug ﬁxes for issues in release 11.5. For more information 
on the ﬁxes in PostgreSQL 11.6, see the PostgreSQL documentation.
This version also includes the following changes:
• Upgraded the pgTAP extension to version 1.1.0.
• Added the plprofiler extension.
• Added to shared_preload_libraries support for pg_prewarm to start automatically.
PostgreSQL version 11.5 on Amazon RDS (Deprecated)
PostgreSQL version 11.5 contains several bug ﬁxes for issues in release 11.4. For more information 
on the ﬁxes in PostgreSQL 11.5, see the PostgreSQL documentation.
This version also includes the following changes:
• A new extension pg_transport is added.
• The extension aws_s3 has been updated to support virtual-hosted style requests. For more 
information, see Amazon S3 path deprecation plan – The rest of the story.
• The PostGIS extension is updated to version 2.5.2.
PostgreSQL version 11.7 on Amazon RDS (Deprecated) 125
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 11.4 on Amazon RDS (Deprecated)
This release contains an important security ﬁx and also bug ﬁxes and improvements done by the 
PostgreSQL community. For more information on the security ﬁx, see the PostgreSQL community 
announcement and the security ﬁx CVE-2019-10164.
With this release, the pg_hint_plan extension has been updated to version 1.3.4.
For more information on the ﬁxes in PostgreSQL 11.4, see the PostgreSQL documentation.
PostgreSQL version 11.2 on Amazon RDS (Deprecated)
PostgreSQL version 11.2 contains several bug ﬁxes for issues in release 11.1. For more information 
on the ﬁxes in PostgreSQL 11.2, see the PostgreSQL documentation.
This version also includes the following changes:
• A new pgTAP extension version 1.0.
• Support for Amazon S3 import. For more information, see  Importing Amazon S3 data into an 
RDS for PostgreSQL DB instance in the Amazon RDS User Guide.
• Multiple major version upgrade is available to PostgreSQL 11.2 from certain previous 
PostgreSQL versions. For more information, see  Choosing a major version upgrade for 
PostgreSQL in the Amazon RDS User Guide.
For information on upgrading the engine version for your PostgreSQL DB instance, see  Upgrading 
the PostgreSQL DB engine for Amazon RDS in the Amazon RDS User Guide.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL version 11.1 on Amazon RDS (Deprecated)
PostgreSQL version 11.1 contains several improvements that were announced in PostgreSQL 11.1 
released! This version includes SQL stored procedures that enable embedded transactions within 
a procedure. This version also includes major improvements to partitioning and parallelism and 
many useful performance improvements. For example, by using a non-null constant for a column 
default, you can now use an ALTER TABLE command to add a column without causing a table 
rewrite.
PostgreSQL version 11.4 on Amazon RDS (Deprecated) 126
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 11.1 contains several bug ﬁxes for issues in release 11. For complete details, 
see the PostgreSQL release 11.1 documentation. Some changes in this version include the 
following:
• Partitioning – Partitioning improvements include support for hash partitioning, enabling creation 
of a default partition, and dynamic row movement to another partition based on the key column 
update.
• Performance – Performance improvements include parallelism while creating indexes, 
materialized views, hash joins, and sequential scans to make the operations perform better.
• Stored procedures – SQL stored procedures now added support embedded transactions.
• Support for Just-In-Time (JIT) capability – RDS for PostgreSQL 11 instances are created with JIT 
capability, speeding evaluation of expressions. To enable JIT capability, set the jit parameter to 
1 in the PostgreSQL parameter group for the database.
• Segment size – The write-ahead logging (WAL) segment size has been changed from 16 MB to 64 
MB.
• Autovacuum improvements – To provide valuable logging, the parameter
rds.force_autovacuum_logging is ON by default in conjunction with the
log_autovacuum_min_duration parameter set to 10 seconds. To increase 
autovacuum eﬀectiveness, the values for the autovacuum_max_workers and
autovacuum_vacuum_cost_limit parameters are computed based on host memory capacity 
to provide larger default values.
• Improved transaction timeout – The parameter idle_in_transaction_session_timeout is 
set to 24 hours. Any session that has been idle more than 24 hours is terminated.
• Performance metrics – The pg_stat_statements extension is included in
shared_preload_libraries by default. This avoids having to reboot the instance 
immediately after creation. However, this functionality still requires you to run the statement
CREATE EXTENSION pg_stat_statements;. Also, track_io_timing is enabled by default 
to add more granular data to pg_stat_statements.
• The tsearch2 extension is no longer supported – If your application uses tsearch2 functions, 
update it to use the equivalent functions provided by the core PostgreSQL engine. For more 
information about the tsearch2 extension, see PostgreSQL tsearch2.
• The chkpass extension is no longer supported – For more information about the chkpass
extension, see PostgreSQL chkpass.
• Extension updates for RDS for PostgreSQL 11.1 include the following:
PostgreSQL version 11.1 on Amazon RDS (Deprecated) 127
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• pgaudit is updated to 1.3.0
• pg_hint_plan is updated to 1.3.2
• pglogical is updated to 2.2.1
• plcoffee is updated to 2.3.8
• plv8 is updated to 2.3.8
• PostGIS is updated to 2.5.1
• prefix is updated to 1.2.8
• wal2json is updated to hash 9e962bad
For information on all extensions, see Extensions supported for RDS for PostgreSQL 11.
PostgreSQL 10 versions (Deprecated)
Minor versions
• PostgreSQL version 10.23 on Amazon RDS (Deprecated)
• PostgreSQL version 10.22 on Amazon RDS (Deprecated)
• PostgreSQL version 10.21 on Amazon RDS (Deprecated)
• PostgreSQL version 10.20 on Amazon RDS (Deprecated)
• PostgreSQL version 10.19 on Amazon RDS (Deprecated)
• PostgreSQL version 10.18 on Amazon RDS (Deprecated)
• PostgreSQL version 10.17 on Amazon RDS (Deprecated)
• PostgreSQL version 10.16 on Amazon RDS (Deprecated)
• PostgreSQL version 10.15 on Amazon RDS (Deprecated)
• PostgreSQL version 10.14 on Amazon RDS (Deprecated)
• PostgreSQL version 10.13 on Amazon RDS (Deprecated)
• PostgreSQL version 10.12 on Amazon RDS (Deprecated)
• PostgreSQL version 10.11 on Amazon RDS (Deprecated)
• PostgreSQL version 10.10 on Amazon RDS (Deprecated)
• PostgreSQL version 10.9 on Amazon RDS (Deprecated)
• PostgreSQL version 10.7 on Amazon RDS (Deprecated)
PostgreSQL 10 versions (Deprecated) 128
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• PostgreSQL version 10.6 on Amazon RDS (Deprecated)
• PostgreSQL version 10.5 on Amazon RDS (Deprecated)
• PostgreSQL version 10.4 on Amazon RDS (Deprecated)
• PostgreSQL version 10.3 on Amazon RDS (Deprecated)
• PostgreSQL version 10.1 on Amazon RDS (Deprecated)
PostgreSQL version 10.23 on Amazon RDS (Deprecated)
PostgreSQL version 10.23 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in the PostgreSQL 10.23 release.
New features and enhancements
• PostgreSQL version 10.23 added support for the tcn ("triggered change notiﬁcation") 
extension which generates notiﬁcation events on table changes via a trigger function called
triggered_change_notification. The tcn extension is useful for applications using drivers 
which support asynchronous notiﬁcation. This makes it possible to notify all clients if the 
contents of a table have been changed, enabling them to take appropriate action in near-real 
time, such as updating a table cache or information display.
However, such functionality should only be used with care as it makes all data changes on the 
table available to all clients (including unprivileged users) through the notiﬁcation events when 
they listen on the tcn channel. It is the user’s responsibility to avoid using tcn trigger on a table 
with sensitive data to avoid information leakage.
This version includes the following changes:
• The seg extension version 1.1 is added.
• The tcn extension version 1.0 is added.
• The orafce extension is updated to 3.24.
• The pgaudit extension is updated to 1.2.4.
• PostGIS dependency GDAL is updated to 3.4.3.
• PostGIS dependency PROJ is updated to 7.0.1.
• The wal2json extension is updated to 2.5.
• The aws_s3 extension is updated to 1.1.
PostgreSQL version 10.23 on Amazon RDS (Deprecated) 129
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For version information on all extensions, see Extensions supported for RDS for PostgreSQL 10.
PostgreSQL version 10.22 on Amazon RDS (Deprecated)
PostgreSQL version 10.22 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements for PostgreSQL announced in PostgreSQL 10.22.
This version includes the following change:
• The PostGIS extension is updated to 3.1.7
For information on all extensions, see Extensions supported for RDS for PostgreSQL 10.
PostgreSQL version 10.21 on Amazon RDS (Deprecated)
PostgreSQL version 10.21 is now available on Amazon RDS. This release contains several ﬁxes and 
improvements that were announced in PostgreSQL 10.21.
This version also includes the following changes:
• The pglogical extension is updated to 2.4.1.
• The aws_commons extension is updated to 1.2.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 10.
PostgreSQL version 10.20 on Amazon RDS (Deprecated)
PostgreSQL version 10.20 is now available on Amazon RDS. PostgreSQL version 10.20 contains 
several improvements that were announced for PostgreSQL release 10.20.
This version also includes the following changes:
• The pgaudit extension is updated to 1.2.3. For information about using this extension with RDS 
for PostgreSQL, see Logging at the session and object level with the pgaudit extension in the
Amazon RDS User Guide.
• The lo module is updated to version 1.1.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 10.
PostgreSQL version 10.22 on Amazon RDS (Deprecated) 130
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 10.19 on Amazon RDS (Deprecated)
PostgreSQL version 10.19 is now available on Amazon RDS. PostgreSQL version 10.19 contains 
several improvements that were announced for PostgreSQL release 10.19.
This version also includes the following change:
• The pg_hint_plan extension is updated to 1.3.6.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 10.
PostgreSQL version 10.18 on Amazon RDS (Deprecated)
PostgreSQL version 10.18 is now available on Amazon RDS. PostgreSQL version 10.18 contains 
several improvements that were announced for PostgreSQL release 10.18.
This version also includes the following changes:
• The pgrouting extension is updated to version 2.5.5.
• The pglogical extension is updated to version 2.4.0.
• The PostGIS extension is updated to version 3.1.4, along with the following related extensions:
• address_standardizer
• address_standardizer_data_us
• PostGIS_raster
• PostGIS_tiger_geocoder
• PostGIS_topology
For information on all extensions, see Extensions supported for RDS for PostgreSQL 10.
PostgreSQL version 10.17 on Amazon RDS (Deprecated)
PostgreSQL version 10.17 is now available on Amazon RDS. PostgreSQL version 10.17 contains 
several improvements that were announced for PostgreSQL release 10.17.
This version also includes the following change:
• The orafce extension is updated to version 3.15.
PostgreSQL version 10.19 on Amazon RDS (Deprecated) 131
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For information on all extensions, see Extensions supported for RDS for PostgreSQL 10.
PostgreSQL version 10.16 on Amazon RDS (Deprecated)
PostgreSQL version 10.16 is now available on Amazon RDS. PostgreSQL version 10.16 contains 
several improvements that were announced for PostgreSQL release 10.16.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 10.
PostgreSQL version 10.15 on Amazon RDS (Deprecated)
PostgreSQL version 10.15 is now available on Amazon RDS. PostgreSQL version 10.15 contains 
several improvements that were announced for PostgreSQL release 10.15.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 10.
PostgreSQL version 10.14 on Amazon RDS (Deprecated)
PostgreSQL version 10.14 is now available on Amazon RDS. PostgreSQL version 10.14 contains 
several improvements that were announced for PostgreSQL release 10.14.
This version also includes the following changes:
• Added the aws_s3 extension version 1.1. For more information, see  Exporting data from an RDS 
for PostgreSQL DB instance to Amazon S3 in the Amazon RDS User Guide.
• Upgraded the pgaudit extension to version 1.2.1
• Upgraded the pglogical extension to version 2.2.2
• Upgraded the wal2json extension to version 2.3
For information on all extensions, see Extensions supported for RDS for PostgreSQL 10.
PostgreSQL version 10.13 on Amazon RDS (Deprecated)
PostgreSQL version 10.13 contains several bug ﬁxes for issues in release 10.12. For more 
information on the ﬁxes in PostgreSQL 10.13, see the PostgreSQL 10.13 documentation.
This version also includes the following change:
PostgreSQL version 10.16 on Amazon RDS (Deprecated) 132
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Upgraded the pg_hint_plan extension to version 1.3.5.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 10.
PostgreSQL version 10.12 on Amazon RDS (Deprecated)
PostgreSQL version 10.12 contains several bug ﬁxes for issues in release 10.11. For more 
information on the ﬁxes in PostgreSQL 10.12, see the PostgreSQL 10.12 documentation.
PostgreSQL version 10.11 on Amazon RDS (Deprecated)
PostgreSQL version 10.11 contains several bug ﬁxes for issues in release 10.10. For more 
information on the ﬁxes in PostgreSQL 10.11, see the PostgreSQL documentation. Changes in this 
version include the following:
• Added the plprofiler extension.
PostgreSQL version 10.10 on Amazon RDS (Deprecated)
PostgreSQL version 10.10 contains several bug ﬁxes for issues in release 10.9. For more 
information on the ﬁxes in PostgreSQL 10.10, see the PostgreSQL documentation. Changes in this 
version include the following:
• The aws_s3 extension is updated to support virtual-hosted style requests. For more information, 
see Amazon S3 path deprecation plan – The rest of the story.
• The The PostGIS extension is updated to version 2.5.2.
PostgreSQL version 10.9 on Amazon RDS (Deprecated)
This release contains an important security ﬁx and also bug ﬁxes and improvements done by the 
PostgreSQL community. For more information on the security ﬁx, see the PostgreSQL community 
announcement and security ﬁx CVE-2019-10164.
With this release, the pg_hint_plan extension has been updated to version 1.3.3.
For more information on the ﬁxes in PostgreSQL 10.9, see the PostgreSQL documentation.
PostgreSQL version 10.12 on Amazon RDS (Deprecated) 133
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 10.7 on Amazon RDS (Deprecated)
PostgreSQL version 10.7 contains several bug ﬁxes for issues in release 10.6. For more information 
on the ﬁxes in 10.7, see the PostgreSQL documentation.
This version also includes the following changes:
• Support for Amazon S3 import. For more information, see  Importing Amazon S3 data into an 
RDS for PostgreSQL DB instance in the Amazon RDS User Guide.
• Multiple major version upgrade is available to PostgreSQL 10.7 from certain previous 
PostgreSQL versions. For more information, see  Choosing a major version upgrade for 
PostgreSQL in the Amazon RDS User Guide.
For information on upgrading the engine version for your PostgreSQL DB instance, see  Upgrading 
the PostgreSQL DB engine for Amazon RDS in the Amazon RDS User Guide.
PostgreSQL version 10.6 on Amazon RDS (Deprecated)
PostgreSQL version 10.6 contains several bug ﬁxes for issues in release 10.5. For more information 
on the ﬁxes in PostgreSQL 10.6, see the PostgreSQL documentation.
This version also includes the following changes:
• A new rds.restrict_password_commands parameter and a new rds_password role 
have been introduced. When the rds.restrict_password_commands parameter is 
enabled, only users who have the rds_password role can make user password and password 
expiration changes. By restricting password-related operations to a limited set of roles, you 
can implement policies such as password complexity requirements from the client side. The
rds.restrict_password_commands parameter is static, so it requires a database restart to 
change it. For more information, see  Restricting password management in the Amazon RDS User 
Guide.
• The logical decoding plugin wal2json has been updated to commit 9e962ba.
For information on upgrading the engine version for your PostgreSQL DB instance, see  Upgrading 
the PostgreSQL DB engine for Amazon RDS in the Amazon RDS User Guide.
For the complete list of extensions supported by Amazon RDS for PostgreSQL, see Extension 
versions for Amazon RDS for PostgreSQL.
PostgreSQL version 10.7 on Amazon RDS (Deprecated) 134
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Note
Amazon RDS for PostgreSQL has announced the removal of the tsearch2 extension in the 
next major release. We encourage customers still using pre-8.3 text search to migrate to 
the equivalent built-in features. For more information about migrating, see the PostgreSQL 
documentation.
PostgreSQL version 10.5 on Amazon RDS (Deprecated)
PostgreSQL version 10.5 contains several bug ﬁxes for issues in release 10.4. For more information 
on the ﬁxes in 10.5, see the PostgreSQL documentation.
This version also includes the following changes:
• Support for the pglogical extension version 2.2.0. Prerequisites for using this extension 
are the same as the prerequisites for using logical replication for PostgreSQL as described in
Performing logical replication for Amazon RDS for PostgreSQL in the Amazon RDS User Guide.
• Support for the pg_similarity extension version 1.0.
• Support for the pageinspect extension version 1.6.
• Support for the libprotobuf extension version 1.3.0 for the PostGIS component.
• An update for the pg_hint_plan extension to version 1.3.1.
• An update for the wal2json extension to version 01c5c1e.
For information on upgrading the engine version for your PostgreSQL DB instance, see  Upgrading 
the PostgreSQL DB engine for Amazon RDS in the Amazon RDS User Guide.
For the complete list of extensions supported by Amazon RDS for PostgreSQL, see Extension 
versions for Amazon RDS for PostgreSQL.
PostgreSQL version 10.4 on Amazon RDS (Deprecated)
PostgreSQL version 10.4 contains several bug ﬁxes for issues in release 10.3. For more information 
on the ﬁxes in 10.4, see the PostgreSQL documentation.
This version also includes the following changes:
PostgreSQL version 10.5 on Amazon RDS (Deprecated) 135
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Support for PostgreSQL 10 Logical Replication using the native publication and subscription 
framework. RDS for PostgreSQL databases can function as both publishers and subscribers. You 
can specify replication to other PostgreSQL databases at the database-level or at the table-
level. With logical replication, the publisher and subscriber databases need not be physically 
identical (block-to-block) to each other. This allows for use cases such as data consolidation, data 
distribution, and data replication across diﬀerent database versions for 10.4 and above. For more 
information, see Performing logical replication for Amazon RDS for PostgreSQL in the Amazon 
RDS User Guide.
• The temporary ﬁle size limitation is user-conﬁgurable. You require the rds_superuser role to 
modify the temp_file_limit parameter.
• Update of the GDAL library, which is used by the PostGIS extension. See  Managing spatial data 
with the PostGIS extension in the Amazon RDS User Guide.
• Update of the ip4r extension to version 2.1.1.
• Update of the pg_repack extension to version 1.4.3. See  Working with the pg_repack extension
in the Amazon RDS User Guide.
• Update of the plv8 extension to version 2.1.2.
For information on upgrading the engine version for your PostgreSQL DB instance, see  Upgrading 
the PostgreSQL DB engine for Amazon RDS in the Amazon RDS User Guide.
For the complete list of extensions supported by Amazon RDS for PostgreSQL, see Extension 
versions for Amazon RDS for PostgreSQL.
Note
The tsearch2 extension is to be removed in the next major release. We encourage 
customers still using pre-8.3 text search to migrate to the equivalent built-in features. For 
more information about migrating, see the PostgreSQL documentation.
PostgreSQL version 10.3 on Amazon RDS (Deprecated)
PostgreSQL version 10.3 contains several bug ﬁxes for issues in release 10. For more information 
on the ﬁxes in 10.3, see the PostgreSQL documentation.
Version 2.1.0 of plv8 is now available. If you use plv8 and upgrade PostgreSQL to a new plv8 
version, you immediately take advantage of the new extension but the catalog metadata doesn't 
PostgreSQL version 10.3 on Amazon RDS (Deprecated) 136
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
reﬂect this fact. For the steps to synchronize your catalog metadata with the new version of plv8, 
see  Upgrading PLV8  in the Amazon RDS User Guide.
For information on upgrading the engine version for your PostgreSQL DB instance, see  Upgrading 
the PostgreSQL DB engine for Amazon RDS in the Amazon RDS User Guide.
For the complete list of extensions supported by Amazon RDS for PostgreSQL, see Extension 
versions for Amazon RDS for PostgreSQL.
PostgreSQL version 10.1 on Amazon RDS (Deprecated)
PostgreSQL version 10.1 contains several bug ﬁxes for issues in release 10. For more information 
on the ﬁxes in 10.1, see the PostgreSQL documentation and the PostgreSQL 10 community 
announcement.
For information on upgrading the engine version for your PostgreSQL DB instance, see  Upgrading 
the PostgreSQL DB engine for Amazon RDS in the Amazon RDS User Guide.
PostgreSQL version 10.1 includes the following changes:
• Declarative table partitioning – PostgreSQL 10 adds table partitioning to SQL syntax and native 
tuple routing.
• Parallel queries – When you create a new PostgreSQL 10.1 instance, parallel queries 
are enabled for the default.postgres10 parameter group. The parameter
max_parallel_workers_per_gather is set to 2 by default, but you can modify it to support your 
speciﬁc workload requirements.
• Support for the international components for unicode (ICU) – You can use the ICU library to 
provide explicitly versioned collations. Amazon RDS for PostgreSQL 10.1 is compiled with ICU 
version 60.2. For more information about ICU implementation in PostgreSQL, see Collation 
support.
• Huge pages – Huge pages is a feature of the Linux kernel that uses multiple page size 
capabilities of modern hardware architectures. Amazon RDS for PostgreSQL supports huge 
pages with a global conﬁguration parameter. When you create a new PostgreSQL 10.1 instance 
with RDS, the huge_pages parameter is set to "on" for the default.postgres10 parameter 
group. You can modify this setting to support your speciﬁc workload requirements.
• Extension plv8 update – plv8 is a procedural language that you can use to write functions in 
JavaScript that you can then call from SQL. This release of PostgreSQL supports version 2.1.0 of 
plv8.
PostgreSQL version 10.1 on Amazon RDS (Deprecated) 137
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Renaming of xlog and location – In PostgreSQL version 10 the abbreviation "xlog" has changed 
to "wal", and the term "location" has changed to "lsn". For more information, see  https://
www.postgresql.org/docs/10/static/release-10.html#id-1.11.6.8.4.
• tsearch2 extension – Amazon RDS continues to provide the tsearch2 extension in PostgreSQL 
version 10, but is to remove it in the next major version release. If your application uses 
tsearch2 functions update it to use the equivalent functions the core engine provides. For more 
information see tsearch2 in the PostgreSQL documentation.
For the complete list of extensions supported by Amazon RDS for PostgreSQL, see Extension 
versions for Amazon RDS for PostgreSQL.
PostgreSQL 9.6 versions (Deprecated)
Minor versions
• PostgreSQL version 9.6.24 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.23 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.22 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.21 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.20 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.19 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.18 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.17 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.16 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.15 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.14 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.12 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.11 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.10 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.9 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.8 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.6 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.5 on Amazon RDS (Deprecated)
PostgreSQL 9.6 versions (Deprecated) 138
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• PostgreSQL version 9.6.3 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.2 on Amazon RDS (Deprecated)
• PostgreSQL version 9.6.1 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.24 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.24 is now available on Amazon RDS. PostgreSQL version 9.6.24 contains 
several improvements that were announced for PostgreSQL release 9.6.24.
This version also includes the following change:
• The pg_hint_plan extension is updated to 1.2.7.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 9.6.
PostgreSQL version 9.6.23 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.23 is now available on Amazon RDS. PostgreSQL version 9.6.23 contains 
several improvements that were announced for PostgreSQL release 9.6.23.
This version also includes the following changes:
• The pglogical extension is updated to version 2.4.0.
• The PostGIS extension is updated to version 2.5.5, along with the following related extensions:
• address_standardizer
• address_standardizer_data_us
• PostGIS_tiger_geocoder
• PostGIS_topology
For information on all extensions, see Extensions supported for RDS for PostgreSQL 9.6.
PostgreSQL version 9.6.22 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.22 is now available on Amazon RDS. PostgreSQL version 9.6.22 contains 
several improvements that were announced for PostgreSQL release 9.6.22.
This version also includes the following change:
PostgreSQL version 9.6.24 on Amazon RDS (Deprecated) 139
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• The orafce extension is updated to version 3.15.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 9.6.
PostgreSQL version 9.6.21 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.21 is now available on Amazon RDS. PostgreSQL version 9.6.21 contains 
several improvements that were announced for PostgreSQL release 9.6.21.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 9.6.
PostgreSQL version 9.6.20 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.20 is now available on Amazon RDS. PostgreSQL version 9.6.20 contains 
several improvements that were announced for PostgreSQL release 9.6.20.
For information on all extensions, see Extensions supported for RDS for PostgreSQL 9.6.
PostgreSQL version 9.6.19 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.19 is now available on Amazon RDS. PostgreSQL version 9.6.19 contains 
several improvements that were announced for PostgreSQL release 9.6.19.
This version also includes the following changes:
• Upgraded the pgaudit extension to version 1.1.2
• Upgraded the pglogical extension to version 2.2.2
• Upgraded the wal2json extension to version 2.3
For information on all extensions, see Extensions supported for RDS for PostgreSQL 9.6.
PostgreSQL version 9.6.18 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.18 contains several bug ﬁxes for issues in release 9.6.17. For more 
information on the ﬁxes in PostgreSQL 9.6.18, see the PostgreSQL 9.6.18 documentation.
This version also includes the following change:
• Upgraded the pg_hint_plan extension to version 1.2.6.
PostgreSQL version 9.6.21 on Amazon RDS (Deprecated) 140
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For information on all extensions, see Extensions supported for RDS for PostgreSQL 9.6.
PostgreSQL version 9.6.17 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.17 contains several bug ﬁxes for issues in release 9.6.16. For more 
information on the ﬁxes in PostgreSQL 9.6.17, see the PostgreSQL 9.6.17 documentation.
PostgreSQL version 9.6.16 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.16 contains several bug ﬁxes for issues in release 9.6.15. For more 
information on the ﬁxes in PostgreSQL 9.6.16, see the PostgreSQL documentation.
PostgreSQL version 9.6.15 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.15 contains several bug ﬁxes for issues in release 9.6.14. For more 
information on the ﬁxes in PostgreSQL 9.6.15, see the PostgreSQL documentation.
The PostGIS extension is updated to version 2.5.2.
PostgreSQL version 9.6.14 on Amazon RDS (Deprecated)
This release contains bug ﬁxes and improvements done by the PostgreSQL community.
With this release, the pg_hint_plan extension has been updated to version 1.2.5.
For more information on the ﬁxes in PostgreSQL 9.6.14, see the PostgreSQL documentation.
PostgreSQL version 9.6.12 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.12 contains several bug ﬁxes for issues in release 9.6.11. For more 
information on the ﬁxes in 9.6.12, see the PostgreSQL documentation.
For information on upgrading the engine version for your PostgreSQL DB instance, see  Upgrading 
the PostgreSQL DB engine for Amazon RDS in the Amazon RDS User Guide.
PostgreSQL version 9.6.11 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.11 contains several bug ﬁxes for issues in release 9.6.10. For more 
information on the ﬁxes in PostgreSQL 9.6.11, see the PostgreSQL documentation. For information 
PostgreSQL version 9.6.17 on Amazon RDS (Deprecated) 141
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
on upgrading the engine version for your PostgreSQL DB instance, see  Upgrading the PostgreSQL 
DB engine for Amazon RDS in the Amazon RDS User Guide.
With this version, the logical decoding plugin wal2json has been updated to commit 9e962ba.
For the complete list of extensions supported by Amazon RDS for PostgreSQL, see Extension 
versions for Amazon RDS for PostgreSQL.
PostgreSQL version 9.6.10 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.10 contains several bug ﬁxes for issues in release 9.6.9. For more 
information on the ﬁxes in 9.6.10, see the PostgreSQL documentation.
This version includes the following changes:
• Support for the pglogical extension version 2.2.0. Prerequisites for using this extension 
are the same as the prerequisites for using logical replication for PostgreSQL as described in
Performing logical replication for Amazon RDS for PostgreSQL in the Amazon RDS User Guide.
• Support for the pg_similarity extension version 2.2.0.
• An update for the wal2json extension to version 01c5c1e.
• An update for the pg_hint_plan extension to version 1.2.3.
For information on upgrading the engine version for your PostgreSQL DB instance, see  Upgrading 
the PostgreSQL DB engine for Amazon RDS in the Amazon RDS User Guide.
For the complete list of extensions supported by Amazon RDS for PostgreSQL, see Extension 
versions for Amazon RDS for PostgreSQL.
PostgreSQL version 9.6.9 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.9 contains several bug ﬁxes for issues in release 9.6.8. For more 
information on the ﬁxes in 9.6.9, see the PostgreSQL documentation. For information on 
upgrading the engine version for your PostgreSQL DB instance, see  Upgrading the PostgreSQL DB 
engine for Amazon RDS in the Amazon RDS User Guide.
This version includes the following changes:
• The temporary ﬁle size limitation is user-conﬁgurable. You require the rds_superuser role to 
modify the temp_file_limit parameter.
PostgreSQL version 9.6.10 on Amazon RDS (Deprecated) 142
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Update of the GDAL library, which is used by the PostGIS extension. See  Working with the 
PostGIS extension in the Amazon RDS User Guide.
• Update of the ip4r extension to version 2.1.1.
• Update of the pgaudit extension to version 1.1.1. See Logging at the session and object level 
with the pgaudit extension in the Amazon RDS User Guide.
Update of the pg_repack extension to version 1.4.3. See  Working with the pg_repack extension
in the Amazon RDS User Guide.
• Update of the plv8 extension to version 2.1.2.
For the complete list of extensions supported by Amazon RDS for PostgreSQL, see Extension 
versions for Amazon RDS for PostgreSQL.
PostgreSQL version 9.6.8 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.8 contains several bug ﬁxes for issues in release 9.6.6. For more 
information on the ﬁxes in 9.6.8, see the PostgreSQL documentation. For information on 
upgrading the engine version for your PostgreSQL DB instance, see  Upgrading the PostgreSQL DB 
engine for Amazon RDS in the Amazon RDS User Guide.
For the complete list of extensions supported by Amazon RDS for PostgreSQL, see Extension 
versions for Amazon RDS for PostgreSQL.
PostgreSQL version 9.6.6 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.6 contains several bug ﬁxes for issues in release 9.6.5. For more 
information on the ﬁxes in 9.6.6, see the PostgreSQL documentation. For information on 
upgrading the engine version for your PostgreSQL DB instance, see  Upgrading the PostgreSQL DB 
engine for Amazon RDS in the Amazon RDS User Guide.
This version includes the following features:
• Supports the orafce extension, version 3.6.1. This extension contains functions that are native 
to commercial databases, and can be helpful if you are porting a commercial database to 
PostgreSQL. For more information about using orafce with Amazon RDS, see Using functions 
from the orafce extensionin the Amazon RDS User Guide.
• Supports the prefix extension, version 1.2.6. This extension provides an operator for text preﬁx 
searches. For more information about prefix, see the preﬁx project on GitHub.
PostgreSQL version 9.6.8 on Amazon RDS (Deprecated) 143
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Supports version 2.3.4 of PostGIS, version 2.4.2 of pgrouting, and an updated version of 
wal2json.
For the complete list of extensions supported by Amazon RDS for PostgreSQL, see Extension 
versions for Amazon RDS for PostgreSQL.
PostgreSQL version 9.6.5 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.5 contains several bug ﬁxes for issues in release 9.6.4. For more 
information on the ﬁxes in 9.6.5, see the PostgreSQL documentation. For information on 
upgrading the engine version for your PostgreSQL DB instance, see  Upgrading the PostgreSQL DB 
engine for Amazon RDS in the Amazon RDS User Guide.
This version also includes support for the pgrouting, postgresql-hll extensions, and the
decoder_raw optional extension.
For the complete list of extensions supported by Amazon RDS for PostgreSQL, see Extension 
versions for Amazon RDS for PostgreSQL.
PostgreSQL version 9.6.3 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.3 contains several new features and bug ﬁxes. This version includes the 
following features:
• Supports the extension pg_repack version 1.4.0. You can use this extension to remove bloat 
from tables and indexes. For more information on using pg_repack with Amazon RDS, see
Reducing bloat in tables and indexes with the pg_repack extension in the Amazon RDS User 
Guide.
• Supports the extension pgaudit version 1.1.0. This extension provides detailed session and 
object audit logging. For more information on using pgaudit with Amazon RDS, see  Logging at 
the session and object level with the pgaudit extension in the Amazon RDS User Guide.
• Supports wal2json, an output plugin for logical decoding.
• Supports the auto_explain extension. You can use this extension to log execution plans of 
slow statements automatically. The following example shows how to use auto_explain from 
within an Amazon RDS PostgreSQL session:
LOAD '$libdir/plugins/auto_explain';
PostgreSQL version 9.6.5 on Amazon RDS (Deprecated) 144
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
For more information on using auto_explain, see the  PostgreSQL documentation.
PostgreSQL version 9.6.2 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.2 contains several new features and bug ﬁxes. The new version also 
includes the following extension versions:
• PostGIS version 2.3.2
• pg_freespacemap version 1.1–Provides a way to examine the free space map (FSM). This 
extension provides an overloaded function called pg_freespace. The functions show the value 
recorded in the free space map for a given page, or for all pages in the relation.
• pg_hint_plan version 1.1.3– Provides control of execution plans by using hinting phrases at the 
beginning of SQL statements.
• log_fdw version 1.0–Using this extension from Amazon RDS, you can load and query your 
database engine log from within the database. For more information, see Using the log_fdw 
extension to access the DB log using SQL in the Amazon RDS User Guide.
• With this version release, you can now edit the max_worker_processes parameter in a DB 
parameter group.
PostgreSQL version 9.6.2 on Amazon RDS also supports altering enum values. For more 
information, see Custom data types and enumerations with RDS for PostgreSQL in the Amazon 
RDS User Guide.
For more information on the ﬁxes in 9.6.2, see the PostgreSQL documentation. For information on 
upgrading the engine version for your PostgreSQL DB instance, see  Upgrading the PostgreSQL DB 
engine for Amazon RDS in the Amazon RDS User Guide.
PostgreSQL version 9.6.1 on Amazon RDS (Deprecated)
PostgreSQL version 9.6.1 contains several new features and improvements. For more information 
about the ﬁxes and improvements in PostgreSQL 9.6.1, see the PostgreSQL documentation. For 
information on upgrading the engine version for your PostgreSQL DB instance, see  Upgrading 
the PostgreSQL DB engine for Amazon RDS in the Amazon RDS User Guide. For information about 
performing parallel queries and phrase searching using Amazon RDS for PostgreSQL 9.6.1, see the
AWS Database Blog.
PostgreSQL version 9.6.2 on Amazon RDS (Deprecated) 145
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
PostgreSQL version 9.6.1 includes the following changes:
• Parallel query processing: Supports parallel processing of large read-only queries, allowing 
sequential scans, hash joins, nested loops, and aggregates to be run in parallel. By default, 
parallel query processing isn't enabled. To enable parallel query processing, set the parameter
max_parallel_workers_per_gather to a value larger than zero.
• Updated postgres_fdw extension: Supports remote JOINs, SORTs, UPDATEs, and DELETE 
operations.
• plv8 update: Provides version 1.5.3 of the plv8 language.
• PostGIS version update: Supports POSTGIS="2.3.0 r15146" GEOS="3.5.0-CAPI-1.9.0 r4084" 
PROJ="Rel. 4.9.2, 08 September 2015" GDAL="GDAL 2.1.1, released 2016/07/07" LIBXML="2.9.1" 
LIBJSON="0.12" RASTER
• Vacuum improvement: Avoids scanning pages unnecessarily during vacuum freeze operations.
• Full-text search support for phrases: Supports the ability to specify a phrase-search query in 
tsquery input using the new operators <-> and <N>.
• Two new extensions are supported:
• bloom, an index access method based on Bloom ﬁlters
• pg_visibility, which provides a means for examining the visibility map and page-level 
visibility information of a table.
• With the release of version 9.6.2, you can now edit the max_worker_processes parameter in a 
PostgreSQL version 9.6.1 DB parameter group.
Deprecation of PostgreSQL 10
On April 17, 2023, Amazon RDS deprecated PostgreSQL 10. For more information, see Deprecation 
of PostgreSQL version 10 in the Amazon RDS User Guide. We strongly recommend that you take 
action as soon as possible and upgrade your PostgreSQL databases running on major version 10 to 
a later major version, such as version 14. For information about how to do so, see Upgrading the 
PostgreSQL DB engine for Amazon RDS in the Amazon RDS User Guide.
Deprecation of PostgreSQL 10 146
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Deprecation of PostgreSQL 9.6
On March 31, 2022, Amazon RDS deprecated PostgreSQL 9.6. This extended the previously 
announced date of January 18, 2022 to April 26, 2022. For more information, see Deprecation 
of PostgreSQL version 9.6 in the Amazon RDS User Guide. We strongly recommend that you 
upgrade all your PostgreSQL 9.6 DB instances to PostgreSQL 12 or higher as soon as possible. For 
information about how to do so, see Upgrading the PostgreSQL DB engine for Amazon RDS in the
Amazon RDS User Guide.
Deprecation of PostgreSQL 9.6 147
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Amazon RDS Extended Support updates
Learn about the Amazon RDS Extended Support updates below.
Topics
• Amazon RDS Extended Support for PostgreSQL 12
• Amazon RDS Extended Support for PostgreSQL 11
Amazon RDS Extended Support for PostgreSQL 12
Minor versions
• Amazon RDS Extended Support version 12.22-RDS.20251114
• Amazon RDS Extended Support version 12.22-RDS.20250814
• Amazon RDS Extended Support version 12.22-RDS.20250508
• Amazon RDS Extended Support version 12.22-RDS.20250220
Amazon RDS Extended Support version 12.22-RDS.20251114
RDS Extended Support version 12.22-RDS.20251114 is now available.
CVEs ﬁxed:
• CVE-2025-12817
• CVE-2025-12818
Amazon RDS Extended Support version 12.22-RDS.20250814
RDS Extended Support version 12.22-RDS.20250814 is now available.
CVEs ﬁxed:
• CVE-2025-8715
• CVE-2025-8714
• CVE-2025-8713
• CVE-2023-3079
Amazon RDS Extended Support for PostgreSQL 12 148
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extensions updated:
• The pgactive extension was updated to 2.1.6.
Amazon RDS Extended Support version 12.22-RDS.20250508
RDS Extended Support version 12.22-RDS.20250508 is now available.
CVEs ﬁxed:
• CVE-2025-4207
Amazon RDS Extended Support version 12.22-RDS.20250220
RDS Extended Supportt version 12.22-RDS.20250220 is now available.
CVEs ﬁxed:
• CVE-2025–1094
Amazon RDS Extended Support for PostgreSQL 11
Minor versions
• Amazon RDS Extended Support version 11.22-RDS.20251114
• Amazon RDS Extended Support version 11.22-RDS.20250814
• Amazon RDS Extended Support version 11.22-RDS.20250508
• Amazon RDS Extended Support version 11.22-RDS.20250220
• Amazon RDS Extended Support version 11.22-RDS.20241121
• Amazon RDS Extended Support version 11.22-RDS.20240808
• Amazon RDS Extended Support version 11.22-RDS.20240509
• Amazon RDS Extended Support version 11.22-RDS.20240418
Amazon RDS Extended Support version 11.22-RDS.20251114
RDS Extended Support version 11.22-RDS.20251114 is now available.
Amazon RDS Extended Support version 12.22-RDS.20250508 149
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
CVEs ﬁxed:
• CVE-2025-12817
• CVE-2025-12818
Amazon RDS Extended Support version 11.22-RDS.20250814
RDS Extended Support version 11.22-RDS.20250814 is now available.
CVEs ﬁxed:
• CVE-2025-8715
• CVE-2025-8714
• CVE-2025-8713
• CVE-2023-3079
Extensions updated:
• The plv8 extension was updated to version 3.1.10.
• The pgactive extension was updated to 2.1.6.
Amazon RDS Extended Support version 11.22-RDS.20250508
RDS Extended Support version 11.22-RDS.20250508 is now available.
CVEs ﬁxed:
• CVE-2025-4207
Amazon RDS Extended Support version 11.22-RDS.20250220
RDS Extended Support version 11.22-RDS.20250220 is now available.
CVEs ﬁxed:
• CVE-2025–1094
Amazon RDS Extended Support version 11.22-RDS.20250814 150
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Amazon RDS Extended Support version 11.22-RDS.20241121
RDS Extended Support version 11.22-RDS.20241121 is now available.
CVEs ﬁxed:
• CVE-2024-10979
• CVE-2024-10978
• CVE-2024-10977
• CVE-2024-10976
Amazon RDS Extended Support version 11.22-RDS.20240808
RDS Extended Support version 11.22-RDS.20240808 is now available.
CVEs ﬁxed:
• CVE-2024-7348
Amazon RDS Extended Support version 11.22-RDS.20240509
RDS Extended Support version 11.22-RDS.20240509 is now available.
Extensions updated:
• The plcoffee extension was updated to version 3.1.6.
• The plls extension was updated to version 3.1.6.
• The plv8 extension was updated to version 3.1.6.
Amazon RDS Extended Support version 11.22-RDS.20240418
RDS Extended Support version 11.22-RDS.20240418 is now available.
Bugs ﬁxed:
• Fixed a bug preventing the termination of autovacuum
Amazon RDS Extended Support version 11.22-RDS.20241121 151
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
CVEs ﬁxed:
• CVE-2024-0985
Amazon RDS Extended Support version 11.22-RDS.20240418 152
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension versions for Amazon RDS for PostgreSQL
Amazon RDS for PostgreSQL support multiple extensions that enhance your database 
functionality. Each major engine version has a minimum supported extension version. When 
we release the ﬁrst minor version of a new major engine, we publish the minimum supported 
extension version for that major engine version. We recommend that you upgrade to the 
latest version of each extension when you upgrade your DB cluster. Extension versions don't 
automatically upgrade during engine version upgrade workﬂows.
AWS plans to oﬀer the latest version of extensions in the next quarterly release after they become 
available. Each extension's versioning scheme, features, and compatibility are determined by the 
extension developers, not AWS.
AWS might need to end support for extensions. When feasible, we provide 12 months notice 
before ending support for an extension. However, in cases involving security or other critical issues, 
we might need to end support for an extension or a speciﬁc version of an extension with less 
than 12 months notice or no notice across all supported engine versions. We might require you to 
upgrade to a newer version of an extension at any time and will provide instructions in such cases.
The PostgreSQL community sometimes refers to the extensions as modules. Extensions expand on 
the functionality provided by the PostgreSQL engine. You can ﬁnd a list of extensions supported by 
Amazon RDS in the default DB parameter group for that PostgreSQL version. You can also see the 
current extensions list using psql by showing the rds.extensions parameter as in the following 
example.
SHOW rds.extensions; 
Note
Extensions added in a minor version release might display inaccurately when using the
rds.extensions parameter in psql.
The following sections show the extensions supported by Amazon RDS for the major PostgreSQL 
versions.
Contents
• Extensions supported for RDS for PostgreSQL 18
153
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
• Extensions supported for RDS for PostgreSQL 17
• Extensions supported for RDS for PostgreSQL 16
• Extensions supported for RDS for PostgreSQL 15
• Extensions supported for RDS for PostgreSQL 14
• Extensions supported for RDS for PostgreSQL 13
• Extensions supported for RDS for PostgreSQL 12
• Extensions supported for RDS for PostgreSQL 11
• Extensions supported for RDS for PostgreSQL 10
• Extensions supported for RDS for PostgreSQL 9.6
Extensions supported for RDS for PostgreSQL 18
The following table shows PostgreSQL extensions for PostgreSQL version 18 that are currently 
supported on Amazon RDS. For more information on PostgreSQL extensions, see Packaging related 
objects into an extension.
Note
The preview documentation is subject to change for Amazon RDS for PostgreSQL versions 
18 Beta 1, 18 Beta 2, 18 Beta 3, and 18 RC1.
Extension 18.3 18.2 18.1 18.0 
Preview
18 RC1 18 Beta 
3
18 Beta 
2
18 Beta 
1
address_s 
tandardiz 
er
3.6.0 3.6.0 3.6.0 3.6.0 N/A N/A N/A N/A
address_s 
tandardiz 
er_data_u 
s
3.6.0 3.6.0 3.6.0 3.6.0 N/A N/A N/A N/A
amcheck 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
Extensions for PostgreSQL 18 154
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 18.3 18.2 18.1 18.0 
Preview
18 RC1 18 Beta 
3
18 Beta 
2
18 Beta 
1
auto_expl 
ain
yes yes yes yes yes yes yes yes
autoinc 
(contrib- 
spi)
1 1 1 1 1 1 1 1
aws_commo 
ns
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
aws_lambd 
a
1 1 1 1 1 1 1 1
aws_s3 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
bloom 1 1 1 1 1 1 1 1
bool_plpe 
rl
1 1 1 1 1 1 1 1
btree_gin 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
btree_gis 
t
1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8
citext 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8
collectio 
n
1.1.0 1.1.0 1.1.0 N/A N/A N/A N/A N/A
cube 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
dblink 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
decoder_r 
aw
yes yes yes yes yes yes yes yes
Extensions for PostgreSQL 18 155
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 18.3 18.2 18.1 18.0 
Preview
18 RC1 18 Beta 
3
18 Beta 
2
18 Beta 
1
dict_int 1 1 1 1 1 1 1 1
dict_xsyn 1 1 1 1 1 1 1 1
earthdist 
ance
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
ﬂow_cont 
rol
1 1 1 1 1 1 1 1
fuzzystrm 
atch
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
h3-pg 4.2.3 4.2.3 4.2.3 4.2.3 N/A N/A N/A N/A
hll 2.18 2.18 2.18 2.18 2.18 2.18 2.18 2.18
hstore 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8
hstore_pl 
perl
1 1 1 1 1 1 1 1
hypopg 1.4.2 1.4.2 1.4.2 1.4.2 1.4.2 1.4.1 1.4.1 1.4.1
ICU 
module
60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2
insert_us 
ername 
(contrib- 
spi)
1 1 1 1 1 1 1 1
intagg 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
intarray 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
ip4r 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2
Extensions for PostgreSQL 18 156
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 18.3 18.2 18.1 18.0 
Preview
18 RC1 18 Beta 
3
18 Beta 
2
18 Beta 
1
isn 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
jsonb_plp 
erl
1 1 1 1 1 1 1 1
lo 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
log_fdw 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
ltree 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
moddateti 
me 
(contrib- 
spi)
1 1 1 1 1 1 1 1
mysql_fdw2.9.3 2.9.3 2.9.3 2.9.2 2.9.2 2.9.2 2.9.2 2.9.2
oracle_fd 
w
2.8.0 2.8.0 2.8.0 2.8.0 2.8.0 2.8.0 2.8.0 N/A
orafce 4.16.3 4.16.3 4.14.0 4.14.0 4.14.0 4.14.0 4.14.0 4.14.0
pageinspe 
ct
1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13
pg_bigm 1.2_20250 
903
1.2_20250 
903
1.2_20250 
903
1.2_20250 
903
1.2_20240 
606
1.2_20240 
606
1.2_20240 
606
N/A
pg_buﬀer 
cache
1.6 1.6 1.6 1.5 1.5 1.5 1.5 1.5
pg_cron 1.6.7 1.6.7 1.6.7 1.6.5 1.6.5 1.6.5 1.6.5 1.6.5
pg_freesp 
acemap
1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
Extensions for PostgreSQL 18 157
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 18.3 18.2 18.1 18.0 
Preview
18 RC1 18 Beta 
3
18 Beta 
2
18 Beta 
1
pg_hint_p 
lan
1.8.0 1.8.0 1.8.0 1.8.0 1.8.0 N/A N/A N/A
pg_logica 
linspect
1 1 1 1 1 1 1 1
pg_partma 
n
5.2.4 5.2.4 5.2.4 5.2.4 5.2.4 5.2.4 5.2.4 N/A
pg_prewar 
m
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_procta 
b
0.0.12 0.0.12 0.0.12 0.0.12 0.0.12 0.0.12 0.0.12 N/A
pg_repack 1.5.3 1.5.3 1.5.2 1.5.2 1.5.2 1.5.1 1.5.1 N/A
pg_simila 
rity
1 1 1 1 1 1 1 1
pg_stat_s 
tatements
1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12
pg_stat_m 
onitor
2.3.1 2.3.1 N/A N/A N/A N/A N/A N/A
pg_tle 1.5.2 1.5.2 1.5.2 1.5.1 1.5.1 1.5.1 1.5.1 N/A
pg_transp 
ort
1 1 1 1.0 1.0 N/A N/A N/A
pg_trgm 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6
pg_visibi 
lity
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
Extensions for PostgreSQL 18 158
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 18.3 18.2 18.1 18.0 
Preview
18 RC1 18 Beta 
3
18 Beta 
2
18 Beta 
1
pg_walins 
pect
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
pgactive 2.1.7 2.1.7 2.1.6 2.1.6 2.1.6 2.1.5 N/A N/A
pgAudit 18 18 18 N/A N/A N/A N/A N/A
pgcrypto 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
pglogical 2.4.6 2.4.6 2.4.6 2.4.6 N/A N/A N/A N/A
pgrouting 3.8.0 3.8.0 3.8.0 3.8.0 N/A N/A N/A N/A
pgrowlock 
s
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pgstattup 
le
1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
pgTAP 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 N/A
pgvector 0.8.1 0.8.1 0.8.1 0.8.0 0.8.0 0.8.0 0.8.0 0.8.0
plperl 1 1 1 1 1 1 1 1
plpgsql 1 1 1 1 1 1 1 1
plproﬁle 
r
4.2.5 4.2.5 4.2.5 4.2.5 4.2.5 4.2.5 4.2.5 4.2.5
plrust N/A N/A N/A N/A N/A N/A N/A N/A
pltcl 1 1 1 1 1 1 1 1
plv8 3.2.4 3.2.4 3.2.4 3.2.4 3.2.4 3.2.4 N/A N/A
PostGIS 3.6.1 3.6.1 3.6.0 3.6.0 N/A N/A N/A N/A
Extensions for PostgreSQL 18 159
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 18.3 18.2 18.1 18.0 
Preview
18 RC1 18 Beta 
3
18 Beta 
2
18 Beta 
1
postgis_r 
aster
3.6.0 3.6.0 3.6.0 3.6.0 N/A N/A N/A N/A
postgis_t 
iger_geoc 
oder
3.6.0 3.6.0 3.6.0 3.6.0 N/A N/A N/A N/A
postgis_t 
opology
N/A N/A N/A 3.6.0 N/A N/A N/A N/A
postgres_ 
fdw
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
preﬁx 1.2.10 1.2.10 1.2.10 1.2.10 1.2.10 1.2.10 1.2.10 1.2.10
rdkit 2024_09_6 
(4.6.1)
2024_09_6 
(4.6.1)
2024_09_6 
(4.6.1)
2024_09_6 
(4.6.1)
2024_09_6 
(4.6.1)
2024_09_6 
(4.6.1)
2024_09_6 
(4.6.1)
N/A
rds_tools 1.9 1.9 1.9 1.9 1.9 1.9 1.9 1.9
reﬁnt 
(contrib- 
spi)
1 1 1 1 1 1 1 1
roaringbi 
tmap
1.1.0 1.1.0 0.5 N/A N/A N/A N/A N/A
seg 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
sslinfo 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
tablefunc 1 1 1 1 1 1 1 1
tcn 1 1 1 1 1 1 1 1
tds_fdw 2.0.5 2.0.5 2.0.5 2.0.4 2.0.4 N/A N/A N/A
Extensions for PostgreSQL 18 160
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 18.3 18.2 18.1 18.0 
Preview
18 RC1 18 Beta 
3
18 Beta 
2
18 Beta 
1
tsm_syste 
m_rows
1 1 1 1 1 1 1 1
tsm_syste 
m_time
1 1 1 1 1 1 1 1
unaccent 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
uuid-
ossp
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
wal2json 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6
Extensions supported for RDS for PostgreSQL 17
The following table shows PostgreSQL extensions for PostgreSQL version 17 that are currently 
supported on Amazon RDS. For more information on PostgreSQL extensions, see Packaging related 
objects into an extension.
Note
The preview documentation is subject to change for Amazon RDS for PostgreSQL versions 
17 Beta 2 and 17 Beta 1.
Extension17.9 17.8 17.7 17.6R217.6 17.5R217.5 17.4R217.4 17.3 17.2 17.1 17.0 
Preview
17 
RC1
17 
Beta 
3
17 
Beta 
2
17 
Beta 
1
address_s 
tandardiz 
er
3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0alph 
a2
3.5.0alph 
a2
3.5.0dev3.5.0dev3.5.0dev3.5.0dev
address_s 
tandardiz 
3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0alph 
a2
3.5.0alph 
a2
3.5.0dev3.5.0dev3.5.0dev3.5.0dev
Extensions for PostgreSQL 17 161
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension17.9 17.8 17.7 17.6R217.6 17.5R217.5 17.4R217.4 17.3 17.2 17.1 17.0 
Preview
17 
RC1
17 
Beta 
3
17 
Beta 
2
17 
Beta 
1
er_data_u 
s
amcheck1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
auto_expl 
ain
yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes
autoinc 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
aws_commo 
ns
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
aws_lambd 
a
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
aws_s31.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
bloom1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
bool_plpe 
rl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
btree_gin1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
btree_gis 
t
1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7
citext1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6
cube 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
dblink1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
Extensions for PostgreSQL 17 162
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension17.9 17.8 17.7 17.6R217.6 17.5R217.5 17.4R217.4 17.3 17.2 17.1 17.0 
Preview
17 
RC1
17 
Beta 
3
17 
Beta 
2
17 
Beta 
1
decoder_r 
aw
yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes
dict_int1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
dict_xsyn1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
earthdist 
ance
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
ﬂow_cont 
rol
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
fuzzystrm 
atch
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
h3-
pg
4.2.3 4.2.3 4.2.3 4.1.3 4.1.3 4.1.3 4.1.3 4.1.3 4.1.3 4.1.3 4.1.3 4.1.3 4.1.3 4.1.3 4.1.3 N/
A
N/
A
hll 2.18 2.18 2.18 2.18 2.18 2.18 2.18 2.18 2.18 2.18 2.18 2.18 2.18 2.18 2.18 2.18 2.18
hstore1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8
hstore_pl 
perl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
hypopg1.4.2 1.4.2 1.4.1 1.4.1 1.4.1 1.4.1 1.4.1 1.4.1 1.4.1 1.4.1 1.4.1 1.4.1 1.4.1 1.4.1 1.4.1 1.4.1 1.4.1
ICU 
module
60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2
insert_us 
ername 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
Extensions for PostgreSQL 17 163
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension17.9 17.8 17.7 17.6R217.6 17.5R217.5 17.4R217.4 17.3 17.2 17.1 17.0 
Preview
17 
RC1
17 
Beta 
3
17 
Beta 
2
17 
Beta 
1
intagg1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
intarray1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
ip4r 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2 2.4.2
isn 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
jsonb_plp 
erl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
lo 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
log_fdw1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
ltree 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
moddateti 
me 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
mysql_fdw2.9.3 2.9.3 2.9.1 2.9.1 2.9.1 2.9.1 2.9.1 2.9.1 2.9.1 2.9.1 2.9.1 2.9.1 2.9.1 2.9.1 N/
A
N/
A
N/
A
old_snaps 
hot
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
oracle_fd 
w
2.8.0 2.8.0 2.8.0 2.7.0 2.8.0 2.7.0 2.7.0 2.7.0 2.7.0 2.7.0 2.7.0 2.6.0 2.6.0 2.6.0 2.6.0 2.6.0 2.6.0
orafce4.16.34.16.34.14.04.14.04.14.04.14.04.14.04.14.04.13.44.13.44.12.04.10.34.10.34.9.4 4.9.4 4.9.4 4.9.4
pageinspe 
ct
1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12
Extensions for PostgreSQL 17 164
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension17.9 17.8 17.7 17.6R217.6 17.5R217.5 17.4R217.4 17.3 17.2 17.1 17.0 
Preview
17 
RC1
17 
Beta 
3
17 
Beta 
2
17 
Beta 
1
pg_bigm1.2_20250 
903
1.2_20250 
903
1.2_20240 
606
1.2_20240 
606
1.2_20240 
606
1.2_20240 
606
1.2_20240 
606
1.2_20240 
606
1.2_20240 
606
1.2_20240 
606
1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_buﬀer 
cache
1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.4 1.4 1.4 1.4 1.4 1.4
pg_cron1.6.7 1.6.7 1.6.5 1.6.5 1.6.5 1.6.5 1.6.5 1.6.5 1.6.4 1.6.4 1.6.4 1.6.3 1.6.3 1.6.2 N/
A
N/
A
N/
A
pg_freesp 
acemap
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_hint_p 
lan
1.7.1 1.7.1 1.7.0 1.7.0 1.7.0 1.7.0 1.7.0 1.7.0 1.7.0 1.7.0 1.7.0 1.7.0 1.7.0 N/
A
N/
A
N/
A
N/
A
pg_partma 
n
5.2.4 5.2.4 5.2.4 5.2.4 5.2.4 5.2.4 5.2.4 5.2.4 5.1.0 5.1.0 5.1.0 5.1.0 5.1.0 5.1.0 5.1.0 5.1.0 5.1.0
pg_prewar 
m
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_procta 
b
0.0.120.0.120.0.120.0.120.0.120.0.120.0.120.0.120.0.120.0.120.0.100.0.100.0.100.0.100.0.100.0.100.0.10
pg_repack1.5.3 1.5.3 1.5.2 1.5.1 1.5.2 1.5.1 1.5.1 1.5.1 1.5.1 1.5.1 1.5.0 1.5.0 1.5.0 1.5.0 N/
A
N/
A
N/
A
pg_simila 
rity
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_stat_s 
tatements
1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.10 1.10 1.10 1.10 1.10 1.10
pg_tle1.5.2 1.5.2 1.5.2 1.4.0 1.4.0 1.4.0 1.4.0 1.4.0 1.4.0 1.4.0 1.4.0 1.4.0 1.4.0 1.4.0 1.4.0 1.4.0 1.4.0
Extensions for PostgreSQL 17 165
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension17.9 17.8 17.7 17.6R217.6 17.5R217.5 17.4R217.4 17.3 17.2 17.1 17.0 
Preview
17 
RC1
17 
Beta 
3
17 
Beta 
2
17 
Beta 
1
pg_transp 
ort
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_trgm1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6
pg_visibi 
lity
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_walins 
pect
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
pgactive2.1.7 2.1.7 2.1.6 2.1.4 2.1.6 2.1.4 2.1.6 2.1.4 2.1.4 2.1.3 2.1.3 2.1.3 2.1.3 2.1.3 2.1.3 N/
A
N/
A
pgAudit17.1 17.1 17.1 17.1 17.1 17.1 17.0 17.0 17.0 17.0 17.0 17beta117beta117beta1N/
A
N/
A
N/
A
pgcrypto1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
pglogical2.4.6 2.4.6 2.4.5 2.4.5 2.4.5 2.4.5 2.4.5 2.4.5 2.4.5 2.4.5 2.4.5 2.4.5 N/
A
N/
A
N/
A
N/
A
N/
A
pgrouting3.6.3 3.6.3 3.6.3 3.6.3 3.6.3 3.6.3 3.6.3 3.6.3 3.6.3 3.6.3 3.6.2 3.6.2 3.6.2 3.6.2 3.6.2 3.6.2 3.6.2
pgrowlock 
s
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pgstattup 
le
1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
pgTAP1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.3 1.3.2 1.3.2 1.3.2
pgvector0.8.1 0.8.1 0.8.0 0.8.0 0.8.0 0.8.0 0.8.0 0.8.0 0.8.0 0.8.0 0.7.4 0.7.3 0.7.3 0.7.0 0.7.0 0.7.0 0.7.0
plperl1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
Extensions for PostgreSQL 17 166
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension17.9 17.8 17.7 17.6R217.6 17.5R217.5 17.4R217.4 17.3 17.2 17.1 17.0 
Preview
17 
RC1
17 
Beta 
3
17 
Beta 
2
17 
Beta 
1
plpgsql1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plproﬁle 
r
4.2.5 4.2.5 4.2.5 4.2.5 4.2.5 4.2.5 4.2.5 4.2.5 4.2.5 4.2.5 4.2.5 4.2.4 4.2.4 4.2.4 4.2.4 4.2.4 4.2.4
plrust1.2.7 1.2.7 1.2.7 1.2.7 1.2.7 1.2.7 1.2.7 1.2.7 1.2.7 1.2.7 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pltcl 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plv8 3.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.10N/
A
N/
A
N/
A
N/
A
PostGIS3.5.1 3.5.1 3.5.1 3.5.1 3.5.1 3.5.1 3.5.1 3.5.1 3.5.0 3.5.0 3.5.0alph 
a2
3.5.0alph 
a2
3.5.0dev3.5.0dev3.5.0dev3.5.0dev3.5.0dev
postgis_r 
aster
3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0alph 
a2
3.5.0alph 
a2
3.5.0dev3.5.0dev3.5.0dev3.5.0dev3.5.0dev
postgis_t 
iger_geoc 
oder
3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0alph 
a2
3.5.0alph 
a2
3.5.0dev3.5.0dev3.5.0dev3.5.0dev3.5.0dev
postgis_t 
opology
3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0 3.5.0alph 
a2
3.5.0alph 
a2
3.5.0dev3.5.0dev3.5.0dev3.5.0dev3.5.0dev
postgres_ 
fdw
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
preﬁx1.2.101.2.101.2.101.2.101.2.101.2.101.2.101.2.101.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9
rdkit 2024_09_6 
(4.6.1)
2024_09_6 
(4.6.1)
2024_09_6 
(4.6.1)
2024_09_6 
(4.6.1)
2024_09_6 
(4.6.1)
2024_09_6 
(4.6.1)
2024_09_3 
(4.6.1)
2024_09_3 
(4.6.1)
2024_09_2 
(4.6.1)
2024_09_2 
(4.6.1)
4.6.0 4.6.0 4.6.0 N/
A
N/
A
N/
A
N/
A
rds_tools1.9 1.9 1.9 1.9 1.9 1.9 1.9 1.9 1.8 1.8 1.6 1.5 1.5 1.5 1.5 1.5 1.5
Extensions for PostgreSQL 17 167
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension17.9 17.8 17.7 17.6R217.6 17.5R217.5 17.4R217.4 17.3 17.2 17.1 17.0 
Preview
17 
RC1
17 
Beta 
3
17 
Beta 
2
17 
Beta 
1
reﬁnt 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
seg 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
sslinfo1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
tablefunc1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tcn 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tds_fdw2.0.5 2.0.5 2.0.4 2.0.4 2.0.4 2.0.4 2.0.4 2.0.4 2.0.4 2.0.4 2.0.4 2.0.3 2.0.3 2.0.3 N/
A
N/
A
N/
A
tsm_syste 
m_rows
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tsm_syste 
m_time
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
unaccent1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
uuid-
ossp
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
wal2json2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6
Extensions supported for RDS for PostgreSQL 16
The following table shows PostgreSQL extensions for PostgreSQL version 16 that are currently 
supported on Amazon RDS. For more information on PostgreSQL extensions, see Packaging related 
objects into an extension.
Extensions for PostgreSQL 16 168
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension16.1316.1216.1116.10R216.1016.9R216.916.8R216.816.716.616.516.416.3-
R2
16.316.2-
R3
16.2-
R2
16.216.1-
R2
16.116.0 
Preview
16 
RC1
16 
Beta 
3
16 
Beta 
2
16 
Beta 
1
address_s 
tandardiz 
er
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.4.03.4.03.4.0dev3.4.0dev3.4.0dev3.4.0dev3.4.0dev
address_s 
tandardiz 
er_data_u 
s
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.4.03.4.03.4.0dev3.4.0dev3.4.0dev3.4.0dev3.4.0dev
amcheck1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
auto_expl 
ain
yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
autoinc 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
aws_commo 
ns
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 N/
A
N/
A
N/
A
aws_lambd 
a
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 N/
A
N/
A
N/
A
aws_s31.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 N/
A
N/
A
N/
A
bloom1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
bool_plpe 
rl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
btree_gin1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
Extensions for PostgreSQL 16 169
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension16.1316.1216.1116.10R216.1016.9R216.916.8R216.816.716.616.516.416.3-
R2
16.316.2-
R3
16.2-
R2
16.216.1-
R2
16.116.0 
Preview
16 
RC1
16 
Beta 
3
16 
Beta 
2
16 
Beta 
1
btree_gis 
t
1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7
citext1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6
cube1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
dblink1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
decoder_r 
aw
yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes
dict_int1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
dict_xsyn1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
earthdist 
ance
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
ﬂow_cont 
rol
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
fuzzystrm 
atch
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
h3-
pg
4.2.34.2.34.2.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.3N/
A
N/
A
N/
A
hll 2.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.172.17N/
A
N/
A
N/
A
N/
A
N/
A
hstore1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8
hstore_pl 
perl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
Extensions for PostgreSQL 16 170
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension16.1316.1216.1116.10R216.1016.9R216.916.8R216.816.716.616.516.416.3-
R2
16.316.2-
R3
16.2-
R2
16.216.1-
R2
16.116.0 
Preview
16 
RC1
16 
Beta 
3
16 
Beta 
2
16 
Beta 
1
hypopg1.4.21.4.21.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.0N/
A
N/
A
N/
A
ICU 
module
60.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.2N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
insert_us 
ername 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
intagg1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
intarray1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
ip4r2.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.12.4.12.4.12.4.12.4.12.4.12.4.12.4.12.4.1
isn 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
jsonb_plp 
erl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
lo 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
log_fdw1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
ltree1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
moddateti 
me 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
mysql_fdw2.9.32.9.32.9.22.9.22.9.22.9.22.9.22.9.22.9.22.9.22.9.22.9.12.9.12.9.12.9.12.9.12.9.12.9.12.9.12.9.02.9.0N/
A
N/
A
N/
A
N/
A
Extensions for PostgreSQL 16 171
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension16.1316.1216.1116.10R216.1016.9R216.916.8R216.816.716.616.516.416.3-
R2
16.316.2-
R3
16.2-
R2
16.216.1-
R2
16.116.0 
Preview
16 
RC1
16 
Beta 
3
16 
Beta 
2
16 
Beta 
1
old_snaps 
hot
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
oracle_fd 
w
2.8.02.8.02.8.02.7.02.8.02.7.02.7.02.7.02.7.02.7.02.6.02.6.02.6.02.6.02.6.02.6.02.6.02.6.02.5.02.5.02.5.0N/
A
N/
A
N/
A
N/
A
orafce4.16.34.16.34.14.04.14.04.14.04.14.04.14.04.14.04.13.44.13.44.10.34.9.44.9.44.9.04.9.04.9.04.6.14.6.14.3.04.3.04.3.04.3.0N/
A
N/
A
N/
A
pageinspe 
ct
1.121.121.121.121.121.121.121.121.121.121.121.121.121.121.121.121.121.121.121.121.121.121.121.121.12
pg_bigm1.2-20250 
903
1.2-20250 
903
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 N/
A
N/
A
N/
A
N/
A
pg_buﬀer 
cache
1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
pg_cron1.6.71.6.71.6.51.6.51.6.51.6.51.6.51.6.51.6.41.6.41.6.31.6.21.6.21.6.21.6.21.6.21.6.11.6.11.5.21.5.2N/
A
N/
A
N/
A
N/
A
N/
A
pg_freesp 
acemap
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_hint_p 
lan
1.6.21.6.21.6.11.6.11.6.11.6.11.6.11.6.11.6.11.6.11.6.01.6.01.6.01.6.01.6.01.6.01.6.01.6.01.6.01.6.01.6.0N/
A
N/
A
N/
A
N/
A
pg_partma 
n
5.2.45.2.45.2.45.2.45.2.45.2.45.2.45.2.45.1.05.1.05.1.05.1.05.1.05.0.15.0.15.0.05.0.05.0.04.7.34.7.34.7.34.7.34.7.34.7.34.7.3
pg_prewar 
m
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_procta 
b
0.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.10N/
A
N/
A
N/
A
N/
A
N/
A
Extensions for PostgreSQL 16 172
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension16.1316.1216.1116.10R216.1016.9R216.916.8R216.816.716.616.516.416.3-
R2
16.316.2-
R3
16.2-
R2
16.216.1-
R2
16.116.0 
Preview
16 
RC1
16 
Beta 
3
16 
Beta 
2
16 
Beta 
1
pg_repack1.5.31.5.31.5.21.5.11.5.21.5.11.5.01.5.01.5.01.5.01.5.01.5.01.5.01.5.01.5.01.5.01.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.8
pg_simila 
rity
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_stat_s 
tatements
1.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.10
pg_tle1.5.21.5.21.5.21.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.1.11.1.11.1.11.1.01.1.01.1.01.0.41.0.41.0.4
pg_transp 
ort
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_trgm1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6
pg_visibi 
lity
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_walins 
pect
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
pgactive2.1.72.1.72.1.62.1.42.1.62.1.42.1.62.1.42.1.32.1.32.1.32.1.32.1.32.1.32.1.32.1.22.1.12.1.1N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pgAudit16.116.116.116.116.116.116.016.016.016.016.016.016.016.016.016.016.016.016.016.016.0N/
A
N/
A
N/
A
N/
A
pgcrypto1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
pglogical2.4.62.4.62.4.52.4.52.4.52.4.52.4.42.4.42.4.42.4.42.4.42.4.42.4.42.4.42.4.42.4.42.4.42.4.4N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pgrouting3.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.5.03.4.13.4.13.4.13.4.13.4.13.4.1
pgrowlock 
s
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
Extensions for PostgreSQL 16 173
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension16.1316.1216.1116.10R216.1016.9R216.916.8R216.816.716.616.516.416.3-
R2
16.316.2-
R3
16.2-
R2
16.216.1-
R2
16.116.0 
Preview
16 
RC1
16 
Beta 
3
16 
Beta 
2
16 
Beta 
1
pgstattup 
le
1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
pgTAP1.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.21.3.21.3.21.3.21.3.11.3.11.3.11.2.01.2.01.2.01.2.01.2.01.2.01.2.0
pgvector0.8.10.8.10.8.00.8.00.8.00.8.00.8.00.8.00.8.00.8.00.7.30.7.00.7.00.6.20.6.20.6.00.5.10.5.10.5.00.4.40.4.40.4.40.4.10.4.10.4.1
plcoﬀee3.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.93.1.83.1.73.1.73.1.7N/
A
N/
A
N/
A
N/
A
plls 3.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.93.1.83.1.73.1.73.1.7N/
A
N/
A
N/
A
N/
A
plperl1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plpgsql1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plproﬁle 
r
4.2.54.2.54.2.54.2.54.2.54.2.54.2.54.2.54.2.54.2.54.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.24.2.24.2.2N/
A
N/
A
N/
A
N/
A
plrust1.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.61.2.41.2.41.2.4N/
A
N/
A
N/
A
N/
A
pltcl1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plv83.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.93.1.83.1.73.1.73.1.7N/
A
N/
A
N/
A
N/
A
PostGIS3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.4.03.4.03.4.0dev3.4.0dev3.4.0dev3.4.0dev3.4.0dev
postgis_r 
aster
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.4.03.4.03.4.0dev3.4.0dev3.4.0dev3.4.0dev3.4.0dev
postgis_t 
iger_geoc 
oder
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.4.03.4.03.4.0dev3.4.0dev3.4.0dev3.4.0dev3.4.0dev
Extensions for PostgreSQL 16 174
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension16.1316.1216.1116.10R216.1016.9R216.916.8R216.816.716.616.516.416.3-
R2
16.316.2-
R3
16.2-
R2
16.216.1-
R2
16.116.0 
Preview
16 
RC1
16 
Beta 
3
16 
Beta 
2
16 
Beta 
1
postgis_t 
opology
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.4.03.4.03.4.0dev3.4.0dev3.4.0dev3.4.0dev3.4.0dev
postgres_ 
fdw
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
preﬁx1.2.101.2.101.2.101.2.101.2.101.2.101.2.101.2.101.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.9
rdkit4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_3 
)
4.6.1 
(Release 
2024_09_3 
)
4.6.14.6.14.5.0 
(Release 
2024_03_5 
)
4.4.04.4.04.4.04.4.04.4.04.4.04.4.04.3.0N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
rds_tools1.9 1.9 1.9 1.9 1.9 1.9 1.9 1.9 1.7 1.7 1.5 1.5 1.5 1.4 1.4 1.4 1.4 1.4 1.2 1.2 1.2 1.2 1.2 1.2 1.2
reﬁnt 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
seg 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
sslinfo1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
tablefunc1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tcn 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
tds_fdw2.0.52.0.52.0.42.0.42.0.42.0.42.0.42.0.42.0.42.0.42.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.3
tsm_syste 
m_rows
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tsm_syste 
m_time
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
Extensions for PostgreSQL 16 175
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension16.1316.1216.1116.10R216.1016.9R216.916.8R216.816.716.616.516.416.3-
R2
16.316.2-
R3
16.2-
R2
16.216.1-
R2
16.116.0 
Preview
16 
RC1
16 
Beta 
3
16 
Beta 
2
16 
Beta 
1
unaccent1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
uuid-
ossp
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
wal2json2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5
Extensions supported for RDS for PostgreSQL 15
The following table shows PostgreSQL extensions for PostgreSQL version 15 that are currently 
supported on Amazon RDS. For more information on PostgreSQL extensions, see Packaging related 
objects into an extension.
Extension15.1715.1615.1515.14R215.1415.13R215.1315.12R215.1215.1115.1015.915.815.7-
R2
15.715.6-
R3
15.6-
R2
15.615.5-
R2
15.515.4-
R3
15.4-
R2
15.415.3-
R2
15.315.2-
R2
address_s 
tandardiz 
er
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.33.3.23.3.23.3.23.3.23.3.2
address_s 
tandardiz 
er_data_u 
s
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.33.3.23.3.23.3.23.3.23.3.2
amcheck1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
auto_expl 
ain
yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes
autoinc 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
Extensions for PostgreSQL 15 176
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension15.1715.1615.1515.14R215.1415.13R215.1315.12R215.1215.1115.1015.915.815.7-
R2
15.715.6-
R3
15.6-
R2
15.615.5-
R2
15.515.4-
R3
15.4-
R2
15.415.3-
R2
15.315.2-
R2
aws_commo 
ns
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
aws_lambd 
a
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
aws_s31.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
bloom1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
bool_plpe 
rl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
btree_gin1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
btree_gis 
t
1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7
citext1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6
cube1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
dblink1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
decoder_r 
aw
yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes
dict_int1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
dict_xsyn1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
earthdist 
ance
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
ﬂow_cont 
rol
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
Extensions for PostgreSQL 15 177
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension15.1715.1615.1515.14R215.1415.13R215.1315.12R215.1215.1115.1015.915.815.7-
R2
15.715.6-
R3
15.6-
R2
15.615.5-
R2
15.515.4-
R3
15.4-
R2
15.415.3-
R2
15.315.2-
R2
fuzzystrm 
atch
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
h3-
pg
4.2.34.2.34.2.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.24.1.24.1.2N/
A
N/
A
N/
A
N/
A
hll 2.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.172.172.172.172.172.172.172.17
hstore1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8 1.8
hstore_pl 
perl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
hypopg1.4.21.4.21.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.3.11.3.1N/
A
N/
A
N/
A
ICU 
module
60.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.2
insert_us 
ername 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
intagg1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
intarray1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
ip4r2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4
isn 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
jsonb_plp 
erl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
lo 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
Extensions for PostgreSQL 15 178
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension15.1715.1615.1515.14R215.1415.13R215.1315.12R215.1215.1115.1015.915.815.7-
R2
15.715.6-
R3
15.6-
R2
15.615.5-
R2
15.515.4-
R3
15.4-
R2
15.415.3-
R2
15.315.2-
R2
log_fdw1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
ltree1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
moddateti 
me 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
mysql_fdw2.9.32.9.32.9.22.9.22.9.22.9.22.9.22.9.22.9.22.9.22.9.22.9.12.9.12.9.12.9.12.9.12.9.12.9.12.9.12.9.12.9.02.9.02.9.02.9.02.9.02.9.0
old_snaps 
hot
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
oracle_fd 
w
2.8.02.8.02.8.02.7.02.8.02.7.02.7.02.7.02.7.02.7.02.6.02.6.02.6.02.6.02.6.02.6.02.6.02.6.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.0
orafce4.16.34.16.34.14.04.14.04.14.04.14.04.14.04.14.04.13.44.13.44.10.34.9.44.9.44.9.04.9.04.9.04.6.14.6.14.3.04.3.04.3.03.243.243.243.243.24
pageinspe 
ct
1.111.111.111.111.111.111.111.111.111.111.111.111.111.111.111.111.111.111.111.111.111.111.111.111.111.11
pg_bigm1.2_20250 
903
1.2_20250 
903
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_buﬀer 
cache
1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
pg_cron1.6.71.6.71.6.51.6.51.6.51.6.51.6.51.6.51.6.41.6.41.6.31.6.21.6.21.6.21.6.21.6.21.6.11.6.11.5.21.5.21.5.21.5.21.5.21.4.11.4.11.4.1
pg_freesp 
acemap
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_hint_p 
lan
1.5.31.5.31.6.11.6.11.6.11.6.11.6.11.6.11.5.21.5.21.5.11.5.11.5.11.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
Extensions for PostgreSQL 15 179
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension15.1715.1615.1515.14R215.1415.13R215.1315.12R215.1215.1115.1015.915.815.7-
R2
15.715.6-
R3
15.6-
R2
15.615.5-
R2
15.515.4-
R3
15.4-
R2
15.415.3-
R2
15.315.2-
R2
pg_partma 
n
5.2.45.2.45.2.45.2.45.2.45.2.45.2.45.2.45.1.05.1.05.1.05.1.05.1.05.0.15.0.15.0.05.0.05.0.04.7.34.7.34.7.34.7.34.7.34.6.24.6.24.6.2
pg_prewar 
m
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_procta 
b
0.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.9
pg_repack1.5.31.5.31.5.21.5.11.5.21.5.11.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.81.4.8
pg_simila 
rity
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_stat_s 
tatements
1.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.101.10
pg_tle1.5.21.5.21.5.21.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.1.11.1.11.1.11.1.11.1.11.1.11.0.41.0.41.0.11.0.1
pg_transp 
ort
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_trgm1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6
pg_visibi 
lity
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_walins 
pect
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pgactive2.1.72.1.72.1.62.1.42.1.62.1.42.1.62.1.42.1.32.1.32.1.32.1.32.1.32.1.32.1.32.1.22.1.12.1.12.1.02.1.0N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pgAudit1.7.11.7.11.7.11.7.11.7.11.7.11.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.01.7.0
pgcrypto1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
Extensions for PostgreSQL 15 180
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension15.1715.1615.1515.14R215.1415.13R215.1315.12R215.1215.1115.1015.915.815.7-
R2
15.715.6-
R3
15.6-
R2
15.615.5-
R2
15.515.4-
R3
15.4-
R2
15.415.3-
R2
15.315.2-
R2
pglogical2.4.62.4.62.4.52.4.52.4.52.4.52.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.22.4.22.4.22.4.22.4.2
pgrouting3.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.13.4.1
pgrowlock 
s
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pgstattup 
le
1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
pgTAP1.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.21.3.21.3.21.3.21.3.11.3.11.3.11.2.01.2.01.2.01.2.01.2.01.2.01.2.01.2.0
pgvector0.8.10.8.10.8.00.8.00.8.00.8.00.8.00.8.00.8.00.8.00.7.30.7.00.7.00.6.20.6.20.6.00.5.10.5.10.5.10.5.00.4.40.4.40.4.10.4.1N/
A
N/
A
plcoﬀee3.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.93.1.83.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.4
plls3.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.93.1.83.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.4
plperl1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plpgsql1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plproﬁle 
r
4.2.54.2.54.2.54.2.54.2.54.2.54.2.54.2.54.2.54.2.54.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.14.2.14.2.14.2.14.2.14.2.14.2.14.2.1
plrust1.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.61.2.51.2.51.2.31.1.11.1.11.0.0N/
A
N/
A
pltcl1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plv83.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.93.1.83.1.83.1.83.1.63.1.63.1.63.1.43.1.43.1.4
PostGIS3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.33.3.23.3.23.3.23.3.23.3.2
postgis_r 
aster
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.33.3.23.3.23.3.23.3.23.3.2
Extensions for PostgreSQL 15 181
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension15.1715.1615.1515.14R215.1415.13R215.1315.12R215.1215.1115.1015.915.815.7-
R2
15.715.6-
R3
15.6-
R2
15.615.5-
R2
15.515.4-
R3
15.4-
R2
15.415.3-
R2
15.315.2-
R2
postgis_t 
iger_geoc 
oder
3.4.3.3.4.3.3.4.3.3.4.3.3.4.3.3.4.3.3.4.3.3.4.3.3.4.3.3.4.3.3.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.33.3.23.3.23.3.23.3.23.3.2
postgis_t 
opology
3.4.23.4.23.4.23.4.23.4.23.4.23.4.23.4.23.4.23.4.23.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.33.3.23.3.23.3.23.3.23.3.2
postgres_ 
fdw
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
preﬁx1.2.101.2.101.2.101.2.101.2.101.2.101.2.101.2.101.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.9
rdkit4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_6 
)
4.6.1 
(Release 
2024_09_3 
)
4.6.1 
(Release 
2024_09_3 
)
4.6.14.6.14.5.0 
(Release 
2024_03_5 
)
4.4.04.4.04.4.04.4.04.4.04.4.04.4.04.3.04.3.04.2.04.2.04.2.04.2.04.2.04.2.0
rds_tools1.9 1.9 1.9 1.9 1.9 1.9 1.9 1.9 1.7 1.7 1.5 1.5 1.5 1.4 1.4 1.4 1.4 1.4 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
reﬁnt 
(contrib- 
spi)
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
seg1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
sslinfo1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
tablefunc1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tcn 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tds_fdw2.0.52.0.52.0.42.0.42.0.42.0.42.0.42.0.42.0.42.0.42.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.32.0.3
tsm_syste 
m_rows
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
Extensions for PostgreSQL 15 182
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension15.1715.1615.1515.14R215.1415.13R215.1315.12R215.1215.1115.1015.915.815.7-
R2
15.715.6-
R3
15.6-
R2
15.615.5-
R2
15.515.4-
R3
15.4-
R2
15.415.3-
R2
15.315.2-
R2
tsm_syste 
m_time
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
unaccent1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
uuid-
ossp
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
wal2json2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.6 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5
Extensions supported for RDS for PostgreSQL 14
The following table shows PostgreSQL extensions for PostgreSQL version 14 that are currently 
supported on Amazon RDS. For more information on PostgreSQL extensions, see Packaging related 
objects into an extension.
Extension14.2214.2114.2014.19R214.1914.18R214.1814.17R214.1714.1614.1514.1414.1314.12-
R2
14.1214.11-
R3
14.11-
R2
14.1114.10-
R2
14.1014.9-
R2
14.914.8-
R2
14.814.714.614.514.414.314.2
address_s 
tandardiz 
er
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.53.1.53.1.5
address_s 
tandardiz 
er_data_u 
s
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.53.1.53.1.5
amcheck1.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.3
autoinc 
(contrib- 
spi)
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
Extensions for PostgreSQL 14 183
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension14.2214.2114.2014.19R214.1914.18R214.1814.17R214.1714.1614.1514.1414.1314.12-
R2
14.1214.11-
R3
14.11-
R2
14.1114.10-
R2
14.1014.9-
R2
14.914.8-
R2
14.814.714.614.514.414.314.2
auto_expl 
ain
yesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyes
aws_commo 
ns
1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
aws_lambd 
a
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
aws_s31.21.21.21.21.21.21.21.21.21.21.21.21.21.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
bloom1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
bool_plpe 
rl
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
btree_gin1.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.3
btree_gis 
t
1.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.6
citext1.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.6
cube1.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.5
dblink1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
dict_int1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
dict_xsyn1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
earthdist 
ance
1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
ﬂow_cont 
rol
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
Extensions for PostgreSQL 14 184
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension14.2214.2114.2014.19R214.1914.18R214.1814.17R214.1714.1614.1514.1414.1314.12-
R2
14.1214.11-
R3
14.11-
R2
14.1114.10-
R2
14.1014.9-
R2
14.914.8-
R2
14.814.714.614.514.414.314.2
fuzzystrm 
atch
1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
h3-
pg
4.2.34.2.34.2.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.24.1.2N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
hll 2.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.162.162.162.162.162.162.162.162.162.152.152.15
hstore1.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.8
hstore_pl 
perl
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
hypopg1.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.3.11.3.1N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
ICU 
module
60.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.2
insert_us 
ername 
(contrib- 
spi)
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
intagg1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
intarray1.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.5
ip4r2.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.4
isn 1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
jsonb_plp 
erl
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
lo 1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
Extensions for PostgreSQL 14 185
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension14.2214.2114.2014.19R214.1914.18R214.1814.17R214.1714.1614.1514.1414.1314.12-
R2
14.1214.11-
R3
14.11-
R2
14.1114.10-
R2
14.1014.9-
R2
14.914.8-
R2
14.814.714.614.514.414.314.2
log_fdw1.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.3
ltree1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
mysql_fdw2.9.32.9.32.9.22.9.22.9.22.9.22.9.22.9.22.9.22.9.22.9.22.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.0N/
A
N/
A
moddateti 
me 
(contrib- 
spi)
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
old_snaps 
hot
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
oracle_fd 
w
2.8.12.8.12.8.02.7.02.8.02.7.02.7.02.7.02.7.02.7.02.6.02.6.02.6.02.6.02.6.02.6.02.6.02.6.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.0
orafce4.16.34.16.34.14.4.14.4.14.4.14.4.14.4.14.4.13.44.13.44.10.34.9.44.9.44.9.04.9.04.9.04.6.14.6.14.3.04.3.03.243.243.243.243.153.153.153.153.153.15
pageinspe 
ct
1.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.9
pg_bigm1.2_20250 
903
1.2_20250 
903
1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
pg_buﬀer 
cache
1.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.3
pg_cron1.6.71.6.71.6.51.6.51.6.51.6.51.6.51.6.51.6.41.6.41.6.31.6.21.6.21.6.21.6.21.6.21.6.11.6.11.5.21.5.21.5.21.5.21.4.11.4.11.4.11.41.41.41.41.4
pg_freesp 
acemap
1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
pg_hint_p 
lan
1.4.41.4.41.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.21.4.21.4.21.41.41.41.41.41.41.41.41.41.41.41.41.41.41.3.71.3.71.3.7
Extensions for PostgreSQL 14 186
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension14.2214.2114.2014.19R214.1914.18R214.1814.17R214.1714.1614.1514.1414.1314.12-
R2
14.1214.11-
R3
14.11-
R2
14.1114.10-
R2
14.1014.9-
R2
14.914.8-
R2
14.814.714.614.514.414.314.2
pg_partma 
n
5.2.45.2.45.2.45.2.45.2.45.2.45.2.45.2.45.1.05.1.05.1.05.1.05.1.05.0.15.0.14.5.14.5.14.5.14.7.34.7.34.7.34.7.34.6.24.6.24.6.24.6.04.6.04.6.04.6.04.6.0
pg_prewar 
m
1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
pg_procta 
b
0.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.9
pg_repack1.5.31.5.31.5.21.4.71.5.21.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.71.4.7
pg_simila 
rity
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
pg_stat_s 
tatements
1.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.91.9
pg_tle1.5.21.5.21.5.21.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.1.11.1.11.1.11.1.11.1.11.0.41.0.41.0.11.0.11.0.1N/
A
N/
A
N/
A
N/
A
pg_transp 
ort
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
pg_trgm1.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.6
pg_visibi 
lity
1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
pgactive2.1.72.1.72.1.62.1.42.1.62.1.42.1.62.1.42.1.32.1.32.1.32.1.32.1.32.1.32.1.32.1.22.1.12.1.1N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pgAudit1.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.21.6.11.6.11.6.11.6.11.61.6
pgcrypto1.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.3
pglogical2.4.62.4.62.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.22.4.22.4.12.4.12.4.12.4.12.4.12.4.02.4.02.4.0
Extensions for PostgreSQL 14 187
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension14.2214.2114.2014.19R214.1914.18R214.1814.17R214.1714.1614.1514.1414.1314.12-
R2
14.1214.11-
R3
14.11-
R2
14.1114.10-
R2
14.1014.9-
R2
14.914.8-
R2
14.814.714.614.514.414.314.2
pgrouting3.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.23.2.03.2.03.2.03.2.03.2.0
pgrowlock 
s
1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
pgstattup 
le
1.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.5
pgTAP1.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.21.3.21.3.21.3.21.3.11.3.11.3.11.2.01.2.01.2.01.2.01.2.01.2.01.1.01.1.01.1.01.1.01.1.01.1.0
pgvector0.8.10.8.10.8.00.8.00.8.00.8.00.8.00.8.00.8.00.8.00.7.30.7.00.7.00.6.20.6.20.6.00.5.10.5.10.5.00.4.40.4.40.4.1N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
plcoﬀee3.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.102.3.153.1.102.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.15
plls3.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.102.3.153.1.102.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.15
plperl1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
plpgsql1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
plproﬁle 
r
4.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.14.14.14.14.14.14.14.14.14.14.14.1
plrust1.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.61.2.51.2.3N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pltcl1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
plv83.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.102.3.153.1.102.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.15
PostGIS3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.53.1.43.1.4
postgis_r 
aster
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.53.1.43.1.4
Extensions for PostgreSQL 14 188
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension14.2214.2114.2014.19R214.1914.18R214.1814.17R214.1714.1614.1514.1414.1314.12-
R2
14.1214.11-
R3
14.11-
R2
14.1114.10-
R2
14.1014.9-
R2
14.914.8-
R2
14.814.714.614.514.414.314.2
postgis_t 
iger_geoc 
oder
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.53.1.43.1.4
postgis_t 
opology
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.23.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.53.1.43.1.4
postgres_ 
fdw
1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
preﬁx1.2.101.2.101.2.101.2.101.2.101.2.101.2.101.2.101.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.9
rdkit4.6.1 
(Release 
2024_09_3 
)
4.6.1 
(Release 
2024_09_3 
)
4.6.1 
(Release 
2024_09_3 
)
4.6.1 
(Release 
2024_09_3 
)
4.6.1 
(Release 
2024_09_3 
)
4.6.1 
(Release 
2024_09_3 
)
4.6.1 
(Release 
2024_09_3 
)
4.6.1 
(Release 
2024_09_3 
)
4.6.14.6.14.5.0 
(Release 
2024_03_5 
)
4.4.04.4.04.4.04.4.04.4.04.4.04.4.04.3.04.2.04.2.04.2.04.2.04.2.03.83.83.83.83.83.8
rds_tools1.91.91.91.91.91.91.91.91.71.71.51.51.51.41.41.41.41.41.01.01.01.01.01.01.01.01.01.01.01.0
reﬁnt 
(contrib- 
spi)
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
seg1.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.4N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
sslinfo1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
tablefunc1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
tcn1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
tds_fdw2.0.52.0.52.0.42.0.42.0.42.0.42.0.42.0.42.0.42.0.42.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.2N/
A
N/
A
Extensions for PostgreSQL 14 189
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension14.2214.2114.2014.19R214.1914.18R214.1814.17R214.1714.1614.1514.1414.1314.12-
R2
14.1214.11-
R3
14.11-
R2
14.1114.10-
R2
14.1014.9-
R2
14.914.8-
R2
14.814.714.614.514.414.314.2
tsm_syste 
m_rows
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
tsm_syste 
m_time
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
unaccent1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
uuid-
ossp
1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
wal2json2.62.62.62.62.62.62.62.62.62.62.62.52.52.52.52.52.52.52.52.52.52.52.52.52.32.32.32.32.32.3
Extensions supported for RDS for PostgreSQL 13
The following table shows PostgreSQL extensions for PostgreSQL version 13 that are currently 
supported on Amazon RDS. For more information on PostgreSQL extensions, see Packaging related 
objects into an extension.
Extension13.2313.22R213.2213.21R213.2113.20R213.2013.1913.1813.1713.1613.15-
R2
13.1513.14-
R3
13.14-
R2
13.1413.13-
R2
13.1313.12-
R2
13.1213.11-
R2
13.1113.1013.913.813.713.613.513.4
address_s 
tandardiz 
er
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.33.0.3
address_s 
tandardiz 
er_data_u 
s
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.33.0.3
amcheck1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
auto_expl 
ain
yesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyes
Extensions for PostgreSQL 13 190
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension13.2313.22R213.2213.21R213.2113.20R213.2013.1913.1813.1713.1613.15-
R2
13.1513.14-
R3
13.14-
R2
13.1413.13-
R2
13.1313.12-
R2
13.1213.11-
R2
13.1113.1013.913.813.713.613.513.4
autoinc 
(contrib- 
spi)
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0N/
A
N/
A
aws_commo 
ns
1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.11.1
aws_lambd 
a
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
aws_s31.21.21.21.21.21.21.21.21.21.21.21.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
bloom1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
bool_plpe 
rl
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
btree_gin1.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.3
btree_gis 
t
1.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.5
citext1.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.61.6
cube1.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.41.4
dblink1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
dict_int1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
dict_xsyn1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
earthdist 
ance
1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
ﬂow_cont 
rol
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
Extensions for PostgreSQL 13 191
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension13.2313.22R213.2213.21R213.2113.20R213.2013.1913.1813.1713.1613.15-
R2
13.1513.14-
R3
13.14-
R2
13.1413.13-
R2
13.1313.12-
R2
13.1213.11-
R2
13.1113.1013.913.813.713.613.513.4
fuzzystrm 
atch
1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
h3-
pg
4.2.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.34.1.24.1.2N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
hll 2.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.182.152.152.152.152.152.152.152.152.152.152.152.152.15
hstore1.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.71.7
hstore_pl 
perl
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
hypopg1.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.11.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.3.11.3.1N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
ICU 
module
60.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.2
insert_us 
ername 
(contrib- 
spi)
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0N/
A
N/
A
intagg1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
intarray1.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.3
ip4r2.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.42.4
isn 1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
jsonb_plp 
erl
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
lo 1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.01.01.01.0
Extensions for PostgreSQL 13 192
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension13.2313.22R213.2213.21R213.2113.20R213.2013.1913.1813.1713.1613.15-
R2
13.1513.14-
R3
13.14-
R2
13.1413.13-
R2
13.1313.12-
R2
13.1213.11-
R2
13.1113.1013.913.813.713.613.513.4
log_fdw1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
ltree1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
moddateti 
me 
(contrib- 
spi)
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0N/
A
N/
A
mysql_fdw2.9.22.9.22.9.22.9.22.9.22.9.22.9.22.9.22.9.22.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.02.7.0N/
A
N/
A
N/
A
N/
A
oracle_fd 
w
2.8.02.7.02.8.02.7.02.7.02.7.02.7.02.7.02.6.02.6.02.6.02.6.02.6.02.6.02.6.02.6.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.0
orafce4.14.04.14.04.14.04.14.04.14.04.14.04.13.44.13.44.10.34.9.44.9.44.9.04.9.04.9.04.6.14.6.14.3.04.3.03.243.243.243.243.153.153.153.153.153.153.15
pageinspe 
ct
1.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.8
pg_bigm1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
pg_buﬀer 
cache
1.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.3
pg_cron1.6.51.6.51.6.51.6.51.6.51.6.51.6.41.6.41.6.31.6.21.6.21.6.21.6.21.6.21.6.11.6.11.5.21.5.21.5.21.5.21.4.11.4.11.4.11.4.11.4.11.4.11.3.11.3.11.3.1
pg_freesp 
acemap
1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
pg_hint_p 
lan
1.3.101.3.101.3.101.3.101.3.101.3.101.3.101.3.101.3.91.3.91.3.91.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.7
pg_partma 
n
4.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.1
Extensions for PostgreSQL 13 193
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension13.2313.22R213.2213.21R213.2113.20R213.2013.1913.1813.1713.1613.15-
R2
13.1513.14-
R3
13.14-
R2
13.1413.13-
R2
13.1313.12-
R2
13.1213.11-
R2
13.1113.1013.913.813.713.613.513.4
pg_prewar 
m
1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
pg_procta 
b
0.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.9
pg_repack1.5.21.5.11.5.21.5.11.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.61.4.6
pg_simila 
rity
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
pg_stat_s 
tatements
1.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.81.8
pg_tle1.5.21.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.4.01.1.11.1.11.1.11.1.11.1.1N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pg_transp 
ort
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
pg_trgm1.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.5
pg_visibi 
lity
1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
pgactive2.1.62.1.42.1.62.1.42.1.62.1.42.1.32.1.32.1.32.1.32.1.32.1.32.1.32.1.22.1.12.1.1N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pgAudit1.5.31.5.31.5.31.5.31.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.21.5.11.5.11.5.11.51.51.51.5
pgcrypto1.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.3
pglogical2.4.52.4.52.4.52.4.52.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.22.4.22.4.12.4.12.4.12.4.12.4.02.4.02.4.02.3.32.3.3
pgrouting3.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.43.1.33.1.33.1.33.1.33.1.03.1.0
Extensions for PostgreSQL 13 194
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension13.2313.22R213.2213.21R213.2113.20R213.2013.1913.1813.1713.1613.15-
R2
13.1513.14-
R3
13.14-
R2
13.1413.13-
R2
13.1313.12-
R2
13.1213.11-
R2
13.1113.1013.913.813.713.613.513.4
pgrowlock 
s
1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
pgstattup 
le
1.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.51.5
pgTAP1.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.31.3.21.3.21.3.21.3.21.3.11.3.11.3.11.2.01.2.01.2.01.2.01.2.01.2.01.1.01.1.01.1.01.1.01.1.01.1.01.1.0
pgvector0.8.00.8.00.8.00.8.00.8.00.8.00.8.00.8.00.7.30.7.00.7.00.6.20.6.20.6.00.5.10.5.10.5.00.4.40.4.40.4.1N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
plcoﬀee3.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.102.3.153.1.102.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.15
plls3.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.102.3.153.1.102.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.15
plperl1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
plpgsql1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
plproﬁle 
r
4.2.54.2.54.2.54.2.54.2.54.2.54.2.54.2.54.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.14.14.14.14.14.14.14.14.14.14.14.14.1
plrust1.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.71.2.61.2.51.2.3N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pltcl1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
plv83.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.103.1.102.3.153.1.102.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.152.3.15
PostGIS3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.33.0.3
postgis_r 
aster
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.33.0.3
postgis_t 
iger_geoc 
oder
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.33.0.3
Extensions for PostgreSQL 13 195
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension13.2313.22R213.2213.21R213.2113.20R213.2013.1913.1813.1713.1613.15-
R2
13.1513.14-
R3
13.14-
R2
13.1413.13-
R2
13.1313.12-
R2
13.1213.11-
R2
13.1113.1013.913.813.713.613.513.4
postgis_t 
opology
3.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.33.0.3
postgres_ 
fdw
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
preﬁx1.2.101.2.101.2.101.2.101.2.101.2.101.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.9
rdkit3.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.83.8
rds_tools1.91.91.91.91.91.91.71.71.51.51.51.41.41.41.41.41.01.01.01.01.01.01.01.01.01.01.01.01.0
reﬁnt 
(contrib- 
spi)
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0N/
A
N/
A
seg1.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.31.3N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
sslinfo1.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.21.2
tablefunc1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
tcn1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
tds_fdw2.0.42.0.42.0.42.0.42.0.42.0.42.0.42.0.42.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.22.0.2N/
A
N/
A
N/
A
N/
A
tsm_syste 
m_rows
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
tsm_syste 
m_time
1.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.01.0
unaccent1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
Extensions for PostgreSQL 13 196
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension13.2313.22R213.2213.21R213.2113.20R213.2013.1913.1813.1713.1613.15-
R2
13.1513.14-
R3
13.14-
R2
13.1413.13-
R2
13.1313.12-
R2
13.1213.11-
R2
13.1113.1013.913.813.713.613.513.4
uuid-
ossp
1.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.11.1
wal2json2.62.62.62.62.62.62.62.62.62.52.52.52.52.52.52.52.52.52.52.52.52.52.32.32.32.32.32.32.3
Extensions supported for RDS for PostgreSQL 12
The following table shows PostgreSQL extensions for PostgreSQL version 12 that are currently 
supported on Amazon RDS. For more information on PostgreSQL extensions, see Packaging related 
objects into an extension.
Extension12.2212.2112.2012.19-
R2
12.1912.18-
R3
12.18-
R2
12.1812.17-
R2
12.1712.16-
R2
12.1612.1512.1412.1312.1212.1112.1012.912.812.7
address_s 
tandardiz 
er
3.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.3
address_s 
tandardiz 
er_data_u 
s
3.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.3
amcheck1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
auto_expl 
ain
yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes
aws_commo 
ns
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.0 1.0 1.0
aws_lambd 
a
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
aws_s31.2 1.2 1.2 1.2 1.2 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
Extensions for PostgreSQL 12 197
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension12.2212.2112.2012.19-
R2
12.1912.18-
R3
12.18-
R2
12.1812.17-
R2
12.1712.16-
R2
12.1612.1512.1412.1312.1212.1112.1012.912.812.7
bloom1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
btree_gin1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
btree_gis 
t
1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
citext1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6
cube1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
dblink1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
dict_int1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
dict_xsyn1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
earthdist 
ance
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
fuzzystrm 
atch
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
hll 2.182.182.182.182.182.182.182.182.182.182.142.142.142.142.142.142.142.142.142.142.14
hstore1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6
hstore_pl 
perl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
ICU 
module
60.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.260.2
intagg1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
intarray1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
ip4r 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4 2.4
Extensions for PostgreSQL 12 198
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension12.2212.2112.2012.19-
R2
12.1912.18-
R3
12.18-
R2
12.1812.17-
R2
12.1712.16-
R2
12.1612.1512.1412.1312.1212.1112.1012.912.812.7
isn 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
jsonb_plp 
erl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
lo 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.0 1.0 1.0
log_fdw1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
ltree1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
oracle_fd 
w
2.7.02.7.02.6.02.6.02.6.02.6.02.6.02.6.02.6.02.6.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.02.3.0
orafce4.13.44.13.44.10.34.9.44.9.44.9.04.9.04.9.04.6.14.6.14.3.04.3.03.243.243.243.153.153.153.153.153.15
pageinspe 
ct
1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7
pg_bigm1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_buﬀer 
cache
1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
pg_cron1.6.41.6.41.6.31.6.21.6.21.6.21.6.21.6.21.6.11.6.11.5.21.5.21.5.21.4.11.4.11.4.11.4.11.4.11.4.11.3.11.3.1
pg_freesp 
acemap
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_hint_p 
lan
1.3.101.3.101.3.91.3.91.3.91.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.71.3.51.3.5
pg_partma 
n
4.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.14.5.1
pg_prewar 
m
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
Extensions for PostgreSQL 12 199
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension12.2212.2112.2012.19-
R2
12.1912.18-
R3
12.18-
R2
12.1812.17-
R2
12.1712.16-
R2
12.1612.1512.1412.1312.1212.1112.1012.912.812.7
pg_procta 
b
0.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.100.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.90.0.9
pg_repack1.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.51.4.5
pg_simila 
rity
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_stat_s 
tatements
1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7
pg_transp 
ort
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_trgm1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
pg_visibi 
lity
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pgactive2.1.32.1.32.1.32.1.32.1.32.1.32.1.32.1.22.1.12.1.1N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pgAudit1.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.21.4.21.4.21.4 1.4 1.4
pgcrypto1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
pglogical2.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.32.4.22.4.12.4.12.4.12.4.12.4.02.4.02.4.02.3.2
pgrouting3.0.63.0.63.0.63.0.63.0.63.0.63.0.63.0.63.0.63.0.63.0.63.0.63.0.63.0.63.0.63.0.63.0.53.0.53.0.53.0.53.0.0
pgrowlock 
s
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pgstattup 
le
1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
pgTAP1.3.31.3.31.3.31.3.21.3.21.3.21.3.21.3.11.3.11.3.11.2.01.2.01.2.01.2.01.2.01.1.01.1.01.1.01.1.01.1.01.1.0
Extensions for PostgreSQL 12 200
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension12.2212.2112.2012.19-
R2
12.1912.18-
R3
12.18-
R2
12.1812.17-
R2
12.1712.16-
R2
12.1612.1512.1412.1312.1212.1112.1012.912.812.7
pgvector0.7.30.7.30.7.30.7.00.7.00.6.20.6.20.6.00.5.10.5.10.5.0N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
plcoﬀee3.1.103.1.103.1.103.1.102.3.143.1.102.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.14
plls 3.1.103.1.103.1.103.1.102.3.143.1.102.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.14
plperl1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plpgsql1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plproﬁle 
r
4.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.2.44.1 4.1 4.1 4.1 4.1 4.1 4.1 4.1 4.1 4.1 4.1
pltcl1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plv83.1.103.1.103.1.103.1.102.3.143.1.102.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.142.3.14
PostGIS3.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.3
postgis_r 
aster
3.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.3
postgis_t 
iger_geoc 
oder
3.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.3
postgis_t 
opology
3.4.33.4.33.4.23.4.23.4.23.4.13.4.13.4.13.4.03.4.03.3.33.3.33.3.23.1.73.1.73.1.73.1.53.1.53.1.43.1.43.0.3
postgres_ 
fdw
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
preﬁx1.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.91.2.9
rdkit3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8
Extensions for PostgreSQL 12 201
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension12.2212.2112.2012.19-
R2
12.1912.18-
R3
12.18-
R2
12.1812.17-
R2
12.1712.16-
R2
12.1612.1512.1412.1312.1212.1112.1012.912.812.7
rds_tools1.7 1.7 1.5 1.5 1.5 1.3 1.3 1.3 1.3 1.3 1 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
seg 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
sslinfo1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
tablefunc1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tcn 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
tsm_syste 
m_rows
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tsm_syste 
m_time
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
unaccent1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
uuid-
ossp
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
wal2json2.6 2.6 2.6 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.3 2.3 2.3 2.3 2.3 2.3
Extensions supported for RDS for PostgreSQL 11
The following tables show PostgreSQL extensions for PostgreSQL version 11.x that are currently 
supported by RDS for PostgreSQL. "N/A" indicates that the extension isn't available for that 
PostgreSQL version. For more information on PostgreSQL extensions, see Packaging related 
objects into an extension.
Extensions for PostgreSQL 11 202
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 11.22-
RDS 
.20240509
11.22-
R2
11.22 11.21 11.20 11.19 11.18 11.17 11.16 11.15 11.14 11.13 11.12
address_s 
tandardizer
3.3.3 3.3.3 3.3.3 3.3.2 3.3.2 3.1.7 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 2.5.1
address_s 
tandardiz 
er_data_us
3.3.3 3.3.3 3.3.3 3.3.2 3.3.2 3.1.7 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 2.5.1
aws_commons 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.1 1.1 1.1 1.1
aws_lambda 1 1 1 1 1 1 1 1 1 N/
A
N/
A
N/
A
N/
A
aws_s3 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
amcheck yes yes yes yes yes yes yes yes yes yes yes yes yes
auto_explain yes yes yes yes yes yes yes yes yes yes yes yes yes
bloom 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
btree_gin 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
btree_gist 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
citext 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
cube 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
dblink 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
dict_int 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
dict_xsyn 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
earthdistance 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
fuzzystrmatch 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
Extensions for PostgreSQL 11 203
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 11.22-
RDS 
.20240509
11.22-
R2
11.22 11.21 11.20 11.19 11.18 11.17 11.16 11.15 11.14 11.13 11.12
hll 2.18 2.18 2.18 2.11 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
hstore 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
hstore_plperl 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
ICU module 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2 60.2
intagg 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
intarray 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
ip4r 2.3 2.3 2.3 2.3 2.3 2.3 2.3 2.3 2.3 2.3 2.3 2.3 2.3
isn 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
lo 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 N/
A
N/
A
N/
A
log_fdw 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
libprotobuf 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0
ltree 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
orafce 4.6.1 4.6.1 4.6.1 3.24 3.24 3.24 3.24 3.15 3.15 3.15 3.15 3.15 3.15
pageinspect 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7 1.7
pg_bigm 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_buﬀercache 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
pg_freesp 
acemap
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
Extensions for PostgreSQL 11 204
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 11.22-
RDS 
.20240509
11.22-
R2
11.22 11.21 11.20 11.19 11.18 11.17 11.16 11.15 11.14 11.13 11.12
pg_hint_plan 1.3.7 1.3.7 1.3.7 1.3.7 1.3.7 1.3.7 1.3.7 1.3.7 1.3.7 1.3.7 1.3.7 1.3.5 1.3.5
pg_prewarm 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_proctab 0.0.100.0.100.0.100.0.9 0.0.9 0.0.9 0.0.9 0.0.9 0.0.9 0.0.9 0.0.9 0.0.9 0.0.9
pg_repack 1.4.4 1.4.4 1.4.4 1.4.4 1.4.4 1.4.4 1.4.4 1.4.4 1.4.4 1.4.4 1.4.4 1.4.4 1.4.4
pg_similarity 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_stat_s 
tatements
1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6 1.6
pg_transport 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_trgm 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
pg_visibility 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pgactive 2.1.1 2.1.1 2.1.1 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pgAudit 1.3.4 1.3.4 1.3.4 1.3.4 1.3.4 1.3.4 1.3.4 1.3.3 1.3.3 1.3.3 1.3.1 1.3.1 1.3.1
pgcrypto 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
pglogical 2.4.3 2.4.3 2.4.3 2.4.2 2.4.2 2.4.1 2.4.1 2.4.1 2.4.1 2.4.0 2.4.0 2.4.0 2.2.2
pgrowlocks 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pgrouting 2.6.3 2.6.3 2.6.3 2.6.3 2.6.3 2.6.3 2.6.3 2.6.3 2.6.3 2.6.3 2.6.3 2.6.3 2.6.1
pgstattuple 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5 1.5
pgTAP 1.3.1 1.3.1 1.3.1 1.2.0 1.2.0 1.2.0 1.2.0 1.1.0 1.1.0 1.1.0 1.1.0 1.1.0 1.1.0
plcoﬀee 3.1.6 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8
Extensions for PostgreSQL 11 205
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 11.22-
RDS 
.20240509
11.22-
R2
11.22 11.21 11.20 11.19 11.18 11.17 11.16 11.15 11.14 11.13 11.12
plls 3.1.6 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8
plperl 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plpgsql 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plproﬁler 4.2.4 4.2.4 4.2.4 4.1 4.1 4.1 4.1 4.1 4.1 4.1 4.1 4.1 4.1
pltcl 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plv8 3.1.6 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8 2.3.8
PostGIS 3.3.3 3.3.3 3.3.3 3.3.2 3.3.2 3.1.7 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 2.5.2
postgis_raster 3.3.3 3.3.3 3.3.3 3.3.2 3.3.2 3.1.7 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 N/
A
postgis_t 
iger_geocoder
3.3.3 3.3.3 3.3.3 3.3.2 3.3.2 3.1.7 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 2.5.1
postgis_t 
opology
3.3.3 3.3.3 3.3.3 3.3.2 3.3.2 3.1.7 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 2.5.1
postgres_fdw 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
preﬁx 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9 1.2.9
rdkit 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8 3.8
rds_tools 1.3 1.3 1.3 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
seg 1.3 1.3 1.3 1.3 1.3 1.3 1.3 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
sslinfo 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
Extensions for PostgreSQL 11 206
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 11.22-
RDS 
.20240509
11.22-
R2
11.22 11.21 11.20 11.19 11.18 11.17 11.16 11.15 11.14 11.13 11.12
tablefunc 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tcn 1.0 1.0 1.0 1.0 1.0 1.0 1.0 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
test_decoding yes yes yes yes yes yes yes yes yes yes yes yes yes
tsm_syste 
m_rows
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tsm_syste 
m_time
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
unaccent 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
uuid-ossp 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
wal2json 2.5 2.5 2.5 2.5 2.5 2.5 2.5 2.3 2.3 2.3 2.3 2.3 2.3
Extensions supported for RDS for PostgreSQL 10
The following tables show PostgreSQL extensions for PostgreSQL version 10 that are currently 
supported by RDS for PostgreSQL. "N/A" indicates that the extension isn't available for that 
PostgreSQL version. For more information on PostgreSQL extensions, see Packaging related 
objects into an extension.
Extension 10.23 10.22 10.21 10.20 10.19 10.18 10.17
address_standardizer 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 2.4.2
address_standardizer_data_us 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 2.4.2
amcheck 1 1 1 1 yes yes yes
auto_explain yes yes yes yes yes yes yes
Extensions for PostgreSQL 10 207
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 10.23 10.22 10.21 10.20 10.19 10.18 10.17
aws_commons 1.2 1.2 1.2 1.1 1.1 1.1 1.1
aws_s3 1.1 1.1 1.1 1.1 1.1 1.1 1.1
bloom 1.0 1.0 1.0 1.0 1.0 1.0 1.0
btree_gin 1.2 1.2 1.2 1.2 1.2 1.2 1.2
btree_gist 1.5 1.5 1.5 1.5 1.5 1.5 1.5
chkpass 1.0 1.0 1.0 1.0 1.0 1.0 1.0
citext 1.4 1.4 1.4 1.4 1.4 1.4 1.4
cube 1.2 1.2 1.2 1.2 1.2 1.2 1.2
dblink 1.2 1.2 1.2 1.2 1.2 1.2 1.2
decoder_raw yes yes yes yes yes yes yes
dict_int 1.0 1.0 1.0 1.0 1.0 1.0 1.0
dict_xsyn 1.0 1.0 1.0 1.0 1.0 1.0 1.0
earthdistance 1.1 1.1 1.1 1.1 1.1 1.1 1.1
fuzzystrmatch 1.1 1.1 1.1 1.1 1.1 1.1 1.1
hll 2.10.2 2.10.2 2.10.2 2.10.2 2.10.2 2.10.2 2.10.2
hstore 1.4 1.4 1.4 1.4 1.4 1.4 1.4
hstore_plperl 1.0 1.0 1.0 1.0 1.0 1.0 1.0
ICU module 60.2 60.2 60.2 60.2 60.2 60.2 60.2
intagg 1.1 1.1 1.1 1.1 1.1 1.1 1.1
intarray 1.2 1.2 1.2 1.2 1.2 1.2 1.2
Extensions for PostgreSQL 10 208
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 10.23 10.22 10.21 10.20 10.19 10.18 10.17
ip4r 2.1.1 2.1.1 2.1.1 2.1.1 2.1.1 2.1.1 2.1.1
isn 1.1 1.1 1.1 1.1 1.1 1.1 1.1
lo 1.1 1.1 1.1 1.1 N/A N/A N/A
log_fdw 1.1 1.1 1.1 1.1 1.0 1.0 1.0
libprotobuf 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0 1.3.0
ltree 1.1 1.1 1.1 1.1 1.1 1.1 1.1
orafce 3.24 3.15 3.15 3.15 3.15 3.15 3.15
pageinspect 1.6 1.6 1.6 1.6 1.6 1.6 1.6
pg_buﬀercache 1.3 1.3 1.3 1.3 1.3 1.3 1.3
pg_freespacemap 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_hint_plan 1.3.6 1.3.6 1.3.6 1.3.6 1.3.6 1.3.5 1.3.5
pg_prewarm 1.1 1.1 1.1 1.1 1.1 1.1 1.1
pg_repack 1.4.3 1.4.3 1.4.3 1.4.3 1.4.3 1.4.3 1.4.3
pg_similarity 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_stat_statements 1.6 1.6 1.6 1.6 1.6 1.6 1.6
pg_transport 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pg_trgm 1.3 1.3 1.3 1.3 1.3 1.3 1.3
pg_visibility 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pgAudit 1.2.4 1.2.3 1.2.3 1.2.3 1.2.1 1.2.1 1.2.1
pgcrypto 1.3 1.3 1.3 1.3 1.3 1.3 1.3
Extensions for PostgreSQL 10 209
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 10.23 10.22 10.21 10.20 10.19 10.18 10.17
pglogical 2.4.1 2.4.1 2.4.1 2.4.0 2.4.0 2.4.0 2.2.2
pgrowlocks 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pgrouting 2.5.5 2.5.5 2.5.5 2.5.5 2.5.5 2.5.5 2.5.2
pgstattuple 1.5 1.5 1.5 1.5 1.5 1.5 1.5
plcoﬀee 2.1.2 2.1.2 2.1.2 2.1.2 2.1.2 2.1.2 2.1.2
plls 2.1.2 2.1.2 2.1.2 2.1.2 2.1.2 2.1.2 2.1.2
plperl 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plpgsql 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plproﬁler 4.1 4.1 4.1 4.1 4.1 4.1 4.1
pltcl 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plv8 2.1.2 2.1.2 2.1.2 2.1.2 2.1.2 2.1.2 2.1.2
PostGIS 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 2.5.2
postgis_raster 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 N/A
postgis_tiger_geocoder 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 2.4.2
postgis_topology 3.1.7 3.1.7 3.1.5 3.1.5 3.1.4 3.1.4 2.4.2
postgres_fdw 1.0 1.0 1.0 1.0 1.0 1.0 1.0
preﬁx 1.2.6 1.2.6 1.2.6 1.2.6 1.2.6 1.2.6 1.2.6
seg 1.1 N/A N/A N/A N/A N/A N/A
sslinfo 1.2 1.2 1.2 1.2 1.2 1.2 1.2
tablefunc 1.0 1.0 1.0 1.0 1.0 1.0 1.0
Extensions for PostgreSQL 10 210
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension 10.23 10.22 10.21 10.20 10.19 10.18 10.17
tcn 1.0 N/A N/A N/A N/A N/A N/A
test_decoding 1 1 1 1 yes yes yes
tsearch2 (deprecated) 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tsm_system_rows 1.1 1.1 1.1 1.1 1.0 1.0 1.0
tsm_system_time 1.1 1.1 1.1 1.1 1.0 1.0 1.0
unaccent 1.1 1.1 1.1 1.1 1.1 1.1 1.1
uuid-ossp 1.1 1.1 1.1 1.1 1.1 1.1 1.1
wal2json 2.5 2.3 2.3 2.3 2.3 2.3 2.3
The tsearch2 extension is deprecated in version 10. The tsearch2 extension was remove from
PostgreSQL version 11.1 on Amazon RDS (Deprecated).
Extensions supported for RDS for PostgreSQL 9.6
The following tables show PostgreSQL extensions for PostgreSQL version 9.6.x that are currently 
supported by RDS for PostgreSQL. "N/A" indicates that the extension isn't available for that 
PostgreSQL version. For more information on PostgreSQL extensions, see Packaging related 
objects into an extension.
Extension9.6.249.6.239.6.229.6.209.6.199.6.189.6.179.6.169.6.159.6.149.6.129.6.119.6.109.6.99.6.89.6.69.6.59.6.39.6.29.6.1
address_s 
tandardiz 
er
2.5.5, 
2.3.7
2.5.5, 
2.3.7
2.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.22.3.22.3.22.3.0
address_s 
tandardiz 
er_data_u 
s
2.5.5, 
2.3.7
2.5.5, 
2.3.7
2.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.22.3.22.3.22.3.0
Extensions for PostgreSQL 9.6 211
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension9.6.249.6.239.6.229.6.209.6.199.6.189.6.179.6.169.6.159.6.149.6.129.6.119.6.109.6.99.6.89.6.69.6.59.6.39.6.29.6.1
auto_expl 
ain
yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes N/
A
N/
A
bloom1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
btree_gin1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
btree_gis 
t
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
chkpass1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
citext1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
cube1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
dblink1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
decoder_r 
aw
yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes N/
A
N/
A
N/
A
dict_int1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
dict_xsyn1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
earthdist 
ance
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
fuzzystrm 
atch
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
hll 2.10.22.10.22.10.22.10.22.10.22.10.22.10.22.10.22.10.22.10.22.10.22.10.22.10.22.10.22.10.22.10.22.10.2N/
A
N/
A
N/
A
hstore1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
hstore_pl 
perl
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
Extensions for PostgreSQL 9.6 212
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension9.6.249.6.239.6.229.6.209.6.199.6.189.6.179.6.169.6.159.6.149.6.129.6.119.6.109.6.99.6.89.6.69.6.59.6.39.6.29.6.1
intagg1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
intarray1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
ip4r 2.1.12.1.12.1.12.1.12.1.12.1.12.1.12.1.12.1.12.1.12.1.12.1.12.1.12.1.12.0 2.0 2.0 2.0 2.0 2.0
isn 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
log_fdw1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 N/
A
ltree1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
orafce3.15 3.15 3.15 3.8 3.8 3.8 3.8 3.6.13.6.13.6.13.6.13.6.13.6.13.6.13.6.13.6.1N/
A
N/
A
N/
A
N/
A
pgAudit1.1.21.1.21.1.21.1.21.1.21.1.11.1.11.1.11.1.11.1.11.1.11.1.11.1.11.1.11.1 1.1 1.1 1.1 N/
A
N/
A
pg_buﬀer 
cache
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pg_freesp 
acemap
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 N/
A
pg_hint_p 
lan
1.2.71.2.61.2.61.2.61.2.61.2.61.2.51.2.51.2.51.2.51.2.31.2.31.2.31.2.21.2.21.1.31.1.31.1.31.1.3N/
A
pg_prewar 
m
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
pg_repack1.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.31.4.21.4.21.4.11.4.0N/
A
N/
A
pg_simila 
rity
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
Extensions for PostgreSQL 9.6 213
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension9.6.249.6.239.6.229.6.209.6.199.6.189.6.179.6.169.6.159.6.149.6.129.6.119.6.109.6.99.6.89.6.69.6.59.6.39.6.29.6.1
pg_stat_s 
tatements
1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
pg_trgm1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
pg_visibi 
lity
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
pgcrypto1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3 1.3
pglogical2.4.02.4.02.2.22.2.22.2.22.2.02.2.02.2.02.2.02.2.02.2.02.2.02.2.0N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
N/
A
pgrowlock 
s
1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
pgrouting2.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.4.22.3.2N/
A
N/
A
N/
A
pgstattup 
le
1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4 1.4
plcoﬀee2.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.21.5.31.5.31.5.31.5.31.5.3
plls 2.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.21.5.31.5.31.5.31.5.31.5.3
plperl1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plpgsql1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
pltcl 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
plv8 2.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.22.1.01.5.31.5.31.5.31.5.31.5.3
PostGIS2.5.5, 
2.3.7
2.5.5, 
2.3.7
2.5.22.5.22.5.22.5.22.5.22.5.22.5.22.3.72.3.72.3.72.3.72.3.72.3.42.3.42.3.22.3.22.3.22.3.0
Extensions for PostgreSQL 9.6 214
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Extension9.6.249.6.239.6.229.6.209.6.199.6.189.6.179.6.169.6.159.6.149.6.129.6.119.6.109.6.99.6.89.6.69.6.59.6.39.6.29.6.1
postgis_t 
iger_geoc 
oder
2.5.5, 
2.3.7
2.5.5, 
2.3.7
2.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.22.3.22.3.22.3.0
postgis_t 
opology
2.5.5, 
2.3.7
2.5.5, 
2.3.7
2.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.42.3.22.3.22.3.22.3.0
postgres_ 
fdw
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
preﬁx1.2.61.2.61.2.61.2.61.2.61.2.61.2.61.2.61.2.61.2.61.2.61.2.61.2.61.2.61.2.61.2.6N/
A
N/
A
N/
A
N/
A
sslinfo1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2 1.2
tablefunc1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
test_deco 
ding
yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes yes
tsearch21.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tsm_syste 
m_rows
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
tsm_syste 
m_time
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
unaccent1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
uuid-
ossp
1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1
wal2jsonversion 
2.3
version 
2.3
version 
2.3
version 
2.3
version 
2.3
version 
2.1
version 
2.1
Commit 
hash 
9e962ba
Commit 
hash 
9e962ba
Commit 
hash 
9e962ba
Commit 
hash 
9e962ba
Commit 
hash 
9e962ba
Commit 
hash 
01c5c1e
Commit 
hash 
5352cc4
Commit 
hash 
5352cc4
Commit 
hash 
645ab69
Commit 
hash 
645ab69
Commit 
hash 
2828409
N/
A
N/
A
Extensions for PostgreSQL 9.6 215
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Document history for the RDS for PostgreSQL release 
notes
The following table describes RDS for PostgreSQL releases.
Change Description Date
Amazon RDS for PostgreSQ 
L versions 18.3, 17.9, 16.13, 
15.17 and 14.22
RDS for PostgreSQL now 
supports versions 18.3, 17.9,
16.13, 15.17, and 14.22.
February 27, 2026
Amazon RDS for PostgreSQ 
L versions 18.2, 17.8, 16.12, 
15.16 and 14.21
RDS for PostgreSQL now 
supports versions 18.2, 17.8,
16.12, 15.16, and 14.21.
February 12, 2026
Amazon RDS for PostgreSQ 
L Extended Support version 
12.22-RDS.20251114 and 
11.22-RDS.20251114
RDS for PostgreSQL now 
supports Amazon RDS 
Extended Support 12.22-RDS 
.20251114 and 11.22-RDS 
.20251114.
January 8, 2026
Amazon RDS for PostgreSQL 
version 13.23-R2 and 14.20-
R2
RDS for PostgreSQL now 
supports versions 13.23-R2 
and 14.20-R2.
January 5, 2026
Amazon RDS for PostgreSQ 
L versions 17.2-R3, 16.6-R3, 
15.10-R3, 14.15-R3, 13.18-
R3, 12.22-R3
Amazon RDS for PostgreSQL 
now supports versions 17.2-
R3, 16.6-R3, 15.10-R3, 14.15-
R3, 13.18-R3, 12.22-R3.
October 30, 2025
Amazon RDS for PostgreSQ 
L versions 17.4-R2, 16.8-R2, 
15.12-R2, 14.17-R2, 13.20-R2
Amazon RDS for PostgreSQL 
now supports versions 17.4-
R2, 16.8-R2, 15.12-R2, 14.17-
R2, 13.20-R2.
October 15, 2025
216
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Amazon RDS for PostgreSQ 
L versions 17.5-R2, 16.9-R2, 
15.13-R2, 14.18-R2, 13.21-R2
Amazon RDS for PostgreSQL 
now supports versions 17.5-
R2, 16.9-R2, 15.13-R2, 14.18-
R2, 13.21-R2.
October 2, 2025
Amazon RDS for PostgreSQ 
L Extended Support version 
12.22-RDS.20250814 and 
11.22-RDS.20250814
RDS for PostgreSQL now 
supports Amazon RDS 
Extended Support 12.22-RDS 
.20250814 and 11.22-RDS 
.20250814.
September 29, 2025
Amazon RDS for PostgreSQL 
versions 17.6-R2, 16.10-R2, 
15.14-R2, 14.19-R2, 13.22-R2
Amazon RDS for PostgreSQ 
L now supports versions 
17.6-R2, 16.10-R2, 15.14-R2, 
14.19-R2, 13.22-R2.
September 25, 2025
Amazon RDS for PostgreSQL 
version 18.0 in Preview
Amazon RDS for PostgreSQL 
now supports version 18.0 in 
Preview.
September 22, 2025
Amazon RDS for PostgreSQL 
version 18 RC1 in Preview
Amazon RDS for PostgreSQ 
L supports version 18 RC1 in 
Preview.
September 4, 2025
Amazon RDS for PostgreSQ 
L versions 17.6, 16.10, 15.14, 
14.19, and 13.22
RDS for PostgreSQL now 
supports versions 17.6, 16.10,
15.14, 14.19, and 13.22.
August 14, 2025
Amazon RDS for PostgreSQL 
version 18 Beta 3 in Preview
Amazon RDS for PostgreSQL 
supports version 18 Beta 3 in 
Preview.
August 14, 2025
Amazon RDS for PostgreSQ 
L versions 17.5, 16.9, 15.13, 
14.18, and 13.21
RDS for PostgreSQL now 
supports versions 17.5, 16.9,
15.13, 14.18, and 13.21.
May 8, 2025
217
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Amazon RDS for PostgreSQ 
L versions 16.4-R3, 15.8-
R3, 14.13-R3, 13.16-R3, and 
12.20-R3
Amazon RDS for PostgreSQL 
now supports versions 16.4-
R3, 15.8-R3, 14.13-R3, 13.16-
R3, and 12.20-R3.
April 23, 2025
Amazon RDS for PostgreSQ 
L versions 16.3-R4, 15.7-
R4, 14.12-R4, 13.15-R4, and 
12.19-R4
Amazon RDS for PostgreSQL 
now supports versions 16.3-
R4, 15.7-R4, 14.12-R4, 13.15-
R4, and 12.19-R4.
April 8, 2025
Amazon RDS for PostgreSQ 
L versions 17.3, 16.7, 15.11, 
14.16, and 13.19
RDS for PostgreSQL now 
supports versions 17.3, 16.7,
15.11, 14.16, and 13.19.
February 13, 2025
Amazon RDS for PostgreSQ 
L Extended Support version 
11.22-RDS.20241121
RDS for PostgreSQL now 
supports Extended Support 
version 11.22-RDS.20241121.
December 12, 2024
Amazon RDS for PostgreSQ 
L versions 17.2, 16.6, 15.10, 
14.15, 13.18, and 12.22
RDS for PostgreSQL now 
supports versions 17.2, 16.6, 
15.10, 14.15, 13.18, and 
12.22.
November 21, 2024
Amazon RDS for PostgreSQ 
L versions 17.1, 16.5, 15.9, 
14.14, 13.17, and 12.21
RDS for PostgreSQL now 
supports versions 17.1, 16.5, 
15.9, 14.14, 13.17, and 12.21.
November 14, 2024
Amazon RDS for PostgreSQ 
L versions 16.4-R2, 16.3-
R3, 15.8-R2, 15.7-R3, 14.13-
R2, 14.12-R3, 14.11-R4, 
13.16-R2, 13.15-R3, 13.14-
R4, 12.20-R2, 12.19-R3, and 
12.18-R4
Amazon RDS for PostgreSQ 
L now supports versions 
16.4-R2, 16.3-R3, 15.8-R2, 
15.7-R3, 14.13-R2, 14.12-R3, 
14.11-R4, 13.16-R2, 13.15-
R3, 13.14-R4, 12.20-R2, 
12.19-R3, and 12.18-R4.
November 11, 2024
Amazon RDS for PostgreSQL 
version 17.0 in Preview
Amazon RDS for PostgreSQL 
now supports version 17.0 in 
Preview.
September 26, 2024
218
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Amazon RDS for PostgreSQL 
version 17 RC1 in Preview
Amazon RDS for PostgreSQL 
now supports version 17 RC1 
in Preview.
September 6, 2024
Amazon RDS Extended 
Support version 11.22-RDS 
.20240808
Amazon RDS Extended 
Support released version 
11.22-RDS.20240808.
August 26, 2024
Amazon RDS for PostgreSQ 
L versions 16.4, 15.8, 14.13, 
13.16, and 12.20
RDS for PostgreSQL now 
supports versions 16.4, 15.8, 
14.13, 13.16, and 12.20.
August 8, 2024
Amazon RDS for PostgreSQL 
version 17 Beta 3 in Preview
Amazon RDS for PostgreSQL 
now supports version 17 Beta 
3 in Preview.
August 8, 2024
Amazon RDS for PostgreSQ 
L versions 16.2-R3, 15.6-
R3, 14.11-R3, 13.14-R3, and 
12.18-R3
RDS for PostgreSQL now 
supports versions 16.2-R3, 
15.6-R3, 14.11-R3, 13.14-R3, 
and 12.18-R3.
July 1, 2024
Amazon RDS for PostgreSQL 
version 17 Beta 2 in Preview
Amazon RDS for PostgreSQL 
supports version 17 Beta 2 in 
Preview.
June 27, 2024
Amazon RDS for PostgreSQ 
L versions 16.3-R2, 15.7-
R2, 14.12-R2, 13.15-R2, and 
12.19-R2
RDS for PostgreSQL now 
supports versions 16.3-R2, 
15.7-R2, 14.12-R2, 13.15-R2, 
and 12.19-R2.
June 20, 2024
Amazon RDS Extended 
Support version 11.22-RDS 
.20240509
Amazon RDS Extended 
Support released version 
11.22-RDS.20240509.
June 10, 2024
Amazon RDS for PostgreSQL 
version 17 Beta 1 in Preview
Amazon RDS for PostgreSQL 
supports version 17 Beta 1 in 
Preview.
May 24, 2024
219
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Amazon RDS Extended 
Support version 11.22-RDS 
.20240418
Amazon RDS Extended 
Support released version 
11.22-RDS.20240418.
May 14, 2024
Amazon RDS for PostgreSQ 
L versions 16.3, 15.7, 14.12, 
13.15, and 12.19
RDS for PostgreSQL now 
supports versions 16.3, 15.7, 
14.12, 13.15, and 12.19.
May 9, 2024
Amazon RDS for PostgreSQ 
L versions 16.2-R2, 15.6-
R2, 14.11-R2, 13.14-R2, and 
12.18-R2
RDS for PostgreSQL now 
supports versions 16.2-R2, 
15.6-R2, 14.11-R2, 13.14-R2, 
and 12.18-R2.
April 18, 2024
Amazon RDS for PostgreSQ 
L versions 16.2, 15.6, 14.11, 
13.14, and 12.18
RDS for PostgreSQL now 
supports versions 16.2, 15.6, 
14.11, 13.14, and 12.18.
February 22, 2024
Amazon RDS for PostgreSQ 
L versions 16.1-R2, 15.5-R2, 
14.10-R2, 13.13-R2, 12.17-
R2, and 11.22-R2
RDS for PostgreSQL now 
supports versions 16.1-R2, 
15.5-R2, 14.10-R2, 13.13-R2, 
12.17-R2, and 11.22-R2.
January 24, 2024
Amazon RDS for PostgreSQ 
L versions 15.5, 14.10, 13.13, 
12.17, and 11.22
RDS for PostgreSQL now 
supports versions 15.5, 14.10, 
13.13, 12.17, and 11.22.
November 17, 2023
Amazon RDS for PostgreSQL 
version 16.1
RDS for PostgreSQL now 
supports version 16.1.
November 17, 2023
Amazon RDS for PostgreSQL 
version 15.4-R3
RDS for PostgreSQL now 
supports version 15.4-R3.
October 25, 2023
Amazon RDS for PostgreSQ 
L versions 15.4-R2, 14.9-R2, 
13.12-R2, and 12.16-R2
RDS for PostgreSQL now 
supports versions 15.4-R2, 
14.9-R2, 13.12-R2, and 12.16-
R2.
October 5, 2023
220
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Amazon RDS for PostgreSQL 
version 16.0 Preview
RDS for PostgreSQL now 
supports version 16.0 
Preview.
September 15, 2023
Amazon RDS for PostgreSQL 
version 16 RC1
RDS for PostgreSQL now 
supports version 16 RC1.
August 31, 2023
Amazon RDS for PostgreSQ 
L versions 15.4, 14.9, 13.12, 
12.16, and 11.21
RDS for PostgreSQL now 
supports versions 15.4, 14.9, 
13.12, 12.16, and 11.21.
August 24, 2023
Amazon RDS for PostgreSQL 
version 16 Beta 3
RDS for PostgreSQL now 
supports PostgreSQL version 
16 Beta 3.
August 11, 2023
Amazon RDS for PostgreSQ 
L versions 15.3-R2, 14.8-R2, 
and 13.11-R2
RDS for PostgreSQL now 
supports PostgreSQL versions 
15.3-R2, 14.8-R2, and 13.11-
R2.
July 6, 2023
Amazon RDS for PostgreSQL 
version 16 Beta 2
RDS for PostgreSQL now 
supports PostgreSQL version 
16 Beta 2.
July 6, 2023
Amazon RDS for PostgreSQL 
version 16 Beta 1
RDS for PostgreSQL now 
supports PostgreSQL version 
16 Beta 1.
May 26, 2023
Amazon RDS for PostgreSQ 
L versions 15.3, 14.8, 13.11, 
12.15 and 11.20
RDS for PostgreSQL now 
supports versions 15.3, 14.8, 
13.11, 12.15 and 11.20.
May 25, 2023
Amazon RDS for PostgreSQ 
L version 15.2-R2 adds 
extension plrust
RDS for PostgreSQL version 
15.2-R2 adds extension 
plrust.
May 22, 2023
Amazon RDS for PostgreSQL 
version 15.2-R2
RDS for PostgreSQL now 
supports version 15.2-R2.
May 3, 2023
221
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Amazon RDS for PostgreSQ 
L versions 14.7, 13.10, 12.14 
and 11.19
RDS for PostgreSQL now 
supports versions 14.7, 13.10, 
12.14 and 11.19.
March 7, 2023
Amazon RDS for PostgreSQL 
version 15.2
RDS for PostgreSQL now 
supports version 15.2.
February 28, 2023
Amazon RDS for PostgreSQ 
L versions 14.6, 13.9, 12.13, 
11.18, and 10.23
RDS for PostgreSQL now 
supports versions 14.6, 13.9, 
12.13, 11.18, and 10.23.
January 31, 2023
Amazon RDS for PostgreSQ 
L versions 14.5, 13.8, 12.12, 
11.17, and 10.22
RDS for PostgreSQL now 
supports versions 14.5, 13.8, 
12.12, 11.17 and 10.22.
November 18, 2022
Amazon RDS for PostgreSQL 
version 14.4
RDS for PostgreSQL now 
supports version 14.4.
August 31, 2022
Amazon RDS for PostgreSQ 
L versions 14.3, 13.7, 12.11, 
11.16, and 10.21
RDS for PostgreSQL now 
supports versions 14.3, 13.7, 
12.11, 11.16 and 10.21.
August 3, 2022
Initial release Initial release of the RDS for 
PostgreSQL Release Notes.
March 22, 2022
Earlier updates
The following table describes the important changes in each release of the Amazon RDS for 
PostgreSQL Release Notes before March 22, 2022.
Change Description Date changed
Amazon RDS 
for PostgreSQ 
L versions 14.2, 
13.6, 12.10, 
11.15, and 10.20
RDS for PostgreSQL now supports versions 14.2, 
13.6, 12.10, 11.15, and 10.20. Version 14.2 and 13.6 
add support for two new foreign data wrappers. The
mysql_fdw  extension lets PostgreSQL work with 
data stored in MySQL, MariaDB, and Aurora MySQL 
databases. The tds_fdw extension lets PostgreSQL 
March 12, 2022
Earlier updates 222
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Change Description Date changed
work with data stored in SQL Server databases. For 
more information, see Working with the supported 
foreign data wrappers for Amazon RDS for PostgreSQ 
L.
Amazon RDS 
for PostgreSQL 
supports version 
14.1
Amazon RDS for PostgreSQL now supports 
PostgreSQL version 14.1.
January 28, 2022
Amazon RDS 
for PostgreSQ 
L versions 13.5, 
12.9, 11.14, 10.19 
and 9.6.24
RDS for PostgreSQL now supports versions 13.5, 
12.9, 11.14, 10.19 and 9.6.24.
January 24, 2022
Amazon RDS 
for PostgreSQ 
L versions 13.4, 
12.8, 11.13, 10.18 
and 9.6.23
RDS for PostgreSQL now supports versions 13.4, 
12.8, 11.13, 10.18 and 9.6.23.
September 30, 
2021
Amazon RDS 
for PostgreSQ 
L versions 13.3, 
12.7, 11.12, 
10.17, and 9.6.22
RDS for PostgreSQL now supports versions 13.3, 
12.7, 11.12, 10.17 and 9.6.22.
July 7, 2021
Amazon RDS 
for PostgreSQ 
L versions 13.2, 
12.6, 11.11, 
10.16, 9.6.21, and 
9.5.25
Amazon RDS for PostgreSQL now supports versions 
13.2, 12.6, 11.11, 10.16, 9.6.21 and 9.5.25.
April 13, 2021
Earlier updates 223
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Change Description Date changed
Amazon RDS 
for PostgreSQL 
version 13.1
Amazon RDS for PostgreSQL now supports version 
13.1.
February 24, 2021
Amazon RDS 
for PostgreSQ 
L versions 12.5, 
11.10, 10.15, 
9.6.20, and 9.5.24
Amazon RDS for PostgreSQL now supports versions 
12.5, 11.10, 10.15, 9.6.20 and 9.5.24.
January 12, 2021
Amazon RDS 
for PostgreSQL 
12.4, 11.9, 10.14, 
9.6.19, and 9.5.23
Amazon RDS for PostgreSQL supports versions 12.4, 
11.9, 10.14, 9.6.19 and 9.5.23.
September 24, 
2020
Amazon RDS 
for PostgreSQ 
L supports 
PostgreSQL 12.3
Amazon RDS for PostgreSQL supports version 12.3. June 17, 2020
Amazon RDS 
for PostgreSQ 
L versions 11.7, 
10.12, 9.6.17, and 
9.5.21
Amazon RDS for PostgreSQL supports versions 11.7, 
10.12, 9.6.17 and 9.5.21.
April 28, 2020
Amazon RDS 
for PostgreSQ 
L supports 
PostgreSQL 12.2
Amazon RDS for PostgreSQL supports version 12.2. March, 31, 2020
Amazon RDS 
for PostgreSQ 
L supports new 
versions
Amazon RDS for PostgreSQL supports versions 11.6, 
10.11, 9.6.16, 9.5.20 and 9.4.25.
February 11, 2020
Earlier updates 224
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Change Description Date changed
Amazon RDS 
for PostgreSQ 
L versions 11.5, 
10.10, 9.6.15, 
9.5.19, and 9.4.24
Amazon RDS for PostgreSQL supports versions 11.5, 
10.10, 9.6.15, 9.5.19 and 9.4.24.
October 8, 2019
Amazon RDS 
for PostgreSQ 
L versions 11.4, 
10.9, 9.6.14, 
9.5.18, and 9.4.23
Amazon RDS for PostgreSQL supports minor versions 
11.4, 10.9, 9.6.14, 9.5.18 and 9.4.23.
July 3, 2019
Amazon RDS 
for PostgreSQ 
L versions 11.2, 
10.7, 9.6.12, 
9.5.16, and 9.4.21
Amazon RDS for PostgreSQL supports minor versions 
11.2, 10.7, 9.6.12, 9.5.16 and 9.4.21.
May 1, 2019
Amazon RDS 
for PostgreSQ 
L supports new 
minor versions
Amazon RDS for PostgreSQL now supports the 
following new minor versions: 10.6, 9.6.11, 9.5.15, 
9.4.20 and 9.3.25.
December 19, 
2018
Amazon RDS 
for PostgreSQ 
L supports new 
minor versions
Amazon RDS for PostgreSQL now supports the 
following new minor versions: 10.5, 9.6.10, 9.5.14, 
9.4.19 and 9.3.24.
October 4, 2018
Amazon RDS 
for PostgreSQ 
L supports new 
minor versions
Amazon RDS for PostgreSQL now supports the 
following new minor versions: 10.4, 9.6.9, 9.5.13, 
9.4.18 and 9.3.23.
July 25, 2018
Support for 
PostgreSQL 10.1
Amazon RDS now supports version 10.1 of PostgreSQ 
L.
February 27, 2018
Earlier updates 225
Amazon Relational Database Service Amazon RDS for PostgreSQL Release Notes
Change Description Date changed
Support for 
PostgreSQL 9.6.6
Amazon RDS PostgreSQL now supports version 9.6.6. January 19, 2018
PostgreSQL 9.6.5, 
9.5.9, 9.4.14, and 
9.3.19
You can now create Amazon RDS DB instances 
running PostgreSQL versions 9.6.5, 9.5.9, 9.4.14 and 
9.3.19.
November 1, 
2017
New Feature Amazon RDS now supports PostgreSQL versions 
9.6.2, 9.5.6, 9.4.11 and 9.3.16.
May 3, 2017
New feature Amazon RDS now supports PostgreSQL version 9.6.1. November 11, 
2016
New features Added support for new PostgreSQL versions 9.5.4, 
9.4.9, and 9.3.14. Also added support for PostgreSQ 
L logical replication, PostgreSQL event triggers, and 
RAM disk for the PostgreSQL stats_temp_directory.
September 14, 
2016
New feature Added support for PostgreSQL versions 9.5.2, 9.4.7 
and 9.3.12.
April 8, 2016
New feature Updated to support three new extensions for 
PostgreSQL versions 9.3.10 and 9.4.5 DB instances.
December 1, 2015
New feature Updated to support PostgreSQL versions 9.3.10 and 
9.4.5 DB instances.
November 27, 
2015
New feature Updated to support PostgreSQL versions 9.4.4 and 
9.3.9.
July 30, 2015
New feature Updated to support PostgreSQL versions 9.3.6 and 
9.4.1.
March 18, 2015
Earlier updates 226
