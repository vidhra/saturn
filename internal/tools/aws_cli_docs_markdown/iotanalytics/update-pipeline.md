# update-pipelineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-pipeline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-pipeline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotanalytics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/index.html#cli-aws-iotanalytics) ]

# update-pipeline

## Description

Updates the settings of a pipeline. You must specify both a `channel` and a `datastore` activity and, optionally, as many as 23 additional activities in the `pipelineActivities` array.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/UpdatePipeline)

## Synopsis

```
update-pipeline
--pipeline-name <value>
--pipeline-activities <value>
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

`--pipeline-name` (string)

The name of the pipeline to update.

`--pipeline-activities` (list)

A list of `PipelineActivity` objects. Activities perform transformations on your messages, such as removing, renaming or adding message attributes; filtering messages based on attribute values; invoking your Lambda functions on messages for advanced processing; or performing mathematical transformations to normalize device data.

The list can be 2-25 `PipelineActivity` objects and must contain both a `channel` and a `datastore` activity. Each entry in the list must contain only one activity. For example:

`pipelineActivities = [ { "channel": { ... } }, { "lambda": { ... } }, ... ]`

(structure)

An activity that performs a transformation on a message.

channel -> (structure)

Determines the source of the messages to be processed.

name -> (string)

The name of the channel activity.

channelName -> (string)

The name of the channel from which the messages are processed.

next -> (string)

The next activity in the pipeline.

lambda -> (structure)

Runs a Lambda function to modify the message.

name -> (string)

The name of the lambda activity.

lambdaName -> (string)

The name of the Lambda function that is run on the message.

batchSize -> (integer)

The number of messages passed to the Lambda function for processing.

The Lambda function must be able to process all of these messages within five minutes, which is the maximum timeout duration for Lambda functions.

next -> (string)

The next activity in the pipeline.

datastore -> (structure)

Specifies where to store the processed message data.

name -> (string)

The name of the datastore activity.

datastoreName -> (string)

The name of the data store where processed messages are stored.

addAttributes -> (structure)

Adds other attributes based on existing attributes in the message.

name -> (string)

The name of the addAttributes activity.

attributes -> (map)

A list of 1-50 `AttributeNameMapping` objects that map an existing attribute to a new attribute.

### Note

The existing attributes remain in the message, so if you want to remove the originals, use `RemoveAttributeActivity` .

key -> (string)

value -> (string)

next -> (string)

The next activity in the pipeline.

removeAttributes -> (structure)

Removes attributes from a message.

name -> (string)

The name of the `removeAttributes` activity.

attributes -> (list)

A list of 1-50 attributes to remove from the message.

(string)

next -> (string)

The next activity in the pipeline.

selectAttributes -> (structure)

Used to create a new message using only the specified attributes from the original message.

name -> (string)

The name of the `selectAttributes` activity.

attributes -> (list)

A list of the attributes to select from the message.

(string)

next -> (string)

The next activity in the pipeline.

filter -> (structure)

Filters a message based on its attributes.

name -> (string)

The name of the filter activity.

filter -> (string)

An expression that looks like a SQL WHERE clause that must return a Boolean value. Messages that satisfy the condition are passed to the next activity.

next -> (string)

The next activity in the pipeline.

math -> (structure)

Computes an arithmetic expression using the messageâs attributes and adds it to the message.

name -> (string)

The name of the math activity.

attribute -> (string)

The name of the attribute that contains the result of the math operation.

math -> (string)

An expression that uses one or more existing attributes and must return an integer value.

next -> (string)

The next activity in the pipeline.

deviceRegistryEnrich -> (structure)

Adds data from the IoT device registry to your message.

name -> (string)

The name of the `deviceRegistryEnrich` activity.

attribute -> (string)

The name of the attribute that is added to the message.

thingName -> (string)

The name of the IoT device whose registry information is added to the message.

roleArn -> (string)

The ARN of the role that allows access to the deviceâs registry information.

next -> (string)

The next activity in the pipeline.

deviceShadowEnrich -> (structure)

Adds information from the IoT Device Shadow service to a message.

name -> (string)

The name of the `deviceShadowEnrich` activity.

attribute -> (string)

The name of the attribute that is added to the message.

thingName -> (string)

The name of the IoT device whose shadow information is added to the message.

roleArn -> (string)

The ARN of the role that allows access to the deviceâs shadow.

next -> (string)

The next activity in the pipeline.

Shorthand Syntax:

```
channel={name=string,channelName=string,next=string},lambda={name=string,lambdaName=string,batchSize=integer,next=string},datastore={name=string,datastoreName=string},addAttributes={name=string,attributes={KeyName1=string,KeyName2=string},next=string},removeAttributes={name=string,attributes=[string,string],next=string},selectAttributes={name=string,attributes=[string,string],next=string},filter={name=string,filter=string,next=string},math={name=string,attribute=string,math=string,next=string},deviceRegistryEnrich={name=string,attribute=string,thingName=string,roleArn=string,next=string},deviceShadowEnrich={name=string,attribute=string,thingName=string,roleArn=string,next=string} ...
```

JSON Syntax:

```
[
  {
    "channel": {
      "name": "string",
      "channelName": "string",
      "next": "string"
    },
    "lambda": {
      "name": "string",
      "lambdaName": "string",
      "batchSize": integer,
      "next": "string"
    },
    "datastore": {
      "name": "string",
      "datastoreName": "string"
    },
    "addAttributes": {
      "name": "string",
      "attributes": {"string": "string"
        ...},
      "next": "string"
    },
    "removeAttributes": {
      "name": "string",
      "attributes": ["string", ...],
      "next": "string"
    },
    "selectAttributes": {
      "name": "string",
      "attributes": ["string", ...],
      "next": "string"
    },
    "filter": {
      "name": "string",
      "filter": "string",
      "next": "string"
    },
    "math": {
      "name": "string",
      "attribute": "string",
      "math": "string",
      "next": "string"
    },
    "deviceRegistryEnrich": {
      "name": "string",
      "attribute": "string",
      "thingName": "string",
      "roleArn": "string",
      "next": "string"
    },
    "deviceShadowEnrich": {
      "name": "string",
      "attribute": "string",
      "thingName": "string",
      "roleArn": "string",
      "next": "string"
    }
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

**To update a pipeline**

The following `update-pipeline` example modifies the settings of the specified pipeline. You must specify both a channel and a data store activity and, optionally, as many as 23 additional activities, in the `pipelineActivities` array.

```
aws iotanalytics update-pipeline \
    --cli-input-json file://update-pipeline.json
```

Contents of update-pipeline.json:

```
{
    "pipelineName": "mypipeline",
    "pipelineActivities": [
        {
            "channel": {
                "name": "myChannelActivity",
                "channelName": "mychannel",
                "next": "myMathActivity"
            }
        },
        {
            "datastore": {
                "name": "myDatastoreActivity",
                "datastoreName": "mydatastore"
            }
        },
        {
            "math": {
                "name": "myMathActivity",
                "math": "(((temp - 32) * 5.0) / 9.0) + 273.15",
                "attribute": "tempK",
                "next": "myDatastoreActivity"
            }
        }
    ]
}
```

This command produces no output.

For more information, see [UpdatePipeline](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_UpdatePipeline.html) in the *AWS IoT Analytics API Reference*.

## Output

None