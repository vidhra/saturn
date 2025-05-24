# describe-imagesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-images.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-images.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appstream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/index.html#cli-aws-appstream) ]

# describe-images

## Description

Retrieves a list that describes one or more specified images, if the image names or image ARNs are provided. Otherwise, all images in the account are described.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appstream-2016-12-01/DescribeImages)

`describe-images` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Images`

## Synopsis

```
describe-images
[--names <value>]
[--arns <value>]
[--type <value>]
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

`--names` (list)

The names of the public or private images to describe.

(string)

Syntax:

```
"string" "string" ...
```

`--arns` (list)

The ARNs of the public, private, and shared images to describe.

(string)

Syntax:

```
"string" "string" ...
```

`--type` (string)

The type of image (public, private, or shared) to describe.

Possible values:

- `PUBLIC`
- `PRIVATE`
- `SHARED`

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

Images -> (list)

Information about the images.

(structure)

Describes an image.

Name -> (string)

The name of the image.

Arn -> (string)

The ARN of the image.

BaseImageArn -> (string)

The ARN of the image from which this image was created.

DisplayName -> (string)

The image name to display.

State -> (string)

The image starts in the `PENDING` state. If image creation succeeds, the state is `AVAILABLE` . If image creation fails, the state is `FAILED` .

Visibility -> (string)

Indicates whether the image is public or private.

ImageBuilderSupported -> (boolean)

Indicates whether an image builder can be launched from this image.

ImageBuilderName -> (string)

The name of the image builder that was used to create the private image. If the image is shared, this value is null.

Platform -> (string)

The operating system platform of the image.

Description -> (string)

The description to display.

StateChangeReason -> (structure)

The reason why the last state change occurred.

Code -> (string)

The state change reason code.

Message -> (string)

The state change reason message.

Applications -> (list)

The applications associated with the image.

(structure)

Describes an application in the application catalog.

Name -> (string)

The name of the application.

DisplayName -> (string)

The application name to display.

IconURL -> (string)

The URL for the application icon. This URL might be time-limited.

LaunchPath -> (string)

The path to the application executable in the instance.

LaunchParameters -> (string)

The arguments that are passed to the application at launch.

Enabled -> (boolean)

If there is a problem, the application can be disabled after image creation.

Metadata -> (map)

Additional attributes that describe the application.

key -> (string)

value -> (string)

WorkingDirectory -> (string)

The working directory for the application.

Description -> (string)

The description of the application.

Arn -> (string)

The ARN of the application.

AppBlockArn -> (string)

The app block ARN of the application.

IconS3Location -> (structure)

The S3 location of the application icon.

S3Bucket -> (string)

The S3 bucket of the S3 object.

S3Key -> (string)

The S3 key of the S3 object.

This is required when used for the following:

- IconS3Location (Actions: CreateApplication and UpdateApplication)
- SessionScriptS3Location (Actions: CreateFleet and UpdateFleet)
- ScriptDetails (Actions: CreateAppBlock)
- SourceS3Location when creating an app block with `CUSTOM` PackagingType (Actions: CreateAppBlock)
- SourceS3Location when creating an app block with `APPSTREAM2` PackagingType, and using an existing application package (VHD file). In this case, `S3Key` refers to the VHD file. If a new application package is required, then `S3Key` is not required. (Actions: CreateAppBlock)

Platforms -> (list)

The platforms on which the application can run.

(string)

InstanceFamilies -> (list)

The instance families for the application.

(string)

CreatedTime -> (timestamp)

The time at which the application was created within the app block.

CreatedTime -> (timestamp)

The time the image was created.

PublicBaseImageReleasedDate -> (timestamp)

The release date of the public base image. For private images, this date is the release date of the base image from which the image was created.

AppstreamAgentVersion -> (string)

The version of the AppStream 2.0 agent to use for instances that are launched from this image.

ImagePermissions -> (structure)

The permissions to provide to the destination AWS account for the specified image.

allowFleet -> (boolean)

Indicates whether the image can be used for a fleet.

allowImageBuilder -> (boolean)

Indicates whether the image can be used for an image builder.

ImageErrors -> (list)

Describes the errors that are returned when a new image canât be created.

(structure)

Describes a resource error.

ErrorCode -> (string)

The error code.

ErrorMessage -> (string)

The error message.

ErrorTimestamp -> (timestamp)

The time the error occurred.

LatestAppstreamAgentVersion -> (string)

Indicates whether the image is using the latest AppStream 2.0 agent version or not.

SupportedInstanceFamilies -> (list)

The supported instances families that determine which image a customer can use when the customer launches a fleet or image builder. The following instances families are supported:

- General Purpose
- Compute Optimized
- Memory Optimized
- Graphics
- Graphics Design
- Graphics Pro
- Graphics G4
- Graphics G5

(string)

DynamicAppProvidersEnabled -> (string)

Indicates whether dynamic app providers are enabled within an AppStream 2.0 image or not.

ImageSharedWithOthers -> (string)

Indicates whether the image is shared with another account ID.

NextToken -> (string)

The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.