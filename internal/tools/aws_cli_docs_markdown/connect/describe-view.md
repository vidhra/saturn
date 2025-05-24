# describe-viewÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-view.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-view.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# describe-view

## Description

Retrieves the view for the specified Amazon Connect instance and view identifier.

The view identifier can be supplied as a ViewId or ARN.

`$SAVED` needs to be supplied if a view is unpublished.

The view identifier can contain an optional qualifier, for example, `<view-id>:$SAVED` , which is either an actual version number or an Amazon Connect managed qualifier `$SAVED | $LATEST` . If it is not supplied, then `$LATEST` is assumed for customer managed views and an error is returned if there is no published content available. Version 1 is assumed for Amazon Web Services managed views.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DescribeView)

## Synopsis

```
describe-view
--instance-id <value>
--view-id <value>
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can find the instanceId in the ARN of the instance.

`--view-id` (string)

The ViewId of the view. This must be an ARN for Amazon Web Services managed views.

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

View -> (structure)

All view data is contained within the View object.

Id -> (string)

The identifier of the view.

Arn -> (string)

The Amazon Resource Name (ARN) of the view.

Name -> (string)

The name of the view.

Status -> (string)

Indicates the view status as either `SAVED` or `PUBLISHED` . The `PUBLISHED` status will initiate validation on the content.

Type -> (string)

The type of the view - `CUSTOMER_MANAGED` .

Description -> (string)

The description of the view.

Version -> (integer)

Current version of the view.

VersionDescription -> (string)

The description of the version.

Content -> (structure)

View content containing all content necessary to render a view except for runtime input data.

InputSchema -> (string)

The data schema matching data that the view template must be provided to render.

Template -> (string)

The view template representing the structure of the view.

Actions -> (list)

A list of possible actions from the view.

(string)

Tags -> (map)

The tags associated with the view resource (not specific to view version).

key -> (string)

value -> (string)

CreatedTime -> (timestamp)

The timestamp of when the view was created.

LastModifiedTime -> (timestamp)

Latest timestamp of the `UpdateViewContent` or `CreateViewVersion` operations.

ViewContentSha256 -> (string)

Indicates the checksum value of the latest published view content.