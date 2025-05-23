# describe-network-interfacesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interfaces.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interfaces.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-network-interfaces

## Description

Describes the specified network interfaces or all your network interfaces.

If you have a large number of network interfaces, the operation fails unless you use pagination or one of the following filters: `group-id` , `mac-address` , `private-dns-name` , `private-ip-address` , `subnet-id` , or `vpc-id` .

### Warning

We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkInterfaces)

`describe-network-interfaces` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `NetworkInterfaces`

## Synopsis

```
describe-network-interfaces
[--dry-run | --no-dry-run]
[--network-interface-ids <value>]
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--network-interface-ids` (list)

The network interface IDs.

Default: Describes all your network interfaces.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

One or more filters.

- `association.allocation-id` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface.
- `association.association-id` - The association ID returned when the network interface was associated with an IPv4 address.
- `addresses.association.owner-id` - The owner ID of the addresses associated with the network interface.
- `addresses.association.public-ip` - The association ID returned when the network interface was associated with the Elastic IP address (IPv4).
- `addresses.primary` - Whether the private IPv4 address is the primary IP address associated with the network interface.
- `addresses.private-ip-address` - The private IPv4 addresses associated with the network interface.
- `association.ip-owner-id` - The owner of the Elastic IP address (IPv4) associated with the network interface.
- `association.public-ip` - The address of the Elastic IP address (IPv4) bound to the network interface.
- `association.public-dns-name` - The public DNS name for the network interface (IPv4).
- `attachment.attach-time` - The time that the network interface was attached to an instance.
- `attachment.attachment-id` - The ID of the interface attachment.
- `attachment.delete-on-termination` - Indicates whether the attachment is deleted when an instance is terminated.
- `attachment.device-index` - The device index to which the network interface is attached.
- `attachment.instance-id` - The ID of the instance to which the network interface is attached.
- `attachment.instance-owner-id` - The owner ID of the instance to which the network interface is attached.
- `attachment.status` - The status of the attachment (`attaching` | `attached` | `detaching` | `detached` ).
- `availability-zone` - The Availability Zone of the network interface.
- `description` - The description of the network interface.
- `group-id` - The ID of a security group associated with the network interface.
- `ipv6-addresses.ipv6-address` - An IPv6 address associated with the network interface.
- `interface-type` - The type of network interface (`api_gateway_managed` | `aws_codestar_connections_managed` | `branch` | `ec2_instance_connect_endpoint` | `efa` | `efa-only` | `efs` | `gateway_load_balancer` | `gateway_load_balancer_endpoint` | `global_accelerator_managed` | `interface` | `iot_rules_managed` | `lambda` | `load_balancer` | `nat_gateway` | `network_load_balancer` | `quicksight` | `transit_gateway` | `trunk` | `vpc_endpoint` ).
- `mac-address` - The MAC address of the network interface.
- `network-interface-id` - The ID of the network interface.
- `operator.managed` - A Boolean that indicates whether this is a managed network interface.
- `operator.principal` - The principal that manages the network interface. Only valid for managed network interfaces, where `managed` is `true` .
- `owner-id` - The Amazon Web Services account ID of the network interface owner.
- `private-dns-name` - The private DNS name of the network interface (IPv4).
- `private-ip-address` - The private IPv4 address or addresses of the network interface.
- `requester-id` - The alias or Amazon Web Services account ID of the principal or service that created the network interface.
- `requester-managed` - Indicates whether the network interface is being managed by an Amazon Web Services service (for example, Amazon Web Services Management Console, Auto Scaling, and so on).
- `source-dest-check` - Indicates whether the network interface performs source/destination checking. A value of `true` means checking is enabled, and `false` means checking is disabled. The value must be `false` for the network interface to perform network address translation (NAT) in your VPC.
- `status` - The status of the network interface. If the network interface is not attached to an instance, the status is `available` ; if a network interface is attached to an instance the status is `in-use` .
- `subnet-id` - The ID of the subnet for the network interface.
- `tag` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.
- `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
- `vpc-id` - The ID of the VPC for the network interface.

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND` , and the request returns only results that match all of the specified filters.

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide* .

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR` , and the request returns all results that match any of the specified values.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To describe your network interfaces**

This example describes all your network interfaces.

Command:

```
aws ec2 describe-network-interfaces
```

Output:

```
{
  "NetworkInterfaces": [
      {
          "Status": "in-use",
          "MacAddress": "02:2f:8f:b0:cf:75",
          "SourceDestCheck": true,
          "VpcId": "vpc-a01106c2",
          "Description": "my network interface",
          "Association": {
              "PublicIp": "203.0.113.12",
              "AssociationId": "eipassoc-0fbb766a",
              "PublicDnsName": "ec2-203-0-113-12.compute-1.amazonaws.com",
              "IpOwnerId": "123456789012"
          },
          "NetworkInterfaceId": "eni-e5aa89a3",
          "PrivateIpAddresses": [
              {
                  "PrivateDnsName": "ip-10-0-1-17.ec2.internal",
                  "Association": {
                      "PublicIp": "203.0.113.12",
                      "AssociationId": "eipassoc-0fbb766a",
                      "PublicDnsName": "ec2-203-0-113-12.compute-1.amazonaws.com",
                      "IpOwnerId": "123456789012"
                  },
                  "Primary": true,
                  "PrivateIpAddress": "10.0.1.17"
              }
          ],
          "RequesterManaged": false,
          "Ipv6Addresses": [],
          "PrivateDnsName": "ip-10-0-1-17.ec2.internal",
          "AvailabilityZone": "us-east-1d",
          "Attachment": {
              "Status": "attached",
              "DeviceIndex": 1,
              "AttachTime": "2013-11-30T23:36:42.000Z",
              "InstanceId": "i-1234567890abcdef0",
              "DeleteOnTermination": false,
              "AttachmentId": "eni-attach-66c4350a",
              "InstanceOwnerId": "123456789012"
          },
          "Groups": [
              {
                  "GroupName": "default",
                  "GroupId": "sg-8637d3e3"
              }
          ],
          "SubnetId": "subnet-b61f49f0",
          "OwnerId": "123456789012",
          "TagSet": [],
          "PrivateIpAddress": "10.0.1.17"
      },
      {
          "Status": "in-use",
          "MacAddress": "02:58:f5:ef:4b:06",
          "SourceDestCheck": true,
          "VpcId": "vpc-a01106c2",
          "Description": "Primary network interface",
          "Association": {
              "PublicIp": "198.51.100.0",
              "IpOwnerId": "amazon"
          },
          "NetworkInterfaceId": "eni-f9ba99bf",
          "PrivateIpAddresses": [
              {
                  "Association": {
                      "PublicIp": "198.51.100.0",
                      "IpOwnerId": "amazon"
                  },
                  "Primary": true,
                  "PrivateIpAddress": "10.0.1.149"
              }
          ],
          "RequesterManaged": false,
          "Ipv6Addresses": [],
          "AvailabilityZone": "us-east-1d",
          "Attachment": {
              "Status": "attached",
              "DeviceIndex": 0,
              "AttachTime": "2013-11-30T23:35:33.000Z",
              "InstanceId": "i-0598c7d356eba48d7",
              "DeleteOnTermination": true,
              "AttachmentId": "eni-attach-1b9db777",
              "InstanceOwnerId": "123456789012"
          },
          "Groups": [
              {
                  "GroupName": "default",
                  "GroupId": "sg-8637d3e3"
              }
          ],
          "SubnetId": "subnet-b61f49f0",
          "OwnerId": "123456789012",
          "TagSet": [],
          "PrivateIpAddress": "10.0.1.149"
      }
  ]
}
```

This example describes network interfaces that have a tag with the key `Purpose` and the value `Prod`.

Command:

```
aws ec2 describe-network-interfaces --filters Name=tag:Purpose,Values=Prod
```

Output:

```
{
  "NetworkInterfaces": [
      {
          "Status": "available",
          "MacAddress": "12:2c:bd:f9:bf:17",
          "SourceDestCheck": true,
          "VpcId": "vpc-8941ebec",
          "Description": "ProdENI",
          "NetworkInterfaceId": "eni-b9a5ac93",
          "PrivateIpAddresses": [
              {
                  "PrivateDnsName": "ip-10-0-1-55.ec2.internal",
                  "Primary": true,
                  "PrivateIpAddress": "10.0.1.55"
              },
              {
                  "PrivateDnsName": "ip-10-0-1-117.ec2.internal",
                  "Primary": false,
                  "PrivateIpAddress": "10.0.1.117"
              }
          ],
          "RequesterManaged": false,
          "PrivateDnsName": "ip-10-0-1-55.ec2.internal",
          "AvailabilityZone": "us-east-1d",
          "Ipv6Addresses": [],
          "Groups": [
              {
                  "GroupName": "MySG",
                  "GroupId": "sg-905002f5"
              }
          ],
          "SubnetId": "subnet-31d6c219",
          "OwnerId": "123456789012",
          "TagSet": [
              {
                  "Value": "Prod",
                  "Key": "Purpose"
              }
          ],
          "PrivateIpAddress": "10.0.1.55"
      }
  ]
}
```

## Output

NetworkInterfaces -> (list)

Information about the network interfaces.

(structure)

Describes a network interface.

Association -> (structure)

The association information for an Elastic IP address (IPv4) associated with the network interface.

AllocationId -> (string)

The allocation ID.

AssociationId -> (string)

The association ID.

IpOwnerId -> (string)

The ID of the Elastic IP address owner.

PublicDnsName -> (string)

The public DNS name.

PublicIp -> (string)

The address of the Elastic IP address bound to the network interface.

CustomerOwnedIp -> (string)

The customer-owned IP address associated with the network interface.

CarrierIp -> (string)

The carrier IP address associated with the network interface.

This option is only available when the network interface is in a subnet which is associated with a Wavelength Zone.

Attachment -> (structure)

The network interface attachment.

AttachTime -> (timestamp)

The timestamp indicating when the attachment initiated.

AttachmentId -> (string)

The ID of the network interface attachment.

DeleteOnTermination -> (boolean)

Indicates whether the network interface is deleted when the instance is terminated.

DeviceIndex -> (integer)

The device index of the network interface attachment on the instance.

NetworkCardIndex -> (integer)

The index of the network card.

InstanceId -> (string)

The ID of the instance.

InstanceOwnerId -> (string)

The Amazon Web Services account ID of the owner of the instance.

Status -> (string)

The attachment state.

EnaSrdSpecification -> (structure)

Configures ENA Express for the network interface that this action attaches to the instance.

EnaSrdEnabled -> (boolean)

Indicates whether ENA Express is enabled for the network interface.

EnaSrdUdpSpecification -> (structure)

Configures ENA Express for UDP network traffic.

EnaSrdUdpEnabled -> (boolean)

Indicates whether UDP traffic to and from the instance uses ENA Express. To specify this setting, you must first enable ENA Express.

EnaQueueCount -> (integer)

The number of ENA queues created with the instance.

AvailabilityZone -> (string)

The Availability Zone.

ConnectionTrackingConfiguration -> (structure)

A security group connection tracking configuration that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see [Connection tracking timeouts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon EC2 User Guide* .

TcpEstablishedTimeout -> (integer)

Timeout (in seconds) for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 432000 seconds. Recommended: Less than 432000 seconds.

UdpStreamTimeout -> (integer)

Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.

UdpTimeout -> (integer)

Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.

Description -> (string)

A description.

Groups -> (list)

Any security groups for the network interface.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.

InterfaceType -> (string)

The type of network interface.

Ipv6Addresses -> (list)

The IPv6 addresses associated with the network interface.

(structure)

Describes an IPv6 address associated with a network interface.

Ipv6Address -> (string)

The IPv6 address.

PublicIpv6DnsName -> (string)

An IPv6-enabled public hostname for a network interface. Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide* .

IsPrimaryIpv6 -> (boolean)

Determines if an IPv6 address associated with a network interface is the primary IPv6 address. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information, see [ModifyNetworkInterfaceAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyNetworkInterfaceAttribute.html) .

MacAddress -> (string)

The MAC address.

NetworkInterfaceId -> (string)

The ID of the network interface.

OutpostArn -> (string)

The Amazon Resource Name (ARN) of the Outpost.

OwnerId -> (string)

The Amazon Web Services account ID of the owner of the network interface.

PrivateDnsName -> (string)

The private hostname. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide* .

PublicDnsName -> (string)

A public hostname. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide* .

PublicIpDnsNameOptions -> (structure)

Public hostname type options. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide* .

DnsHostnameType -> (string)

The public hostname type. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide* .

PublicIpv4DnsName -> (string)

An IPv4-enabled public hostname for a network interface. Requests from within the VPC resolve to the private primary IPv4 address of the network interface. Requests from the internet resolve to the public IPv4 address of the network interface.

PublicIpv6DnsName -> (string)

An IPv6-enabled public hostname for a network interface. Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface.

PublicDualStackDnsName -> (string)

A dual-stack public hostname for a network interface. Requests from within the VPC resolve to both the private IPv4 address and the IPv6 Global Unicast Address of the network interface. Requests from the internet resolve to both the public IPv4 and the IPv6 GUA address of the network interface.

PrivateIpAddress -> (string)

The IPv4 address of the network interface within the subnet.

PrivateIpAddresses -> (list)

The private IPv4 addresses associated with the network interface.

(structure)

Describes the private IPv4 address of a network interface.

Association -> (structure)

The association information for an Elastic IP address (IPv4) associated with the network interface.

AllocationId -> (string)

The allocation ID.

AssociationId -> (string)

The association ID.

IpOwnerId -> (string)

The ID of the Elastic IP address owner.

PublicDnsName -> (string)

The public DNS name.

PublicIp -> (string)

The address of the Elastic IP address bound to the network interface.

CustomerOwnedIp -> (string)

The customer-owned IP address associated with the network interface.

CarrierIp -> (string)

The carrier IP address associated with the network interface.

This option is only available when the network interface is in a subnet which is associated with a Wavelength Zone.

Primary -> (boolean)

Indicates whether this IPv4 address is the primary private IPv4 address of the network interface.

PrivateDnsName -> (string)

The private DNS name.

PrivateIpAddress -> (string)

The private IPv4 address.

Ipv4Prefixes -> (list)

The IPv4 prefixes that are assigned to the network interface.

(structure)

Describes an IPv4 prefix.

Ipv4Prefix -> (string)

The IPv4 prefix. For information, see [Assigning prefixes to network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html) in the *Amazon EC2 User Guide* .

Ipv6Prefixes -> (list)

The IPv6 prefixes that are assigned to the network interface.

(structure)

Describes the IPv6 prefix.

Ipv6Prefix -> (string)

The IPv6 prefix.

RequesterId -> (string)

The alias or Amazon Web Services account ID of the principal or service that created the network interface.

RequesterManaged -> (boolean)

Indicates whether the network interface is being managed by Amazon Web Services.

SourceDestCheck -> (boolean)

Indicates whether source/destination checking is enabled.

Status -> (string)

The status of the network interface.

SubnetId -> (string)

The ID of the subnet.

TagSet -> (list)

Any tags assigned to the network interface.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

VpcId -> (string)

The ID of the VPC.

DenyAllIgwTraffic -> (boolean)

Indicates whether a network interface with an IPv6 address is unreachable from the public internet. If the value is `true` , inbound traffic from the internet is dropped and you cannot assign an elastic IP address to the network interface. The network interface is reachable from peered VPCs and resources connected through a transit gateway, including on-premises networks.

Ipv6Native -> (boolean)

Indicates whether this is an IPv6 only network interface.

Ipv6Address -> (string)

The IPv6 globally unique address associated with the network interface.

Operator -> (structure)

The service provider that manages the network interface.

Managed -> (boolean)

If `true` , the resource is managed by a service provider.

Principal -> (string)

If `managed` is `true` , then the principal is returned. The principal is the service provider that manages the resource.

NextToken -> (string)

The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.