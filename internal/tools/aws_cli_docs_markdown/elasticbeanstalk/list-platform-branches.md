# list-platform-branchesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/list-platform-branches.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/list-platform-branches.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# list-platform-branches

## Description

Lists the platform branches available for your account in an AWS Region. Provides summary information about each platform branch.

For definitions of platform branch and other platform-related terms, see [AWS Elastic Beanstalk Platforms Glossary](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/ListPlatformBranches)

## Synopsis

```
list-platform-branches
[--filters <value>]
[--max-records <value>]
[--next-token <value>]
[--cli-input-json | --cli-input-yaml]
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

Criteria for restricting the resulting list of platform branches. The filter is evaluated as a logical conjunction (AND) of the separate `SearchFilter` terms.

The following list shows valid attribute values for each of the `SearchFilter` terms. Most operators take a single value. The `in` and `not_in` operators can take multiple values.

- `Attribute = BranchName` :
- `Operator` : `=` | `!=` | `begins_with` | `ends_with` | `contains` | `in` | `not_in`
- `Attribute = LifecycleState` :
- `Operator` : `=` | `!=` | `in` | `not_in`
- `Values` : `beta` | `supported` | `deprecated` | `retired`
- `Attribute = PlatformName` :
- `Operator` : `=` | `!=` | `begins_with` | `ends_with` | `contains` | `in` | `not_in`
- `Attribute = TierType` :
- `Operator` : `=` | `!=`
- `Values` : `WebServer/Standard` | `Worker/SQS/HTTP`

Array size: limited to 10 `SearchFilter` objects.

Within each `SearchFilter` item, the `Values` array is limited to 10 items.

(structure)

Describes criteria to restrict a list of results.

For operators that apply a single value to the attribute, the filter is evaluated as follows: `Attribute Operator Values[1]`

Some operators, e.g. `in` , can apply multiple values. In this case, the filter is evaluated as a logical union (OR) of applications of the operator to the attribute with each one of the values: `(Attribute Operator Values[1]) OR (Attribute Operator Values[2]) OR ...`

The valid values for attributes of `SearchFilter` depend on the API action. For valid values, see the reference page for the API action youâre calling that takes a `SearchFilter` parameter.

Attribute -> (string)

The result attribute to which the filter values are applied. Valid values vary by API action.

Operator -> (string)

The operator to apply to the `Attribute` with each of the `Values` . Valid values vary by `Attribute` .

Values -> (list)

The list of values applied to the `Attribute` and `Operator` attributes. Number of values and valid values vary by `Attribute` .

(string)

Shorthand Syntax:

```
Attribute=string,Operator=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Attribute": "string",
    "Operator": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--max-records` (integer)

The maximum number of platform branch values returned in one call.

`--next-token` (string)

For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.

If no `NextToken` is specified, the first page is retrieved.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

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

PlatformBranchSummaryList -> (list)

Summary information about the platform branches.

(structure)

Summary information about a platform branch.

PlatformName -> (string)

The name of the platform to which this platform branch belongs.

BranchName -> (string)

The name of the platform branch.

LifecycleState -> (string)

The support life cycle state of the platform branch.

Possible values: `beta` | `supported` | `deprecated` | `retired`

BranchOrder -> (integer)

An ordinal number that designates the order in which platform branches have been added to a platform. This can be helpful, for example, if your code calls the `ListPlatformBranches` action and then displays a list of platform branches.

A larger `BranchOrder` value designates a newer platform branch within the platform.

SupportedTierList -> (list)

The environment tiers that platform versions in this branch support.

Possible values: `WebServer/Standard` | `Worker/SQS/HTTP`

(string)

NextToken -> (string)

In a paginated request, if this value isnât `null` , itâs the token that you can pass in a subsequent request to get the next response page.