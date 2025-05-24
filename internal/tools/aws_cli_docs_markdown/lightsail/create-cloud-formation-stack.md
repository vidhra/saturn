# create-cloud-formation-stackÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-cloud-formation-stack.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-cloud-formation-stack.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# create-cloud-formation-stack

## Description

Creates an AWS CloudFormation stack, which creates a new Amazon EC2 instance from an exported Amazon Lightsail snapshot. This operation results in a CloudFormation stack record that can be used to track the AWS CloudFormation stack created. Use the `get cloud formation stack records` operation to get a list of the CloudFormation stacks created.

### Warning

Wait until after your new Amazon EC2 instance is created before running the `create cloud formation stack` operation again with the same export snapshot record.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateCloudFormationStack)

## Synopsis

```
create-cloud-formation-stack
--instances <value>
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

`--instances` (list)

An array of parameters that will be used to create the new Amazon EC2 instance. You can only pass one instance entry at a time in this array. You will get an invalid parameter error if you pass more than one instance entry in this array.

(structure)

Describes the Amazon Elastic Compute Cloud instance and related resources to be created using the `create cloud formation stack` operation.

sourceName -> (string)

The name of the export snapshot record, which contains the exported Lightsail instance snapshot that will be used as the source of the new Amazon EC2 instance.

Use the `get export snapshot records` operation to get a list of export snapshot records that you can use to create a CloudFormation stack.

instanceType -> (string)

The instance type (`t2.micro` ) to use for the new Amazon EC2 instance.

portInfoSource -> (string)

The port configuration to use for the new Amazon EC2 instance.

The following configuration options are available:

- `DEFAULT` - Use the default firewall settings from the Lightsail instance blueprint. If this is specified, then IPv4 and IPv6 will be configured for the new instance that is created in Amazon EC2.
- `INSTANCE` - Use the configured firewall settings from the source Lightsail instance. If this is specified, the new instance that is created in Amazon EC2 will be configured to match the configuration of the source Lightsail instance. For example, if the source instance is configured for dual-stack (IPv4 and IPv6), then IPv4 and IPv6 will be configured for the new instance that is created in Amazon EC2. If the source instance is configured for IPv4 only, then only IPv4 will be configured for the new instance that is created in Amazon EC2.
- `NONE` - Use the default Amazon EC2 security group. If this is specified, then only IPv4 will be configured for the new instance that is created in Amazon EC2.
- `CLOSED` - All ports closed. If this is specified, then only IPv4 will be configured for the new instance that is created in Amazon EC2.

### Note

If you configured `lightsail-connect` as a `cidrListAliases` on your instance, or if you chose to allow the Lightsail browser-based SSH or RDP clients to connect to your instance, that configuration is not carried over to your new Amazon EC2 instance.

userData -> (string)

A launch script you can create that configures a server with additional user data. For example, you might want to run `apt-get -y update` .

### Note

Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use `yum` , Debian and Ubuntu use `apt-get` , and FreeBSD uses `pkg` .

availabilityZone -> (string)

The Availability Zone for the new Amazon EC2 instance.

Shorthand Syntax:

```
sourceName=string,instanceType=string,portInfoSource=string,userData=string,availabilityZone=string ...
```

JSON Syntax:

```
[
  {
    "sourceName": "string",
    "instanceType": "string",
    "portInfoSource": "DEFAULT"|"INSTANCE"|"NONE"|"CLOSED",
    "userData": "string",
    "availabilityZone": "string"
  }
  ...
]
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

operations -> (list)

An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(structure)

Describes the API operation.

id -> (string)

The ID of the operation.

resourceName -> (string)

The resource name.

resourceType -> (string)

The resource type.

createdAt -> (timestamp)

The timestamp when the operation was initialized (`1479816991.349` ).

location -> (structure)

The Amazon Web Services Region and Availability Zone.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

isTerminal -> (boolean)

A Boolean value indicating whether the operation is terminal.

operationDetails -> (string)

Details about the operation (`Debian-1GB-Ohio-1` ).

operationType -> (string)

The type of operation.

status -> (string)

The status of the operation.

statusChangedAt -> (timestamp)

The timestamp when the status was changed (`1479816991.349` ).

errorCode -> (string)

The error code.

errorDetails -> (string)

The error details.