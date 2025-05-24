# get-componentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-component.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-component.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# get-component

## Description

Gets a component object.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/GetComponent)

## Synopsis

```
get-component
--component-build-version-arn <value>
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

`--component-build-version-arn` (string)

The Amazon Resource Name (ARN) of the component that you want to get. Regex requires the suffix `/\d+$` .

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

**To get component details**

The following `get-component` example lists the details of a component by specifying its ARN.

```
aws imagebuilder get-component \
    --component-build-version-arn arn:aws:imagebuilder:us-west-2:123456789012:component/component-name/1.0.0/1
```

Output:

```
{
    "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "component": {
        "arn": "arn:aws:imagebuilder:us-west-2:123456789012:component/component-name/1.0.0/1",
        "name": "component-name",
        "version": "1.0.0",
        "type": "TEST",
        "platform": "Linux",
        "owner": "123456789012",
        "data": "name: HelloWorldTestingDocument\ndescription: This is hello world testing document.\nschemaVersion: 1.0\n\nphases:\n  - name: test\n    steps:\n      - name: HelloWorldStep\n        action: ExecuteBash\n        inputs:\n          commands:\n            - echo \"Hello World! Test.\"\n",
        "encrypted": true,
        "dateCreated": "2020-01-27T20:43:30.306Z",
        "tags": {}
    }
}
```

For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html) in the *EC2 Image Builder Users Guide*.

## Output

requestId -> (string)

The request ID that uniquely identifies this request.

component -> (structure)

The component object specified in the request.

arn -> (string)

The Amazon Resource Name (ARN) of the component.

name -> (string)

The name of the component.

version -> (string)

The version of the component.

description -> (string)

The description of the component.

changeDescription -> (string)

Describes what change has been made in this version of the component, or what makes this version different from other versions of the component.

type -> (string)

The component type specifies whether Image Builder uses the component to build the image or only to test it.

platform -> (string)

The operating system platform of the component.

supportedOsVersions -> (list)

The operating system (OS) version supported by the component. If the OS information is available, Image Builder performs a prefix match against the base image OS version during image recipe creation.

(string)

state -> (structure)

Describes the current status of the component.

status -> (string)

The current state of the component.

reason -> (string)

Describes how or why the component changed state.

parameters -> (list)

Contains parameter details for each of the parameters that the component document defined for the component.

(structure)

Defines a parameter that is used to provide configuration details for the component.

name -> (string)

The name of this input parameter.

type -> (string)

The type of input this parameter provides. The currently supported value is âstringâ.

defaultValue -> (list)

The default value of this parameter if no input is provided.

(string)

description -> (string)

Describes this parameter.

owner -> (string)

The owner of the component.

data -> (string)

Component data contains the YAML document content for the component.

kmsKeyId -> (string)

The KMS key identifier used to encrypt the component.

encrypted -> (boolean)

The encryption status of the component.

dateCreated -> (string)

The date that Image Builder created the component.

tags -> (map)

The tags that apply to the component.

key -> (string)

value -> (string)

publisher -> (string)

Contains the name of the publisher if this is a third-party component. Otherwise, this property is empty.

obfuscate -> (boolean)

Indicates whether component source is hidden from view in the console, and from component detail results for API, CLI, or SDK operations.

productCodes -> (list)

Contains product codes that are used for billing purposes for Amazon Web Services Marketplace components.

(structure)

Information about a single product code.

productCodeId -> (string)

For Amazon Web Services Marketplace components, this contains the product code ID that can be stamped onto an EC2 AMI to ensure that components are billed correctly. If this property is empty, it might mean that the component is not published.

productCodeType -> (string)

The owner of the product code thatâs billed. If this property is empty, it might mean that the component is not published.