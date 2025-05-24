# get-log-delivery-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-log-delivery-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-log-delivery-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# get-log-delivery-configuration

## Description

Given a user pool ID, returns the logging configuration. User pools can export message-delivery error and threat-protection activity logs to external Amazon Web Services services. For more information, see [Exporting user pool logs](https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html) .

### Note

Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.

**Learn more**

- [Signing Amazon Web Services API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
- [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/GetLogDeliveryConfiguration)

## Synopsis

```
get-log-delivery-configuration
--user-pool-id <value>
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

`--user-pool-id` (string)

The ID of the user pool that has the logging configuration that you want to view.

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

**To display the log delivery configuration**

The following `get-log-delivery-configuration` example displays the log export settings of the requested user pool.

```
aws cognito-idp get-log-delivery-configuration \
    --user-pool-id us-west-2_EXAMPLE
```

Output:

```
{
    "LogDeliveryConfiguration": {
        "UserPoolId": "us-west-2_EXAMPLE",
        "LogConfigurations": [
            {
                "LogLevel": "INFO",
                "EventSource": "userAuthEvents",
                "FirehoseConfiguration": {
                    "StreamArn": "arn:aws:firehose:us-west-2:123456789012:deliverystream/my-test-deliverystream"
                }
            },
            {
                "LogLevel": "ERROR",
                "EventSource": "userNotification",
                "CloudWatchLogsConfiguration": {
                    "LogGroupArn": "arn:aws:logs:us-west-2:123456789012:log-group:my-message-delivery-logs"
                }
            }
        ]
    }
}
```

For more information, see [Exporting user pool logs](https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html) in the *Amazon Cognito Developer Guide*.

## Output

LogDeliveryConfiguration -> (structure)

The logging configuration of the requested user pool. Includes types of logs configured and their destinations.

UserPoolId -> (string)

The ID of the user pool where you configured logging.

LogConfigurations -> (list)

A logging destination of a user pool. User pools can have multiple logging destinations for message-delivery and user-activity logs.

(structure)

The configuration of user event logs to an external Amazon Web Services service like Amazon Data Firehose, Amazon S3, or Amazon CloudWatch Logs.

LogLevel -> (string)

The `errorlevel` selection of logs that a user pool sends for detailed activity logging. To send `userNotification` activity with [information about message delivery](https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html) , choose `ERROR` with `CloudWatchLogsConfiguration` . To send `userAuthEvents` activity with user logs from threat protection with the Plus feature plan, choose `INFO` with one of `CloudWatchLogsConfiguration` , `FirehoseConfiguration` , or `S3Configuration` .

EventSource -> (string)

The source of events that your user pool sends for logging. To send error-level logs about user notification activity, set to `userNotification` . To send info-level logs about threat-protection user activity in user pools with the Plus feature plan, set to `userAuthEvents` .

CloudWatchLogsConfiguration -> (structure)

The CloudWatch log group destination of user pool detailed activity logs, or of user activity log export with threat protection.

LogGroupArn -> (string)

The Amazon Resource Name (arn) of a CloudWatch Logs log group where your user pool sends logs. The log group must not be encrypted with Key Management Service and must be in the same Amazon Web Services account as your user pool.

To send logs to log groups with a resource policy of a size greater than 5120 characters, configure a log group with a path that starts with `/aws/vendedlogs` . For more information, see [Enabling logging from certain Amazon Web Services services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) .

S3Configuration -> (structure)

The Amazon S3 bucket destination of user activity log export with threat protection. To activate this setting, your user pool must be on the [Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html) .

BucketArn -> (string)

The ARN of an Amazon S3 bucket thatâs the destination for threat protection log export.

FirehoseConfiguration -> (structure)

The Amazon Data Firehose stream destination of user activity log export with threat protection. To activate this setting, your user pool must be on the [Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html) .

StreamArn -> (string)

The ARN of an Amazon Data Firehose stream thatâs the destination for threat protection log export.