# modify-current-db-cluster-capacityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-current-db-cluster-capacity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-current-db-cluster-capacity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# modify-current-db-cluster-capacity

## Description

Set the capacity of an Aurora Serverless v1 DB cluster to a specific value.

Aurora Serverless v1 scales seamlessly based on the workload on the DB cluster. In some cases, the capacity might not scale fast enough to meet a sudden change in workload, such as a large number of new transactions. Call `ModifyCurrentDBClusterCapacity` to set the capacity explicitly.

After this call sets the DB cluster capacity, Aurora Serverless v1 can automatically scale the DB cluster based on the cooldown period for scaling up and the cooldown period for scaling down.

For more information about Aurora Serverless v1, see [Using Amazon Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html) in the *Amazon Aurora User Guide* .

### Warning

If you call `ModifyCurrentDBClusterCapacity` with the default `TimeoutAction` , connections that prevent Aurora Serverless v1 from finding a scaling point might be dropped. For more information about scaling points, see [Autoscaling for Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.auto-scaling) in the *Amazon Aurora User Guide* .

### Note

This operation only applies to Aurora Serverless v1 DB clusters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/ModifyCurrentDBClusterCapacity)

## Synopsis

```
modify-current-db-cluster-capacity
--db-cluster-identifier <value>
[--capacity <value>]
[--seconds-before-timeout <value>]
[--timeout-action <value>]
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

The DB cluster identifier for the cluster being modified. This parameter isnât case-sensitive.

Constraints:

- Must match the identifier of an existing DB cluster.

`--capacity` (integer)

The DB cluster capacity.

When you change the capacity of a paused Aurora Serverless v1 DB cluster, it automatically resumes.

Constraints:

- For Aurora MySQL, valid capacity values are `1` , `2` , `4` , `8` , `16` , `32` , `64` , `128` , and `256` .
- For Aurora PostgreSQL, valid capacity values are `2` , `4` , `8` , `16` , `32` , `64` , `192` , and `384` .

`--seconds-before-timeout` (integer)

The amount of time, in seconds, that Aurora Serverless v1 tries to find a scaling point to perform seamless scaling before enforcing the timeout action. The default is 300.

Specify a value between 10 and 600 seconds.

`--timeout-action` (string)

The action to take when the timeout is reached, either `ForceApplyCapacityChange` or `RollbackCapacityChange` .

`ForceApplyCapacityChange` , the default, sets the capacity to the specified value as soon as possible.

`RollbackCapacityChange` ignores the capacity change if a scaling point isnât found in the timeout period.

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

**To scale the capacity of an Aurora Serverless DB cluster**

The following `modify-current-db-cluster-capacity` example scales the capacity of an Aurora Serverless DB cluster to 8.

```
aws rds modify-current-db-cluster-capacity \
    --db-cluster-identifier mydbcluster \
    --capacity 8
```

Output:

```
{
    "DBClusterIdentifier": "mydbcluster",
    "PendingCapacity": 8,
    "CurrentCapacity": 1,
    "SecondsBeforeTimeout": 300,
    "TimeoutAction": "ForceApplyCapacityChange"
}
```

For more information, see [Scaling Aurora Serverless v1 DB cluster capacity manually](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.setting-capacity.html) in the *Amazon Aurora User Guide*.

## Output

DBClusterIdentifier -> (string)

A user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

PendingCapacity -> (integer)

A value that specifies the capacity that the DB cluster scales to next.

CurrentCapacity -> (integer)

The current capacity of the DB cluster.

SecondsBeforeTimeout -> (integer)

The number of seconds before a call to `ModifyCurrentDBClusterCapacity` times out.

TimeoutAction -> (string)

The timeout action of a call to `ModifyCurrentDBClusterCapacity` , either `ForceApplyCapacityChange` or `RollbackCapacityChange` .