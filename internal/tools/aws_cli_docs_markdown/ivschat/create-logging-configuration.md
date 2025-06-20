# create-logging-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/create-logging-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/create-logging-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ivschat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/index.html#cli-aws-ivschat) ]

# create-logging-configuration

## Description

Creates a logging configuration that allows clients to store and record sent messages.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ivschat-2020-07-14/CreateLoggingConfiguration)

## Synopsis

```
create-logging-configuration
[--name <value>]
--destination-configuration <value>
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

Logging-configuration name. The value does not need to be unique.

`--destination-configuration` (tagged union structure)

A complex type that contains a destination configuration for where chat content will be logged. There can be only one type of destination (`cloudWatchLogs` , `firehose` , or `s3` ) in a `destinationConfiguration` .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`, `cloudWatchLogs`, `firehose`.

s3 -> (structure)

An Amazon S3 destination configuration where chat activity will be logged.

bucketName -> (string)

Name of the Amazon S3 bucket where chat activity will be logged.

cloudWatchLogs -> (structure)

An Amazon CloudWatch Logs destination configuration where chat activity will be logged.

logGroupName -> (string)

Name of the Amazon Cloudwatch Logs destination where chat activity will be logged.

firehose -> (structure)

An Amazon Kinesis Data Firehose destination configuration where chat activity will be logged.

deliveryStreamName -> (string)

Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.

Shorthand Syntax:

```
s3={bucketName=string},cloudWatchLogs={logGroupName=string},firehose={deliveryStreamName=string}
```

JSON Syntax:

```
{
  "s3": {
    "bucketName": "string"
  },
  "cloudWatchLogs": {
    "logGroupName": "string"
  },
  "firehose": {
    "deliveryStreamName": "string"
  }
}
```

`--tags` (map)

Tags to attach to the resource. Array of maps, each of the form `string:string (key:value)` . See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging Amazon Web Services Resources and Tag Editor* for details, including restrictions that apply to tags and âTag naming limits and requirementsâ; Amazon IVS Chat has no constraints on tags beyond what is documented there.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a chat LoggingConfiguration resource**

The following `create-logging-configuration` example creates a LoggingConfiguration resource that allows clients to store and record sent messages.

```
aws ivschat create-logging-configuration \
    --destination-configuration s3={bucketName=demo-logging-bucket} \
    --name "test-logging-config" \
    --tags "key1=value1, key2=value2"
```

Output:

```
{
    "arn": "arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ",
    "createTime": "2022-09-14T17:48:00.653000+00:00",
    "destinationConfiguration": {
        "s3": {
            "bucketName": "demo-logging-bucket"
        }
    },
    "id": "ABcdef34ghIJ",
    "name": "test-logging-config",
    "state": "ACTIVE",
    "tags": { "key1" : "value1", "key2" : "value2" },
    "updateTime": "2022-09-14T17:48:01.104000+00:00"
}
```

For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html) in the *Amazon Interactive Video Service User Guide*.

## Output

arn -> (string)

Logging-configuration ARN, assigned by the system.

id -> (string)

Logging-configuration ID, generated by the system. This is a relative identifier, the part of the ARN that uniquely identifies the logging configuration.

createTime -> (timestamp)

Time when the logging configuration was created. This is an ISO 8601 timestamp; *note that this is returned as a string* .

updateTime -> (timestamp)

Time of the logging configurationâs last update. This is an ISO 8601 timestamp; *note that this is returned as a string* .

name -> (string)

Logging-configuration name, from the request (if specified).

destinationConfiguration -> (tagged union structure)

A complex type that contains a destination configuration for where chat content will be logged, from the request. There is only one type of destination (`cloudWatchLogs` , `firehose` , or `s3` ) in a `destinationConfiguration` .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`, `cloudWatchLogs`, `firehose`.

s3 -> (structure)

An Amazon S3 destination configuration where chat activity will be logged.

bucketName -> (string)

Name of the Amazon S3 bucket where chat activity will be logged.

cloudWatchLogs -> (structure)

An Amazon CloudWatch Logs destination configuration where chat activity will be logged.

logGroupName -> (string)

Name of the Amazon Cloudwatch Logs destination where chat activity will be logged.

firehose -> (structure)

An Amazon Kinesis Data Firehose destination configuration where chat activity will be logged.

deliveryStreamName -> (string)

Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.

state -> (string)

The state of the logging configuration. When the state is `ACTIVE` , the configuration is ready to log chat content.

tags -> (map)

Tags attached to the resource, from the request (if specified). Array of maps, each of the form `string:string (key:value)` .

key -> (string)

value -> (string)