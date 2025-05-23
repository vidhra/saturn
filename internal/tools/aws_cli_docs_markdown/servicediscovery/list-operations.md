# list-operationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-operations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-operations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicediscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/index.html#cli-aws-servicediscovery) ]

# list-operations

## Description

Lists operations that match the criteria that you specify.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListOperations)

`list-operations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Operations`

## Synopsis

```
list-operations
[--filters <value>]
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

`--filters` (list)

A complex type that contains specifications for the operations that you want to list, for example, operations that you started between a specified start date and end date.

If you specify more than one filter, an operation must match all filters to be returned by `ListOperations` .

(structure)

A complex type that lets you select the operations that you want to list.

Name -> (string)

Specify the operations that you want to get:

- **NAMESPACE_ID** : Gets operations related to specified namespaces.
- **SERVICE_ID** : Gets operations related to specified services.
- **STATUS** : Gets operations based on the status of the operations: `SUBMITTED` , `PENDING` , `SUCCEED` , or `FAIL` .
- **TYPE** : Gets specified types of operation.
- **UPDATE_DATE** : Gets operations that changed status during a specified date/time range.

Values -> (list)

Specify values that are applicable to the value that you specify for `Name` :

- **NAMESPACE_ID** : Specify one namespace ID.
- **SERVICE_ID** : Specify one service ID.
- **STATUS** : Specify one or more statuses: `SUBMITTED` , `PENDING` , `SUCCEED` , or `FAIL` .
- **TYPE** : Specify one or more of the following types: `CREATE_NAMESPACE` , `DELETE_NAMESPACE` , `UPDATE_SERVICE` , `REGISTER_INSTANCE` , or `DEREGISTER_INSTANCE` .
- **UPDATE_DATE** : Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value.

(string)

Condition -> (string)

The operator that you want to use to determine whether an operation matches the specified value. Valid values for condition include:

- `EQ` : When you specify `EQ` for the condition, you can specify only one value. `EQ` is supported for `NAMESPACE_ID` , `SERVICE_ID` , `STATUS` , and `TYPE` . `EQ` is the default condition and can be omitted.
- `IN` : When you specify `IN` for the condition, you can specify a list of one or more values. `IN` is supported for `STATUS` and `TYPE` . An operation must match one of the specified values to be returned in the response.
- `BETWEEN` : Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value. `BETWEEN` is supported for `UPDATE_DATE` .

Shorthand Syntax:

```
Name=string,Values=string,string,Condition=string ...
```

JSON Syntax:

```
[
  {
    "Name": "NAMESPACE_ID"|"SERVICE_ID"|"STATUS"|"TYPE"|"UPDATE_DATE",
    "Values": ["string", ...],
    "Condition": "EQ"|"IN"|"BETWEEN"|"BEGINS_WITH"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list operations that meet the specified criteria**

The following `list-operations` example lists operations that have a status of `PENDING` or `SUCCESS`.

```
aws servicediscovery list-operations \
    --service-id srv-e4anhexample0004 \
    --filters Name=STATUS,Condition=IN,Values=PENDING,SUCCESS
```

Output:

```
{
    "Operations": [
        {
            "Id": "76yy8ovhpdz0plmjzbsnqgnrqvpv2qdt-kexample",
            "Status": "SUCCESS"
        },
        {
            "Id": "prysnyzpji3u2ciy45nke83x2zanl7yk-dexample",
            "Status": "SUCCESS"
        },
        {
            "Id": "ko4ekftir7kzlbechsh7xvcdgcpk66gh-7example",
            "Status": "PENDING"
        }
    ]
}
```

For more information, see [What is AWS Cloud Map?](https://docs.aws.amazon.com/cloud-map/latest/dg/what-is-cloud-map.html) in the *AWS Cloud Map Developer Guide*.

## Output

Operations -> (list)

Summary information about the operations that match the specified criteria.

(structure)

A complex type that contains information about an operation that matches the criteria that you specified in a [ListOperations](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html) request.

Id -> (string)

The ID for an operation.

Status -> (string)

The status of the operation. Values include the following:

- **SUBMITTED** : This is the initial state immediately after you submit a request.
- **PENDING** : Cloud Map is performing the operation.
- **SUCCESS** : The operation succeeded.
- **FAIL** : The operation failed. For the failure reason, see `ErrorMessage` .

NextToken -> (string)

If the response contains `NextToken` , submit another `ListOperations` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.

### Note

Cloud Map gets `MaxResults` operations and then filters them based on the specified criteria. Itâs possible that no operations in the first `MaxResults` operations matched the specified criteria but that subsequent groups of `MaxResults` operations do contain operations that match the criteria.