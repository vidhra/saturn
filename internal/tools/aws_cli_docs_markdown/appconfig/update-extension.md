# update-extensionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-extension.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-extension.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appconfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/index.html#cli-aws-appconfig) ]

# update-extension

## Description

Updates an AppConfig extension. For more information about extensions, see [Extending workflows](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) in the *AppConfig User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appconfig-2019-10-09/UpdateExtension)

## Synopsis

```
update-extension
--extension-identifier <value>
[--description <value>]
[--actions <value>]
[--parameters <value>]
[--version-number <value>]
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

`--extension-identifier` (string)

The name, the ID, or the Amazon Resource Name (ARN) of the extension.

`--description` (string)

Information about the extension.

`--actions` (map)

The actions defined in the extension.

key -> (string)

value -> (list)

(structure)

An action defines the tasks that the extension performs during the AppConfig workflow. Each action includes an action point, as shown in the following list:

- `PRE_CREATE_HOSTED_CONFIGURATION_VERSION`
- `PRE_START_DEPLOYMENT`
- `AT_DEPLOYMENT_TICK`
- `ON_DEPLOYMENT_START`
- `ON_DEPLOYMENT_STEP`
- `ON_DEPLOYMENT_BAKING`
- `ON_DEPLOYMENT_COMPLETE`
- `ON_DEPLOYMENT_ROLLED_BACK`

Each action also includes a name, a URI to an Lambda function, and an Amazon Resource Name (ARN) for an Identity and Access Management assume role. You specify the name, URI, and ARN for each *action point* defined in the extension.

Name -> (string)

The action name.

Description -> (string)

Information about the action.

Uri -> (string)

The extension URI associated to the action point in the extension definition. The URI can be an Amazon Resource Name (ARN) for one of the following: an Lambda function, an Amazon Simple Queue Service queue, an Amazon Simple Notification Service topic, or the Amazon EventBridge default event bus.

RoleArn -> (string)

An Amazon Resource Name (ARN) for an Identity and Access Management assume role.

Shorthand Syntax:

```
KeyName1=[{Name=string,Description=string,Uri=string,RoleArn=string},{Name=string,Description=string,Uri=string,RoleArn=string}],KeyName2=[{Name=string,Description=string,Uri=string,RoleArn=string},{Name=string,Description=string,Uri=string,RoleArn=string}]

Where valid key names are:
  PRE_CREATE_HOSTED_CONFIGURATION_VERSION
  PRE_START_DEPLOYMENT
  AT_DEPLOYMENT_TICK
  ON_DEPLOYMENT_START
  ON_DEPLOYMENT_STEP
  ON_DEPLOYMENT_BAKING
  ON_DEPLOYMENT_COMPLETE
  ON_DEPLOYMENT_ROLLED_BACK
```

JSON Syntax:

```
{"PRE_CREATE_HOSTED_CONFIGURATION_VERSION"|"PRE_START_DEPLOYMENT"|"AT_DEPLOYMENT_TICK"|"ON_DEPLOYMENT_START"|"ON_DEPLOYMENT_STEP"|"ON_DEPLOYMENT_BAKING"|"ON_DEPLOYMENT_COMPLETE"|"ON_DEPLOYMENT_ROLLED_BACK": [
      {
        "Name": "string",
        "Description": "string",
        "Uri": "string",
        "RoleArn": "string"
      }
      ...
    ]
  ...}
```

`--parameters` (map)

One or more parameters for the actions called by the extension.

key -> (string)

value -> (structure)

A value such as an Amazon Resource Name (ARN) or an Amazon Simple Notification Service topic entered in an extension when invoked. Parameter values are specified in an extension association. For more information about extensions, see [Extending workflows](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) in the *AppConfig User Guide* .

Description -> (string)

Information about the parameter.

Required -> (boolean)

A parameter value must be specified in the extension association.

Dynamic -> (boolean)

Indicates whether this parameterâs value can be supplied at the extensionâs action point instead of during extension association. Dynamic parameters canât be marked `Required` .

Shorthand Syntax:

```
KeyName1=Description=string,Required=boolean,Dynamic=boolean,KeyName2=Description=string,Required=boolean,Dynamic=boolean
```

JSON Syntax:

```
{"string": {
      "Description": "string",
      "Required": true|false,
      "Dynamic": true|false
    }
  ...}
```

`--version-number` (integer)

The extension version number.

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

**To update an AWS AppConfig extension**

The following `update-extension` example adds an additional parameter Key to an extension in AWS AppConfig.

```
aws appconfig update-extension \
    --region us-west-2 \
    --extension-identifier S3-backup-extension \
    --parameters S3bucket={Required=true},CampaignID={Required=false}
```

Output:

```
{
    "Id": "1A2B3C4D",
    "Name": "S3-backup-extension",
    "VersionNumber": 1,
    "Arn": "arn:aws:appconfig:us-west-2:123456789012:extension/1A2B3C4D/1",
    "Actions": {
        "PRE_CREATE_HOSTED_CONFIGURATION_VERSION": [
            {
                "Name": "S3backup",
                "Uri": "arn:aws:lambda:us-west-2:123456789012:function:S3backupfunction",
                "RoleArn": "arn:aws:iam::123456789012:role/appconfigextensionrole"
            }
        ]
    },
    "Parameters": {
        "CampaignID": {
            "Required": false
        },
        "S3bucket": {
            "Required": true
        }
    }
}
```

For more information, see [Working with AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) in the *AWS AppConfig User Guide*.

## Output

Id -> (string)

The system-generated ID of the extension.

Name -> (string)

The extension name.

VersionNumber -> (integer)

The extension version number.

Arn -> (string)

The system-generated Amazon Resource Name (ARN) for the extension.

Description -> (string)

Information about the extension.

Actions -> (map)

The actions defined in the extension.

key -> (string)

value -> (list)

(structure)

An action defines the tasks that the extension performs during the AppConfig workflow. Each action includes an action point, as shown in the following list:

- `PRE_CREATE_HOSTED_CONFIGURATION_VERSION`
- `PRE_START_DEPLOYMENT`
- `AT_DEPLOYMENT_TICK`
- `ON_DEPLOYMENT_START`
- `ON_DEPLOYMENT_STEP`
- `ON_DEPLOYMENT_BAKING`
- `ON_DEPLOYMENT_COMPLETE`
- `ON_DEPLOYMENT_ROLLED_BACK`

Each action also includes a name, a URI to an Lambda function, and an Amazon Resource Name (ARN) for an Identity and Access Management assume role. You specify the name, URI, and ARN for each *action point* defined in the extension.

Name -> (string)

The action name.

Description -> (string)

Information about the action.

Uri -> (string)

The extension URI associated to the action point in the extension definition. The URI can be an Amazon Resource Name (ARN) for one of the following: an Lambda function, an Amazon Simple Queue Service queue, an Amazon Simple Notification Service topic, or the Amazon EventBridge default event bus.

RoleArn -> (string)

An Amazon Resource Name (ARN) for an Identity and Access Management assume role.

Parameters -> (map)

The parameters accepted by the extension. You specify parameter values when you associate the extension to an AppConfig resource by using the `CreateExtensionAssociation` API action. For Lambda extension actions, these parameters are included in the Lambda request object.

key -> (string)

value -> (structure)

A value such as an Amazon Resource Name (ARN) or an Amazon Simple Notification Service topic entered in an extension when invoked. Parameter values are specified in an extension association. For more information about extensions, see [Extending workflows](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) in the *AppConfig User Guide* .

Description -> (string)

Information about the parameter.

Required -> (boolean)

A parameter value must be specified in the extension association.

Dynamic -> (boolean)

Indicates whether this parameterâs value can be supplied at the extensionâs action point instead of during extension association. Dynamic parameters canât be marked `Required` .