# list-linux-subscription-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-linux-subscriptions/list-linux-subscription-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-linux-subscriptions/list-linux-subscription-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [license-manager-linux-subscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-linux-subscriptions/index.html#cli-aws-license-manager-linux-subscriptions) ]

# list-linux-subscription-instances

## Description

Lists the running Amazon EC2 instances that were discovered with commercial Linux subscriptions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/license-manager-linux-subscriptions-2018-05-10/ListLinuxSubscriptionInstances)

`list-linux-subscription-instances` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Instances`

## Synopsis

```
list-linux-subscription-instances
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

An array of structures that you can use to filter the results by your specified criteria. For example, you can specify `Region` in the `Name` , with the `contains` operator to list all subscriptions that match a partial string in the `Value` , such as `us-west` .

For each filter, you can specify one of the following values for the `Name` key to streamline results:

- `AccountID`
- `AmiID`
- `DualSubscription`
- `InstanceID`
- `InstanceType`
- `ProductCode`
- `Region`
- `Status`
- `UsageOperation`

For each filter, you can use one of the following `Operator` values to define the behavior of the filter:

- `contains`
- `equals`
- `Notequal`

(structure)

A filter object that is used to return more specific results from a describe operation. Filters can be used to match a set of resources by specific criteria.

Name -> (string)

The type of name to filter by.

Operator -> (string)

An operator for filtering results.

Values -> (list)

One or more values for the name to filter by.

(string)

Shorthand Syntax:

```
Name=string,Operator=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Operator": "Equal"|"NotEqual"|"Contains",
    "Values": ["string", ...]
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

Instances -> (list)

An array that contains instance objects.

(structure)

Details discovered information about a running instance using Linux subscriptions.

AccountID -> (string)

The account ID which owns the instance.

AmiId -> (string)

The AMI ID used to launch the instance.

DualSubscription -> (string)

Indicates that you have two different license subscriptions for the same software on your instance.

InstanceID -> (string)

The instance ID of the resource.

InstanceType -> (string)

The instance type of the resource.

LastUpdatedTime -> (string)

The time in which the last discovery updated the instance details.

OsVersion -> (string)

The operating system software version that runs on your instance.

ProductCode -> (list)

The product code for the instance. For more information, see [Usage operation values](https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions-usage-operation.html) in the *License Manager User Guide* .

(string)

Region -> (string)

The Region the instance is running in.

RegisteredWithSubscriptionProvider -> (string)

Indicates that your instance uses a BYOL license subscription from a third-party Linux subscription provider that youâve registered with License Manager.

Status -> (string)

The status of the instance.

SubscriptionName -> (string)

The name of the license subscription that the instance uses.

SubscriptionProviderCreateTime -> (string)

The timestamp when you registered the third-party Linux subscription provider for the subscription that the instance uses.

SubscriptionProviderUpdateTime -> (string)

The timestamp from the last time that the instance synced with the registered third-party Linux subscription provider.

UsageOperation -> (string)

The usage operation of the instance. For more information, see For more information, see [Usage operation values](https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions-usage-operation.html) in the *License Manager User Guide* .

NextToken -> (string)

The next token used for paginated responses. When this field isnât empty, there are additional elements that the service hasnât included in this request. Use this token with the next request to retrieve additional objects.