# backtrack-db-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/backtrack-db-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/backtrack-db-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# backtrack-db-cluster

## Description

Backtracks a DB cluster to a specific time, without creating a new DB cluster.

For more information on backtracking, see [Backtracking an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html) in the *Amazon Aurora User Guide* .

### Note

This action applies only to Aurora MySQL DB clusters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/BacktrackDBCluster)

## Synopsis

```
backtrack-db-cluster
--db-cluster-identifier <value>
--backtrack-to <value>
[--force | --no-force]
[--use-earliest-time-on-point-in-time-unavailable | --no-use-earliest-time-on-point-in-time-unavailable]
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

`--db-cluster-identifier` (string)

The DB cluster identifier of the DB cluster to be backtracked. This parameter is stored as a lowercase string.

Constraints:

- Must contain from 1 to 63 alphanumeric characters or hyphens.
- First character must be a letter.
- Canât end with a hyphen or contain two consecutive hyphens.

Example: `my-cluster1`

`--backtrack-to` (timestamp)

The timestamp of the time to backtrack the DB cluster to, specified in ISO 8601 format. For more information about ISO 8601, see the [ISO8601 Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)

### Note

If the specified time isnât a consistent time for the DB cluster, Aurora automatically chooses the nearest possible consistent time for the DB cluster.

Constraints:

- Must contain a valid ISO 8601 timestamp.
- Canât contain a timestamp set in the future.

Example: `2017-07-08T18:00Z`

`--force` | `--no-force` (boolean)

Specifies whether to force the DB cluster to backtrack when binary logging is enabled. Otherwise, an error occurs when binary logging is enabled.

`--use-earliest-time-on-point-in-time-unavailable` | `--no-use-earliest-time-on-point-in-time-unavailable` (boolean)

Specifies whether to backtrack the DB cluster to the earliest possible backtrack time when *BacktrackTo* is set to a timestamp earlier than the earliest backtrack time. When this parameter is disabled and *BacktrackTo* is set to a timestamp earlier than the earliest backtrack time, an error occurs.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To backtrack an Aurora DB cluster**

The following `backtrack-db-cluster` example backtracks the specified DB cluster sample-cluster to March 19, 2018, at 10 a.m.

```
aws rds backtrack-db-cluster --db-cluster-identifier sample-cluster --backtrack-to 2018-03-19T10:00:00+00:00
```

This command outputs a JSON block that acknowledges the change to the RDS resource.

## Output

DBClusterIdentifier -> (string)

Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

BacktrackIdentifier -> (string)

Contains the backtrack identifier.

BacktrackTo -> (timestamp)

The timestamp of the time to which the DB cluster was backtracked.

BacktrackedFrom -> (timestamp)

The timestamp of the time from which the DB cluster was backtracked.

BacktrackRequestCreationTime -> (timestamp)

The timestamp of the time at which the backtrack was requested.

Status -> (string)

The status of the backtrack. This property returns one of the following values:

- `applying` - The backtrack is currently being applied to or rolled back from the DB cluster.
- `completed` - The backtrack has successfully been applied to or rolled back from the DB cluster.
- `failed` - An error occurred while the backtrack was applied to or rolled back from the DB cluster.
- `pending` - The backtrack is currently pending application to or rollback from the DB cluster.