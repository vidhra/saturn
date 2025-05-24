# create-component-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/create-component-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/create-component-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [greengrassv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/index.html#cli-aws-greengrassv2) ]

# create-component-version

## Description

Creates a component. Components are software that run on Greengrass core devices. After you develop and test a component on your core device, you can use this operation to upload your component to IoT Greengrass. Then, you can deploy the component to other core devices.

You can use this operation to do the following:

- **Create components from recipes**   Create a component from a recipe, which is a file that defines the componentâs metadata, parameters, dependencies, lifecycle, artifacts, and platform capability. For more information, see [IoT Greengrass component recipe reference](https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html) in the *IoT Greengrass V2 Developer Guide* . To create a component from a recipe, specify `inlineRecipe` when you call this operation.
- **Create components from Lambda functions**   Create a component from an Lambda function that runs on IoT Greengrass. This creates a recipe and artifacts from the Lambda functionâs deployment package. You can use this operation to migrate Lambda functions from IoT Greengrass V1 to IoT Greengrass V2. This function accepts Lambda functions in all supported versions of Python, Node.js, and Java runtimes. IoT Greengrass doesnât apply any additional restrictions on deprecated Lambda runtime versions. To create a component from a Lambda function, specify `lambdaFunction` when you call this operation.

### Note

IoT Greengrass currently supports Lambda functions on only Linux core devices.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/greengrassv2-2020-11-30/CreateComponentVersion)

## Synopsis

```
create-component-version
[--inline-recipe <value>]
[--lambda-function <value>]
[--tags <value>]
[--client-token <value>]
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

`--inline-recipe` (blob)

The recipe to use to create the component. The recipe defines the componentâs metadata, parameters, dependencies, lifecycle, artifacts, and platform compatibility.

You must specify either `inlineRecipe` or `lambdaFunction` .

`--lambda-function` (structure)

The parameters to create a component from a Lambda function.

You must specify either `inlineRecipe` or `lambdaFunction` .

lambdaArn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Lambda function. The ARN must include the version of the function to import. You canât use version aliases like `$LATEST` .

componentName -> (string)

The name of the component.

Defaults to the name of the Lambda function.

componentVersion -> (string)

The version of the component.

Defaults to the version of the Lambda function as a semantic version. For example, if your function version is `3` , the component version becomes `3.0.0` .

componentPlatforms -> (list)

The platforms that the component version supports.

(structure)

Contains information about a platform that a component supports.

name -> (string)

The friendly name of the platform. This name helps you identify the platform.

If you omit this parameter, IoT Greengrass creates a friendly name from the `os` and `architecture` of the platform.

attributes -> (map)

A dictionary of attributes for the platform. The IoT Greengrass Core software defines the `os` and `architecture` by default. You can specify additional platform attributes for a core device when you deploy the Greengrass nucleus component. For more information, see the [Greengrass nucleus component](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html) in the *IoT Greengrass V2 Developer Guide* .

key -> (string)

value -> (string)

componentDependencies -> (map)

The component versions on which this Lambda function component depends.

key -> (string)

value -> (structure)

Contains information about a component dependency for a Lambda function component.

versionRequirement -> (string)

The component version requirement for the component dependency.

IoT Greengrass V2 uses semantic version constraints. For more information, see [Semantic Versioning](https://semver.org/) .

dependencyType -> (string)

The type of this dependency. Choose from the following options:

- `SOFT` â The component doesnât restart if the dependency changes state.
- `HARD` â The component restarts if the dependency changes state.

Default: `HARD`

componentLambdaParameters -> (structure)

The system and runtime parameters for the Lambda function as it runs on the Greengrass core device.

eventSources -> (list)

The list of event sources to which to subscribe to receive work messages. The Lambda function runs when it receives a message from an event source. You can subscribe this function to local publish/subscribe messages and Amazon Web Services IoT Core MQTT messages.

(structure)

Contains information about an event source for an Lambda function. The event source defines the topics on which this Lambda function subscribes to receive messages that run the function.

topic -> (string)

The topic to which to subscribe to receive event messages.

type -> (string)

The type of event source. Choose from the following options:

- `PUB_SUB` â Subscribe to local publish/subscribe messages. This event source type doesnât support MQTT wildcards (`+` and `#` ) in the event source topic.
- `IOT_CORE` â Subscribe to Amazon Web Services IoT Core MQTT messages. This event source type supports MQTT wildcards (`+` and `#` ) in the event source topic.

maxQueueSize -> (integer)

The maximum size of the message queue for the Lambda function component. The IoT Greengrass core stores messages in a FIFO (first-in-first-out) queue until it can run the Lambda function to consume each message.

maxInstancesCount -> (integer)

The maximum number of instances that a non-pinned Lambda function can run at the same time.

maxIdleTimeInSeconds -> (integer)

The maximum amount of time in seconds that a non-pinned Lambda function can idle before the IoT Greengrass Core software stops its process.

timeoutInSeconds -> (integer)

The maximum amount of time in seconds that the Lambda function can process a work item.

statusTimeoutInSeconds -> (integer)

The interval in seconds at which a pinned (also known as long-lived) Lambda function component sends status updates to the Lambda manager component.

pinned -> (boolean)

Whether or not the Lambda function is pinned, or long-lived.

- A pinned Lambda function starts when IoT Greengrass starts and keeps running in its own container.
- A non-pinned Lambda function starts only when it receives a work item and exists after it idles for `maxIdleTimeInSeconds` . If the function has multiple work items, the IoT Greengrass Core software creates multiple instances of the function.

Default: `true`

inputPayloadEncodingType -> (string)

The encoding type that the Lambda function supports.

Default: `json`

execArgs -> (list)

The list of arguments to pass to the Lambda function when it runs.

(string)

environmentVariables -> (map)

The map of environment variables that are available to the Lambda function when it runs.

key -> (string)

value -> (string)

linuxProcessParams -> (structure)

The parameters for the Linux process that contains the Lambda function.

isolationMode -> (string)

The isolation mode for the process that contains the Lambda function. The process can run in an isolated runtime environment inside the IoT Greengrass container, or as a regular process outside any container.

Default: `GreengrassContainer`

containerParams -> (structure)

The parameters for the container in which the Lambda function runs.

memorySizeInKB -> (integer)

The memory size of the container, expressed in kilobytes.

Default: `16384` (16 MB)

mountROSysfs -> (boolean)

Whether or not the container can read information from the deviceâs `/sys` folder.

Default: `false`

volumes -> (list)

The list of volumes that the container can access.

(structure)

Contains information about a volume that Linux processes in a container can access. When you define a volume, the IoT Greengrass Core software mounts the source files to the destination inside the container.

sourcePath -> (string)

The path to the physical volume in the file system.

destinationPath -> (string)

The path to the logical volume in the file system.

permission -> (string)

The permission to access the volume: read/only (`ro` ) or read/write (`rw` ).

Default: `ro`

addGroupOwner -> (boolean)

Whether or not to add the IoT Greengrass user group as an owner of the volume.

Default: `false`

devices -> (list)

The list of system devices that the container can access.

(structure)

Contains information about a device that Linux processes in a container can access.

path -> (string)

The mount path for the device in the file system.

permission -> (string)

The permission to access the device: read/only (`ro` ) or read/write (`rw` ).

Default: `ro`

addGroupOwner -> (boolean)

Whether or not to add the componentâs system user as an owner of the device.

Default: `false`

JSON Syntax:

```
{
  "lambdaArn": "string",
  "componentName": "string",
  "componentVersion": "string",
  "componentPlatforms": [
    {
      "name": "string",
      "attributes": {"string": "string"
        ...}
    }
    ...
  ],
  "componentDependencies": {"string": {
        "versionRequirement": "string",
        "dependencyType": "HARD"|"SOFT"
      }
    ...},
  "componentLambdaParameters": {
    "eventSources": [
      {
        "topic": "string",
        "type": "PUB_SUB"|"IOT_CORE"
      }
      ...
    ],
    "maxQueueSize": integer,
    "maxInstancesCount": integer,
    "maxIdleTimeInSeconds": integer,
    "timeoutInSeconds": integer,
    "statusTimeoutInSeconds": integer,
    "pinned": true|false,
    "inputPayloadEncodingType": "json"|"binary",
    "execArgs": ["string", ...],
    "environmentVariables": {"string": "string"
      ...},
    "linuxProcessParams": {
      "isolationMode": "GreengrassContainer"|"NoContainer",
      "containerParams": {
        "memorySizeInKB": integer,
        "mountROSysfs": true|false,
        "volumes": [
          {
            "sourcePath": "string",
            "destinationPath": "string",
            "permission": "ro"|"rw",
            "addGroupOwner": true|false
          }
          ...
        ],
        "devices": [
          {
            "path": "string",
            "permission": "ro"|"rw",
            "addGroupOwner": true|false
          }
          ...
        ]
      }
    }
  }
}
```

`--tags` (map)

A list of key-value pairs that contain metadata for the resource. For more information, see [Tag your resources](https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html) in the *IoT Greengrass V2 Developer Guide* .

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

`--client-token` (string)

A unique, case-sensitive identifier that you can provide to ensure that the request is idempotent. Idempotency means that the request is successfully processed only once, even if you send the request multiple times. When a request succeeds, and you specify the same client token for subsequent successful requests, the IoT Greengrass V2 service returns the successful response that it caches from the previous request. IoT Greengrass V2 caches successful responses for idempotent requests for up to 8 hours.

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

**Example 1: To create a component version from a recipe**

The following `create-component-version` example creates a version of a Hello World component from a recipe file.

```
aws greengrassv2 create-component-version \
    --inline-recipe fileb://com.example.HelloWorld-1.0.0.json
```

Contents of `com.example.HelloWorld-1.0.0.json`:

```
{
    "RecipeFormatVersion": "2020-01-25",
    "ComponentName": "com.example.HelloWorld",
    "ComponentVersion": "1.0.0",
    "ComponentDescription": "My first AWS IoT Greengrass component.",
    "ComponentPublisher": "Amazon",
    "ComponentConfiguration": {
        "DefaultConfiguration": {
            "Message": "world"
        }
    },
    "Manifests": [
        {
            "Platform": {
                "os": "linux"
            },
            "Lifecycle": {
                "Run": "echo 'Hello {configuration:/Message}'"
            }
        }
    ]
}
```

Output:

```
{
    "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0",
    "componentName": "com.example.HelloWorld",
    "componentVersion": "1.0.0",
    "creationTimestamp": "2021-01-07T16:24:33.650000-08:00",
    "status": {
        "componentState": "REQUESTED",
        "message": "NONE",
        "errors": {}
    }
}
```

For more information, see [Create custom components](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-components.html) and [Upload components to deploy](https://docs.aws.amazon.com/greengrass/v2/developerguide/upload-components.html) in the *AWS IoT Greengrass V2 Developer Guide*.

**Example 2: To create a component version from an AWS Lambda function**

The following `create-component-version` example creates a version of a Hello World component from an AWS Lambda function.

```
aws greengrassv2 create-component-version \
    --cli-input-json file://lambda-function-component.json
```

Contents of `lambda-function-component.json`:

```
{
    "lambdaFunction": {
        "lambdaArn": "arn:aws:lambda:us-west-2:123456789012:function:HelloWorldPythonLambda:1",
        "componentName": "com.example.HelloWorld",
        "componentVersion": "1.0.0",
        "componentLambdaParameters": {
            "eventSources": [
                {
                    "topic": "hello/world/+",
                    "type": "IOT_CORE"
                }
            ]
        }
    }
}
```

Output:

```
{
    "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0",
    "componentName": "com.example.HelloWorld",
    "componentVersion": "1.0.0",
    "creationTimestamp": "2021-01-07T17:05:27.347000-08:00",
    "status": {
        "componentState": "REQUESTED",
        "message": "NONE",
        "errors": {}
    }
}
```

For more information, see [Run AWS Lambda functions](https://docs.aws.amazon.com/greengrass/v2/developerguide/run-lambda-functions.html) in the *AWS IoT Greengrass V2 Developer Guide*.

## Output

arn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the component version.

componentName -> (string)

The name of the component.

componentVersion -> (string)

The version of the component.

creationTimestamp -> (timestamp)

The time at which the component was created, expressed in ISO 8601 format.

status -> (structure)

The status of the component version in IoT Greengrass V2. This status is different from the status of the component on a core device.

componentState -> (string)

The state of the component version.

message -> (string)

A message that communicates details, such as errors, about the status of the component version.

errors -> (map)

A dictionary of errors that communicate why the component version is in an error state. For example, if IoT Greengrass canât access an artifact for the component version, then `errors` contains the artifactâs URI as a key, and the error message as the value for that key.

key -> (string)

value -> (string)

vendorGuidance -> (string)

The vendor guidance state for the component version. This state indicates whether the component version has any issues that you should consider before you deploy it. The vendor guidance state can be:

- `ACTIVE` â This component version is available and recommended for use.
- `DISCONTINUED` â This component version has been discontinued by its publisher. You can deploy this component version, but we recommend that you use a different version of this component.
- `DELETED` â This component version has been deleted by its publisher, so you canât deploy it. If you have any existing deployments that specify this component version, those deployments will fail.

vendorGuidanceMessage -> (string)

A message that communicates details about the vendor guidance state of the component version. This message communicates why a component version is discontinued or deleted.