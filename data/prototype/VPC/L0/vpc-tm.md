# Traﬃc Mirroring

## What is Traﬃc Mirroring?

## Traﬃc Mirroring concepts

## Work with Traﬃc Mirroring

Traﬃc Mirroring
Amazon Virtual Private Cloud
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
## Traﬃc Mirroring beneﬁts

## Regional availability

## Supported instance types

## Virtualized instances

Amazon Virtual Private Cloud Traﬃc Mirroring
Amazon Virtual Private Cloud: Traﬃc Mirroring
Copyright © 2026 Amazon Web Services, Inc. and/or its aﬃliates. All rights reserved.
Amazon's trademarks and trade dress may not be used in connection with any product or service 
that is not Amazon's, in any manner that is likely to cause confusion among customers, or in any 
manner that disparages or discredits Amazon. All other trademarks not owned by Amazon are 
the property of their respective owners, who may or may not be aﬃliated with, connected to, or 
sponsored by Amazon.
## Bare metal instances

## Pricing

Amazon Virtual Private Cloud Traﬃc Mirroring
Table of Contents
What is Traﬃc Mirroring? ............................................................................................................... 1
Traﬃc Mirroring concepts ........................................................................................................................... 1
Work with Traﬃc Mirroring ........................................................................................................................ 1
Traﬃc Mirroring beneﬁts ............................................................................................................................ 2
Regional availability ..................................................................................................................................... 2
Supported instance types ........................................................................................................................... 2
Virtualized instances ............................................................................................................................... 2
Bare metal instances .............................................................................................................................. 3
Pricing ............................................................................................................................................................. 3
How Traﬃc Mirroring works ........................................................................................................... 5
Targets ............................................................................................................................................................ 6
Network interfaces .................................................................................................................................. 7
Network Load Balancer .......................................................................................................................... 7
Gateway Load Balancer endpoints ...................................................................................................... 8
VXLAN encapsulation ............................................................................................................................. 9
Routing and security groups ................................................................................................................. 9
Processing mirrored traﬃc .................................................................................................................. 10
Filters ............................................................................................................................................................ 10
Sessions ........................................................................................................................................................ 11
Traﬃc mirror sources ........................................................................................................................... 11
Connectivity options .................................................................................................................................. 12
Packet format ............................................................................................................................................. 13
Get started ..................................................................................................................................... 15
Prerequisites ................................................................................................................................................ 16
Step 1: Create the traﬃc mirror target ................................................................................................. 16
Step 2: Create the traﬃc mirror ﬁlter ................................................................................................... 16
Step 3: Create the traﬃc mirror session ............................................................................................... 17
Step 4: Analyze the data .......................................................................................................................... 18
Traﬃc Mirroring example scenarios ............................................................................................. 19
Mirror inbound TCP traﬃc to a single appliance ................................................................................ 19
Step 1: Create a traﬃc mirror target ............................................................................................... 20
Step 2: Create a traﬃc mirror ﬁlter .................................................................................................. 20
Step 3: Create a traﬃc mirror session ............................................................................................. 21
Mirror inbound TCP and UDP traﬃc to multiple appliances ............................................................. 21
iii
Amazon Virtual Private Cloud Traﬃc Mirroring
Step 1: Create a traﬃc mirror target for Appliance A .................................................................. 23
Step 2: Create a traﬃc mirror target for Appliance B ................................................................... 23
Step 3: Create a traﬃc mirror ﬁlter with a rule for TCP traﬃc ................................................... 23
Step 4: Create a traﬃc mirror ﬁlter with a rule for UDP traﬃc .................................................. 23
Step 5: Create a traﬃc mirror session for the TCP traﬃc ............................................................ 24
Step 6: Create a traﬃc mirror session for the UDP traﬃc ........................................................... 25
Mirror non-local VPC traﬃc ..................................................................................................................... 25
Step 1: Create a traﬃc mirror target ............................................................................................... 26
Step 2: Create a traﬃc mirror ﬁlter .................................................................................................. 26
Step 3: Create a traﬃc mirror session ............................................................................................. 29
Mirror traﬃc to a Gateway Load Balancer endpoint .......................................................................... 29
Step 1: Create a traﬃc mirror target in Spoke VPC1 .................................................................... 31
Step 2: Create a traﬃc mirror target in Spoke VPC2 .................................................................... 31
Step 3: Create a traﬃc mirror ﬁlter rule ......................................................................................... 31
Step 4: Create a traﬃc mirror session in Spoke VPC1 .................................................................. 32
Step 5: Create a traﬃc mirror session in Spoke VPC2 .................................................................. 32
Work with Traﬃc Mirroring .......................................................................................................... 33
Create or delete a traﬃc mirror target ................................................................................................. 33
View traﬃc mirror targets and modify target tags ............................................................................ 35
Share a traﬃc mirror target .................................................................................................................... 35
Accept or delete a shared traﬃc mirror target .................................................................................... 36
Create, modify, or delete a traﬃc mirror ﬁlter .................................................................................... 37
Create, modify, or delete a traﬃc mirror session ................................................................................ 39
Work with open-source tools ....................................................................................................... 41
Step 1: Install the Suricata software on the EC2 instance target .................................................... 41
Step 2: Create a traﬃc mirror target ..................................................................................................... 42
Step 3: Create a traﬃc mirror ﬁlter ....................................................................................................... 42
Step 4: Create a traﬃc mirror session ................................................................................................... 43
Monitor mirrored traﬃc ................................................................................................................ 44
Traﬃc Mirroring metrics and dimensions ............................................................................................. 44
View Traﬃc Mirroring CloudWatch metrics .......................................................................................... 47
Limitations ..................................................................................................................................... 48
General limitations ..................................................................................................................................... 48
MTU and packet length limitations ........................................................................................................ 49
Traﬃc bandwidth and prioritization limitations .................................................................................. 49
Checksum oﬄoading limitations ............................................................................................................ 50
iv
## How Traﬃc Mirroring works

Amazon Virtual Private Cloud Traﬃc Mirroring
Quotas ............................................................................................................................................ 51
Sessions ........................................................................................................................................................ 51
Targets .......................................................................................................................................................... 51
Filters ............................................................................................................................................................ 52
Throughput .................................................................................................................................................. 52
Packets .......................................................................................................................................................... 52
Sources ......................................................................................................................................................... 52
Identity and access management ................................................................................................. 55
Document history .......................................................................................................................... 57
v
## Targets

Amazon Virtual Private Cloud Traﬃc Mirroring
What is Traﬃc Mirroring?
Traﬃc Mirroring is an Amazon VPC feature that you can use to copy network traﬃc from an elastic 
network interface of type interface. You can then send the traﬃc to out-of-band security and 
monitoring appliances for:
• Content inspection
• Threat monitoring
• Troubleshooting
The security and monitoring appliances can be deployed as individual instances, or as a ﬂeet of 
instances behind either a Network Load Balancer or a Gateway Load Balancer with a UDP listener. 
Traﬃc Mirroring supports ﬁlters and packet truncation, so that you can extract only the traﬃc of 
interest, using the monitoring tools of your choice.
Traﬃc Mirroring concepts
The following are the key concepts for Traﬃc Mirroring:
• Source — The network interface to monitor.
• Filter — A set of rules that deﬁnes the traﬃc that is mirrored.
• Target — The destination for mirrored traﬃc.
• Session — Establishes a relationship between a source, a ﬁlter, and a target.
Work with Traﬃc Mirroring
You can create, access, and manage your traﬃc mirror resources using any of the following:
• AWS Management Console— Provides a web interface that you can use to access your traﬃc 
mirror resources.
• AWS Command Line Interface (AWS CLI) — Provides commands for a broad set of AWS services, 
including Amazon VPC. The AWS CLI is supported on Windows, macOS, and Linux. For more 
information, see AWS Command Line Interface.
Traﬃc Mirroring concepts 1
## Network interfaces

## Network Load Balancer

Amazon Virtual Private Cloud Traﬃc Mirroring
• AWS SDKs — Provide language-speciﬁc APIs. The AWS SDKs take care of many of the connection 
details, such as calculating signatures, handling request retries, and handling errors. For more 
information, see AWS SDKs.
• Query API— Provides low-level API actions that you call using HTTPS requests. Using the Query 
API is the most direct way to access Amazon VPC. However, it requires that your application 
handle low-level details such as generating the hash to sign the request and handling errors. For 
more information, see Amazon VPC actions in the Amazon EC2 API Reference.
Traﬃc Mirroring beneﬁts
Traﬃc Mirroring oﬀers the following beneﬁts:
• Simpliﬁed operation — Mirror any range of your VPC traﬃc without having to manage packet 
forwarding agents on your EC2 instances.
• Enhanced security — Capture packets at the elastic network interface, which cannot be disabled 
or tampered with from a user space.
• Increased monitoring options — Send your mirrored traﬃc to any security device.
Regional availability
Traﬃc Mirroring is available in all Regions.
Supported instance types
Instance types in the following instance families are supported as Traﬃc Mirroring source.
Virtualized instances
Virtualized instance types in the following instance families are supported as Traﬃc Mirroring 
source:
• General purpose: A1 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | M6g | M6gd | M6i 
| M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex | Mac1 | Mac2 | Mac2-m1ultra | Mac2-
m2 | Mac2-m2pro | T3 | T3a | T4g
• Compute optimized: C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in | 
C7a | C7g | C7gd | C7i | C7i-ﬂex
Traﬃc Mirroring beneﬁts 2
## Gateway Load Balancer endpoints

Amazon Virtual Private Cloud Traﬃc Mirroring
• Memory optimized: R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i | R6id 
| R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | 
U-24tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb | U7inh-32tb | X1 | 
X1e | X2gd | X2idn | X2iedn | X2iezn | z1d
• Storage optimized: D2 | D3 | D3en | H1 | I3 | I3en | I4g | I4i | I7i | Im4gn | Is4gen
• Accelerated computing: DL1 | DL2q | F1 | F2 | G3 | G4ad | G4dn | G5 | G5g | G6 | G6e | G6f | Gr6 | 
Gr6f | Inf1 | Inf2 | P3 | P3dn | P4d | P4de | P5 | P5e | Trn1 | Trn1n | VT1
• High-performance computing: Hpc6a | Hpc6id | Hpc7a
Bare metal instances
Bare metal instance types in the following instance families are supported as Traﬃc Mirroring 
source:
• General purpose: M5 | M5d | M6g | M6gd | Mac1 | Mac2 | Mac2-m1ultra | Mac2-m2 | Mac2-
m2pro | A1
• Compute optimized: C5 | C5d | C6g | C6gd
• Memory optimized: R5 | R5b | R5d | R6g | R6gd | X2gd | z1d
• Storage optimized: I3
• Accelerated computing: G5g
• Previous generation: A1
Note
Only Nitro v2 bare-metal instances are supported as Traﬃc Mirroring source. Bare metal 
instances of any other Nitro version are not supported as Traﬃc Mirroring source.
Pricing
You are charged on an hourly basis for each active traﬃc mirror session. You'll continue to be 
charged for Traﬃc Mirroring until you delete all active traﬃc mirror sessions. For example, you'll 
still be charged in the following scenarios:
• You detached the network interface from the mirror source
Bare metal instances 3
## VXLAN encapsulation

## Routing and security groups

Amazon Virtual Private Cloud Traﬃc Mirroring
• You stopped or terminated the mirror source
• You changed the instance type of the mirror source to an unsupported instance type
Data transfer charges apply. If your traﬃc mirroring targets are behind a gateway or network load 
balancer, data processing for the load balancing services also applies.
For information about pricing for Traﬃc Mirroring, see Network Analysis on the Amazon VPC 
pricing page.
Pricing 4
## Processing mirrored traﬃc

## Filters

Amazon Virtual Private Cloud Traﬃc Mirroring
How Traﬃc Mirroring works
Traﬃc Mirroring copies inbound and outbound traﬃc from the network interfaces that are 
attached to your instances. You can send the mirrored traﬃc to the network interface of another 
instance, a Network Load Balancer that has a UDP listener, or a Gateway Load Balancer that has a 
UDP listener. The traﬃc mirror source and the traﬃc mirror target (monitoring appliance) can be 
in the same VPC. Or they can be in a diﬀerent VPCs that are connected through intra-Region VPC 
peering, a transit gateway, or by a Gateway Load Balancer endpoint to connect to a Gateway Load 
Balancer in a diﬀerent VPC.
Consider the following scenario, where you mirror traﬃc from two sources (Source A and Source B) 
to a single traﬃc mirror target (Target D). After you create the traﬃc mirror session, any traﬃc that 
matches the ﬁlter rules is encapsulated in a VXLAN header. It is then sent to the target.
The following procedures are required:
• Identify the traﬃc mirror source (Source A)
• Identify the traﬃc mirror source (Source B)
• Conﬁgure the traﬃc mirror target (Target D)
• Conﬁgure the traﬃc mirror ﬁlter (Filter A)
• Conﬁgure the traﬃc mirror session for Source A, Filter A, and Target D
• Conﬁgure the traﬃc mirror session for Source B, Filter A, and Target D
Contents
• Understand traﬃc mirror target concepts
• Understand traﬃc mirror ﬁlter concepts
• Understand traﬃc mirror session concepts
5
## Sessions

## Traﬃc mirror sources

Amazon Virtual Private Cloud Traﬃc Mirroring
• Understand traﬃc mirror source and target connectivity options
• Understanding traﬃc mirror packet format
Understand traﬃc mirror target concepts
A traﬃc mirror target is the destination for mirrored traﬃc. In Amazon VPC, traﬃc mirroring allows 
you to copy network traﬃc from an elastic network interface (ENI) and send it to a traﬃc mirror 
target for monitoring and analysis purposes.
You can use the following resources as traﬃc mirror targets:
• Network interfaces of type interface
• Network Load Balancers
• Gateway Load Balancer endpoints
For high availability, we recommend that you use a Network Load Balancer or a Gateway Load 
Balancer endpoint as a mirror target.
You might experience out-of-order delivery of mirrored packets when you use a Network Load 
Balancer or Gateway Load Balancer endpoint as your traﬃc mirror target. If your monitoring 
appliance can't handle out-of-order packets, we recommend using a network interface as your 
traﬃc mirror target.
A traﬃc mirror target can be owned by an AWS account that is diﬀerent from the traﬃc mirror 
source.
After you create a traﬃc mirror target, you add it to a traﬃc mirror session. You can use a traﬃc 
mirror target in more than one traﬃc mirror session. For more information, see the section called 
“Sessions”.
Note
If the underlying resource chosen as the target is deleted, we stop traﬃc mirroring for any 
sessions that use that target. To update a traﬃc mirroring target and resume the traﬃc 
mirroring session, you can use modify-traﬃc-mirror-session.
Targets 6
## Connectivity options

Amazon Virtual Private Cloud Traﬃc Mirroring
Network interfaces
The following diagram shows a traﬃc mirror session where the traﬃc mirror target is a network 
interface for an EC2 instance. Traﬃc Mirroring ﬁlters the traﬃc from the network interface of the 
mirror source and sends the accepted mirrored traﬃc to the mirror target.
Network Load Balancer
The following diagram shows a traﬃc mirror session where the traﬃc mirror target is a Network 
Load Balancer. You install the monitoring software on the target instances, and then register them 
with the load balancer. Traﬃc Mirroring ﬁlters the traﬃc from the network interface of the mirror 
source and sends the accepted mirrored traﬃc to the load balancer. The load balancer sends the 
mirrored traﬃc to the target instances.
Network interfaces 7
## Packet format

Amazon Virtual Private Cloud Traﬃc Mirroring
Considerations
• Traﬃc mirroring can't occur unless the load balancer has UDP listeners on port 4789. If you 
remove the UDP listeners, Traﬃc Mirroring fails without an error indication.
• To improve availability and fault tolerance, we recommend that you select at least two 
Availability Zones when you create the Network Load Balancer, and that you register target 
instances in each selected Availability Zone.
• We recommend that you enable cross-zone load balancing for your Network Load Balancer. If 
all registered target instances in an Availability Zone become unhealthy and cross-zone load 
balancing is disabled, the load balancer can't send the mirrored traﬃc to target instances in 
another Availability Zone. If you enable cross-zone load balancing, the load balancer can send 
the mirrored traﬃc to healthy target instances in another Availability Zone.
• If you select an additional Availability Zone for your Network Load Balancer after you create it, 
Traﬃc Mirroring does not send mirrored traﬃc to target instances in the new Availability Zone 
unless you enable cross-zone load balancing.
• When the Network Load Balancer removes a load balancer node from the DNS table, Traﬃc 
Mirroring continues to send the mirrored traﬃc to that node.
Gateway Load Balancer endpoints
The following diagram shows a traﬃc mirror session where the traﬃc mirror target is a Gateway 
Load Balancer endpoint. The mirror source is in the service consumer VPC and the Gateway 
Load Balancer is in the service provider VPC. You install the monitoring software on the target 
appliances, and then register them with the load balancer. Traﬃc Mirroring ﬁlters the traﬃc from 
the network interface of the mirror source and sends the accepted mirrored traﬃc to the Gateway 
Load Balancer endpoint. The load balancer sends the mirrored traﬃc to the target appliances.
Gateway Load Balancer endpoints 8
Amazon Virtual Private Cloud Traﬃc Mirroring
Considerations
• A listener for Gateway Load Balancers listens for all IP packets across all ports, and then forwards 
traﬃc to the target group.
• To improve availability and fault tolerance, we recommend that you select at least two 
Availability Zones when you create the Gateway Load Balancer, and that you register target 
appliances in each selected Availability Zone.
• If all registered target appliances in an Availability Zone become unhealthy and cross-zone load 
balancing is disabled, the load balancer can't send the mirrored traﬃc to target appliances in 
another Availability Zone. If you enable cross-zone load balancing, the load balancer can send 
the mirrored traﬃc to healthy target appliances in another Availability Zone.
• The maximum MTU supported by the Gateway Load Balancer is 8500. Traﬃc Mirroring adds 54 
bytes of additional headers to the original packet payload when using IPv4, and 74 bytes when 
using IPv6. Therefore, the maximum packet size that can be delivered to an appliance without 
truncation is 8500 – 54 = 8446 when using IPv4, or 8500 – 74 = 8426 when using IPv6.
• You can use the BytesProcessed and PacketsDropped CloudWatch metrics for VPC 
endpoints to monitor the volume of traﬃc being sent over the Gateway Load Balancer endpoint. 
You can also use CloudWatch metrics for Traﬃc Mirroring. For more information, see Monitor 
mirrored traﬃc.
VXLAN encapsulation
Mirrored traﬃc is encapsulated in VXLAN packets and then routed to the mirror target. The 
security groups for a traﬃc mirror target must allow VXLAN traﬃc (UDP port 4789) from the traﬃc 
mirror source. The route table for the subnet with the traﬃc mirror source must have a route that 
sends the mirrored traﬃc to the traﬃc mirror target. The monitoring software that you run on the 
mirror target must be able to process encapsulated VXLAN packets.
Routing and security groups
Encapsulated mirror traﬃc is routed to the traﬃc mirror target by using the VPC route table. Make 
sure that your route table is conﬁgured to send the mirrored traﬃc to the traﬃc mirror target.
Inbound traﬃc that is dropped at the traﬃc mirror source, because of the inbound security group 
rules or the inbound network ACL rules, is not mirrored.
VXLAN encapsulation 9
## Get started

Amazon Virtual Private Cloud Traﬃc Mirroring
Mirrored outbound traﬃc is not subject to the outbound security group rules for the traﬃc mirror 
source.
Processing mirrored traﬃc
You can use open-source tools or choose a monitoring solution available on AWS Marketplace. You 
can stream mirrored traﬃc to any network packet collector or analytics tool, without having to 
install vendor-speciﬁc agents.
Understand traﬃc mirror ﬁlter concepts
A traﬃc mirror ﬁlter is a set of inbound and outbound rules that determines which traﬃc is copied 
from the traﬃc mirror source and sent to the traﬃc mirror target. You can also choose to mirror 
certain network services traﬃc, including Amazon DNS. When you add network services traﬃc, all 
traﬃc (inbound and outbound) related to that network service is mirrored.
We evaluate traﬃc mirror ﬁlter rules from the lowest value to the highest value. The ﬁrst rule that 
matches the traﬃc determines whether the traﬃc is mirrored. If you don't add any rules, then no 
traﬃc is mirrored.
For example, in the following set of ﬁlter rules, rule 10 ensures that SSH traﬃc from my network to 
my VPC is not mirrored and rule 20 mirrors all other IPv4 TCP traﬃc.
Number Rule 
action
Protocol Source 
port range
Destinati 
on port 
range
Source 
CIDR block
Destinati 
on CIDR 
block
10 reject TCP (6)   22 my-
network
vpc-cidr
20 accept TCP (6)     0.0.0.0/0 0.0.0.0/0
In the following set of ﬁlter rules, rule 10 mirrors HTTPS traﬃc from all IPv4 addresses and rule 20 
mirrors HTTPS traﬃc from all IPv6 addresses.
Processing mirrored traﬃc 10
## Prerequisites

## Step 1: Create the traﬃc mirror target

## Step 2: Create the traﬃc mirror ﬁlter

Amazon Virtual Private Cloud Traﬃc Mirroring
Number Rule 
action
Protocol Source 
port range
Destinati 
on port 
range
Source 
CIDR block
Destinati 
on CIDR 
block
10 accept TCP (6)   443 0.0.0.0/0 0.0.0.0/0
20 accept TCP (6)   443 ::/0 ::/0
Note that if you don't add outbound rules, then no outbound traﬃc is mirrored.
Understand traﬃc mirror session concepts
A traﬃc mirror session establishes a relationship between a traﬃc mirror source and a traﬃc mirror 
target. Traﬃc mirror sessions are evaluated based on the ascending session number that you deﬁne 
when you create the session.
A traﬃc mirror session contains the following resources:
• A traﬃc mirror source
• A traﬃc mirror target
• A traﬃc mirror ﬁlter
Each packet is mirrored once. However, you can use multiple traﬃc mirror sessions on the same 
mirror source. This is useful if you want to send a subset of the mirrored traﬃc from a traﬃc mirror 
source to multiple tools. For example, you can ﬁlter HTTP traﬃc in a higher priority traﬃc mirror 
session and send it to a speciﬁc monitoring appliance. At the same time, you can ﬁlter all other TCP 
traﬃc in a lower priority traﬃc mirror session and send it to another monitoring appliance.
Traﬃc mirror sources
A traﬃc mirror source is the network interface of type interface. For example, a network 
interface for an EC2 instance or an RDS instance.
A network interface can't be used as a traﬃc mirror source if the same Elastic network interface is 
already in use in an existing traﬃc mirror target.
Sessions 11
## Step 3: Create the traﬃc mirror session

Amazon Virtual Private Cloud Traﬃc Mirroring
Note
If the source network interface gets deleted, AWS deletes the traﬃc mirroring session.
Traﬃc Mirroring is not available on all instance types.
Virtualized instance types in the following instance families are supported as Traﬃc Mirroring 
source:
• General purpose: A1 | M4 | M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | M6g | M6gd | M6i 
| M6id | M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-ﬂex | Mac1 | Mac2 | Mac2-m1ultra | Mac2-
m2 | Mac2-m2pro | T3 | T3a | T4g
• Compute optimized: C4 | C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in | 
C7a | C7g | C7gd | C7i | C7i-ﬂex
• Memory optimized: R4 | R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i | R6id 
| R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | 
U-24tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb | U7inh-32tb | X1 | 
X1e | X2gd | X2idn | X2iedn | X2iezn | z1d
• Storage optimized: D2 | D3 | D3en | H1 | I3 | I3en | I4g | I4i | I7i | Im4gn | Is4gen
• Accelerated computing: DL1 | DL2q | F1 | F2 | G3 | G4ad | G4dn | G5 | G5g | G6 | G6e | G6f | Gr6 | 
Gr6f | Inf1 | Inf2 | P3 | P3dn | P4d | P4de | P5 | P5e | Trn1 | Trn1n | VT1
• High-performance computing: Hpc6a | Hpc6id | Hpc7a
Understand traﬃc mirror source and target connectivity 
options
Connecting traﬃc mirror sources and targets in diﬀerent VPCs can be useful for monitoring and 
analyzing network traﬃc across multiple environments. This allows you to centralize your network 
monitoring and security analysis, even if your application infrastructure is spread across diﬀerent 
VPCs or AWS accounts.
The traﬃc mirror source and the traﬃc mirror target (monitoring appliance) can be in the same 
VPC or diﬀerent VPCs and can be connected using the following resources:
• An intra-Region VPC peering connection.
Connectivity options 12
## Step 4: Analyze the data

Amazon Virtual Private Cloud Traﬃc Mirroring
• A transit gateway.
• A Gateway Load Balancer endpoint.
The traﬃc mirror target can be owned by an AWS account that is diﬀerent from the traﬃc mirror 
source.
The mirrored traﬃc is sent to the traﬃc mirror target using the source VPC route table. Before you 
conﬁgure Traﬃc Mirroring, make sure that the traﬃc mirror source can route to the traﬃc mirror 
target.
The following table describes the available resource conﬁgurations.
Source 
owner
Source VPC Target 
owner
Target VPC Connectivity option
Account A VPC 1 Account A VPC1 No additional conﬁguration
Account A VPC 1 Account A VPC 2 Intra-Region peering or a 
transit gateway or Gateway 
Load Balancer endpoint
Account A VPC 1 Account B VPC 2 Cross-account intra-Region 
peering connection, a transit 
gateway, or a Gateway Load 
Balancer endpoint
Account A VPC 1 Account B VPC 1 VPC sharing
Understanding traﬃc mirror packet format
Mirrored traﬃc is encapsulated with a VXLAN header. All appliances that receive traﬃc directly 
with this feature should be able parse a VXLAN-encapsulated packet, as shown in the following 
example:
Packet format 13
## Traﬃc Mirroring example scenarios

## Mirror inbound TCP traﬃc to a single appliance

Amazon Virtual Private Cloud Traﬃc Mirroring
For more information about the VXLAN protocol, see RFC 7348.
The following ﬁelds apply to Traﬃc Mirroring:
• VXLAN ID — The virtual network ID that you can assign to a traﬃc mirror session. If you do not 
assign a value, we assign a random value that is unique to all sessions in the account.
• Source IP address — The primary IP address of the source network interface.
• Source port — The port is determined by a 5-tuple hash of the original L2 packet, for ICMP, 
TCP, and UDP ﬂows. For other ﬂows, the port is determined by a 3-tuple hash of the original L2 
packet.
• Destination IP address — The primary IP address of the appliance, Gateway Load Balancer 
endpoint, or Network Load Balancer (when the appliance is deployed behind one).
• Destination port — The port is 4789, which is the well known port for VXLAN.
Appliances that received mirrored traﬃc through a Gateway Load Balancer should be able to 
parse both outer GENEVE encapsulation (from Gateway Load Balancer) and an inner VXLAN 
encapsulation (from VPC Traﬃc Mirroring) to retrieve the original L3 packet. The following shows 
an example:
Packet format 14
## Step 1: Create a traﬃc mirror target

## Step 2: Create a traﬃc mirror ﬁlter

Amazon Virtual Private Cloud Traﬃc Mirroring
Get started using Traﬃc Mirroring to monitor network 
traﬃc
To get started using Amazon VPC Traﬃc Mirroring, you'll need a VPC with at least one elastic 
network interface (ENI) that you want to mirror traﬃc from. In this section, you'll create a traﬃc 
mirror target and you'll create a traﬃc mirror session, which deﬁnes the parameters of the traﬃc 
mirroring operation, such as the source ENI, the mirror target, and any ﬁltering rules. Once these 
components are in place, you'll start mirroring traﬃc to the target for monitoring and analysis.
A mirror session is a connection between a mirror source and a mirror target. In the following 
diagram, both the mirror source and the mirror target are EC2 instances. The mirror ﬁlter 
determines which network packets are mirrored. For example, you can add inbound and outbound 
rules to the ﬁlter such that it rejects SSH traﬃc but accepts all other traﬃc. Traﬃc Mirroring 
applies the ﬁlter rules, and then copies the accepted traﬃc from the network interface of the 
mirror source to the network interface of the mirror target. You can run your capture and analysis 
tools on the packets delivered to the mirror target.
Tasks
• Prerequisites
• Step 1: Create the traﬃc mirror target
• Step 2: Create the traﬃc mirror ﬁlter
• Step 3: Create the traﬃc mirror session
• Step 4: Analyze the data
15
## Step 3: Create a traﬃc mirror session

## Mirror inbound TCP and UDP traﬃc to multiple appliances

Amazon Virtual Private Cloud Traﬃc Mirroring
Prerequisites
• The traﬃc mirror source is a network interface that you want to mirror traﬃc from. The traﬃc 
mirror target is the destination for the mirrored traﬃc, such as an EC2 instance.
• The traﬃc mirror source and traﬃc mirror target must be in the same VPC or in VPCs that are 
connected (for example, using VPC peering or a transit gateway).
• The traﬃc mirror target must allow traﬃc to UDP port 4789.
• The traﬃc mirror source must have a route table entry for the traﬃc mirror target.
• Security group rules and network ACL rules on the traﬃc mirror target cannot drop the mirrored 
traﬃc from the traﬃc mirror source.
Step 1: Create the traﬃc mirror target
Use an EC2 instance as the destination for the mirrored traﬃc.
To create a traﬃc mirror target
1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
2. In the Region selector, choose the AWS Region that you used when you created the EC2 
instance.
3. On the navigation pane, choose Traﬃc Mirroring, Mirror targets.
4. Choose Create traﬃc mirror target.
5. (Optional) For Name tag, enter a name for the traﬃc mirror target.
6. (Optional) For Description, enter a description for the traﬃc mirror target.
7. For Target type, choose Network Interface.
8. For Target, choose the network interface of the EC2 instance.
9. (Optional) For each tag to add, choose Add new tag and enter the tag key and tag value.
10. Choose Create.
Step 2: Create the traﬃc mirror ﬁlter
A traﬃc mirror ﬁlter contains one or more traﬃc mirror rules, and a set of network services. The 
ﬁlters and rules that you add deﬁne the traﬃc that is mirrored.
Prerequisites 16
Amazon Virtual Private Cloud Traﬃc Mirroring
To create a traﬃc mirror ﬁlter
1. On the navigation pane, choose Traﬃc Mirroring, Mirror ﬁlters.
2. Choose Create traﬃc mirror ﬁlter.
3. (Optional For Name tag, enter a name for the traﬃc mirror ﬁlter.
4. (Optional) For Description, enter a description for the traﬃc mirror ﬁlter.
5. For each rule, inbound or outbound, choose Add rule, and then specify the following 
information:
• Number: The rule priority.
• Rule action: Indicates whether to accept or reject the packets.
• Protocol: The protocol.
• (Optional) Source port range: The source port range.
• (Optional) Destination port range: The destination port range.
• Source CIDR block: The source CIDR block.
• Destination CIDR block: The destination CIDR block.
• Description: A description for the rule.
6. (Optional) For each tag to add, choose Add new tag and enter the tag key and tag value.
7. Choose Create.
Step 3: Create the traﬃc mirror session
Create a traﬃc mirror session that sends mirrored packets from the source to a target so that you 
can monitor and analyze traﬃc.
To create a traﬃc mirror session
1. In the navigation pane, choose Traﬃc Mirroring, Mirror sessions.
2. Choose Create traﬃc mirror session.
3. (Optional) For Name tag, enter a name for the traﬃc mirror session.
4. (Optional) For Description, enter a description for the traﬃc mirror session.
5. For Mirror source, choose the network interface of the mirror source.
6. For Mirror target, choose your traﬃc mirror target.
7. For Additional settings, do the following:
Step 3: Create the traﬃc mirror session 17
Amazon Virtual Private Cloud Traﬃc Mirroring
a. For Session number, enter 1, which is the highest priority.
b. (Optional) For VNI, enter the VXLAN ID to use for the traﬃc mirror session. For more 
information about the VXLAN protocol, see RFC 7348.
If you do not enter a value, we assign a random unused number.
c. (Optional) For Packet length, enter the number of bytes in each packet to mirror.
To mirror the entire packet, do not enter a value. To mirror only a portion of each packet, 
set this value to the number of bytes to mirror. For example, if you set this value to 100, the 
ﬁrst 100 bytes after the VXLAN header that meet the ﬁlter criteria are copied to the target.
d. For Filter, choose your traﬃc mirror ﬁlter.
8. (Optional) For each tag to add, choose Add new tag and enter the tag key and tag value.
9. Choose Create.
Step 4: Analyze the data
After the mirrored traﬃc is copied to the traﬃc mirror target, you can use a tool from the AWS 
Partner Network to analyze the data.
Step 4: Analyze the data 18
Amazon Virtual Private Cloud Traﬃc Mirroring
Traﬃc Mirroring example conﬁguration scenarios
This section consists of step-by-step instructions you can use to conﬁgure Traﬃc Mirroring for the 
following scenarios:
• Mirror inbound TCP traﬃc to a single appliance
• Mirror inbound TCP and UDP traﬃc to multiple appliances
• Mirror non-local VPC traﬃc
• Mirror traﬃc to a Gateway Load Balancer endpoint
To mirror traﬃc from multiple network interfaces, see VPC Traﬃc Mirroring Source Automation 
Application on github.
Example: Mirror inbound TCP traﬃc to a single monitoring 
appliance
Consider the scenario where you want to mirror inbound TCP traﬃc on an instance, and send it to a 
single monitoring appliance. You need the following traﬃc mirror resources for this example.
Resources
• A traﬃc mirror target for the appliance (Target A)
• A traﬃc mirror ﬁlter with a traﬃc mirror rule for the TCP inbound traﬃc (Filter 1)
Mirror inbound TCP traﬃc to a single appliance 19
Amazon Virtual Private Cloud Traﬃc Mirroring
• A traﬃc mirror session that has the following:
• A traﬃc mirror source
• A traﬃc mirror target for the appliance
• A traﬃc mirror ﬁlter with a traﬃc mirror rule for the TCP inbound traﬃc
Step 1: Create a traﬃc mirror target
Create a traﬃc mirror target (Target A) for the monitoring appliance. Depending on your 
conﬁguration, the target is one of the following types:
• The network interface of the monitoring appliance
• The Network Load Balancer when the appliance is deployed behind one
• The Gateway Load Balancer endpoint when the appliance is deployed behind a Gateway Load 
Balancer
For more information, see the section called “Create or delete a traﬃc mirror target”.
Step 2: Create a traﬃc mirror ﬁlter
Create a traﬃc mirror ﬁlter (Filter 1) that has the following inbound rule. For more information, see
the section called “Create, modify, or delete a traﬃc mirror ﬁlter”.
Option Value
Rule action Accept
Protocol TCP
Source port range  
Destination port range  
Source CIDR block 0.0.0.0/0
Destination CIDR block 0.0.0.0/0
Description TCP Rule
Step 1: Create a traﬃc mirror target 20
Amazon Virtual Private Cloud Traﬃc Mirroring
Step 3: Create a traﬃc mirror session
Create and conﬁgure a traﬃc mirror session with the following options. For more information, see
the section called “Create, modify, or delete a traﬃc mirror session”.
Option Value
Mirror source The network interface of the instance that you 
want to monitor.
Mirror target Target A
Filter Filter 1
Example: Mirror inbound TCP and UDP traﬃc to multiple 
appliances
Consider the scenario where you want to mirror inbound TCP and UDP traﬃc on an instance. But 
you want to send the TCP traﬃc to one appliance (Appliance A), and the UDP traﬃc to a second 
appliance (Appliance B). You need the following traﬃc mirror entities for this example.
Step 3: Create a traﬃc mirror session 21
Amazon Virtual Private Cloud Traﬃc Mirroring
Resources
• A traﬃc mirror target for Appliance A (Target A)
• A traﬃc mirror target for Appliance B (Target B)
• A traﬃc mirror ﬁlter with a traﬃc mirror rule for the TCP inbound traﬃc (Filter 1)
• A traﬃc mirror ﬁlter with a traﬃc mirror rule for the UDP inbound traﬃc (Filter 2)
• A traﬃc mirror session that has the following:
• A traﬃc mirror source
• A traﬃc mirror target (Target A) for Appliance A
• A traﬃc mirror ﬁlter (Filter 1) with a traﬃc mirror rule for the TCP inbound traﬃc
• A traﬃc mirror session that has the following:
• A traﬃc mirror source
• A traﬃc mirror target (Target B) for Appliance B
• A traﬃc mirror ﬁlter (Filter 2) with a traﬃc mirror rule for the UDP inbound traﬃc
Mirror inbound TCP and UDP traﬃc to multiple appliances 22
Amazon Virtual Private Cloud Traﬃc Mirroring
Step 1: Create a traﬃc mirror target for Appliance A
Create a traﬃc mirror target for Appliance A (Target A). Depending on your conﬁguration, the 
target is one of the following types:
• The network interface of the monitoring appliance
• The Network Load Balancer when the appliance is deployed behind one
• The Gateway Load Balancer endpoint when the appliance is deployed behind a Gateway Load 
Balancer
For more information, see the section called “Create or delete a traﬃc mirror target”.
Step 2: Create a traﬃc mirror target for Appliance B
Create a traﬃc mirror target (Target B) for Appliance B. Depending on your conﬁguration, the 
target is one of the following types:
• The network interface of the monitoring appliance
• The Network Load Balancer when the appliance is deployed behind one
• The Gateway Load Balancer endpoint when the appliance is deployed behind a Gateway Load 
Balancer
For more information, see the section called “Create or delete a traﬃc mirror target”.
Step 3: Create a traﬃc mirror ﬁlter with a rule for TCP traﬃc
Create a traﬃc mirror ﬁlter (Filter 1) with the following inbound rule for TCP traﬃc. For more 
information, see the section called “Create, modify, or delete a traﬃc mirror ﬁlter”
Option Value
Rule action Accept
Protocol TCP
Source port range  
Destination port range  
Step 1: Create a traﬃc mirror target for Appliance A 23
Amazon Virtual Private Cloud Traﬃc Mirroring
Option Value
Source CIDR block 0.0.0.0/0
Destination CIDR block 0.0.0.0/0
Description TCP Rule
Step 4: Create a traﬃc mirror ﬁlter with a rule for UDP traﬃc
Create a traﬃc mirror ﬁlter (Filter 2) with the following inbound rule for UDP traﬃc. For more 
information, see the section called “Create, modify, or delete a traﬃc mirror ﬁlter”
Option Value
Rule action Accept
Protocol UDP
Source port range  
Destination port range  
Source CIDR block 0.0.0.0/0
Destination CIDR block 0.0.0.0/0
Description UDP Rule
Step 5: Create a traﬃc mirror session for the TCP traﬃc
Create and conﬁgure a traﬃc mirror session with the following options. For more information, see
the section called “Create, modify, or delete a traﬃc mirror session”.
Option Value
Mirror source The network interface of the instance that you 
want to monitor.
Step 4: Create a traﬃc mirror ﬁlter with a rule for UDP traﬃc 24
Amazon Virtual Private Cloud Traﬃc Mirroring
Option Value
Mirror target Target A
Filter Filter 1
Session number 1
Step 6: Create a traﬃc mirror session for the UDP traﬃc
Create and conﬁgure a traﬃc mirror session with the following options. For more information, see
the section called “Create, modify, or delete a traﬃc mirror session”.
Option Value
Mirror source The network interface of the instance that you 
want to monitor.
Mirror target Target B
Filter Filter 2
Session number 2
Example: Mirror non-local VPC traﬃc
Consider the scenario where you want to monitor traﬃc leaving your VPC or traﬃc whose source is 
outside your VPC. In this case, you will mirror all traﬃc except traﬃc passing within your VPC and 
send it to a single monitoring appliance. You need the following traﬃc mirror resources:
• A traﬃc mirror target for the appliance (Target A)
• A traﬃc mirror ﬁlter that has two sets of rules for outbound and inbound traﬃc. For outbound 
traﬃc, it will reject all packets which have a destination IP in the VPC CIDR block and accept all 
other outbound packets. For inbound traﬃc, it will reject all packets which have a source IP in the 
VPC CIDR block and accept all other inbound packets.
• A traﬃc mirror session that has the following:
• A traﬃc mirror source
Step 6: Create a traﬃc mirror session for the UDP traﬃc 25
Amazon Virtual Private Cloud Traﬃc Mirroring
• A traﬃc mirror target for the appliance (Target A)
• A traﬃc mirror ﬁlter with a traﬃc mirror rule for the TCP inbound traﬃc (Filter F)
In this example, the VPC CIDR block is 10.0.0.0/16.
Step 1: Create a traﬃc mirror target
Create a traﬃc mirror target (Target A) for the monitoring appliance. Depending on your 
conﬁguration, the target is one of the following types:
• The network interface of the monitoring appliance
• The Network Load Balancer when the appliance is deployed behind one
• The Gateway Load Balancer endpoint when the appliance is deployed behind a Gateway Load 
Balancer
For more information, see the section called “Create or delete a traﬃc mirror target”.
Step 2: Create a traﬃc mirror ﬁlter
Create a traﬃc mirror ﬁlter (Filter F) that has the following rules. For more information, see the 
section called “Create, modify, or delete a traﬃc mirror ﬁlter”.
Outbound traﬃc mirror ﬁlter rules
Create the following outbound rules:
• Reject all outbound packets which have a destination IP in the VPC CIDR block
• Accept all other outbound packets (destination CIDR block 0.0.0.0/0)
Option Value
Rule number 10
Rule action Reject
Protocol All
Step 1: Create a traﬃc mirror target 26
Amazon Virtual Private Cloud Traﬃc Mirroring
Option Value
Source port range  
Destination port range  
Source CIDR block 0.0.0.0/0
Destination CIDR block 10.0.0.0/16
Description Reject all intra-VPC traﬃc
Option Value
Rule number 20
Rule action Accept
Protocol All
Source port range  
Destination port range  
Source CIDR block 0.0.0.0/0
Destination CIDR block 0.0.0.0/0
Description Accept all outbound traﬃc
Inbound traﬃc mirror ﬁlter rules
Create the following inbound rules:
• Reject all inbound packets which have a source IP in the VPC CIDR block
• Accept all other inbound packets (source CIDR block 0.0.0.0/0)
Step 2: Create a traﬃc mirror ﬁlter 27
Amazon Virtual Private Cloud Traﬃc Mirroring
Option Value
Rule number 10
Rule action Reject
Protocol All
Source port range  
Destination port range  
Source CIDR block 10.0.0.0/16
Destination CIDR block 0.0.0.0/0
Description Reject all intra-VPC traﬃc
Option Value
Rule number 20
Rule action Accept
Protocol All
Source port range  
Destination port range  
Source CIDR block 0.0.0.0/0
Destination CIDR block 0.0.0.0/0
Description Accept all inbound traﬃc
Step 2: Create a traﬃc mirror ﬁlter 28
Amazon Virtual Private Cloud Traﬃc Mirroring
Step 3: Create a traﬃc mirror session
Create and conﬁgure a traﬃc mirror session with the following options. For more information, see
the section called “Create, modify, or delete a traﬃc mirror session”.
Option Value
Mirror source The network interface of the instance that you 
want to monitor.
Mirror target Target A
Filter Filter F
Example: Mirror traﬃc to appliances behind a Gateway Load 
Balancer using Gateway Load Balancer endpoints
You can deploy a Gateway Load Balancer (GWLB) and Gateway Load Balancer endpoint (GWLBe) to 
securely send mirror traﬃc across VPC and accounts. The GWLBe is a VPC endpoint that provides 
private connectivity between VPC with the mirror sources and the monitoring appliances deployed 
behind the GWLB.
The following diagram shows a deployment of a GWLB for traﬃc mirroring utilizing GWLBe 
interfaces. The GWLB is deployed in a centralized Service VPC with multiple appliances as targets. 
The GWLB is set up for each Availability Zone that the customer wants to monitor traﬃc, and it 
can conﬁgure their GWLB with cross-zone load balancing as an option to protect against single 
Availability Zone failures. In the spoke VPCs, GWLBe interfaces are deployed in each spoke VPC. 
These endpoints are connected to the GWLB to send traﬃc from the spoke VPC to the Service VPC.
Step 3: Create a traﬃc mirror session 29
Amazon Virtual Private Cloud Traﬃc Mirroring
Consider the scenario where you want to mirror inbound TCP traﬃc on an instance and then send 
it to a Gateway Load Balancer using a Gateway Load Balancer endpoint. You need the following 
Traﬃc Mirroring entities for this example:
• A Traﬃc Mirroring target for the Gateway Load Balancer endpoint (Target A) in Spoke VPC1
• A Traﬃc Mirroring target for the Gateway Load Balancer endpoint (Target B) in Spoke VPC2
• A Traﬃc Mirroring ﬁlter with a Traﬃc Mirroring rule for the TCP inbound traﬃc (Filter 1) for the 
Gateway Load Balancer endpoint
• A Traﬃc Mirroring session for Spoke VPC1 that has the following:
• A Traﬃc Mirroring source
• A Traﬃc Mirroring target (Target A) for the Gateway Load Balancer endpoint
• A Traﬃc Mirroring ﬁlter (Filter 1) with a Traﬃc Mirroring rule for the TCP inbound traﬃc
• A Traﬃc Mirroring session for Spoke VPC2 that has the following:
• A Traﬃc Mirroring source
• A Traﬃc Mirroring target (Target B) for the Gateway Load Balancer endpoint
• A Traﬃc Mirroring ﬁlter (Filter 1) with a Traﬃc Mirroring rule for the TCP inbound traﬃc
Mirror traﬃc to a Gateway Load Balancer endpoint 30
Amazon Virtual Private Cloud Traﬃc Mirroring
Step 1: Create a traﬃc mirror target in Spoke VPC1
Create a traﬃc mirror target (Target A) for the Gateway Load Balancer endpoint in Spoke VPC1. For 
more information, see Create or delete a traﬃc mirror target.
The Gateway Load Balancer endpoint will be the target when the monitoring appliances are 
deployed behind a Gateway Load Balancer.
Step 2: Create a traﬃc mirror target in Spoke VPC2
Create a traﬃc mirror target (Target B) for the Gateway Load Balancer endpoint in Spoke VPC1. For 
more information, see Create or delete a traﬃc mirror target.
The Gateway Load Balancer endpoint will be the target when the monitoring appliances are 
deployed behind a Gateway Load Balancer.
Step 3: Create a traﬃc mirror ﬁlter rule
Create a traﬃc mirror ﬁlter (Filter 1) that has the following inbound rule. For more information on 
creating a ﬁlter, see Create, modify, or delete a traﬃc mirror ﬁlter.
Option Value
Rule action Accept
Protocol TCP
Source port range  
Destination port range  
Source CIDR block 0.0.0.0/0
Destination CIDR block 0.0.0.0/0
Description TCP Rule
Step 1: Create a traﬃc mirror target in Spoke VPC1 31
Amazon Virtual Private Cloud Traﬃc Mirroring
Step 4: Create a traﬃc mirror session in Spoke VPC1
Create and conﬁgure a traﬃc mirror session with the following options. For more information, see
the section called “Create, modify, or delete a traﬃc mirror session”.
Option Value
Mirror source The network interface of the instance that you 
want to monitor.
Mirror target Target A
Filter Filter 1
Step 5: Create a traﬃc mirror session in Spoke VPC2
Create and conﬁgure a traﬃc mirror session with the following options. For more information, see
the section called “Create, modify, or delete a traﬃc mirror session”.
Option Value
Mirror source The network interface of the instance that you 
want to monitor.
Mirror target Target B
Filter Filter 1
Step 4: Create a traﬃc mirror session in Spoke VPC1 32
Amazon Virtual Private Cloud Traﬃc Mirroring
Work with Traﬃc Mirroring to copy network traﬃc
Traﬃc Mirroring allows you to create, manage, and share traﬃc mirror targets. These targets 
capture and forward a copy of your traﬃc to the destination of your choice. Whether you're a 
network administrator, security analyst, or DevOps engineer, Traﬃc Mirroring enables you to 
proactively identify and address network issues, ensure compliance, and optimize your overall 
network performance.
With Traﬃc Mirroring, you can create and delete traﬃc mirror targets, view and modify their 
conﬁgurations, and even share them with other AWS accounts. You can also construct custom 
traﬃc mirror ﬁlters to capture only the data you need, and set up, modify, or delete traﬃc mirror 
sessions to control the ﬂow of mirrored data. By leveraging these powerful features, you can 
unlock new insights and make informed decisions about your infrastructure, ultimately enhancing 
your organization's overall network visibility and security.
By using Traﬃc Mirroring, you can gain visibility into your network, enabling you to make more 
informed decisions, improve security posture, and drive greater operational eﬃciency across your 
AWS environment.
You can work with traﬃc mirror targets, sessions, and ﬁlters by using the Amazon VPC console or 
the AWS CLI.
Contents
• Create or delete a traﬃc mirror target
• View traﬃc mirror targets and modify target tags
• Share a traﬃc mirror target
• Accept or delete a shared traﬃc mirror target
• Create, modify, or delete a traﬃc mirror ﬁlter
• Create, modify, or delete a traﬃc mirror session
Create or delete a traﬃc mirror target
A traﬃc mirror target is the destination for mirrored traﬃc. For more information, see the section 
called “Targets”.
Before you can delete a traﬃc mirror target, you must remove it from any traﬃc mirror sessions.
Create or delete a traﬃc mirror target 33
Amazon Virtual Private Cloud Traﬃc Mirroring
After you create a target, assign it to a traﬃc mirror session. For more information, see the section 
called “Create, modify, or delete a traﬃc mirror session”.
You must conﬁgure a security group for the traﬃc mirror target that allows VXLAN traﬃc (UDP 
port 4789) from the traﬃc mirror source.
You can share a traﬃc mirror target across accounts. For more information, see Share a traﬃc 
mirror target.
To create a traﬃc mirror target using the console
1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
2. In the Region selector, choose the AWS Region that you used when you created the resource to 
use as the destination for the mirrored traﬃc.
3. On the navigation pane, choose Traﬃc Mirroring, Mirror targets.
4. Choose Create traﬃc mirror target.
5. (Optional) For Name tag, enter a name for the traﬃc mirror target.
6. (Optional) For Description, enter a description for the traﬃc mirror target.
7. For Target type, choose the type of the traﬃc mirror target:
• Network interface
• Network Load Balancer
• Gateway Load Balancer endpoint
8. For Target, choose the destination resource. We display resources based on the target type 
that you selected in the previous step.
9. (Optional) For each tag to add, choose Add new tag and enter the tag key and tag value.
10. Choose Create.
To create a traﬃc mirror target using the AWS CLI
Use the create-traﬃc-mirror-target command.
To delete a traﬃc mirror target using the console
1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
2. On the navigation pane, choose Traﬃc Mirroring, Mirror targets.
Create or delete a traﬃc mirror target 34
Amazon Virtual Private Cloud Traﬃc Mirroring
3. Select the traﬃc mirror target and choose Delete.
4. When prompted for conﬁrmation, enter delete, and then choose Delete.
To delete a traﬃc mirror target using the AWS CLI
Use the delete-traﬃc-mirror-target command.
View traﬃc mirror targets and modify target tags
A traﬃc mirror target is the destination for mirrored traﬃc. For more information, see the section 
called “Targets”.
Complete the steps in this section to view traﬃc mirror targets or modify target tags.
To view your traﬃc mirror targets and modify tags using the console
1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
2. On the navigation pane, choose Traﬃc Mirroring, Mirror targets.
3. To view a target, select the ID of the traﬃc mirror target to open its details page.
4. To modify the tags, on the Tags tab, choose Manage tags.
5. (Optional) For each tag to add, choose Add new tag and enter the tag key and tag value. For 
each tag to remove, choose Remove.
6. Choose Save.
To view your traﬃc mirror targets using the AWS CLI
Use the describe-traﬃc-mirror-targets command.
To modify your traﬃc mirror target tags using the AWS CLI
Use the create-tags command to add a tag. Use the delete-tags command to remove a tag.
Share a traﬃc mirror target
A traﬃc mirror target can be owned by an AWS account that is diﬀerent from the traﬃc mirror 
source.
View traﬃc mirror targets and modify target tags 35
Amazon Virtual Private Cloud Traﬃc Mirroring
You can use AWS Resource Access Manager (RAM) to share a traﬃc mirror target across accounts. 
Use the following procedure to share a traﬃc mirror target that you own.
You must create a traﬃc mirror target before you share it. For more information, see the section 
called “Create or delete a traﬃc mirror target”.
To share a traﬃc mirror target
1. Open the AWS Resource Access Manager console at https://console.aws.amazon.com/ram/.
2. Choose Create a resource share.
3. Under Description, for Name, enter a descriptive name for the resource share.
4. For Select resource type, choose Traﬃc Mirror Targets. Select the traﬃc mirror target.
5. For Principals, add principals to the resource share. For each AWS account, OU, or 
organization, specify its ID and choose Add.
For Allow external accounts, choose whether to allow sharing for this resource with AWS 
accounts that are external to your organization.
6. (Optional) Under Tags, enter a tag key and tag value pair for each tag. These tags are applied 
to the resource share but not to the traﬃc mirror target.
7. Choose Create resource share.
Accept or delete a shared traﬃc mirror target
Before you can use a cross-account traﬃc mirror target, the traﬃc mirror target owner shares 
the target with you by using the AWS Resource Access Manager. When you are in diﬀerent AWS 
Organizations from the owner, after the owner shares the traﬃc mirror target, you accept the share 
request. After you accept the share request, you can use the traﬃc mirror target in a traﬃc mirror 
session.
The traﬃc mirror target is visible to shared accounts in their DescribeTrafficMirrorTarget
API calls. Only the traﬃc mirror target owner can modify or delete the traﬃc mirror target.
Traﬃc mirror sessions that are created in a diﬀerent account than the traﬃc mirror target are 
visible in DescribeTrafficMirrorSession API calls that are made by the traﬃc mirror target 
owner.
If you are in diﬀerent AWS Organizations from the share owner, you must accept the resource share 
before you can access the shared resources.
Accept or delete a shared traﬃc mirror target 36
Amazon Virtual Private Cloud Traﬃc Mirroring
You can delete a resource share at any time. When you delete a resource share, all principals that 
are associated with the resource share lose access to the shared resources. Deleting a resource 
share does not delete the shared resources.
When you delete a shared traﬃc mirror target that is in use, the traﬃc mirror session becomes 
inactive.
To accept or delete a shared traﬃc mirror target
1. Open the AWS Resource Access Manager console at https://console.aws.amazon.com/ram/.
2. To accept a shared traﬃc mirror target, in the navigation pane, choose Shared with me,
Resource shares.
3. Select the resource share.
4. Choose Accept resource share.
5. To view the shared traﬃc mirror target, open the Traﬃc Mirror Targets page in the Amazon 
VPC console.
6. To delete a shared traﬃc mirror target, on the navigation pane, choose Shared by me,
Resource shares.
7. Select the resource share.
Be sure to select the correct resource share. You cannot recover a resource share after you 
delete it.
8. Choose Delete.
9. When prompted for conﬁrmation, enter delete, and then choose Delete.
Create, modify, or delete a traﬃc mirror ﬁlter
Use a traﬃc mirror ﬁlter and its rules to determine the traﬃc that is mirrored. A traﬃc mirror ﬁlter 
contains one or more traﬃc mirror rules. For more information, see the section called “Filters”.
Rules are evaluated from the lowest value to the highest value. The ﬁrst rule that matches the 
traﬃc determines the action to take.
Before you can delete a traﬃc mirror ﬁlter, you must remove it from any traﬃc mirror sessions.
To create, modify, or delete a traﬃc mirror ﬁlter using the console
1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
Create, modify, or delete a traﬃc mirror ﬁlter 37
Amazon Virtual Private Cloud Traﬃc Mirroring
2. On the navigation pane, choose Traﬃc Mirroring, Mirror ﬁlters.
3. To delete a ﬁlter, select the traﬃc mirror ﬁlter, and then choose Actions, Delete.
4. When prompted for conﬁrmation, enter delete, and then choose Delete.
5. To modify a ﬁlter, select the ID of the traﬃc mirror ﬁlter to open its details page. For each rule 
to add, choose either Inbound rules , Add inbound rule or Outbound rules, and then choose
Actions and modify the the rule.
6. To create a ﬁlter, choose Create traﬃc mirror ﬁlter.
7. (Optional) For Name tag, enter a name for the traﬃc mirror ﬁlter.
8. (Optional) For Description, enter a description for the traﬃc mirror ﬁlter.
9. (Optional) If you need to mirror Amazon DNS traﬃc, select amazon-dns.
10. For each rule, inbound or outbound, choose Add rule, and then specify the following 
information:
• Number: The rule priority.
• Rule action: Indicates whether to accept or reject the packets.
• Protocol: The protocol.
• (Optional) Source port range: The source port range.
• (Optional) Destination port range: The destination port range.
• Source CIDR block: The source CIDR block. The source and destination CIDR blocks must 
both be either IPv4 ranges or IPv6 ranges.
• Destination CIDR block: The destination CIDR block. The source and destination CIDR blocks 
must both be either IPv4 ranges or IPv6 ranges.
• Description: A description for the rule.
11. (Optional) For each tag to add, choose Add new tag and enter the tag key and tag value.
12. Choose Create.
To create a traﬃc mirror ﬁlter using the AWS CLI
Use the create-traﬃc-mirror-ﬁlter command.
To delete a traﬃc mirror ﬁlter using the AWS CLI
Use the delete-traﬃc-mirror-ﬁlter command.
Create, modify, or delete a traﬃc mirror ﬁlter 38
Amazon Virtual Private Cloud Traﬃc Mirroring
Create, modify, or delete a traﬃc mirror session
A traﬃc mirror session establishes a relationship between a traﬃc mirror source and a traﬃc mirror 
target. For more information, see the section called “Sessions”.
You can create a traﬃc mirror session only if you are the owner of the network interface or the 
subnet for the traﬃc mirror source.
To create, modify, or delete a traﬃc mirror session using the console
1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
2. In the Region selector, choose the AWS Region that you used when you created the VPCs.
3. In the navigation pane, choose Traﬃc Mirroring, Mirror sessions.
4. Select the traﬃc mirror session, and then choose Actions, Delete.
5. When prompted for conﬁrmation, enter delete, and then choose Delete.
6. To modify a session, select the radio button for the traﬃc mirror session.
7. Choose Actions, Modify session.
8. To create a session, choose Create traﬃc mirror session.
9. (Optional) For Name tag, enter a name for the traﬃc mirror session.
10. (Optional) For Description, enter a description for the traﬃc mirror session.
11. For Mirror source, choose the network interface of the mirror source.
12. For Mirror target, choose an existing traﬃc mirror target or choose Create target to create 
one. For more information, see the section called “Create or delete a traﬃc mirror target”.
If the mirror target is owned by another account and shared with you, you must ﬁrst accept the 
resource share.
13. For Additional settings, do the following:
a. For Session number, enter the session number. The valid values are 1 to 32,766, where 1 is 
the highest priority. Sessions are evaluated based on the priority indicated by this session 
number.
b. (Optional) For VNI, enter the VXLAN ID to use for the traﬃc mirror session. For more 
information about the VXLAN protocol, see RFC 7348.
If you do not enter a value, we assign a random number.
c. (Optional) For Packet Length, enter the number of bytes in each packet to mirror.
Create, modify, or delete a traﬃc mirror session 39
Amazon Virtual Private Cloud Traﬃc Mirroring
To mirror the entire packet, do not enter a value. To mirror only a portion of each packet, 
set this value to the number of bytes to mirror. For example, if you set this value to 100, the 
ﬁrst 100 bytes after the VXLAN header that meet the ﬁlter criteria are copied to the target.
d. For Filter, choose an existing traﬃc mirror ﬁlter. Alternatively, choose Create ﬁlter. For 
more information, see the section called “Step 2: Create the traﬃc mirror ﬁlter”.
14. (Optional) For each tag to add, choose Add new tag and enter the tag key and tag value.
15. If you're modifying a session, choose Modify. If you're creating a session, choose Create.
To create a traﬃc mirror session using the AWS CLI
Use the create-traﬃc-mirror-session command.
Create, modify, or delete a traﬃc mirror session 40
Amazon Virtual Private Cloud Traﬃc Mirroring
Work with open-source tools for traﬃc mirroring
You can use open-source tools to monitor network traﬃc from Amazon EC2 instances. The 
following tools work with Traﬃc Mirroring:
• Zeek — For more information, see the Zeek website.
• Suricata — For more information see the Suricata website.
These open-source tools support VXLAN decapsulation, and they can be used at scale to monitor 
VPC traﬃc. For information about how Zeek handles VXLAN support and to download the code, 
see Zeek vxlan on the GitHub website. For information about how Suricata handles VXLAN support 
and to download the code, see Suricata on the GitHub website.
The following example uses the Suricata open-source tool. You can follow similar steps for Zeek.
Consider the scenario where you want to mirror inbound TCP traﬃc on an instance and send the 
traﬃc to an instance that has the Suricata software installed. You need the following traﬃc mirror 
entities for this example:
• An EC2 instance with the Suricata software installed on it
• A traﬃc mirror target for the EC2 instance (Target A)
• A traﬃc mirror ﬁlter with a traﬃc mirror rule for the TCP inbound traﬃc (Filter rule 1)
• A traﬃc mirror session that has the following:
• A traﬃc mirror source
• A traﬃc mirror target for the appliance
• A traﬃc mirror ﬁlter with a traﬃc mirror rule for the TCP inbound traﬃc
Step 1: Install the Suricata software on the EC2 instance target
Launch an EC2 instance, and then install the Suricata software on it by using the following 
commands.
# Become sudo
sudo -s
# Install epel-release
amazon-linux-extras install -y epel
Step 1: Install the Suricata software on the EC2 instance target 41
Amazon Virtual Private Cloud Traﬃc Mirroring
# Install suricata
yum install -y suricata
# Create the default suricata rules directory
mkdir /var/lib/suricata/rules
# Add a rule to match all UDP traffic
echo 'alert udp any any -> any any (msg:"UDP traffic detected"; sid:200001; rev:1;)' 
 > /var/lib/suricata/rules/suricata.rules
# Start suricata listening on eth0 in daemon mode
suricata -c /etc/suricata/suricata.yaml -k none -i eth0 -D
# Capture logs can be found in /var/log/suricata/fast.log 
Step 2: Create a traﬃc mirror target
Create a traﬃc mirror target (Target A) for the EC2 instance. Depending on your conﬁguration, the 
target is one of the following types:
• The network interface of the monitoring appliance
• The Network Load Balancer when the appliance is deployed behind one.
• The Gateway Load Balancer endpoint when the appliance is deployed behind a Gateway Load 
Balancer
For more information, see the section called “Create or delete a traﬃc mirror target”.
Step 3: Create a traﬃc mirror ﬁlter
Create a traﬃc mirror ﬁlter (Filter 1) with the following inbound rule. For more information, see the 
section called “Create, modify, or delete a traﬃc mirror ﬁlter”.
Option Value
Rule action Accept
Protocol TCP
Source port range  
Destination port range  
Step 2: Create a traﬃc mirror target 42
Amazon Virtual Private Cloud Traﬃc Mirroring
Option Value
Source CIDR block 0.0.0.0/0
Destination CIDR block 0.0.0.0/0
Description TCP Rule
Step 4: Create a traﬃc mirror session
Create and conﬁgure a traﬃc mirror session with the following options. For more information, see
the section called “Create, modify, or delete a traﬃc mirror session”.
Option Value
Mirror source The network interface of the instance that you 
want to monitor.
Mirror target Target A
Filter Filter 1
Step 4: Create a traﬃc mirror session 43
Amazon Virtual Private Cloud Traﬃc Mirroring
Monitor mirrored traﬃc using Amazon CloudWatch
You can monitor your mirrored traﬃc using Amazon CloudWatch, which collects information from 
your network interface that is part of a traﬃc mirror session, and creates readable, near real-time 
metrics. You can use this information to monitor and troubleshoot Traﬃc Mirroring.
For more information about Amazon CloudWatch, see the Amazon CloudWatch User Guide. For 
more information, see CloudWatch metrics that are available for your instances in Amazon EC2 
User Guide. For more information, see Amazon CloudWatch Pricing.
Traﬃc Mirroring metrics and dimensions
The following metrics are available for your mirrored traﬃc at the traﬃc mirror source:
Metric Description
NetworkMirrorIn The number of bytes received on all network 
interfaces by the instance that are mirrored.
The number reported is the number of bytes 
received during the period. If you are using 
basic (ﬁve-minute) monitoring, you can divide 
this number by 300 to ﬁnd Bytes/second. If 
you have detailed (one-minute) monitoring, 
divide it by 60.
Units: Bytes
NetworkMirrorOut The number of bytes sent out on all network 
interfaces by the instance that are mirrored.
The number reported is the number of bytes 
sent during the period. If you are using basic 
(ﬁve-minute) monitoring, you can divide this 
number by 300 to ﬁnd Bytes/second. If you 
have detailed (one-minute) monitoring, divide 
it by 60.
Traﬃc Mirroring metrics and dimensions 44
Amazon Virtual Private Cloud Traﬃc Mirroring
Metric Description
Units: Bytes
NetworkPacketsMirrorIn The number of packets received on all 
network interfaces by the instance that are 
mirrored. This metric is available for basic 
monitoring only.
Units: Count
NetworkPacketsMirrorOut The number of packets sent out on all network 
interfaces by the instance that are mirrored. 
This metric is available for basic monitoring 
only.
Units: Count
NetworkSkipMirrorIn The number of bytes received, that meet 
the traﬃc mirror ﬁlter rules, that did not get 
mirrored because of production traﬃc taking 
priority.
Units: Bytes
NetworkSkipMirrorOut The number of bytes sent out, that meet 
the traﬃc mirror ﬁlter rules, that did not get 
mirrored because of production traﬃc taking 
priority.
Units: Bytes
NetworkPacketsSkipMirrorIn The number of packets received, that meet 
the traﬃc mirror ﬁlter rules, that did not get 
mirrored because of production traﬃc taking 
priority. This metric is available for basic 
monitoring only.
Units: Count
Traﬃc Mirroring metrics and dimensions 45
Amazon Virtual Private Cloud Traﬃc Mirroring
Metric Description
NetworkPacketsSkipMirrorOut The number of packets sent out, that meet 
the traﬃc mirror ﬁlter rules, that did not get 
mirrored because of production traﬃc taking 
priority. This metric is available for basic 
monitoring only.
Units: Count
To ﬁlter the metric data, use the following dimensions.
Dimension Description
AutoScalingGroupName This dimension ﬁlters the data you request for 
all instances in a speciﬁed capacity group. An 
Auto Scaling group is a collection of instances 
you deﬁne if you're using Auto Scaling. This 
dimension is available only for Amazon EC2 
metrics when the instances are in such an Auto 
Scaling group. Available for instances with 
Detailed or Basic Monitoring enabled.
ImageId This dimension ﬁlters the data you request for 
all instances running this Amazon EC2 Amazon 
Machine Image (AMI). Available for instances 
with Detailed Monitoring enabled.
InstanceId This dimension ﬁlters the data you request 
for the identiﬁed instance only. This helps 
you pinpoint an exact instance from which 
to monitor data. Available for instances with 
Detailed or Basic Monitoring enabled.
InstanceType This dimension ﬁlters the data you request 
for all instances running with this speciﬁed 
instance type. This helps you categorize your 
Traﬃc Mirroring metrics and dimensions 46
Amazon Virtual Private Cloud Traﬃc Mirroring
Dimension Description
data by the type of instance running. For 
example, you might compare data from an 
m1.small instance and an m1.large instance to 
determine which has the better business value 
for your application. Available for instances 
with Detailed Monitoring enabled.
View Traﬃc Mirroring CloudWatch metrics
You can view the metrics for Traﬃc Mirroring as follows.
To view metrics using the CloudWatch console
Metrics are grouped ﬁrst by the service namespace, and then by the various dimension 
combinations within each namespace.
1. Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.
2. In the navigation pane, choose Metrics.
3. Under All metrics, choose the EC2 metric namespace.
4. To view the metrics, select the metric dimension.
To view metrics using the AWS CLI
At a command prompt, use the following command to list the metrics that are available for Traﬃc 
Mirroring:
aws cloudwatch list-metrics --namespace "AWS/EC2"
The Traﬃc Mirroring metrics are included with the metrics for Amazon EC2.
View Traﬃc Mirroring CloudWatch metrics 47
Amazon Virtual Private Cloud Traﬃc Mirroring
Traﬃc Mirroring limitations
This section contains the limitations for Traﬃc Mirroring.
Contents
• General limitations
• MTU and packet length limitations
• Traﬃc bandwidth and prioritization limitations
• Checksum oﬄoading limitations
General limitations
This section contains general Traﬃc Mirroring limitations.
IPv6 traﬃc
Traﬃc Mirroring is not supported for IPv6-only subnets.
Traﬃc types
Traﬃc Mirroring can't mirror the following traﬃc types:
• ARP
• DHCP
• Instance metadata service
• NTP
• Windows activation
VPC Flow Logs
VPC Flow Logs do not capture mirrored traﬃc.
Shared VPCs and subnets
• Participants cannot describe, create, modify, or delete a traﬃc mirror session or target that 
belongs to the VPC owner. Participants can describe, create, modify, and delete a traﬃc mirror 
session or target that belongs to them.
General limitations 48
Amazon Virtual Private Cloud Traﬃc Mirroring
• VPC owners cannot describe, create, modify, or delete a traﬃc mirror session or target that 
belongs to the participant.
For more information see, Share your VPC with other accounts in the Amazon VPC User Guide.
Sources
You can only use requester-managed network interfaces created by Amazon RDS or Amazon 
ElastiCache as a Traﬃc Mirroring source in a session.
MTU and packet length limitations
We truncate the packet to the MTU value when both of the following are true:
• The traﬃc mirror target is a standalone instance.
• The mirrored traﬃc packet size is greater than the traﬃc mirror target MTU value.
For example, if an 8996 byte packet is mirrored, and the traﬃc mirror target MTU value is 9001 
bytes, the mirror encapsulation results in the mirrored packet being greater than the MTU value. In 
this case, the mirror packet is truncated. To prevent mirror packets from being truncated, set the 
traﬃc mirror source interface MTU value to 54 bytes less than the traﬃc mirror target MTU value 
for IPv4 and 74 bytes less than the traﬃc mirror target MTU value when you use IPv6. Therefore, 
the maximum MTU value supported by Traﬃc Mirroring with no packet truncation is 8947 bytes.
In addition, the packet length cannot be less than 35 bytes (for IPv4 traﬃc) and 55 bytes (for IPv6 
traﬃc).
For more information about conﬁguring the network MTU value, see Network maximum 
transmission unit (MTU) in the Amazon EC2 User Guide.
Traﬃc bandwidth and prioritization limitations
Mirrored traﬃc counts toward instance bandwidth. For example, if you mirror a network interface 
that has 1 Gbps of inbound traﬃc and 1 Gbps of outbound traﬃc, the instance must handle 4 
Gbps of traﬃc (1 Gbps inbound, 1 Gbps mirrored inbound, 1 Gbps outbound, and 1 Gbps mirrored 
outbound) and your packet size should be equal to or greater than 1500 Bytes. Note that the per 
ﬂow limit for EC2 instances not in placement groups is 5 Gbps. For instances not in placement 
groups, the per ﬂow throughput should be lower than 2.5 Gbps or mirrored packets is dropped.
MTU and packet length limitations 49
Amazon Virtual Private Cloud Traﬃc Mirroring
By default, each Gateway Load Balancer endpoint can support a bandwidth of up to 10 Gbps 
per Availability Zone and automatically scales up to 100 Gbps. For more information, see AWS 
PrivateLink quotas in the AWS PrivateLink Guide.
If the network traﬃc exceeds the bandwidth or packet-per-second (PPS) limits of an instance, 
mirrored traﬃc is dropped. This gives production traﬃc priority when there is traﬃc congestion. 
However, if production traﬃc continues to exceed the bandwidth or PPS limits, it is also dropped. 
Mirrored traﬃc might also be dropped at lower bandwidths if the average packet size of your 
traﬃc is small.
Checksum oﬄoading limitations
The Elastic Network Adapter (ENA) provides checksum oﬄoading capabilities. If a packet is 
truncated, this might result in the packet checksum not being calculated for the mirrored packet. 
The following checksums are not calculated when the mirrored packet is truncated:
• If the mirror packet is truncated, the mirror packet L4 checksum is not calculated.
• If any part of the L3 header is truncated, the L3 checksum is not calculated.
If this causes issues, you can disable ENA checksum oﬄoading on the ENA for the source. For 
example, use the following commands on Amazon Linux 2:
[ec2-user ~]$ sudo ethtool --offload eth0 tx off 
[ec2-user ~]$ sudo ethtool --show-offload eth0
Features for eth0:
rx-checksumming: on
tx-checksumming: off 
     tx-checksum-ipv4: off 
     tx-checksum-ip-generic: off [fixed] 
     tx-checksum-ipv6: off [fixed] 
     tx-checksum-fcoe-crc: off [fixed] 
     tx-checksum-sctp: off [fixed]
Checksum oﬄoading limitations 50
Amazon Virtual Private Cloud Traﬃc Mirroring
Traﬃc Mirroring quotas
The following are the quotas for Traﬃc Mirroring for your AWS account.
Contents
• Sessions
• Targets
• Filters
• Throughput
• Packets
• Sources
Sessions
Name Default Adjustable
Maximum number of sessions per account 10,000 No
Maximum number of sessions per source 
network interface
3 No
Maximum number of sessions for a single 
Gateway Load Balancer endpoint
Unlimited Not applicable
Targets
Name Default Adjustable
Maximum number of targets per account 10,000 No
Sessions 51
Amazon Virtual Private Cloud Traﬃc Mirroring
Filters
Name Default Adjustable
Maximum number of ﬁlters per account 10,000 No
Maximum number of sessions per source 
network interface
3 No
Maximum number of ﬁlter rules per ﬁlter 10 No
Throughput
Name Default Adjustable
Maximum throughput through a single 
Gateway Load Balancer endpoint
100 Gbps No
Packets
Name Default Adjustable
Maximum number of MTUs for a Gateway 
Load Balancer endpoint
8,500 No
Sources
Name Default Adjustable
Maximum number of sources per Network 
Load Balancer
No limit No
Maximum number of sources per Gateway 
Load Balancer endpoint
No limit No
Filters 52
Amazon Virtual Private Cloud Traﬃc Mirroring
Name Default Adjustable
Maximum number of sources per target 100 or 10 depending 
on the instance type. 
For more informati 
on, see the list below
1
No
1 The following instance types support up to 100 sources per target. All other instance types 
support up to 10 sources per target.
• General Purpose: m5.24xlarge | m5d.24xlarge | m5dn.24xlarge | m5n.24xlarge | m5zn.12xlarge 
| m6a.48xlarge | m6g.16xlarge | m6gd.16xlarge | m6i.32xlarge | m6id.32xlarge | m6idn.32xlarge 
| m6in.32xlarge | m7a.48xlarge | m7i.48xlarge | m8a.48xlarge | m8azn.24xlarge | m8g.48xlarge 
| m8gb.24xlarge | m8gb.48xlarge | m8gd.48xlarge | m8gn.24xlarge | m8gn.48xlarge | 
m8i.96xlarge | m8id.96xlarge
• Compute Optimized: c5.18xlarge | c5.24xlarge | c5d.18xlarge | c5d.24xlarge | c5n.18xlarge 
| c6a.48xlarge | c6g.16xlarge | c6gd.16xlarge | c6gn.16xlarge | c6i.32xlarge | c6id.32xlarge 
| c6in.32xlarge | c7a.48xlarge | c7gn.16xlarge | c7i.48xlarge | c8a.48xlarge | c8g.48xlarge | 
c8gb.24xlarge | c8gb.48xlarge | c8gd.48xlarge | c8gn.24xlarge | c8gn.48xlarge | c8i.96xlarge | 
c8id.96xlarge
• Memory Optimized: r5.24xlarge | r5b.24xlarge | r5d.24xlarge | r5dn.24xlarge | r5n.24xlarge 
| r6a.48xlarge | r6g.16xlarge | r6gd.16xlarge | r6i.32xlarge | r6id.32xlarge | r6idn.32xlarge 
| r6in.32xlarge | r7a.48xlarge | r7i.48xlarge | r7iz.32xlarge | r8a.48xlarge | r8g.48xlarge | 
r8gb.24xlarge | r8gb.48xlarge | r8gd.48xlarge | r8gn.24xlarge | r8gn.48xlarge | r8i.96xlarge 
| r8id.96xlarge | u-6tb1.56xlarge | u-6tb1.112xlarge | u-9tb1.112xlarge | u-12tb1.112xlarge 
| u-18tb1.112xlarge | u-24tb1.112xlarge | u7i-6tb.112xlarge | u7i-8tb.112xlarge | 
u7i-12tb.224xlarge | u7in-16tb.224xlarge | u7in-24tb.224xlarge | u7in-32tb.224xlarge | 
u7inh-32tb.480xlarge | x2gd.16xlarge | x2idn.32xlarge | x2iedn.32xlarge | x2iezn.12xlarge | 
x8g.48xlarge | x8aedz.24xlarge | x8i.96xlarge | z1d.12xlarge
• Storage Optimized: i3en.24xlarge | i4g.16xlarge | i4i.32xlarge | i7i.48xlarge | i7ie.48xlarge | 
i8g.48xlarge | i8ge.48xlarge | im4gn.16xlarge
• Accelerated Computing: dl1.24xlarge | dl2q.24xlarge | f2.48xlarge | g5.48xlarge | g5g.16xlarge 
| g6.48xlarge | g6e.12xlarge | g6e.24xlarge | g6e.48xlarge | g7e.12xlarge | g7e.24xlarge | 
g7e.48xlarge | inf1.24xlarge | inf2.48xlarge | p3dn.24xlarge | p4d.24xlarge | p4de.24xlarge | 
Sources 53
Amazon Virtual Private Cloud Traﬃc Mirroring
p5.4xlarge | p5.48xlarge | p5e.48xlarge | p5en.48xlarge | p6-b200.48xlarge | p6-b300.48xlarge 
| p6e-gb200.36xlarge | trn1.32xlarge | trn1n.32xlarge | trn2.3xlarge | trn2.48xlarge | 
trn2u.48xlarge | vt1.24xlarge
• High Performance Computing: hpc6a.48xlarge | hpc6id.32xlarge | hpc7a.12xlarge | 
hpc7a.24xlarge | hpc7a.48xlarge | hpc7a.96xlarge | hpc7g.4xlarge | hpc7g.8xlarge | 
hpc7g.16xlarge | hpc8a.96xlarge
Sources 54
Amazon Virtual Private Cloud Traﬃc Mirroring
Identity and access management for Traﬃc Mirroring
AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely 
control access to AWS resources. Administrators control who can be authenticated (signed in) and
authorized (have permissions) to use traﬃc mirror resources.
To allow access to traﬃc mirror resources, you create and attach an IAM policy to an IAM role and 
users or groups assume that role.
The IAM role must be given permission to use speciﬁc traﬃc mirror resources and API actions. 
When you attach a policy to a role, it allows or denies permission to perform the speciﬁed tasks on 
the speciﬁed resources.
You can also use resource-level permissions to restrict what resources users can use when they 
invoke APIs.
Example: CreateTraﬃcMirrorSession policy
The following IAM policy allows users to use the CreateTrafficMirrorSession API, but 
restricts the action to a speciﬁc traﬃc mirror target (tmt-12345645678). To create a traﬃc mirror 
session, users must also have permission to use the traﬃc mirror ﬁlter and network interface 
resources. Therefore, you must include these resources in the IAM policy attached to the role.
JSON
{ 
    "Version":"2012-10-17",        
    "Statement": [ 
        { 
            "Effect": "Allow", 
            "Action": "ec2:CreateTrafficMirrorSession", 
            "Resource": [ 
                "arn:aws:ec2:*:*:traffic-mirror-target/tmt-12345645678", 
                "arn:aws:ec2:*:*:traffic-mirror-filter/*", 
                "arn:aws:ec2:*:*:network-interface/*" 
            ] 
        } 
     ]
}
55
Amazon Virtual Private Cloud Traﬃc Mirroring
For more information about supported traﬃc mirror actions, resources, and condition keys, see
Actions, resources, and condition keys for Amazon EC2 in the Service Authorization Reference.
56
Amazon Virtual Private Cloud Traﬃc Mirroring
Document history for Traﬃc Mirroring
The following table describes the releases for Traﬃc Mirroring.
Change Description Date
Supported instance types Additional instance types 
available as Traﬃc Mirroring 
source.
August 28, 2025
Support for Gateway Load 
Balancer endpoints as traﬃc 
mirror targets
Send mirrored traﬃc to 
monitoring appliances 
registered with a Gateway 
Load Balancer.
May 12, 2022
Support for non-Nitro 
instance types
Enable Traﬃc Mirroring on 
the following non-Nitro 
instance types: C4, D2, G3, 
G3s, H1, I3, M4, P2, P3, R4, X1 
and X1e.
February 10, 2021
Support for Amazon 
CloudWatch
Monitor your mirrored traﬃc 
using Amazon CloudWatch.
November 25, 2019
Initial release This release introduces Traﬃc 
Mirroring.
June 25, 2019
57
