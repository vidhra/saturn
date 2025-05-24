# describe-configuration-optionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-configuration-options.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-configuration-options.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# describe-configuration-options

## Description

Describes the configuration options that are used in a particular configuration template or environment, or that a specified solution stack defines. The description includes the values the options, their default values, and an indication of the required action on a running environment if an option value is changed.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions)

## Synopsis

```
describe-configuration-options
[--application-name <value>]
[--template-name <value>]
[--environment-name <value>]
[--solution-stack-name <value>]
[--platform-arn <value>]
[--options <value>]
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

`--application-name` (string)

The name of the application associated with the configuration template or environment. Only needed if you want to describe the configuration options associated with either the configuration template or environment.

`--template-name` (string)

The name of the configuration template whose configuration options you want to describe.

`--environment-name` (string)

The name of the environment whose configuration options you want to describe.

`--solution-stack-name` (string)

The name of the solution stack whose configuration options you want to describe.

`--platform-arn` (string)

The ARN of the custom platform.

`--options` (list)

If specified, restricts the descriptions to only the specified options.

(structure)

A specification identifying an individual configuration option.

ResourceName -> (string)

A unique resource name for a time-based scaling configuration option.

Namespace -> (string)

A unique namespace identifying the optionâs associated AWS resource.

OptionName -> (string)

The name of the configuration option.

Shorthand Syntax:

```
ResourceName=string,Namespace=string,OptionName=string ...
```

JSON Syntax:

```
[
  {
    "ResourceName": "string",
    "Namespace": "string",
    "OptionName": "string"
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

**To view configuration options for an environment**

The following command retrieves descriptions of all available configuration options for an environment named `my-env`:

```
aws elasticbeanstalk describe-configuration-options --environment-name my-env --application-name my-app
```

Output (abbreviated):

```
{
    "Options": [
        {
            "Name": "JVMOptions",
            "UserDefined": false,
            "DefaultValue": "Xms=256m,Xmx=256m,XX:MaxPermSize=64m,JVM Options=",
            "ChangeSeverity": "RestartApplicationServer",
            "Namespace": "aws:cloudformation:template:parameter",
            "ValueType": "KeyValueList"
        },
        {
            "Name": "Interval",
            "UserDefined": false,
            "DefaultValue": "30",
            "ChangeSeverity": "NoInterruption",
            "Namespace": "aws:elb:healthcheck",
            "MaxValue": 300,
            "MinValue": 5,
            "ValueType": "Scalar"
        },
        ...
        {
            "Name": "LowerThreshold",
            "UserDefined": false,
            "DefaultValue": "2000000",
            "ChangeSeverity": "NoInterruption",
            "Namespace": "aws:autoscaling:trigger",
            "MinValue": 0,
            "ValueType": "Scalar"
        },
        {
            "Name": "ListenerEnabled",
            "UserDefined": false,
            "DefaultValue": "true",
            "ChangeSeverity": "Unknown",
            "Namespace": "aws:elb:listener",
            "ValueType": "Boolean"
        }
    ]
}
```

Available configuration options vary per platform and configuration version. For more information about namespaces and supported options, see [Option Values](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the *AWS Elastic Beanstalk Developer Guide*.

## Output

SolutionStackName -> (string)

The name of the solution stack these configuration options belong to.

PlatformArn -> (string)

The ARN of the platform version.

Options -> (list)

A list of  ConfigurationOptionDescription .

(structure)

Describes the possible values for a configuration option.

Namespace -> (string)

A unique namespace identifying the optionâs associated AWS resource.

Name -> (string)

The name of the configuration option.

DefaultValue -> (string)

The default value for this configuration option.

ChangeSeverity -> (string)

An indication of which action is required if the value for this configuration option changes:

- `NoInterruption` : There is no interruption to the environment or application availability.
- `RestartEnvironment` : The environment is entirely restarted, all AWS resources are deleted and recreated, and the environment is unavailable during the process.
- `RestartApplicationServer` : The environment is available the entire time. However, a short application outage occurs when the application servers on the running Amazon EC2 instances are restarted.

UserDefined -> (boolean)

An indication of whether the user defined this configuration option:

- `true` : This configuration option was defined by the user. It is a valid choice for specifying if this as an `Option to Remove` when updating configuration settings.
- `false` : This configuration was not defined by the user.

Constraint: You can remove only `UserDefined` options from a configuration.

Valid Values: `true` | `false`

ValueType -> (string)

An indication of which type of values this option has and whether it is allowable to select one or more than one of the possible values:

- `Scalar` : Values for this option are a single selection from the possible values, or an unformatted string, or numeric value governed by the `MIN/MAX/Regex` constraints.
- `List` : Values for this option are multiple selections from the possible values.
- `Boolean` : Values for this option are either `true` or `false` .
- `Json` : Values for this option are a JSON representation of a `ConfigDocument` .

ValueOptions -> (list)

If specified, values for the configuration option are selected from this list.

(string)

MinValue -> (integer)

If specified, the configuration option must be a numeric value greater than this value.

MaxValue -> (integer)

If specified, the configuration option must be a numeric value less than this value.

MaxLength -> (integer)

If specified, the configuration option must be a string value no longer than this value.

Regex -> (structure)

If specified, the configuration option must be a string value that satisfies this regular expression.

Pattern -> (string)

The regular expression pattern that a string configuration option value with this restriction must match.

Label -> (string)

A unique name representing this regular expression.