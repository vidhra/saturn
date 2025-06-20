# describe-stack-summaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-stack-summary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-stack-summary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# describe-stack-summary

## Description

Describes the number of layers and apps in a specified stack, and the number of instances in each state, such as `running_setup` or `online` .

**Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information about user permissions, see [Managing User Permissions](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStackSummary)

## Synopsis

```
describe-stack-summary
--stack-id <value>
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

The stack ID.

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

**To describe a stackâs configuration**

The following `describe-stack-summary` command returns a summary of the specified stackâs configuration.

```
aws opsworks --region us-east-1 describe-stack-summary --stack-id 8c428b08-a1a1-46ce-a5f8-feddc43771b8
```

*Output*:

```
{
  "StackSummary": {
    "StackId": "8c428b08-a1a1-46ce-a5f8-feddc43771b8",
    "InstancesCount": {
      "Booting": 1
    },
    "Name": "CLITest",
    "AppsCount": 1,
    "LayersCount": 1,
    "Arn": "arn:aws:opsworks:us-west-2:123456789012:stack/8c428b08-a1a1-46ce-a5f8-feddc43771b8/"
  }
}
```

**More Information**

For more information, see [Stacks](http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks.html) in the *AWS OpsWorks User Guide*.

## Output

StackSummary -> (structure)

A `StackSummary` object that contains the results.

StackId -> (string)

The stack ID.

Name -> (string)

The stack name.

Arn -> (string)

The stackâs ARN.

LayersCount -> (integer)

The number of layers.

AppsCount -> (integer)

The number of apps.

InstancesCount -> (structure)

An `InstancesCount` object with the number of instances in each status.

Assigning -> (integer)

The number of instances in the Assigning state.

Booting -> (integer)

The number of instances with `booting` status.

ConnectionLost -> (integer)

The number of instances with `connection_lost` status.

Deregistering -> (integer)

The number of instances in the Deregistering state.

Online -> (integer)

The number of instances with `online` status.

Pending -> (integer)

The number of instances with `pending` status.

Rebooting -> (integer)

The number of instances with `rebooting` status.

Registered -> (integer)

The number of instances in the Registered state.

Registering -> (integer)

The number of instances in the Registering state.

Requested -> (integer)

The number of instances with `requested` status.

RunningSetup -> (integer)

The number of instances with `running_setup` status.

SetupFailed -> (integer)

The number of instances with `setup_failed` status.

ShuttingDown -> (integer)

The number of instances with `shutting_down` status.

StartFailed -> (integer)

The number of instances with `start_failed` status.

StopFailed -> (integer)

The number of instances with `stop_failed` status.

Stopped -> (integer)

The number of instances with `stopped` status.

Stopping -> (integer)

The number of instances with `stopping` status.

Terminated -> (integer)

The number of instances with `terminated` status.

Terminating -> (integer)

The number of instances with `terminating` status.

Unassigning -> (integer)

The number of instances in the Unassigning state.