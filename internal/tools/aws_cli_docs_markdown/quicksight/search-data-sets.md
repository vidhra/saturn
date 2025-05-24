# search-data-setsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/search-data-sets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/search-data-sets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# search-data-sets

## Description

Use the `SearchDataSets` operation to search for datasets that belong to an account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/SearchDataSets)

`search-data-sets` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `DataSetSummaries`

## Synopsis

```
search-data-sets
--aws-account-id <value>
--filters <value>
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

`--aws-account-id` (string)

The Amazon Web Services account ID.

`--filters` (list)

The filters to apply to the search.

(structure)

A filter that you apply when searching for datasets.

Operator -> (string)

The comparison operator that you want to use as a filter, for example `"Operator": "StringEquals"` . Valid values are `"StringEquals"` and `"StringLike"` .

If you set the operator value to `"StringEquals"` , you need to provide an ownership related filter in the `"NAME"` field and the arn of the user or group whose datasets you want to search in the `"Value"` field. For example, `"Name":"QUICKSIGHT_OWNER", "Operator": "StringEquals", "Value": "arn:aws:quicksight:us-east- 1:1:user/default/UserName1"` .

If you set the value to `"StringLike"` , you need to provide the name of the datasets you are searching for. For example, `"Name":"DATASET_NAME", "Operator": "StringLike", "Value": "Test"` . The `"StringLike"` operator only supports the `NAME` value `DATASET_NAME` .

Name -> (string)

The name of the value that you want to use as a filter, for example, `"Name": "QUICKSIGHT_OWNER"` .

Valid values are defined as follows:

- `QUICKSIGHT_VIEWER_OR_OWNER` : Provide an ARN of a user or group, and any datasets with that ARN listed as one of the dataset owners or viewers are returned. Implicit permissions from folders or groups are considered.
- `QUICKSIGHT_OWNER` : Provide an ARN of a user or group, and any datasets with that ARN listed as one of the owners of the dataset are returned. Implicit permissions from folders or groups are considered.
- `DIRECT_QUICKSIGHT_SOLE_OWNER` : Provide an ARN of a user or group, and any datasets with that ARN listed as the only owner of the dataset are returned. Implicit permissions from folders or groups are not considered.
- `DIRECT_QUICKSIGHT_OWNER` : Provide an ARN of a user or group, and any datasets with that ARN listed as one of the owners if the dataset are returned. Implicit permissions from folders or groups are not considered.
- `DIRECT_QUICKSIGHT_VIEWER_OR_OWNER` : Provide an ARN of a user or group, and any datasets with that ARN listed as one of the owners or viewers of the dataset are returned. Implicit permissions from folders or groups are not considered.
- `DATASET_NAME` : Any datasets whose names have a substring match to this value will be returned.

Value -> (string)

The value of the named item, in this case `QUICKSIGHT_OWNER` , that you want to use as a filter, for example, `"Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1"` .

Shorthand Syntax:

```
Operator=string,Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Operator": "StringEquals"|"StringLike",
    "Name": "QUICKSIGHT_VIEWER_OR_OWNER"|"QUICKSIGHT_OWNER"|"DIRECT_QUICKSIGHT_VIEWER_OR_OWNER"|"DIRECT_QUICKSIGHT_OWNER"|"DIRECT_QUICKSIGHT_SOLE_OWNER"|"DATASET_NAME",
    "Value": "string"
  }
  ...
]
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

DataSetSummaries -> (list)

A `DataSetSummaries` object that returns a summary of a dataset.

(structure)

Dataset summary.

Arn -> (string)

The Amazon Resource Name (ARN) of the dataset.

DataSetId -> (string)

The ID of the dataset.

Name -> (string)

A display name for the dataset.

CreatedTime -> (timestamp)

The time that this dataset was created.

LastUpdatedTime -> (timestamp)

The last time that this dataset was updated.

ImportMode -> (string)

A value that indicates whether you want to import the data into SPICE.

RowLevelPermissionDataSet -> (structure)

The row-level security configuration for the dataset.

Namespace -> (string)

The namespace associated with the dataset that contains permissions for RLS.

Arn -> (string)

The Amazon Resource Name (ARN) of the dataset that contains permissions for RLS.

PermissionPolicy -> (string)

The type of permissions to use when interpreting the permissions for RLS. `DENY_ACCESS` is included for backward compatibility only.

FormatVersion -> (string)

The user or group rules associated with the dataset that contains permissions for RLS.

By default, `FormatVersion` is `VERSION_1` . When `FormatVersion` is `VERSION_1` , `UserName` and `GroupName` are required. When `FormatVersion` is `VERSION_2` , `UserARN` and `GroupARN` are required, and `Namespace` must not exist.

Status -> (string)

The status of the row-level security permission dataset. If enabled, the status is `ENABLED` . If disabled, the status is `DISABLED` .

RowLevelPermissionTagConfigurationApplied -> (boolean)

Whether or not the row level permission tags are applied.

ColumnLevelPermissionRulesApplied -> (boolean)

A value that indicates if the dataset has column level permission configured.

UseAs -> (string)

The usage of the dataset.

NextToken -> (string)

A pagination token that can be used in a subsequent request.

Status -> (integer)

The HTTP status of the request.

RequestId -> (string)

The Amazon Web Services request ID for this operation.