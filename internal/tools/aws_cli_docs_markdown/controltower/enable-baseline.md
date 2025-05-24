# enable-baselineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/enable-baseline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/enable-baseline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [controltower](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/index.html#cli-aws-controltower) ]

# enable-baseline

## Description

Enable (apply) a `Baseline` to a Target. This API starts an asynchronous operation to deploy resources specified by the `Baseline` to the specified Target. For usage examples, see ` *the Amazon Web Services Control Tower User Guide* [https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples](https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples).html`__ .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/controltower-2018-05-10/EnableBaseline)

`enable-baseline` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
enable-baseline
--baseline-identifier <value>
--baseline-version <value>
[--parameters <value>]
[--tags <value>]
--target-identifier <value>
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

`--baseline-identifier` (string)

The ARN of the baseline to be enabled.

`--baseline-version` (string)

The specific version to be enabled of the specified baseline.

`--parameters` (list)

A list of `key-value` objects that specify enablement parameters, where `key` is a string and `value` is a document of any type.

(structure)

A key-value parameter to an `EnabledBaseline` resource.

key -> (string)

A string denoting the parameter key.

value -> (document)

A low-level `Document` object of any type (for example, a Java Object).

Shorthand Syntax:

```
key=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": {...}
  }
  ...
]
```

`--tags` (map)

Tags associated with input to `EnableBaseline` .

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

`--target-identifier` (string)

The ARN of the target on which the baseline will be enabled. Only OUs are supported as targets.

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

arn -> (string)

The ARN of the `EnabledBaseline` resource.

operationIdentifier -> (string)

The ID (in UUID format) of the asynchronous `EnableBaseline` operation. This `operationIdentifier` is used to track status through calls to the `GetBaselineOperation` API.