# list-configuration-managersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-quicksetup/list-configuration-managers.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-quicksetup/list-configuration-managers.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm-quicksetup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-quicksetup/index.html#cli-aws-ssm-quicksetup) ]

# list-configuration-managers

## Description

Returns Quick Setup configuration managers.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-quicksetup-2018-05-10/ListConfigurationManagers)

`list-configuration-managers` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ConfigurationManagersList`

## Synopsis

```
list-configuration-managers
[--filters <value>]
[--max-items <value>]
[--starting-token <value>]
[--cli-input-json | --cli-input-yaml]
[--page-size <value>]
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

Filters the results returned by the request.

(structure)

A key-value pair to filter results.

Key -> (string)

The key for the filter.

Values -> (list)

The values for the filter keys.

(string)

Shorthand Syntax:

```
Key=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

ConfigurationManagersList -> (list)

The configuration managers returned by the request.

(structure)

A summary of a Quick Setup configuration manager.

ConfigurationDefinitionSummaries -> (list)

A summary of the Quick Setup configuration definition.

(structure)

A summarized definition of a Quick Setup configuration definition.

FirstClassParameters -> (map)

The common parameters and values for the configuration definition.

key -> (string)

value -> (string)

Id -> (string)

The ID of the configuration definition.

Type -> (string)

The type of the Quick Setup configuration used by the configuration definition.

TypeVersion -> (string)

The version of the Quick Setup type used by the configuration definition.

Description -> (string)

The description of the configuration.

ManagerArn -> (string)

The ARN of the Quick Setup configuration.

Name -> (string)

The name of the configuration

StatusSummaries -> (list)

Summaries of the state of the configuration manager. These summaries include an aggregate of the statuses from the configuration definition associated with the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.

(structure)

A summarized description of the status.

LastUpdatedAt -> (timestamp)

The datetime stamp when the status was last updated.

Status -> (string)

The current status.

StatusDetails -> (map)

Details about the status.

key -> (string)

value -> (string)

StatusMessage -> (string)

When applicable, returns an informational message relevant to the current status and status type of the status summary object. We donât recommend implementing parsing logic around this value since the messages returned can vary in format.

StatusType -> (string)

The type of a status summary.

NextToken -> (string)

The token to use when requesting the next set of configuration managers. If there are no additional operations to return, the string is empty.