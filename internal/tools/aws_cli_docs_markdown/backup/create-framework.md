# create-frameworkÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-framework.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-framework.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# create-framework

## Description

Creates a framework with one or more controls. A framework is a collection of controls that you can use to evaluate your backup practices. By using pre-built customizable controls to define your policies, you can evaluate whether your backup practices comply with your policies and which resources are not yet in compliance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/CreateFramework)

## Synopsis

```
create-framework
--framework-name <value>
[--framework-description <value>]
--framework-controls <value>
[--idempotency-token <value>]
[--framework-tags <value>]
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

`--framework-name` (string)

The unique name of the framework. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).

`--framework-description` (string)

An optional description of the framework with a maximum of 1,024 characters.

`--framework-controls` (list)

The controls that make up the framework. Each control in the list has a name, input parameters, and scope.

(structure)

Contains detailed information about all of the controls of a framework. Each framework must contain at least one control.

ControlName -> (string)

The name of a control. This name is between 1 and 256 characters.

ControlInputParameters -> (list)

The name/value pairs.

(structure)

The parameters for a control. A control can have zero, one, or more than one parameter. An example of a control with two parameters is: âbackup plan frequency is at least `daily` and the retention period is at least `1 year` â. The first parameter is `daily` . The second parameter is `1 year` .

ParameterName -> (string)

The name of a parameter, for example, `BackupPlanFrequency` .

ParameterValue -> (string)

The value of parameter, for example, `hourly` .

ControlScope -> (structure)

The scope of a control. The control scope defines what the control will evaluate. Three examples of control scopes are: a specific backup plan, all backup plans with a specific tag, or all backup plans.

For more information, see ` `ControlScope` . <[https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ControlScope.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ControlScope.html)>`__

ComplianceResourceIds -> (list)

The ID of the only Amazon Web Services resource that you want your control scope to contain.

(string)

ComplianceResourceTypes -> (list)

Describes whether the control scope includes one or more types of resources, such as `EFS` or `RDS` .

(string)

Tags -> (map)

The tag key-value pair applied to those Amazon Web Services resources that you want to trigger an evaluation for a rule. A maximum of one key-value pair can be provided. The tag value is optional, but it cannot be an empty string if you are creating or editing a framework from the console (though the value can be an empty string when included in a CloudFormation template).

The structure to assign a tag is: `[{"Key":"string","Value":"string"}]` .

key -> (string)

value -> (string)

Shorthand Syntax:

```
ControlName=string,ControlInputParameters=[{ParameterName=string,ParameterValue=string},{ParameterName=string,ParameterValue=string}],ControlScope={ComplianceResourceIds=[string,string],ComplianceResourceTypes=[string,string],Tags={KeyName1=string,KeyName2=string}} ...
```

JSON Syntax:

```
[
  {
    "ControlName": "string",
    "ControlInputParameters": [
      {
        "ParameterName": "string",
        "ParameterValue": "string"
      }
      ...
    ],
    "ControlScope": {
      "ComplianceResourceIds": ["string", ...],
      "ComplianceResourceTypes": ["string", ...],
      "Tags": {"string": "string"
        ...}
    }
  }
  ...
]
```

`--idempotency-token` (string)

A customer-chosen string that you can use to distinguish between otherwise identical calls to `CreateFrameworkInput` . Retrying a successful request with the same idempotency token results in a success message with no action taken.

`--framework-tags` (map)

The tags to assign to the framework.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

## Output

FrameworkName -> (string)

The unique name of the framework. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).

FrameworkArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.