# get-parameters-by-pathÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameters-by-path.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameters-by-path.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# get-parameters-by-path

## Description

Retrieve information about one or more parameters under a specified level in a hierarchy.

Request results are returned on a best-effort basis. If you specify `MaxResults` in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of `MaxResults` . If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a `NextToken` . You can specify the `NextToken` in a subsequent call to get the next set of results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetParametersByPath)

`get-parameters-by-path` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Parameters`

## Synopsis

```
get-parameters-by-path
--path <value>
[--recursive | --no-recursive]
[--parameter-filters <value>]
[--with-decryption | --no-with-decryption]
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

`--path` (string)

The hierarchy for the parameter. Hierarchies start with a forward slash (/). The hierarchy is the parameter name except the last part of the parameter. For the API call to succeed, the last part of the parameter name canât be in the path. A parameter name hierarchy can have a maximum of 15 levels. Here is an example of a hierarchy: `/Finance/Prod/IAD/WinServ2016/license33`

`--recursive` | `--no-recursive` (boolean)

Retrieve all parameters within a hierarchy.

### Warning

If a user has access to a path, then the user can access all levels of that path. For example, if a user has permission to access path `/a` , then the user can also access `/a/b` . Even if a user has explicitly been denied access in IAM for parameter `/a/b` , they can still call the GetParametersByPath API operation recursively for `/a` and view `/a/b` .

`--parameter-filters` (list)

Filters to limit the request results.

### Note

The following `Key` values are supported for `GetParametersByPath` : `Type` , `KeyId` , and `Label` .

The following `Key` values arenât supported for `GetParametersByPath` : `tag` , `DataType` , `Name` , `Path` , and `Tier` .

(structure)

One or more filters. Use a filter to return a more specific list of results.

Key -> (string)

The name of the filter.

The `ParameterStringFilter` object is used by the  DescribeParameters and  GetParametersByPath API operations. However, not all of the pattern values listed for `Key` can be used with both operations.

For `DescribeParameters` , all of the listed patterns are valid except `Label` .

For `GetParametersByPath` , the following patterns listed for `Key` arenât valid: `tag` , `DataType` , `Name` , `Path` , and `Tier` .

For examples of Amazon Web Services CLI commands demonstrating valid parameter filter constructions, see [Searching for Systems Manager parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-search.html) in the *Amazon Web Services Systems Manager User Guide* .

Option -> (string)

For all filters used with  DescribeParameters , valid options include `Equals` and `BeginsWith` . The `Name` filter additionally supports the `Contains` option. (Exception: For filters using the key `Path` , valid options include `Recursive` and `OneLevel` .)

For filters used with  GetParametersByPath , valid options include `Equals` and `BeginsWith` . (Exception: For filters using `Label` as the Key name, the only valid option is `Equals` .)

Values -> (list)

The value you want to search for.

(string)

Shorthand Syntax:

```
Key=string,Option=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Option": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--with-decryption` | `--no-with-decryption` (boolean)

Retrieve all parameters in a hierarchy with their value decrypted.

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

**To list parameters in a specific path**

The following `get-parameters-by-path` example lists the parameters within the specified hierarchy.

```
aws ssm get-parameters-by-path \
    --path "/site/newyork/department/"
```

Output:

```
{
    "Parameters": [
        {
            "Name": "/site/newyork/department/marketing",
            "Type": "String",
            "Value": "Floor 2",
            "Version": 1,
            "LastModifiedDate": 1530018761.888,
            "ARN": "arn:aws:ssm:us-east-1:111222333444:parameter/site/newyork/department/marketing"
        },
        {
            "Name": "/site/newyork/department/infotech",
            "Type": "String",
            "Value": "Floor 3",
            "Version": 1,
            "LastModifiedDate": 1530018823.429,
            "ARN": "arn:aws:ssm:us-east-1:111222333444:parameter/site/newyork/department/infotech"
        },
        ...
    ]
}
```

For more information, see [Working with parameter hierarchies](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-hierarchies.html) in the *AWS Systems Manager User Guide*.

## Output

Parameters -> (list)

A list of parameters found in the specified hierarchy.

(structure)

An Amazon Web Services Systems Manager parameter in Parameter Store.

Name -> (string)

The name of the parameter.

Type -> (string)

The type of parameter. Valid values include the following: `String` , `StringList` , and `SecureString` .

### Note

If type is `StringList` , the system returns a comma-separated string with no spaces between commas in the `Value` field.

Value -> (string)

The parameter value.

### Note

If type is `StringList` , the system returns a comma-separated string with no spaces between commas in the `Value` field.

Version -> (long)

The parameter version.

Selector -> (string)

Either the version number or the label used to retrieve the parameter value. Specify selectors by using one of the following formats:

parameter_name:version

parameter_name:label

SourceResult -> (string)

Applies to parameters that reference information in other Amazon Web Services services. `SourceResult` is the raw result or response from the source.

LastModifiedDate -> (timestamp)

Date the parameter was last changed or updated and the parameter version was created.

ARN -> (string)

The Amazon Resource Name (ARN) of the parameter.

DataType -> (string)

The data type of the parameter, such as `text` or `aws:ec2:image` . The default is `text` .

NextToken -> (string)

The token for the next set of items to return. Use this token to get the next set of results.