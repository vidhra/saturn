# list-investigationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-investigations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-investigations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [detective](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/index.html#cli-aws-detective) ]

# list-investigations

## Description

Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident. `ListInvestigations` lists all active Detective investigations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/detective-2018-10-26/ListInvestigations)

## Synopsis

```
list-investigations
--graph-arn <value>
[--next-token <value>]
[--max-results <value>]
[--filter-criteria <value>]
[--sort-criteria <value>]
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

`--graph-arn` (string)

The Amazon Resource Name (ARN) of the behavior graph.

`--next-token` (string)

Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.

Each pagination token expires after 24 hours. Using an expired pagination token will return a Validation Exception error.

`--max-results` (integer)

Lists the maximum number of investigations in a page.

`--filter-criteria` (structure)

Filters the investigation results based on a criteria.

Severity -> (structure)

Filter the investigation results based on the severity.

Value -> (string)

The string filter value.

Status -> (structure)

Filter the investigation results based on the status.

Value -> (string)

The string filter value.

State -> (structure)

Filter the investigation results based on the state.

Value -> (string)

The string filter value.

EntityArn -> (structure)

Filter the investigation results based on the Amazon Resource Name (ARN) of the entity.

Value -> (string)

The string filter value.

CreatedTime -> (structure)

Filter the investigation results based on when the investigation was created.

StartInclusive -> (timestamp)

A timestamp representing the start of the time period from when data is filtered, including the start date.

EndInclusive -> (timestamp)

A timestamp representing the end date of the time period until when data is filtered, including the end date.

Shorthand Syntax:

```
Severity={Value=string},Status={Value=string},State={Value=string},EntityArn={Value=string},CreatedTime={StartInclusive=timestamp,EndInclusive=timestamp}
```

JSON Syntax:

```
{
  "Severity": {
    "Value": "string"
  },
  "Status": {
    "Value": "string"
  },
  "State": {
    "Value": "string"
  },
  "EntityArn": {
    "Value": "string"
  },
  "CreatedTime": {
    "StartInclusive": timestamp,
    "EndInclusive": timestamp
  }
}
```

`--sort-criteria` (structure)

Sorts the investigation results based on a criteria.

Field -> (string)

Represents the `Field` attribute to sort investigations.

SortOrder -> (string)

The order by which the sorted findings are displayed.

Shorthand Syntax:

```
Field=string,SortOrder=string
```

JSON Syntax:

```
{
  "Field": "SEVERITY"|"STATUS"|"CREATED_TIME",
  "SortOrder": "ASC"|"DESC"
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

InvestigationDetails -> (list)

Lists the summary of uncommon behavior or malicious activity which indicates a compromise.

(structure)

Details about the investigation related to a potential security event identified by Detective.

InvestigationId -> (string)

The investigation ID of the investigation report.

Severity -> (string)

Severity based on the likelihood and impact of the indicators of compromise discovered in the investigation.

Status -> (string)

Status based on the completion status of the investigation.

State -> (string)

The current state of the investigation. An archived investigation indicates you have completed reviewing the investigation.

CreatedTime -> (timestamp)

The time stamp of the creation time of the investigation report. The value is an UTC ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z` .

EntityArn -> (string)

The unique Amazon Resource Name (ARN) of the IAM user and IAM role.

EntityType -> (string)

Type of entity. For example, Amazon Web Services accounts, such as IAM user and role.

NextToken -> (string)

Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.

Each pagination token expires after 24 hours.