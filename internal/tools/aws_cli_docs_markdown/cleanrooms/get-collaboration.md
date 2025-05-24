# get-collaborationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/get-collaboration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/get-collaboration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# get-collaboration

## Description

Returns metadata about a collaboration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/GetCollaboration)

## Synopsis

```
get-collaboration
--collaboration-identifier <value>
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

`--collaboration-identifier` (string)

The identifier for the collaboration.

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

collaboration -> (structure)

The entire collaboration for this identifier.

id -> (string)

The unique ID for the collaboration.

arn -> (string)

The unique ARN for the collaboration.

name -> (string)

A human-readable identifier provided by the collaboration owner. Display names are not unique.

description -> (string)

A description of the collaboration provided by the collaboration owner.

creatorAccountId -> (string)

The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.

creatorDisplayName -> (string)

A display name of the collaboration creator.

createTime -> (timestamp)

The time when the collaboration was created.

updateTime -> (timestamp)

The time the collaboration metadata was last updated.

memberStatus -> (string)

The status of a member in a collaboration.

membershipId -> (string)

The unique ID for your membership within the collaboration.

membershipArn -> (string)

The unique ARN for your membership within the collaboration.

dataEncryptionMetadata -> (structure)

The settings for client-side encryption for cryptographic computing.

allowCleartext -> (boolean)

Indicates whether encrypted tables can contain cleartext data (`TRUE` ) or are to cryptographically process every column (`FALSE` ).

allowDuplicates -> (boolean)

Indicates whether Fingerprint columns can contain duplicate entries (`TRUE` ) or are to contain only non-repeated values (`FALSE` ).

allowJoinsOnColumnsWithDifferentNames -> (boolean)

Indicates whether Fingerprint columns can be joined on any other Fingerprint column with a different name (`TRUE` ) or can only be joined on Fingerprint columns of the same name (`FALSE` ).

preserveNulls -> (boolean)

Indicates whether NULL values are to be copied as NULL to encrypted tables (`TRUE` ) or cryptographically processed (`FALSE` ).

queryLogStatus -> (string)

An indicator as to whether query logging has been enabled or disabled for the collaboration.

When `ENABLED` , Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED` .

jobLogStatus -> (string)

An indicator as to whether job logging has been enabled or disabled for the collaboration.

When `ENABLED` , Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is `DISABLED` .

analyticsEngine -> (string)

The analytics engine for the collaboration.