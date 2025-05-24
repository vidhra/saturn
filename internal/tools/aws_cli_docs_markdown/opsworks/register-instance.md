# register-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# register-instance

## Description

Registers instances that were created outside of OpsWorks Stacks with a specified stack.

### Note

We do not recommend using this action to register instances. The complete registration operation includes two tasks: installing the OpsWorks Stacks agent on the instance, and registering the instance with the stack. `RegisterInstance` handles only the second step. You should instead use the CLI `register` command, which performs the entire registration operation. For more information, see [Registering an Instance with an OpsWorks Stacks Stack](https://docs.aws.amazon.com/opsworks/latest/userguide/registered-instances-register.html) .

Registered instances have the same requirements as instances that are created by using the  CreateInstance API. For example, registered instances must be running a supported Linux-based operating system, and they must have a supported instance type. For more information about requirements for instances that you want to register, see [Preparing the Instance](https://docs.aws.amazon.com/opsworks/latest/userguide/registered-instances-register-registering-preparer.html) .

**Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack or an attached policy that explicitly grants permissions. For more information on user permissions, see [Managing User Permissions](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/RegisterInstance)

## Synopsis

```
register-instance
--stack-id <value>
[--hostname <value>]
[--public-ip <value>]
[--private-ip <value>]
[--rsa-public-key <value>]
[--rsa-public-key-fingerprint <value>]
[--instance-identity <value>]
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

`--stack-id` (string)

The ID of the stack that the instance is to be registered with.

`--hostname` (string)

The instanceâs host name. The following are character limits for instance host names.

- Linux-based instances: 63 characters
- Windows-based instances: 15 characters

`--public-ip` (string)

The instanceâs public IP address.

`--private-ip` (string)

The instanceâs private IP address.

`--rsa-public-key` (string)

The instances public RSA key. This key is used to encrypt communication between the instance and the service.

`--rsa-public-key-fingerprint` (string)

The instances public RSA key fingerprint.

`--instance-identity` (structure)

An InstanceIdentity object that contains the instanceâs identity.

Document -> (string)

A JSON document that contains the metadata.

Signature -> (string)

A signature that can be used to verify the documentâs accuracy and authenticity.

Shorthand Syntax:

```
Document=string,Signature=string
```

JSON Syntax:

```
{
  "Document": "string",
  "Signature": "string"
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

## Output

InstanceId -> (string)

The registered instanceâs OpsWorks Stacks ID.