# describe-studioÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-studio.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-studio.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# describe-studio

## Description

Returns details for the specified Amazon EMR Studio including ID, Name, VPC, Studio access URL, and so on.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/DescribeStudio)

## Synopsis

```
describe-studio
--studio-id <value>
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

`--studio-id` (string)

The Amazon EMR Studio ID.

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

Studio -> (structure)

The Amazon EMR Studio details.

StudioId -> (string)

The ID of the Amazon EMR Studio.

StudioArn -> (string)

The Amazon Resource Name (ARN) of the Amazon EMR Studio.

Name -> (string)

The name of the Amazon EMR Studio.

Description -> (string)

The detailed description of the Amazon EMR Studio.

AuthMode -> (string)

Specifies whether the Amazon EMR Studio authenticates users with IAM or IAM Identity Center.

VpcId -> (string)

The ID of the VPC associated with the Amazon EMR Studio.

SubnetIds -> (list)

The list of IDs of the subnets associated with the Amazon EMR Studio.

(string)

ServiceRole -> (string)

The name of the IAM role assumed by the Amazon EMR Studio.

UserRole -> (string)

The name of the IAM role assumed by users logged in to the Amazon EMR Studio. A Studio only requires a `UserRole` when you use IAM authentication.

WorkspaceSecurityGroupId -> (string)

The ID of the Workspace security group associated with the Amazon EMR Studio. The Workspace security group allows outbound network traffic to resources in the Engine security group and to the internet.

EngineSecurityGroupId -> (string)

The ID of the Engine security group associated with the Amazon EMR Studio. The Engine security group allows inbound network traffic from resources in the Workspace security group.

Url -> (string)

The unique access URL of the Amazon EMR Studio.

CreationTime -> (timestamp)

The time the Amazon EMR Studio was created.

DefaultS3Location -> (string)

The Amazon S3 location to back up Amazon EMR Studio Workspaces and notebook files.

IdpAuthUrl -> (string)

Your identity providerâs authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.

IdpRelayStateParameterName -> (string)

The name of your identity providerâs `RelayState` parameter.

Tags -> (list)

A list of tags associated with the Amazon EMR Studio.

(structure)

A key-value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html) .

Key -> (string)

A user-defined key, which is the minimum required information for a valid tag. For more information, see [Tag](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html) .

Value -> (string)

A user-defined value, which is optional in a tag. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html) .

IdcInstanceArn -> (string)

The ARN of the IAM Identity Center instance the Studio application belongs to.

TrustedIdentityPropagationEnabled -> (boolean)

Indicates whether the Studio has Trusted identity propagation enabled. The default value is `false` .

IdcUserAssignment -> (string)

Indicates whether the Studio has `REQUIRED` or `OPTIONAL` IAM Identity Center user assignment. If the value is set to `REQUIRED` , users must be explicitly assigned to the Studio application to access the Studio.

EncryptionKeyArn -> (string)

The KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.