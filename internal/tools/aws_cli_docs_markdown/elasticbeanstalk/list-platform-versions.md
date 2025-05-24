# list-platform-versionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/list-platform-versions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/list-platform-versions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# list-platform-versions

## Description

Lists the platform versions available for your account in an AWS Region. Provides summary information about each platform version. Compare to  DescribePlatformVersion , which provides full details about a single platform version.

For definitions of platform version and other platform-related terms, see [AWS Elastic Beanstalk Platforms Glossary](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/ListPlatformVersions)

`list-platform-versions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `PlatformSummaryList`

## Synopsis

```
list-platform-versions
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

Criteria for restricting the resulting list of platform versions. The filter is interpreted as a logical conjunction (AND) of the separate `PlatformFilter` terms.

(structure)

Describes criteria to restrict the results when listing platform versions.

The filter is evaluated as follows: `Type Operator Values[1]`

Type -> (string)

The platform version attribute to which the filter values are applied.

Valid values: `PlatformName` | `PlatformVersion` | `PlatformStatus` | `PlatformBranchName` | `PlatformLifecycleState` | `PlatformOwner` | `SupportedTier` | `SupportedAddon` | `ProgrammingLanguageName` | `OperatingSystemName`

Operator -> (string)

The operator to apply to the `Type` with each of the `Values` .

Valid values: `=` | `!=` | `<` | `<=` | `>` | `>=` | `contains` | `begins_with` | `ends_with`

Values -> (list)

The list of values applied to the filtering platform version attribute. Only one value is supported for all current operators.

The following list shows valid filter values for some filter attributes.

- `PlatformStatus` : `Creating` | `Failed` | `Ready` | `Deleting` | `Deleted`
- `PlatformLifecycleState` : `recommended`
- `SupportedTier` : `WebServer/Standard` | `Worker/SQS/HTTP`
- `SupportedAddon` : `Log/S3` | `Monitoring/Healthd` | `WorkerDaemon/SQSD`

(string)

Shorthand Syntax:

```
Type=string,Operator=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Type": "string",
    "Operator": "string",
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

PlatformSummaryList -> (list)

Summary information about the platform versions.

(structure)

Summary information about a platform version.

PlatformArn -> (string)

The ARN of the platform version.

PlatformOwner -> (string)

The AWS account ID of the person who created the platform version.

PlatformStatus -> (string)

The status of the platform version. You can create an environment from the platform version once it is ready.

PlatformCategory -> (string)

The category of platform version.

OperatingSystemName -> (string)

The operating system used by the platform version.

OperatingSystemVersion -> (string)

The version of the operating system used by the platform version.

SupportedTierList -> (list)

The tiers in which the platform version runs.

(string)

SupportedAddonList -> (list)

The additions associated with the platform version.

(string)

PlatformLifecycleState -> (string)

The state of the platform version in its lifecycle.

Possible values: `recommended` | empty

If an empty value is returned, the platform version is supported but isnât the recommended one for its branch.

PlatformVersion -> (string)

The version string of the platform version.

PlatformBranchName -> (string)

The platform branch to which the platform version belongs.

PlatformBranchLifecycleState -> (string)

The state of the platform versionâs branch in its lifecycle.

Possible values: `beta` | `supported` | `deprecated` | `retired`

NextToken -> (string)

In a paginated request, if this value isnât `null` , itâs the token that you can pass in a subsequent request to get the next response page.