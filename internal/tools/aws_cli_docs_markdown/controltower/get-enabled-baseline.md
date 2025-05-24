# get-enabled-baselineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-enabled-baseline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-enabled-baseline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [controltower](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/index.html#cli-aws-controltower) ]

# get-enabled-baseline

## Description

Retrieve details of an `EnabledBaseline` resource by specifying its identifier.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/controltower-2018-05-10/GetEnabledBaseline)

`get-enabled-baseline` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
get-enabled-baseline
--enabled-baseline-identifier <value>
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

`--enabled-baseline-identifier` (string)

Identifier of the `EnabledBaseline` resource to be retrieved, in ARN format.

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

enabledBaselineDetails -> (structure)

Details of the `EnabledBaseline` resource.

arn -> (string)

The ARN of the `EnabledBaseline` resource.

baselineIdentifier -> (string)

The specific `Baseline` enabled as part of the `EnabledBaseline` resource.

baselineVersion -> (string)

The enabled version of the `Baseline` .

driftStatusSummary -> (structure)

The drift status of the enabled baseline.

types -> (structure)

The types of drift that can be detected for an enabled baseline. Amazon Web Services Control Tower detects inheritance drift on enabled baselines that apply at the OU level.

inheritance -> (structure)

At least one account within the target OU does not match the baseline configuration defined on that OU. An account is in inheritance drift when it does not match the configuration of a parent OU, possibly a new parent OU, if the account is moved.

status -> (string)

The inheritance drift status for enabled baselines.

parameters -> (list)

Shows the parameters that are applied when enabling this `Baseline` .

(structure)

Summary of an applied parameter to an `EnabledBaseline` resource.

key -> (string)

A string denoting the parameter key.

value -> (document)

A low-level document object of any type (for example, a Java Object).

parentIdentifier -> (string)

An ARN that represents the parent `EnabledBaseline` at the Organizational Unit (OU) level, from which the child `EnabledBaseline` inherits its configuration. The value is returned by `GetEnabledBaseline` .

statusSummary -> (structure)

The deployment summary of an `EnabledControl` or `EnabledBaseline` resource.

lastOperationIdentifier -> (string)

The last operation identifier for the enabled resource.

status -> (string)

The deployment status of the enabled resource.

Valid values:

- `SUCCEEDED` : The `EnabledControl` or `EnabledBaseline` configuration was deployed successfully.
- `UNDER_CHANGE` : The `EnabledControl` or `EnabledBaseline` configuration is changing.
- `FAILED` : The `EnabledControl` or `EnabledBaseline` configuration failed to deploy.

targetIdentifier -> (string)

The target on which to enable the `Baseline` .