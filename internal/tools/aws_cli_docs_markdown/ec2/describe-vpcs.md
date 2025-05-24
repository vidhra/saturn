# describe-vpcsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpcs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpcs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-vpcs

## Description

Describes your VPCs. The default is to describe all your VPCs. Alternatively, you can specify specific VPC IDs or filter the results to include only the VPCs that match specific criteria.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcs)

`describe-vpcs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Vpcs`

## Synopsis

```
describe-vpcs
[--filters <value>]
[--vpc-ids <value>]
[--dry-run | --no-dry-run]
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

`--filters` (list)

The filters.

- `cidr` - The primary IPv4 CIDR block of the VPC. The CIDR block you specify must exactly match the VPCâs CIDR block for information to be returned for the VPC. Must contain the slash followed by one or two digits (for example, `/28` ).
- `cidr-block-association.cidr-block` - An IPv4 CIDR block associated with the VPC.
- `cidr-block-association.association-id` - The association ID for an IPv4 CIDR block associated with the VPC.
- `cidr-block-association.state` - The state of an IPv4 CIDR block associated with the VPC.
- `dhcp-options-id` - The ID of a set of DHCP options.
- `ipv6-cidr-block-association.ipv6-cidr-block` - An IPv6 CIDR block associated with the VPC.
- `ipv6-cidr-block-association.ipv6-pool` - The ID of the IPv6 address pool from which the IPv6 CIDR block is allocated.
- `ipv6-cidr-block-association.association-id` - The association ID for an IPv6 CIDR block associated with the VPC.
- `ipv6-cidr-block-association.state` - The state of an IPv6 CIDR block associated with the VPC.
- `is-default` - Indicates whether the VPC is the default VPC.
- `owner-id` - The ID of the Amazon Web Services account that owns the VPC.
- `state` - The state of the VPC (`pending` | `available` ).
- `tag` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.
- `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
- `vpc-id` - The ID of the VPC.

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

`--vpc-ids` (list)

The IDs of the VPCs.

(string)

Syntax:

```
"string" "string" ...
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

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

**Example 1: To describe all of your VPCs**

The following `describe-vpcs` example retrieves details about your VPCs.

```
aws ec2 describe-vpcs
```

Output:

```
{
    "Vpcs": [
        {
            "CidrBlock": "30.1.0.0/16",
            "DhcpOptionsId": "dopt-19edf471",
            "State": "available",
            "VpcId": "vpc-0e9801d129EXAMPLE",
            "OwnerId": "111122223333",
            "InstanceTenancy": "default",
            "CidrBlockAssociationSet": [
                {
                    "AssociationId": "vpc-cidr-assoc-062c64cfafEXAMPLE",
                    "CidrBlock": "30.1.0.0/16",
                    "CidrBlockState": {
                        "State": "associated"
                    }
                }
            ],
            "IsDefault": false,
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Not Shared"
                }
            ]
        },
        {
            "CidrBlock": "10.0.0.0/16",
            "DhcpOptionsId": "dopt-19edf471",
            "State": "available",
            "VpcId": "vpc-06e4ab6c6cEXAMPLE",
            "OwnerId": "222222222222",
            "InstanceTenancy": "default",
            "CidrBlockAssociationSet": [
                {
                    "AssociationId": "vpc-cidr-assoc-00b17b4eddEXAMPLE",
                    "CidrBlock": "10.0.0.0/16",
                    "CidrBlockState": {
                        "State": "associated"
                    }
                }
            ],
            "IsDefault": false,
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Shared VPC"
                }
            ]
        }
    ]
}
```

**Example 2: To describe a specified VPC**

The following `describe-vpcs` example retrieves details for the specified VPC.

```
aws ec2 describe-vpcs \
    --vpc-ids vpc-06e4ab6c6cEXAMPLE
```

Output:

```
{
    "Vpcs": [
        {
            "CidrBlock": "10.0.0.0/16",
            "DhcpOptionsId": "dopt-19edf471",
            "State": "available",
            "VpcId": "vpc-06e4ab6c6cEXAMPLE",
            "OwnerId": "111122223333",
            "InstanceTenancy": "default",
            "CidrBlockAssociationSet": [
                {
                    "AssociationId": "vpc-cidr-assoc-00b17b4eddEXAMPLE",
                    "CidrBlock": "10.0.0.0/16",
                    "CidrBlockState": {
                        "State": "associated"
                    }
                }
            ],
            "IsDefault": false,
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Shared VPC"
                }
            ]
        }
    ]
}
```

## Output

NextToken -> (string)

The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.

Vpcs -> (list)

Information about the VPCs.

(structure)

Describes a VPC.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the VPC.

InstanceTenancy -> (string)

The allowed tenancy of instances launched into the VPC.

Ipv6CidrBlockAssociationSet -> (list)

Information about the IPv6 CIDR blocks associated with the VPC.

(structure)

Describes an IPv6 CIDR block associated with a VPC.

AssociationId -> (string)

The association ID for the IPv6 CIDR block.

Ipv6CidrBlock -> (string)

The IPv6 CIDR block.

Ipv6CidrBlockState -> (structure)

Information about the state of the CIDR block.

State -> (string)

The state of the CIDR block.

StatusMessage -> (string)

A message about the status of the CIDR block, if applicable.

NetworkBorderGroup -> (string)

The name of the unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses, for example, `us-east-1-wl1-bos-wlz-1` .

Ipv6Pool -> (string)

The ID of the IPv6 address pool from which the IPv6 CIDR block is allocated.

Ipv6AddressAttribute -> (string)

Public IPv6 addresses are those advertised on the internet from Amazon Web Services. Private IP addresses are not and cannot be advertised on the internet from Amazon Web Services.

IpSource -> (string)

The source that allocated the IP address space. `byoip` or `amazon` indicates public IP address space allocated by Amazon or space that you have allocated with Bring your own IP (BYOIP). `none` indicates private space.

CidrBlockAssociationSet -> (list)

Information about the IPv4 CIDR blocks associated with the VPC.

(structure)

Describes an IPv4 CIDR block associated with a VPC.

AssociationId -> (string)

The association ID for the IPv4 CIDR block.

CidrBlock -> (string)

The IPv4 CIDR block.

CidrBlockState -> (structure)

Information about the state of the CIDR block.

State -> (string)

The state of the CIDR block.

StatusMessage -> (string)

A message about the status of the CIDR block, if applicable.

IsDefault -> (boolean)

Indicates whether the VPC is the default VPC.

EncryptionControl -> (structure)

VpcId -> (string)

VpcEncryptionControlId -> (string)

Mode -> (string)

State -> (string)

StateMessage -> (string)

ResourceExclusions -> (structure)

InternetGateway -> (structure)

State -> (string)

StateMessage -> (string)

EgressOnlyInternetGateway -> (structure)

State -> (string)

StateMessage -> (string)

NatGateway -> (structure)

State -> (string)

StateMessage -> (string)

VirtualPrivateGateway -> (structure)

State -> (string)

StateMessage -> (string)

VpcPeering -> (structure)

State -> (string)

StateMessage -> (string)

Tags -> (list)

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

Tags -> (list)

Any tags assigned to the VPC.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

BlockPublicAccessStates -> (structure)

The state of VPC Block Public Access (BPA).

InternetGatewayBlockMode -> (string)

The mode of VPC BPA.

- `off` : VPC BPA is not enabled and traffic is allowed to and from internet gateways and egress-only internet gateways in this Region.
- `block-bidirectional` : Block all traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets).
- `block-ingress` : Block all internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded). Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.

VpcId -> (string)

The ID of the VPC.

State -> (string)

The current state of the VPC.

CidrBlock -> (string)

The primary IPv4 CIDR block for the VPC.

DhcpOptionsId -> (string)

The ID of the set of DHCP options youâve associated with the VPC.