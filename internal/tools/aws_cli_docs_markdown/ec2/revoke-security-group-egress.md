# revoke-security-group-egressÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/revoke-security-group-egress.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/revoke-security-group-egress.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# revoke-security-group-egress

## Description

Removes the specified outbound (egress) rules from the specified security group.

You can specify rules using either rule IDs or security group rule properties. If you use rule properties, the values that you specify (for example, ports) must match the existing ruleâs values exactly. Each rule has a protocol, from and to ports, and destination (CIDR range, security group, or prefix list). For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code. If the security group rule has a description, you do not need to specify the description to revoke the rule.

For a default VPC, if the values you specify do not match the existing ruleâs values, no error is returned, and the output describes the security group rules that were not revoked.

Amazon Web Services recommends that you describe the security group to verify that the rules were removed.

Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RevokeSecurityGroupEgress)

## Synopsis

```
revoke-security-group-egress
[--security-group-rule-ids <value>]
[--dry-run | --no-dry-run]
--group-id <value>
[--ip-permissions <value>]
[--protocol <value>]
[--port <value>]
[--cidr <value>]
[--source-group <value>]
[--group-owner <value>]
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

`--security-group-rule-ids` (list)

The IDs of the security group rules.

(string)

Syntax:

```
"string" "string" ...
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--group-id` (string)

The ID of the security group.

`--ip-permissions` (list)

The sets of IP permissions. You canât specify a destination security group and a CIDR IP address range in the same set of permissions.

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

Shorthand Syntax:

```
IpProtocol=string,FromPort=integer,ToPort=integer,UserIdGroupPairs=[{Description=string,UserId=string,GroupName=string,GroupId=string,VpcId=string,VpcPeeringConnectionId=string,PeeringStatus=string},{Description=string,UserId=string,GroupName=string,GroupId=string,VpcId=string,VpcPeeringConnectionId=string,PeeringStatus=string}],IpRanges=[{Description=string,CidrIp=string},{Description=string,CidrIp=string}],Ipv6Ranges=[{Description=string,CidrIpv6=string},{Description=string,CidrIpv6=string}],PrefixListIds=[{Description=string,PrefixListId=string},{Description=string,PrefixListId=string}] ...
```

JSON Syntax:

```
[
  {
    "IpProtocol": "string",
    "FromPort": integer,
    "ToPort": integer,
    "UserIdGroupPairs": [
      {
        "Description": "string",
        "UserId": "string",
        "GroupName": "string",
        "GroupId": "string",
        "VpcId": "string",
        "VpcPeeringConnectionId": "string",
        "PeeringStatus": "string"
      }
      ...
    ],
    "IpRanges": [
      {
        "Description": "string",
        "CidrIp": "string"
      }
      ...
    ],
    "Ipv6Ranges": [
      {
        "Description": "string",
        "CidrIpv6": "string"
      }
      ...
    ],
    "PrefixListIds": [
      {
        "Description": "string",
        "PrefixListId": "string"
      }
      ...
    ]
  }
  ...
]
```

`--protocol` (string)

The IP protocol: `tcp` | `udp` | `icmp`

(VPC only) Use `all` to specify all protocols.

If this argument is provided without also providing the `port` argument, then it will be applied to all ports for the specified protocol.

`--port` (string)

For TCP or UDP: The range of ports to allow. A single integer or a range (`min-max` ).

For ICMP: A single integer or a range (`type-code` ) representing the ICMP type number and the ICMP code number respectively. A value of -1 indicates all ICMP codes for all ICMP types. A value of -1 just for `type` indicates all ICMP codes for the specified ICMP type.

`--cidr` (string)

The IPv4 address range, in CIDR format.

`--source-group` (string)

The name or ID of the source security group.

`--group-owner` (string)

The AWS account ID that owns the source security group. Cannot be used when specifying a CIDR IP address.

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

**Example 1: To remove the rule that allows outbound traffic to a specific address range**

The following `revoke-security-group-egress` example command removes the rule that grants access to the specified address ranges on TCP port 80.

```
aws ec2 revoke-security-group-egress \
    --group-id sg-026c12253ce15eff7 \
    --ip-permissions [{IpProtocol=tcp,FromPort=80,ToPort=80,IpRanges=[{CidrIp=10.0.0.0/16}]
```

This command produces no output.

For more information, see [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) in the *Amazon EC2 User Guide*.

**Example 2: To remove the rule that allows outbound traffic to a specific security group**

The following `revoke-security-group-egress` example command removes the rule that grants access to the specified security group on TCP port 80.

```
aws ec2 revoke-security-group-egress \
    --group-id sg-026c12253ce15eff7 \
    --ip-permissions '[{"IpProtocol": "tcp", "FromPort": 443, "ToPort": 443,"UserIdGroupPairs": [{"GroupId": "sg-06df23a01ff2df86d"}]}]'
```

This command produces no output.

For more information, see [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) in the *Amazon EC2 User Guide*.

## Output

Return -> (boolean)

Returns `true` if the request succeeds; otherwise, returns an error.

UnknownIpPermissions -> (list)

The outbound rules that were unknown to the service. In some cases, `unknownIpPermissionSet` might be in a different format from the request parameter.

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

RevokedSecurityGroupRules -> (list)

Details about the revoked security group rules.

(structure)

A security group rule removed with [RevokeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html) or [RevokeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html) .

SecurityGroupRuleId -> (string)

A security group rule ID.

GroupId -> (string)

A security group ID.

IsEgress -> (boolean)

Defines if a security group rule is an outbound rule.

IpProtocol -> (string)

The security group ruleâs protocol.

FromPort -> (integer)

The âfromâ port number of the security group rule.

ToPort -> (integer)

The âtoâ port number of the security group rule.

CidrIpv4 -> (string)

The IPv4 CIDR of the traffic source.

CidrIpv6 -> (string)

The IPv6 CIDR of the traffic source.

PrefixListId -> (string)

The ID of a prefix list thatâs the traffic source.

ReferencedGroupId -> (string)

The ID of a referenced security group.

Description -> (string)

A description of the revoked security group rule.