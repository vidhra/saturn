# create-instance-profileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-instance-profile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-instance-profile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# create-instance-profile

## Description

Creates the instance profile using the specified parameters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateInstanceProfile)

## Synopsis

```
create-instance-profile
[--availability-zone <value>]
[--kms-key-arn <value>]
[--publicly-accessible | --no-publicly-accessible]
[--tags <value>]
[--network-type <value>]
[--instance-profile-name <value>]
[--description <value>]
[--subnet-group-identifier <value>]
[--vpc-security-groups <value>]
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

`--availability-zone` (string)

The Availability Zone where the instance profile will be created. The default value is a random, system-chosen Availability Zone in the Amazon Web Services Region where your data provider is created, for examplem `us-east-1d` .

`--kms-key-arn` (string)

The Amazon Resource Name (ARN) of the KMS key that is used to encrypt the connection parameters for the instance profile.

If you donât specify a value for the `KmsKeyArn` parameter, then DMS uses your default encryption key.

KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

Specifies the accessibility options for the instance profile. A value of `true` represents an instance profile with a public IP address. A value of `false` represents an instance profile with a private IP address. The default value is `true` .

`--tags` (list)

One or more tags to be assigned to the instance profile.

(structure)

A user-defined key-value pair that describes metadata added to an DMS resource and that is used by operations such as the following:

- `AddTagsToResource`
- `ListTagsForResource`
- `RemoveTagsFromResource`

Key -> (string)

A key is the required name of the tag. The string value can be 1-128 Unicode characters in length and canât be prefixed with âaws:â or âdms:â. The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regular expressions: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be 1-256 Unicode characters in length and canât be prefixed with âaws:â or âdms:â. The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regular expressions: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

ResourceArn -> (string)

The Amazon Resource Name (ARN) string that uniquely identifies the resource for which the tag is created.

Shorthand Syntax:

```
Key=string,Value=string,ResourceArn=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string",
    "ResourceArn": "string"
  }
  ...
]
```

`--network-type` (string)

Specifies the network type for the instance profile. A value of `IPV4` represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of `IPV6` represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of `DUAL` represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.

`--instance-profile-name` (string)

A user-friendly name for the instance profile.

`--description` (string)

A user-friendly description of the instance profile.

`--subnet-group-identifier` (string)

A subnet group to associate with the instance profile.

`--vpc-security-groups` (list)

Specifies the VPC security group names to be used with the instance profile. The VPC security group must work with the VPC containing the instance profile.

(string)

Syntax:

```
"string" "string" ...
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

## Output

InstanceProfile -> (structure)

The instance profile that was created.

InstanceProfileArn -> (string)

The Amazon Resource Name (ARN) string that uniquely identifies the instance profile.

AvailabilityZone -> (string)

The Availability Zone where the instance profile runs.

KmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the KMS key that is used to encrypt the connection parameters for the instance profile.

If you donât specify a value for the `KmsKeyArn` parameter, then DMS uses your default encryption key.

KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

PubliclyAccessible -> (boolean)

Specifies the accessibility options for the instance profile. A value of `true` represents an instance profile with a public IP address. A value of `false` represents an instance profile with a private IP address. The default value is `true` .

NetworkType -> (string)

Specifies the network type for the instance profile. A value of `IPV4` represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of `IPV6` represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of `DUAL` represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.

InstanceProfileName -> (string)

The user-friendly name for the instance profile.

Description -> (string)

A description of the instance profile. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens (â-â). Also, it canât end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.

InstanceProfileCreationTime -> (timestamp)

The time the instance profile was created.

SubnetGroupIdentifier -> (string)

The identifier of the subnet group that is associated with the instance profile.

VpcSecurityGroups -> (list)

The VPC security groups that are used with the instance profile. The VPC security group must work with the VPC containing the instance profile.

(string)