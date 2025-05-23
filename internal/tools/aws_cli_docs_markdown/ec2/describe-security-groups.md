# describe-security-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-groups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-groups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-security-groups

## Description

Describes the specified security groups or all of your security groups.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSecurityGroups)

`describe-security-groups` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `SecurityGroups`

## Synopsis

```
describe-security-groups
[--group-ids <value>]
[--group-names <value>]
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

`--group-ids` (list)

The IDs of the security groups. Required for security groups in a nondefault VPC.

Default: Describes all of your security groups.

(string)

Syntax:

```
"string" "string" ...
```

`--group-names` (list)

[Default VPC] The names of the security groups. You can specify either the security group name or the security group ID.

Default: Describes all of your security groups.

(string)

Syntax:

```
"string" "string" ...
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--filters` (list)

The filters. If using multiple filters for rules, the results include security groups for which any combination of rules - not necessarily a single rule - match all filters.

- `description` - The description of the security group.
- `egress.ip-permission.cidr` - An IPv4 CIDR block for an outbound security group rule.
- `egress.ip-permission.from-port` - For an outbound rule, the start of port range for the TCP and UDP protocols, or an ICMP type number.
- `egress.ip-permission.group-id` - The ID of a security group that has been referenced in an outbound security group rule.
- `egress.ip-permission.group-name` - The name of a security group that is referenced in an outbound security group rule.
- `egress.ip-permission.ipv6-cidr` - An IPv6 CIDR block for an outbound security group rule.
- `egress.ip-permission.prefix-list-id` - The ID of a prefix list to which a security group rule allows outbound access.
- `egress.ip-permission.protocol` - The IP protocol for an outbound security group rule (`tcp` | `udp` | `icmp` , a protocol number, or -1 for all protocols).
- `egress.ip-permission.to-port` - For an outbound rule, the end of port range for the TCP and UDP protocols, or an ICMP code.
- `egress.ip-permission.user-id` - The ID of an Amazon Web Services account that has been referenced in an outbound security group rule.
- `group-id` - The ID of the security group.
- `group-name` - The name of the security group.
- `ip-permission.cidr` - An IPv4 CIDR block for an inbound security group rule.
- `ip-permission.from-port` - For an inbound rule, the start of port range for the TCP and UDP protocols, or an ICMP type number.
- `ip-permission.group-id` - The ID of a security group that has been referenced in an inbound security group rule.
- `ip-permission.group-name` - The name of a security group that is referenced in an inbound security group rule.
- `ip-permission.ipv6-cidr` - An IPv6 CIDR block for an inbound security group rule.
- `ip-permission.prefix-list-id` - The ID of a prefix list from which a security group rule allows inbound access.
- `ip-permission.protocol` - The IP protocol for an inbound security group rule (`tcp` | `udp` | `icmp` , a protocol number, or -1 for all protocols).
- `ip-permission.to-port` - For an inbound rule, the end of port range for the TCP and UDP protocols, or an ICMP code.
- `ip-permission.user-id` - The ID of an Amazon Web Services account that has been referenced in an inbound security group rule.
- `owner-id` - The Amazon Web Services account ID of the owner of the security group.
- `tag` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.
- `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
- `vpc-id` - The ID of the VPC specified when the security group was created.

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

**Example 1: To describe a security group**

The following `describe-security-groups` example describes the specified security group.

```
aws ec2 describe-security-groups \
    --group-ids sg-903004f8
```

Output:

```
{
    "SecurityGroups": [
        {
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "UserIdGroupPairs": [],
                    "PrefixListIds": []
                }
            ],
            "Description": "My security group",
            "Tags": [
                {
                    "Value": "SG1",
                    "Key": "Name"
                }
            ],
            "IpPermissions": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [],
                    "UserIdGroupPairs": [
                        {
                            "UserId": "123456789012",
                            "GroupId": "sg-903004f8"
                        }
                    ],
                    "PrefixListIds": []
                },
                {
                    "PrefixListIds": [],
                    "FromPort": 22,
                    "IpRanges": [
                        {
                            "Description": "Access from NY office",
                            "CidrIp": "203.0.113.0/24"
                        }
                    ],
                    "ToPort": 22,
                    "IpProtocol": "tcp",
                    "UserIdGroupPairs": []
                    }
            ],
            "GroupName": "MySecurityGroup",
            "VpcId": "vpc-1a2b3c4d",
            "OwnerId": "123456789012",
            "GroupId": "sg-903004f8",
        }
    ]
}
```

**Example 2: To describe security groups that have specific rules**

The following `describe-security-groups` example uses filters to scope the results to security groups that have a rule that allows SSH traffic (port 22) and a rule that allows traffic from all addresses (`0.0.0.0/0`). The example uses the `--query` parameter to display only the names of the security groups. Security groups must match all filters to be returned in the results; however, a single rule does not have to match all filters. For example, the output returns a security group with a rule that allows SSH traffic from a specific IP address and another rule that allows HTTP traffic from all addresses.

```
aws ec2 describe-security-groups \
    --filters Name=ip-permission.from-port,Values=22 Name=ip-permission.to-port,Values=22 Name=ip-permission.cidr,Values='0.0.0.0/0' \
    --query "SecurityGroups[*].[GroupName]" \
    --output text
```

Output:

```
default
my-security-group
web-servers
launch-wizard-1
```

**Example 3: To describe security groups based on tags**

The following `describe-security-groups` example uses filters to scope the results to security groups that include `test` in the security group name, and that have the tag `Test=To-delete`. The example uses the `--query` parameter to display only the names and IDs of the security groups.

```
aws ec2 describe-security-groups \
    --filters Name=group-name,Values=*test* Name=tag:Test,Values=To-delete \
    --query "SecurityGroups[*].{Name:GroupName,ID:GroupId}"
```

Output:

```
[
    {
        "Name": "testfornewinstance",
        "ID": "sg-33bb22aa"
    },
    {
        "Name": "newgrouptest",
        "ID": "sg-1a2b3c4d"
    }
]
```

For additional examples using tag filters, see [Working with tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_CLI) in the *Amazon EC2 User Guide*.

## Output

NextToken -> (string)

The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.

SecurityGroups -> (list)

Information about the security groups.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

IpPermissionsEgress -> (list)

The outbound rules associated with the security group.

(structure)

Describes the permissions for a security group rule.

IpProtocol -> (string)

The IP protocol name (`tcp` , `udp` , `icmp` , `icmpv6` ) or number (see [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) ).

Use `-1` to specify all protocols. When authorizing security group rules, specifying `-1` or a protocol number other than `tcp` , `udp` , `icmp` , or `icmpv6` allows traffic on all ports, regardless of any port range you specify. For `tcp` , `udp` , and `icmp` , you must specify a port range. For `icmpv6` , the port range is optional; if you omit the port range, traffic for all types and codes is allowed.

FromPort -> (integer)

If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).

ToPort -> (integer)

If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).

UserIdGroupPairs -> (list)

The security group and Amazon Web Services account ID pairs.

(structure)

Describes a security group and Amazon Web Services account ID pair.

Description -> (string)

A description for the security group rule that references this user ID group pair.

Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*

UserId -> (string)

The ID of an Amazon Web Services account.

For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.

GroupName -> (string)

[Default VPC] The name of the security group. For a security group in a nondefault VPC, use the security group ID.

For a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.

GroupId -> (string)

The ID of the security group.

VpcId -> (string)

The ID of the VPC for the referenced security group, if applicable.

VpcPeeringConnectionId -> (string)

The ID of the VPC peering connection, if applicable.

PeeringStatus -> (string)

The status of a VPC peering connection, if applicable.

IpRanges -> (list)

The IPv4 address ranges.

(structure)

Describes an IPv4 address range.

Description -> (string)

A description for the security group rule that references this IPv4 address range.

Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*

CidrIp -> (string)

The IPv4 address range. You can either specify a CIDR block or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length.

### Note

Amazon Web Services [canonicalizes](https://en.wikipedia.org/wiki/Canonicalization) IPv4 and IPv6 CIDRs. For example, if you specify 100.68.0.18/18 for the CIDR block, Amazon Web Services canonicalizes the CIDR block to 100.68.0.0/18. Any subsequent DescribeSecurityGroups and DescribeSecurityGroupRules calls will return the canonicalized form of the CIDR block. Additionally, if you attempt to add another rule with the non-canonical form of the CIDR (such as 100.68.0.18/18) and there is already a rule for the canonicalized form of the CIDR block (such as 100.68.0.0/18), the API throws an duplicate rule error.

Ipv6Ranges -> (list)

The IPv6 address ranges.

(structure)

Describes an IPv6 address range.

Description -> (string)

A description for the security group rule that references this IPv6 address range.

Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*

CidrIpv6 -> (string)

The IPv6 address range. You can either specify a CIDR block or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length.

### Note

Amazon Web Services [canonicalizes](https://en.wikipedia.org/wiki/Canonicalization) IPv4 and IPv6 CIDRs. For example, if you specify 100.68.0.18/18 for the CIDR block, Amazon Web Services canonicalizes the CIDR block to 100.68.0.0/18. Any subsequent DescribeSecurityGroups and DescribeSecurityGroupRules calls will return the canonicalized form of the CIDR block. Additionally, if you attempt to add another rule with the non-canonical form of the CIDR (such as 100.68.0.18/18) and there is already a rule for the canonicalized form of the CIDR block (such as 100.68.0.0/18), the API throws an duplicate rule error.

PrefixListIds -> (list)

The prefix list IDs.

(structure)

Describes a prefix list ID.

Description -> (string)

A description for the security group rule that references this prefix list ID.

Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*

PrefixListId -> (string)

The ID of the prefix.

Tags -> (list)

Any tags assigned to the security group.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

VpcId -> (string)

The ID of the VPC for the security group.

SecurityGroupArn -> (string)

The ARN of the security group.

OwnerId -> (string)

The Amazon Web Services account ID of the owner of the security group.

GroupName -> (string)

The name of the security group.

Description -> (string)

A description of the security group.

IpPermissions -> (list)

The inbound rules associated with the security group.

(structure)

Describes the permissions for a security group rule.

IpProtocol -> (string)

The IP protocol name (`tcp` , `udp` , `icmp` , `icmpv6` ) or number (see [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) ).

Use `-1` to specify all protocols. When authorizing security group rules, specifying `-1` or a protocol number other than `tcp` , `udp` , `icmp` , or `icmpv6` allows traffic on all ports, regardless of any port range you specify. For `tcp` , `udp` , and `icmp` , you must specify a port range. For `icmpv6` , the port range is optional; if you omit the port range, traffic for all types and codes is allowed.

FromPort -> (integer)

If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).

ToPort -> (integer)

If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).

UserIdGroupPairs -> (list)

The security group and Amazon Web Services account ID pairs.

(structure)

Describes a security group and Amazon Web Services account ID pair.

Description -> (string)

A description for the security group rule that references this user ID group pair.

Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*

UserId -> (string)

The ID of an Amazon Web Services account.

For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.

GroupName -> (string)

[Default VPC] The name of the security group. For a security group in a nondefault VPC, use the security group ID.

For a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.

GroupId -> (string)

The ID of the security group.

VpcId -> (string)

The ID of the VPC for the referenced security group, if applicable.

VpcPeeringConnectionId -> (string)

The ID of the VPC peering connection, if applicable.

PeeringStatus -> (string)

The status of a VPC peering connection, if applicable.

IpRanges -> (list)

The IPv4 address ranges.

(structure)

Describes an IPv4 address range.

Description -> (string)

A description for the security group rule that references this IPv4 address range.

Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*

CidrIp -> (string)

The IPv4 address range. You can either specify a CIDR block or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length.

### Note

Amazon Web Services [canonicalizes](https://en.wikipedia.org/wiki/Canonicalization) IPv4 and IPv6 CIDRs. For example, if you specify 100.68.0.18/18 for the CIDR block, Amazon Web Services canonicalizes the CIDR block to 100.68.0.0/18. Any subsequent DescribeSecurityGroups and DescribeSecurityGroupRules calls will return the canonicalized form of the CIDR block. Additionally, if you attempt to add another rule with the non-canonical form of the CIDR (such as 100.68.0.18/18) and there is already a rule for the canonicalized form of the CIDR block (such as 100.68.0.0/18), the API throws an duplicate rule error.

Ipv6Ranges -> (list)

The IPv6 address ranges.

(structure)

Describes an IPv6 address range.

Description -> (string)

A description for the security group rule that references this IPv6 address range.

Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*

CidrIpv6 -> (string)

The IPv6 address range. You can either specify a CIDR block or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length.

### Note

Amazon Web Services [canonicalizes](https://en.wikipedia.org/wiki/Canonicalization) IPv4 and IPv6 CIDRs. For example, if you specify 100.68.0.18/18 for the CIDR block, Amazon Web Services canonicalizes the CIDR block to 100.68.0.0/18. Any subsequent DescribeSecurityGroups and DescribeSecurityGroupRules calls will return the canonicalized form of the CIDR block. Additionally, if you attempt to add another rule with the non-canonical form of the CIDR (such as 100.68.0.18/18) and there is already a rule for the canonicalized form of the CIDR block (such as 100.68.0.0/18), the API throws an duplicate rule error.

PrefixListIds -> (list)

The prefix list IDs.

(structure)

Describes a prefix list ID.

Description -> (string)

A description for the security group rule that references this prefix list ID.

Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*

PrefixListId -> (string)

The ID of the prefix.