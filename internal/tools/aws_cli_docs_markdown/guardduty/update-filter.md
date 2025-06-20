# update-filterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-filter.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-filter.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [guardduty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html#cli-aws-guardduty) ]

# update-filter

## Description

Updates the filter specified by the filter name.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateFilter)

## Synopsis

```
update-filter
--detector-id <value>
--filter-name <value>
[--description <value>]
[--action <value>]
[--rank <value>]
[--finding-criteria <value>]
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

`--detector-id` (string)

The unique ID of the detector that specifies the GuardDuty service where you want to update a filter.

To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

`--filter-name` (string)

The name of the filter.

`--description` (string)

The description of the filter. Valid characters include alphanumeric characters, and special characters such as hyphen, period, colon, underscore, parentheses (`{ }` , `[ ]` , and `( )` ), forward slash, horizontal tab, vertical tab, newline, form feed, return, and whitespace.

`--action` (string)

Specifies the action that is to be applied to the findings that match the filter.

Possible values:

- `NOOP`
- `ARCHIVE`

`--rank` (integer)

Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.

`--finding-criteria` (structure)

Represents the criteria to be used in the filter for querying findings.

Criterion -> (map)

Represents a map of finding properties that match specified conditions and values when querying findings.

key -> (string)

value -> (structure)

Contains information about the condition.

Eq -> (list)

Represents the *equal* condition to be applied to a single field when querying for findings.

(string)

Neq -> (list)

Represents the *not equal* condition to be applied to a single field when querying for findings.

(string)

Gt -> (integer)

Represents a *greater than* condition to be applied to a single field when querying for findings.

Gte -> (integer)

Represents a *greater than or equal* condition to be applied to a single field when querying for findings.

Lt -> (integer)

Represents a *less than* condition to be applied to a single field when querying for findings.

Lte -> (integer)

Represents a *less than or equal* condition to be applied to a single field when querying for findings.

Equals -> (list)

Represents an *equal*  condition to be applied to a single field when querying for findings.

(string)

NotEquals -> (list)

Represents a *not equal*  condition to be applied to a single field when querying for findings.

(string)

GreaterThan -> (long)

Represents a *greater than* condition to be applied to a single field when querying for findings.

GreaterThanOrEqual -> (long)

Represents a *greater than or equal* condition to be applied to a single field when querying for findings.

LessThan -> (long)

Represents a *less than* condition to be applied to a single field when querying for findings.

LessThanOrEqual -> (long)

Represents a *less than or equal* condition to be applied to a single field when querying for findings.

Shorthand Syntax:

```
Criterion={KeyName1={Eq=[string,string],Neq=[string,string],Gt=integer,Gte=integer,Lt=integer,Lte=integer,Equals=[string,string],NotEquals=[string,string],GreaterThan=long,GreaterThanOrEqual=long,LessThan=long,LessThanOrEqual=long},KeyName2={Eq=[string,string],Neq=[string,string],Gt=integer,Gte=integer,Lt=integer,Lte=integer,Equals=[string,string],NotEquals=[string,string],GreaterThan=long,GreaterThanOrEqual=long,LessThan=long,LessThanOrEqual=long}}
```

JSON Syntax:

```
{
  "Criterion": {"string": {
        "Eq": ["string", ...],
        "Neq": ["string", ...],
        "Gt": integer,
        "Gte": integer,
        "Lt": integer,
        "Lte": integer,
        "Equals": ["string", ...],
        "NotEquals": ["string", ...],
        "GreaterThan": long,
        "GreaterThanOrEqual": long,
        "LessThan": long,
        "LessThanOrEqual": long
      }
    ...}
}
```

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

Name -> (string)

The name of the filter.