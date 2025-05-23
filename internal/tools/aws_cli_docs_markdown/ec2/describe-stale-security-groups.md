# describe-stale-security-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-stale-security-groups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-stale-security-groups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-stale-security-groups

## Description

Describes the stale security group rules for security groups referenced across a VPC peering connection, transit gateway connection, or with a security group VPC association. Rules are stale when they reference a deleted security group. Rules can also be stale if they reference a security group in a peer VPC for which the VPC peering connection has been deleted, across a transit gateway where the transit gateway has been deleted (or [the transit gateway security group referencing feature](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security) has been disabled), or if a security group VPC association has been disassociated.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeStaleSecurityGroups)

`describe-stale-security-groups` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `StaleSecurityGroupSet`

## Synopsis

```
describe-stale-security-groups
[--dry-run | --no-dry-run]
--vpc-id <value>
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

`--vpc-id` (string)

The ID of the VPC.

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

**To describe stale security groups**

This example describes stale security group rules for `vpc-11223344`. The response shows that sg-5fa68d3a in your account has a stale ingress SSH rule that references `sg-279ab042` in the peer VPC, and that `sg-fe6fba9a` in your account has a stale egress SSH rule that references `sg-ef6fba8b` in the peer VPC.

Command:

```
aws ec2 describe-stale-security-groups --vpc-id vpc-11223344
```

Output:

```
{
  "StaleSecurityGroupSet": [
      {
          "VpcId": "vpc-11223344",
          "StaleIpPermissionsEgress": [
              {
                  "ToPort": 22,
                  "FromPort": 22,
                  "UserIdGroupPairs": [
                      {
                          "VpcId": "vpc-7a20e51f",
                          "GroupId": "sg-ef6fba8b",
                          "VpcPeeringConnectionId": "pcx-b04deed9",
                          "PeeringStatus": "active"
                      }
                  ],
                  "IpProtocol": "tcp"
              }
          ],
          "GroupName": "MySG1",
          "StaleIpPermissions": [],
          "GroupId": "sg-fe6fba9a",
          "Description": MySG1"
      },
      {
          "VpcId": "vpc-11223344",
          "StaleIpPermissionsEgress": [],
          "GroupName": "MySG2",
          "StaleIpPermissions": [
              {
                  "ToPort": 22,
                  "FromPort": 22,
                  "UserIdGroupPairs": [
                      {
                          "VpcId": "vpc-7a20e51f",
                          "GroupId": "sg-279ab042",
                          "Description": "Access from pcx-b04deed9",
                          "VpcPeeringConnectionId": "pcx-b04deed9",
                          "PeeringStatus": "active"
                      }
                  ],
                  "IpProtocol": "tcp"
              }
          ],
          "GroupId": "sg-5fa68d3a",
          "Description": "MySG2"
      }
  ]
}
```

## Output

NextToken -> (string)

The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.

StaleSecurityGroupSet -> (list)

Information about the stale security groups.

(structure)

Describes a stale security group (a security group that contains stale rules).

Description -> (string)

The description of the security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.

StaleIpPermissions -> (list)

Information about the stale inbound rules in the security group.

(structure)

Describes a stale rule in a security group.

FromPort -> (integer)

If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).

IpProtocol -> (string)

The IP protocol name (`tcp` , `udp` , `icmp` , `icmpv6` ) or number (see [Protocol Numbers)](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) .

IpRanges -> (list)

The IP ranges. Not applicable for stale security group rules.

(string)

PrefixListIds -> (list)

The prefix list IDs. Not applicable for stale security group rules.

(string)

ToPort -> (integer)

If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes).

UserIdGroupPairs -> (list)

The security group pairs. Returns the ID of the referenced security group and VPC, and the ID and status of the VPC peering connection.

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

StaleIpPermissionsEgress -> (list)

Information about the stale outbound rules in the security group.

(structure)

Describes a stale rule in a security group.

FromPort -> (integer)

If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).

IpProtocol -> (string)

The IP protocol name (`tcp` , `udp` , `icmp` , `icmpv6` ) or number (see [Protocol Numbers)](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) .

IpRanges -> (list)

The IP ranges. Not applicable for stale security group rules.

(string)

PrefixListIds -> (list)

The prefix list IDs. Not applicable for stale security group rules.

(string)

ToPort -> (integer)

If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes).

UserIdGroupPairs -> (list)

The security group pairs. Returns the ID of the referenced security group and VPC, and the ID and status of the VPC peering connection.

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

VpcId -> (string)

The ID of the VPC for the security group.