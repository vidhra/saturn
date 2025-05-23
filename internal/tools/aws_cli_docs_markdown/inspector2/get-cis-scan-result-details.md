# get-cis-scan-result-detailsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/get-cis-scan-result-details.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/get-cis-scan-result-details.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/index.html#cli-aws-inspector2) ]

# get-cis-scan-result-details

## Description

Retrieves CIS scan result details.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector2-2020-06-08/GetCisScanResultDetails)

`get-cis-scan-result-details` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `scanResultDetails`

## Synopsis

```
get-cis-scan-result-details
--account-id <value>
[--filter-criteria <value>]
--scan-arn <value>
[--sort-by <value>]
[--sort-order <value>]
--target-resource-id <value>
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

`--account-id` (string)

The account ID.

`--filter-criteria` (structure)

The filter criteria.

checkIdFilters -> (list)

The criteriaâs check ID filters.

(structure)

The CIS string filter.

comparison -> (string)

The comparison value of the CIS string filter.

value -> (string)

The value of the CIS string filter.

findingArnFilters -> (list)

The criteriaâs finding ARN filters.

(structure)

The CIS string filter.

comparison -> (string)

The comparison value of the CIS string filter.

value -> (string)

The value of the CIS string filter.

findingStatusFilters -> (list)

The criteriaâs finding status filters.

(structure)

The CIS finding status filter.

comparison -> (string)

The comparison value of the CIS finding status filter.

value -> (string)

The value of the CIS finding status filter.

securityLevelFilters -> (list)

The criteriaâs security level filters. . Security level refers to the Benchmark levels that CIS assigns to a profile.

(structure)

The CIS security level filter. Security level refers to the Benchmark levels that CIS assigns to a profile.

comparison -> (string)

The CIS security filter comparison value.

value -> (string)

The CIS security filter value.

titleFilters -> (list)

The criteriaâs title filters.

(structure)

The CIS string filter.

comparison -> (string)

The comparison value of the CIS string filter.

value -> (string)

The value of the CIS string filter.

Shorthand Syntax:

```
checkIdFilters=[{comparison=string,value=string},{comparison=string,value=string}],findingArnFilters=[{comparison=string,value=string},{comparison=string,value=string}],findingStatusFilters=[{comparison=string,value=string},{comparison=string,value=string}],securityLevelFilters=[{comparison=string,value=string},{comparison=string,value=string}],titleFilters=[{comparison=string,value=string},{comparison=string,value=string}]
```

JSON Syntax:

```
{
  "checkIdFilters": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "findingArnFilters": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "findingStatusFilters": [
    {
      "comparison": "EQUALS",
      "value": "PASSED"|"FAILED"|"SKIPPED"
    }
    ...
  ],
  "securityLevelFilters": [
    {
      "comparison": "EQUALS",
      "value": "LEVEL_1"|"LEVEL_2"
    }
    ...
  ],
  "titleFilters": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ]
}
```

`--scan-arn` (string)

The scan ARN.

`--sort-by` (string)

The sort by order.

Possible values:

- `CHECK_ID`
- `STATUS`

`--sort-order` (string)

The sort order.

Possible values:

- `ASC`
- `DESC`

`--target-resource-id` (string)

The target resource ID.

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

scanResultDetails -> (list)

The scan result details.

(structure)

The CIS scan result details.

accountId -> (string)

The CIS scan result detailsâ account ID.

checkDescription -> (string)

The account ID thatâs associated with the CIS scan result details.

checkId -> (string)

The CIS scan result detailsâ check ID.

findingArn -> (string)

The CIS scan result detailsâ finding ARN.

level -> (string)

The CIS scan result detailsâ level.

platform -> (string)

The CIS scan result detailsâ platform.

remediation -> (string)

The CIS scan result detailsâ remediation.

scanArn -> (string)

The CIS scan result detailsâ scan ARN.

status -> (string)

The CIS scan result detailsâ status.

statusReason -> (string)

The CIS scan result detailsâ status reason.

targetResourceId -> (string)

The CIS scan result detailsâ target resource ID.

title -> (string)

The CIS scan result detailsâ title.