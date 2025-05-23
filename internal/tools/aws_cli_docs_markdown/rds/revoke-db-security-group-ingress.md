# revoke-db-security-group-ingressÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/revoke-db-security-group-ingress.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/revoke-db-security-group-ingress.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# revoke-db-security-group-ingress

## Description

Revokes ingress from a DBSecurityGroup for previously authorized IP ranges or EC2 or VPC security groups. Required parameters for this API are one of CIDRIP, EC2SecurityGroupId for VPC, or (EC2SecurityGroupOwnerId and either EC2SecurityGroupName or EC2SecurityGroupId).

### Note

EC2-Classic was retired on August 15, 2022. If you havenât migrated from EC2-Classic to a VPC, we recommend that you migrate as soon as possible. For more information, see [Migrate from EC2-Classic to a VPC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html) in the *Amazon EC2 User Guide* , the blog [EC2-Classic Networking is Retiring â Hereâs How to Prepare](http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/) , and [Moving a DB instance not in a VPC into a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html) in the *Amazon RDS User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/RevokeDBSecurityGroupIngress)

## Synopsis

```
revoke-db-security-group-ingress
--db-security-group-name <value>
[--cidrip <value>]
[--ec2-security-group-name <value>]
[--ec2-security-group-id <value>]
[--ec2-security-group-owner-id <value>]
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

`--db-security-group-name` (string)

The name of the DB security group to revoke ingress from.

`--cidrip` (string)

The IP range to revoke access from. Must be a valid CIDR range. If `CIDRIP` is specified, `EC2SecurityGroupName` , `EC2SecurityGroupId` and `EC2SecurityGroupOwnerId` canât be provided.

`--ec2-security-group-name` (string)

The name of the EC2 security group to revoke access from. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, EC2SecurityGroupOwnerId and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.

`--ec2-security-group-id` (string)

The id of the EC2 security group to revoke access from. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, EC2SecurityGroupOwnerId and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.

`--ec2-security-group-owner-id` (string)

The Amazon Web Services account number of the owner of the EC2 security group specified in the `EC2SecurityGroupName` parameter. The Amazon Web Services access key ID isnât an acceptable value. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, EC2SecurityGroupOwnerId and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.

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

## Output

DBSecurityGroup -> (structure)

Contains the details for an Amazon RDS DB security group.

This data type is used as a response element in the `DescribeDBSecurityGroups` action.

OwnerId -> (string)

Provides the Amazon Web Services ID of the owner of a specific DB security group.

DBSecurityGroupName -> (string)

Specifies the name of the DB security group.

DBSecurityGroupDescription -> (string)

Provides the description of the DB security group.

VpcId -> (string)

Provides the VpcId of the DB security group.

EC2SecurityGroups -> (list)

Contains a list of `EC2SecurityGroup` elements.

(structure)

This data type is used as a response element in the following actions:

- `AuthorizeDBSecurityGroupIngress`
- `DescribeDBSecurityGroups`
- `RevokeDBSecurityGroupIngress`

Status -> (string)

Provides the status of the EC2 security group. Status can be âauthorizingâ, âauthorizedâ, ârevokingâ, and ârevokedâ.

EC2SecurityGroupName -> (string)

Specifies the name of the EC2 security group.

EC2SecurityGroupId -> (string)

Specifies the id of the EC2 security group.

EC2SecurityGroupOwnerId -> (string)

Specifies the Amazon Web Services ID of the owner of the EC2 security group specified in the `EC2SecurityGroupName` field.

IPRanges -> (list)

Contains a list of `IPRange` elements.

(structure)

This data type is used as a response element in the `DescribeDBSecurityGroups` action.

Status -> (string)

The status of the IP range. Status can be âauthorizingâ, âauthorizedâ, ârevokingâ, and ârevokedâ.

CIDRIP -> (string)

The IP range.

DBSecurityGroupArn -> (string)

The Amazon Resource Name (ARN) for the DB security group.