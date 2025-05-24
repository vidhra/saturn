# update-logging-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-logging-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-logging-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [network-firewall](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/index.html#cli-aws-network-firewall) ]

# update-logging-configuration

## Description

Sets the logging configuration for the specified firewall.

To change the logging configuration, retrieve the  LoggingConfiguration by calling  DescribeLoggingConfiguration , then change it and provide the modified object to this update call. You must change the logging configuration one  LogDestinationConfig at a time inside the retrieved  LoggingConfiguration object.

You can perform only one of the following actions in any call to `UpdateLoggingConfiguration` :

- Create a new log destination object by adding a single `LogDestinationConfig` array element to `LogDestinationConfigs` .
- Delete a log destination object by removing a single `LogDestinationConfig` array element from `LogDestinationConfigs` .
- Change the `LogDestination` setting in a single `LogDestinationConfig` array element.

You canât change the `LogDestinationType` or `LogType` in a `LogDestinationConfig` . To change these settings, delete the existing `LogDestinationConfig` object and create a new one, using two separate calls to this update operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/network-firewall-2020-11-12/UpdateLoggingConfiguration)

## Synopsis

```
update-logging-configuration
[--firewall-arn <value>]
[--firewall-name <value>]
[--logging-configuration <value>]
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

`--firewall-arn` (string)

The Amazon Resource Name (ARN) of the firewall.

You must specify the ARN or the name, and you can specify both.

`--firewall-name` (string)

The descriptive name of the firewall. You canât change the name of a firewall after you create it.

You must specify the ARN or the name, and you can specify both.

`--logging-configuration` (structure)

Defines how Network Firewall performs logging for a firewall. If you omit this setting, Network Firewall disables logging for the firewall.

LogDestinationConfigs -> (list)

Defines the logging destinations for the logs for a firewall. Network Firewall generates logs for stateful rule groups.

(structure)

Defines where Network Firewall sends logs for the firewall for one log type. This is used in  LoggingConfiguration . You can send each type of log to an Amazon S3 bucket, a CloudWatch log group, or a Firehose delivery stream.

Network Firewall generates logs for stateful rule groups. You can save alert, flow, and TLS log types.

LogType -> (string)

The type of log to record. You can record the following types of logs from your Network Firewall stateful engine.

- `ALERT` - Logs for traffic that matches your stateful rules and that have an action that sends an alert. A stateful rule sends alerts for the rule actions DROP, ALERT, and REJECT. For more information, see  StatefulRule .
- `FLOW` - Standard network traffic flow logs. The stateful rules engine records flow logs for all network traffic that it receives. Each flow log record captures the network flow for a specific standard stateless rule group.
- `TLS` - Logs for events that are related to TLS inspection. For more information, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-configurations.html) in the *Network Firewall Developer Guide* .

LogDestinationType -> (string)

The type of storage destination to send these logs to. You can send logs to an Amazon S3 bucket, a CloudWatch log group, or a Firehose delivery stream.

LogDestination -> (map)

The named location for the logs, provided in a key:value mapping that is specific to the chosen destination type.

- For an Amazon S3 bucket, provide the name of the bucket, with key `bucketName` , and optionally provide a prefix, with key `prefix` .  The following example specifies an Amazon S3 bucket named `DOC-EXAMPLE-BUCKET` and the prefix `alerts` :   `"LogDestination": { "bucketName": "DOC-EXAMPLE-BUCKET", "prefix": "alerts" }`
- For a CloudWatch log group, provide the name of the CloudWatch log group, with key `logGroup` . The following example specifies a log group named `alert-log-group` :   `"LogDestination": { "logGroup": "alert-log-group" }`
- For a Firehose delivery stream, provide the name of the delivery stream, with key `deliveryStream` . The following example specifies a delivery stream named `alert-delivery-stream` :   `"LogDestination": { "deliveryStream": "alert-delivery-stream" }`

key -> (string)

value -> (string)

Shorthand Syntax:

```
LogDestinationConfigs=[{LogType=string,LogDestinationType=string,LogDestination={KeyName1=string,KeyName2=string}},{LogType=string,LogDestinationType=string,LogDestination={KeyName1=string,KeyName2=string}}]
```

JSON Syntax:

```
{
  "LogDestinationConfigs": [
    {
      "LogType": "ALERT"|"FLOW"|"TLS",
      "LogDestinationType": "S3"|"CloudWatchLogs"|"KinesisDataFirehose",
      "LogDestination": {"string": "string"
        ...}
    }
    ...
  ]
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

FirewallArn -> (string)

The Amazon Resource Name (ARN) of the firewall.

FirewallName -> (string)

The descriptive name of the firewall. You canât change the name of a firewall after you create it.

LoggingConfiguration -> (structure)

Defines how Network Firewall performs logging for a  Firewall .

LogDestinationConfigs -> (list)

Defines the logging destinations for the logs for a firewall. Network Firewall generates logs for stateful rule groups.

(structure)

Defines where Network Firewall sends logs for the firewall for one log type. This is used in  LoggingConfiguration . You can send each type of log to an Amazon S3 bucket, a CloudWatch log group, or a Firehose delivery stream.

Network Firewall generates logs for stateful rule groups. You can save alert, flow, and TLS log types.

LogType -> (string)

The type of log to record. You can record the following types of logs from your Network Firewall stateful engine.

- `ALERT` - Logs for traffic that matches your stateful rules and that have an action that sends an alert. A stateful rule sends alerts for the rule actions DROP, ALERT, and REJECT. For more information, see  StatefulRule .
- `FLOW` - Standard network traffic flow logs. The stateful rules engine records flow logs for all network traffic that it receives. Each flow log record captures the network flow for a specific standard stateless rule group.
- `TLS` - Logs for events that are related to TLS inspection. For more information, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-configurations.html) in the *Network Firewall Developer Guide* .

LogDestinationType -> (string)

The type of storage destination to send these logs to. You can send logs to an Amazon S3 bucket, a CloudWatch log group, or a Firehose delivery stream.

LogDestination -> (map)

The named location for the logs, provided in a key:value mapping that is specific to the chosen destination type.

- For an Amazon S3 bucket, provide the name of the bucket, with key `bucketName` , and optionally provide a prefix, with key `prefix` .  The following example specifies an Amazon S3 bucket named `DOC-EXAMPLE-BUCKET` and the prefix `alerts` :   `"LogDestination": { "bucketName": "DOC-EXAMPLE-BUCKET", "prefix": "alerts" }`
- For a CloudWatch log group, provide the name of the CloudWatch log group, with key `logGroup` . The following example specifies a log group named `alert-log-group` :   `"LogDestination": { "logGroup": "alert-log-group" }`
- For a Firehose delivery stream, provide the name of the delivery stream, with key `deliveryStream` . The following example specifies a delivery stream named `alert-delivery-stream` :   `"LogDestination": { "deliveryStream": "alert-delivery-stream" }`

key -> (string)

value -> (string)