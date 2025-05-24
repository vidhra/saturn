# modify-db-parameter-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-parameter-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-parameter-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# modify-db-parameter-group

## Description

Modifies the parameters of a DB parameter group. To modify more than one parameter, submit a list of the following: `ParameterName` , `ParameterValue` , and `ApplyMethod` . A maximum of 20 parameters can be modified in a single request.

### Warning

After you modify a DB parameter group, you should wait at least 5 minutes before creating your first DB instance that uses that DB parameter group as the default parameter group. This allows Amazon RDS to fully complete the modify operation before the parameter group is used as the default for a new DB instance. This is especially important for parameters that are critical when creating the default database for a DB instance, such as the character set for the default database defined by the `character_set_database` parameter. You can use the *Parameter Groups* option of the [Amazon RDS console](https://console.aws.amazon.com/rds/) or the *DescribeDBParameters* command to verify that your DB parameter group has been created or modified.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/ModifyDBParameterGroup)

## Synopsis

```
modify-db-parameter-group
--db-parameter-group-name <value>
--parameters <value>
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

`--db-parameter-group-name` (string)

The name of the DB parameter group.

Constraints:

- If supplied, must match the name of an existing `DBParameterGroup` .

`--parameters` (list)

An array of parameter names, values, and the application methods for the parameter update. At least one parameter name, value, and application method must be supplied; later arguments are optional. A maximum of 20 parameters can be modified in a single request.

Valid Values (for the application method): `immediate | pending-reboot`

You can use the `immediate` value with dynamic parameters only. You can use the `pending-reboot` value for both dynamic and static parameters.

When the application method is `immediate` , changes to dynamic parameters are applied immediately to the DB instances associated with the parameter group.

When the application method is `pending-reboot` , changes to dynamic and static parameters are applied after a reboot without failover to the DB instances associated with the parameter group.

### Note

You canât use `pending-reboot` with dynamic parameters on RDS for SQL Server DB instances. Use `immediate` .

For more information on modifying DB parameters, see [Working with DB parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide* .

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

**To modify a DB parameter group**

The following `modify-db-parameter-group` example changes the value of the `clr enabled` parameter in a DB parameter group. The `--apply-immediately` parameter causes the DB parameter group to be modified immediately, instead of waiting until the next maintenance window.

```
aws rds modify-db-parameter-group \
    --db-parameter-group-name test-sqlserver-se-2017 \
    --parameters "ParameterName='clr enabled',ParameterValue=1,ApplyMethod=immediate"
```

Output:

```
{
    "DBParameterGroupName": "test-sqlserver-se-2017"
}
```

For more information, see [Modifying Parameters in a DB Parameter Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html#USER_WorkingWithParamGroups.Modifying) in the *Amazon RDS User Guide*.

## Output

DBParameterGroupName -> (string)

The name of the DB parameter group.