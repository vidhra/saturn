# create-channelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-channel.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-channel.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotanalytics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/index.html#cli-aws-iotanalytics) ]

# create-channel

## Description

Used to create a channel. A channel collects data from an MQTT topic and archives the raw, unprocessed messages before publishing the data to a pipeline.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreateChannel)

## Synopsis

```
create-channel
--channel-name <value>
[--channel-storage <value>]
[--retention-period <value>]
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

`--channel-name` (string)

The name of the channel.

`--channel-storage` (structure)

Where channel data is stored. You can choose one of `serviceManagedS3` or `customerManagedS3` storage. If not specified, the default is `serviceManagedS3` . You canât change this storage option after the channel is created.

serviceManagedS3 -> (structure)

Used to store channel data in an S3 bucket managed by IoT Analytics. You canât change the choice of S3 storage after the data store is created.

customerManagedS3 -> (structure)

Used to store channel data in an S3 bucket that you manage. If customer managed storage is selected, the `retentionPeriod` parameter is ignored. You canât change the choice of S3 storage after the data store is created.

bucket -> (string)

The name of the S3 bucket in which channel data is stored.

keyPrefix -> (string)

(Optional) The prefix used to create the keys of the channel data objects. Each object in an S3 bucket has a key that is its unique identifier in the bucket. Each object in a bucket has exactly one key. The prefix must end with a forward slash (/).

roleArn -> (string)

The ARN of the role that grants IoT Analytics permission to interact with your Amazon S3 resources.

Shorthand Syntax:

```
serviceManagedS3={},customerManagedS3={bucket=string,keyPrefix=string,roleArn=string}
```

JSON Syntax:

```
{
  "serviceManagedS3": {

  },
  "customerManagedS3": {
    "bucket": "string",
    "keyPrefix": "string",
    "roleArn": "string"
  }
}
```

`--retention-period` (structure)

How long, in days, message data is kept for the channel. When `customerManagedS3` storage is selected, this parameter is ignored.

unlimited -> (boolean)

If true, message data is kept indefinitely.

numberOfDays -> (integer)

The number of days that message data is kept. The `unlimited` parameter must be false.

Shorthand Syntax:

```
unlimited=boolean,numberOfDays=integer
```

JSON Syntax:

```
{
  "unlimited": true|false,
  "numberOfDays": integer
}
```

`--tags` (list)

Metadata which can be used to manage the channel.

(structure)

A set of key-value pairs that are used to manage the resource.

key -> (string)

The tagâs key.

value -> (string)

The tagâs value.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a channel**

The following `create-channel` example creates a channel with the specified configuration. A channel collects data from an MQTT topic and archives the raw, unprocessed messages before publishing the data to a pipeline.

```
aws iotanalytics create-channel \
    --cli-input-json file://create-channel.json
```

Contents of `create-channel.json`:

```
{
    "channelName": "mychannel",
    "retentionPeriod": {
        "unlimited": true
    },
    "tags": [
        {
            "key": "Environment",
            "value": "Production"
        }
    ]
}
```

Output:

```
{
    "channelArn": "arn:aws:iotanalytics:us-west-2:123456789012:channel/mychannel",
    "channelName": "mychannel",
    "retentionPeriod": {
        "unlimited": true
    }
}
```

For more information, see [CreateChannel](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_CreateChannel.html) in the *AWS IoT Analytics API Reference*.

## Output

channelName -> (string)

The name of the channel.

channelArn -> (string)

The ARN of the channel.

retentionPeriod -> (structure)

How long, in days, message data is kept for the channel.

unlimited -> (boolean)

If true, message data is kept indefinitely.

numberOfDays -> (integer)

The number of days that message data is kept. The `unlimited` parameter must be false.