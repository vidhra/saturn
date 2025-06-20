# create-ipam-poolÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-ipam-pool.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-ipam-pool.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# create-ipam-pool

## Description

Create an IP address pool for Amazon VPC IP Address Manager (IPAM). In IPAM, a pool is a collection of contiguous IP addresses CIDRs. Pools enable you to organize your IP addresses according to your routing and security needs. For example, if you have separate routing and security needs for development and production applications, you can create a pool for each.

For more information, see [Create a top-level pool](https://docs.aws.amazon.com/vpc/latest/ipam/create-top-ipam.html) in the *Amazon VPC IPAM User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateIpamPool)

## Synopsis

```
create-ipam-pool
[--dry-run | --no-dry-run]
--ipam-scope-id <value>
[--locale <value>]
[--source-ipam-pool-id <value>]
[--description <value>]
--address-family <value>
[--auto-import | --no-auto-import]
[--publicly-advertisable | --no-publicly-advertisable]
[--allocation-min-netmask-length <value>]
[--allocation-max-netmask-length <value>]
[--allocation-default-netmask-length <value>]
[--allocation-resource-tags <value>]
[--tag-specifications <value>]
[--client-token <value>]
[--aws-service <value>]
[--public-ip-source <value>]
[--source-resource <value>]
[--cli-input-json | --cli-input-yaml]
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

A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--ipam-scope-id` (string)

The ID of the scope in which you would like to create the IPAM pool.

`--locale` (string)

The locale for the pool should be one of the following:

- An Amazon Web Services Region where you want this IPAM pool to be available for allocations.
- The network border group for an Amazon Web Services Local Zone where you want this IPAM pool to be available for allocations ([supported Local Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail) ). This option is only available for IPAM IPv4 pools in the public scope.

Possible values: Any Amazon Web Services Region or supported Amazon Web Services Local Zone. Default is `none` and means any locale.

`--source-ipam-pool-id` (string)

The ID of the source IPAM pool. Use this option to create a pool within an existing pool. Note that the CIDR you provision for the pool within the source pool must be available in the source poolâs CIDR range.

`--description` (string)

A description for the IPAM pool.

`--address-family` (string)

The IP protocol assigned to this IPAM pool. You must choose either IPv4 or IPv6 protocol for a pool.

Possible values:

- `ipv4`
- `ipv6`

`--auto-import` | `--no-auto-import` (boolean)

If selected, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as allocations into your IPAM. The CIDRs that will be allocated for these resources must not already be allocated to other resources in order for the import to succeed. IPAM will import a CIDR regardless of its compliance with the poolâs allocation rules, so a resource might be imported and subsequently marked as noncompliant. If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only. If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only.

A locale must be set on the pool for this feature to work.

`--publicly-advertisable` | `--no-publicly-advertisable` (boolean)

Determines if the pool is publicly advertisable. The request can only contain `PubliclyAdvertisable` if `AddressFamily` is `ipv6` and `PublicIpSource` is `byoip` .

`--allocation-min-netmask-length` (integer)

The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. The minimum netmask length must be less than the maximum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.

`--allocation-max-netmask-length` (integer)

The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. The maximum netmask length must be greater than the minimum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.

`--allocation-default-netmask-length` (integer)

The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16.

`--allocation-resource-tags` (list)

Tags that are required for resources that use CIDRs from this IPAM pool. Resources that do not have these tags will not be allowed to allocate space from the pool. If the resources have their tags changed after they have allocated space or if the allocation tagging requirements are changed on the pool, the resource may be marked as noncompliant.

(structure)

A tag on an IPAM resource.

Key -> (string)

The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.

Value -> (string)

The value for the tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--tag-specifications` (list)

The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.

(structure)

The tags to apply to a resource when the resource is being created. When you specify a tag, you must specify the resource type to tag, otherwise the request will fail.

### Note

The `Valid Values` lists all the resource types that can be tagged. However, the action youâre using might not support tagging all of these resource types. If you try to tag a resource type that is unsupported for the action youâre using, youâll get an error.

ResourceType -> (string)

The type of resource to tag on creation.

Tags -> (list)

The tags to apply to the resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

Shorthand Syntax:

```
ResourceType=string,Tags=[{Key=string,Value=string},{Key=string,Value=string}] ...
```

JSON Syntax:

```
[
  {
    "ResourceType": "capacity-reservation"|"client-vpn-endpoint"|"customer-gateway"|"carrier-gateway"|"coip-pool"|"declarative-policies-report"|"dedicated-host"|"dhcp-options"|"egress-only-internet-gateway"|"elastic-ip"|"elastic-gpu"|"export-image-task"|"export-instance-task"|"fleet"|"fpga-image"|"host-reservation"|"image"|"import-image-task"|"import-snapshot-task"|"instance"|"instance-event-window"|"internet-gateway"|"ipam"|"ipam-pool"|"ipam-scope"|"ipv4pool-ec2"|"ipv6pool-ec2"|"key-pair"|"launch-template"|"local-gateway"|"local-gateway-route-table"|"local-gateway-virtual-interface"|"local-gateway-virtual-interface-group"|"local-gateway-route-table-vpc-association"|"local-gateway-route-table-virtual-interface-group-association"|"natgateway"|"network-acl"|"network-interface"|"network-insights-analysis"|"network-insights-path"|"network-insights-access-scope"|"network-insights-access-scope-analysis"|"outpost-lag"|"placement-group"|"prefix-list"|"replace-root-volume-task"|"reserved-instances"|"route-table"|"security-group"|"security-group-rule"|"service-link-virtual-interface"|"snapshot"|"spot-fleet-request"|"spot-instances-request"|"subnet"|"subnet-cidr-reservation"|"traffic-mirror-filter"|"traffic-mirror-session"|"traffic-mirror-target"|"transit-gateway"|"transit-gateway-attachment"|"transit-gateway-connect-peer"|"transit-gateway-multicast-domain"|"transit-gateway-policy-table"|"transit-gateway-route-table"|"transit-gateway-route-table-announcement"|"volume"|"vpc"|"vpc-endpoint"|"vpc-endpoint-connection"|"vpc-endpoint-service"|"vpc-endpoint-service-permission"|"vpc-peering-connection"|"vpn-connection"|"vpn-gateway"|"vpc-flow-log"|"capacity-reservation-fleet"|"traffic-mirror-filter-rule"|"vpc-endpoint-connection-device-type"|"verified-access-instance"|"verified-access-group"|"verified-access-endpoint"|"verified-access-policy"|"verified-access-trust-provider"|"vpn-connection-device-type"|"vpc-block-public-access-exclusion"|"route-server"|"route-server-endpoint"|"route-server-peer"|"ipam-resource-discovery"|"ipam-resource-discovery-association"|"instance-connect-endpoint"|"verified-access-endpoint-target"|"ipam-external-resource-verification-token"|"mac-modification-task",
    "Tags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  }
  ...
]
```

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) .

`--aws-service` (string)

Limits which service in Amazon Web Services that the pool can be used in. âec2â, for example, allows users to use space for Elastic IP addresses and VPCs.

Possible values:

- `ec2`

`--public-ip-source` (string)

The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip` . For more information, see [Create IPv6 pools](https://docs.aws.amazon.com/vpc/latest/ipam/intro-create-ipv6-pools.html) in the *Amazon VPC IPAM User Guide* . By default, you can add only one Amazon-provided IPv6 CIDR block to a top-level IPv6 pool if PublicIpSource is `amazon` . For information on increasing the default limit, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide* .

Possible values:

- `amazon`
- `byoip`

`--source-resource` (structure)

The resource used to provision CIDRs to a resource planning pool.

ResourceId -> (string)

The source resource ID.

ResourceType -> (string)

The source resource type.

ResourceRegion -> (string)

The source resource Region.

ResourceOwner -> (string)

The source resource owner.

Shorthand Syntax:

```
ResourceId=string,ResourceType=string,ResourceRegion=string,ResourceOwner=string
```

JSON Syntax:

```
{
  "ResourceId": "string",
  "ResourceType": "vpc",
  "ResourceRegion": "string",
  "ResourceOwner": "string"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

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

**To create an IPAM pool**

The following `create-ipam-pool` example creates an IPAM pool.

(Linux):

```
aws ec2 create-ipam-pool \
    --ipam-scope-id ipam-scope-02fc38cd4c48e7d38 \
    --address-family ipv4 \
    --auto-import \
    --allocation-min-netmask-length 16 \
    --allocation-max-netmask-length 26 \
    --allocation-default-netmask-length 24 \
    --allocation-resource-tags "Key=Environment,Value=Preprod" \
    --tag-specifications 'ResourceType=ipam-pool,Tags=[{Key=Name,Value="Preprod pool"}]'
```

(Windows):

```
aws ec2 create-ipam-pool ^
    --ipam-scope-id ipam-scope-02fc38cd4c48e7d38 ^
    --address-family ipv4 ^
    --auto-import ^
    --allocation-min-netmask-length 16 ^
    --allocation-max-netmask-length 26 ^
    --allocation-default-netmask-length 24 ^
    --allocation-resource-tags "Key=Environment,Value=Preprod" ^
    --tag-specifications ResourceType=ipam-pool,Tags=[{Key=Name,Value="Preprod pool"}]
```

Output:

```
{
    "IpamPool": {
        "OwnerId": "123456789012",
        "IpamPoolId": "ipam-pool-0533048da7d823723",
        "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0533048da7d823723",
        "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-02fc38cd4c48e7d38",
        "IpamScopeType": "private",
        "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-08440e7a3acde3908",
        "IpamRegion": "us-east-1",
        "Locale": "None",
        "PoolDepth": 1,
        "State": "create-in-progress",
        "AutoImport": true,
        "AddressFamily": "ipv4",
        "AllocationMinNetmaskLength": 16,
        "AllocationMaxNetmaskLength": 26,
        "AllocationDefaultNetmaskLength": 24,
        "AllocationResourceTags": [
            {
                "Key": "Environment",
                "Value": "Preprod"
            }
        ],
        "Tags": [
            {
                "Key": "Name",
                "Value": "Preprod pool"
            }
        ]
    }
}
```

For more information, see [Plan for IP address provisioning](https://docs.aws.amazon.com/vpc/latest/ipam/planning-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Output

IpamPool -> (structure)

Information about the IPAM pool created.

OwnerId -> (string)

The Amazon Web Services account ID of the owner of the IPAM pool.

IpamPoolId -> (string)

The ID of the IPAM pool.

SourceIpamPoolId -> (string)

The ID of the source IPAM pool. You can use this option to create an IPAM pool within an existing source pool.

IpamPoolArn -> (string)

The Amazon Resource Name (ARN) of the IPAM pool.

IpamScopeArn -> (string)

The ARN of the scope of the IPAM pool.

IpamScopeType -> (string)

In IPAM, a scope is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The private scope is intended for all private IP address space. The public scope is intended for all public IP address space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict.

IpamArn -> (string)

The ARN of the IPAM.

IpamRegion -> (string)

The Amazon Web Services Region of the IPAM pool.

Locale -> (string)

The locale of the IPAM pool.

The locale for the pool should be one of the following:

- An Amazon Web Services Region where you want this IPAM pool to be available for allocations.
- The network border group for an Amazon Web Services Local Zone where you want this IPAM pool to be available for allocations ([supported Local Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail) ). This option is only available for IPAM IPv4 pools in the public scope.

If you choose an Amazon Web Services Region for locale that has not been configured as an operating Region for the IPAM, youâll get an error.

PoolDepth -> (integer)

The depth of pools in your IPAM pool. The pool depth quota is 10. For more information, see [Quotas in IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide* .

State -> (string)

The state of the IPAM pool.

StateMessage -> (string)

The state message.

Description -> (string)

The description of the IPAM pool.

AutoImport -> (boolean)

If selected, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as allocations into your IPAM. The CIDRs that will be allocated for these resources must not already be allocated to other resources in order for the import to succeed. IPAM will import a CIDR regardless of its compliance with the poolâs allocation rules, so a resource might be imported and subsequently marked as noncompliant. If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only. If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only.

A locale must be set on the pool for this feature to work.

PubliclyAdvertisable -> (boolean)

Determines if a pool is publicly advertisable. This option is not available for pools with AddressFamily set to `ipv4` .

AddressFamily -> (string)

The address family of the pool.

AllocationMinNetmaskLength -> (integer)

The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. The minimum netmask length must be less than the maximum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.

AllocationMaxNetmaskLength -> (integer)

The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. The maximum netmask length must be greater than the minimum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.

AllocationDefaultNetmaskLength -> (integer)

The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16.

AllocationResourceTags -> (list)

Tags that are required for resources that use CIDRs from this IPAM pool. Resources that do not have these tags will not be allowed to allocate space from the pool. If the resources have their tags changed after they have allocated space or if the allocation tagging requirements are changed on the pool, the resource may be marked as noncompliant.

(structure)

The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.

Key -> (string)

The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.

Value -> (string)

The value of the tag.

Tags -> (list)

The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

AwsService -> (string)

Limits which service in Amazon Web Services that the pool can be used in. âec2â, for example, allows users to use space for Elastic IP addresses and VPCs.

PublicIpSource -> (string)

The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `BYOIP` . For more information, see [Create IPv6 pools](https://docs.aws.amazon.com/vpc/latest/ipam/intro-create-ipv6-pools.html) in the *Amazon VPC IPAM User Guide* . By default, you can add only one Amazon-provided IPv6 CIDR block to a top-level IPv6 pool. For information on increasing the default limit, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide* .

SourceResource -> (structure)

The resource used to provision CIDRs to a resource planning pool.

ResourceId -> (string)

The source resource ID.

ResourceType -> (string)

The source resource type.

ResourceRegion -> (string)

The source resource Region.

ResourceOwner -> (string)

The source resource owner.