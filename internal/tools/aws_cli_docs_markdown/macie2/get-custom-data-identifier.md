# get-custom-data-identifierÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-custom-data-identifier.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-custom-data-identifier.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [macie2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/index.html#cli-aws-macie2) ]

# get-custom-data-identifier

## Description

Retrieves the criteria and other settings for a custom data identifier.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/macie2-2020-01-01/GetCustomDataIdentifier)

## Synopsis

```
get-custom-data-identifier
--id <value>
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

The unique identifier for the Amazon Macie resource that the request applies to.

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

The Amazon Resource Name (ARN) of the custom data identifier.

createdAt -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when the custom data identifier was created.

deleted -> (boolean)

Specifies whether the custom data identifier was deleted. If you delete a custom data identifier, Amazon Macie doesnât delete it permanently. Instead, it soft deletes the identifier.

description -> (string)

The custom description of the custom data identifier.

id -> (string)

The unique identifier for the custom data identifier.

ignoreWords -> (list)

An array that lists specific character sequences (*ignore words* ) to exclude from the results. If the text matched by the regular expression contains any string in this array, Amazon Macie ignores it. Ignore words are case sensitive.

(string)

keywords -> (list)

An array that lists specific character sequences (*keywords* ), one of which must precede and be within proximity (maximumMatchDistance) of the regular expression to match. Keywords arenât case sensitive.

(string)

maximumMatchDistance -> (integer)

The maximum number of characters that can exist between the end of at least one complete character sequence specified by the keywords array and the end of the text that matches the regex pattern. If a complete keyword precedes all the text that matches the pattern and the keyword is within the specified distance, Amazon Macie includes the result. Otherwise, Macie excludes the result.

name -> (string)

The custom name of the custom data identifier.

regex -> (string)

The regular expression (*regex* ) that defines the pattern to match.

severityLevels -> (list)

Specifies the severity thatâs assigned to findings that the custom data identifier produces, based on the number of occurrences of text that match the custom data identifierâs detection criteria. By default, Amazon Macie creates findings for S3 objects that contain at least one occurrence of text that matches the detection criteria, and Macie assigns the MEDIUM severity to those findings.

(structure)

Specifies a severity level for findings that a custom data identifier produces. A severity level determines which severity is assigned to the findings, based on the number of occurrences of text that match the custom data identifierâs detection criteria.

occurrencesThreshold -> (long)

The minimum number of occurrences of text that must match the custom data identifierâs detection criteria in order to produce a finding with the specified severity (severity).

severity -> (string)

The severity to assign to a finding: if the number of occurrences is greater than or equal to the specified threshold (occurrencesThreshold); and, if applicable, the number of occurrences is less than the threshold for the next consecutive severity level for the custom data identifier, moving from LOW to HIGH.

tags -> (map)

A map of key-value pairs that identifies the tags (keys and values) that are associated with the custom data identifier.

key -> (string)

value -> (string)