# batch-disable-standardsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-disable-standards.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-disable-standards.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securityhub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html#cli-aws-securityhub) ]

# batch-disable-standards

## Description

Disables the standards specified by the provided `StandardsSubscriptionArns` .

For more information, see [Security Standards](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html) section of the *Security Hub User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/BatchDisableStandards)

## Synopsis

```
batch-disable-standards
--standards-subscription-arns <value>
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

`--standards-subscription-arns` (list)

The ARNs of the standards subscriptions to disable.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To disable a standard**

The following `batch-disable-standards` example disables the standard associated with the specified subscription ARN.

```
aws securityhub batch-disable-standards \
    --standards-subscription-arns "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1"
```

Output:

```
{
    "StandardsSubscriptions": [
        {
            "StandardsArn": "arn:aws:securityhub:eu-central-1::standards/pci-dss/v/3.2.1",
            "StandardsInput": { },
            "StandardsStatus": "DELETING",
            "StandardsSubscriptionArn": "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1"
        }
    ]
}
```

For more information, see [Disabling or enabling a security standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html) in the *AWS Security Hub User Guide*.

## Output

StandardsSubscriptions -> (list)

The details of the standards subscriptions that were disabled.

(structure)

A resource that represents your subscription to a supported standard.

StandardsSubscriptionArn -> (string)

The ARN of the resource that represents your subscription to the standard.

StandardsArn -> (string)

The ARN of the standard.

StandardsInput -> (map)

A key-value pair of input for the standard.

key -> (string)

value -> (string)

StandardsStatus -> (string)

The status of your subscription to the standard. Possible values are:

- `PENDING` - The standard is in the process of being enabled. Or the standard is already enabled and Security Hub is adding new controls to the standard.
- `READY` - The standard is enabled.
- `INCOMPLETE` - The standard could not be enabled completely. One or more errors (`StandardsStatusReason` ) occurred when Security Hub attempted to enable the standard.
- `DELETING` - The standard is in the process of being disabled.
- `FAILED` - The standard could not be disabled. One or more errors (`StandardsStatusReason` ) occurred when Security Hub attempted to disable the standard.

StandardsControlsUpdatable -> (string)

Specifies whether you can retrieve information about and configure individual controls that apply to the standard. Possible values are:

- `READY_FOR_UPDATES` - Controls in the standard can be retrieved and configured.
- `NOT_READY_FOR_UPDATES` - Controls in the standard cannot be retrieved or configured.

StandardsStatusReason -> (structure)

The reason for the current status.

StatusReasonCode -> (string)

The reason code that represents the reason for the current status of a standard subscription.