# create-configuration-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-configuration-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-configuration-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# create-configuration-template

## Description

Creates an AWS Elastic Beanstalk configuration template, associated with a specific Elastic Beanstalk application. You define application configuration settings in a configuration template. You can then use the configuration template to deploy different versions of the application with the same configuration settings.

Templates arenât associated with any environment. The `EnvironmentName` response element is always `null` .

Related Topics

- DescribeConfigurationOptions
- DescribeConfigurationSettings
- ListAvailableSolutionStacks

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate)

## Synopsis

```
create-configuration-template
--application-name <value>
--template-name <value>
[--solution-stack-name <value>]
[--platform-arn <value>]
[--source-configuration <value>]
[--environment-id <value>]
[--description <value>]
[--option-settings <value>]
[--tags <value>]
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

The name of the Elastic Beanstalk application to associate with this configuration template.

`--template-name` (string)

The name of the configuration template.

Constraint: This name must be unique per application.

`--solution-stack-name` (string)

The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, `64bit Amazon Linux 2013.09 running Tomcat 7 Java 7` . A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html) in the *AWS Elastic Beanstalk Developer Guide* .

You must specify `SolutionStackName` if you donât specify `PlatformArn` , `EnvironmentId` , or `SourceConfiguration` .

Use the ` `ListAvailableSolutionStacks` [https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks).html`__ API to obtain a list of available solution stacks.

`--platform-arn` (string)

The Amazon Resource Name (ARN) of the custom platform. For more information, see [Custom Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the *AWS Elastic Beanstalk Developer Guide* .

### Note

If you specify `PlatformArn` , then donât specify `SolutionStackName` .

`--source-configuration` (structure)

An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.

Values specified in `OptionSettings` override any values obtained from the `SourceConfiguration` .

You must specify `SourceConfiguration` if you donât specify `PlatformArn` , `EnvironmentId` , or `SolutionStackName` .

Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.

ApplicationName -> (string)

The name of the application associated with the configuration.

TemplateName -> (string)

The name of the configuration template.

Shorthand Syntax:

```
ApplicationName=string,TemplateName=string
```

JSON Syntax:

```
{
  "ApplicationName": "string",
  "TemplateName": "string"
}
```

`--environment-id` (string)

The ID of an environment whose settings you want to use to create the configuration template. You must specify `EnvironmentId` if you donât specify `PlatformArn` , `SolutionStackName` , or `SourceConfiguration` .

`--description` (string)

An optional description for this configuration.

`--option-settings` (list)

Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the *AWS Elastic Beanstalk Developer Guide* .

(structure)

A specification identifying an individual configuration option along with its current value. For a list of possible namespaces and option values, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the *AWS Elastic Beanstalk Developer Guide* .

ResourceName -> (string)

A unique resource name for the option setting. Use it for a timeâbased scaling configuration option.

Namespace -> (string)

A unique namespace that identifies the optionâs associated AWS resource.

OptionName -> (string)

The name of the configuration option.

Value -> (string)

The current value for the configuration option.

Shorthand Syntax:

```
ResourceName=string,Namespace=string,OptionName=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "ResourceName": "string",
    "Namespace": "string",
    "OptionName": "string",
    "Value": "string"
  }
  ...
]
```

`--tags` (list)

Specifies the tags applied to the configuration template.

(structure)

Describes a tag applied to a resource in an environment.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
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

**To create a configuration template**

The following command creates a configuration template named `my-app-v1` from the settings applied to an environment with the id `e-rpqsewtp2j`:

```
aws elasticbeanstalk create-configuration-template --application-name my-app --template-name my-app-v1 --environment-id e-rpqsewtp2j
```

Output:

```
{
    "ApplicationName": "my-app",
    "TemplateName": "my-app-v1",
    "DateCreated": "2015-08-12T18:40:39Z",
    "DateUpdated": "2015-08-12T18:40:39Z",
    "SolutionStackName": "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8"
}
```

## Output

SolutionStackName -> (string)

The name of the solution stack this configuration set uses.

PlatformArn -> (string)

The ARN of the platform version.

ApplicationName -> (string)

The name of the application associated with this configuration set.

TemplateName -> (string)

If not `null` , the name of the configuration template for this configuration set.

Description -> (string)

Describes this configuration set.

EnvironmentName -> (string)

If not `null` , the name of the environment for this configuration set.

DeploymentStatus -> (string)

If this configuration set is associated with an environment, the `DeploymentStatus` parameter indicates the deployment status of this configuration set:

- `null` : This configuration is not associated with a running environment.
- `pending` : This is a draft configuration that is not deployed to the associated environment but is in the process of deploying.
- `deployed` : This is the configuration that is currently deployed to the associated running environment.
- `failed` : This is a draft configuration that failed to successfully deploy.

DateCreated -> (timestamp)

The date (in UTC time) when this configuration set was created.

DateUpdated -> (timestamp)

The date (in UTC time) when this configuration set was last modified.

OptionSettings -> (list)

A list of the configuration options and their values in this configuration set.

(structure)

A specification identifying an individual configuration option along with its current value. For a list of possible namespaces and option values, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the *AWS Elastic Beanstalk Developer Guide* .

ResourceName -> (string)

A unique resource name for the option setting. Use it for a timeâbased scaling configuration option.

Namespace -> (string)

A unique namespace that identifies the optionâs associated AWS resource.

OptionName -> (string)

The name of the configuration option.

Value -> (string)

The current value for the configuration option.