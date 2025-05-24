# modify-verified-access-instance-logging-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-verified-access-instance-logging-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-verified-access-instance-logging-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-verified-access-instance-logging-configuration

## Description

Modifies the logging configuration for the specified Amazon Web Services Verified Access instance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyVerifiedAccessInstanceLoggingConfiguration)

## Synopsis

```
modify-verified-access-instance-logging-configuration
--verified-access-instance-id <value>
--access-logs <value>
[--dry-run | --no-dry-run]
[--client-token <value>]
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

`--verified-access-instance-id` (string)

The ID of the Verified Access instance.

`--access-logs` (structure)

The configuration options for Verified Access instances.

S3 -> (structure)

Sends Verified Access logs to Amazon S3.

Enabled -> (boolean)

Indicates whether logging is enabled.

BucketName -> (string)

The bucket name.

Prefix -> (string)

The bucket prefix.

BucketOwner -> (string)

The ID of the Amazon Web Services account that owns the Amazon S3 bucket.

CloudWatchLogs -> (structure)

Sends Verified Access logs to CloudWatch Logs.

Enabled -> (boolean)

Indicates whether logging is enabled.

LogGroup -> (string)

The ID of the CloudWatch Logs log group.

KinesisDataFirehose -> (structure)

Sends Verified Access logs to Kinesis.

Enabled -> (boolean)

Indicates whether logging is enabled.

DeliveryStream -> (string)

The ID of the delivery stream.

LogVersion -> (string)

The logging version.

Valid values: `ocsf-0.1` | `ocsf-1.0.0-rc.2`

IncludeTrustContext -> (boolean)

Indicates whether to include trust data sent by trust providers in the logs.

Shorthand Syntax:

```
S3={Enabled=boolean,BucketName=string,Prefix=string,BucketOwner=string},CloudWatchLogs={Enabled=boolean,LogGroup=string},KinesisDataFirehose={Enabled=boolean,DeliveryStream=string},LogVersion=string,IncludeTrustContext=boolean
```

JSON Syntax:

```
{
  "S3": {
    "Enabled": true|false,
    "BucketName": "string",
    "Prefix": "string",
    "BucketOwner": "string"
  },
  "CloudWatchLogs": {
    "Enabled": true|false,
    "LogGroup": "string"
  },
  "KinesisDataFirehose": {
    "Enabled": true|false,
    "DeliveryStream": "string"
  },
  "LogVersion": "string",
  "IncludeTrustContext": true|false
}
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--client-token` (string)

A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) .

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

**To enable logging for a Verified Access instance**

The following `modify-verified-access-instance-logging-configuration` example enables access logging for the specified Verified Access instance. The logs will be delivered to the specified CloudWatch Logs log group.

```
aws ec2 modify-verified-access-instance-logging-configuration \
    --verified-access-instance-id vai-0ce000c0b7643abea \
    --access-logs CloudWatchLogs={Enabled=true,LogGroup=my-log-group}
```

Output:

```
{
    "LoggingConfiguration": {
        "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea",
        "AccessLogs": {
            "S3": {
                "Enabled": false
            },
            "CloudWatchLogs": {
                "Enabled": true,
                "DeliveryStatus": {
                    "Code": "success"
                },
                "LogGroup": "my-log-group"
            },
            "KinesisDataFirehose": {
                "Enabled": false
            },
            "LogVersion": "ocsf-1.0.0-rc.2",
            "IncludeTrustContext": false
        }
    }
}
```

For more information, see [Verified Access logs](https://docs.aws.amazon.com/verified-access/latest/ug/access-logs.html) in the *AWS Verified Access User Guide*.

## Output

LoggingConfiguration -> (structure)

The logging configuration for the Verified Access instance.

VerifiedAccessInstanceId -> (string)

The ID of the Amazon Web Services Verified Access instance.

AccessLogs -> (structure)

Details about the logging options.

S3 -> (structure)

Amazon S3 logging options.

Enabled -> (boolean)

Indicates whether logging is enabled.

DeliveryStatus -> (structure)

The delivery status.

Code -> (string)

The status code.

Message -> (string)

The status message.

BucketName -> (string)

The bucket name.

Prefix -> (string)

The bucket prefix.

BucketOwner -> (string)

The Amazon Web Services account number that owns the bucket.

CloudWatchLogs -> (structure)

CloudWatch Logs logging destination.

Enabled -> (boolean)

Indicates whether logging is enabled.

DeliveryStatus -> (structure)

The delivery status for access logs.

Code -> (string)

The status code.

Message -> (string)

The status message.

LogGroup -> (string)

The ID of the CloudWatch Logs log group.

KinesisDataFirehose -> (structure)

Kinesis logging destination.

Enabled -> (boolean)

Indicates whether logging is enabled.

DeliveryStatus -> (structure)

The delivery status.

Code -> (string)

The status code.

Message -> (string)

The status message.

DeliveryStream -> (string)

The ID of the delivery stream.

LogVersion -> (string)

The log version.

IncludeTrustContext -> (boolean)

Indicates whether trust data is included in the logs.