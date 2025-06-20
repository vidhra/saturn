# instance-existsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/wait/instance-exists.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/wait/instance-exists.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) . [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/wait/index.html#cli-aws-ec2-wait) ]

# instance-exists

## Description

Wait until JMESPath query length(Reservations[]) > 0 returns True when polling with `describe-instances`. It will poll every 5 seconds until a successful state has been reached. This will exit with a return code of 255 after 40 failed checks.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances)

`instance-exists` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Reservations`

## Synopsis

```
instance-exists
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

**To wait until an instance exists**

The following `wait instance-exists` example pauses and resumes running only after it confirms that the specified instance exists. It produces no output.

```
aws ec2 wait instance-exists \
  --instance-ids i-1234567890abcdef0
```

## Output

None