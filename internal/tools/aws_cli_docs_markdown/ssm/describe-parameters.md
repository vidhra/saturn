# describe-parametersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-parameters.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-parameters.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# describe-parameters

## Description

Lists the parameters in your Amazon Web Services account or the parameters shared with you when you enable the [Shared](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html#systemsmanager-DescribeParameters-request-Shared) option.

Request results are returned on a best-effort basis. If you specify `MaxResults` in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of `MaxResults` . If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a `NextToken` . You can specify the `NextToken` in a subsequent call to get the next set of results.

### Warning

If you change the KMS key alias for the KMS key used to encrypt a parameter, then you must also update the key alias the parameter uses to reference KMS. Otherwise, `DescribeParameters` retrieves whatever the original key alias was referencing.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeParameters)

`describe-parameters` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Parameters`

## Synopsis

```
describe-parameters
[--filters <value>]
[--parameter-filters <value>]
[--shared | --no-shared]
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

This data type is deprecated. Instead, use `ParameterFilters` .

(structure)

This data type is deprecated. Instead, use  ParameterStringFilter .

Key -> (string)

The name of the filter.

Values -> (list)

The filter values.

(string)

Shorthand Syntax:

```
Key=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Key": "Name"|"Type"|"KeyId",
    "Values": ["string", ...]
  }
  ...
]
```

`--parameter-filters` (list)

Filters to limit the request results.

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

`--shared` | `--no-shared` (boolean)

Lists parameters that are shared with you.

### Note

By default when using this option, the command returns parameters that have been shared using a standard Resource Access Manager Resource Share. In order for a parameter that was shared using the  PutResourcePolicy command to be returned, the associated `RAM Resource Share Created From Policy` must have been promoted to a standard Resource Share using the RAM [PromoteResourceShareCreatedFromPolicy](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html) API operation.

For more information about sharing parameters, see [Working with shared parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html) in the *Amazon Web Services Systems Manager User Guide* .

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

**Example 1: To list all parameters**

The following `describe-parameters` example lists all parameters in the current AWS account and Region.

```
aws ssm describe-parameters
```

Output:

```
{
    "Parameters": [
        {
            "Name": "MySecureStringParameter",
            "Type": "SecureString",
            "KeyId": "alias/aws/ssm",
            "LastModifiedDate": 1582155479.205,
            "LastModifiedUser": "arn:aws:sts::111222333444:assumed-role/Admin/Richard-Roe-Managed",
            "Description": "This is a SecureString parameter",
            "Version": 2,
            "Tier": "Advanced",
            "Policies": [
                {
                    "PolicyText": "{\"Type\":\"Expiration\",\"Version\":\"1.0\",\"Attributes\":{\"Timestamp\":\"2020-07-07T22:30:00Z\"}}",
                    "PolicyType": "Expiration",
                    "PolicyStatus": "Pending"
                },
                {
                    "PolicyText": "{\"Type\":\"ExpirationNotification\",\"Version\":\"1.0\",\"Attributes\":{\"Before\":\"12\",\"Unit\":\"Hours\"}}",
                    "PolicyType": "ExpirationNotification",
                    "PolicyStatus": "Pending"
                }
            ]
        },
        {
            "Name": "MyStringListParameter",
            "Type": "StringList",
            "LastModifiedDate": 1582154764.222,
            "LastModifiedUser": "arn:aws:iam::111222333444:user/Mary-Major",
            "Description": "This is a StringList parameter",
            "Version": 1,
            "Tier": "Standard",
            "Policies": []
        },
        {
            "Name": "MyStringParameter",
            "Type": "String",
            "LastModifiedDate": 1582154711.976,
            "LastModifiedUser": "arn:aws:iam::111222333444:user/Alejandro-Rosalez",
            "Description": "This is a String parameter",
            "Version": 1,
            "Tier": "Standard",
            "Policies": []
        },
        {
            "Name": "latestAmi",
            "Type": "String",
            "LastModifiedDate": 1580862415.521,
            "LastModifiedUser": "arn:aws:sts::111222333444:assumed-role/lambda-ssm-role/Automation-UpdateSSM-Param",
            "Version": 3,
            "Tier": "Standard",
            "Policies": []
        }
    ]
}
```

**Example 2: To list all parameters matching specific metadata**

This `describe-parameters` example lists all parameters matching a filter.

**aws ssm describe-parameters**:
âfilters âKey=Type,Values=StringListâ

Output:

```
{
    "Parameters": [
        {
            "Name": "MyStringListParameter",
            "Type": "StringList",
            "LastModifiedDate": 1582154764.222,
            "LastModifiedUser": "arn:aws:iam::111222333444:user/Mary-Major",
            "Description": "This is a StringList parameter",
            "Version": 1,
            "Tier": "Standard",
            "Policies": []
        }
    ]
}
```

For more information, see [Searching for Systems Manager Parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-search.html) in the *AWS Systems Manager User Guide*.

## Output

Parameters -> (list)

Parameters returned by the request.

(structure)

Metadata includes information like the Amazon Resource Name (ARN) of the last user to update the parameter and the date and time the parameter was last used.

Name -> (string)

The parameter name.

ARN -> (string)

The Amazon Resource Name (ARN) of the parameter.

Type -> (string)

The type of parameter. Valid parameter types include the following: `String` , `StringList` , and `SecureString` .

KeyId -> (string)

The alias of the Key Management Service (KMS) key used to encrypt the parameter. Applies to `SecureString` parameters only.

LastModifiedDate -> (timestamp)

Date the parameter was last changed or updated.

LastModifiedUser -> (string)

Amazon Resource Name (ARN) of the Amazon Web Services user who last changed the parameter.

Description -> (string)

Description of the parameter actions.

AllowedPattern -> (string)

A parameter name can include only the following letters and symbols.

[a-zA-Z0-9_](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-parameters.html#id1).-

Version -> (long)

The parameter version.

Tier -> (string)

The parameter tier.

Policies -> (list)

A list of policies associated with a parameter.

(structure)

One or more policies assigned to a parameter.

PolicyText -> (string)

The JSON text of the policy.

PolicyType -> (string)

The type of policy. Parameter Store, a tool in Amazon Web Services Systems Manager, supports the following policy types: Expiration, ExpirationNotification, and NoChangeNotification.

PolicyStatus -> (string)

The status of the policy. Policies report the following statuses: Pending (the policy hasnât been enforced or applied yet), Finished (the policy was applied), Failed (the policy wasnât applied), or InProgress (the policy is being applied now).

DataType -> (string)

The data type of the parameter, such as `text` or `aws:ec2:image` . The default is `text` .

NextToken -> (string)

The token to use when requesting the next set of items.