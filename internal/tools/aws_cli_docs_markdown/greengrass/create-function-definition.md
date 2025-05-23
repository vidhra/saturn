# create-function-definitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-function-definition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-function-definition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [greengrass](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/index.html#cli-aws-greengrass) ]

# create-function-definition

## Description

Creates a Lambda function definition which contains a list of Lambda functions and their configurations to be used in a group. You can create an initial version of the definition by providing a list of Lambda functions and their configurations now, or use ââCreateFunctionDefinitionVersionââ later.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateFunctionDefinition)

## Synopsis

```
create-function-definition
[--amzn-client-token <value>]
[--initial-version <value>]
[--name <value>]
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

`--amzn-client-token` (string)
A client token used to correlate requests and responses.

`--initial-version` (structure)
Information about the initial version of the function definition.DefaultConfig -> (structure)

The default configuration that applies to all Lambda functions in this function definition version. Individual Lambda functions can override these settings.

Execution -> (structure)

Configuration information that specifies how a Lambda function runs.

IsolationMode -> (string)

Specifies whether the Lambda function runs in a Greengrass container (default) or without containerization. Unless your scenario requires that you run without containerization, we recommend that you run in a Greengrass container. Omit this value to run the Lambda function with the default containerization for the group.

RunAs -> (structure)

Specifies the user and group whose permissions are used when running the Lambda function. You can specify one or both values to override the default values. We recommend that you avoid running as root unless absolutely necessary to minimize the risk of unintended changes or malicious attacks. To run as root, you must set ââIsolationModeââ to ââNoContainerââ and update config.json in ââgreengrass-root/configââ to set ââallowFunctionsToRunAsRootââ to ââyesââ.

Gid -> (integer)

The group ID whose permissions are used to run a Lambda function.

Uid -> (integer)

The user ID whose permissions are used to run a Lambda function.

Functions -> (list)

A list of Lambda functions in this function definition version.

(structure)

Information about a Lambda function.

FunctionArn -> (string)

The ARN of the Lambda function.

FunctionConfiguration -> (structure)

The configuration of the Lambda function.

EncodingType -> (string)

The expected encoding type of the input payload for the function. The default is ââjsonââ.

Environment -> (structure)

The environment configuration of the function.

AccessSysfs -> (boolean)

If true, the Lambda function is allowed to access the hostâs /sys folder. Use this when the Lambda function needs to read device information from /sys. This setting applies only when you run the Lambda function in a Greengrass container.

Execution -> (structure)

Configuration related to executing the Lambda function

IsolationMode -> (string)

Specifies whether the Lambda function runs in a Greengrass container (default) or without containerization. Unless your scenario requires that you run without containerization, we recommend that you run in a Greengrass container. Omit this value to run the Lambda function with the default containerization for the group.

RunAs -> (structure)

Specifies the user and group whose permissions are used when running the Lambda function. You can specify one or both values to override the default values. We recommend that you avoid running as root unless absolutely necessary to minimize the risk of unintended changes or malicious attacks. To run as root, you must set ââIsolationModeââ to ââNoContainerââ and update config.json in ââgreengrass-root/configââ to set ââallowFunctionsToRunAsRootââ to ââyesââ.

Gid -> (integer)

The group ID whose permissions are used to run a Lambda function.

Uid -> (integer)

The user ID whose permissions are used to run a Lambda function.

ResourceAccessPolicies -> (list)

A list of the resources, with their permissions, to which the Lambda function will be granted access. A Lambda function can have at most 10 resources. ResourceAccessPolicies apply only when you run the Lambda function in a Greengrass container.

(structure)

A policy used by the function to access a resource.

Permission -> (string)

The permissions that the Lambda function has to the resource. Can be one of âârwââ (read/write) or ââroââ (read-only).

ResourceId -> (string)

The ID of the resource. (This ID is assigned to the resource when you create the resource definiton.)

Variables -> (map)

Environment variables for the Lambda functionâs configuration.

key -> (string)

value -> (string)

ExecArgs -> (string)

The execution arguments.

Executable -> (string)

The name of the function executable.

MemorySize -> (integer)

The memory size, in KB, which the function requires. This setting is not applicable and should be cleared when you run the Lambda function without containerization.

Pinned -> (boolean)

True if the function is pinned. Pinned means the function is long-lived and starts when the core starts.

Timeout -> (integer)

The allowed function execution time, after which Lambda should terminate the function. This timeout still applies to pinned Lambda functions for each request.

FunctionRuntimeOverride -> (string)

The Lambda runtime supported by Greengrass which is to be used instead of the one specified in the Lambda function.

Id -> (string)

A descriptive or arbitrary ID for the function. This value must be unique within the function definition version. Max length is 128 characters with pattern ââ[a-zA-Z0-9:_-]+ââ.

JSON Syntax:

```
{
  "DefaultConfig": {
    "Execution": {
      "IsolationMode": "GreengrassContainer"|"NoContainer",
      "RunAs": {
        "Gid": integer,
        "Uid": integer
      }
    }
  },
  "Functions": [
    {
      "FunctionArn": "string",
      "FunctionConfiguration": {
        "EncodingType": "binary"|"json",
        "Environment": {
          "AccessSysfs": true|false,
          "Execution": {
            "IsolationMode": "GreengrassContainer"|"NoContainer",
            "RunAs": {
              "Gid": integer,
              "Uid": integer
            }
          },
          "ResourceAccessPolicies": [
            {
              "Permission": "ro"|"rw",
              "ResourceId": "string"
            }
            ...
          ],
          "Variables": {"string": "string"
            ...}
        },
        "ExecArgs": "string",
        "Executable": "string",
        "MemorySize": integer,
        "Pinned": true|false,
        "Timeout": integer,
        "FunctionRuntimeOverride": "string"
      },
      "Id": "string"
    }
    ...
  ]
}
```

`--name` (string)
The name of the function definition.

`--tags` (map)
Tag(s) to add to the new resource.key -> (string)

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a Lambda function definition**

The following `create-function-definition` example creates a Lambda function definition and an initial version by providing a list of Lambda functions (in this case, a list of just one function named `TempMonitorFunction`) and their configurations. Before you can create the function definition, you need the Lambda function ARN. To create the function and its alias, use Lambdaâs `create-function` and `publish-version` commands. Lambdaâs `create-function` command requires the ARN of the execution role, even though AWS IoT Greengrass doesnât use that role because permissions are specified in the Greengrass group role.  You can use the IAM `create-role` command to create an empty role to get an ARN to use with Lambdaâs `create-function` or you can use an existing execution role.

```
aws greengrass create-function-definition \
    --name MyGreengrassFunctions \
    --initial-version "{\"Functions\": [{\"Id\": \"TempMonitorFunction\", \"FunctionArn\": \"arn:aws:lambda:us-west-2:123456789012:function:TempMonitor:GG_TempMonitor\", \"FunctionConfiguration\": {\"Executable\": \"temp_monitor.function_handler\", \"MemorySize\": 16000,\"Timeout\": 5}}]}"
```

Output:

```
{
    "Arn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/3b0d0080-87e7-48c6-b182-503ec743a08b",
    "CreationTimestamp": "2019-06-19T22:24:44.585Z",
    "Id": "3b0d0080-87e7-48c6-b182-503ec743a08b",
    "LastUpdatedTimestamp": "2019-06-19T22:24:44.585Z",
    "LatestVersion": "67f918b9-efb4-40b0-b87c-de8c9faf085b",
    "LatestVersionArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/definition/functions/3b0d0080-87e7-48c6-b182-503ec743a08b/versions/67f918b9-efb4-40b0-b87c-de8c9faf085b",
    "Name": "MyGreengrassFunctions"
}
```

For more information, see [How to Configure Local Resource Access Using the AWS Command Line Interface](https://docs.aws.amazon.com/greengrass/latest/developerguide/lra-cli.html) in the *AWS IoT Greengrass Developer Guide*.

## Output

Arn -> (string)

The ARN of the definition.

CreationTimestamp -> (string)

The time, in milliseconds since the epoch, when the definition was created.

Id -> (string)

The ID of the definition.

LastUpdatedTimestamp -> (string)

The time, in milliseconds since the epoch, when the definition was last updated.

LatestVersion -> (string)

The ID of the latest version associated with the definition.

LatestVersionArn -> (string)

The ARN of the latest version associated with the definition.

Name -> (string)

The name of the definition.