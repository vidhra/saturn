# list-cis-scan-configurationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-cis-scan-configurations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-cis-scan-configurations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/index.html#cli-aws-inspector2) ]

# list-cis-scan-configurations

## Description

Lists CIS scan configurations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector2-2020-06-08/ListCisScanConfigurations)

`list-cis-scan-configurations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `scanConfigurations`

## Synopsis

```
list-cis-scan-configurations
[--filter-criteria <value>]
[--sort-by <value>]
[--sort-order <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--filter-criteria` (structure)

The CIS scan configuration filter criteria.

scanConfigurationArnFilters -> (list)

The list of scan configuration ARN filters.

(structure)

The CIS string filter.

comparison -> (string)

The comparison value of the CIS string filter.

value -> (string)

The value of the CIS string filter.

scanNameFilters -> (list)

The list of scan name filters.

(structure)

The CIS string filter.

comparison -> (string)

The comparison value of the CIS string filter.

value -> (string)

The value of the CIS string filter.

targetResourceTagFilters -> (list)

The list of target resource tag filters.

(structure)

The tag filter.

comparison -> (string)

The tag filter comparison value.

key -> (string)

The tag filter key.

value -> (string)

The tag filter value.

Shorthand Syntax:

```
scanConfigurationArnFilters=[{comparison=string,value=string},{comparison=string,value=string}],scanNameFilters=[{comparison=string,value=string},{comparison=string,value=string}],targetResourceTagFilters=[{comparison=string,key=string,value=string},{comparison=string,key=string,value=string}]
```

JSON Syntax:

```
{
  "scanConfigurationArnFilters": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "scanNameFilters": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "targetResourceTagFilters": [
    {
      "comparison": "EQUALS",
      "key": "string",
      "value": "string"
    }
    ...
  ]
}
```

`--sort-by` (string)

The CIS scan configuration sort by order.

Possible values:

- `SCAN_NAME`
- `SCAN_CONFIGURATION_ARN`

`--sort-order` (string)

The CIS scan configuration sort order order.

Possible values:

- `ASC`
- `DESC`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

nextToken -> (string)

The pagination token from a previous request thatâs used to retrieve the next page of results.

scanConfigurations -> (list)

The CIS scan configuration scan configurations.

(structure)

The CIS scan configuration.

ownerId -> (string)

The CIS scan configurationâs owner ID.

scanConfigurationArn -> (string)

The CIS scan configurationâs scan configuration ARN.

scanName -> (string)

The name of the CIS scan configuration.

schedule -> (tagged union structure)

The CIS scan configurationâs schedule.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `daily`, `monthly`, `oneTime`, `weekly`.

daily -> (structure)

The scheduleâs daily.

startTime -> (structure)

The schedule start time.

timeOfDay -> (string)

The time of day in 24-hour format (00:00).

timezone -> (string)

The timezone.

monthly -> (structure)

The scheduleâs monthly.

day -> (string)

The monthly scheduleâs day.

startTime -> (structure)

The monthly scheduleâs start time.

timeOfDay -> (string)

The time of day in 24-hour format (00:00).

timezone -> (string)

The timezone.

oneTime -> (structure)

The scheduleâs one time.

weekly -> (structure)

The scheduleâs weekly.

days -> (list)

The weekly scheduleâs days.

(string)

startTime -> (structure)

The weekly scheduleâs start time.

timeOfDay -> (string)

The time of day in 24-hour format (00:00).

timezone -> (string)

The timezone.

securityLevel -> (string)

The CIS scan configurationâs security level.

tags -> (map)

The CIS scan configurationâs tags.

key -> (string)

value -> (string)

targets -> (structure)

The CIS scan configurationâs targets.

accountIds -> (list)

The CIS target account ids.

(string)

targetResourceTags -> (map)

The CIS target resource tags.

key -> (string)

value -> (list)

(string)