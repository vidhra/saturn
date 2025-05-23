# describe-db-engine-versionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-engine-versions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-engine-versions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/index.html#cli-aws-neptune) ]

# describe-db-engine-versions

## Description

Returns a list of the available DB engines.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBEngineVersions)

`describe-db-engine-versions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `DBEngineVersions`

## Synopsis

```
describe-db-engine-versions
[--engine <value>]
[--engine-version <value>]
[--db-parameter-group-family <value>]
[--filters <value>]
[--default-only | --no-default-only]
[--list-supported-character-sets | --no-list-supported-character-sets]
[--list-supported-timezones | --no-list-supported-timezones]
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

`--engine` (string)

The database engine to return.

`--engine-version` (string)

The database engine version to return.

Example: `5.1.49`

`--db-parameter-group-family` (string)

The name of a specific DB parameter group family to return details for.

Constraints:

- If supplied, must match an existing DBParameterGroupFamily.

`--filters` (list)

Not currently supported.

(structure)

This type is not currently supported.

Name -> (string)

This parameter is not currently supported.

Values -> (list)

This parameter is not currently supported.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--default-only` | `--no-default-only` (boolean)

Indicates that only the default version of the specified engine or engine and major version combination is returned.

`--list-supported-character-sets` | `--no-list-supported-character-sets` (boolean)

If this parameter is specified and the requested engine supports the `CharacterSetName` parameter for `CreateDBInstance` , the response includes a list of supported character sets for each engine version.

`--list-supported-timezones` | `--no-list-supported-timezones` (boolean)

If this parameter is specified and the requested engine supports the `TimeZone` parameter for `CreateDBInstance` , the response includes a list of supported time zones for each engine version.

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

Marker -> (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .

DBEngineVersions -> (list)

A list of `DBEngineVersion` elements.

(structure)

This data type is used as a response element in the action  DescribeDBEngineVersions .

Engine -> (string)

The name of the database engine.

EngineVersion -> (string)

The version number of the database engine.

DBParameterGroupFamily -> (string)

The name of the DB parameter group family for the database engine.

DBEngineDescription -> (string)

The description of the database engine.

DBEngineVersionDescription -> (string)

The description of the database engine version.

DefaultCharacterSet -> (structure)

*(Not supported by Neptune)*

CharacterSetName -> (string)

The name of the character set.

CharacterSetDescription -> (string)

The description of the character set.

SupportedCharacterSets -> (list)

*(Not supported by Neptune)*

(structure)

Specifies a character set.

CharacterSetName -> (string)

The name of the character set.

CharacterSetDescription -> (string)

The description of the character set.

ValidUpgradeTarget -> (list)

A list of engine versions that this database engine version can be upgraded to.

(structure)

The version of the database engine that a DB instance can be upgraded to.

Engine -> (string)

The name of the upgrade target database engine.

EngineVersion -> (string)

The version number of the upgrade target database engine.

Description -> (string)

The version of the database engine that a DB instance can be upgraded to.

AutoUpgrade -> (boolean)

A value that indicates whether the target version is applied to any source DB instances that have AutoMinorVersionUpgrade set to true.

IsMajorVersionUpgrade -> (boolean)

A value that indicates whether a database engine is upgraded to a major version.

SupportsGlobalDatabases -> (boolean)

A value that indicates whether you can use Neptune global databases with the target engine version.

SupportedTimezones -> (list)

A list of the time zones supported by this engine for the `Timezone` parameter of the `CreateDBInstance` action.

(structure)

A time zone associated with a  DBInstance .

TimezoneName -> (string)

The name of the time zone.

ExportableLogTypes -> (list)

The types of logs that the database engine has available for export to CloudWatch Logs.

(string)

SupportsLogExportsToCloudwatchLogs -> (boolean)

A value that indicates whether the engine version supports exporting the log types specified by ExportableLogTypes to CloudWatch Logs.

SupportsReadReplica -> (boolean)

Indicates whether the database engine version supports read replicas.

SupportsGlobalDatabases -> (boolean)

A value that indicates whether you can use Aurora global databases with a specific DB engine version.