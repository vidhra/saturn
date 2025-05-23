# describe-change-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/describe-change-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/describe-change-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [marketplace-catalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/index.html#cli-aws-marketplace-catalog) ]

# describe-change-set

## Description

Provides information about a given change set.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/marketplace-catalog-2018-09-17/DescribeChangeSet)

`describe-change-set` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
describe-change-set
--catalog <value>
--change-set-id <value>
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

`--catalog` (string)

Required. The catalog related to the request. Fixed value: `AWSMarketplace`

`--change-set-id` (string)

Required. The unique identifier for the `StartChangeSet` request that you want to describe the details for.

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

ChangeSetId -> (string)

Required. The unique identifier for the change set referenced in this request.

ChangeSetArn -> (string)

The ARN associated with the unique identifier for the change set referenced in this request.

ChangeSetName -> (string)

The optional name provided in the `StartChangeSet` request. If you do not provide a name, one is set by default.

Intent -> (string)

The optional intent provided in the `StartChangeSet` request. If you do not provide an intent, `APPLY` is set by default.

StartTime -> (string)

The date and time, in ISO 8601 format (2018-02-27T13:45:22Z), the request started.

EndTime -> (string)

The date and time, in ISO 8601 format (2018-02-27T13:45:22Z), the request transitioned to a terminal state. The change cannot transition to a different state. Null if the request is not in a terminal state.

Status -> (string)

The status of the change request.

FailureCode -> (string)

Returned if the change set is in `FAILED` status. Can be either `CLIENT_ERROR` , which means that there are issues with the request (see the `ErrorDetailList` ), or `SERVER_FAULT` , which means that there is a problem in the system, and you should retry your request.

FailureDescription -> (string)

Returned if there is a failure on the change set, but that failure is not related to any of the changes in the request.

ChangeSet -> (list)

An array of `ChangeSummary` objects.

(structure)

This object is a container for common summary information about the change. The summary doesnât contain the whole change structure.

ChangeType -> (string)

The type of the change.

Entity -> (structure)

The entity to be changed.

Type -> (string)

The type of entity.

Identifier -> (string)

The identifier for the entity.

Details -> (string)

This object contains details specific to the change type of the requested change.

DetailsDocument -> (document)

The JSON value of the details specific to the change type of the requested change.

ErrorDetailList -> (list)

An array of `ErrorDetail` objects associated with the change.

(structure)

Details about the error.

ErrorCode -> (string)

The error code that identifies the type of error.

ErrorMessage -> (string)

The message for the error.

ChangeName -> (string)

Optional name for the change.