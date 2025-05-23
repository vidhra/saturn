# create-studioÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-studio.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-studio.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# create-studio

## Description

Creates a new Amazon EMR Studio.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/CreateStudio)

## Synopsis

```
create-studio
--name <value>
[--description <value>]
--auth-mode <value>
--vpc-id <value>
--subnet-ids <value>
--service-role <value>
[--user-role <value>]
--workspace-security-group-id <value>
--engine-security-group-id <value>
--default-s3-location <value>
[--idp-auth-url <value>]
[--idp-relay-state-parameter-name <value>]
[--tags <value>]
[--trusted-identity-propagation-enabled | --no-trusted-identity-propagation-enabled]
[--idc-user-assignment <value>]
[--idc-instance-arn <value>]
[--encryption-key-arn <value>]
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

`--name` (string)

A descriptive name for the Amazon EMR Studio.

`--description` (string)

A detailed description of the Amazon EMR Studio.

`--auth-mode` (string)

Specifies whether the Studio authenticates users using IAM or IAM Identity Center.

Possible values:

- `SSO`
- `IAM`

`--vpc-id` (string)

The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.

`--subnet-ids` (list)

A list of subnet IDs to associate with the Amazon EMR Studio. A Studio can have a maximum of 5 subnets. The subnets must belong to the VPC specified by `VpcId` . Studio users can create a Workspace in any of the specified subnets.

(string)

Syntax:

```
"string" "string" ...
```

`--service-role` (string)

The IAM role that the Amazon EMR Studio assumes. The service role provides a way for Amazon EMR Studio to interoperate with other Amazon Web Services services.

`--user-role` (string)

The IAM user role that users and groups assume when logged in to an Amazon EMR Studio. Only specify a `UserRole` when you use IAM Identity Center authentication. The permissions attached to the `UserRole` can be scoped down for each user or group using session policies.

`--workspace-security-group-id` (string)

The ID of the Amazon EMR Studio Workspace security group. The Workspace security group allows outbound network traffic to resources in the Engine security group, and it must be in the same VPC specified by `VpcId` .

`--engine-security-group-id` (string)

The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by `VpcId` .

`--default-s3-location` (string)

The Amazon S3 location to back up Amazon EMR Studio Workspaces and notebook files.

`--idp-auth-url` (string)

The authentication endpoint of your identity provider (IdP). Specify this value when you use IAM authentication and want to let federated users log in to a Studio with the Studio URL and credentials from your IdP. Amazon EMR Studio redirects users to this endpoint to enter credentials.

`--idp-relay-state-parameter-name` (string)

The name that your identity provider (IdP) uses for its `RelayState` parameter. For example, `RelayState` or `TargetSource` . Specify this value when you use IAM authentication and want to let federated users log in to a Studio using the Studio URL. The `RelayState` parameter differs by IdP.

`--tags` (list)

A list of tags to associate with the Amazon EMR Studio. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.

(structure)

A key-value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html) .

Key -> (string)

A user-defined key, which is the minimum required information for a valid tag. For more information, see [Tag](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html) .

Value -> (string)

A user-defined value, which is optional in a tag. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html) .

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

`--trusted-identity-propagation-enabled` | `--no-trusted-identity-propagation-enabled` (boolean)

A Boolean indicating whether to enable Trusted identity propagation for the Studio. The default value is `false` .

`--idc-user-assignment` (string)

Specifies whether IAM Identity Center user assignment is `REQUIRED` or `OPTIONAL` . If the value is set to `REQUIRED` , users must be explicitly assigned to the Studio application to access the Studio.

Possible values:

- `REQUIRED`
- `OPTIONAL`

`--idc-instance-arn` (string)

The ARN of the IAM Identity Center instance to create the Studio application.

`--encryption-key-arn` (string)

The KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.

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

StudioId -> (string)

The ID of the Amazon EMR Studio.

Url -> (string)

The unique Studio access URL.