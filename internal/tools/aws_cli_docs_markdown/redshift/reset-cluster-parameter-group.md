# reset-cluster-parameter-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reset-cluster-parameter-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reset-cluster-parameter-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# reset-cluster-parameter-group

## Description

Sets one or more parameters of the specified parameter group to their default values and sets the source values of the parameters to âengine-defaultâ. To reset the entire parameter group specify the *ResetAllParameters* parameter. For parameter changes to take effect you must reboot any associated clusters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ResetClusterParameterGroup)

## Synopsis

```
reset-cluster-parameter-group
--parameter-group-name <value>
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

`--parameter-group-name` (string)

The name of the cluster parameter group to be reset.

`--reset-all-parameters` | `--no-reset-all-parameters` (boolean)

If `true` , all parameters in the specified parameter group will be reset to their default values.

Default: `true`

`--parameters` (list)

An array of names of parameters to be reset. If *ResetAllParameters* option is not used, then at least one parameter name must be supplied.

Constraints: A maximum of 20 parameters can be reset in a single request.

(structure)

Describes a parameter in a cluster parameter group.

ParameterName -> (string)

The name of the parameter.

ParameterValue -> (string)

The value of the parameter. If `ParameterName` is `wlm_json_configuration` , then the maximum size of `ParameterValue` is 8000 characters.

Description -> (string)

A description of the parameter.

Source -> (string)

The source of the parameter value, such as âengine-defaultâ or âuserâ.

DataType -> (string)

The data type of the parameter.

AllowedValues -> (string)

The valid range of values for the parameter.

ApplyType -> (string)

Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Cluster Management Guide* .

IsModifiable -> (boolean)

If `true` , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion -> (string)

The earliest engine version to which the parameter can apply.

Shorthand Syntax:

```
ParameterName=string,ParameterValue=string,Description=string,Source=string,DataType=string,AllowedValues=string,ApplyType=string,IsModifiable=boolean,MinimumEngineVersion=string ...
```

JSON Syntax:

```
[
  {
    "ParameterName": "string",
    "ParameterValue": "string",
    "Description": "string",
    "Source": "string",
    "DataType": "string",
    "AllowedValues": "string",
    "ApplyType": "static"|"dynamic",
    "IsModifiable": true|false,
    "MinimumEngineVersion": "string"
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

### Reset Parameters in a Parameter Group

This example shows how to reset all of the parameters in a parameter group.

Command:

```
aws redshift reset-cluster-parameter-group --parameter-group-name myclusterparametergroup --reset-all-parameters
```

## Output

ParameterGroupName -> (string)

The name of the cluster parameter group.

ParameterGroupStatus -> (string)

The status of the parameter group. For example, if you made a change to a parameter group name-value pair, then the change could be pending a reboot of an associated cluster.