# list-hub-content-versionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-hub-content-versions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-hub-content-versions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# list-hub-content-versions

## Description

List hub content versions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListHubContentVersions)

## Synopsis

```
list-hub-content-versions
--hub-name <value>
--hub-content-type <value>
--hub-content-name <value>
[--min-version <value>]
[--max-schema-version <value>]
[--creation-time-before <value>]
[--creation-time-after <value>]
[--sort-by <value>]
[--sort-order <value>]
[--max-results <value>]
[--next-token <value>]
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

`--hub-name` (string)

The name of the hub to list the content versions of.

`--hub-content-type` (string)

The type of hub content to list versions of.

Possible values:

- `Model`
- `Notebook`
- `ModelReference`

`--hub-content-name` (string)

The name of the hub content.

`--min-version` (string)

The lower bound of the hub content versions to list.

`--max-schema-version` (string)

The upper bound of the hub content schema version.

`--creation-time-before` (timestamp)

Only list hub content versions that were created before the time specified.

`--creation-time-after` (timestamp)

Only list hub content versions that were created after the time specified.

`--sort-by` (string)

Sort hub content versions by either name or creation time.

Possible values:

- `HubContentName`
- `CreationTime`
- `HubContentStatus`

`--sort-order` (string)

Sort hub content versions by ascending or descending order.

Possible values:

- `Ascending`
- `Descending`

`--max-results` (integer)

The maximum number of hub content versions to list.

`--next-token` (string)

If the response to a previous `ListHubContentVersions` request was truncated, the response includes a `NextToken` . To retrieve the next set of hub content versions, use the token in the next request.

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

HubContentSummaries -> (list)

The summaries of the listed hub content versions.

(structure)

Information about hub content.

HubContentName -> (string)

The name of the hub content.

HubContentArn -> (string)

The Amazon Resource Name (ARN) of the hub content.

SageMakerPublicHubContentArn -> (string)

The ARN of the public hub content.

HubContentVersion -> (string)

The version of the hub content.

HubContentType -> (string)

The type of hub content.

DocumentSchemaVersion -> (string)

The version of the hub content document schema.

HubContentDisplayName -> (string)

The display name of the hub content.

HubContentDescription -> (string)

A description of the hub content.

SupportStatus -> (string)

The support status of the hub content.

HubContentSearchKeywords -> (list)

The searchable keywords for the hub content.

(string)

HubContentStatus -> (string)

The status of the hub content.

CreationTime -> (timestamp)

The date and time that the hub content was created.

OriginalCreationTime -> (timestamp)

The date and time when the hub content was originally created, before any updates or revisions.

NextToken -> (string)

If the response is truncated, SageMaker returns this token. To retrieve the next set of hub content versions, use it in the subsequent request.