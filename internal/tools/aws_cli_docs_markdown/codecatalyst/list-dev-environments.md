# list-dev-environmentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-dev-environments.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-dev-environments.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codecatalyst](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/index.html#cli-aws-codecatalyst) ]

# list-dev-environments

## Description

Retrieves a list of Dev Environments in a project.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codecatalyst-2022-09-28/ListDevEnvironments)

`list-dev-environments` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `items`

## Synopsis

```
list-dev-environments
--space-name <value>
[--project-name <value>]
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

`--space-name` (string)

The name of the space.

`--project-name` (string)

The name of the project in the space.

`--filters` (list)

Information about filters to apply to narrow the results returned in the list.

(structure)

Information about a filter used to limit results of a query.

key -> (string)

A key that can be used to sort results.

values -> (list)

The values of the key.

(string)

comparisonOperator -> (string)

The operator used to compare the fields.

Shorthand Syntax:

```
key=string,values=string,string,comparisonOperator=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "values": ["string", ...],
    "comparisonOperator": "string"
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

items -> (list)

Information about the Dev Environments in a project.

(structure)

Information about a Dev Environment.

spaceName -> (string)

The name of the space.

projectName -> (string)

The name of the project in the space.

id -> (string)

The system-generated unique ID for the Dev Environment.

lastUpdatedTime -> (timestamp)

The time when the Dev Environment was last updated, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6) .

creatorId -> (string)

The system-generated unique ID of the user who created the Dev Environment.

status -> (string)

The status of the Dev Environment.

statusReason -> (string)

The reason for the status.

repositories -> (list)

Information about the repositories that will be cloned into the Dev Environment. If no rvalue is specified, no repository is cloned.

(structure)

Information about the source repsitory for a Dev Environment.

repositoryName -> (string)

The name of the source repository.

branchName -> (string)

The name of the branch in a source repository cloned into the Dev Environment.

alias -> (string)

The user-specified alias for the Dev Environment.

ides -> (list)

Information about the integrated development environment (IDE) configured for a Dev Environment.

(structure)

Information about an integrated development environment (IDE) used in a Dev Environment.

runtime -> (string)

A link to the IDE runtime image.

name -> (string)

The name of the IDE.

instanceType -> (string)

The Amazon EC2 instace type used for the Dev Environment.

inactivityTimeoutMinutes -> (integer)

The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. Dev Environments consume compute minutes when running.

persistentStorage -> (structure)

Information about the configuration of persistent storage for the Dev Environment.

sizeInGiB -> (integer)

The size of the persistent storage in gigabytes (specifically GiB).

### Note

Valid values for storage are based on memory sizes in 16GB increments. Valid values are 16, 32, and 64.

vpcConnectionName -> (string)

The name of the connection used to connect to Amazon VPC used when the Dev Environment was created, if any.

nextToken -> (string)

A token returned from a call to this API to indicate the next batch of results to return, if any.