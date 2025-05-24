# delete-canaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-canary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-canary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [synthetics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/index.html#cli-aws-synthetics) ]

# delete-canary

## Description

Permanently deletes the specified canary.

If the canaryâs `ProvisionedResourceCleanup` field is set to `AUTOMATIC` or you specify `DeleteLambda` in this operation as `true` , CloudWatch Synthetics also deletes the Lambda functions and layers that are used by the canary.

Other resources used and created by the canary are not automatically deleted. After you delete a canary, you should also delete the following:

- The CloudWatch alarms created for this canary. These alarms have a name of [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-canary.html#id1)Synthetics-Alarm-*first-198-characters-of-canary-name* -*canaryId* -*alarm number* ``
- Amazon S3 objects and buckets, such as the canaryâs artifact location.
- IAM roles created for the canary. If they were created in the console, these roles have the name [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-canary.html#id3)role/service-role/CloudWatchSyntheticsRole-*First-21-Characters-of-CanaryName* ``
- CloudWatch Logs log groups created for the canary. These logs groups have the name [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-canary.html#id5)/aws/lambda/cwsyn-*First-21-Characters-of-CanaryName* ``

Before you delete a canary, you might want to use `GetCanary` to display the information about this canary. Make note of the information returned by this operation so that you can delete these resources after you delete the canary.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/synthetics-2017-10-11/DeleteCanary)

## Synopsis

```
delete-canary
--name <value>
[--delete-lambda | --no-delete-lambda]
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

The name of the canary that you want to delete. To find the names of your canaries, use [DescribeCanaries](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html) .

`--delete-lambda` | `--no-delete-lambda` (boolean)

Specifies whether to also delete the Lambda functions and layers used by this canary. The default is `false` .

Your setting for this parameter is used only if the canary doesnât have `AUTOMATIC` for its `ProvisionedResourceCleanup` field. If that field is set to `AUTOMATIC` , then the Lambda functions and layers will be deleted when this canary is deleted.

Type: Boolean

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

**To permanently delete a canary**

The following `delete-canary` example deletes a canary named `demo_canary`.

```
aws synthetics delete-canary \
    --name demo_canary
```

This command produces no output.

For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) in the *Amazon CloudWatch User Guide*.

## Output

None