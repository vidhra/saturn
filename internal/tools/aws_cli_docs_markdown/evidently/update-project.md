# update-projectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/update-project.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/update-project.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [evidently](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/index.html#cli-aws-evidently) ]

# update-project

## Description

Updates the description of an existing project.

To create a new project, use [CreateProject](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateProject.html) .

Donât use this operation to update the data storage options of a project. Instead, use [UpdateProjectDataDelivery](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateProjectDataDelivery.html) .

Donât use this operation to update the tags of a project. Instead, use [TagResource](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_TagResource.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/evidently-2021-02-01/UpdateProject)

## Synopsis

```
update-project
[--app-config-resource <value>]
[--description <value>]
--project <value>
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

`--app-config-resource` (structure)

Use this parameter if the project will use client-side evaluation powered by AppConfig. Client-side evaluation allows your application to assign variations to user sessions locally instead of by calling the [EvaluateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html) operation. This mitigates the latency and availability risks that come with an API call. allows you to

This parameter is a structure that contains information about the AppConfig application that will be used for client-side evaluation.

applicationId -> (string)

The ID of the AppConfig application to use for client-side evaluation.

environmentId -> (string)

The ID of the AppConfig environment to use for client-side evaluation. This must be an environment that is within the application that you specify for `applicationId` .

Shorthand Syntax:

```
applicationId=string,environmentId=string
```

JSON Syntax:

```
{
  "applicationId": "string",
  "environmentId": "string"
}
```

`--description` (string)

An optional description of the project.

`--project` (string)

The name or ARN of the project to update.

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

project -> (structure)

A structure containing information about the updated project.

activeExperimentCount -> (long)

The number of ongoing experiments currently in the project.

activeLaunchCount -> (long)

The number of ongoing launches currently in the project.

appConfigResource -> (structure)

This structure defines the configuration of how your application integrates with AppConfig to run client-side evaluation.

applicationId -> (string)

The ID of the AppConfig application to use for client-side evaluation.

configurationProfileId -> (string)

The ID of the AppConfig profile to use for client-side evaluation.

environmentId -> (string)

The ID of the AppConfig environment to use for client-side evaluation. This must be an environment that is within the application that you specify for `applicationId` .

arn -> (string)

The name or ARN of the project.

createdTime -> (timestamp)

The date and time that the project is created.

dataDelivery -> (structure)

A structure that contains information about where Evidently is to store evaluation events for longer term storage.

cloudWatchLogs -> (structure)

If the project stores evaluation events in CloudWatch Logs, this structure stores the log group name.

logGroup -> (string)

The name of the log group where the project stores evaluation events.

s3Destination -> (structure)

If the project stores evaluation events in an Amazon S3 bucket, this structure stores the bucket name and bucket prefix.

bucket -> (string)

The name of the bucket in which Evidently stores evaluation events.

prefix -> (string)

The bucket prefix in which Evidently stores evaluation events.

description -> (string)

The user-entered description of the project.

experimentCount -> (long)

The number of experiments currently in the project. This includes all experiments that have been created and not deleted, whether they are ongoing or not.

featureCount -> (long)

The number of features currently in the project.

lastUpdatedTime -> (timestamp)

The date and time that the project was most recently updated.

launchCount -> (long)

The number of launches currently in the project. This includes all launches that have been created and not deleted, whether they are ongoing or not.

name -> (string)

The name of the project.

status -> (string)

The current state of the project.

tags -> (map)

The list of tag keys and values associated with this project.

key -> (string)

value -> (string)