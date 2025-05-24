# describe-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-instances

## Description

Describes the specified instances or all instances.

If you specify instance IDs, the output includes information for only the specified instances. If you specify filters, the output includes information for only those instances that meet the filter criteria. If you do not specify instance IDs or filters, the output includes information for all instances, which can affect performance. We recommend that you use pagination to ensure that the operation returns quickly and successfully.

If you specify an instance ID that is not valid, an error is returned. If you specify an instance that you do not own, it is not included in the output.

Recently terminated instances might appear in the returned results. This interval is usually less than one hour.

If you describe instances in the rare case where an Availability Zone is experiencing a service disruption and you specify instance IDs that are in the affected zone, or do not specify any instance IDs at all, the call fails. If you describe instances and specify only instance IDs that are in an unaffected zone, the call works normally.

The Amazon EC2 API follows an eventual consistency model. This means that the result of an API command you run that creates or modifies resources might not be immediately available to all subsequent commands you run. For guidance on how to manage eventual consistency, see [Eventual consistency in the Amazon EC2 API](https://docs.aws.amazon.com/ec2/latest/devguide/eventual-consistency.html) in the *Amazon EC2 Developer Guide* .

### Warning

We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts.

### Note

The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances)

`describe-instances` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Reservations`

## Synopsis

```
describe-instances
[--instance-ids <value>]
[--dry-run | --no-dry-run]
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

`--instance-ids` (list)

The instance IDs.

Default: Describes all your instances.

(string)

Syntax:

```
"string" "string" ...
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--filters` (list)

The filters.

- `affinity` - The affinity setting for an instance running on a Dedicated Host (`default` | `host` ).
- `architecture` - The instance architecture (`i386` | `x86_64` | `arm64` ).
- `availability-zone` - The Availability Zone of the instance.
- `block-device-mapping.attach-time` - The attach time for an EBS volume mapped to the instance, for example, `2022-09-15T17:15:20.000Z` .
- `block-device-mapping.delete-on-termination` - A Boolean that indicates whether the EBS volume is deleted on instance termination.
- `block-device-mapping.device-name` - The device name specified in the block device mapping (for example, `/dev/sdh` or `xvdh` ).
- `block-device-mapping.status` - The status for the EBS volume (`attaching` | `attached` | `detaching` | `detached` ).
- `block-device-mapping.volume-id` - The volume ID of the EBS volume.
- `boot-mode` - The boot mode that was specified by the AMI (`legacy-bios` | `uefi` | `uefi-preferred` ).
- `capacity-reservation-id` - The ID of the Capacity Reservation into which the instance was launched.
- `capacity-reservation-specification.capacity-reservation-preference` - The instanceâs Capacity Reservation preference (`open` | `none` ).
- `capacity-reservation-specification.capacity-reservation-target.capacity-reservation-id` - The ID of the targeted Capacity Reservation.
- `capacity-reservation-specification.capacity-reservation-target.capacity-reservation-resource-group-arn` - The ARN of the targeted Capacity Reservation group.
- `client-token` - The idempotency token you provided when you launched the instance.
- `current-instance-boot-mode` - The boot mode that is used to launch the instance at launch or start (`legacy-bios` | `uefi` ).
- `dns-name` - The public DNS name of the instance.
- `ebs-optimized` - A Boolean that indicates whether the instance is optimized for Amazon EBS I/O.
- `ena-support` - A Boolean that indicates whether the instance is enabled for enhanced networking with ENA.
- `enclave-options.enabled` - A Boolean that indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.
- `hibernation-options.configured` - A Boolean that indicates whether the instance is enabled for hibernation. A value of `true` means that the instance is enabled for hibernation.
- `host-id` - The ID of the Dedicated Host on which the instance is running, if applicable.
- `hypervisor` - The hypervisor type of the instance (`ovm` | `xen` ). The value `xen` is used for both Xen and Nitro hypervisors.
- `iam-instance-profile.arn` - The instance profile associated with the instance. Specified as an ARN.
- `iam-instance-profile.id` - The instance profile associated with the instance. Specified as an ID.
- `image-id` - The ID of the image used to launch the instance.
- `instance-id` - The ID of the instance.
- `instance-lifecycle` - Indicates whether this is a Spot Instance, a Scheduled Instance, or a Capacity Block (`spot` | `scheduled` | `capacity-block` ).
- `instance-state-code` - The state of the instance, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped).
- `instance-state-name` - The state of the instance (`pending` | `running` | `shutting-down` | `terminated` | `stopping` | `stopped` ).
- `instance-type` - The type of instance (for example, `t2.micro` ).
- `instance.group-id` - The ID of the security group for the instance.
- `instance.group-name` - The name of the security group for the instance.
- `ip-address` - The public IPv4 address of the instance.
- `ipv6-address` - The IPv6 address of the instance.
- `kernel-id` - The kernel ID.
- `key-name` - The name of the key pair used when the instance was launched.
- `launch-index` - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).
- `launch-time` - The time when the instance was launched, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), for example, `2021-09-29T11:04:43.305Z` . You can use a wildcard (`*` ), for example, `2021-09-29T*` , which matches an entire day.
- `maintenance-options.auto-recovery` - The current automatic recovery behavior of the instance (`disabled` | `default` ).
- `metadata-options.http-endpoint` - The status of access to the HTTP metadata endpoint on your instance (`enabled` | `disabled` )
- `metadata-options.http-protocol-ipv4` - Indicates whether the IPv4 endpoint is enabled (`disabled` | `enabled` ).
- `metadata-options.http-protocol-ipv6` - Indicates whether the IPv6 endpoint is enabled (`disabled` | `enabled` ).
- `metadata-options.http-put-response-hop-limit` - The HTTP metadata request put response hop limit (integer, possible values `1` to `64` )
- `metadata-options.http-tokens` - The metadata request authorization state (`optional` | `required` )
- `metadata-options.instance-metadata-tags` - The status of access to instance tags from the instance metadata (`enabled` | `disabled` )
- `metadata-options.state` - The state of the metadata option changes (`pending` | `applied` ).
- `monitoring-state` - Indicates whether detailed monitoring is enabled (`disabled` | `enabled` ).
- `network-interface.addresses.association.allocation-id` - The allocation ID.
- `network-interface.addresses.association.association-id` - The association ID.
- `network-interface.addresses.association.carrier-ip` - The carrier IP address.
- `network-interface.addresses.association.customer-owned-ip` - The customer-owned IP address.
- `network-interface.addresses.association.ip-owner-id` - The owner ID of the private IPv4 address associated with the network interface.
- `network-interface.addresses.association.public-dns-name` - The public DNS name.
- `network-interface.addresses.association.public-ip` - The ID of the association of an Elastic IP address (IPv4) with a network interface.
- `network-interface.addresses.primary` - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address.
- `network-interface.addresses.private-dns-name` - The private DNS name.
- `network-interface.addresses.private-ip-address` - The private IPv4 address associated with the network interface.
- `network-interface.association.allocation-id` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface.
- `network-interface.association.association-id` - The association ID returned when the network interface was associated with an IPv4 address.
- `network-interface.association.carrier-ip` - The customer-owned IP address.
- `network-interface.association.customer-owned-ip` - The customer-owned IP address.
- `network-interface.association.ip-owner-id` - The owner of the Elastic IP address (IPv4) associated with the network interface.
- `network-interface.association.public-dns-name` - The public DNS name.
- `network-interface.association.public-ip` - The address of the Elastic IP address (IPv4) bound to the network interface.
- `network-interface.attachment.attach-time` - The time that the network interface was attached to an instance.
- `network-interface.attachment.attachment-id` - The ID of the interface attachment.
- `network-interface.attachment.delete-on-termination` - Specifies whether the attachment is deleted when an instance is terminated.
- `network-interface.attachment.device-index` - The device index to which the network interface is attached.
- `network-interface.attachment.instance-id` - The ID of the instance to which the network interface is attached.
- `network-interface.attachment.instance-owner-id` - The owner ID of the instance to which the network interface is attached.
- `network-interface.attachment.network-card-index` - The index of the network card.
- `network-interface.attachment.status` - The status of the attachment (`attaching` | `attached` | `detaching` | `detached` ).
- `network-interface.availability-zone` - The Availability Zone for the network interface.
- `network-interface.deny-all-igw-traffic` - A Boolean that indicates whether a network interface with an IPv6 address is unreachable from the public internet.
- `network-interface.description` - The description of the network interface.
- `network-interface.group-id` - The ID of a security group associated with the network interface.
- `network-interface.group-name` - The name of a security group associated with the network interface.
- `network-interface.ipv4-prefixes.ipv4-prefix` - The IPv4 prefixes that are assigned to the network interface.
- `network-interface.ipv6-address` - The IPv6 address associated with the network interface.
- `network-interface.ipv6-addresses.ipv6-address` - The IPv6 address associated with the network interface.
- `network-interface.ipv6-addresses.is-primary-ipv6` - A Boolean that indicates whether this is the primary IPv6 address.
- `network-interface.ipv6-native` - A Boolean that indicates whether this is an IPv6 only network interface.
- `network-interface.ipv6-prefixes.ipv6-prefix` - The IPv6 prefix assigned to the network interface.
- `network-interface.mac-address` - The MAC address of the network interface.
- `network-interface.network-interface-id` - The ID of the network interface.
- `network-interface.operator.managed` - A Boolean that indicates whether the instance has a managed network interface.
- `network-interface.operator.principal` - The principal that manages the network interface. Only valid for instances with managed network interfaces, where `managed` is `true` .
- `network-interface.outpost-arn` - The ARN of the Outpost.
- `network-interface.owner-id` - The ID of the owner of the network interface.
- `network-interface.private-dns-name` - The private DNS name of the network interface.
- `network-interface.private-ip-address` - The private IPv4 address.
- `network-interface.public-dns-name` - The public DNS name.
- `network-interface.requester-id` - The requester ID for the network interface.
- `network-interface.requester-managed` - Indicates whether the network interface is being managed by Amazon Web Services.
- `network-interface.status` - The status of the network interface (`available` ) | `in-use` ).
- `network-interface.source-dest-check` - Whether the network interface performs source/destination checking. A value of `true` means that checking is enabled, and `false` means that checking is disabled. The value must be `false` for the network interface to perform network address translation (NAT) in your VPC.
- `network-interface.subnet-id` - The ID of the subnet for the network interface.
- `network-interface.tag-key` - The key of a tag assigned to the network interface.
- `network-interface.tag-value` - The value of a tag assigned to the network interface.
- `network-interface.vpc-id` - The ID of the VPC for the network interface.
- `network-performance-options.bandwidth-weighting` - Where the performance boost is applied, if applicable. Valid values: `default` , `vpc-1` , `ebs-1` .
- `operator.managed` - A Boolean that indicates whether this is a managed instance.
- `operator.principal` - The principal that manages the instance. Only valid for managed instances, where `managed` is `true` .
- `outpost-arn` - The Amazon Resource Name (ARN) of the Outpost.
- `owner-id` - The Amazon Web Services account ID of the instance owner.
- `placement-group-name` - The name of the placement group for the instance.
- `placement-partition-number` - The partition in which the instance is located.
- `platform` - The platform. To list only Windows instances, use `windows` .
- `platform-details` - The platform (`Linux/UNIX` | `Red Hat BYOL Linux` | `Red Hat Enterprise Linux` | `Red Hat Enterprise Linux with HA` | `Red Hat Enterprise Linux with SQL Server Standard and HA` | `Red Hat Enterprise Linux with SQL Server Enterprise and HA` | `Red Hat Enterprise Linux with SQL Server Standard` | `Red Hat Enterprise Linux with SQL Server Web` | `Red Hat Enterprise Linux with SQL Server Enterprise` | `SQL Server Enterprise` | `SQL Server Standard` | `SQL Server Web` | `SUSE Linux` | `Ubuntu Pro` | `Windows` | `Windows BYOL` | `Windows with SQL Server Enterprise` | `Windows with SQL Server Standard` | `Windows with SQL Server Web` ).
- `private-dns-name` - The private IPv4 DNS name of the instance.
- `private-dns-name-options.enable-resource-name-dns-a-record` - A Boolean that indicates whether to respond to DNS queries for instance hostnames with DNS A records.
- `private-dns-name-options.enable-resource-name-dns-aaaa-record` - A Boolean that indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.
- `private-dns-name-options.hostname-type` - The type of hostname (`ip-name` | `resource-name` ).
- `private-ip-address` - The private IPv4 address of the instance. This can only be used to filter by the primary IP address of the network interface attached to the instance. To filter by additional IP addresses assigned to the network interface, use the filter `network-interface.addresses.private-ip-address` .
- `product-code` - The product code associated with the AMI used to launch the instance.
- `product-code.type` - The type of product code (`devpay` | `marketplace` ).
- `ramdisk-id` - The RAM disk ID.
- `reason` - The reason for the current state of the instance (for example, shows âUser Initiated [date]â when you stop or terminate the instance). Similar to the state-reason-code filter.
- `requester-id` - The ID of the entity that launched the instance on your behalf (for example, Amazon Web Services Management Console, Auto Scaling, and so on).
- `reservation-id` - The ID of the instanceâs reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you get one reservation ID. If you launch ten instances using the same launch request, you also get one reservation ID.
- `root-device-name` - The device name of the root device volume (for example, `/dev/sda1` ).
- `root-device-type` - The type of the root device volume (`ebs` | `instance-store` ).
- `source-dest-check` - Indicates whether the instance performs source/destination checking. A value of `true` means that checking is enabled, and `false` means that checking is disabled. The value must be `false` for the instance to perform network address translation (NAT) in your VPC.
- `spot-instance-request-id` - The ID of the Spot Instance request.
- `state-reason-code` - The reason code for the state change.
- `state-reason-message` - A message that describes the state change.
- `subnet-id` - The ID of the subnet for the instance.
- `tag:<key>` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.
- `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value.
- `tenancy` - The tenancy of an instance (`dedicated` | `default` | `host` ).
- `tpm-support` - Indicates if the instance is configured for NitroTPM support (`v2.0` ).
- `usage-operation` - The usage operation value for the instance (`RunInstances` | `RunInstances:00g0` | `RunInstances:0010` | `RunInstances:1010` | `RunInstances:1014` | `RunInstances:1110` | `RunInstances:0014` | `RunInstances:0210` | `RunInstances:0110` | `RunInstances:0100` | `RunInstances:0004` | `RunInstances:0200` | `RunInstances:000g` | `RunInstances:0g00` | `RunInstances:0002` | `RunInstances:0800` | `RunInstances:0102` | `RunInstances:0006` | `RunInstances:0202` ).
- `usage-operation-update-time` - The time that the usage operation was last updated, for example, `2022-09-15T17:15:20.000Z` .
- `virtualization-type` - The virtualization type of the instance (`paravirtual` | `hvm` ).
- `vpc-id` - The ID of the VPC that the instance is running in.

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

**Example 1: To describe an instance**

The following `describe-instances` example describes the specified instance.

```
aws ec2 describe-instances \
    --instance-ids i-1234567890abcdef0
```

Output:

```
{
    "Reservations": [
        {
            "Groups": [],
            "Instances": [
                {
                    "AmiLaunchIndex": 0,
                    "ImageId": "ami-0abcdef1234567890",
                    "InstanceId": "i-1234567890abcdef0",
                    "InstanceType": "t3.nano",
                    "KeyName": "my-key-pair",
                    "LaunchTime": "2022-11-15T10:48:59+00:00",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "AvailabilityZone": "us-east-2a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal",
                    "PrivateIpAddress": "10-0-0-157",
                    "ProductCodes": [],
                    "PublicDnsName": "ec2-34-253-223-13.us-east-2.compute.amazonaws.com",
                    "PublicIpAddress": "34.253.223.13",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "StateTransitionReason": "",
                    "SubnetId": "subnet-04a636d18e83cfacb",
                    "VpcId": "vpc-1234567890abcdef0",
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/xvda",
                            "Ebs": {
                                "AttachTime": "2022-11-15T10:49:00+00:00",
                                "DeleteOnTermination": true,
                                "Status": "attached",
                                "VolumeId": "vol-02e6ccdca7de29cf2"
                            }
                        }
                    ],
                    "ClientToken": "1234abcd-1234-abcd-1234-d46a8903e9bc",
                    "EbsOptimized": true,
                    "EnaSupport": true,
                    "Hypervisor": "xen",
                    "IamInstanceProfile": {
                        "Arn": "arn:aws:iam::111111111111:instance-profile/AmazonSSMRoleForInstancesQuickSetup",
                        "Id": "111111111111111111111"
                    },
                    "NetworkInterfaces": [
                        {
                            "Association": {
                                "IpOwnerId": "amazon",
                                "PublicDnsName": "ec2-34-253-223-13.us-east-2.compute.amazonaws.com",
                                "PublicIp": "34.253.223.13"
                            },
                            "Attachment": {
                                "AttachTime": "2022-11-15T10:48:59+00:00",
                                "AttachmentId": "eni-attach-1234567890abcdefg",
                                "DeleteOnTermination": true,
                                "DeviceIndex": 0,
                                "Status": "attached",
                                "NetworkCardIndex": 0
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupName": "launch-wizard-146",
                                    "GroupId": "sg-1234567890abcdefg"
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "00:11:22:33:44:55",
                            "NetworkInterfaceId": "eni-1234567890abcdefg",
                            "OwnerId": "104024344472",
                            "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal",
                            "PrivateIpAddress": "10-0-0-157",
                            "PrivateIpAddresses": [
                                {
                                    "Association": {
                                        "IpOwnerId": "amazon",
                                        "PublicDnsName": "ec2-34-253-223-13.us-east-2.compute.amazonaws.com",
                                        "PublicIp": "34.253.223.13"
                                    },
                                    "Primary": true,
                                    "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal",
                                    "PrivateIpAddress": "10-0-0-157"
                                }
                            ],
                            "SourceDestCheck": true,
                            "Status": "in-use",
                            "SubnetId": "subnet-1234567890abcdefg",
                            "VpcId": "vpc-1234567890abcdefg",
                            "InterfaceType": "interface"
                        }
                    ],
                    "RootDeviceName": "/dev/xvda",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupName": "launch-wizard-146",
                            "GroupId": "sg-1234567890abcdefg"
                        }
                    ],
                    "SourceDestCheck": true,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "my-instance"
                        }
                    ],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 2
                    },
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {
                        "Configured": false
                    },
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "optional",
                        "HttpPutResponseHopLimit": 1,
                        "HttpEndpoint": "enabled",
                        "HttpProtocolIpv6": "disabled",
                        "InstanceMetadataTags": "enabled"
                    },
                    "EnclaveOptions": {
                        "Enabled": false
                    },
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "UsageOperationUpdateTime": "2022-11-15T10:48:59+00:00",
                    "PrivateDnsNameOptions": {
                        "HostnameType": "ip-name",
                        "EnableResourceNameDnsARecord": true,
                        "EnableResourceNameDnsAAAARecord": false
                    },
                    "MaintenanceOptions": {
                        "AutoRecovery": "default"
                    }
                }
            ],
            "OwnerId": "111111111111",
            "ReservationId": "r-1234567890abcdefg"
        }
    ]
}
```

**Example 2: To filter for instances with the specified type**

The following `describe-instances` example uses filters to scope the results to instances of the specified type.

```
aws ec2 describe-instances \
    --filters Name=instance-type,Values=m5.large
```

For example output, see Example 1.

For more information, see [List and filter using the CLI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide*.

**Example 3: To filter for instances with the specified type and Availability Zone**

The following `describe-instances` example uses multiple filters to scope the results to instances with the specified type that are also in the specified Availability Zone.

```
aws ec2 describe-instances \
    --filters Name=instance-type,Values=t2.micro,t3.micro Name=availability-zone,Values=us-east-2c
```

For example output, see Example 1.

**Example 4: To filter for instances with the specified type and Availability Zone using a JSON file**

The following `describe-instances` example uses a JSON input file to perform the same filtering as the previous example. When filters get more complicated, they can be easier to specify in a JSON file.

```
aws ec2 describe-instances \
    --filters file://filters.json
```

Contents of `filters.json`:

```
[
    {
        "Name": "instance-type",
        "Values": ["t2.micro", "t3.micro"]
    },
    {
        "Name": "availability-zone",
        "Values": ["us-east-2c"]
    }
]
```

For example output, see Example 1.

**Example 5: To filter for instances with the specified Owner tag**

The following `describe-instances` example uses tag filters to scope the results to instances that have a tag with the specified tag key (Owner), regardless of the tag value.

```
aws ec2 describe-instances \
    --filters "Name=tag-key,Values=Owner"
```

For example output, see Example 1.

**Example 6: To filter for instances with the specified my-team tag value**

The following `describe-instances` example uses tag filters to scope the results to instances that have a tag with the specified tag value (my-team), regardless of the tag key.

```
aws ec2 describe-instances \
    --filters "Name=tag-value,Values=my-team"
```

For example output, see Example 1.

**Example 7: To filter for instances with the specified Owner tag and my-team value**

The following `describe-instances` example uses tag filters to scope the results to instances that have the specified tag (Owner=my-team).

```
aws ec2 describe-instances \
    --filters "Name=tag:Owner,Values=my-team"
```

For example output, see Example 1.

**Example 8: To display only instance and subnet IDs for all instances**

The following `describe-instances` examples use the `--query` parameter to display only the instance and subnet IDs for all instances, in JSON format.

Linux and macOS:

```
aws ec2 describe-instances \
    --query 'Reservations[*].Instances[*].{Instance:InstanceId,Subnet:SubnetId}' \
    --output json
```

Windows:

```
aws ec2 describe-instances ^
    --query "Reservations[*].Instances[*].{Instance:InstanceId,Subnet:SubnetId}" ^
    --output json
```

Output:

```
[
    {
        "Instance": "i-057750d42936e468a",
        "Subnet": "subnet-069beee9b12030077"
    },
    {
        "Instance": "i-001efd250faaa6ffa",
        "Subnet": "subnet-0b715c6b7db68927a"
    },
    {
        "Instance": "i-027552a73f021f3bd",
        "Subnet": "subnet-0250c25a1f4e15235"
    }
    ...
]
```

**Example 9: To filter instances of the specified type and only display their instance IDs**

The following `describe-instances` example uses filters to scope the results to instances of the specified type and the `--query` parameter to display only the instance IDs.

```
aws ec2 describe-instances \
    --filters "Name=instance-type,Values=t2.micro" \
    --query "Reservations[*].Instances[*].[InstanceId]" \
    --output text
```

Output:

```
i-031c0dc19de2fb70c
i-00d8bff789a736b75
i-0b715c6b7db68927a
i-0626d4edd54f1286d
i-00b8ae04f9f99908e
i-0fc71c25d2374130c
```

**Example 10: To filter instances of the specified type and only display their instance IDs, Availability Zone, and the specified tag value**

The following `describe-instances` examples display the instance ID, Availability Zone, and the value of the `Name` tag for instances that have a tag with the name `tag-key`, in table format.

Linux and macOS:

```
aws ec2 describe-instances \
    --filters Name=tag-key,Values=Name \
    --query 'Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==`Name`]|[0].Value}' \
    --output table
```

Windows:

```
aws ec2 describe-instances ^
    --filters Name=tag-key,Values=Name ^
    --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value}" ^
    --output table
```

Output:

```
-------------------------------------------------------------
|                     DescribeInstances                     |
+--------------+-----------------------+--------------------+
|      AZ      |       Instance        |        Name        |
+--------------+-----------------------+--------------------+
|  us-east-2b  |  i-057750d42936e468a  |  my-prod-server    |
|  us-east-2a  |  i-001efd250faaa6ffa  |  test-server-1     |
|  us-east-2a  |  i-027552a73f021f3bd  |  test-server-2     |
+--------------+-----------------------+--------------------+
```

**Example 11: To describe instances in a partition placement group**

The following `describe-instances` example describes the specified instance. The output includes the placement information for the instance, which contains the placement group name and the partition number for the instance.

```
aws ec2 describe-instances \
    --instance-ids i-0123a456700123456 \
    --query "Reservations[*].Instances[*].Placement"
```

Output:

```
[
    [
        {
            "AvailabilityZone": "us-east-1c",
            "GroupName": "HDFS-Group-A",
            "PartitionNumber": 3,
            "Tenancy": "default"
        }

    ]
]
```

For more information, see [Describing instances in a placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#describe-instance-placement) in the *Amazon EC2 User Guide*.

**Example 12: To filter to instances with the specified placement group and partition number**

The following `describe-instances` example filters the results to only those instances with the specified placement group and partition number.

```
aws ec2 describe-instances \
    --filters "Name=placement-group-name,Values=HDFS-Group-A" "Name=placement-partition-number,Values=7"
```

The following shows only the relevant information from the output.

```
"Instances": [
    {
        "InstanceId": "i-0123a456700123456",
        "InstanceType": "r4.large",
        "Placement": {
            "AvailabilityZone": "us-east-1c",
            "GroupName": "HDFS-Group-A",
            "PartitionNumber": 7,
            "Tenancy": "default"
        }
    },
    {
        "InstanceId": "i-9876a543210987654",
        "InstanceType": "r4.large",
        "Placement": {
            "AvailabilityZone": "us-east-1c",
            "GroupName": "HDFS-Group-A",
            "PartitionNumber": 7,
            "Tenancy": "default"
        }
    ],
```

For more information, see [Describing instances in a placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#describe-instance-placement) in the *Amazon EC2 User Guide*.

**Example 13: To filter to instances that are configured to allow access to tags from instance metadata**

The following `describe-instances` example filters the results to only those instances that are configured to allow access to instance tags from instance metadata.

```
aws ec2 describe-instances \
    --filters "Name=metadata-options.instance-metadata-tags,Values=enabled" \
    --query "Reservations[*].Instances[*].InstanceId" \
    --output text
```

The following shows the expected output.

```
i-1234567890abcdefg
i-abcdefg1234567890
i-11111111aaaaaaaaa
i-aaaaaaaa111111111
```

For more information, see [Work with instance tags in instance metadata](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/Using_Tags.html#view-access-to-tags-in-IMDS) in the *Amazon EC2 User Guide*.

## Output

NextToken -> (string)

The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.

Reservations -> (list)

Information about the reservations.

(structure)

Describes a launch request for one or more instances, and includes owner, requester, and security group information that applies to all instances in the launch request.

ReservationId -> (string)

The ID of the reservation.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the reservation.

RequesterId -> (string)

The ID of the requester that launched the instances on your behalf (for example, Amazon Web Services Management Console or Auto Scaling).

Groups -> (list)

Not supported.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.

Instances -> (list)

The instances.

(structure)

Describes an instance.

Architecture -> (string)

The architecture of the image.

BlockDeviceMappings -> (list)

Any block device mapping entries for the instance.

(structure)

Describes a block device mapping.

DeviceName -> (string)

The device name (for example, `/dev/sdh` or `xvdh` ).

Ebs -> (structure)

Parameters used to automatically set up EBS volumes when the instance is launched.

AttachTime -> (timestamp)

The time stamp when the attachment initiated.

DeleteOnTermination -> (boolean)

Indicates whether the volume is deleted on instance termination.

Status -> (string)

The attachment state.

VolumeId -> (string)

The ID of the EBS volume.

AssociatedResource -> (string)

The ARN of the Amazon ECS or Fargate task to which the volume is attached.

VolumeOwnerId -> (string)

The ID of the Amazon Web Services account that owns the volume.

This parameter is returned only for volumes that are attached to Fargate tasks.

Operator -> (structure)

The service provider that manages the EBS volume.

Managed -> (boolean)

If `true` , the resource is managed by a service provider.

Principal -> (string)

If `managed` is `true` , then the principal is returned. The principal is the service provider that manages the resource.

ClientToken -> (string)

The idempotency token you provided when you launched the instance, if applicable.

EbsOptimized -> (boolean)

Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isnât available with all instance types. Additional usage charges apply when using an EBS Optimized instance.

EnaSupport -> (boolean)

Specifies whether enhanced networking with ENA is enabled.

Hypervisor -> (string)

The hypervisor type of the instance. The value `xen` is used for both Xen and Nitro hypervisors.

IamInstanceProfile -> (structure)

The IAM instance profile associated with the instance, if applicable.

Arn -> (string)

The Amazon Resource Name (ARN) of the instance profile.

Id -> (string)

The ID of the instance profile.

InstanceLifecycle -> (string)

Indicates whether this is a Spot Instance or a Scheduled Instance.

ElasticGpuAssociations -> (list)

Deprecated.

### Note

Amazon Elastic Graphics reached end of life on January 8, 2024.

(structure)

### Note

Amazon Elastic Graphics reached end of life on January 8, 2024.

Describes the association between an instance and an Elastic Graphics accelerator.

ElasticGpuId -> (string)

The ID of the Elastic Graphics accelerator.

ElasticGpuAssociationId -> (string)

The ID of the association.

ElasticGpuAssociationState -> (string)

The state of the association between the instance and the Elastic Graphics accelerator.

ElasticGpuAssociationTime -> (string)

The time the Elastic Graphics accelerator was associated with the instance.

ElasticInferenceAcceleratorAssociations -> (list)

Deprecated

### Note

Amazon Elastic Inference is no longer available.

(structure)

### Note

Amazon Elastic Inference is no longer available.

Describes the association between an instance and an elastic inference accelerator.

ElasticInferenceAcceleratorArn -> (string)

The Amazon Resource Name (ARN) of the elastic inference accelerator.

ElasticInferenceAcceleratorAssociationId -> (string)

The ID of the association.

ElasticInferenceAcceleratorAssociationState -> (string)

The state of the elastic inference accelerator.

ElasticInferenceAcceleratorAssociationTime -> (timestamp)

The time at which the elastic inference accelerator is associated with an instance.

NetworkInterfaces -> (list)

The network interfaces for the instance.

(structure)

Describes a network interface.

Association -> (structure)

The association information for an Elastic IPv4 associated with the network interface.

CarrierIp -> (string)

The carrier IP address associated with the network interface.

CustomerOwnedIp -> (string)

The customer-owned IP address associated with the network interface.

IpOwnerId -> (string)

The ID of the owner of the Elastic IP address.

PublicDnsName -> (string)

The public DNS name.

PublicIp -> (string)

The public IP address or Elastic IP address bound to the network interface.

Attachment -> (structure)

The network interface attachment.

AttachTime -> (timestamp)

The time stamp when the attachment initiated.

AttachmentId -> (string)

The ID of the network interface attachment.

DeleteOnTermination -> (boolean)

Indicates whether the network interface is deleted when the instance is terminated.

DeviceIndex -> (integer)

The index of the device on the instance for the network interface attachment.

Status -> (string)

The attachment state.

NetworkCardIndex -> (integer)

The index of the network card.

EnaSrdSpecification -> (structure)

Contains the ENA Express settings for the network interface thatâs attached to the instance.

EnaSrdEnabled -> (boolean)

Indicates whether ENA Express is enabled for the network interface.

EnaSrdUdpSpecification -> (structure)

Configures ENA Express for UDP network traffic.

EnaSrdUdpEnabled -> (boolean)

Indicates whether UDP traffic to and from the instance uses ENA Express. To specify this setting, you must first enable ENA Express.

EnaQueueCount -> (integer)

The number of ENA queues created with the instance.

Description -> (string)

The description.

Groups -> (list)

The security groups.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.

Ipv6Addresses -> (list)

The IPv6 addresses associated with the network interface.

(structure)

Describes an IPv6 address.

Ipv6Address -> (string)

The IPv6 address.

IsPrimaryIpv6 -> (boolean)

Determines if an IPv6 address associated with a network interface is the primary IPv6 address. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information, see [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) .

MacAddress -> (string)

The MAC address.

NetworkInterfaceId -> (string)

The ID of the network interface.

OwnerId -> (string)

The ID of the Amazon Web Services account that created the network interface.

PrivateDnsName -> (string)

The private DNS name.

PrivateIpAddress -> (string)

The IPv4 address of the network interface within the subnet.

PrivateIpAddresses -> (list)

The private IPv4 addresses associated with the network interface.

(structure)

Describes a private IPv4 address.

Association -> (structure)

The association information for an Elastic IP address for the network interface.

CarrierIp -> (string)

The carrier IP address associated with the network interface.

CustomerOwnedIp -> (string)

The customer-owned IP address associated with the network interface.

IpOwnerId -> (string)

The ID of the owner of the Elastic IP address.

PublicDnsName -> (string)

The public DNS name.

PublicIp -> (string)

The public IP address or Elastic IP address bound to the network interface.

Primary -> (boolean)

Indicates whether this IPv4 address is the primary private IP address of the network interface.

PrivateDnsName -> (string)

The private IPv4 DNS name.

PrivateIpAddress -> (string)

The private IPv4 address of the network interface.

SourceDestCheck -> (boolean)

Indicates whether source/destination checking is enabled.

Status -> (string)

The status of the network interface.

SubnetId -> (string)

The ID of the subnet.

VpcId -> (string)

The ID of the VPC.

InterfaceType -> (string)

The type of network interface.

Valid values: `interface` | `efa` | `efa-only` | `trunk`

Ipv4Prefixes -> (list)

The IPv4 delegated prefixes that are assigned to the network interface.

(structure)

Information about an IPv4 prefix.

Ipv4Prefix -> (string)

One or more IPv4 prefixes assigned to the network interface.

Ipv6Prefixes -> (list)

The IPv6 delegated prefixes that are assigned to the network interface.

(structure)

Information about an IPv6 prefix.

Ipv6Prefix -> (string)

One or more IPv6 prefixes assigned to the network interface.

ConnectionTrackingConfiguration -> (structure)

A security group connection tracking configuration that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see [Connection tracking timeouts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon EC2 User Guide* .

TcpEstablishedTimeout -> (integer)

Timeout (in seconds) for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 432000 seconds. Recommended: Less than 432000 seconds.

UdpStreamTimeout -> (integer)

Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.

UdpTimeout -> (integer)

Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.

Operator -> (structure)

The service provider that manages the network interface.

Managed -> (boolean)

If `true` , the resource is managed by a service provider.

Principal -> (string)

If `managed` is `true` , then the principal is returned. The principal is the service provider that manages the resource.

OutpostArn -> (string)

The Amazon Resource Name (ARN) of the Outpost.

RootDeviceName -> (string)

The device name of the root device volume (for example, `/dev/sda1` ).

RootDeviceType -> (string)

The root device type used by the AMI. The AMI can use an EBS volume or an instance store volume.

SecurityGroups -> (list)

The security groups for the instance.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.

SourceDestCheck -> (boolean)

Indicates whether source/destination checking is enabled.

SpotInstanceRequestId -> (string)

If the request is a Spot Instance request, the ID of the request.

SriovNetSupport -> (string)

Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.

StateReason -> (structure)

The reason for the most recent state transition.

Code -> (string)

The reason code for the state change.

Message -> (string)

The message for the state change.

- `Server.InsufficientInstanceCapacity` : There was insufficient capacity available to satisfy the launch request.
- `Server.InternalError` : An internal error caused the instance to terminate during launch.
- `Server.ScheduledStop` : The instance was stopped due to a scheduled retirement.
- `Server.SpotInstanceShutdown` : The instance was stopped because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.
- `Server.SpotInstanceTermination` : The instance was terminated because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.
- `Client.InstanceInitiatedShutdown` : The instance was shut down from the operating system of the instance.
- `Client.InstanceTerminated` : The instance was terminated or rebooted during AMI creation.
- `Client.InternalError` : A client error caused the instance to terminate during launch.
- `Client.InvalidSnapshot.NotFound` : The specified snapshot was not found.
- `Client.UserInitiatedHibernate` : Hibernation was initiated on the instance.
- `Client.UserInitiatedShutdown` : The instance was shut down using the Amazon EC2 API.
- `Client.VolumeLimitExceeded` : The limit on the number of EBS volumes or total storage was exceeded. Decrease usage or request an increase in your account limits.

Tags -> (list)

Any tags assigned to the instance.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

VirtualizationType -> (string)

The virtualization type of the instance.

CpuOptions -> (structure)

The CPU options for the instance.

CoreCount -> (integer)

The number of CPU cores for the instance.

ThreadsPerCore -> (integer)

The number of threads per CPU core.

AmdSevSnp -> (string)

Indicates whether the instance is enabled for AMD SEV-SNP. For more information, see [AMD SEV-SNP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html) .

CapacityReservationId -> (string)

The ID of the Capacity Reservation.

CapacityReservationSpecification -> (structure)

Information about the Capacity Reservation targeting option.

CapacityReservationPreference -> (string)

Describes the instanceâs Capacity Reservation preferences. Possible preferences include:

- `open` - The instance can run in any `open` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).
- `none` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity.

CapacityReservationTarget -> (structure)

Information about the targeted Capacity Reservation or Capacity Reservation group.

CapacityReservationId -> (string)

The ID of the targeted Capacity Reservation.

CapacityReservationResourceGroupArn -> (string)

The ARN of the targeted Capacity Reservation group.

HibernationOptions -> (structure)

Indicates whether the instance is enabled for hibernation.

Configured -> (boolean)

If `true` , your instance is enabled for hibernation; otherwise, it is not enabled for hibernation.

Licenses -> (list)

The license configurations for the instance.

(structure)

Describes a license configuration.

LicenseConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the license configuration.

MetadataOptions -> (structure)

The metadata options for the instance.

State -> (string)

The state of the metadata option changes.

`pending` - The metadata options are being updated and the instance is not ready to process metadata traffic with the new selection.

`applied` - The metadata options have been successfully applied on the instance.

HttpTokens -> (string)

Indicates whether IMDSv2 is required.

- `optional` - IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.
- `required` - IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.

HttpPutResponseHopLimit -> (integer)

The maximum number of hops that the metadata token can travel.

Possible values: Integers from `1` to `64`

HttpEndpoint -> (string)

Indicates whether the HTTP metadata endpoint on your instances is enabled or disabled.

If the value is `disabled` , you cannot access your instance metadata.

HttpProtocolIpv6 -> (string)

Indicates whether the IPv6 endpoint for the instance metadata service is enabled or disabled.

Default: `disabled`

InstanceMetadataTags -> (string)

Indicates whether access to instance tags from the instance metadata is enabled or disabled. For more information, see [Work with instance tags using the instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS) .

EnclaveOptions -> (structure)

Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.

Enabled -> (boolean)

If this parameter is set to `true` , the instance is enabled for Amazon Web Services Nitro Enclaves; otherwise, it is not enabled for Amazon Web Services Nitro Enclaves.

BootMode -> (string)

The boot mode that was specified by the AMI. If the value is `uefi-preferred` , the AMI supports both UEFI and Legacy BIOS. The `currentInstanceBootMode` parameter is the boot mode that is used to boot the instance at launch or start.

### Note

The operating system contained in the AMI must be configured to support the specified boot mode.

For more information, see [Boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the *Amazon EC2 User Guide* .

PlatformDetails -> (string)

The platform details value for the instance. For more information, see [AMI billing information fields](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html) in the *Amazon EC2 User Guide* .

UsageOperation -> (string)

The usage operation value for the instance. For more information, see [AMI billing information fields](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html) in the *Amazon EC2 User Guide* .

UsageOperationUpdateTime -> (timestamp)

The time that the usage operation was last updated.

PrivateDnsNameOptions -> (structure)

The options for the instance hostname.

HostnameType -> (string)

The type of hostname to assign to an instance.

EnableResourceNameDnsARecord -> (boolean)

Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

EnableResourceNameDnsAAAARecord -> (boolean)

Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

Ipv6Address -> (string)

The IPv6 address assigned to the instance.

TpmSupport -> (string)

If the instance is configured for NitroTPM support, the value is `v2.0` . For more information, see [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html) in the *Amazon EC2 User Guide* .

MaintenanceOptions -> (structure)

Provides information on the recovery and maintenance options of your instance.

AutoRecovery -> (string)

Provides information on the current automatic recovery behavior of your instance.

RebootMigration -> (string)

Specifies whether to attempt reboot migration during a user-initiated reboot of an instance that has a scheduled `system-reboot` event:

- `default` - Amazon EC2 attempts to migrate the instance to new hardware (reboot migration). If successful, the `system-reboot` event is cleared. If unsuccessful, an in-place reboot occurs and the event remains scheduled.
- `disabled` - Amazon EC2 keeps the instance on the same hardware (in-place reboot). The `system-reboot` event remains scheduled.

This setting only applies to supported instances that have a scheduled reboot event. For more information, see [Enable or disable reboot migration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html#reboot-migration) in the *Amazon EC2 User Guide* .

CurrentInstanceBootMode -> (string)

The boot mode that is used to boot the instance at launch or start. For more information, see [Boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the *Amazon EC2 User Guide* .

NetworkPerformanceOptions -> (structure)

Contains settings for the network performance options for your instance.

BandwidthWeighting -> (string)

When you configure network bandwidth weighting, you can boost your baseline bandwidth for either networking or EBS by up to 25%. The total available baseline bandwidth for your instance remains the same. The default option uses the standard bandwidth configuration for your instance type.

Operator -> (structure)

The service provider that manages the instance.

Managed -> (boolean)

If `true` , the resource is managed by a service provider.

Principal -> (string)

If `managed` is `true` , then the principal is returned. The principal is the service provider that manages the resource.

InstanceId -> (string)

The ID of the instance.

ImageId -> (string)

The ID of the AMI used to launch the instance.

State -> (structure)

The current state of the instance.

Code -> (integer)

The state of the instance as a 16-bit unsigned integer.

The high byte is all of the bits between 2^8 and (2^16)-1, which equals decimal values between 256 and 65,535. These numerical values are used for internal purposes and should be ignored.

The low byte is all of the bits between 2^0 and (2^8)-1, which equals decimal values between 0 and 255.

The valid values for instance-state-code will all be in the range of the low byte and they are:

- `0` : `pending`
- `16` : `running`
- `32` : `shutting-down`
- `48` : `terminated`
- `64` : `stopping`
- `80` : `stopped`

You can ignore the high byte value by zeroing out all of the bits above 2^8 or 256 in decimal.

Name -> (string)

The current state of the instance.

PrivateDnsName -> (string)

[IPv4 only] The private DNS hostname name assigned to the instance. This DNS hostname can only be used inside the Amazon EC2 network. This name is not available until the instance enters the `running` state.

The Amazon-provided DNS server resolves Amazon-provided private DNS hostnames if youâve enabled DNS resolution and DNS hostnames in your VPC. If you are not using the Amazon-provided DNS server in your VPC, your custom domain name servers must resolve the hostname as appropriate.

PublicDnsName -> (string)

[IPv4 only] The public DNS name assigned to the instance. This name is not available until the instance enters the `running` state. This name is only available if youâve enabled DNS hostnames for your VPC.

StateTransitionReason -> (string)

The reason for the most recent state transition. This might be an empty string.

KeyName -> (string)

The name of the key pair, if this instance was launched with an associated key pair.

AmiLaunchIndex -> (integer)

The AMI launch index, which can be used to find this instance in the launch group.

ProductCodes -> (list)

The product codes attached to this instance, if applicable.

(structure)

Describes a product code.

ProductCodeId -> (string)

The product code.

ProductCodeType -> (string)

The type of product code.

InstanceType -> (string)

The instance type.

LaunchTime -> (timestamp)

The time that the instance was last launched. To determine the time that instance was first launched, see the attachment time for the primary network interface.

Placement -> (structure)

The location where the instance launched, if applicable.

Affinity -> (string)

The affinity setting for the instance on the Dedicated Host.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) or [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) .

GroupName -> (string)

The name of the placement group that the instance is in. If you specify `GroupName` , you canât specify `GroupId` .

PartitionNumber -> (integer)

The number of the partition that the instance is in. Valid only if the placement group strategy is set to `partition` .

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

HostId -> (string)

The ID of the Dedicated Host on which the instance resides.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) or [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) .

Tenancy -> (string)

The tenancy of the instance. An instance with a tenancy of `dedicated` runs on single-tenant hardware.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) . The `host` tenancy is not supported for [ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) or for T3 instances that are configured for the `unlimited` CPU credit option.

SpreadDomain -> (string)

Reserved for future use.

HostResourceGroupArn -> (string)

The ARN of the host resource group in which to launch the instances.

If you specify this parameter, either omit the **Tenancy** parameter or set it to `host` .

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

GroupId -> (string)

The ID of the placement group that the instance is in. If you specify `GroupId` , you canât specify `GroupName` .

AvailabilityZone -> (string)

The Availability Zone of the instance.

If not specified, an Availability Zone will be automatically chosen for you based on the load balancing criteria for the Region.

This parameter is not supported for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) .

KernelId -> (string)

The kernel associated with this instance, if applicable.

RamdiskId -> (string)

The RAM disk associated with this instance, if applicable.

Platform -> (string)

The platform. This value is `windows` for Windows instances; otherwise, it is empty.

Monitoring -> (structure)

The monitoring for the instance.

State -> (string)

Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

SubnetId -> (string)

The ID of the subnet in which the instance is running.

VpcId -> (string)

The ID of the VPC in which the instance is running.

PrivateIpAddress -> (string)

The private IPv4 address assigned to the instance.

PublicIpAddress -> (string)

The public IPv4 address, or the Carrier IP address assigned to the instance, if applicable.

A Carrier IP address only applies to an instance launched in a subnet associated with a Wavelength Zone.