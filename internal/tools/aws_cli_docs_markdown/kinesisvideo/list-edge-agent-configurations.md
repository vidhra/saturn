# list-edge-agent-configurationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/list-edge-agent-configurations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/list-edge-agent-configurations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesisvideo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/index.html#cli-aws-kinesisvideo) ]

# list-edge-agent-configurations

## Description

Returns an array of edge configurations associated with the specified Edge Agent.

In the request, you must specify the Edge Agent `HubDeviceArn` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesisvideo-2017-09-30/ListEdgeAgentConfigurations)

`list-edge-agent-configurations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `EdgeConfigs`

## Synopsis

```
list-edge-agent-configurations
--hub-device-arn <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--hub-device-arn` (string)

The âInternet of Things (IoT) Thingâ Arn of the edge agent.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

EdgeConfigs -> (list)

A description of a single streamâs edge configuration.

(structure)

A description of a single streamâs edge configuration.

StreamName -> (string)

The name of the stream.

StreamARN -> (string)

The Amazon Resource Name (ARN) of the stream.

CreationTime -> (timestamp)

The timestamp when the stream first created the edge config.

LastUpdatedTime -> (timestamp)

The timestamp when the stream last updated the edge config.

SyncStatus -> (string)

The current sync status of the streamâs edge configuration.

FailedStatusDetails -> (string)

A description of the generated failure status.

EdgeConfig -> (structure)

A description of the streamâs edge configuration that will be used to sync with the Edge Agent IoT Greengrass component. The Edge Agent component will run on an IoT Hub Device setup at your premise.

HubDeviceArn -> (string)

The â**Internet of Things (IoT) Thing** â Arn of the stream.

RecorderConfig -> (structure)

The recorder configuration consists of the local `MediaSourceConfig` details, that are used as credentials to access the local media files streamed on the camera.

MediaSourceConfig -> (structure)

The configuration details that consist of the credentials required (`MediaUriSecretArn` and `MediaUriType` ) to access the media files streamed to the camera.

MediaUriSecretArn -> (string)

The Amazon Web Services Secrets Manager ARN for the username and password of the camera, or a local media file location.

MediaUriType -> (string)

The Uniform Resource Identifier (URI) type. The `FILE_URI` value can be used to stream local media files.

### Note

Preview only supports the `RTSP_URI` media source URI format .

ScheduleConfig -> (structure)

The configuration that consists of the `ScheduleExpression` and the `DurationInMinutes` details that specify the scheduling to record from a camera, or local media file, onto the Edge Agent. If the `ScheduleExpression` attribute is not provided, then the Edge Agent will always be set to recording mode.

ScheduleExpression -> (string)

The Quartz cron expression that takes care of scheduling jobs to record from the camera, or local media file, onto the Edge Agent. If the `ScheduleExpression` is not provided for the `RecorderConfig` , then the Edge Agent will always be set to recording mode.

For more information about Quartz, refer to the ` *Cron Trigger Tutorial* [http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger).html`__ page to understand the valid expressions and its use.

DurationInSeconds -> (integer)

The total duration to record the media. If the `ScheduleExpression` attribute is provided, then the `DurationInSeconds` attribute should also be specified.

UploaderConfig -> (structure)

The uploader configuration contains the `ScheduleExpression` details that are used to schedule upload jobs for the recorded media files from the Edge Agent to a Kinesis Video Stream.

ScheduleConfig -> (structure)

The configuration that consists of the `ScheduleExpression` and the `DurationInMinutes` details that specify the scheduling to record from a camera, or local media file, onto the Edge Agent. If the `ScheduleConfig` is not provided in this `UploaderConfig` , then the Edge Agent will upload at regular intervals (every 1 hour).

ScheduleExpression -> (string)

The Quartz cron expression that takes care of scheduling jobs to record from the camera, or local media file, onto the Edge Agent. If the `ScheduleExpression` is not provided for the `RecorderConfig` , then the Edge Agent will always be set to recording mode.

For more information about Quartz, refer to the ` *Cron Trigger Tutorial* [http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger).html`__ page to understand the valid expressions and its use.

DurationInSeconds -> (integer)

The total duration to record the media. If the `ScheduleExpression` attribute is provided, then the `DurationInSeconds` attribute should also be specified.

DeletionConfig -> (structure)

The deletion configuration is made up of the retention time (`EdgeRetentionInHours` ) and local size configuration (`LocalSizeConfig` ) details that are used to make the deletion.

EdgeRetentionInHours -> (integer)

The number of hours that you want to retain the data in the stream on the Edge Agent. The default value of the retention time is 720 hours, which translates to 30 days.

LocalSizeConfig -> (structure)

The value of the local size required in order to delete the edge configuration.

MaxLocalMediaSizeInMB -> (integer)

The overall maximum size of the media that you want to store for a stream on the Edge Agent.

StrategyOnFullSize -> (string)

The strategy to perform when a streamâs `MaxLocalMediaSizeInMB` limit is reached.

DeleteAfterUpload -> (boolean)

The `boolean` value used to indicate whether or not you want to mark the media for deletion, once it has been uploaded to the Kinesis Video Stream cloud. The media files can be deleted if any of the deletion configuration values are set to `true` , such as when the limit for the `EdgeRetentionInHours` , or the `MaxLocalMediaSizeInMB` , has been reached.

Since the default value is set to `true` , configure the uploader schedule such that the media files are not being deleted before they are initially uploaded to the Amazon Web Services cloud.

NextToken -> (string)

If the response is truncated, the call returns this element with a given token. To get the next batch of edge configurations, use this token in your next request.