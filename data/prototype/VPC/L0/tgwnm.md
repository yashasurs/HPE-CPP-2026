# AWS Global Networks for Transit Gateways User Guide

## What is AWS Global Networks for Transit Gateways?

## Global networks concepts

## Home Region

AWS Global Networks for Transit Gateways User Guide
AWS Network Manager
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
## PrivateLink support

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
AWS Network Manager: AWS Global Networks for Transit Gateways 
User Guide
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
Amazon's trademarks and trade dress may not be used in connection with any product or service 
that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any 
manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are 
the property of their respective owners, who may or may not be aﬃliated with, connected to, or 
sponsored by Amazon.
## IPv6 support

## Region availability

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Table of Contents
What is AWS Global Networks for Transit Gateways? ................................................................... 1
Global networks concepts .......................................................................................................................... 1
Home Region ............................................................................................................................................ 1
PrivateLink support ...................................................................................................................................... 2
IPv6 support .................................................................................................................................................. 3
Region availability ........................................................................................................................................ 3
How to get started with global networks for transit gateways .......................................................... 5
Pricing ............................................................................................................................................................. 5
How global networks work ............................................................................................................. 6
Register transit gateways ........................................................................................................................... 6
Multi-Region and multi-account network .......................................................................................... 7
Deﬁne and associate your on-premises network ................................................................................... 8
Supported resource types ........................................................................................................................... 9
Get started ..................................................................................................................................... 11
Prerequisites ................................................................................................................................................ 11
Step 1: Create a global network ............................................................................................................. 11
Step 2: Register your transit gateway ................................................................................................... 12
Step 3: (Optional) Deﬁne and associate your on-premises network resources .............................. 12
Step 4: (Optional) Enable multi-account access .................................................................................. 13
Step 5: View and monitor your global network .................................................................................. 14
Scenarios ........................................................................................................................................ 15
AWS-only multi-Region and multi-account global network ............................................................. 15
Single device with a single VPN connection ........................................................................................ 16
Device with multiple VPN connections ................................................................................................. 17
Multi-device and multi-link site .............................................................................................................. 19
SD-WAN connecting to AWS ................................................................................................................... 20
Connection between devices ................................................................................................................... 21
Modify a global network .............................................................................................................. 23
Multi-account .............................................................................................................................................. 24
Prerequisites ........................................................................................................................................... 24
Manage multiple accounts .................................................................................................................. 25
Enable trusted access ........................................................................................................................... 29
Disabled trusted access ....................................................................................................................... 30
Register a delegated administrator .................................................................................................. 31
iii
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Deregister a delegated administrator ............................................................................................... 32
Manage IAM role deployments .......................................................................................................... 32
Troubleshoot self-managed roles ...................................................................................................... 33
Global networks ......................................................................................................................................... 35
Create a global network ...................................................................................................................... 36
View a global network ......................................................................................................................... 37
Update a global network .................................................................................................................... 37
Delete a global network ...................................................................................................................... 38
Transit gateway registrations .................................................................................................................. 38
Transit gateway limitations ................................................................................................................ 38
Register a transit gateway .................................................................................................................. 39
View registered transit gateways ...................................................................................................... 40
Deregister a transit gateway .............................................................................................................. 40
Sites and links ............................................................................................................................................. 41
Sites ......................................................................................................................................................... 41
Links ......................................................................................................................................................... 41
Create a site ........................................................................................................................................... 41
View site details .................................................................................................................................... 42
Update a site ......................................................................................................................................... 43
Delete a site ........................................................................................................................................... 44
Add a link ............................................................................................................................................... 44
Edit a link ............................................................................................................................................... 45
Delete a link ........................................................................................................................................... 45
Devices .......................................................................................................................................................... 46
Add a device .......................................................................................................................................... 47
Delete a device ...................................................................................................................................... 48
Edit a device ........................................................................................................................................... 48
View device details ............................................................................................................................... 49
Connections ................................................................................................................................................. 55
Create a connection ............................................................................................................................. 55
Update a connection ............................................................................................................................ 56
Delete a connection ............................................................................................................................. 57
Gateway associations ................................................................................................................................. 57
Customer gateway associations ......................................................................................................... 57
Transit Gateway Connect peer associations .................................................................................... 58
Associate a customer gateway with a device .................................................................................. 58
iv
## How to get started with global networks for transit gateways

## Pricing

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Disassociate a customer gateway association from a device ....................................................... 59
Add a Connect peer association ........................................................................................................ 60
Disassociate a Connect peer from a device ..................................................................................... 62
Resource tags .............................................................................................................................................. 63
Supported resources ............................................................................................................................ 63
Tagging restrictions .............................................................................................................................. 63
Transit gateway network and transit gateway dashboards ........................................................ 65
Access transit gateway network dashboards ........................................................................................ 65
Overview ................................................................................................................................................. 66
Geography .............................................................................................................................................. 68
Topology tree ......................................................................................................................................... 72
Events ...................................................................................................................................................... 75
Monitoring .............................................................................................................................................. 76
Route analyzer ....................................................................................................................................... 77
Access transit gateway dashboards ........................................................................................................ 79
Overview ................................................................................................................................................. 79
Topology tree ......................................................................................................................................... 81
Events ...................................................................................................................................................... 83
Monitoring .............................................................................................................................................. 76
On-premises associations .................................................................................................................... 86
Connect peer associations .................................................................................................................. 86
Route Analyzer ............................................................................................................................... 88
Route Analyzer basics ............................................................................................................................... 88
Perform a route analysis .......................................................................................................................... 89
Example: Route analysis for peered transit gateways ........................................................................ 90
Example: Route analysis with a middlebox conﬁguration ................................................................. 91
Metrics and events ........................................................................................................................ 94
Monitor with CloudWatch metrics .......................................................................................................... 94
View CloudWatch metrics for on-premises resources ................................................................... 95
View global network CloudWatch metrics ...................................................................................... 96
Monitor with EventBridge ........................................................................................................................ 97
Get started ............................................................................................................................................. 98
Topology change events ................................................................................................................... 100
Routing update events ...................................................................................................................... 113
Status update events ......................................................................................................................... 116
Log API calls using CloudTrail ............................................................................................................... 120
v
## How global networks work

## Register transit gateways

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Global network information in CloudTrail .................................................................................... 121
Identity and access management ............................................................................................... 122
How Network Manager works with IAM ............................................................................................. 123
Actions .................................................................................................................................................. 123
Resources .............................................................................................................................................. 123
Condition keys ..................................................................................................................................... 123
Example policies ....................................................................................................................................... 124
Service-linked role ................................................................................................................................... 130
Permissions granted by the service-linked role ........................................................................... 130
Create the service-linked role .......................................................................................................... 130
Edit the service-linked role .............................................................................................................. 131
Delete the service-linked role .......................................................................................................... 131
Supported Regions ............................................................................................................................. 131
AWS managed policies ........................................................................................................................... 131
NetworkAdministrator ....................................................................................................................... 132
AWSNetworkManagerReadOnlyAccess ........................................................................................... 132
AWSNetworkManagerServiceRolePolicy ........................................................................................ 132
Policy updates ..................................................................................................................................... 133
Multi-account access roles ..................................................................................................................... 135
CloudWatch-CrossAccountSharingRole .......................................................................................... 135
IAMRoleForAWSNetworkManagerCrossAccountResourceAccess ............................................... 136
Permission templates ........................................................................................................................ 137
Quotas .......................................................................................................................................... 146
General quotas ......................................................................................................................................... 146
Document history ........................................................................................................................ 147
vi
## Multi-Region and multi-account network

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
What is AWS Global Networks for Transit Gateways?
AWS Global Networks for Transit Gateways enables you to create one or more global networks 
and then centrally manage those global networks across AWS accounts, Regions, and on-premises 
locations.
Note
If you want to create a core network within one of your global networks you'll use AWS 
Cloud WAN to create, manage, and monitor that core network. For more information on 
creating a global network with a core network, see the AWS Cloud WAN User Guide.
Global networks concepts
The following are the key concepts when using global networks to manage transit gateways.
• Global network — A single, private network that acts as the high-level container for your 
network objects. A global network can contain both AWS Transit Gateways and, if you're using 
AWS Cloud WAN, other Cloud WAN core networks. You can see these through the AWS Network 
Manager console.
• Device — Represents a physical or a virtual appliance in an on-premises network, data center, 
AWS Cloud, or other cloud providers.
• Connection — Represents connectivity between two devices. The connection can be between 
a physical or virtual appliance and a third-party virtual appliance inside a VPC, or it can be 
between physical appliances in an on-premises network.
• Link — Represents a single internet connection from a site.
• Site — Represents a physical on-premises location. It could be a branch, oﬃce, store, campus, or 
a data center.
Home Region
The home Region is the AWS Region where data related to your use of your AWS Global Networks 
for Transit Gateways global network is aggregated and stored. Global networks aggregates and 
stores this information in the home Region to provide you with a central dashboard with visualized 
Global networks concepts 1
## Deﬁne and associate your on-premises network

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
insights into your global network. Currently, global networks only supports US West (Oregon) as 
the home Region.
Important
• Global networks aggregates and stores regional usage data associated with the transit 
gateways speciﬁed from the AWS Regions you're using to the US West (Oregon) Region.
• Global networks aggregates and stores regional usage data associated with the transit 
gateways from the AWS GovCloud (US) Regions to the AWS GovCloud (US-West) Region.
• Once established, you can't change the home Region.
We aggregate and store this regional usage data from the AWS Regions you are using to US West 
(Oregon) using Amazon Simple Queue Service (SQS) and Amazon Simple Storage Service (S3). This 
data includes but is not limited to:
• Topology data for registered transit gateways
• Event data for transit gateways and VPNs
• Transit gateway IDs for registering transit gateways into a global network
• (Optional) Location data related to your device and site registrations
• (Optional) Provider and link data related to your link registrations
• (Optional) IP address and CIDR ranges used in transit gateway Connect peers
All movement and data aggregation occurs over a secure and encrypted channel and stored with 
encryption at rest.
AWS Global Networks for Transit Gateways uses Amazon Location Service to create maps of your 
global network. For more information about Amazon Location Service, see Amazon Location 
Service.
AWS PrivateLink support
Network Manager supports AWS PrivateLink to create private connectivity between Network 
Manager and your VPCs. Using PrivateLink, you can establish secure and private connectivity 
without the need for using an internet gateway or any NAT devices to communicate with your 
VPCs.
PrivateLink support 2
## Supported resource types

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
While there is no price charge for using Network Manager, there is a price charge for using 
PrivateLink. See for more information.
Note
• PrivateLink only supports IPv6 dual-stack endpoints.
• Support for PrivateLink through Network Manager is currently available only in the us-
west-2 and us-gov-west-1 Regions.
For more information on PrivateLink, see the AWS PrivateLink Guide.
IPv6 support
Network Manager supports Internet Protocol version 6 (IPv6) on dual-stack endpoints. 
Backwards compatibility is supported for IPv4 endpoints. For example, networkmanager.us-
west-2.api.aws.
Region availability
AWS Global Networks for Transit Gateways is available in the following AWS Regions:
AWS Region Description
af-south-1 Africa (Cape Town)
ap-east-1 Asia Paciﬁc (Hong Kong)
ap-northeast-1 Asia Paciﬁc (Tokyo)
ap-northeast-2 Asia Paciﬁc (Seoul)
ap-northeast-3 Asia Paciﬁc (Osaka)
ap-south-1 Asia Paciﬁc (Mumbai)
ap-south-2 Asia Paciﬁc (Hyderabad)
ap-southeast-1 Asia Paciﬁc (Singapore)
IPv6 support 3
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
AWS Region Description
ap-southeast-2 Asia Paciﬁc (Sydney)
ap-southeast-3 Asia Paciﬁc (Jakarta)
ap-southeast-4 Asia Paciﬁc (Melbourne)
ap-southeast-5 Asia Paciﬁc (Malaysia)
ca-central-1 Canada (Central)
ca-west-1 Canada West (Calgary)
eu-central-1 Europe (Frankfurt)
eu-central-2 Europe (Zurich)
eu-north-1 Europe (Stockholm)
eu-south-1 Europe (Milan)
eu-south-2 Europe (Spain)
eu-west-1 Europe (Ireland)
eu-west-2 Europe (London)
eu-west-3 Europe (Paris)
il-central-1 Israel (Tel Aviv)
me-central-1 Middle East (UAE)
me-south-1 Middle East (Bahrain)
sa-east-1 South America (São Paulo)
us-east-1 US East (N. Virginia)
us-east-2 US East (Ohio)
Region availability 4
## Get started

## Prerequisites

## Step 1: Create a global network

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
AWS Region Description
us-west-1 US West (N. California)
us-west-2 US West (Oregon)
us-gov-east-1 AWS GovCloud (US-East)
us-gov-west-1 AWS GovCloud (US-West)
How to get started with global networks for transit gateways
Use the following resources to help you use global networks:
• How AWS Global Networks for Transit Gateways works
• Get started
• the section called “Access transit gateway network dashboards”
Pricing
There are no additional fees for using global networks to manage transit gateways networks. You 
are charged the standard fees for the network resources that you manage in your global network 
(such as transit gateways). For more information about pricing, see AWS Transit Gateway pricing.
How to get started with global networks for transit gateways 5
## Step 2: Register your transit gateway

## Step 3: (Optional) Deﬁne and associate your on-premises network resources

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
How AWS Global Networks for Transit Gateways works
To use global networks for transit gateways, you ﬁrst create a global network to represent your 
network. Initially, the global network is empty. You then register your existing transit gateways and 
deﬁne your on-premises resources in the global network. This enables you to visualize and monitor 
your AWS resources and your on-premises networks through the global networks dashboard on the 
AWS Network Manager console.
After you create your global network, you can monitor your networks through this dashboard. You 
can view network activity and health using Amazon CloudWatch metrics and Amazon CloudWatch 
Events. The global networks dashboard can help you identify whether issues in your network are 
caused by AWS resources, your on-premises resources, or the connections between them.
global networks does not create, modify, or delete your transit gateways and their attachments. To 
work with transit gateways, use the Amazon VPC console and the Amazon EC2 APIs.
Contents
• Register transit gateways
• Deﬁne and associate your on-premises network
• Supported resource types
Register transit gateways
You can register transit gateways that are in the same AWS account as your global network. 
When you register a transit gateway, the following transit gateway attachments are automatically 
included in your global network:
• VPCs
• Site-to-Site VPN connections
• Direct Connect gateways
• Transit Gateway Connect
• Transit gateway peering connections
Register transit gateways 6
## Step 4: (Optional) Enable multi-account access

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
When you register a transit gateway that has a peering attachment, you can view the peer transit 
gateway in your global network, but you cannot view its attachments. If you own the peer transit 
gateway, you can register it in your global network to view its attachments.
If you delete a transit gateway, it's automatically deregistered from your global network.
Multi-Region and multi-account network
You can create a global network that includes transit gateways in multiple AWS Regions and 
accounts. This enables you to monitor the global health of your AWS network. In the following 
diagram, the global network includes a transit gateway in the us-east-2 Region from Account 
A and a transit gateway in the us-west-2 Region from Account B. Each transit gateway has VPC 
and VPN attachments. You can use the Network Manager console to view and monitor both of the 
transit gateways and their attachments.
Multi-Region and multi-account network 7
## Step 5: View and monitor your global network

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Deﬁne and associate your on-premises network
To represent your on-premises network, you add devices, links, and sites to your global network. A 
site represents the physical location of your branch, oﬃce, store, campus, or data center. When you 
add a site, you can specify the location information, including the physical address and coordinates.
A device represents the physical or virtual appliance that establishes connectivity with a transit 
gateway over an IPsec tunnel. A link represents a single outbound internet connection used by a 
device, for example, a 20-Mbps broadband link.
When you create a device, you can specify its physical location, and the site where it's located. A 
device can have a more speciﬁc location than the site, for example, a building in a campus or a 
ﬂoor in a building. When you create a link, you create it for a speciﬁc site. You can then associate a 
device with a link.
To connect your on-premises network to your AWS resources, associate a customer gateway that's 
in your global network with the device. If you've created a device to represent a virtual appliance 
sitting inside your VPC, and you've established a Connect peer from your virtual appliance to your 
AWS Transit Gateway, associate a Connect peer with the device to connect your virtual appliance 
network to your AWS resources. In the following diagram, the on-premises network is connected to 
a transit gateway through a Site-to-Site VPN connection.
Deﬁne and associate your on-premises network 8
## Scenarios

## AWS-only multi-Region and multi-account global network

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
You can have multiple devices in a site, which you can associate a device with multiple links. For 
examples, see AWS Global Networks for Transit Gateways scenarios.
You can work with one of our Partners in the AWS Partner Network (APN) to provision and connect 
your on-premises networks. For more information, see AWS Network Manager.
Supported resource types
After you register a transit gateway, you can view and monitor the resources in your global 
network.
Amazon VPC resources
Resource Related resources
Transit gateway • Transit gateway attachment
• Transit gateway route table
Transit gateway attachment • Direct Connect gateway
• Transit gateway
• Transit gateway attachment
• Transit Gateway Connect peer
• VPC
• VPN connection
Transit gateway route table • Transit gateway
Transit Gateway Connect peer • Device
• Transit gateway attachment
Site-to-Site VPN resources
Resource Related resources
Customer gateway • Device
• VPN connection
VPN connection • Customer gateway
Supported resource types 9
## Single device with a single VPN connection

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• Transit gateway attachment
Direct Connect resources
Resource Related resources
Direct Connect connection • Virtual interface
Direct Connect gateway • Transit gateway attachment
• Virtual interface
Virtual interface • Direct Connect connection
• Direct Connect gateway
AWS Network Manager resources
Resource Related resources
Connection • Device
Device • Connection
• Customer gateway
• Link
• Site
• Transit Gateway Connect peer
Link • Device
• Site
Site • Device
• Link
Supported resource types 10
## Device with multiple VPN connections

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Get started with AWS Global Networks for Transit 
Gateways
The following tasks help you become familiar with AWS Global Networks for Transit Gateways. For 
more information about how AWS Global Networks for Transit Gateways works, see How global 
networks work.
In this example, you create a global network and register your transit gateway with the global 
network. You can also deﬁne and associate your on-premises network resources with the global 
network.
Tasks
• Prerequisites
• Step 1: Create a global network
• Step 2: Register your transit gateway
• Step 3: (Optional) Deﬁne and associate your on-premises network resources
• Step 4: (Optional) Enable multi-account access
• Step 5: View and monitor your global network
Prerequisites
Before you begin, ensure that you have a transit gateway with attachments in your account or 
in any account within your organization. For more information, see Getting Started with Transit 
Gateways.
The transit gateway can be in the same AWS account as the global network or in a diﬀerent AWS 
account within the organization.
Step 1: Create a global network
Create a global network as a container for your transit gateway.
To create a global network
1. Open the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
Prerequisites 11
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
2. Under Connectivity, choose Global Networks.
3. Choose Create global network.
4. Enter a name and description for the global network, and choose Create global network.
Step 2: Register your transit gateway
Register a transit gateway in your global network.
To register the transit gateway
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit gateways, and then choose Register transit gateway.
5. From the Select account dropdown list, choose the account that you want to register the 
transit gateway from.
A list of transit gateways from that account appear in the Select transit gateway to register
section.
6. Select one or more transit gateways from the list, and then choose Register transit gateway.
Step 3: (Optional) Deﬁne and associate your on-premises 
network resources
You can deﬁne your on-premises network by creating sites, links, and devices to represent objects 
in your network. For more information, see the following procedures:
• Create a site using AWS Network Manager
• Adding a link
• Add a device using AWS Network Manager
You associate the device with a speciﬁc site, and with one or more links. For more information, 
see the section called “Associate or disassociate a device link”.
Step 2: Register your transit gateway 12
## Multi-device and multi-link site

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
On your transit gateway you can
• Create a Site-to-Site VPN connection attachment. For more information, see the section called 
“Customer gateway associations”.
• Create a transit gateway Connect attachment, and then associate the Connect peer with the 
device. For more information, see the section called “Add a Connect peer association”.
You can also work with one of our Partners in the AWS Partner Network (APN) to provision and 
connect your on-premises network. For more information, see AWS Network Manager.
Step 4: (Optional) Enable multi-account access
Enable multi-account access to register transit gateways from multiple accounts, allowing you to 
view and manage transit gateways and associated resources from those registered accounts in your 
global network. Onboarding to AWS Organizations is a prerequisite for enabling multi-account 
access for Network Manager.
1. Create your organization using AWS Organizations.
If you've already done this skip this step. For more information on creating an organization using 
AWS Organizations, see Creating and managing an organization in the AWS Organizations User 
Guide.
2. Enable multi-account on the Network Manager console.
This enables trusted access for Network Manager and allows for registering delegated 
administrators. For more information enabling trusted access and registering delegated 
administrators, see Multi-account in AWS Global Networks for Transit Gateways.
3. Create your global network.
For more information on creating a global network, see Create a global network using AWS 
Network Manager.
4. Register transit gateways.
With multi-account enabled, you can register transit gateways from multiple accounts to your 
global network. For more information about registering transit gateways, see Transit gateway 
registrations in AWS Global Networks for Transit Gateways.
Step 4: (Optional) Enable multi-account access 13
## SD-WAN connecting to AWS

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Step 5: View and monitor your global network
The Network Manager console provides a dashboard for you to view and monitor both your transit 
gateway network objects in your global network.
To access the dashboard for your global network
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. The Overview page provides an inventory of the objects in your global network for your 
transit gateway network. For more information about the pages in the dashboard, see the 
section called “Access transit gateway network dashboards”.
Step 5: View and monitor your global network 14
## Connection between devices

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
AWS Global Networks for Transit Gateways scenarios
The following are common use cases and scenarios for using AWS Global Networks for Transit 
Gateways to manage your transit gateways.
Contents
• AWS-only multi-Region and multi-account global network
• Single device with a single VPN connection
• Device with multiple VPN connections
• Multi-device and multi-link site
• SD-WAN connecting to AWS
• Connection between devices
AWS-only multi-Region and multi-account global network
In this scenario, your AWS network consists of three transit gateways. You own transit gateways
tgw-1 and tgw-3. Transit gateway tgw-1 has a peering attachment with transit gateway tgw-2
that's in a diﬀerent AWS account. Your entire network is within AWS, and does not consist of on-
premises resources.
AWS-only multi-Region and multi-account global network 15
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
For this scenario, do the following in Network Manager:
• Create a global network. For more information, see Create a global network using AWS Network 
Manager.
• Register the transit gateways tgw-1 and tgw-3 with your global network. For more information, 
see Register a transit gateway using AWS Network Manager.
When you register tgw-1, the transit gateway peering attachment is included in the global 
network, and you can see information about tgw-2. However, any attachments for tgw-2 are not 
included in your global network. To see attachments for tgw-2, you must enable multi-account 
access.
• This enables trusted access for global networks and allows for registering delegated 
administrators. For more information enabling trusted access and registering delegated 
administrators, see Multi-account in AWS Global Networks for Transit Gateways.
• Register the tgw-2 transit gateway with your global network. For more information, see Transit 
gateway registrations in AWS Global Networks for Transit Gateways.
Single device with a single VPN connection
In the following scenario, your global network consists of a single site with a single device and link. 
The site is connected to your AWS network through a Site-to-Site VPN attachment on a transit 
gateway. Your transit gateway also has two VPC attachments.
Single device with a single VPN connection 16
## Modify a global network

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
For this scenario, do the following in Network Manager:
• Create a global network. For more information, see Create a global network using AWS Network 
Manager.
• Register the transit gateway. For more information, see Register a transit gateway using AWS 
Network Manager.
• Create a site, device, and link. For more information, see the section called “Sites and links” and
the section called “Devices”.
• Associate the device with the site and with the link. For more information, see the section called 
“Associate or disassociate a device link”.
• Associate the customer gateway (for the transit gateway Site-to-Site VPN attachment) with the 
device, and optionally, the link. For more information, see the section called “Customer gateway 
associations”.
Device with multiple VPN connections
In the following scenario, your on-premises network consists of a device with two Site-to-Site VPN 
connections to AWS. The device is associated with two customer gateways on two diﬀerent transit 
Device with multiple VPN connections 17
## Multi-account

## Prerequisites

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
gateways. Each VPN connection uses a separate link. To indicate which link applies to which VPN 
connection, you associate the customer gateway with both the device and the corresponding link.
For this scenario, do the following in global networks:
• Create a global network. For more information, see Create a global network using AWS Network 
Manager.
• Register the transit gateways. For more information, see Register a transit gateway using AWS 
Network Manager.
• Create a site, device, and link. For more information, see the section called “Sites and links” and
the section called “Devices”. />.
• Associate the device with the site and both links. For more information, see the section called 
“Associate or disassociate a device link”.
• Associate each customer gateway with the device and the corresponding link. For more 
information, see the section called “Customer gateway associations”.
Device with multiple VPN connections 18
## Manage multiple accounts

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Multi-device and multi-link site
In the following scenario, your on-premises network consists of a site with two devices and two 
separate Site-to-Site VPN connections to AWS. For example, in a single building or campus, you 
might have multiple devices connected to AWS resources. Each device is associated with a customer 
gateway that's attached to your transit gateway.
Your AWS network is also connected to your on-premises network though an Direct Connect 
gateway, which is an attachment on your transit gateway.
For this scenario, do the following in global networks:
• Create a global network. For more information, see Create a global network using AWS Network 
Manager.
• Register the transit gateway. For more information, see Register a transit gateway using AWS 
Network Manager.
Multi-device and multi-link site 19
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• Create one site, two devices, and two links. For more information, see the section called “Sites 
and links” and the section called “Devices”.
• Associate each device with the corresponding link. For more information, see the section called 
“Associate or disassociate a device link”.
• Associate each customer gateway with the corresponding device and link. For more information, 
see the section called “Customer gateway associations”.
SD-WAN connecting to AWS
In the following example, your on-premises network consists of two sites. The Chicago site has two 
devices and the New York site has one device. Your AWS network consists of two transit gateways. 
All devices are associated with customer gateways (Site-to-Site VPN attachments) on both transit 
gateways.
Your on-premises network is managed using SD-WAN. The SD-WAN controller creates Site-to-Site 
VPN connections to the transit gateways, and creates the device, site, and link resources in Network 
Manager. This automates connectivity and enables you to get a full view of your network in global 
networks. The SD-WAN controller can also use global networks events and metrics to enhance its 
dashboard.
SD-WAN connecting to AWS 20
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
For more information about Partners who can help you set up your Site-to-Site VPN connections, 
see AWS Network Manager.
Connection between devices
In the following scenario, your AWS network consists of a transit gateway with a Connect 
attachment to a VPC that contains a virtual appliance on an EC2 instance. A Connect peer (GRE 
tunnel) is established between the transit gateway and the appliance. The appliance is connected 
to a physical device in your on-premises network through a connection.
Connection between devices 21
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
For this scenario, do the following in global networks:
• Create a global network. For more information, see Create a global network using AWS Network 
Manager.
• Register the transit gateway. For more information, see Register a transit gateway using AWS 
Network Manager.
• Create a site, device, and link for your on-premises network. For more information, see the 
section called “Sites and links” and the section called “Devices”.
• Associate the device with the site and with the link. For more information, see the section called 
“Associate or disassociate a device link”.
• Create a device for the EC2 virtual device. For visualization in the global networks console, 
specify the AWS location of the device (for example, the Availability Zone). For more information, 
see the section called “Devices”.
• Create a connection between the on-premises device and the virtual device. For more 
information, see the section called “Associate or disassociae an on-premises link”.
• Associate the Connect peer with the on-premises device. For more information, see the section 
called “Associate or disassociate a Connect peer”.
Connection between devices 22
## Enable trusted access

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Modify a global network using AWS Network Manager
After setting up a global network you further modify it by performing a number of tasks.
Tasks you can perform to enhance your global network include:
• Monitor and manage global network resources from other AWS accounts.
AWS Global Networks for Transit Gateways supports multi-account access. If enabled, multi-
account allows you to manage, monitor, and view dashboards of resources from AWS accounts 
shared with your account.
• Register a transit gateway
Register existing transit gateways in your global network. When you register a transit gateway 
all transit gateway attachments are automatically included in the registration. A transit gateway 
must ﬁrst be created before it can be registered. For more information about transit gateways 
and creating one, see Transit gateways in the Amazon VPC Transit Gateways User Guide.
• Create sites and links, and connect devices
Add representations of physical devices and sites to your global network. You can then create a 
link that associates a device and a site.
• Create customer gateway associations
Create associations between two devices or between a device and a transit gateway Connect 
peer.
• Access global network dashboards
AWS Global Networks for Transit Gateways includes separate transit gateway network and 
transit gateway dashboards. On these dashboards you can view logical trees and geographic 
maps of your networks, which includes attachments, sites and devices. You can also view 
monitoring and events dashboards, allowing you to view Amazon CloudWatch metrics and to set 
threshold alarms on these metrics.
If your account is set up for multi-account, you can manage global network resources from multiple 
AWS accounts. For more information on multi-account, see the section called “Multi-account”.
Contents
23
## Disabled trusted access

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• Multi-account in AWS Global Networks for Transit Gateways
• Global networks in AWS Global Networks for Transit Gateways
• Transit gateway registrations in AWS Global Networks for Transit Gateways
• Sites and links in AWS Global Networks for Transit Gateways
• Devices in AWS Global Networks for Transit Gateways
• Connections in AWS Global Networks for Transit Gateways
• Gateway associations in AWS Global Networks for Transit Gateways
• Resource tags in AWS Global Networks for Transit Gateways
Multi-account in AWS Global Networks for Transit Gateways
With AWS Global Networks for Transit Gateways, you can manage, monitor, and view dashboards 
of global network resources from multiple AWS accounts associated with a single organization 
using AWS Network Manager. For more information about setting up multi-account, see Manage 
multiple accounts in global networks using AWS Organizations below.
Important
• We strongly recommended that you use the global networks console for enabling 
multi-account settings with global networks, because the console automatically creates 
all required roles and permissions for multi-account access. Choosing an alternative 
approach requires an advanced level of expertise, and opens the multi-account set up for 
your global network to be more prone to error.
• Multi-account is not available in the AWS GovCloud (US-West) and the AWS GovCloud 
(US-East) Regions.
Prerequisites
To enable multi-account, you ﬁrst set up an account in AWS Organizations. This ﬁrst account 
becomes the management account. Using this account, you can then add other accounts as 
member accounts to your organization. For more information about how multi-account support 
works, see Creating and managing an organization in the AWS Organizations User Guide.
Multi-account 24
## Register a delegated administrator

AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Manage multiple accounts in global networks using AWS Organizations
AWS Global Networks for Transit Gateways allows you to centrally manage, monitor, and visualize 
network resources from multiple accounts within an organization in a single global network. To 
manage resources from multiple accounts in global networks, you ﬁrst set up an organization 
using AWS Organizations. The ﬁrst account that you use to create an organization becomes the 
management account. Using this account, you can add other accounts as member accounts to your 
organization. From the management account, you can designate one or more accounts within the 
orgaization as delegated administrator accounts by registering them using the global networks 
console. For more information about setting up an organization, see Creating and managing an 
organization in the AWS Organizations User Guide.
To enable multi-account access in the global networks console, you ﬁrst enable trusted access 
for the Network Manager service, and then register a delegated administrator account for your 
organization.
Important
• We strongly recommended that you use the global networks console for enabling 
multi-account settings with global networks, because the console automatically creates 
all required roles and permissions for multi-account access. Choosing an alternative 
approach requires an advanced level of expertise, and opens the multi-account set up for 
your global network to be more prone to error.
• Multi-account is not available in the AWS GovCloud (US-West) and the AWS GovCloud 
(US-East) Regions.
With multi-account support, you can create a single global network for any of your AWS accounts, 
and then register transit gateways from those accounts using the global networks console. Multi-
account is supported in all AWS Regions where global networks is supported. For more information 
about multi-account, see Multi-account in AWS Global Networks for Transit Gateways.
Trusted access
Trusted access creates AWSServiceAccess for global networks and CloudFormation StackSets 
with AWS Organizations. Enabling trusted access provides required permissions for AWS 
Organizations to deploy service-linked roles (SLRs) to all member accounts within your 
organization.
Manage multiple accounts 25
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Enable trusted access
When you enable trusted access from the global networks console, you select a one-time 
permission level (IAMRoleForAWSNetworkManagerCrossAccountResourceAccess) as either 
administrator or read-only for each of the management and delegated administrator accounts.
• Admin — Assign this permission if the delegated administrator and management accounts need 
to be able to modify resources from other accounts in the global network while using the global 
networks console switch role.
• Read-only — Assign this permission if the delegated administrator and management accounts 
only need to review information about resources from other accounts in the global network 
while using the global networks console switch role, but don't need to make any changes.
The global networks console manages all of this when calling the Network Manager API.
When you enable trusted access, the following roles are deployed in your organization using 
CloudFormation StackSets and AWS Identity and Access Management (IAM) services:
• The Network Manager SLR (AWSServiceRoleForNetworkManager) to all member accounts
• The CloudFormation StackSets member SLR 
(AWSServiceRoleForCloudFormationStackSetsOrgMember) to all member accounts
• The Network Manager SLR (AWSServiceRoleForNetworkManager) to the management 
account
• The CloudFormation StackSets admin 
(AWSServiceRoleForCloudFormationStackSetsOrgAdmin) SLR to the management 
account
• The Amazon CloudWatch sharing role (CloudWatch-CrossAccountSharingRole) to all 
member accounts
• The global networks console switch role 
(IAMRoleForAWSNetworkManagerCrossAccountResourceAccess) to all member accounts
• The Amazon CloudWatch monitoring role (AWSServiceRoleForCloudWatchCrossAccount) 
to the management account
For more information about enabling trusted access, see Enable trusted access in an AWS global 
network.
Manage multiple accounts 26
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Disable trusted access
Note
Disabling trusted access through the global networks console removes
AWSServiceAccess for global networks with AWS Organizations. Disabling trusted 
access removes global networks access to perform tasks within your organization. AWS 
Organizations won't allow you to disable an organization's trusted access for the Network 
Manager service if there are any delegated administrators that haven't been deregistered 
from that organization.
• Disabling trusted access through the global networks console won't remove
AWSServiceAccess for CloudFormation StackSets with AWS Organizations. You can manually 
remove the service access for CloudFormation StackSets by using the CloudFormation StackSet 
console or by using the Organizations API/CLI. For more information on disabling trusted access 
for CloudFormation StackSets, see Disable trusted access with AWS CloudFormation StackSets in 
the AWS Organizations User Guide.
• Disabling trusted access won't remove any SLRs that were deployed when enabling trusted 
access.
When you disable trusted access, the following are aﬀected in global networks:
• All transit gateways owned by other accounts in your organization. You won't be able to see 
transit gateways or their attached resources from other accounts in your organization that were 
registered to your global network.
• IAM roles deployed in all member accounts managed by the Network Manager service. Disabling 
trusted access doesn't remove accounts, transit gateways, or resources but does deregister them 
from other delegated administrator's global networks. These can be added back in as needed 
by re-enabling trusted access. For more information about the DeleteStackSet API, see
DeleteStackSet in the AWS CloudFormation API Reference.
For more information about disabling trusted access, see Disable trusted access in an AWS global 
network.
Manage multiple accounts 27
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Delegated administrators
Member accounts in your organization with delegated administrator access are able to leverage 
service-linked roles and assume IAM roles for access across multiple accounts. Only member 
accounts that are part of your AWS Organizations can be registered as delegated administrators. 
Your organization can have up to ten registered delegated administrators. Before you register a 
delegated administrator, you must enable global networks trusted access for your organization. For 
more information, see Enable trusted access in an AWS global network.
Important
Using your AWS Organizations management account to manage your global network in 
global networks is not recommended because the required service-linked roles are not 
propagated to this account. For more information on service-linked roles, see the section 
called “Service-linked role”.
Register delegated administrators
After it's registered, a delegated administrator has the same permissions as the management 
account. A delegated administrator for the Network Manager service can leverage the SLRs in 
the member accounts that were deployed when trusted access was enabled and can view transit 
gateways from other member accounts and can register them to your global network. This allows 
transit gateways and associated resources to appear in your global network topology. In addition 
CloudFormation StackSets is updated to include the delegated administrator accounts in the 
trusted relationship of the deployed IAM roles in the member accounts.
For information about registering a delegated administrator, see Register an administrator for 
multi-account in an AWS global network.
Deregister delegated administrators
Deregistering a delegated administrator removes that account's permission to leverage SLRs and 
assume IAM roles in other member accounts that were set up using AWS Organizations.
After it's deregistered, the delegated administrator no longer has the same permissions as the 
management account. The following occurs:
• A delegated administrator is no longer able to leverage the deployed SLRs in the member 
accounts that were deployed when trusted access was enabled.
Manage multiple accounts 28
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• All registered transit gateways from other member accounts are deregistered from any global 
network for the speciﬁc delegated administrator. The network topology is updated to no longer 
show resources from other member accounts.
• CloudFormation StackSets are updated with the removal of the delegated administrator account. 
That account is no longer able to assume any IAM roles deployed in other member accounts.
For information about deregistering a delegated administrator, see Deregister an administrator 
from multi-account in an AWS global network.
Multi-account tasks
• Enable trusted access in an AWS global network
• Disable trusted access in an AWS global network
• Register an administrator for multi-account in an AWS global network
• Deregister an administrator from multi-account in an AWS global network
• Manage IAM multi-account role deployments in an AWS global network
• Troubleshoot multi-account self-managed roles in an AWS global network
Enable trusted access in an AWS global network
Enabling trust is a one-time task that deploys the required service-linked roles (SLRs) and custom 
Identity and Access Management (IAM) roles to all accounts in your organization that can be 
assumed by the management account or delegated administrators for access across multiple 
accounts. For more information about trusted access, see Trusted access.
To enable multi-account trusted access
1. Log into the global networks console at https://console.aws.amazon.com/networkmanager/
home/, using the AWS Organizations management account.
2. Choose Get started.
3. In the navigation pane, choose Enable trusted access.
4. From the Permission level dropdown list in Enable trusted access,
choose the Permission level for the Network Manager console switch role
IAMRoleForAWSNetworkManagerCrossAccountResourceAccess. This role is deployed to 
all member accounts and is assumed by the delegated administrator or management account 
Enable trusted access 29
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
when accessing resources from other accounts using the global networks console. You can 
choose only one permission level for all accounts. Permission can be one of the following:
• Read-only — Assign this permission if the delegated administrator and management 
accounts only need to review information about resources from other accounts in the global 
network while using the console switch role, but don't need to make any changes.
• Admin — Assign this permission if the delegated administrator and management accounts 
need to be able to modify resources from other accounts in the global network while using 
the global networks console switch role.
5. Choose Enable trusted access.
Depending on your organization size, it might take a few minutes or more to enable trusted 
access. During this time the State shown in the Trusted access section displays Enabling in 
progress. When access is enabled, the State changes to Enabled. Additionally, the IAM role 
deployments status section at the bottom of the page displays the status of the IAM roles 
being deployed to member accounts of the organization.
6. After trusted access is enabled, you can register delegated administrators.
Disable trusted access in an AWS global network
Disabling trusted access removes the trust relationship between the Network Manager service 
access and your organization. Network Manager is no longer able to perform actions within 
your organization or access information about your organization. Trusted access remains for 
CloudFormation StackSets in the event that your organization is using that service outside of 
Network Manager. For more information on disabling CloudFormation StackSets, see Disabling 
trusted access with AWS CloudFormation Stacksets in the AWS Organizations User Guide.
Transit gateways from other accounts are deregistered from global networks owned by the 
management account and can no longer provide access to their attached resources. For more 
information about disabling trusted access, see Disable trusted access.
You must ﬁrst deregister all delegated administrators before you can disable trusted access. If you 
have registered delegated administrators, you will be prompted to deregister them during the 
disable trusted access process.
You can enable trusted access again after disabling it. However you will need to set up the list of 
delegated administrators again.
Disabled trusted access 30
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
To disable trusted access
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/ with the management account.
2. Under Connectivity, choose Global Networks.
3. In the navigation pane, choose Settings.
4. In the Trusted Access section, choose Disable trusted access.
5. If you have any registered delegated administrators, you can deregister them by choosing
Deregister delegated administrators.
6. Choose Disable trusted access on the conﬁrmation dialog box to conﬁrm that you want to 
disable trusted access.
Depending on the size of your organization, it might take several minutes or longer to disable 
trusted access. The State displays Disabling in progress. During this time you won't be able to 
re-enable trusted access. When ﬁnished, the Status changes to Disabled.
Register an administrator for multi-account in an AWS global network
Use the AWS Global Networks for Transit Gateways console to register delegated administrators. 
You can register up to ten delegated administrators. Delegated administrators can assume the SLR 
and IAM roles deployed while enabling trusted access for access across multiple accounts. For more 
information about delegated administrators, see Delegated administrators.
To register a delegated administrator
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/ with the management account.
2. Under Connectivity, choose Global Networks.
3. In the navigation pane, choose Settings.
4. In the Delegated Administrators section, choose Register delegated administrator.
5. From the AWS account ID dropdown list, choose one or more AWS Organizations accounts 
that you want to delegate administrator permissions to.
6. Choose Register delegated administrator.
7. When the delegated administrator is registered, you can then register transit gateways from 
any transit gateways from any account within your organization to the global network in the 
Register a delegated administrator 31
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
delegated administrator account. For more information about registering transit gateways in 
the global network of a delegated administrator account, see Transit gateway registrations in 
AWS Global Networks for Transit Gateways.
Deregister an administrator from multi-account in an AWS global 
network
Deregistering delegated administrators removes that account's permission to manage global 
networks for your organization. All registered transit gateways from other member accounts are 
deregistered from the speciﬁc delegated administrator's global networks. For more information 
about how deregistering delegated administrators works, see Deregister delegated administrators.
To deregister a delegated administrator
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/ with the management account.
2. Under Connectivity, choose Global Networks.
3. In the navigation pane, choose Settings.
4. In the Delegated Administrators section, choose one or more accounts that you want to 
deregister.
Depending on your organization size and the number of delegated administrators you're 
deregistering, this could take several minutes. During this time you won't be able to register 
any new delegated administrators.
Manage IAM multi-account role deployments in an AWS global network
The IAM role deployments status section displays the current role deployments status for all 
member accounts set up in your account.
• Member account ID  — The account ID for the account set up in AWS Organizations. This 
includes member accounts and members that have been registered as delegated administrators.
• CloudWatch role status — The status of the account's Amazon CloudWatch role. If you enable 
multi-account using the Network Manager console, this is StackSets-managed if deployed 
successfully. Otherwise, this is Self-managed.
Deregister a delegated administrator 32
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• Console role status — The status of the account's Network Manager console role. If you enable 
multi-account using the Network Manager console, this is StackSets-managed if deployed 
successfully. Otherwise, this is Self-managed.
• Review required  — This applies only to Self-managed roles. A review is required to ensure 
that the permissions set up for the account are correct. For more information, see Multi-account 
access roles for AWS Global Networks for Transit Gateways.
If you make changes to your role policies, or if you've updated a self-managed role, you can deploy 
the updated policy to your AWS Organizations accounts.
To retry the IAM role deployment status
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/ with the management account.
2. Under Connectivity, choose Global Networks.
3. In the navigation pane, choose Settings.
4. In the IAM role deployments status section, choose Retry role deployment.
Depending on your organization size and the number of member accounts in your 
organization, this could take several minutes. During this time you won't be able to register or 
deregister any new delegated administrators.
Troubleshoot multi-account self-managed roles in an AWS global 
network
AWS Global Networks for Transit Gateways uses AWS CloudFormation StackSets to deploy 
the required IAMRoleForAWSNetworkManagerCrossAccountResourceAccess role and 
the CloudWatch monitoring CloudWatch-CrossAccountSharingRole role in your AWS 
Organizations member accounts for cross-account access. For a CloudFormation StackSets-
managed deployment, IAM roles must have the required policies attached, as well as the trusted 
relationship to allow registered delegated administrators and the management account the 
ability to assume these roles. In a self-managed deployment, you own the responsibility to attach 
the appropriate policies and to manage the trusted relationship required for the delegated 
administrator and management accounts to access multiple accounts.
Troubleshoot self-managed roles 33
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Important
We strongly recommend that you use the global networks console for enabling multi-
account settings using the global networks console as this automatically sets up all 
required roles and permissions for multi-account access. Choosing an alternative approach 
requires an advanced level of expertise and opens the multi-account setup for your global 
network to be more prone to error.
If the CloudFormation StackSets deployment fails, and the Review required message is IAM 
role exists, follow the steps below in IAM role exists to change the role from Self-managed to
StackSets-managed. For any message other than IAM role exists, ﬁle an AWS Support case. For 
more information on creating a support case, see Creating a support case in the AWS Support User 
Guide.
IAM role exists
If the IAM role has the exact same name in a current the member account, these roles appear 
in the IAM role deployments status with a status of Self-managed. In order to change this to 
StackSets-managed, delete the IAM role from the member account with the duplicate role name. 
After deleting the IAM role, use the global networks console to retry the role deployment. For 
the steps to retry a role deployment, see Manage IAM multi-account role deployments in an AWS 
global network to retry the role deployment.
To change a role from self-managed to StackSets-managed
1. Access the AWS Identity and Access Management (IAM) console at https:// 
console.aws.amazon.com//iamv2/home?#/ with the member account that has a self-managed 
role status.
2. In the navigation pane, choose Roles.
3. In the Roles ﬁeld, search for the role name you want to delete.
4. Choose the role, and then choose Delete.
5. Conﬁrm that you want to delete the role.
Troubleshoot self-managed roles 34
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Warning
This might break other functionality if a custom role has other attached policies or 
trusted relationships.
6. Access the global networks console at https://console.aws.amazon.com/networkmanager/
home/ with the AWS Organizations management account.
7. Choose Get started.
8. In the navigation pane, choose Settings.
9. In the IAM role deployment status section, choose Retry role deployment.
Depending on the size of your organization, it might take several minutes or longer to disable 
trusted access. During this time you won't be able to re-enable trusted access.
Global networks in AWS Global Networks for Transit Gateways
A global network in AWS Global Networks for Transit Gateways is a container for your network 
objects. When you create a global network, you create only the framework of the global network 
itself. You'll then further deﬁne this network by adding network objects to it, such as
• transit gateways.
• sites, devices, and links, and then creating connections using links between those sites and 
devices.
• customer gateway associations.
• Connect peer associations.
Note
When creating a global network, you're prompted to create an associated core network. 
A core network is a feature of AWS Cloud WAN and is not needed if you're not using this 
feature. While creating a global network, you're prompted whether or not to create a core 
network. Clear the option to create the core network. If you decide later on that you want 
to create a core network for this global network you can. For the steps to create a core 
network, see What is AWS Cloud WAN in the AWS Cloud WAN User Guide.
Global networks 35
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
You can create, view, update, and delete a global network using either the AWS Network Manager 
console or by using the CLI.
Global network tasks
• Create a global network using AWS Network Manager
• View a global network using AWS Global Networks for Transit Gateways
• Update a global network using AWS Network Manager
• Delete a global network using AWS Network Manager
Create a global network using AWS Network Manager
Create a global network.
To create a global network
1. Open the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3.
Choose Create global network.
4. Enter a Name and Description for your global network.
5. (Optional) In Additional settings, add Key and Value tags that further help identify an Network 
Manager resource. To add multiple tags, choose Add tag for each tag you want to add.
6. Choose Next.
7. To create a AWS Transit Gateway network only, clear the Add core network in your global 
network check box on the Create global network - optional page, and then choose Next.
Note
Core networks are only used with AWS Cloud WAN. If you're creating global network 
for AWS Cloud WAN and want to create a core network, see Create a core network 
policy in the AWS Cloud WAN User Guide.
8. Review the information for the global network you want to create, and then choose Create 
global network.
Create a global network 36
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
To create a global network using the AWS CLI
Use the create-global-network command.
View a global network using AWS Global Networks for Transit 
Gateways
View the details of your global network and information about the network objects in your global 
network.
To view your global network information
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. The Overview page displays an inventory of the objects in both your core network and transit 
gateway network. To view details about the global network resource (such as its ARN), choose
Details. For more information about the other pages on the dashboard, see the section called 
“Access transit gateway network dashboards”.
To view global network details using the AWS CLI
Use the describe-global-networks command.
Update a global network using AWS Network Manager
Update a global network by modifying the description or tags.
To update your global network
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. Choose Edit.
5. For Description, enter a new description for the global network.
View a global network 37
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
6. For Tags, choose Remove tag to remove an existing tag, or choose Add tag to add a new tag.
7. Choose Edit global network.
To update a global network using the AWS CLI
Use the update-global-network command to update the description. Use the tag-resource and
untag-resource commands to update the tags.
Delete a global network using AWS Network Manager
Delete a global network framework. You cannot delete a global network if there are any network 
objects in the global network, including transit gateways, links, devices, and sites. You must ﬁrst 
deregister or delete the network objects.
To delete your global network
1. Open the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. In the navigation pane, choose Global networks.
4. Choose your global network and choose Delete.
5. In the conﬁrmation dialog box, choose Delete.
To delete a global network using the AWS CLI
Use the delete-global-network command.
Transit gateway registrations in AWS Global Networks for 
Transit Gateways
You can register your existing transit gateways with a global network. Any transit gateway 
attachments (such as VPCs, VPN connections, and Direct Connect gateways) are automatically 
included in your global network.
Transit gateway limitations
Note the following about registering transit gateways in a global network:
Delete a global network 38
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• A transit gateway must ﬁrst be created in Amazon Virtual Private Cloud (VPC) before it can be 
registered in a global network. For more information about transit gateways and creating one, 
see Transit gateways in the Amazon VPC Transit Gateways User Guide.
• You can have multiple global networks, but you can only register one transit gateway with one 
global network.
• You can register transit gateways that are in the same AWS account as the global network.
• You cannot create, delete, or modify your transit gateways and their attachments using the 
Network Manager console or APIs. To work with transit gateways, use the Amazon VPC console 
or the Amazon EC2 APIs.
Transit gateway registration tasks
• Register a transit gateway using AWS Network Manager
• View registered transit gateways using AWS Network Manager
• Deregister a transit gateway using AWS Network Manager
Register a transit gateway using AWS Network Manager
Register a transit gateway created using Amazon Virtual Private Cloud with your AWS global 
network using either the Network Manager console or using the CLI. You cannot register a transit 
gateway with more than one global network.
To register a transit gateway
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit gateways., and then choose Register transit gateway.
5. (Optional) If your account is enabled for multi-account access, from the Select account
dropdown list choose the account you want to register transit gateways from.
The Select transit gateway to register section populates with that account's transit gateways.
6. Choose one or more transit gateways, and then choose Register transit gateway.
Register a transit gateway 39
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
To register a transit gateway using the AWS CLI
Use the register-transit-gateway command.
View registered transit gateways using AWS Network Manager
View a transit gateway registered with your AWS global network using either the Network Manager 
console or using the CLI.
To access your registered transit gateways
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit gateways.
5. The Transit gateways page lists your registered transit gateways. Choose the ID of transit 
gateway to view its details.
To view your registered transit gateways using the AWS CLI
Use the get-transit-gateway-registrations command.
Deregister a transit gateway using AWS Network Manager
Deregister a transit gateway from a global network using either the Network Manager console or 
using the CLI. Once deregistered, you can re-register this transit gateway with the same global 
network or with a diﬀerent global network.
To deregister a transit gateway
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit gateways.
5. Select your transit gateway, and choose Deregister.
View registered transit gateways 40
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
To deregister a transit gateway using the AWS CLI
Use the deregister-transit-gateway command.
Sites and links in AWS Global Networks for Transit Gateways
After you've added any devices to your AWS global network, you can associate of your devices with 
that particular site using a connection, or link. For information on adding devices, see the section 
called “Devices”.
Sites
A site represents the physical location of your network, using location information such as latitude, 
longitude, and address. You can have multiple sites for each of your network locations. Sites are 
useful when viewing the global network dashboard, which provides you the geographical location 
of these sites based on location information you provided. Once you create a site you can view the 
devices associated with the site and create links between devices and sites. You can also view any 
VPNs associated with the site as well as monitor CloudWatch metrics for this site.
Links
A link represents the connection between a device and a site. Once you've added a device and 
created a site, you can create an association between the device and a site.
Tasks
Create a site using AWS Network Manager
Create a site to represent the physical location of your network. Location information is used in the 
Network Manager transit gateway dashboards.
To create a site
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Sites. Choose Create site.
Sites and links 41
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
5. For Name and Description, enter a name and description for the site.
6. For Address, enter the physical address of the site, for example, New York, NY 10004.
7. For Latitude, enter the latitude coordinates for the site, for example, 40.7128.
8. For Longitude, enter the longitude coordinates for the site, for example, -74.0060.
9. Choose Create site.
Creating and viewing a site using the AWS CLI
Use the following commands:
• To create a site: create-site
• To view your sites: get-sites
View site details using AWS Network Manager
View details about a core network site using the Network Manager console.
To view details about a site
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Sites.
5. Choose the link that you want to see site details for.
6. The General details page provides information about the site.
7. Choose the Devices tab. This page displays information about the devices that are connected 
to the site. If you don't see a device listed, you'll need to add it. For more information on 
adding devices, see the section called “Add a device”.
8. Choose the Links tab. This page displays the links that represent a connection from a device. If 
you don't see a link listed, you'll need to create the link. For the steps to create a link, see the 
section called “Add a link”.
9. Choose the VPNs tab. This page displays site-related VPN information.
View site details 42
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
10. Choose the Monitoring tab. This page displays Data In and Data Out information for your 
links.
11. From the dropdown list, choose the link that you want to view information for.
12. (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To 
set a custom time frame, choose Custom and then choose a Relative or Absolute time, and 
then choose if you want to see that date range in UTC or the edge location's Local time zone.
Choose Add to dashboard to add this metric to your CloudWatch dashboard. For more 
information about using CloudWatch dashboards, see Using Amazon CloudWatch Dashboards
in the Amazon CloudWatch User Guide.
Note
The Add to dashboard option only works if your registered transit gateway is in the US 
West (Oregon) Region.
Update a site using AWS Network Manager
Update any of the details of a site you've added, including the description, address, latitude, and 
longitude.
To update a site
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Sites, and select your site.
5. Choose Edit.
6. Update the Description, Address, Latitude, Longitude, and Tags as needed.
7. Choose Edit site.
Update a site using the AWS CLI
Use the update-site command.
Update a site 43
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Delete a site using AWS Network Manager
Delete sites from your global network if the site is no longer valid or you no longer want to return 
any information about the site. You must ﬁrst disassociate the site from any devices and delete any 
links for the site.
To delete a site
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Sites.
5. Select the site and choose Delete.
6. In the conﬁrmation dialog box, choose Delete.
Deleting a site using the AWS CLI
Use the delete-site command.
Add a link using AWS Network Manager
Add a link to associated a device with a site.
To add a link
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Sites.
5. Choose the link for the site ID that you want to add a link to, and then choose the Links tab.
Note
Choose the link. Do not select the check box.
Delete a site 44
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
6. Choose the Links tab, and then choose Create link.
7. For Name and Description, enter a name and description for the link.
8. For Upload speed (Mbps), enter the upload speed in Mbps.
9. For Download speed (Mbps), enter the download speed in Mbps.
10. (Optional) For Provider, enter the name of the service provider.
11. (Optional) For Type, enter the type of link, for example, broadband.
12. (Optional) Under Additional settings, add one or more Key and Value Tags to help further 
identify this link.
13. Choose Create link.
Edit a link using AWS Network Manager
Edit the link between two devices in your Cloud WAN global network.
To update a link
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Sites.
5. Choose the Links tab.
6. On the Links page, select the check box for the link that you want to update, and then choose
Edit.
7. Modify any of the link settings as needed, including adding, editing, or removing tags.
8. Choose Edit link.
Delete a link using AWS Network Manager
You can delete the link between two devices without deleting the devices.
To delete a link
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
Edit a link 45
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Sites.
5. Choose the Links tab.
6. On the Links page, select the check box for the link that you want to delete, and then choose
Delete.
7. Conﬁrm that you want to delete the link by choosing Delete again.
Devices in AWS Global Networks for Transit Gateways
Devices represent a physical or virtual appliance in AWS Global Networks for Transit Gateways. 
When you add a device to your core network using AWS Network Manager, you can include 
optional information such as vendor, model and serial number to help you more easily identify the 
device.
In addition, you'll indicate whether the device is on-premises or in the AWS Cloud. If the device is 
on-premises you can specify optional information such as physical address. If the device is in the 
AWS Cloud, you can specify the zone, subnet ID, latitude and longitude, and physical address. Tags 
are also used to more help you identify this Network Manager resource.
Once added to your global network, a device can then be associated with a site. Before you can 
associate the device with a site using a link, you must ﬁrst create the site. For more information on 
creating sites and linking the site to a device, see the section called “Sites and links”.
Note
A single device can't be associated with multiple sites.
Topics
• Add a device using AWS Network Manager
• Delete a device using AWS Network Manager
• Edit a device using AWS Network Manager
• View device details using AWS Network Manager
Devices 46
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Add a device using AWS Network Manager
Create a device to represent a physical or virtual appliance.
To add a device
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices. Choose Create device.
5. For Name and Description, enter a name and description for the device.
6. For Model, enter the device model number.
7. For Serial number, enter the serial number for the device.
8. For Type, enter the device type.
9. For Vendor, enter the name of the vendor, for example, Cisco.
10. For Location type, specify whether the device is located in a remote location (on-premises 
network, data center, or other cloud provider) or in AWS.
If you choose AWS Cloud, specify the location of the device within AWS. For Zone, specify 
the name of an Availability Zone, Local Zone, Wavelength Zone, or an Outpost. For Subnet, 
specify the Amazon Resource Name (ARN) of a subnet (for example, arn:aws:ec2:us-
east-1:111111111111:subnet/subnet-abcd1234).
11. For Address, enter the physical address of the site, for example, New York, NY 10004.
12. For Latitude, enter the latitude coordinates for the site, for example, 40.7128.
13. For Longitude, enter the longitude coordinates for the site, for example, -74.0060.
14. Choose Create device.
Creating and viewing a device using the AWS CLI
Use the following commands:
• To create a device: create-device
• To view your devices: get-devices
Add a device 47
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Delete a device using AWS Network Manager
Delete any device from your global network that's no longer needed or is no longer available.
To delete a site
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices.
5. Choose the device that you want to want to delete, and then choose Delete.
6. Conﬁrm that you want to delete the site by choosing Delete again.
Deletion occurs immediately.
Edit a device using AWS Network Manager
Edit the details of a device, including whether the location type is either on-premises or AWS 
Cloud.
To update a device
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices.
5. Choose the check box of the device that you want to update, and then choose Edit.
6. Choose Edit device.
7. Add or update any of the following device information:
• Description
• Model
• Serial number
Delete a device 48
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• Type
• Vendor
• Location type
• Latitude
• Longitude
• Tags
8. Choose Edit device.
View device details using AWS Network Manager
View details about a device. On the device details page you can access tabs:
• Overview
This tab provides general information about the device, such as the device State, Vendor, and 
Model. You can also edit, delete, and associate or disassociate the device with a site,
• Links
Associate or disassociate a link with a device.
• On-premises associations
Associate or disassociate a device with a customer gateway. You must have at least one gateway 
set up and one link to create the association.
• Connect peer associations
Associate a Connect peer with a device, allowing you to connect with a transit gateway. You must 
have at least one Connect peer and one link.
• Connections
Create a connection between two devices using a link. You can create a connection between two 
devices in your global network. The connection can be between a physical or virtual appliance 
and a third-party appliance in a VPC, or between physical appliances in an on-premises network. 
A connection is created for a speciﬁc global network and cannot be shared with other global 
networks.
• VPNs
View device details 49
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
View the VPNs associated with the device. On this tab you can only view the associations of a 
transit gateway with a device.
• Monitoring
Monitor the device's data in, data out, and Tunnel down count average with CloudWatch metrics. 
You can modify the CloudWatch time frame as well as add these metrics to your global network 
dashboard.
Topics
• Associate or disassociate a device link using AWS Network Manager
• Associate or disassociate an on-premises link using AWS Network Manager
• Associate or disassociate a Connect peer using AWS Network Manager
• View VPNs using AWS Network Manager
• Monitor devices using AWS Network Manager
Associate or disassociate a device link using AWS Network Manager
Associate a link with a device in your AWS global network. In order to associate a link with a device, 
you must ﬁrst create the link. For more information on creating links, see the section called “Add a 
link”.
You can only associate one link with one device. If a link is already associated with a device, and 
you want to use that link with another device, you must ﬁrst disassociate the link the device it's 
associated with.
To associate a link with a device
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices.
5. Choose the link for the device ID that you want to add a link to, and then choose the Links tab.
View device details 50
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Note
Choose the link. Do not select the check box.
6. Choose the Links tab, and then choose Associate link.
7. Choose the link that you want to associate with the device.
8. Choose Associate link.
The link is available to use immediately.
If you to use a link with another device, you must ﬁrst disassociate the link from its original device.
To disassociate a link from a device
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices.
5. Choose the link for the device ID that you want to add a link to, and then choose the Links tab.
Note
Choose the link. Do not select the check box.
6. Choose the Links tab, and then choose Associate link.
7. Choose the check box for the link that you want to disassociate from a device.
8. Choose Disassociate link.
Disassociation occurs immediately.
Associate or disassociate an on-premises link using AWS Network Manager
Associate or disassociate an on-premises device link association in your AWS global network.
View device details 51
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
You can only associate one link with a customer gateway. If a link is already associated with a 
customer gateway, and you want to use that link with another gateway, you must ﬁrst disassociate 
the link the gateway it's currently associated with.
To create an on-premises association
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices.
5. Choose the link for the device ID that you want to create an on-premises association for.
6. Choose the On-premises associations tab.
7. Choose Associate.
8. Choose the on-premises Customer gateway.
9. (Optional) Choose the Link used for the connection.
10. Choose Create on-premises association.
The link is available to use immediately.
To disassociate an on-premises association
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices.
5. Choose the device ID link.
6. Choose the On-premises association tab.
7. Choose the check box for the on-premises association that you want to disassociate.
8. Choose Disassociate.
Disassociation occurs immediately.
View device details 52
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Associate or disassociate a Connect peer using AWS Network Manager
Associate or disassociate a Connect peer device link association in your AWS global network.
You can only associate one link with a Connect peer. If a link is already associated with a Connect 
peer, and you want to use that link with another Connect peer, you must ﬁrst disassociate the link 
the Connect peer it's associated with.
To create a Connect peer association
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices.
5. Choose the link for the device ID that you want to create an on-premises association for.
6. Choose the Connect peer tab.
7. Choose Associate.
8. Choose the on-premises Connect peer.
9. (Optional) Choose the Link used for the connection.
10. Choose Create Connect peer association.
The link is available to use immediately.
To disassociate a Connect peer association
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices.
5. Choose the device ID link.
6. Choose the Connect peer tab.
7. Choose the check box for the Connect peer that you want to disassociate.
View device details 53
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
8. Choose Disassociate.
Disassociation occurs immediately.
View VPNs using AWS Network Manager
The VPNs page displays a list of your VPN connections for a device.
To view device VPN connections
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices.
5. Choose the device that you want to view the VPN connections for.
6. Choose VPNs.
Monitor devices using AWS Network Manager
Monitor device Amazon CloudWatch events on the Network Manager Monitoring page.
To monitor devices
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices.
5. Choose the Monitoring tab.
6. The Monitoring page displays data for the following:
• Data In
• Data Out
• Tunnel down count Average
View device details 54
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
(Optional) Metrics and events use the default time set up in the CloudWatch Events event. To 
set a custom time frame, choose Custom and then choose a Relative or Absolute time, and 
then choose if you want to see that date range in UTC or the edge location's Local time zone.
Choose Add to dashboard to add this metric to your CloudWatch dashboard. For more 
information about using CloudWatch dashboards, see Using Amazon CloudWatch Dashboards
in the Amazon CloudWatch User Guide.
Note
The Add to dashboard option only works if your registered transit gateway is in the US 
West (Oregon) Region.
Connections in AWS Global Networks for Transit Gateways
Create a connection between two devices in your global network using AWS Network Manager. The 
connection can be between a physical or virtual appliance and a third-party appliance in a VPC, or 
between physical appliances in an on-premises network. To create a connection the device must 
ﬁrst be added to your global network. For the steps to add a device, see the section called “Add a 
device”. You can also use an optional link to create the connection. For the steps to create a link, 
see the section called “Add a link”.
A connection is created for a speciﬁc global network and cannot be shared with other global 
networks.
Tasks
• Create a connection using AWS Network Manager
• Update a connection using AWS Network Manager
• Delete a connection using AWS Network Manager
Create a connection using AWS Network Manager
Create a connection between two existing devices in your global network.
Connections 55
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
To create a connection
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices, and choose the ID of the device.
5. Choose Connections, and then choose Create connection.
6. For Name and Description, enter a name and description for the connection.
7. (Optional) For Link, choose a link to associate with the ﬁrst device in the connection.
8. For Connected device, choose the ID of the second device in the connection.
9. (Optional) For Connected link, choose a link to associate with the second device in the 
connection.
10. Choose Create connection.
To create a connection using the AWS CLI
Use the create-connection command.
Update a connection using AWS Network Manager
You can update the information for an existing connection.
To update a connection
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices, and select the device.
5. Choose Connections, and select the connection.
6. Choose Edit.
7. Update the connection details as needed, and then choose Edit connection.
To update a connection using the AWS CLI
Update a connection 56
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Use the update-connection command.
Delete a connection using AWS Network Manager
If you no longer need a connection, you can delete it.
To delete a connection
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices, and select the device.
5. Choose Connections, and select the connection.
6. Choose Delete.
7. When prompted for conﬁrmation, choose Delete.
To delete a connection using the AWS CLI
Use the delete-connection command.
Gateway associations in AWS Global Networks for Transit 
Gateways
Create a customer gateway association with either a device or with a transit gateway Connect peer.
Customer gateway associations
To add your on-premises network to your global network, you associate a customer gateway 
with your device, and optionally, a link. The customer gateway must already be in your global 
network as part of a VPN attachment in your transit gateway. If you specify a link, it must already 
be associated with the speciﬁed device.
For more information about creating a customer gateway, see Create a Customer Gateway in the
AWS Site-to-Site VPN User Guide. For more information about creating a VPN attachment to a 
transit gateway, see Transit Gateway VPN Attachments in Amazon VPC Transit Gateways.
Delete a connection 57
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
For more information about viewing the topology of your on-premises network in Network 
Manager, see the section called “Access transit gateway network dashboards” />.
Transit Gateway Connect peer associations
You can associate a Connect peer (in a transit gateway Connect attachment) with a device, and 
optionally, with a link.
If you specify a link, it must be associated with the speciﬁed device.
Topics
• Associate a customer gateway using AWS Network Manager
• Disassociate a customer gateway using AWS Network Manager
• Add a Connect peer association using AWS Network Manager
• Disassociate a Connect peer using AWS Network Manager
Associate a customer gateway using AWS Network Manager
You can associate a customer gateway with a device and link using the Network Manager console 
on either of the following pages:
• On the Transit gateways page
• On the Devices page
Transit gateways page
To associate a customer gateway using the Transit gateways page
1. Access the Network Manager console at https://console.aws.amazon.com/
networkmanager/home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit gateways, and then choose the ID of your transit 
gateway.
5. Choose On-premises associations.
Transit Gateway Connect peer associations 58
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
6. Select your customer gateway and choose Associate.
7. For Device, select the ID of the device to associate. For Link, select the ID of the link to 
associate.
8. Choose Edit on-premises association.
Devices page
To associate a customer gateway using the Devices page
1. Access the Network Manager console at https://console.aws.amazon.com/
networkmanager/home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices, and then choose the ID of your device.
5. Choose On-premises associations.
6. Choose Associate.
7. For Customer gateway, select the ID of the customer gateway to associate. For Link, select 
the ID of the link to associate.
8. Choose Create on-premises association.
Create a customer gateway association using the AWS CLI
You can view and create a customer gateway association using the following commands.
• To associate a customer gateway with a device and link: associate-customer-gateway
• To view your customer gateway associations: get-customer-gateway-associations
Disassociate a customer gateway using AWS Network Manager
You can disassociate a customer gateway from a device or link using the Network Manager console 
on either of the following pages:
• On the Transit gateways page
• On the Devices page
Disassociate a customer gateway association from a device 59
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Transit gateways page
To disassociate a customer gateway using the Transit gateways page
1. Access the Network Manager console at https://console.aws.amazon.com/
networkmanager/home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit gateways, and then choose On-premises 
associations.
5. Select your customer gateway and choose Disassociate.
Devices page
To disassociate a customer gateway using the Devices page
1. Access the Network Manager console at https://console.aws.amazon.com/
networkmanager/home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices, and then choose the ID of your device.
5. Choose On-premises associations.
6. Select your customer gateway and choose Disassociate.
Disassociate a customer gateway association using the AWS CLI
You can view and disassociate a customer gateway association using the following command.
• To view your customer gateway associations: get-customer-gateway-associations
• To disassociate a customer gateway from a device and link: disassociate-customer-gateway
Add a Connect peer association using AWS Network Manager
Create a transit gateway Connect peer association using the Network Manager console on either of 
the following pages:
Add a Connect peer association 60
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• On the Transit gateways page
• On the Devices page
Transit gateways page
To associate a Connect peer using the Transit gateways page
1. Access the Network Manager console at https://console.aws.amazon.com/
networkmanager/home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit gateways, and then choose the ID of your transit 
gateway.
5. Choose Connect peer associations.
6. Select the Connect peer and choose Edit.
7. For Device, select the ID of the device to associate. For Link, select the ID of the link to 
associate.
8. Choose Edit Connect peer association.
Devices page
To associate a Connect peer using the Devices page
1. Access the Network Manager console at https://console.aws.amazon.com/
networkmanager/home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices, and choose the ID of the device.
5. Choose Connect peer associations.
6. Choose Associate.
7. For Connect peer, choose the Connect peer.
8. (Optional) For Link, choose the link for the Connect peer association.
9. Choose Create Connect peer association.
Add a Connect peer association 61
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Working with Connect peer associations using the AWS CLI
You can view and create Connect peer associations using the following commands.
• To associate a Connect peer with a device: associate-transit-gateway-connect-peer
• To view your Connect peer associations: get-transit-gateway-connect-peer-associations
Disassociate a Connect peer using AWS Network Manager
You can disassociate a Connect peer from a device in one of the following ways:
• On the Transit gateways page
• On the Devices page
Transit gateways page
To disassociate a Connect peer using the Transit gateways page
1. Access the Network Manager console at https://console.aws.amazon.com/
networkmanager/home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit gateways, and then choose Connect peer 
associations.
5. Select the Connect peer and choose Disassociate.
Devices page
To disassociate a Connect peer using the Devices page
1. Access the Network Manager console at https://console.aws.amazon.com/
networkmanager/home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Devices, and then choose the ID of your device.
5. Choose Connect peer associations.
Disassociate a Connect peer from a device 62
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
6. Select the Connect peer and choose Disassociate.
Working with Connect peer associations using the AWS CLI
You can view and disassociate Connect peer associations using the following commands.
• To view your Connect peer associations: get-transit-gateway-connect-peer-associations
• To disassociate a Connect peer from a device: disassociate-transit-gateway-connect-peer
Resource tags in AWS Global Networks for Transit Gateways
A tag is a metadata label that either you or AWS assigns to an AWS resource. Each tag consists of a
key and a value. For tags that you assign, you deﬁne the key and the value. For example, you might 
deﬁne the key as purpose and the value as test for one resource.
Tags help you do the following:
• Identify and organize your AWS resources. Many AWS services support tagging, so you can assign 
the same tag to resources from diﬀerent services to indicate that the resources are related.
• Control access to your AWS resources. For more information, see Controlling access to AWS 
resources using tags in the IAM User Guide.
Supported resources
The following global networks resources support tagging:
• Global networks
• Devices
• Sites
• Links
Tagging restrictions
The following basic restrictions apply to tags on global networks resources:
• Maximum number of tags that you can assign to a resource: 200
Resource tags 63
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• Maximum key length: 128 Unicode characters
• Maximum value length: 256 Unicode characters
• Valid characters for key and value: a-z, A-Z, 0-9, space, and the following characters: _ . : / = + - 
and @
• Keys and values are case sensitive
• You cannot use aws: as a preﬁx for keys; it's reserved for AWS use
Tagging restrictions 64
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
AWS Global Networks for Transit Gateways dashboards
The AWS Network Manager console uses dashboard visualizations to help you view and monitor all 
aspects of your transit gateway networks and transit gateways. Some of the dashboards include:
• World maps that pinpoint where your network resources, such as edge locations, devices, and 
attachments, are located.
• Monitoring that uses CloudWatch to track 15-months' worth of statistics, giving you a better 
perspective on how your networks are performing.
• Event tracking that streams real-time events to an events dashboard.
• Topological and logical diagrams of your transit gateway networks and transit gateways.
There are separate dashboards for your transit gateway networks and transit gateways.
Topics
• Access transit gateway network dashboards using AWS Network Manager
• Access transit gateway dashboards using AWS Network Manager
Access transit gateway network dashboards using AWS 
Network Manager
he AWS Network Manager console provides a group of dashboards for AWS Global Networks for 
Transit Gateways, allowing you to view and monitor your network of transit gateways. Dashboards 
include information about network resources, their geographic locations, the network topology, 
and the logical network associations. If you want to view the dashboards for a speciﬁc transit 
gateway, see the section called “Access transit gateway dashboards”.
Topics
• Overview
• Geography
• Topology tree
• Events
• Monitoring
Access transit gateway network dashboards 65
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• Route analyzer
Overview
The Overview page displays details about your transit gateway network, the VPN status, the 
Connect peer status, and any network events aﬀecting your transit gateways.
To access transit gateway network details
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway network.
5. The Overview page opens by default, showing information about your transit gateways.
6. On the Overview page you contains the following information:
• Your transit gateway network Inventory:
IconDescription
Transit gateways
The total number of registered transit gateways in your global network. Choose the 
link to open the Transit gateways page to view more information about your transit 
gateways.
Sites
The total number of sites associated with your transit gateways. Choose the link to open 
the Sites page to view more information about your transit gateway sites.
Devices
The total number of devices associated with your transit gateways. Choose the link to 
open the Devices page to view more information about your transit gateway devices.
Overview 66
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• The Transit gateways VPN status. The following is displayed:
• ID – The ID of the transit gateway. Choose the link to open details about the transit 
gateway.
• Name – Name of the transit gateway.
• Region – Region where the transit gateway is located
• Down VPN – The percentage of your total transit gateway VPNs that are down.
• Impaired VPN –The percentage of your total VPNs that are impaired.
• Up VPN – The percentage of your total VPNs that are up.
• The Transit gateways connect peer status. The following is displayed:
• ID – The ID of the transit gateway.
• Name – Name of the transit gateway.
• Region – Region where the transit peer is located
• Down Connect peer – The percentage of your total transit gateway Connect peers that are 
down.
• Impaired Connect peer – The percentage of your total transit gateway Connect peers that 
are impaired.
• Up VPN – The percentage of your total transit gateway Connect peers that are up.
• The Network events summary displays CloudWatch Events number of core network 
attachments per edge, shown as a stacked column chart.
(Optional) Metrics and events use the default time set up in the CloudWatch Events event. 
To set a custom time frame, choose Custom and then choose a Relative or Absolute time, 
and then choose if you want to see that date range in UTC or the edge location's Local time 
zone.
Choose Add to dashboard to add this metric to your CloudWatch dashboard. For more 
information about using CloudWatch dashboards, see Using Amazon CloudWatch 
Dashboards in the Amazon CloudWatch User Guide.
Note
The Add to dashboard option only works if your registered transit gateway is in the 
US West (Oregon) Region.
Overview 67
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Geography
The Geography page displays a world map showing the locations of your transit gateway network.
To access a geographic map of your transit gateways
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway network.
5. The Overview page opens by default, showing information about your transit gateways.
6. Choose the Geography tab.
A world map displays, showing you the locations of the following:
• AWS TGWs and VPCs.
• The Connectivity of VPNs, Direct Connects, and Connect peers.
• On-premises Sites and Devices.
• Not associated Sites and Devices.
7. In the following example, there are four AWS Regions, us-west-1 us-west-2, us-east-1, and us-
east-2. Each Region is labeled and represented by a number, indicating the number of transit 
gateways in that Region. For example, us-east-2 is represented by the number 3, indicating 
that there are three network resources associated with the us-west-2 Region.
Geography 68
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
8. If your account is a delegated administrator in a multi-account environment, you can view 
details about the transit gateways for diﬀerent accounts.
9. Choose the number representing a Region. For example, choose 3. The following information 
displays:
• The right pane shows the AWS Region, us-east-2.
• A bottom panel shows with a Transit Gateways dropdown list option, displaying each transit 
gateway in that Region. In this example, there are 3 transit gateways in us-east-2. Choose 
a transit gateway from the dropdown list to view details about that transit gateway. In this 
example, you can see that the Resource Account ID  for this transit gateway is another 
account in the multi-account environment, 98765432101.
Geography 69
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
10. To view more details about the transit gateway, choose the ID link to open the Transit 
gateway details page for the gateway.
If your global network is part of a multi-account environment, you can choose an ID from a 
member account and view details about that attachment. The Resource Account ID column 
displays the account ID that the transit gateway belongs to.
Viewing details about a member's resources prompts you to use the Network Manager console 
to switch roles to the member account where the resource is located.
Note
Switching roles logs you out of the current account and into the member account 
associated with the attachment.
Switch global networks console roles to view resource details
To view resource details in a member account
1. When choosing a link to a member account, you're prompted to switch console roles:
Geography 70
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
2. The following values populate the Switch Role screen. Keep the following values:
• Account — The account ID for the member account that the resource is associated with.
• Role — IAMRoleForAWSNetworkManagerCrossAccountResourceAccess is the 
required IAM role for accessing resources across multiple accounts.
3. Choose Switch Role.
You're logged out of your current account and into that member account. A new tab opens 
showing the details of the resource. For example, if you choose a VPC resource, the VPC 
resource page opens for the member account that owns the resource.
4. Depending on the delegated permission level assigned to the delegated administrators and 
the management account when trusted access was enabled, you can either view information 
(read-only permission) about the resource or add/modify (administrator permission) the 
resource.
5. To return to the original member account, choose one of the following:
• On your current tab, choose the browser Back button. On the Switch Role login screen, 
enter the Account ID of the account you want, and then choose Switch Role.
Geography 71
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• If you haven't closed it, choose the tab for the account you've just logged out of, and then 
choose Reload.
Topology tree
The Topology tree page shows a logical diagram of your transit gateway network.
To access the topology tree for a transit gateway network
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway network.
5. The Overview page opens by default, showing information about your transit gateways.
6. Choose the Topology tree tab.
7. By default, the Topology tree page displays all Sites, Devices, and Customer Gateways of 
your transit gateway and the logical relationships between them. You can ﬁlter the network 
tree to show speciﬁc resources types only to view information about the speciﬁc resource it 
represents. The line colors represent the state of the relationships between AWS and the on-
premises resources.
The following example shows the topology tree for two edge locations, us-west-1 and us-
east-1.
Topology tree 72
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
8. In the Topology tree, choose an attachment. The attachment details display in the left pane.
9. If your global network is part of a multi-account environment, you can choose a Resource ID
from a member account and view details about that attachment.
Viewing details about a member's resources prompts you to switch Network Manager console 
roles to the member account where the resource is located.
Note
Switching roles logs you out of the current account and into the delegated 
administrator account associated with the attachment.
Topology tree 73
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Switch global networks console roles to view resource details
To view resource details in a member account
1. When choosing a link to a member account, you're prompted to switch console roles:
2. The following values populate the Switch Role screen. Keep the following values:
• Account — The account ID for the member account that the resource is associated with.
• Role — IAMRoleForAWSNetworkManagerCrossAccountResourceAccess is the 
required IAM role for accessing resources across multiple accounts.
3. Choose Switch Role.
You're logged out of your current account and into that member account. A new tab opens 
showing the details of the resource. For example, if you choose a VPC resource, the VPC 
resource page opens for the member account that owns the resource.
4. Depending on the delegated permission level assigned to the delegated administrators and 
the management account when trusted access was enabled, you can either view information 
(read-only permission) about the resource or add/modify (administrator permission) the 
resource.
5. To return to the original member account, choose one of the following:
Topology tree 74
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• On your current tab, choose the browser Back button. On the Switch Role login screen, 
enter the Account ID of the account you want, and then choose Switch Role.
• If you haven't closed it, choose the tab for the account you've just logged out of, and then 
choose Reload.
Events
Track your transit gateway events using Amazon EventBridge that delivers a near-real-time stream 
of system events that describe changes in your resources. Using simple rules that you can quickly 
set up, you can match events and route them to one or more target functions or streams. For more 
information, see the Amazon EventBridge User Guide.
To access transit gateway network events
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway network.
5. The Overview page opens by default, showing information about your transit gateways.
6. Choose the Events tab.
The Events section updates with the events that occurred during the time frame.
(Optional) Metrics and events use the default time set up in the CloudWatch Events event. To 
set a custom time frame, choose Custom and then choose a Relative or Absolute time, and 
then choose if you want to see that date range in UTC or the edge location's Local time zone.
Choose Add to dashboard to add this metric to your CloudWatch dashboard. For more 
information about using CloudWatch dashboards, see Using Amazon CloudWatch Dashboards
in the Amazon CloudWatch User Guide.
Note
The Add to dashboard option only works if your registered transit gateway is in the US 
West (Oregon) Region.
Events 75
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Monitoring
You can monitor your transit gateways using Amazon CloudWatch which collects raw data and 
processes it into readable, near-real-time metrics. These statistics are kept for 15 months, so 
that you can access historical information and gain a better perspective on how your network is 
performing. You can also set alarms that watch for certain thresholds, and send notiﬁcations or 
take actions when those thresholds are met. For more information, see the Amazon CloudWatch 
User Guide.
On the monitoring page you can view usage metrics for your transit gateways, ﬁltering by speciﬁc 
transit gateways.
To access transit gateway network monitoring details
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway network.
5. The Overview page opens by default, showing information about your transit gateways.
6. Choose the Monitoring tab.
7. Choose a transit gateway that you want to monitor.
If you're using an account that's set up as a delegated administrator between accounts, you can 
choose a transit gateway from one of those other accounts. The transit gateway list displays 
the ID, the Region, and the account ID.
8. (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To 
set a custom time frame, choose Custom and then choose a Relative or Absolute time, and 
then choose if you want to see that date range in UTC or the edge location's Local time zone.
Choose Add to dashboard to add this metric to your CloudWatch dashboard. For more 
information about using CloudWatch dashboards, see Using Amazon CloudWatch Dashboards
in the Amazon CloudWatch User Guide.
Monitoring 76
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Note
The Add to dashboard option only works if your registered transit gateway is in the US 
West (Oregon) Region.
9. The page updates the following transit gateway monitors:
• Bytes in
• Bytes out
• Bytes dropped – black hole
• Bytes dropped – no route
• Packets in
• Packets out
• Packets dropped – black hole
• Packets dropped – no route
10. (Optional) Choose Add to dashboard to add this metric to your CloudWatch dashboard. 
For more information about using CloudWatch dashboards, see Using Amazon CloudWatch 
Dashboards in the Amazon CloudWatchUser Guide.
Note
The Add to dashboard option only works if your registered transit gateway is in the US 
West (Oregon) Region.
Route analyzer
The Route Analyzer analyzes the routing path between a speciﬁed source and destination.
Note
Route Analyzer checks the routes on Transit Gateway route tables only
Route analyzer 77
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
To analyze transit gateway routes
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway network.
5. The Overview page opens by default, showing information about your transit gateways.
6. Choose the Route Analyzer tab.
7. In the Source section,
• Choose the source Transit Gateway for the route that you want to analyze.
If you're logged on to an account that's set up as a delegated administrator between 
accounts, you can choose a transit gateway from one of those other accounts. The transit 
gateway list displays the ID, the Region, and the account ID.
• Choose the source Transit Gateway attachment for the route.
• Enter either the IPv4 or IPv6 IP address.
• Clear the Include return path in results check box if you don't want . This is chosen by 
default.
• Choose if this is a Middlebox appliance. For more information on middlebox conﬁgurations, 
see Route analysis with a middlebox conﬁguration.
8. In the Destination section,
• Choose the destination Transit Gateway.
If you're logged on to an account that's set up as a delegated administrator between 
accounts, you can choose a transit gateway from one of those other accounts. The transit 
gateway list displays the ID, the Region, and the account ID.
• Choose the destination Transit Gateway attachment for the route.
• Enter either the IPv4 or IPv6 IP address.
9. Choose Run route analysis.
10. The Results of route analysis return the Source and Destination transit gateways and the 
current Status. An error message is returned if no information is found in the transit gateway 
route table. For more information on route tables, see Transit gateway route tables.
Route analyzer 78
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Access transit gateway dashboards using AWS Network 
Manager
The AWS Network Manager console provides a group of dashboards for AWS Global Networks for 
Transit Gateways, allowing you to view and monitor your transit gateways. Dashboards include 
information about network resources, their geographic locations, the network topology, and the 
logical network associations. If you want to view the dashboards for all transit gateways in your 
global network, see the section called “Access transit gateway network dashboards”.
Topics
• Overview
• Topology tree
• Events
• Monitoring
• On-premises associations
• Connect peer associations
Overview
To access the transit gateway resource inventory
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway networks.
5. The Transit gateways page opens, showing a list of your transit gateways.
6. Choose the ID of the transit gateway you want to see more information about.
7. On the Overview page you can view the following information:
• Your transit gateway details.
• The transit gateway attachments, along with information about each of those attachments.
Use the following legend to understand the icons on this page:
Access transit gateway dashboards 79
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
IconDescription
VPC
The total number of VPC attachments in your transit gateway network.
VPN
The total number of VPN attachments in your transit gateway.
Direct Connect Gateway
The total number of Direct Connect gateways attached to your transit gateway.
Connect
The total number of Connect peer attachments in your transit gateway.
Transit Gateway
The total number of Transit Gateways.
8. The Details section shows information about your global network: the transit gateway ID, its
Name, the Region where it's located, and the current State of the gateway.
Note
To see details about a diﬀerent transit gateway, choose the dropdown list and then 
choose the transit gateway.
9. The Transit Gateway attachment section displays details about your attachments: the Transit 
Gateway ID, the Resource ID, and the Resource Type.
10. The VPNs section displays details about your VPN attachments: the VPN ID, the Device using 
the VPN attachment, and any Link associated with the attachment.
11. The Connect peers section displays details about your Connect peer attachments: the name of 
the Connect peer and the Device using that Connect peer.
12. The Network events summary  section shows the network events for that transit gateway. You 
must ﬁrst onboard to see network events. Choose Onboard CloudWatch Insights to enable 
viewing network events.
Overview 80
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
13. (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To 
set a custom time frame, choose Custom and then choose a Relative or Absolute time, and 
then choose if you want to see that date range in UTC or the edge location's Local time zone.
Choose Add to dashboard to add this metric to your CloudWatch dashboard. For more 
information about using CloudWatch dashboards, see Using Amazon CloudWatch Dashboards
in the Amazon CloudWatch User Guide.
Note
The Add to dashboard option only works if your registered transit gateway is in the US 
West (Oregon) Region.
Topology tree
The Topology tree page shows a logical diagram of your transit gateways.
To view a transit gateway topology tree
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway networks.
5. The Transit gateways page opens, showing a list of your transit gateways.
6. Choose the ID of the transit gateway you want to see more information about.
7. Choose the Topology tree tab.
8. By default, the Topology tree page displays all Sites, Devices, and Customer Gateways of 
your transit gateway and the logical relationships between them. You can ﬁlter the network 
tree to show speciﬁc resources types only to view information about the speciﬁc resource it 
represents. The line colors represent the state of the relationships between AWS and the on-
premises resources.
9. In the Topology tree, choose a resource. The resource details display in the right pane.
10. If your global network is part of a multi-account environment, you can choose a Resource ID
from a member account and view details about that attachment.
Topology tree 81
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Viewing details about a member's resources prompts you to switch Network Manager console 
roles to the member account where the resource is located.
Note
Switching roles logs you out of the current account and into the delegated 
administrator account associated with the attachment.
Switch global networks console roles to view resource details
To view resource details in a member account
1. When choosing a link to a member account, you're prompted to switch console roles:
2. The following values populate the Switch Role screen. Keep the following values:
• Account — The account ID for the member account that the resource is associated with.
• Role — IAMRoleForAWSNetworkManagerCrossAccountResourceAccess is the 
required IAM role for accessing resources across multiple accounts.
Topology tree 82
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
3. Choose Switch Role.
You're logged out of your current account and into that member account. A new tab opens 
showing the details of the resource. For example, if you choose a VPC resource, the VPC 
resource page opens for the member account that owns the resource.
4. Depending on the delegated permission level assigned to the delegated administrators and 
the management account when trusted access was enabled, you can either view information 
(read-only permission) about the resource or add/modify (administrator permission) the 
resource.
5. To return to the original member account, choose one of the following:
• On your current tab, choose the browser Back button. On the Switch Role login screen, 
enter the Account ID of the account you want, and then choose Switch Role.
• If you haven't closed it, choose the tab for the account you've just logged out of, and then 
choose Reload.
Events
Track your transit gateway events using Amazon EventBridge that delivers a near-real-time stream 
of system events that describe changes in your resources. Using simple rules that you can quickly 
set up, you can match events and route them to one or more target functions or streams. For more 
information, see the Amazon EventBridge User Guide.
To track transit gateway events
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway network.
5. The Overview page opens by default, showing information about your transit gateways.
6. Choose the Events tab.
The Events section updates with the events that occurred during the time frame.
Events 83
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
(Optional) Metrics and events use the default time set up in the CloudWatch Events event. To 
set a custom time frame, choose Custom and then choose a Relative or Absolute time, and 
then choose if you want to see that date range in UTC or the edge location's Local time zone.
Choose Add to dashboard to add this metric to your CloudWatch dashboard. For more 
information about using CloudWatch dashboards, see Using Amazon CloudWatch Dashboards
in the Amazon CloudWatch User Guide.
Note
The Add to dashboard option only works if your registered transit gateway is in the US 
West (Oregon) Region.
Monitoring
You can monitor your transit gateways using Amazon CloudWatch, which collects raw data and 
processes it into readable, near-real-time metrics. These statistics are kept for 15 months, so 
that you can access historical information and gain a better perspective on how your network is 
performing. You can also set alarms that watch for certain thresholds, and send notiﬁcations or 
take actions when those thresholds are met. For more information, see the Amazon CloudWatch 
User Guide.
On the monitoring page you can view usage metrics for your transit gateways, ﬁltering by speciﬁc 
transit gateways.
To view transit monitoring details
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway networks.
5. The Transit gateways page opens, showing a list of your transit gateways.
6. Choose the ID of the transit gateway you want to see more information about.
7. Choose the Monitoring tab.
Monitoring 84
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
8. If you want to choose a diﬀerent transit gateway to monitor, choose that transit gateway from 
the list.
9. (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To 
set a custom time frame, choose Custom and then choose a Relative or Absolute time, and 
then choose if you want to see that date range in UTC or the edge location's Local time zone.
Choose Add to dashboard to add this metric to your CloudWatch dashboard. For more 
information about using CloudWatch dashboards, see Using Amazon CloudWatch Dashboards
in the Amazon CloudWatch User Guide.
Note
The Add to dashboard option only works if your registered transit gateway is in the US 
West (Oregon) Region.
10. The page updates the following transit gateway monitors:
• Bytes in
• Bytes out
• Bytes dropped – black hole
• Bytes dropped – no route
• Packets in
• Packets out
• Packets dropped – black hole
• Packets dropped – no route
11. (Optional) Choose Add to dashboard to add this metric to your CloudWatch dashboard. 
For more information about using CloudWatch dashboards, see Using Amazon CloudWatch 
Dashboards in the Amazon CloudWatchUser Guide.
Note
The Add to dashboard option only works if your registered transit gateway is in the US 
West (Oregon) Region.
Monitoring 85
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
On-premises associations
The On-premises page displays information about your on-premises devices for this transit 
gateway. On this page you can associate or disassociate any of your devices..
To view on-premises associations
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway networks.
5. The Transit gateways page opens, showing a list of your transit gateways.
6. Choose the ID of the transit gateway you want to see more information about.
7. Choose the On-premises associations tab.
8. The Transit Gateway on-premises association page displays the Customer gateway, Device,
Link, and State of the transit gateway.
To associate a device
1. Choose the Customer gateway you want to associate a device with.
2. Choose Associate.
3. On the Edit on-premises association page, choose the Device and optional Link for the 
association.
4. Choose Edit on-premises association.
To disassociate an on-premises device
1. Choose the Customer gateway you want to disassociate.
2. Choose Disassociate.
Connect peer associations
The Connect peer associations page displays information about your Connect peers for this transit 
gateway. You can also disassociate any of your devices.
On-premises associations 86
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
To access Connect peer associations
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway networks.
5. The Transit gateways page opens, showing a list of your transit gateways.
6. Choose the ID of the transit gateway you want to see more information about.
7. Choose the Connect peer associations tab.
8. The Connect peer associations page displays the Connect peer, Device, Link, and State of the 
transit gateway.
To disassociate a Connect peer device
1. Choose the Connect peer you want to disassociate.
2. Choose Disassociate.
Connect peer associations 87
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Route Analyzer for AWS Network Manager
With AWS Global Networks for Transit Gateways, you can use the Route Analyzer to perform 
an analysis of the routes in your transit gateway route tables. Through AWS Network Manager, 
Route Analyzer analyzes the routing path between a speciﬁed source and destination, and returns 
information about the connectivity between components. You can use the Route Analyzer to do 
the following:
• Verify that the transit gateway route table conﬁguration will work as expected before you start 
sending traﬃc.
• Validate your existing route conﬁguration.
• Diagnose route-related issues that are causing traﬃc disruption in your global network.
Note
Route Analyzer does not work with intra-Region peering.
Topics
• Route Analyzer basics
• Perform a route analysis
• Example: Route analysis for peered transit gateways
• Example: Route analysis with a middlebox conﬁguration
Route Analyzer basics
To use the Route Analyzer, you indicate the path for the traﬃc from a source to a destination. 
For the source, you specify the transit gateway, the transit gateway attachment from which the 
traﬃc originates, and a source IPv4 or IPv6 address. The Route Analyzer analyzes the routes in the 
associated transit gateway route table for the transit gateway attachment. For the destination, 
you specify a target IPv4 or IPv6 address, and the destination transit gateway and transit gateway 
attachment.
If you've conﬁgured a middlebox appliance in your VPC, you can indicate the location of the 
appliance in the route analysis. This enables you to specify multiple network hops in a route 
Route Analyzer basics 88
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
between a source and destination, to help you analyze the route of the traﬃc. We store this 
information for use in future analyses. You can update your middlebox appliances later on as 
needed.
You can also analyze the return path for traﬃc from the speciﬁed destination back to the source.
The following rules apply when using the Route Analyzer:
• The Route Analyzer analyzes routes in transit gateway route tables only. It does not analyze 
routes in VPC route tables or in your customer gateway devices.
• The transit gateways must be registered in your global network.
• The Route Analyzer does not analyze security group rules or network ACL rules. To capture 
information about accepted and rejected IP traﬃc in your VPC, you can use VPC ﬂow logs.
• The Route Analyzer only returns information for the return path if it can successfully return 
information for the forward path.
Perform a route analysis
Perform a route analysis of your AWS global network. You can only use Route Analyzer using the 
AWS Global Networks for Transit Gateways console.
To analyze your routes
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit Gateway network.
5. The Overview page opens by default, showing information about your transit gateways.
6. Choose the Route Analyzer tab.
7. Under Source, do the following:
• Choose the transit gateway and the transit gateway attachment.
• For IP address, enter a source IPv4 or IPv6 address.
8. Under Destination, do the following:
• Choose the transit gateway and the transit gateway attachment.
Perform a route analysis 89
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• For IP address, enter a target IPv4 or IPv6 address.
9. (Optional) To analyze the return path, ensure that you enable Include return path in results. If 
enabled, you must specify an IP address under Source.
10. To specify middlebox appliances in the routing path, choose Middlebox appliance?. We store 
this information for use in future analyses. You can update your middlebox appliances later on 
as needed.
11. Choose Run route analysis.
12. The results are displayed under Results of route analysis. If you speciﬁed Middlebox 
appliance?, choose Yes or No for each of the attachments to indicate the location of the 
appliances and to complete the route analysis.
You can choose the ID of any of the resources in the path to view more information about the 
resources.
Example: Route analysis for peered transit gateways
In the following example, transit gateway 1 has two VPC attachments, and a peering attachment 
to transit gateway 2. Transit gateway 2 has a Site-to-Site VPN attachment to your on-premises 
network. You want to use the Route Analyzer to ensure that the VPCs and Site-to-Site VPN 
connections can route traﬃc to each other through the transit gateways.
In the Route Analyzer, do the following:
1. Under Source, specify transit gateway 1 and the transit gateway attachment for VPC A. Specify 
an IP address from the CIDR block of VPC A, for example, 10.0.0.7.
2. Under Destination, specify transit gateway 2 and the VPN attachment. Specify an IP address 
from the range of the on-premises network, for example, 172.31.0.8.
3. Ensure that Include return path in results is selected.
Example: Route analysis for peered transit gateways 90
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
4. Run the route analysis. In the results, verify the path between the source and destination. For 
example, the following results indicate that there is a forward path from transit gateway 1 to 
transit gateway 2, but no return path. Check the route table for transit gateway 2, and ensure 
that there is a static route that points to the peering attachment.
5. To run the analysis between VPC B and the VPN connection, modify the information under
Source. Choose the transit gateway attachment for VPC B, and specify an IP address from the 
CIDR block of VPC B, for example, 10.2.0.9.
6. Reload the results and verify the path between the source and destination.
For more information about the routing conﬁguration for this scenario, see the transit gateway 
peering example.
Example: Route analysis with a middlebox conﬁguration
If you've conﬁgured a VPC to act as a middlebox appliance for inspecting traﬃc that ﬂows to 
other parts of your network, you can indicate the location of the appliance in the route analysis. 
In the following example, the transit gateway has two VPC attachments and a VPN attachment. 
VPC A runs a ﬁrewall appliance (middlebox) that inspects the traﬃc that ﬂows between the VPN 
connection and VPC B.
Example: Route analysis with a middlebox conﬁguration 91
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
In the Route Analyzer, you can specify the location of the middlebox appliance as follows:
1. Under Source, specify the transit gateway and the VPN attachment. Specify an IP address from 
the range of the on-premises network, for example, 10.0.0.7.
2. Under Destination, specify the transit gateway and the attachment for VPC B. Specify an IP 
address from the CIDR block of VPC B, for example, 172.31.0.8.
3. For Middlebox appliance?, choose Include.
4. Run the route analysis.
5. For the Middlebox appliance? sections for the transit gateway attachment for VPC A, choose
Yes.
You can choose the ID of any resource in the path to view more information about that resource.
Example: Route analysis with a middlebox conﬁguration 92
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Example: Route analysis with a middlebox conﬁguration 93
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Amazon CloudWatch metrics and events
AWS provides the following monitoring tools to watch the resources in your global network, report 
when something is wrong, and take automatic actions when appropriate.
• Amazon CloudWatch monitors your AWS resources and the applications that you run on AWS in 
real time. You can collect and track metrics, create customized dashboards, and set alarms that 
notify you or take actions when a speciﬁed metric reaches a threshold that you specify. For more 
information, see the Amazon CloudWatch User Guide.
• Amazon EventBridge delivers a near-real-time stream of system events that describe changes in 
AWS resources. EventBridge enables automated event-driven computing, as you can write rules 
that watch for certain events and trigger automated actions in other AWS services when these 
events happen. For more information, see the Amazon EventBridge User Guide.
• AWS CloudTrail provides a record of actions taken by a user, role, or an AWS services in your 
global network, capturing all API calls for global network events.
Topics
• Monitor your global network with Amazon CloudWatch metrics
• Monitor your global network using EventBridge
• Log AWS Global Networks for Transit Gateways API calls using AWS CloudTrail
Monitor your global network with Amazon CloudWatch metrics
You can monitor AWS Global Networks for Transit Gateways using Amazon CloudWatch, which 
collects raw data and processes it into readable, near-real-time metrics. These statistics are kept for 
15 months, so that you can access historical information and gain a better perspective on how your 
web application or service is performing. You can also set alarms that watch for certain thresholds, 
and send notiﬁcations or take actions when those thresholds are met. For more information, see 
the Amazon CloudWatch User Guide.
You can view CloudWatch metrics in your global network for your registered transited gateways, 
your associated Site-to-Site VPN connections, and your on-premises resources. You can view 
metrics per transit gateway and per transit gateway attachment, per global network.
For more information about the supported metrics, see the following topics:
Monitor with CloudWatch metrics 94
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• CloudWatch metrics for your transit gateways
• Monitor VPN tunnels using Amazon CloudWatch
• View CloudWatch metrics for on-premises resources
For examples of creating alarms, see Creating Amazon CloudWatch Alarms in the Amazon 
CloudWatch User Guide.
View CloudWatch metrics for on-premises resources
AWS Global Networks for Transit Gateways publishes data points to Amazon CloudWatch for your 
on-premises resources, including devices and links. CloudWatch enables you to retrieve statistics 
about those data points as an ordered set of time series data, known as metrics. Each data point 
has an associated timestamp and an optional unit of measurement.
You can use metrics to verify that your system is performing as expected. For example, you can 
create a CloudWatch alarm to monitor a speciﬁed metric and initiate an action (such as sending a 
notiﬁcation to an email address) if the metric goes outside what you consider an acceptable range.
Device metrics
The AWS/NetworkManager namespace includes the following metrics for devices.
Metric Description
DataIn The number of bytes received by the device.
DataOut The number of bytes sent by the device.
TunnelDownCount The number of VPN tunnels on the device 
that have a DOWN status. Static VPN tunnels 
with a DOWN status, and BGP VPN tunnels 
with any state other than ESTABLISHED, are 
included in the count.
Metric dimensions for devices
To ﬁlter the metrics for your devices, use the following dimensions.
View CloudWatch metrics for on-premises resources 95
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Dimension Description
DeviceId Filters the metric data by the device.
Link metrics
The AWS/NetworkManager namespace includes the following metrics for links.
Metric Description
DataIn The number of bytes received by the on-
premises network using this link.
DataOut The number of bytes sent from the on-premis 
es network using this link.
Metric dimensions for links
To ﬁlter the metrics for your links, use the following dimensions.
Dimension Description
LinkId Filters the metric data by the link.
View global network CloudWatch metrics
There are various options for viewing CloudWatch metrics for your global network, including the 
following:
• Viewing metrics for the global network and ﬁltering by transit gateway
• Viewing metrics for a speciﬁc transit gateway and its attachments
To view metrics for your global network and ﬁlter by transit gateway
1. Open the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
View global network CloudWatch metrics 96
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
2. In the navigation pane, choose Global networks, and choose the ID for your global network.
3. In the navigation pane, choose Transit gateway network.
4. Choose Monitoring. On this page, you can ﬁlter by transit gateway to view metrics for that 
transit gateway.
To view metrics for a speciﬁc transit gateway and its attachments
1. Open the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. In the navigation pane, choose Global networks, and choose the ID for your global network.
3. In the navigation pane, choose Transit gateways, and choose the ID for your transit gateway.
4. (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To 
set a custom time frame, choose Custom and then choose a Relative or Absolute time, and 
then choose if you want to see that date range in UTC or the edge location's Local time zone.
Choose Add to dashboard to add this metric to your CloudWatch dashboard. For more 
information about using CloudWatch dashboards, see Using Amazon CloudWatch Dashboards
in the Amazon CloudWatch User Guide.
Note
The Add to dashboard option only works if your registered transit gateway is in the US 
West (Oregon) Region.
Monitor your global network using EventBridge
Amazon EventBridge delivers a near-real-time stream of system events that describe changes 
in your resources. Using simple rules that you can quickly set up, you can match events and 
route them to one or more target functions or streams. For more information, see the Amazon 
EventBridge User Guide.
AWS Global Networks for Transit Gateways sends the following types of events to EventBridge:
• Topology change events
• Routing update events
• Status update events
Monitor with EventBridge 97
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Get started
Before you can view events for your global network, you must onboard to CloudWatch Logs 
Insights. In the global networks console, choose the ID of your global network. In the Network 
events summary section, choose Onboard to CloudWatch Log Insights.
An IAM principal in your account, such as an IAM user, must have suﬃcient permissions to onboard 
to CloudWatch Logs Insights. Ensure that the IAM policy contains the following permissions.
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "events:PutTargets", 
                "events:DescribeRule", 
                "logs:PutResourcePolicy", 
                "logs:DescribeLogGroups", 
                "logs:DescribeResourcePolicies", 
                "events:PutRule", 
                "logs:CreateLogGroup" 
            ], 
            "Resource": "*" 
        } 
    ]
}
The preceding policy does not grant permission to create, modify, or delete Network Manager 
resources. For more information about IAM policies for working with Network Manager, see Identity 
and access management for AWS Global Networks for Transit Gateways.
When you onboard to CloudWatch Logs Insights, the following occurs:
• A CloudWatch event rule with the name DON_NOT_DELETE_networkmanager_rule is created 
in the US West (Oregon) Region.
• A CloudWatch Logs log group with the name /aws/events/networkmanagerloggroup is 
created in the US West (Oregon) Region.
Get started 98
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
• The CloudWatch event rule is conﬁgured with the CloudWatch Logs log group as a target.
• A CloudWatch resource policy with the name
DO_NOT_DELETE_networkmanager_TrustEventsToStoreLogEvents is created in the US 
West (Oregon) Region. To view this policy, use the following AWS CLI command: aws logs 
describe-resource-policies --region us-west-2
View transit gateway events using the AWS Transit Gateway console
You can view events for your global network or view a speciﬁc transit gateway using the global 
networks console.
To view global network events
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit gateway network.
5. Choose Events.
On this page you can view events for your transit gateway network. For more information 
about this page, see the section called “Events”.
To view events for a speciﬁc transit gateway
1. Access the Network Manager console at https://console.aws.amazon.com/networkmanager/
home/.
2. Under Connectivity, choose Global Networks.
3. On the Global networks page, choose the global network ID.
4. In the navigation pane, choose Transit gateways.
5. Choose the Transit gateway ID.
6. Choose Events.
On this page you can view events for your transit gateway network. For more information 
about this page, see the section called “Events”.
Get started 99
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Topology change events
Topology change events occur when there have been changes to the resources in your global 
network. These include the following:
Events
• A transit gateway in the global network was deleted (TGW-DELETED)
• A VPN connection was created for a transit gateway (VPN-CONNECTION-CREATED)
• A VPN connection was deleted on a transit gateway (VPN-CONNECTION-DELETED)
• The customer gateway for a VPN connection was changed (VPN-CONNECTION-CUSTOMER-
GATEWAY-MODIFIED)
• The target gateway for a VPN connection was changed (VPN-CONNECTION-TARGET-GATEWAY-
MODIFIED)
• A VPC was attached to a transit gateway (VPC-ATTACHMENT-CREATED)
• A VPC attachment was deleted from a transit gateway (VPC-ATTACHMENT-DELETED)
• An Direct Connect gateway was attached to a transit gateway (DXGW-ATTACHMENT-CREATED)
• An Direct Connect gateway was detached from a transit gateway (DXGW-ATTACHMENT-
DELETED)
• A transit gateway peering connection attachment was created (TGW_PEERING_CREATED)
• A transit gateway peering connection was deleted (TGW-PEERING-DELETED)
• A transit gateway Connect attachment was created for a transit gateway 
(CONNECT_ATTACHMENT_CREATED)
• A transit gateway Connect attachment was deleted for a transit gateway 
(CONNECT_ATTACHMENT_DELETED)
• A transit gateway Connect peer was created in a Connect attachment (TGW-CONNECT-PEER-
CREATED)
• A transit gateway Connect peer was deleted in a Connect attachment 
(CONNECT_PEER_DELETED)
• A Network Firewall attachment was created (NETWORK-FIREWALL-ATTACHMENT-CREATED)
• A Network Firewall attachment was deleted (NETWORK-FIREWALL-ATTACHMENT-DELETED)
Topology change events 100
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
A transit gateway in the global network was deleted (TGW-DELETED)
{"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-18T22:18:44Z",
"region":"us-west-2",
"resources":[ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
],
"detail":{ 
    "changeType":"TGW-DELETED", 
    "changeDescription":"A Transit Gateway in the global network has been deleted.", 
    "region":"us-east-1", 
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/
tgw-1234567890abcdef0"}}
A VPN connection was created for a transit gateway (VPN-CONNECTION-
CREATED)
{
"version":"0",
"id":"7636f496-ba9f-b1cc-22a6-8c90bbca8540",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-18T19:52:42Z",
"region":"us-west-2",
"resources":[ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-01c3c3738ab9f83c5"
],
"detail":{ 
    "changeType":"VPN-CONNECTION-CREATED", 
    "changeDescription":"A Site-to-Site VPN connection has been created.", 
    "region":"us-east-1", 
Topology change events 101
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
    "transitGatewayAttachmentArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway-
attachment/tgw-attach-1234567890abcdef0", 
    "vpnConnectionArn":"arn:aws:ec2:us-east-1:123456789012:vpn-connection/
vpn-1234567890abcdef0", 
    "customerGatewayArn":"arn:aws:ec2:us-east-1:123456789012:customer-gateway/
cgw-1234567890abcdef0", 
    "outsideIpAddresses":["54.166.146.158","3.93.214.172"], 
    "routing":"dynamic_route", 
    "accelerated":false, 
    "isPrivateVpn":false, 
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
A VPN connection was deleted on a transit gateway (VPN-CONNECTION-
DELETED)
{
"version":"0",
"id":"877fe5fd-4c95-1553-84ef-cfa271121081",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-19T19:43:12Z",
"region":"us-west-2",
"resources":[ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-1234567890abcdef0" 
    ],
"detail":{ 
    "changeType":"VPN-CONNECTION-DELETED", 
    "changeDescription":"A Site-to-Site VPN connection has been deleted.", 
    "region":"us-east-1", 
    "transitGatewayAttachmentArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway-
attachment/tgw-attach-1234567890abcdef0", 
    "vpnConnectionArn":"arn:aws:ec2:us-east-1:123456789012:vpn-connection/
vpn-1234567890abcdef0", 
    "customerGatewayArn":"arn:aws:ec2:us-east-1:123456789012:customer-gateway/
cgw-1234567890abcdef0", 
    "isPrivateVpn":false, 
Topology change events 102
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
The customer gateway for a VPN connection was changed (VPN-CONNECTION-
CUSTOMER-GATEWAY-MODIFIED)
{"version":"0",
"id":"76594f68-2b9f-7885-895e-58ece42ac48a",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012","time":"2023-06-28T19:25:12Z",
"region":"us-west-2",
"resources":[ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-0822025a9ea3dde43"
],
"detail":{ 
    "changeType":"VPN-CONNECTION-CUSTOMER-GATEWAY-MODIFIED", 
    "changeDescription":"The customer gateway of a Site-to-Site VPN connection has been 
 modified", 
    "region":"us-east-1", 
    "vpnConnectionArn":"arn:aws:ec2:us-east-1:123456789012:vpn-connection/
vpn-1234567890abcdef0", 
    "previousCustomerGatewayArn":"arn:aws:ec2:us-east-1:123456789012:customer-gateway/
cgw-1234567890abcdef0", 
    "currentCustomerGatewayArn":"arn:aws:ec2:us-east-1:123456789012:customer-gateway/
cgw-1234567890abcdef0", 
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
The target gateway for a VPN connection was changed (VPN-CONNECTION-
TARGET-GATEWAY-MODIFIED)
{"version":"0",
"id":"668a4e46-a757-3663-dc32-308c5ac5d87f",
"detail-type":"Network Manager Topology Change",
Topology change events 103
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
"source":"aws.networkmanager",
"account":"503089527312",
"time":"2023-06-27T18:27:24Z",
"region":"us-west-2",
"resources":[ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:ec2:us-east-1:123456789012:vpn-connection/vpn-1234567890abcdef0"
],
"detail":{ 
    "changeType":"VPN-CONNECTION-TARGET-GATEWAY-MODIFIED", 
    "changeDescription":"The target gateway of a Site-to-Site VPN connection has been 
 modified", 
    "region":"us-east-1", 
    "vpnConnectionArn":"arn:aws:ec2:us-east-1:123456789012:vpn-connection/
vpn-1234567890abcdef0", 
    "previousTargetGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/
tgw-1234567890abcdef0", 
    "currentTargetGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/
tgw-1234567890abcdef0", 
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
A VPC was attached to a transit gateway (VPC-ATTACHMENT-CREATED)
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-18T19:52:52Z",
"region":"us-west-2",
"resources": [ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
],
"detail":{ 
    "changeType":"VPC-ATTACHMENT-CREATED", 
    "changeDescription":"A VPC attachment has been created for a Core Network.", 
Topology change events 104
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
    "edgeLocation":"us-east-2", 
    "attachmentArn":"arn:aws:networkmanager::123456789012:attachment/
attachment-1234567890abcdef0", 
    "vpcArn":"arn:aws:ec2:us-east-2:123456789012:vpc/vpc-1234567890abcdef0", 
    "coreNetworkArn":"arn:aws:networkmanager::123456789012:core-network/core-
network-1234567890abcdef0" 
    }
}
A VPC attachment was deleted from a transit gateway (VPC-ATTACHMENT-
DELETED)
{ 
  "account": "123456789012", 
  "region": "us-west-2", 
  "detail-type": "Network Manager Topology Change", 
  "source": "aws.networkmanager", 
  "version": "0", 
  "time": "2019-06-30T23:18:50Z", 
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", 
  "resources": [ 
     "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
     "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0" 
  ], 
  "detail": { 
     "changeType": "VPC-ATTACHMENT-DELETED", 
     "changeDescription": "A VPC attachment has been deleted.", 
     "region": "us-east-1", 
     "transit-gateway-arn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway/
tgw-11111111111122222", 
     "transit-gateway-attachment-arn": "arn:aws:ec2:us-east-1:123456789012:transit-
gateway-attachment/tgw-attach-1234567890abcdef0", 
     "vpc-arn": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-1234567890abcdef0" 
  }
}
An Direct Connect gateway was attached to a transit gateway (DXGW-
ATTACHMENT-CREATED)
{
"version":"0",
Topology change events 105
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-19T18:57:29Z",
"region":"us-west-2",
"resources":[ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:ec2:us-west-1:123456789012:transit-gateway/tgw-1234567890abcdef0"], 
    "detail":{ 
        "changeType":"DXGW-ATTACHMENT-CREATED", 
        "changeDescription":"A Direct Connect Gateway attachment has been created.", 
        "region":"us-west-1", 
        "transitGatewayAttachmentArn":"arn:aws:ec2:us-west-1:123456789012:transit-
gateway-attachment/tgw-attach-1234567890abcdef0", 
        "directConnectGatewayArn":"arn:aws:directconnect::123456789012:dx-gateway/
a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", 
        "transitGatewayArn":"arn:aws:ec2:us-west-1:123456789012:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
An Direct Connect gateway was detached from a transit gateway (DXGW-
ATTACHMENT-DELETED)
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-19T19:16:23Z",
"region":"us-west-2",
"resources":[ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:ec2:us-west-1:123456789012:transit-gateway/tgw-1234567890abcdef0"
],
"detail":{ 
    "changeType":"DXGW-ATTACHMENT-DELETED", 
    "changeDescription":"A Direct Connect Gateway attachment has been deleted.", 
    "region":"us-west-1", 
Topology change events 106
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
    "transitGatewayAttachmentArn":"arn:aws:ec2:us-west-1:123456789012:transit-gateway-
attachment/tgw-attach-1234567890abcdef0", 
    "directConnectGatewayArn":"arn:aws:directconnect::123456789012:dx-gateway/
a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", 
    "transitGatewayArn":"arn:aws:ec2:us-west-1:123456789012:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
A transit gateway peering connection attachment was created 
(TGW_PEERING_CREATED)
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-18T22:28:51Z",
"region":"us-west-2",
"resources":[ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0"
],
"detail":{ 
    "changeType":"TGW_PEERING_CREATED", 
    "changeDescription":"A Transit Gateway peering has been created for a Core 
 Network.", 
    "edgeLocation":"us-east-1", 
    "peeringArn":"arn:aws:networkmanager::123456789012:peering/
peering-1234567890abcdef0", 
    "transitGatewayArn":"arn:aws:ec2:us-east-1:123456789012:transit-gateway/
tgw-1234567890abcdef0", 
    "coreNetworkArn":"arn:aws:networkmanager::123456789012:core-network/core-
network-1234567890abcdef0" 
    }
}
A transit gateway peering connection was deleted (TGW-PEERING-DELETED)
{
Topology change events 107
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"503089527312",
"time":"2023-06-27T19:55:59Z",
"region":"us-west-2",
"resources":[ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0"
],
"detail":{ 
    "changeType":"TGW-PEERING-DELETED", 
    "changeDescription":"A Transit Gateway peering attachment has been deleted.", 
    "region":"us-east-1", 
    "transitGatewayAttachmentArn":"arn:aws:ec2:us-east-1:111122223333:transit-gateway-
attachment/tgw-attach-1234567890abcdef0", 
    "peeredTransitGatewayArn":"arn:aws:ec2:us-east-1:111122223333:transit-gateway/
tgw-1234567890abcdef0", 
    "transitGatewayArn":"arn:aws:ec2:us-east-1:111122223333:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
A transit gateway Connect attachment was created for a transit gateway 
(CONNECT_ATTACHMENT_CREATED)
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2022-11-21T23:23:46Z",
"region":"us-west-2",
"resources":[ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0" 
    ],
"detail":{ 
    "changeType":"CONNECT_ATTACHMENT_CREATED", 
Topology change events 108
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
    "changeDescription":"A Connect attachment has been created for a Core Network.", 
    "edgeLocation":"us-east-1", 
    "attachmentArn":"arn:aws:networkmanager::123456789012:attachment/
attachment-1234567890abcdef0", 
    "transportAttachmentArn":"arn:aws:networkmanager::123456789012:attachment/
attachment-1234567890abcdef0", 
    "protocol":"GRE", 
    "coreNetworkArn":"arn:aws:networkmanager::123456789012:core-network/core-
network-1234567890abcdef0" 
    }
}
A transit gateway Connect attachment was deleted for a transit gateway 
(CONNECT_ATTACHMENT_DELETED)
{
"version":"0",
"id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
"detail-type":"Network Manager Topology Change",
"source":"aws.networkmanager",
"account":"123456789012",
"time":"2023-01-19T19:26:26Z",
"region":"us-west-2","resources":[ 
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws:networkmanager::123456789012:core-network/core-network-1234567890abcdef0" 
    ],
"detail":{ 
    "changeType":"CONNECT_ATTACHMENT_DELETED", 
    "changeDescription":"A Connect attachment has been deleted for a Core Network.", 
    "edgeLocation":"us-east-1", 
    "attachmentArn":"arn:aws:networkmanager::123456789012:attachment/
attachment-1234567890abcdef0", 
    "transportAttachmentArn":"arn:aws:networkmanager::123456789012:attachment/
attachment-1234567890abcdef0", 
    "coreNetworkArn":"arn:aws:networkmanager::123456789012:core-network/core-
network-1234567890abcdef0" 
    }
}
Topology change events 109
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
A transit gateway Connect peer was created in a Connect attachment (TGW-
CONNECT-PEER-CREATED)
{  
"version": "0",  
"id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",  
"detail-type": "Network Manager Topology Change",  
"source": "aws.networkmanager",  
"account": "123456789012",  
"time": "2023-06-27T17:22:45Z",  
"region": "us-west-2",  
"resources": [  
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0",  
    "arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0"  
],  
"detail": {  
    "changeType": "TGW-CONNECT-PEER-CREATED",  
    "changeDescription": "A TGW Connect Peer has been created in a Connect 
 attachment.",  
    "region": "us-east-1",  
    "transitGatewayAttachmentArn": "arn:aws:ec2:us-east-1:111122223333:transit-gateway-
attachment/tgw-attach-1234567890abcdef0",  
    "connectPeerArn": "arn:aws:ec2:us-east-1:111122223333:transit-gateway-connect-peer/
tgw-connect-peer-1234567890abcdef0",  
    "peerAddress": "10.1.2.3",  
    "transitGatewayAddress": "10.0.0.1", 111122223333 
    "transitGatewayArn": "arn:aws:ec2:us-east-1:111122223333:transit-gateway/
tgw-1234567890abcdef0"  
    }  
}
A transit gateway Connect peer was deleted in a Connect attachment 
(CONNECT_PEER_DELETED)
{ 
    "version": "0", 
    "id": "437f664b-cc6c-ccb8-b322-2c185ebe0c10", 
    "detail-type": "Network Manager Topology Change", 
    "source": "aws.networkmanager", 
    "account": "738040852526", 
    "time": "2023-11-13T20:49:34Z", 
Topology change events 110
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
    "region": "us-west-2", 
    "resources": [ 
        "arn:aws:networkmanager::738040852526:global-network/global-
network-02e49afd6fa01d0c3", 
        "arn:aws:networkmanager::738040852526:core-network/core-
network-0d6ee69cdc931f7b5" 
    ], 
    "detail": { 
        "changeType": "CONNECT_PEER_DELETED", 
        "changeDescription": "A Connect peer has been deleted in a Connect 
 attachment.", 
        "edgeLocation": "eu-west-2", 
        "attachmentArn": "arn:aws:networkmanager::738040852526:attachment/
attachment-05e447f0df042a011", 
        "connectPeerArn": "arn:aws:networkmanager::738040852526:connect-peer/connect-
peer-024b3172d38112df5", 
        "coreNetworkArn": "arn:aws:networkmanager::738040852526:core-network/core-
network-0d6ee69cdc931f7b5" 
    }
}
A Network Firewall attachment was created (NETWORK-FIREWALL-ATTACHMENT-
CREATED)
{ 
    "version": "0", 
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", 
    "detail-type": "Network Manager Topology Change", 
    "source": "aws.networkmanager", 
    "account": "123456789012", 
    "time": "2023-01-19T18:57:29Z", 
    "region": "us-west-2", 
    "resources": [ 
        "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
        "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0" 
    ], 
    "detail": { 
        "changeType": "  ", 
        "changeDescription": "A Network Firewall attachment has been created.", 
        "region": "us-east-1", 
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-east-1:123456789012:transit-
gateway-attachment/tgw-attach-1234567890abcdef0", 
Topology change events 111
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
        "resourceArns":[ 
            "arn:aws:network-firewall:us-east-1:123456789012:firewall/arn:aws:network-
firewall:us-east-1:123456789012:firewall/firewall-network-manager-event-example" 
            ], 
        "transitGatewayArn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
A Network Firewall attachment was deleted (NETWORK-FIREWALL-
ATTACHMENT-DELETED)
{ 
    "version": "0", 
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", 
    "detail-type": "Network Manager Topology Change", 
    "source": "aws.networkmanager", 
    "account": "123456789012", 
    "time": "2023-01-19T19:16:23Z", 
    "region": "us-west-2", 
    "resources": [ 
        "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
        "arn:aws:ec2:us-east-1:123456789012:transit-gateway/tgw-1234567890abcdef0" 
    ], 
    "detail": { 
        "changeType": "NETWORK-FIREWALL-ATTACHMENT-DELETED", 
        "changeDescription": "A Network Firewall attachment has been deleted.", 
        "region": "us-east-1", 
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-east-1:123456789012:transit-
gateway-attachment/tgw-attach-1234567890abcdef0", 
                "resourceArns":[ 
            "arn:aws:network-firewall:us-east-1:123456789012:firewall/arn:aws:network-
firewall:us-east-1:123456789012:firewall/firewall-network-manager-event-example" 
            ], 
        "transitGatewayArn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
Topology change events 112
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Routing update events
Routing update events occur when there have been changes to the transit gateway route tables in 
your global network. These include the following:
Events
• A transit gateway attachment's route table changed (CONNECT_PEER_DELETED)
• A route was created in a transit gateway route table (TGW-ROUTE-INSTALLED)
• A route was deleted in a transit gateway route table gateway (TGW-ROUTE-UNINSTALLED)
A transit gateway attachment's route table changed (CONNECT_PEER_DELETED)
{ 
    "version": "0", 
    "id": "437f664b-cc6c-ccb8-b322-2c185ebe0c10", 
    "detail-type": "Network Manager Topology Change", 
    "source": "aws.networkmanager", 
    "account": "738040852526", 
    "time": "2023-11-13T20:49:34Z", 
    "region": "us-west-2", 
    "resources": [ 
        "arn:aws:networkmanager::738040852526:global-network/global-
network-02e49afd6fa01d0c3", 
        "arn:aws:networkmanager::738040852526:core-network/core-
network-0d6ee69cdc931f7b5" 
    ], 
    "detail": { 
        "changeType": "CONNECT_PEER_DELETED", 
        "changeDescription": "A Connect peer has been deleted in a Connect 
 attachment.", 
        "edgeLocation": "eu-west-2", 
        "attachmentArn": "arn:aws:networkmanager::738040852526:attachment/
attachment-05e447f0df042a011", 
        "connectPeerArn": "arn:aws:networkmanager::738040852526:connect-peer/connect-
peer-024b3172d38112df5", 
        "coreNetworkArn": "arn:aws:networkmanager::738040852526:core-network/core-
network-0d6ee69cdc931f7b5" 
    }
}
Routing update events 113
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
A route was created in a transit gateway route table (TGW-ROUTE-INSTALLED)
{  
"version": "0",  
"id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",  
"detail-type": "Network Manager Routing Update",  
"source": "aws.networkmanager",  
"account": "123456789012",  
"time": "2023-06-27T15:24:32Z",  
"region": "us-west-2",  
"resources": [  
    "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0",  
    "arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-1234567890abcdef0"  
],  
"detail": {  
    "changeType": "TGW-ROUTE-INSTALLED",  
    "changeDescription": "Routes in one or more Transit Gateway route tables have been 
 installed.",  
    "region": "us-east-1",  
    "transitGatewayRouteTableArns": [  
        "arn:aws:ec2:us-east-1:111122223333:transit-gateway-route-table/tgw-
rtb-1234567890abcdef0"  
    ],  
    "sequenceNumber": 1687879467281,  
    "routes": [{  
        "destinationCidrBlock": "11.0.0.0/16",  
        "attachments": [  
            { "tgwAttachmentId": "tgw-attach-1234567890abcdef0",  
              "resourceId": "vpc-1234567890abcdef0",  
              "attachmentType": "vpc"  
            }  
            ],  
        "routeType":  
            "route_propagated",  
            "routeState": "active",  
            "propagatedRouteFamily":  
                "connected" }  
            ],  
   "transitGatewayArn": "arn:aws:ec2:us-east-1:111122223333:transit-gateway/
tgw-1234567890abcdef0"  
}
Routing update events 114
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
A route was deleted in a transit gateway route table gateway (TGW-ROUTE-
UNINSTALLED)
{ 
  "version": "0", 
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", 
  "detail-type": "Network Manager Routing Update", 
  "source": "aws.networkmanager", 
  "account": "123456789012", 
  "time": "2022-02-30T23:18:50Z", 
  "region": "us-east-1", 
  "resources": [ 
    "arn:aws-us-east-1:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
    "arn:aws-us-east-1:ec2:us-east-1:111122223333:transit-gateway/
tgw-1234567890abcdef0" 
  ], 
  "detail": { 
    "changeType": "TGW-ROUTE-UNINSTALLED", 
    "changeDescription": "Routes in one or more Transit Gateway route tables have been 
 uninstalled.", 
    "region": "us-east-1", 
    "transitGatewayRouteTableArns": [ 
      "arn:aws-us-east-1:ec2:us-east-1:111122223333:transit-gateway-route-table/tgw-
rtb-1234567890abcdef0" 
    ], 
    "sequenceNumber": 1648147298451, 
    "routes": [{ 
      "destinationCidrBlock": "10.10.10.0/16", 
      "attachments": [], 
      "routeType": "route_static", 
      "routeState": "blackhole" 
    } 
    ], 
    "transitGatewayArn": "arn:aws-us-east-1:ec2:us-east-1:111122223333:transit-gateway/
tgw-1234567890abcdef0" 
  }
}
Routing update events 115
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Status update events
Status update events occur when there have been changes to the status of the connectivity of your 
VPN connections in the global network. These include the following:
Events
• A VPN tunnel's IPsec session went down (VPN-CONNECTION-IPSEC-DOWN)
• A VPN tunnel's IPsec session went up (after being down) (VPN-CONNECTION-IPSEC-UP)
• A VPN tunnel's BGP session went down (VPN-CONNECTION-BGP-DOWN)
• A VPN tunnel's BGP session went up (after being down) (VPN-CONNECTION-BGP-ESTABLISH)
• A Connect peer (GRE tunnel) BGP session went down (CONNECT_PEER_BGP_DOWN)
• A Connect peer (GRE tunnel) BGP session went up after being down) (CONNECT_PEER_BGP_UP)
A VPN tunnel's IPsec session went down (VPN-CONNECTION-IPSEC-DOWN)
{ 
    "version": "0", 
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", 
    "detail-type": "Network Manager Status Update", 
    "source": "aws.networkmanager",     
    "account": "123456789012", 
    "time": "2023-01-31T19:48:05Z", 
    "region": "us-west-2", 
    "resources": [ 
        "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
        "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-1234567890abcdef0" 
     ], 
    "detail": { 
        "changeType": "VPN-CONNECTION-IPSEC-DOWN", 
        "changeDescription": "IPsec for a VPN connection has gone down.", 
        "region": "us-west-2", 
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-west-2:111122223333:transit-
gateway-attachment/tgw-attach-1234567890abcdef0", 
        "vpnConnectionArn": "arn:aws:ec2:us-west-2:111122223333:vpn-connection/
vpn-1234567890abcdef0", 
        "outsideIpAddress": "35.84.102.207", 
        "transitGatewayArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway/
tgw-1234567890abcdef0" 
Status update events 116
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
    }
}
A VPN tunnel's IPsec session went up (after being down) (VPN-CONNECTION-
IPSEC-UP)
{ 
    "version": "0", 
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", 
    "detail-type": "Network Manager Status Update", 
    "source": "aws.networkmanager", 
    "account": "123456789012", 
    "time": "2023-01-31T19:34:54Z", 
    "region": "us-west-2", 
    "resources": [ 
        "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
        "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-1234567890abcdef0" 
    ], 
    "detail": { 
        "changeType": "VPN-CONNECTION-IPSEC-UP", 
        "changeDescription": "IPsec for a VPN connection has come up.", 
        "region": "us-west-2", 
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-west-2:111122223333:transit-
gateway-attachment/tgw-attach-1234567890abcdef0", 
        "vpnConnectionArn": "arn:aws:ec2:us-west-2:111122223333:vpn-connection/
vpn-1234567890abcdef0", 
        "outsideIpAddress": "52.37.214.193", 
        "transitGatewayArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
A VPN tunnel's BGP session went down (VPN-CONNECTION-BGP-DOWN)
{ 
    "version": "0", 
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", 
    "detail-type": "Network Manager Status Update", 
    "source": "aws.networkmanager", 
    "account": "123456789012", 
    "time": "2023-01-31T19:48:23Z", 
Status update events 117
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
    "region": "us-west-2", 
    "resources": [ 
        "arn:aws:networkmanager::123456789012:global-network/global-
network-0c243052669618f74", 
        "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-0fdb136628eff65a8" 
    ], 
    "detail": { 
        "changeType": "VPN-CONNECTION-BGP-DOWN", 
        "changeDescription": "BGP for a VPN connection has gone down.", 
        "region": "us-west-2", 
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-west-2:111122223333:transit-
gateway-attachment/tgw-attach-1234567890abcdef0", 
        "vpnConnectionArn": "arn:aws:ec2:us-west-2:111122223333:vpn-connection/
vpn-1234567890abcdef0", 
        "outsideIpAddress": "54.190.210.71", 
        "peerAsn": "65001", 
        "transitGatewayArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
A VPN tunnel's BGP session went up (after being down) (VPN-CONNECTION-BGP-
ESTABLISH)
{ 
    "version": "0", 
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", 
    "detail-type": "Network Manager Status Update", 
    "source": "aws.networkmanager", 
    "account": "123456789012", 
    "time": "2023-01-31T19:34:40Z", 
    "region": "us-west-2", 
    "resources": [ 
        "arn:aws:networkmanager::123456789012:global-network/global-
network-1234567890abcdef0", 
        "arn:aws:ec2:us-west-2:111122223333:vpn-connection/vpn-1234567890abcdef0" 
    ], 
    "detail": { 
        "changeType": "VPN-CONNECTION-BGP-ESTABLISH", 
        "changeDescription": "BGP for a VPN connection has been established.", 
        "region": "us-west-2", 
        "transitGatewayAttachmentArn": "arn:aws:ec2:us-west-2:111122223333:transit-
gateway-attachment/tgw-attach-1234567890abcdef0", 
Status update events 118
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
        "vpnConnectionArn": "arn:aws:ec2:us-west-2:111122223333:vpn-connection/
vpn-1234567890abcdef0", 
        "outsideIpAddress": "52.37.214.193", 
        "peerAsn": "65001", 
        "transitGatewayArn": "arn:aws:ec2:us-west-2:111122223333:transit-gateway/
tgw-1234567890abcdef0" 
    }
}
A Connect peer (GRE tunnel) BGP session went down 
(CONNECT_PEER_BGP_DOWN)
{ 
    "version": "0", 
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", 
    "detail-type": "Network Manager Status Update", 
    "source": "aws.networkmanager", 
    "account": "123456789012", 
    "time": "2023-03-01T19:57:34Z", 
    "region": "us-west-2", 
    "resources": ["arn:aws:networkmanager::123456789012:global-network/global-
network-07a82dd610af0cc57", "arn:aws:networkmanager::123456789012:core-network/core-
network-1234567890abcdef0"], 
    "detail": { 
        "changeType": "CONNECT_PEER_BGP_DOWN", 
        "changeDescription": "BGP for a Connect peer has gone down.", 
        "edgeLocation": "ap-southeast-1", 
        "attachmentArn": "arn:aws:networkmanager::123456789012:attachment/
attachment-1234567890abcdef0", 
        "connectPeerArn": "arn:aws:networkmanager::123456789012:connect-peer/connect-
peer-1234567890abcdef0", 
        "peerAsn": "65011", 
        "coreNetworkAddress": "192.0.2.0", 
        "coreNetworkArn": "arn:aws:networkmanager::123456789012:core-network/core-
network-1234567890abcdef0" 
    }    
}
A Connect peer (GRE tunnel) BGP session went up after being down) 
(CONNECT_PEER_BGP_UP)
{ 
Status update events 119
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
    "version": "0", 
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", 
    "detail-type": "Network Manager Status Update", 
    "source": "aws.networkmanager", 
    "account": "123456789012", 
    "time": "2023-03-01T19:57:49Z", 
    "region": "us-west-2", 
    "resources": ["arn:aws:networkmanager::123456789012:global-network/global-
network-07a82dd610af0cc57", "arn:aws:networkmanager::123456789012:core-network/core-
network-1234567890abcdef0"], 
    "detail": { 
        "changeType": "CONNECT_PEER_BGP_UP", 
        "changeDescription": "BGP for a Connect peer has been established.", 
        "edgeLocation": "ap-southeast-1", 
        "attachmentArn": "arn:aws:networkmanager::123456789012:attachment/
attachment-1234567890abcdef0", 
        "connectPeerArn": "arn:aws:networkmanager::123456789012:connect-peer/connect-
peer-1234567890abcdef0", 
        "peerAsn": "65011", 
        "coreNetworkAddress": "192.0.2.0", 
        "coreNetworkArn": "arn:aws:networkmanager::123456789012:core-network/core-
network-1234567890abcdef0" 
    }
}
Log AWS Global Networks for Transit Gateways API calls using 
AWS CloudTrail
AWS Global Networks for Transit Gateways works with AWS CloudTrail, a service that provides a 
record of actions taken by a user, role, or an AWS service in global networks. CloudTrail captures all 
API calls for global network as events. The calls that are captured include calls from the Network 
Manager console and code calls to the global API operations. If you create a trail, you can enable 
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Global 
Networks. If you don't conﬁgure a trail, you can still view the most recent events in the CloudTrail 
console in Event history. Using the information collected by CloudTrail, you can determine what 
request was made to global networks, the IP address from which the request was made, who made 
the request, when it was made, and additional details.
To learn more about CloudTrail, see the AWS CloudTrail User Guide.
Log API calls using CloudTrail 120
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Global network information in CloudTrail
CloudTrail is enabled on your AWS account when you create the account. When activity occurs in a 
global network, that activity is recorded in a CloudTrail event along with other AWS service events 
in Event history. You can view, search, and download recent events in your AWS account. For more 
information, see Viewing Events with CloudTrail Event History.
For an ongoing record of events in your AWS account, including events for a global network create 
a trail. A trail enables CloudTrail to deliver log ﬁles to an Amazon S3 bucket. By default, when 
you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all 
Regions in the AWS partition, and delivers the log ﬁles to the Amazon S3 bucket that you specify. 
Additionally, you can conﬁgure other AWS services to further analyze and act upon the event data 
collected in CloudTrail logs. For more information, see the following topics in the AWS CloudTrail 
User Guide.
• Overview for Creating a Trail
• CloudTrail Supported Services and Integrations
• Receiving CloudTrail Log Files from Multiple Regions and Receiving CloudTrail Log Files from 
Multiple Accounts
All actions in a global network are logged by CloudTrail and are documented in the Network 
Manager API Reference. For example, calls to the CreateGlobalNetwork action generate entries 
in the CloudTrail log ﬁles.
Every event or log entry contains information about who generated the request. The identity 
information helps you determine the following:
• Whether the request was made with root or AWS Identity and Access Management (IAM user) 
credentials
• Whether the request was made with temporary security credentials for a role or federated user
• Whether the request was made by another AWS service
For more information, see the CloudTrail userIdentity Element.
Global network information in CloudTrail 121
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Identity and access management for AWS Global 
Networks for Transit Gateways
AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely 
control access to AWS resources. IAM administrators control who can be authenticated (signed in) 
and authorized (have permissions) to use AWS Global Networks for Transit Gateways resources. IAM 
is an AWS service that you can use with no additional charge. You can use features of IAM to allow 
other users, services, and applications to use your AWS resources fully or in a limited way, without 
sharing your security credentials.
By default, IAM users don't have permission to create, view, or modify AWS resources. To allow an 
IAM user to access resources, such as a global network, and perform tasks, you must:
• Create an IAM policy that grants the IAM user permission to use the speciﬁc resources and API 
actions they need
• Attach the policy to the IAM user or to the group to which the IAM user belongs
When you attach a policy to a user or group of users, it allows or denies the user permissions to 
perform the speciﬁed tasks on the speciﬁed resources.
Important
If you grant access to a global network in Network Manager, you grant access to all AWS 
service data associated with the registered transit gateways across all Regions.
Contents
• How Network Manager works with IAM
• Example policies to manage global networks
• AWS Global Networks for Transit Gateways service-linked roles
• AWS managed policies for AWS Global Networks for Transit Gateways
• Multi-account access roles for AWS Global Networks for Transit Gateways
122
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
How Network Manager works with IAM
With IAM identity-based policies, you can specify allowed or denied actions and resources, and 
specify the conditions under which actions are allowed or denied. Network Manager supports 
speciﬁc actions, resources, and condition keys. For a complete list, see Actions, Resources, and 
Condition Keys for AWS Network Manager in the Service Authorization Reference.
To learn about all of the elements that you use in a JSON policy, see IAM JSON Policy Elements 
Reference in the IAM User Guide.
Actions
Policy actions in Network Manager use the following preﬁx before the action:
networkmanager:. For example, to grant someone permission to create a 
global network with the CreateGlobalNetwork API operation, you include the
networkmanager:CreateGlobalNetwork action in their policy.
For a list of global networks actions, see the Network Manager API Reference.
Resources
The Resource element speciﬁes the object or objects to which the action applies. Statements must 
include either a Resource or a NotResource element. You specify a resource using an ARN or using 
the wildcard (*) to indicate that the statement applies to all resources.
The global network resource has the following ARN.
arn:${Partition}:networkmanager::${Account}:global-network/${GlobalNetworkId} 
For example, to specify the global-network-1122334455aabbccd global network in your 
statement, use the following ARN.
"Resource": "arn:aws:networkmanager::123456789012:global-network/global-
network-1122334455aabbccd"
Condition keys
The Condition element (or Condition block) lets you specify conditions in which a statement 
is in eﬀect. The Condition element is optional. You can build conditional expressions that use
How Network Manager works with IAM 123
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
condition operators, such as equals or less than, to match the condition in the policy with values in 
the request.
If you specify multiple Condition elements in a statement, or multiple keys in a single
Condition element, AWS evaluates them using a logical AND operation. If you specify multiple 
values for a single condition key, AWS evaluates the condition using a logical OR operation. All of 
the conditions must be met before the statement's permissions are granted.
You can also use placeholder variables when you specify conditions. For example, you can grant 
an IAM user permission to access a resource only if it is tagged with their IAM user name. For more 
information, see IAM Policy Elements: Variables and Tags in the IAM User Guide.
You can attach tags to global networks resources or pass tags in a request to global networks. To 
control access based on tags, you provide tag information in the condition element of a policy 
using the aws:ResourceTag/key-name, aws:RequestTag/key-name, or aws:TagKeys
condition keys.
To see all AWS global condition keys, see AWS Global Condition Context Keys in the IAM User 
Guide.
global networks also supports the following condition keys:
• networkmanager:tgwArn—Controls which transit gateways can be registered or deregistered 
in your global network.
• networkmanager:cgwArn—Controls which customer gateways can be associated or 
disassociated from devices and links in your global network.
• networkmanager:tgwConnectPeerArn—Controls which Connect peers can be associated or 
disassociated from devices and links in your global network.
Example policies to manage global networks
The following are example IAM policies for working with global networks.
Administrator access
The following IAM policy grants full access to the Amazon EC2, global networks, Direct Connect, 
and CloudWatch APIs. This enables administrators to create and manage transit gateways and their 
attachments (such as VPCs and Direct Connect gateways), create and manage global networks 
Example policies 124
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
resources, and monitor global networks using CloudWatch metrics and events. The policy also 
grants user permissions to create any required service-linked roles.
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
        { 
            "Effect": "Allow", 
            "Action": "ec2:*", 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": "networkmanager:*", 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": "cloudwatch:*", 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": "events:*", 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": "directconnect:*", 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": "iam:CreateServiceLinkedRole", 
            "Resource": "arn:aws:iam::*:role/aws-service-role/*" 
        } 
    ]
}
Example policies 125
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Read-only access
The following IAM policy grants read-only access to the Amazon EC2, global networks, Direct 
Connect, CloudWatch, and EventBridge APIs. This enables users to use the global networks console 
to view and monitor global networks and their associated resources, and view metrics and events 
for the resources. Users cannot create or modify any resources.
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "ec2:Get*", 
                "ec2:Describe*" 
            ], 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "networkmanager:Get*", 
                "networkmanager:Describe*" 
            ], 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "cloudwatch:List*", 
                "cloudwatch:Get*", 
                "cloudwatch:Describe*" 
            ], 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "logs:Describe*", 
                "logs:Get*", 
Example policies 126
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
                "logs:List*", 
                "logs:StartQuery", 
                "logs:StopQuery", 
                "logs:TestMetricFilter", 
                "logs:FilterLogEvents" 
            ], 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "events:List*", 
                "events:TestEventPattern", 
                "events:Describe*" 
            ], 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": "directconnect:Describe*", 
            "Resource": "*" 
        } 
    ]
}
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "networkmanager:CreateSite" 
            ], 
            "Resource": [ 
                "arn:aws:networkmanager::111122223333:global-network/global-
network-1122334455aabbccd", 
                "arn:aws:networkmanager::111122223333:site/*" 
            ] 
        }, 
        { 
Example policies 127
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
            "Effect": "Allow", 
            "Action": [ 
                "networkmanager:CreateDevice" 
            ], 
            "Resource": [ 
                "arn:aws:networkmanager::111122223333:global-network/global-
network-1122334455aabbccd", 
                "arn:aws:networkmanager::111122223333:site/*", 
                "arn:aws:networkmanager::111122223333:device/*" 
            ] 
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "networkmanager:CreateLink" 
            ], 
            "Resource": [ 
                "arn:aws:networkmanager::111122223333:global-network/global-
network-1122334455aabbccd", 
                "arn:aws:networkmanager::111122223333:link/*" 
            ] 
        } 
    ]
}
Controlling the use of transit gateways and customer gateways
The following IAM policy enables users to work with global networks resources, but they are 
explicitly denied permission to do the following:
• Register or deregister a speciﬁc transit gateway (tgw-aabbccdd112233445) in the global 
network.
• Associate or disassociate a speciﬁc customer gateway (cgw-11223344556677abc) in the global 
network.
The policy uses the networkmanager:tgwArn and networkmanager:cgwArn condition keys to 
enforce these conditions.
Example policies 128
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "networkmanager:*" 
            ], 
            "Resource": [ 
                "*" 
            ] 
        }, 
        { 
            "Effect": "Deny", 
            "Action": [ 
                "networkmanager:RegisterTransitGateway", 
                "networkmanager:DeregisterTransitGateway" 
            ], 
            "Resource": [ 
                "*" 
            ], 
            "Condition": { 
                "StringEquals": { 
                    "networkmanager:tgwArn": 
 "arn:aws:ec2:region:123456789012:transit-gateway/tgw-aabbccdd112233445" 
                } 
            } 
        }, 
        { 
            "Effect": "Deny", 
            "Action": [ 
                "networkmanager:AssociateCustomerGateway", 
                "networkmanager:DisassociateCustomerGateway" 
            ], 
            "Resource": [ 
                "*" 
            ], 
            "Condition": { 
                "StringEquals": { 
                    "networkmanager:cgwArn": 
 "arn:aws:ec2:region:123456789012:customer-gateway/cgw-11223344556677abc" 
Example policies 129
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
                } 
            } 
        } 
    ]
}
AWS Global Networks for Transit Gateways service-linked roles
AWS Global Networks for Transit Gateways uses service-linked roles for the permissions that it 
requires to call other AWS services on your behalf. These service-linked roles are not propagated to 
your AWS Organizations management account.
Permissions granted by the service-linked role
AWS Global Networks for Transit Gateways uses a Network Manager service-linked role named 
AWSServiceRoleForNetworkManager to call the actions on your behalf when you work with global 
networks.
The AWSServiceRoleForNetworkManager service-linked role trusts the following service to assume 
the role:
• networkmanager.amazonaws.com
This service-linked role uses the managed policy AWSNetworkManagerServiceRolePolicy. To view 
the permissions for this policy, see AWSNetworkManagerServiceRolePolicy in the AWS Managed 
Policy Reference.
Create the service-linked role
You don't need to manually create the AWSServiceRoleForNetworkManager role. global networks 
creates this role for you when you create your ﬁrst global network.
For global networks to create a service-linked role on your behalf, you must have the required 
permissions. For more information, see Service-linked role permissions in the IAM User Guide.
Service-linked role 130
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Edit the service-linked role
You can edit the description of AWSServiceRoleForNetworkManager using IAM. For more 
information, see Edit a service-linked role description in the IAM User Guide.
Delete the service-linked role
If you no longer need to use global networks, we recommend that you delete the
AWSServiceRoleForNetworkManager role.
You can delete this service-linked role only after you delete your global network. For information 
about how to delete your global network, see Delete a global network.
You can use the IAM console, the IAM CLI, or the IAM API to delete service-linked roles. For more 
information, see Delete a service-linked role in the IAM User Guide.
After you delete AWSServiceRoleForNetworkManager, Network Manager will create the role again 
when you create a new global network.
Supported Regions for AWS Global Networks for Transit Gateways 
service-linked roles
AWS Global Networks for Transit Gateways supports the custom-linked roles in all of AWS Regions 
where the service is available. For more information, see the section called “Region availability”.
AWS managed policies for AWS Global Networks for Transit 
Gateways
To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to 
write policies yourself. It takes time and expertise to create IAM customer managed policies that 
provide your team with only the permissions they need. To get started quickly, you can use our 
AWS managed policies. These policies cover common use cases and are available in your AWS 
account. For more information about AWS managed policies, see AWS managed policies in the IAM 
User Guide.
AWS services maintain and update AWS managed policies. You can't change the permissions in 
AWS managed policies. Services occasionally add additional permissions to an AWS managed 
Edit the service-linked role 131
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
policy to support new features. This type of update aﬀects all identities (users, groups, and roles) 
where the policy is attached. Services are most likely to update an AWS managed policy when 
a new feature is launched or when new operations become available. Services do not remove 
permissions from an AWS managed policy, so policy updates won't break your existing permissions.
Additionally, AWS supports managed policies for job functions that span multiple services. For 
example, the ReadOnlyAccess AWS managed policy provides read-only access to all AWS services 
and resources. When a service launches a new feature, AWS adds read-only permissions for new 
operations and resources. For a list and descriptions of job function policies, see AWS managed 
policies for job functions in the IAM User Guide.
AWS managed policy: NetworkAdministrator
You can attach the NetworkAdministrator policy to your IAM identities. This policy grants 
permissions that allow registered delegated administrators and the management account
administrator access to global networks. For more information, see the section called “Multi-
account access roles”.
To view the permissions for this policy, see NetworkAdministrator in the AWS Managed Policy 
Reference.
AWS managed policy: AWSNetworkManagerReadOnlyAccess
You can attach the AWSNetworkManagerReadOnlyAccess policy to your IAM identities. This policy 
grants permissions that allow registered delegated administrators and the management account
read-only access to global networks. For more information, see the section called “Multi-account 
access roles”.
To view the permissions for this policy, see AWSNetworkManagerReadOnlyAccess in the AWS 
Managed Policy Reference.
AWS managed policy: AWSNetworkManagerServiceRolePolicy
This policy is attached to the service-linked role named AWSServiceRoleForNetworkManager to 
allow AWS Global Networks for Transit Gateways to call API actions on your behalf when you work 
with global networks. For more information, see the section called “Service-linked role”.
To view the permissions for this policy, see AWSNetworkManagerServiceRolePolicy in the AWS 
Managed Policy Reference.
NetworkAdministrator 132
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
AWS Global Networks for Transit Gateways updates to AWS managed 
policies
View details about updates to AWS managed policies for Network Manager since this service began 
tracking these changes in April 2021. For automatic alerts about changes to this page, subscribe to 
the RSS feed on the Network Manager Document history page.
Change Description Date
AWSNetworkManagerS 
erviceRolePolicy
AWS Global Networks for 
Transit Gateways added 
permission to call the 
following API action:
GetTransitGatewayR 
outeTablePropagati 
ons .
July 12, 2022
NetworkAdministrator AWS Global Networks for 
Transit Gateways began using 
administrative permissions in 
member accounts for multi-
account access.
May 24, 2022
AWSNetworkManagerR 
eadOnlyAccess - Updated 
existing policy
AWS Global Networks for 
Transit Gateways began using 
read-only permissions in 
member accounts for multi-
account access.
May 24, 2022
AWSNetworkManagerS 
erviceRolePolicy - Updated 
existing policy
AWS Global Networks for 
Transit Gateways added 
permission to call the 
following API actions:
organizations:Desc 
ribeAccount ,
organizations:Desc 
ribeOrganization ,
May 24, 2022
Policy updates 133
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Change Description Date
organizations:List 
Accounts , organizat 
ions:ListAWSServic 
eAccessForOrganiza 
tion , and organizat 
ions:ListDelegated 
Administrators .
AWSNetworkManagerS 
erviceRolePolicy - Updated 
existing policy
AWS Global Networks for 
Transit Gateways added 
permissions to call the 
following API action:
ec2:DescribeRegions .
December 2, 2021
AWSNetworkManagerS 
erviceRolePolicy: updated 
existing policy
AWS Global Networks for 
Transit Gateways added 
permissions to call the 
following API actions:
directconnect:Desc 
ribeDirectConnectG 
ateways , ec2:Descr 
ibeVpnConnections ,
ec2:DescribeVpcs ,
ec2:GetTransitGate 
wayRouteTableAssoc 
iations , ec2:Searc 
hTransitGatewayRou 
tes , ec2:Descr 
ibeTransitGatewayP 
eeringAttachments ,
ec2:DescribeTransi 
tGatewayConnects , and
ec2:DescribeTransi 
tGatewayConnectPee 
rs .
June 1, 2021
Policy updates 134
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Multi-account access roles for AWS Global Networks for Transit 
Gateways
AWS Global Networks for Transit Gateways uses CloudFormation StackSets to deploy and manage 
the following two custom IAM roles in AWS Organizations member accounts to support multi-
account permissions. These two roles are deployed to every member account in the organization 
when AWSServiceAccess is enabled (trusted access). For more information about multi-account, 
see Manage multiple accounts in global networks using AWS Organizations.
The custom IAM roles are created automatically through the Network Manager service when you 
enable multi-account access using the global networks console. We strongly recommend that you 
use the console for enabling multi-account. Choosing an alternative approach requires an advanced 
level of expertise, and opens the multi-account for your global network to be more prone to error.
CloudWatch-CrossAccountSharingRole
This policy provides delegated administrators and the management accounts access to CloudWatch 
monitoring data from other member accounts. The following is an example of the template.
AWSTemplateFormatVersion: '2010-09-09'
Description: Enables CloudWatch in central monitoring accounts to assume permissions to 
 view CloudWatch data in the current account
Resources: 
  CloudWatch-CrossAccountSharingRole: 
    Type: AWS::IAM::Role 
    Properties: 
      RoleName: CloudWatch-CrossAccountSharingRole 
      AssumeRolePolicyDocument: 
        Version: '2012-10-17' 
        Statement: 
          - Effect: Allow 
            Principal: 
              AWS: [ 
                "arn:aws:iam::<account1-id>:root", 
                "arn:aws:iam::<account2-id>:root", 
                "arn:aws:iam::<account3-id>:root" 
              ] 
            Action: 
              - sts:AssumeRole 
Multi-account access roles 135
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
      Path: "/" 
      ManagedPolicyArns: 
          - arn:aws:iam::aws:policy/CloudWatchReadOnlyAccess
IAMRoleForAWSNetworkManagerCrossAccountResourceAccess
The IAMRoleForAWSNetworkManagerCrossAccountResourceAccess IAM policy role, based 
on your selection when enabling trusted access through the global networksconsole, enables 
either administrative or read-only global networks console switch role access. An associated 
administrative or read-only template is also deployed along with the policy. For information about 
these templates, see the section called “Permission templates”.
The following is an example of the administrator role template.
AWSTemplateFormatVersion: '2010-09-09'
Description: Enables admin cross account resource access through switch role
Resources: 
  IAMRoleForAWSNetworkManagerCrossAccountResourceAccess: 
    Type: AWS::IAM::Role 
    Properties: 
      RoleName: IAMRoleForAWSNetworkManagerCrossAccountResourceAccess 
      AssumeRolePolicyDocument: 
        Version: '2012-10-17' 
        Statement: 
          - Effect: Allow 
            Principal: 
              AWS: [ 
                "arn:aws:iam::<account1-id>:root", 
                "arn:aws:iam::<account2-id>:root", 
                "arn:aws:iam::<account3-id>:root" 
              ] 
            Action: 
              - sts:AssumeRole 
      Path: "/" 
      ManagedPolicyArns: 
          - arn:aws:iam::aws:policy/NetworkAdministrator
The following is the read-only role template.
AWSTemplateFormatVersion: '2010-09-09'
IAMRoleForAWSNetworkManagerCrossAccountResourceAccess 136
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Description: Enables read only cross account resource access through switch role
Resources: 
 IAMRoleForAWSNetworkManagerCrossAccountResourceAccess: 
 Type: AWS::IAM::Role 
 Properties: 
    RoleName: IAMRoleForAWSNetworkManagerCrossAccountResourceAccess 
    AssumeRolePolicyDocument: 
    Version: '2012-10-17' 
    Statement: 
      - Effect: Allow 
        Principal: 
          AWS: [ 
            "arn:aws:iam::<account1-id>:root", 
            "arn:aws:iam::<account2-id>:root", 
            "arn:aws:iam::<account3-id>:root" 
          ] 
       Action: 
         - sts:AssumeRole 
    Path: "/" 
    ManagedPolicyArns: 
        - arn:aws:iam::aws:policy/AWSNetworkManagerReadOnlyAccess 
        - arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess 
        - arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess 
        - arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess                         
Permission templates
When choosing the IAMRoleForAWSNetworkManagerCrossAccountResourceAccess
permission, an associated administrative or read-only template is also passed to CloudFormation 
StackSets. These templates contain a list of accounts that are able to assume these roles. These 
accounts include the AWS Organizations management account and all registered delegated 
administrators for the Network Manager service. Deregistering a delegated administrator removes 
it from this list so that it can no longer assume these roles. Disabling trusted access deletes the 
CloudFormation StackSets, and in turn all member account stacks and custom IAM roles in those 
accounts that were StackSets-managed for multi-account.
NetworkAdministrator
This policy enables administrator permission for the delegated administrator and management 
accounts to modify resources from other accounts in the global network while using the Network 
Manager console switch role.
Permission templates 137
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "autoscaling:Describe*", 
                "cloudfront:ListDistributions", 
                "cloudwatch:DeleteAlarms", 
                "cloudwatch:DescribeAlarms", 
                "cloudwatch:GetMetricStatistics", 
                "cloudwatch:PutMetricAlarm", 
                "directconnect:*", 
                "ec2:AcceptVpcEndpointConnections", 
                "ec2:AllocateAddress", 
                "ec2:AssignIpv6Addresses", 
                "ec2:AssignPrivateIpAddresses", 
                "ec2:AssociateAddress", 
                "ec2:AssociateDhcpOptions", 
                "ec2:AssociateRouteTable", 
                "ec2:AssociateSubnetCidrBlock", 
                "ec2:AssociateVpcCidrBlock", 
                "ec2:AttachInternetGateway", 
                "ec2:AttachNetworkInterface", 
                "ec2:AttachVpnGateway", 
                "ec2:CreateCarrierGateway", 
                "ec2:CreateCustomerGateway", 
                "ec2:CreateDefaultSubnet", 
                "ec2:CreateDefaultVpc", 
                "ec2:CreateDhcpOptions", 
                "ec2:CreateEgressOnlyInternetGateway", 
                "ec2:CreateFlowLogs", 
                "ec2:CreateInternetGateway", 
                "ec2:CreateNatGateway", 
                "ec2:CreateNetworkAcl", 
                "ec2:CreateNetworkAclEntry", 
                "ec2:CreateNetworkInterface", 
                "ec2:CreateNetworkInterfacePermission", 
                "ec2:CreatePlacementGroup", 
                "ec2:CreateRoute", 
                "ec2:CreateRouteTable", 
Permission templates 138
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
                "ec2:CreateSecurityGroup", 
                "ec2:CreateSubnet", 
                "ec2:CreateTags", 
                "ec2:CreateVpc", 
                "ec2:CreateVpcEndpoint", 
                "ec2:CreateVpcEndpointConnectionNotification", 
                "ec2:CreateVpcEndpointServiceConfiguration", 
                "ec2:CreateVpnConnection", 
                "ec2:CreateVpnConnectionRoute", 
                "ec2:CreateVpnGateway", 
                "ec2:DeleteCarrierGateway", 
                "ec2:DeleteEgressOnlyInternetGateway", 
                "ec2:DeleteFlowLogs", 
                "ec2:DeleteNatGateway", 
                "ec2:DeleteNetworkInterface", 
                "ec2:DeleteNetworkInterfacePermission", 
                "ec2:DeletePlacementGroup", 
                "ec2:DeleteSubnet", 
                "ec2:DeleteTags", 
                "ec2:DeleteVpc", 
                "ec2:DeleteVpcEndpointConnectionNotifications", 
                "ec2:DeleteVpcEndpointServiceConfigurations", 
                "ec2:DeleteVpcEndpoints", 
                "ec2:DeleteVpnConnection", 
                "ec2:DeleteVpnConnectionRoute", 
                "ec2:DeleteVpnGateway", 
                "ec2:DescribeAccountAttributes", 
                "ec2:DescribeAddresses", 
                "ec2:DescribeAvailabilityZones", 
                "ec2:DescribeCarrierGateways", 
                "ec2:DescribeClassicLinkInstances", 
                "ec2:DescribeCustomerGateways", 
                "ec2:DescribeDhcpOptions", 
                "ec2:DescribeEgressOnlyInternetGateways", 
                "ec2:DescribeFlowLogs", 
                "ec2:DescribeInstances", 
                "ec2:DescribeInternetGateways", 
                "ec2:DescribeKeyPairs", 
                "ec2:DescribeMovingAddresses", 
                "ec2:DescribeNatGateways", 
                "ec2:DescribeNetworkAcls", 
                "ec2:DescribeNetworkInterfaceAttribute", 
                "ec2:DescribeNetworkInterfacePermissions", 
                "ec2:DescribeNetworkInterfaces", 
Permission templates 139
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
                "ec2:DescribePlacementGroups", 
                "ec2:DescribePrefixLists", 
                "ec2:DescribeRouteTables", 
                "ec2:DescribeSecurityGroupReferences", 
                "ec2:DescribeSecurityGroupRules", 
                "ec2:DescribeSecurityGroups", 
                "ec2:DescribeStaleSecurityGroups", 
                "ec2:DescribeSubnets", 
                "ec2:DescribeTags", 
                "ec2:DescribeVpcAttribute", 
                "ec2:DescribeVpcClassicLink", 
                "ec2:DescribeVpcClassicLinkDnsSupport", 
                "ec2:DescribeVpcEndpointConnectionNotifications", 
                "ec2:DescribeVpcEndpointConnections", 
                "ec2:DescribeVpcEndpointServiceConfigurations", 
                "ec2:DescribeVpcEndpointServicePermissions", 
                "ec2:DescribeVpcEndpointServices", 
                "ec2:DescribeVpcEndpoints", 
                "ec2:DescribeVpcPeeringConnections", 
                "ec2:DescribeVpcs", 
                "ec2:DescribeVpnConnections", 
                "ec2:DescribeVpnGateways", 
                "ec2:DescribePublicIpv4Pools", 
                "ec2:DescribeIpv6Pools", 
                "ec2:DetachInternetGateway", 
                "ec2:DetachNetworkInterface", 
                "ec2:DetachVpnGateway", 
                "ec2:DisableVgwRoutePropagation", 
                "ec2:DisableVpcClassicLinkDnsSupport", 
                "ec2:DisassociateAddress", 
                "ec2:DisassociateRouteTable", 
                "ec2:DisassociateSubnetCidrBlock", 
                "ec2:DisassociateVpcCidrBlock", 
                "ec2:EnableVgwRoutePropagation", 
                "ec2:EnableVpcClassicLinkDnsSupport", 
                "ec2:ModifyNetworkInterfaceAttribute", 
                "ec2:ModifySecurityGroupRules", 
                "ec2:ModifySubnetAttribute", 
                "ec2:ModifyVpcAttribute", 
                "ec2:ModifyVpcEndpoint", 
                "ec2:ModifyVpcEndpointConnectionNotification", 
                "ec2:ModifyVpcEndpointServiceConfiguration", 
                "ec2:ModifyVpcEndpointServicePermissions", 
                "ec2:ModifyVpcPeeringConnectionOptions", 
Permission templates 140
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
                "ec2:ModifyVpcTenancy", 
                "ec2:MoveAddressToVpc", 
                "ec2:RejectVpcEndpointConnections", 
                "ec2:ReleaseAddress", 
                "ec2:ReplaceNetworkAclAssociation", 
                "ec2:ReplaceNetworkAclEntry", 
                "ec2:ReplaceRoute", 
                "ec2:ReplaceRouteTableAssociation", 
                "ec2:ResetNetworkInterfaceAttribute", 
                "ec2:RestoreAddressToClassic", 
                "ec2:UnassignIpv6Addresses", 
                "ec2:UnassignPrivateIpAddresses", 
                "ec2:UpdateSecurityGroupRuleDescriptionsEgress", 
                "ec2:UpdateSecurityGroupRuleDescriptionsIngress", 
                "elasticbeanstalk:Describe*", 
                "elasticbeanstalk:List*", 
                "elasticbeanstalk:RequestEnvironmentInfo", 
                "elasticbeanstalk:RetrieveEnvironmentInfo", 
                "elasticloadbalancing:*", 
                "logs:DescribeLogGroups", 
                "logs:DescribeLogStreams", 
                "logs:GetLogEvents", 
                "route53:*", 
                "route53domains:*", 
                "sns:CreateTopic", 
                "sns:ListSubscriptionsByTopic", 
                "sns:ListTopics" 
            ], 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "ec2:AcceptVpcPeeringConnection", 
                "ec2:AttachClassicLinkVpc", 
                "ec2:AuthorizeSecurityGroupEgress", 
                "ec2:AuthorizeSecurityGroupIngress", 
                "ec2:CreateVpcPeeringConnection", 
                "ec2:DeleteCustomerGateway", 
                "ec2:DeleteDhcpOptions", 
                "ec2:DeleteInternetGateway", 
                "ec2:DeleteNetworkAcl", 
                "ec2:DeleteNetworkAclEntry", 
                "ec2:DeleteRoute", 
Permission templates 141
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
                "ec2:DeleteRouteTable", 
                "ec2:DeleteSecurityGroup", 
                "ec2:DeleteVolume", 
                "ec2:DeleteVpcPeeringConnection", 
                "ec2:DetachClassicLinkVpc", 
                "ec2:DisableVpcClassicLink", 
                "ec2:EnableVpcClassicLink", 
                "ec2:GetConsoleScreenshot", 
                "ec2:RejectVpcPeeringConnection", 
                "ec2:RevokeSecurityGroupEgress", 
                "ec2:RevokeSecurityGroupIngress" 
            ], 
            "Resource": [ 
                "*" 
            ] 
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "ec2:CreateLocalGatewayRoute", 
                "ec2:CreateLocalGatewayRouteTableVpcAssociation", 
                "ec2:DeleteLocalGatewayRoute", 
                "ec2:DeleteLocalGatewayRouteTableVpcAssociation", 
                
 "ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations", 
                "ec2:DescribeLocalGatewayRouteTableVpcAssociations", 
                "ec2:DescribeLocalGatewayRouteTables", 
                "ec2:DescribeLocalGatewayVirtualInterfaceGroups", 
                "ec2:DescribeLocalGatewayVirtualInterfaces", 
                "ec2:DescribeLocalGateways", 
                "ec2:SearchLocalGatewayRoutes" 
            ], 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "s3:GetBucketLocation", 
                "s3:GetBucketWebsite", 
                "s3:ListBucket" 
            ], 
            "Resource": [ 
                "*" 
            ] 
Permission templates 142
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "iam:GetRole", 
                "iam:ListRoles", 
                "iam:PassRole" 
            ], 
            "Resource": "arn:aws:iam::*:role/flow-logs-*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "networkmanager:*" 
            ], 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "ec2:AcceptTransitGatewayVpcAttachment", 
                "ec2:AssociateTransitGatewayRouteTable", 
                "ec2:CreateTransitGateway", 
                "ec2:CreateTransitGatewayRoute", 
                "ec2:CreateTransitGatewayRouteTable", 
                "ec2:CreateTransitGatewayVpcAttachment", 
                "ec2:DeleteTransitGateway", 
                "ec2:DeleteTransitGatewayRoute", 
                "ec2:DeleteTransitGatewayRouteTable", 
                "ec2:DeleteTransitGatewayVpcAttachment", 
                "ec2:DescribeTransitGatewayAttachments", 
                "ec2:DescribeTransitGatewayRouteTables", 
                "ec2:DescribeTransitGatewayVpcAttachments", 
                "ec2:DescribeTransitGateways", 
                "ec2:DisableTransitGatewayRouteTablePropagation", 
                "ec2:DisassociateTransitGatewayRouteTable", 
                "ec2:EnableTransitGatewayRouteTablePropagation", 
                "ec2:ExportTransitGatewayRoutes", 
                "ec2:GetTransitGatewayAttachmentPropagations", 
                "ec2:GetTransitGatewayRouteTableAssociations", 
                "ec2:GetTransitGatewayRouteTablePropagations", 
                "ec2:ModifyTransitGateway", 
                "ec2:ModifyTransitGatewayVpcAttachment", 
                "ec2:RejectTransitGatewayVpcAttachment", 
Permission templates 143
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
                "ec2:ReplaceTransitGatewayRoute", 
                "ec2:SearchTransitGatewayRoutes" 
            ], 
            "Resource": "*" 
        }, 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "iam:CreateServiceLinkedRole" 
            ], 
            "Resource": "*", 
            "Condition": { 
                "StringLike": { 
                    "iam:AWSServiceName": [ 
                        "transitgateway.amazonaws.com" 
                    ] 
                } 
            } 
        } 
    ]
}
AWSNetworkManagerReadOnlyAccess
This policy enables read-only permission for the delegated administrator and management 
accounts to review information about resources from other accounts in the global network while 
using the global networks console switch role, but doesn't allow either account to make changes.
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
        { 
            "Effect": "Allow", 
            "Action": [ 
                "networkmanager:Describe*", 
                "networkmanager:Get*", 
                "networkmanager:List*" 
            ], 
            "Resource": "*" 
Permission templates 144
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
        } 
    ]
}
Permission templates 145
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
AWS Global Networks for Transit Gateways Quotas
Your AWS account has the quotas shown in the following table for AWS Global Networks for 
Transit Gateways.
The Service Quotas console also provides information about global networks quotas. You can 
use the Service Quotas console to view default quotas and request quota increases for adjustable 
quotas. For more information, see Requesting a quota increase in the Service Quotas User Guide.
General quotas
The following global networks general quotas apply.
Quota Default Adjustable
Global networks per AWS 
account
5 Yes
Number of devices per global 
network
200 Yes
Number of sites per global 
network
200 Yes
Number of links per global 
network
200 Yes
Number of connections per 
global network
200 Yes
Number of registered 
delegated administrators 
for an organization in AWS 
Organizations
10 Yes
General quotas 146
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Document history for AWS Global Networks for Transit 
Gateways
Change Description Date
Support for dual-stack IPv6 
endpoints.
Network Manager now 
supports dual-stack IPv6 
endpoints.
March 25, 2025
Support PrivateLink. Network Manager now 
supports PrivateLink in the 
us-west-2 and us-gov-west-1 
Regions.
March 25, 2025
Support PrivateLink. Network Manager now 
supports PrivateLink in the 
us-west-2 and us-gov-west-1 
Regions.
March 25, 2025
Support PrivateLink. Network Manager now 
supports PrivateLink in the 
us-west-2 and us-gov-west-1 
Regions.
March 25, 2025
New Region support Added ap-southeast-5  to 
the list of available Regions.
March 13, 2025
New Region support Added me-central-1 ,
ap-south-2 , ap-southe 
ast-4 , ca-west-1 , eu-
south-2 , and eu-centra 
l-2  to the list of available 
Regions.
October 3, 2024
New Region support Added ap-southeast-3  to 
the list of available Regions.
March 26, 2024
147
AWS Network Manager AWS Global Networks for Transit Gateways User Guide
Guide renamed The Network Manager User 
Guide was renamed to the
AWS Global Networks for 
Transit Gateways User Guide, 
as the AWS Network Manager 
console was reorganized. AWS 
Global Networks for Transit 
Gateways are now a part of 
the greater-feature Network 
Manager console.
November 28, 2022
Updated AWS managed policy Network Manager added 
a new action, GetTransi 
tGatewayRouteTable 
Propagations , to its AWS 
managed policies.
July 12, 2022
Multi-account support Network Manager now 
supports multi-account, 
which allows you to centrally 
manage multiple AWS 
Organizations accounts and 
transit gateways in a single 
global network.
May 24, 2022
New guide created Network Manager documenta 
tion was removed from the
AWS Transit Gateway User 
Guide  and included as part 
of a new, standalone AWS 
Network Manager User Guide.
December 2, 2021
Documentation updated for 
AWS Cloud WAN
The AWS Network Manager 
User Guide was updated, as 
Network Manager supports 
both AWS Transit Gateways 
and AWS Cloud WAN.
December 2, 2021
148
