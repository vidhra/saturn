# list-coverage-statisticsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-coverage-statistics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-coverage-statistics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/index.html#cli-aws-inspector2) ]

# list-coverage-statistics

## Description

Lists Amazon Inspector coverage statistics for your environment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector2-2020-06-08/ListCoverageStatistics)

`list-coverage-statistics` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `countsByGroup`

## Synopsis

```
list-coverage-statistics
[--filter-criteria <value>]
[--group-by <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

An object that contains details on the filters to apply to the coverage data for your environment.

accountId -> (list)

An array of Amazon Web Services account IDs to return coverage statistics for.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

ec2InstanceTags -> (list)

The Amazon EC2 instance tags to filter on.

(structure)

Contains details of a coverage map filter.

comparison -> (string)

The operator to compare coverage on.

key -> (string)

The tag key associated with the coverage map filter.

value -> (string)

The tag value associated with the coverage map filter.

ecrImageInUseCount -> (list)

The number of Amazon ECR images in use.

(structure)

The coverage number to be used in the filter.

lowerInclusive -> (long)

The lower inclusive for the coverage number.

upperInclusive -> (long)

The upper inclusive for the coverage number.>

ecrImageLastInUseAt -> (list)

The Amazon ECR image that was last in use.

(structure)

Contains details of a coverage date filter.

endInclusive -> (timestamp)

A timestamp representing the end of the time period to filter results by.

startInclusive -> (timestamp)

A timestamp representing the start of the time period to filter results by.

ecrImageTags -> (list)

The Amazon ECR image tags to filter on.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

ecrRepositoryName -> (list)

The Amazon ECR repository name to filter on.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

imagePulledAt -> (list)

The date an image was last pulled at.

(structure)

Contains details of a coverage date filter.

endInclusive -> (timestamp)

A timestamp representing the end of the time period to filter results by.

startInclusive -> (timestamp)

A timestamp representing the start of the time period to filter results by.

lambdaFunctionName -> (list)

Returns coverage statistics for Amazon Web Services Lambda functions filtered by function names.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

lambdaFunctionRuntime -> (list)

Returns coverage statistics for Amazon Web Services Lambda functions filtered by runtime.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

lambdaFunctionTags -> (list)

Returns coverage statistics for Amazon Web Services Lambda functions filtered by tag.

(structure)

Contains details of a coverage map filter.

comparison -> (string)

The operator to compare coverage on.

key -> (string)

The tag key associated with the coverage map filter.

value -> (string)

The tag value associated with the coverage map filter.

lastScannedAt -> (list)

Filters Amazon Web Services resources based on whether Amazon Inspector has checked them for vulnerabilities within the specified time range.

(structure)

Contains details of a coverage date filter.

endInclusive -> (timestamp)

A timestamp representing the end of the time period to filter results by.

startInclusive -> (timestamp)

A timestamp representing the start of the time period to filter results by.

resourceId -> (list)

An array of Amazon Web Services resource IDs to return coverage statistics for.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

resourceType -> (list)

An array of Amazon Web Services resource types to return coverage statistics for. The values can be `AWS_EC2_INSTANCE` , `AWS_LAMBDA_FUNCTION` , `AWS_ECR_CONTAINER_IMAGE` , `AWS_ECR_REPOSITORY` or `AWS_ACCOUNT` .

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

scanMode -> (list)

The filter to search for Amazon EC2 instance coverage by scan mode. Valid values are `EC2_SSM_AGENT_BASED` and `EC2_AGENTLESS` .

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

scanStatusCode -> (list)

The scan status code to filter on. Valid values are: `ValidationException` , `InternalServerException` , `ResourceNotFoundException` , `BadRequestException` , and `ThrottlingException` .

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

scanStatusReason -> (list)

The scan status reason to filter on.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

scanType -> (list)

An array of Amazon Inspector scan types to return coverage statistics for.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

Shorthand Syntax:

```
accountId=[{comparison=string,value=string},{comparison=string,value=string}],ec2InstanceTags=[{comparison=string,key=string,value=string},{comparison=string,key=string,value=string}],ecrImageInUseCount=[{lowerInclusive=long,upperInclusive=long},{lowerInclusive=long,upperInclusive=long}],ecrImageLastInUseAt=[{endInclusive=timestamp,startInclusive=timestamp},{endInclusive=timestamp,startInclusive=timestamp}],ecrImageTags=[{comparison=string,value=string},{comparison=string,value=string}],ecrRepositoryName=[{comparison=string,value=string},{comparison=string,value=string}],imagePulledAt=[{endInclusive=timestamp,startInclusive=timestamp},{endInclusive=timestamp,startInclusive=timestamp}],lambdaFunctionName=[{comparison=string,value=string},{comparison=string,value=string}],lambdaFunctionRuntime=[{comparison=string,value=string},{comparison=string,value=string}],lambdaFunctionTags=[{comparison=string,key=string,value=string},{comparison=string,key=string,value=string}],lastScannedAt=[{endInclusive=timestamp,startInclusive=timestamp},{endInclusive=timestamp,startInclusive=timestamp}],resourceId=[{comparison=string,value=string},{comparison=string,value=string}],resourceType=[{comparison=string,value=string},{comparison=string,value=string}],scanMode=[{comparison=string,value=string},{comparison=string,value=string}],scanStatusCode=[{comparison=string,value=string},{comparison=string,value=string}],scanStatusReason=[{comparison=string,value=string},{comparison=string,value=string}],scanType=[{comparison=string,value=string},{comparison=string,value=string}]
```

JSON Syntax:

```
{
  "accountId": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ec2InstanceTags": [
    {
      "comparison": "EQUALS",
      "key": "string",
      "value": "string"
    }
    ...
  ],
  "ecrImageInUseCount": [
    {
      "lowerInclusive": long,
      "upperInclusive": long
    }
    ...
  ],
  "ecrImageLastInUseAt": [
    {
      "endInclusive": timestamp,
      "startInclusive": timestamp
    }
    ...
  ],
  "ecrImageTags": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ecrRepositoryName": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "imagePulledAt": [
    {
      "endInclusive": timestamp,
      "startInclusive": timestamp
    }
    ...
  ],
  "lambdaFunctionName": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "lambdaFunctionRuntime": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "lambdaFunctionTags": [
    {
      "comparison": "EQUALS",
      "key": "string",
      "value": "string"
    }
    ...
  ],
  "lastScannedAt": [
    {
      "endInclusive": timestamp,
      "startInclusive": timestamp
    }
    ...
  ],
  "resourceId": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "resourceType": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "scanMode": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "scanStatusCode": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "scanStatusReason": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "scanType": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ]
}
```

`--group-by` (string)

The value to group the results by.

Possible values:

- `SCAN_STATUS_CODE`
- `SCAN_STATUS_REASON`
- `ACCOUNT_ID`
- `RESOURCE_TYPE`
- `ECR_REPOSITORY_NAME`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To list coverage statistics by groups**

The following `list-coverage-statistics` example lists the coverage statistics of your AWS environment by groups.

```
aws inspector2 list-coverage-statistics \
   --group-by RESOURCE_TYPE
```

Output:

```
{
    "countsByGroup": [
        {
            "count": 56,
            "groupKey": "AWS_LAMBDA_FUNCTION"
        },
        {
            "count": 27,
            "groupKey": "AWS_ECR_REPOSITORY"
        },
        {
            "count": 18,
            "groupKey": "AWS_EC2_INSTANCE"
        },
        {
            "count": 3,
            "groupKey": "AWS_ECR_CONTAINER_IMAGE"
        },
        {
            "count": 1,
            "groupKey": "AWS_ACCOUNT"
        }
    ],
    "totalCounts": 105
}
```

For more information, see [Assessing Amazon Inspector coverage of your AWS environment](https://docs.aws.amazon.com/inspector/latest/user/assessing-coverage.html) in the *Amazon Inspector User Guide*.

**Example 2: To list coverage statistics by resource type**

The following `list-coverage-statistics` example lists the coverage statistics of your AWS environment by resource type.

```
aws inspector2 list-coverage-statistics
    --filter-criteria '{"resourceType":[{"comparison":"EQUALS","value":"AWS_ECR_REPOSITORY"}]}'
    --group-by SCAN_STATUS_REASON
```

Output:

```
{
    "countsByGroup": [
        {
            "count": 27,
            "groupKey": "SUCCESSFUL"
        }
    ],
    "totalCounts": 27
}
```

For more information, see [Assessing Amazon Inspector coverage of your AWS environment](https://docs.aws.amazon.com/inspector/latest/user/assessing-coverage.html) in the *Amazon Inspector User Guide*.

**Example 3: To list coverage statistics by ECR repository name**

The following `list-coverage-statistics` example lists the coverage statistics of your AWS environment by ECR repository name.

```
aws inspector2 list-coverage-statistics
   --filter-criteria '{"ecrRepositoryName":[{"comparison":"EQUALS","value":"debian"}]}'
   --group-by SCAN_STATUS_REASON
```

Output:

```
{
    "countsByGroup": [
        {
            "count": 3,
            "groupKey": "SUCCESSFUL"
        }
    ],
    "totalCounts": 3
}
```

For more information, see [Assessing Amazon Inspector coverage of your AWS environment](https://docs.aws.amazon.com/inspector/latest/user/assessing-coverage.html) in the *Amazon Inspector User Guide*.

## Output

countsByGroup -> (list)

An array with the number for each group.

(structure)

a structure that contains information on the count of resources within a group.

count -> (long)

The number of resources.

groupKey -> (string)

The key associated with this group

nextToken -> (string)

A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.

totalCounts -> (long)

The total number for all groups.