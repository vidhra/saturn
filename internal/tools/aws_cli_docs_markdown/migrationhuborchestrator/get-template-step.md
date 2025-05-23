# get-template-stepÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhuborchestrator/get-template-step.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhuborchestrator/get-template-step.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [migrationhuborchestrator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhuborchestrator/index.html#cli-aws-migrationhuborchestrator) ]

# get-template-step

## Description

Get a specific step in a template.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/migrationhuborchestrator-2021-08-28/GetTemplateStep)

## Synopsis

```
get-template-step
--id <value>
--template-id <value>
--step-group-id <value>
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

`--id` (string)

The ID of the step.

`--template-id` (string)

The ID of the template.

`--step-group-id` (string)

The ID of the step group.

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

id -> (string)

The ID of the step.

stepGroupId -> (string)

The ID of the step group.

templateId -> (string)

The ID of the template.

name -> (string)

The name of the step.

description -> (string)

The description of the step.

stepActionType -> (string)

The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.

creationTime -> (string)

The time at which the step was created.

previous -> (list)

The previous step.

(string)

next -> (list)

The next step.

(string)

outputs -> (list)

The outputs of the step.

(structure)

The output of the step.

name -> (string)

The name of the step.

dataType -> (string)

The data type of the step output.

required -> (boolean)

Determine if an output is required from a step.

stepAutomationConfiguration -> (structure)

The custom script to run tests on source or target environments.

scriptLocationS3Bucket -> (string)

The Amazon S3 bucket where the script is located.

scriptLocationS3Key -> (structure)

The Amazon S3 key for the script location.

linux -> (string)

The script location for Linux.

windows -> (string)

The script location for Windows.

command -> (structure)

The command to run the script.

linux -> (string)

Command for Linux.

windows -> (string)

Command for Windows.

runEnvironment -> (string)

The source or target environment.

targetType -> (string)

The servers on which to run the script.