# list-service-level-objectivesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-signals/list-service-level-objectives.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-signals/list-service-level-objectives.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [application-signals](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-signals/index.html#cli-aws-application-signals) ]

# list-service-level-objectives

## Description

Returns a list of SLOs created in this account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/application-signals-2024-04-15/ListServiceLevelObjectives)

`list-service-level-objectives` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `SloSummaries`

## Synopsis

```
list-service-level-objectives
[--key-attributes <value>]
[--operation-name <value>]
[--dependency-config <value>]
[--metric-source-types <value>]
[--include-linked-accounts | --no-include-linked-accounts]
[--slo-owner-aws-account-id <value>]
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

`--key-attributes` (map)

You can use this optional field to specify which services you want to retrieve SLO information for.

This is a string-to-string map. It can include the following fields.

- `Type` designates the type of object this is.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--operation-name` (string)

The name of the operation that this SLO is associated with.

`--dependency-config` (structure)

Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName` .

DependencyKeyAttributes -> (map)

This is a string-to-string map. It can include the following fields.

- `Type` designates the type of object this is.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

DependencyOperationName -> (string)

The name of the called operation in the dependency.

Shorthand Syntax:

```
DependencyKeyAttributes={KeyName1=string,KeyName2=string},DependencyOperationName=string
```

JSON Syntax:

```
{
  "DependencyKeyAttributes": {"string": "string"
    ...},
  "DependencyOperationName": "string"
}
```

`--metric-source-types` (list)

Use this optional field to only include SLOs with the specified metric source types in the output. Supported types are:

- Service operation
- Service dependency
- CloudWatch metric

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  ServiceOperation
  CloudWatchMetric
  ServiceDependency
```

`--include-linked-accounts` | `--no-include-linked-accounts` (boolean)

If you are using this operation in a monitoring account, specify `true` to include SLO from source accounts in the returned data. `</p> <p>When you are monitoring an account, you can use Amazon Web Services account ID in <code>KeyAttribute</code> filter for service source account and <code>SloOwnerawsaccountID</code> for SLO source account with <code>IncludeLinkedAccounts</code> to filter the returned data to only a single source account. </p>`

`--slo-owner-aws-account-id` (string)

SLOâs Amazon Web Services account ID.

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

SloSummaries -> (list)

An array of structures, where each structure contains information about one SLO.

(structure)

A structure that contains information about one service level objective (SLO) created in Application Signals.

Arn -> (string)

The ARN of this service level objective.

Name -> (string)

The name of the service level objective.

KeyAttributes -> (map)

This is a string-to-string map. It can include the following fields.

- `Type` designates the type of object this service level objective is for.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

OperationName -> (string)

If this service level objective is specific to a single operation, this field displays the name of that operation.

DependencyConfig -> (structure)

Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName` .

DependencyKeyAttributes -> (map)

This is a string-to-string map. It can include the following fields.

- `Type` designates the type of object this is.
- `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service` , `RemoteService` , or `AWS::Service` .
- `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource` .
- `Environment` specifies the location where this object is hosted, or what it belongs to.

key -> (string)

value -> (string)

DependencyOperationName -> (string)

The name of the called operation in the dependency.

CreatedTime -> (timestamp)

The date and time that this service level objective was created. It is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.

EvaluationType -> (string)

Displays whether this is a period-based SLO or a request-based SLO.

MetricSourceType -> (string)

Displays the SLI metric source type for this SLO. Supported types are:

- Service operation
- Service dependency
- CloudWatch metric

NextToken -> (string)

Include this value in your next use of this API to get next set of service level objectives.