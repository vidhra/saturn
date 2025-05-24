# get-qualification-scoreÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/get-qualification-score.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/get-qualification-score.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mturk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/index.html#cli-aws-mturk) ]

# get-qualification-score

## Description

The `GetQualificationScore` operation returns the value of a Workerâs Qualification for a given Qualification type.

To get a Workerâs Qualification, you must know the Workerâs ID. The Workerâs ID is included in the assignment data returned by the `ListAssignmentsForHIT` operation.

Only the owner of a Qualification type can query the value of a Workerâs Qualification of that type.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/GetQualificationScore)

## Synopsis

```
get-qualification-score
--qualification-type-id <value>
--worker-id <value>
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

`--qualification-type-id` (string)

The ID of the QualificationType.

`--worker-id` (string)

The ID of the Worker whose Qualification is being updated.

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

Qualification -> (structure)

The Qualification data structure of the Qualification assigned to a user, including the Qualification type and the value (score).

QualificationTypeId -> (string)

The ID of the Qualification type for the Qualification.

WorkerId -> (string)

The ID of the Worker who possesses the Qualification.

GrantTime -> (timestamp)

The date and time the Qualification was granted to the Worker. If the Workerâs Qualification was revoked, and then re-granted based on a new Qualification request, GrantTime is the date and time of the last call to the AcceptQualificationRequest operation.

IntegerValue -> (integer)

The value (score) of the Qualification, if the Qualification has an integer value.

LocaleValue -> (structure)

The Locale data structure represents a geographical region or location.

Country -> (string)

The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.

Subdivision -> (string)

The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.

Status -> (string)

The status of the Qualification. Valid values are Granted | Revoked.