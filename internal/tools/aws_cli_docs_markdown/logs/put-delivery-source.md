# put-delivery-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-delivery-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-delivery-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# put-delivery-source

## Description

Creates or updates a logical *delivery source* . A delivery source represents an Amazon Web Services resource that sends logs to an logs delivery destination. The destination can be CloudWatch Logs, Amazon S3, or Firehose.

To configure logs delivery between a delivery destination and an Amazon Web Services service that is supported as a delivery source, you must do the following:

- Use `PutDeliverySource` to create a delivery source, which is a logical object that represents the resource that is actually sending the logs.
- Use `PutDeliveryDestination` to create a *delivery destination* , which is a logical object that represents the actual delivery destination. For more information, see [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html) .
- If you are delivering logs cross-account, you must use [PutDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html) in the destination account to assign an IAM policy to the destination. This policy allows delivery to that destination.
- Use `CreateDelivery` to create a *delivery* by pairing exactly one delivery source and one delivery destination. For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) .

You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.

Only some Amazon Web Services services support being configured as a delivery source. These services are listed as **Supported [V2 Permissions]** in the table at [Enabling logging from Amazon Web Services services.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html)

If you use this operation to update an existing delivery source, all the current delivery source parameters are overwritten with the new parameter values that you specify.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/PutDeliverySource)

## Synopsis

```
put-delivery-source
--name <value>
--resource-arn <value>
--log-type <value>
[--tags <value>]
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

A name for this delivery source. This name must be unique for all delivery sources in your account.

`--resource-arn` (string)

The ARN of the Amazon Web Services resource that is generating and sending logs. For example, `arn:aws:workmail:us-east-1:123456789012:organization/m-1234EXAMPLEabcd1234abcd1234abcd1234`

`--log-type` (string)

Defines the type of log that the source is sending.

- For Amazon Bedrock, the valid value is `APPLICATION_LOGS` .
- For CloudFront, the valid value is `ACCESS_LOGS` .
- For Amazon CodeWhisperer, the valid value is `EVENT_LOGS` .
- For Elemental MediaPackage, the valid values are `EGRESS_ACCESS_LOGS` and `INGRESS_ACCESS_LOGS` .
- For Elemental MediaTailor, the valid values are `AD_DECISION_SERVER_LOGS` , `MANIFEST_SERVICE_LOGS` , and `TRANSCODE_LOGS` .
- For IAM Identity Center, the valid value is `ERROR_LOGS` .
- For Amazon Q, the valid value is `EVENT_LOGS` .
- For Amazon SES mail manager, the valid value is `APPLICATION_LOG` .
- For Amazon WorkMail, the valid values are `ACCESS_CONTROL_LOGS` , `AUTHENTICATION_LOGS` , `WORKMAIL_AVAILABILITY_PROVIDER_LOGS` , `WORKMAIL_MAILBOX_ACCESS_LOGS` , and `WORKMAIL_PERSONAL_ACCESS_TOKEN_LOGS` .

`--tags` (map)

An optional list of key-value pairs to associate with the resource.

For more information about tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

deliverySource -> (structure)

A structure containing information about the delivery source that was just created or updated.

name -> (string)

The unique name of the delivery source.

arn -> (string)

The Amazon Resource Name (ARN) that uniquely identifies this delivery source.

resourceArns -> (list)

This array contains the ARN of the Amazon Web Services resource that sends logs and is represented by this delivery source. Currently, only one ARN can be in the array.

(string)

service -> (string)

The Amazon Web Services service that is sending logs.

logType -> (string)

The type of log that the source is sending. For valid values for this parameter, see the documentation for the source service.

tags -> (map)

The tags that have been assigned to this delivery source.

key -> (string)

value -> (string)