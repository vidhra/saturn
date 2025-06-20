# create-qualification-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/create-qualification-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/create-qualification-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mturk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/index.html#cli-aws-mturk) ]

# create-qualification-type

## Description

The `CreateQualificationType` operation creates a new Qualification type, which is represented by a `QualificationType` data structure.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/CreateQualificationType)

## Synopsis

```
create-qualification-type
--name <value>
[--keywords <value>]
--description <value>
--qualification-type-status <value>
[--retry-delay-in-seconds <value>]
[--test <value>]
[--answer-key <value>]
[--test-duration-in-seconds <value>]
[--auto-granted | --no-auto-granted]
[--auto-granted-value <value>]
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

`--name` (string)

The name you give to the Qualification type. The type name is used to represent the Qualification to Workers, and to find the type using a Qualification type search. It must be unique across all of your Qualification types.

`--keywords` (string)

One or more words or phrases that describe the Qualification type, separated by commas. The keywords of a type make the type easier to find during a search.

`--description` (string)

A long description for the Qualification type. On the Amazon Mechanical Turk website, the long description is displayed when a Worker examines a Qualification type.

`--qualification-type-status` (string)

The initial status of the Qualification type.

Constraints: Valid values are: Active | Inactive

Possible values:

- `Active`
- `Inactive`

`--retry-delay-in-seconds` (long)

The number of seconds that a Worker must wait after requesting a Qualification of the Qualification type before the worker can retry the Qualification request.

Constraints: None. If not specified, retries are disabled and Workers can request a Qualification of this type only once, even if the Worker has not been granted the Qualification. It is not possible to disable retries for a Qualification type after it has been created with retries enabled. If you want to disable retries, you must delete existing retry-enabled Qualification type and then create a new Qualification type with retries disabled.

`--test` (string)

The questions for the Qualification test a Worker must answer correctly to obtain a Qualification of this type. If this parameter is specified, `TestDurationInSeconds` must also be specified.

Constraints: Must not be longer than 65535 bytes. Must be a QuestionForm data structure. This parameter cannot be specified if AutoGranted is true.

Constraints: None. If not specified, the Worker may request the Qualification without answering any questions.

`--answer-key` (string)

The answers to the Qualification test specified in the Test parameter, in the form of an AnswerKey data structure.

Constraints: Must not be longer than 65535 bytes.

Constraints: None. If not specified, you must process Qualification requests manually.

`--test-duration-in-seconds` (long)

The number of seconds the Worker has to complete the Qualification test, starting from the time the Worker requests the Qualification.

`--auto-granted` | `--no-auto-granted` (boolean)

Specifies whether requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test.

Constraints: If the Test parameter is specified, this parameter cannot be true.

`--auto-granted-value` (integer)

The Qualification value to use for automatically granted Qualifications. This parameter is used only if the AutoGranted parameter is true.

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

QualificationType -> (structure)

The created Qualification type, returned as a QualificationType data structure.

QualificationTypeId -> (string)

A unique identifier for the Qualification type. A Qualification type is given a Qualification type ID when you call the CreateQualificationType operation.

CreationTime -> (timestamp)

The date and time the Qualification type was created.

Name -> (string)

The name of the Qualification type. The type name is used to identify the type, and to find the type using a Qualification type search.

Description -> (string)

A long description for the Qualification type.

Keywords -> (string)

One or more words or phrases that describe theQualification type, separated by commas. The Keywords make the type easier to find using a search.

QualificationTypeStatus -> (string)

The status of the Qualification type. A Qualification typeâs status determines if users can apply to receive a Qualification of this type, and if HITs can be created with requirements based on this type. Valid values are Active | Inactive.

Test -> (string)

The questions for a Qualification test associated with this Qualification type that a user can take to obtain a Qualification of this type. This parameter must be specified if AnswerKey is present. A Qualification type cannot have both a specified Test parameter and an AutoGranted value of true.

TestDurationInSeconds -> (long)

The amount of time, in seconds, given to a Worker to complete the Qualification test, beginning from the time the Worker requests the Qualification.

AnswerKey -> (string)

The answers to the Qualification test specified in the Test parameter.

RetryDelayInSeconds -> (long)

The amount of time, in seconds, Workers must wait after taking the Qualification test before they can take it again. Workers can take a Qualification test multiple times if they were not granted the Qualification from a previous attempt, or if the test offers a gradient score and they want a better score. If not specified, retries are disabled and Workers can request a Qualification only once.

IsRequestable -> (boolean)

Specifies whether the Qualification type is one that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is False for Qualifications assigned automatically by the system. Valid values are True | False.

AutoGranted -> (boolean)

Specifies that requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test. Valid values are True | False.

AutoGrantedValue -> (integer)

The Qualification integer value to use for automatically granted Qualifications, if AutoGranted is true. This is 1 by default.