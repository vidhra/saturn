# create-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/create-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/create-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gameliftstreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/index.html#cli-aws-gameliftstreams) ]

# create-application

## Description

Creates an application resource in Amazon GameLift Streams, which specifies the application content you want to stream, such as a game build or other software, and configures the settings to run it.

Before you create an application, upload your application content files to an Amazon Simple Storage Service (Amazon S3) bucket. For more information, see **Getting Started** in the Amazon GameLift Streams Developer Guide.

### Warning

Make sure that your files in the Amazon S3 bucket are the correct version you want to use. As soon as you create a Amazon GameLift Streams application, you cannot change the files at a later time.

If the request is successful, Amazon GameLift Streams begins to create an application and sets the status to `INITIALIZED` . When an application reaches `READY` status, you can use the application to set up stream groups and start streams. To track application status, call [GetApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetApplication.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gameliftstreams-2018-05-10/CreateApplication)

## Synopsis

```
create-application
[--application-log-output-uri <value>]
[--application-log-paths <value>]
--application-source-uri <value>
[--client-token <value>]
--description <value>
--executable-path <value>
--runtime-environment <value>
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

`--application-log-output-uri` (string)

An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more `ApplicationLogPaths` .

### Note

The log bucket must have permissions that give Amazon GameLift Streams access to write the log files. For more information, see **Getting Started** in the Amazon GameLift Streams Developer Guide.

`--application-log-paths` (list)

Locations of log files that your content generates during a stream session. Enter path values that are relative to the `ApplicationSourceUri` location. You can specify up to 10 log paths. Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in `ApplicationLogOutputUri` at the end of a stream session. To retrieve stored log files, call [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) and get the `LogFileLocationUri` .

(string)

Syntax:

```
"string" "string" ...
```

`--application-source-uri` (string)

The location of the content that you want to stream. Enter an Amazon S3 URI to a bucket that contains your game or other application. The location can have a multi-level prefix structure, but it must include all the files needed to run the content. Amazon GameLift Streams copies everything under the specified location.

This value is immutable. To designate a different content location, create a new application.

### Note

The Amazon S3 bucket and the Amazon GameLift Streams application must be in the same Amazon Web Services Region.

`--client-token` (string)

A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field.

`--description` (string)

A human-readable label for the application. You can update this value later.

`--executable-path` (string)

The path and file name of the executable file that launches the content for streaming. Enter a path value that is relative to the location set in `ApplicationSourceUri` .

`--runtime-environment` (structure)

Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers.

A runtime environment can be one of the following:

- For Linux applications
- Ubuntu 22.04 LTS (`Type=UBUNTU, Version=22_04_LTS` )
- For Windows applications
- Microsoft Windows Server 2022 Base (`Type=WINDOWS, Version=2022` )
- Proton 8.0-5 (`Type=PROTON, Version=20241007` )
- Proton 8.0-2c (`Type=PROTON, Version=20230704` )

Type -> (string)

The operating system and other drivers. For Proton, this also includes the Proton compatibility layer.

Version -> (string)

Versioned container environment for the application operating system.

Shorthand Syntax:

```
Type=string,Version=string
```

JSON Syntax:

```
{
  "Type": "PROTON"|"WINDOWS"|"UBUNTU",
  "Version": "string"
}
```

`--tags` (map)

A list of labels to assign to the new application resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. See [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference* . You can use [TagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html) to add tags, [UntagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html) to remove tags, and [ListTagsForResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html) to view tags on existing resources.

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

ApplicationLogOutputUri -> (string)

An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more `ApplicationLogPaths` .

ApplicationLogPaths -> (list)

Locations of log files that your content generates during a stream session. Amazon GameLift Streams uploads log files to the Amazon S3 bucket that you specify in `ApplicationLogOutputUri` at the end of a stream session. To retrieve stored log files, call [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) and get the `LogFileLocationUri` .

(string)

ApplicationSourceUri -> (string)

The original Amazon S3 location of uploaded stream content for the application.

Arn -> (string)

An Amazon Resource Name (ARN) thatâs assigned to an application resource and uniquely identifies it across all Amazon Web Services Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:application/[resource ID]` .

AssociatedStreamGroups -> (list)

A newly created application is not associated to any stream groups. This value is empty.

(string)

CreatedAt -> (timestamp)

A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).

Description -> (string)

A human-readable label for the application. You can edit this value.

ExecutablePath -> (string)

The path and file name of the executable file that launches the content for streaming.

Id -> (string)

An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the application resource. Format example: ARN-`arn:aws:gameliftstreams:us-west-2:123456789012:application/a-9ZY8X7Wv6` or ID-`a-9ZY8X7Wv6` .

LastUpdatedAt -> (timestamp)

A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).

ReplicationStatuses -> (list)

A set of replication statuses for each location.

(structure)

Represents the status of the replication of an application to a location. An application cannot be streamed from a location until it has finished replicating there.

Location -> (string)

A locationâs name. For example, `us-east-1` . For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions and quotas](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide* .

Status -> (string)

The current status of the replication process.

RuntimeEnvironment -> (structure)

Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers.

A runtime environment can be one of the following:

- For Linux applications
- Ubuntu 22.04 LTS (`Type=UBUNTU, Version=22_04_LTS` )
- For Windows applications
- Microsoft Windows Server 2022 Base (`Type=WINDOWS, Version=2022` )
- Proton 8.0-5 (`Type=PROTON, Version=20241007` )
- Proton 8.0-2c (`Type=PROTON, Version=20230704` )

Type -> (string)

The operating system and other drivers. For Proton, this also includes the Proton compatibility layer.

Version -> (string)

Versioned container environment for the application operating system.

Status -> (string)

The current status of the application resource. Possible statuses include the following:

- `INITIALIZED` : Amazon GameLift Streams has received the request and is initiating the work flow to create an application.
- `PROCESSING` : The create application work flow is in process. Amazon GameLift Streams is copying the content and caching for future deployment in a stream group.
- `READY` : The application is ready to deploy in a stream group.
- `ERROR` : An error occurred when setting up the application. See `StatusReason` for more information.
- `DELETING` : Amazon GameLift Streams is in the process of deleting the application.

StatusReason -> (string)

A short description of the status reason when the application is in `ERROR` status.