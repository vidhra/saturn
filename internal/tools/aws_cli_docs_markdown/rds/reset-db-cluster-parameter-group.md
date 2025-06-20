# reset-db-cluster-parameter-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reset-db-cluster-parameter-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reset-db-cluster-parameter-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# reset-db-cluster-parameter-group

## Description

Modifies the parameters of a DB cluster parameter group to the default value. To reset specific parameters submit a list of the following: `ParameterName` and `ApplyMethod` . To reset the entire DB cluster parameter group, specify the `DBClusterParameterGroupName` and `ResetAllParameters` parameters.

When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to `pending-reboot` to take effect on the next DB instance restart or `RebootDBInstance` request. You must call `RebootDBInstance` for every DB instance in your DB cluster that you want the updated static parameter to apply to.

For more information on Amazon Aurora DB clusters, see [What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide* .

For more information on Multi-AZ DB clusters, see [Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.*

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/ResetDBClusterParameterGroup)

## Synopsis

```
reset-db-cluster-parameter-group
--db-cluster-parameter-group-name <value>
[--reset-all-parameters | --no-reset-all-parameters]
[--parameters <value>]
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

`--db-cluster-parameter-group-name` (string)

The name of the DB cluster parameter group to reset.

`--reset-all-parameters` | `--no-reset-all-parameters` (boolean)

Specifies whether to reset all parameters in the DB cluster parameter group to their default values. You canât use this parameter if there is a list of parameter names specified for the `Parameters` parameter.

`--parameters` (list)

A list of parameter names in the DB cluster parameter group to reset to the default values. You canât use this parameter if the `ResetAllParameters` parameter is enabled.

(structure)

This data type is used as a request parameter in the `ModifyDBParameterGroup` and `ResetDBParameterGroup` actions.

This data type is used as a response element in the `DescribeEngineDefaultParameters` and `DescribeDBParameters` actions.

ParameterName -> (string)

The name of the parameter.

ParameterValue -> (string)

The value of the parameter.

Description -> (string)

Provides a description of the parameter.

Source -> (string)

The source of the parameter value.

ApplyType -> (string)

Specifies the engine specific parameters type.

DataType -> (string)

Specifies the valid data type for the parameter.

AllowedValues -> (string)

Specifies the valid range of values for the parameter.

IsModifiable -> (boolean)

Indicates whether (`true` ) or not (`false` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion -> (string)

The earliest engine version to which the parameter can apply.

ApplyMethod -> (string)

Indicates when to apply parameter updates.

SupportedEngineModes -> (list)

The valid DB engine modes.

(string)

Shorthand Syntax:

```
ParameterName=string,ParameterValue=string,Description=string,Source=string,ApplyType=string,DataType=string,AllowedValues=string,IsModifiable=boolean,MinimumEngineVersion=string,ApplyMethod=string,SupportedEngineModes=string,string ...
```

JSON Syntax:

```
[
  {
    "ParameterName": "string",
    "ParameterValue": "string",
    "Description": "string",
    "Source": "string",
    "ApplyType": "string",
    "DataType": "string",
    "AllowedValues": "string",
    "IsModifiable": true|false,
    "MinimumEngineVersion": "string",
    "ApplyMethod": "immediate"|"pending-reboot",
    "SupportedEngineModes": ["string", ...]
  }
  ...
]
```

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

**Example 1: To reset all parameters to their default values**

The following `reset-db-cluster-parameter-group` example resets all parameter values in a customer-created DB cluster parameter group to their default values.

```
aws rds reset-db-cluster-parameter-group \
    --db-cluster-parameter-group-name mydbclpg \
    --reset-all-parameters
```

Output:

```
{
    "DBClusterParameterGroupName": "mydbclpg"
}
```

For more information, see [Working with DB parameter groups and DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.

**Example 2: To reset specific parameters to their default values**

The following `reset-db-cluster-parameter-group` example resets the parameter values for specific parameters to their default values in a customer-created DB cluster parameter group.

```
aws rds reset-db-cluster-parameter-group \
    --db-cluster-parameter-group-name mydbclpgy \
    --parameters "ParameterName=max_connections,ApplyMethod=immediate" \
                 "ParameterName=max_allowed_packet,ApplyMethod=immediate"
```

Output:

```
{
    "DBClusterParameterGroupName": "mydbclpg"
}
```

For more information, see [Working with DB parameter groups and DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) in the *Amazon Aurora User Guide*.

## Output

DBClusterParameterGroupName -> (string)

The name of the DB cluster parameter group.

Constraints:

- Must be 1 to 255 letters or numbers.
- First character must be a letter
- Canât end with a hyphen or contain two consecutive hyphens

### Note

This value is stored as a lowercase string.