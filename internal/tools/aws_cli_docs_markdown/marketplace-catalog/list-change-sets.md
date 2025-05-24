# list-change-setsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/list-change-sets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/list-change-sets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [marketplace-catalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/index.html#cli-aws-marketplace-catalog) ]

# list-change-sets

## Description

Returns the list of change sets owned by the account being used to make the call. You can filter this list by providing any combination of `entityId` , `ChangeSetName` , and status. If you provide more than one filter, the API operation applies a logical AND between the filters.

You can describe a change during the 60-day request history retention period for API calls.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/marketplace-catalog-2018-09-17/ListChangeSets)

`list-change-sets` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ChangeSetSummaryList`

## Synopsis

```
list-change-sets
--catalog <value>
[--filter-list <value>]
[--sort <value>]
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

`--catalog` (string)

The catalog related to the request. Fixed value: `AWSMarketplace`

`--filter-list` (list)

An array of filter objects.

(structure)

A filter object, used to optionally filter results from calls to the `ListEntities` and `ListChangeSets` actions.

Name -> (string)

For `ListEntities` , the supported value for this is an `EntityId` .

For `ListChangeSets` , the supported values are as follows:

ValueList -> (list)

`ListEntities` - This is a list of unique `EntityId` s.

`ListChangeSets` - The supported filter names and associated `ValueList` s is as follows:

- `ChangeSetName` - The supported `ValueList` is a list of non-unique `ChangeSetName` s. These are defined when you call the `StartChangeSet` action.
- `Status` - The supported `ValueList` is a list of statuses for all change set requests.
- `EntityId` - The supported `ValueList` is a list of unique `EntityId` s.
- `BeforeStartTime` - The supported `ValueList` is a list of all change sets that started before the filter value.
- `AfterStartTime` - The supported `ValueList` is a list of all change sets that started after the filter value.
- `BeforeEndTime` - The supported `ValueList` is a list of all change sets that ended before the filter value.
- `AfterEndTime` - The supported `ValueList` is a list of all change sets that ended after the filter value.

(string)

Shorthand Syntax:

```
Name=string,ValueList=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "ValueList": ["string", ...]
  }
  ...
]
```

`--sort` (structure)

An object that contains two attributes, `SortBy` and `SortOrder` .

SortBy -> (string)

For `ListEntities` , supported attributes include `LastModifiedDate` (default) and `EntityId` . In addition to `LastModifiedDate` and `EntityId` , each `EntityType` might support additional fields.

For `ListChangeSets` , supported attributes include `StartTime` and `EndTime` .

SortOrder -> (string)

The sorting order. Can be `ASCENDING` or `DESCENDING` . The default value is `DESCENDING` .

Shorthand Syntax:

```
SortBy=string,SortOrder=string
```

JSON Syntax:

```
{
  "SortBy": "string",
  "SortOrder": "ASCENDING"|"DESCENDING"
}
```

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

ChangeSetSummaryList -> (list)

Array of `ChangeSetSummaryListItem` objects.

(structure)

A summary of a change set returned in a list of change sets when the `ListChangeSets` action is called.

ChangeSetId -> (string)

The unique identifier for a change set.

ChangeSetArn -> (string)

The ARN associated with the unique identifier for the change set referenced in this request.

ChangeSetName -> (string)

The non-unique name for the change set.

StartTime -> (string)

The time, in ISO 8601 format (2018-02-27T13:45:22Z), when the change set was started.

EndTime -> (string)

The time, in ISO 8601 format (2018-02-27T13:45:22Z), when the change set was finished.

Status -> (string)

The current status of the change set.

EntityIdList -> (list)

This object is a list of entity IDs (string) that are a part of a change set. The entity ID list is a maximum of 20 entities. It must contain at least one entity.

(string)

FailureCode -> (string)

Returned if the change set is in `FAILED` status. Can be either `CLIENT_ERROR` , which means that there are issues with the request (see the `ErrorDetailList` of `DescribeChangeSet` ), or `SERVER_FAULT` , which means that there is a problem in the system, and you should retry your request.

NextToken -> (string)

The value of the next token, if it exists. Null if there are no more results.