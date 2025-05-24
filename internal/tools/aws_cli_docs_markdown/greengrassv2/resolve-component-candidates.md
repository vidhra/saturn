# resolve-component-candidatesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/resolve-component-candidates.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/resolve-component-candidates.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [greengrassv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/index.html#cli-aws-greengrassv2) ]

# resolve-component-candidates

## Description

Retrieves a list of components that meet the component, version, and platform requirements of a deployment. Greengrass core devices call this operation when they receive a deployment to identify the components to install.

This operation identifies components that meet all dependency requirements for a deployment. If the requirements conflict, then this operation returns an error and the deployment fails. For example, this occurs if component `A` requires version `>2.0.0` and component `B` requires version `<2.0.0` of a component dependency.

When you specify the component candidates to resolve, IoT Greengrass compares each componentâs digest from the core device with the componentâs digest in the Amazon Web Services Cloud. If the digests donât match, then IoT Greengrass specifies to use the version from the Amazon Web Services Cloud.

### Warning

To use this operation, you must use the data plane API endpoint and authenticate with an IoT device certificate. For more information, see [IoT Greengrass endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/greengrass.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/greengrassv2-2020-11-30/ResolveComponentCandidates)

## Synopsis

```
resolve-component-candidates
[--platform <value>]
[--component-candidates <value>]
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

`--platform` (structure)

The platform to use to resolve compatible components.

name -> (string)

The friendly name of the platform. This name helps you identify the platform.

If you omit this parameter, IoT Greengrass creates a friendly name from the `os` and `architecture` of the platform.

attributes -> (map)

A dictionary of attributes for the platform. The IoT Greengrass Core software defines the `os` and `architecture` by default. You can specify additional platform attributes for a core device when you deploy the Greengrass nucleus component. For more information, see the [Greengrass nucleus component](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html) in the *IoT Greengrass V2 Developer Guide* .

key -> (string)

value -> (string)

Shorthand Syntax:

```
name=string,attributes={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "name": "string",
  "attributes": {"string": "string"
    ...}
}
```

`--component-candidates` (list)

The list of components to resolve.

(structure)

Contains information about a component that is a candidate to deploy to a Greengrass core device.

componentName -> (string)

The name of the component.

componentVersion -> (string)

The version of the component.

versionRequirements -> (map)

The version requirements for the componentâs dependencies. Greengrass core devices get the version requirements from component recipes.

IoT Greengrass V2 uses semantic version constraints. For more information, see [Semantic Versioning](https://semver.org/) .

key -> (string)

value -> (string)

Shorthand Syntax:

```
componentName=string,componentVersion=string,versionRequirements={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "componentName": "string",
    "componentVersion": "string",
    "versionRequirements": {"string": "string"
      ...}
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

## Output

resolvedComponentVersions -> (list)

A list of components that meet the requirements that you specify in the request. This list includes each componentâs recipe that you can use to install the component.

(structure)

Contains information about a component version that is compatible to run on a Greengrass core device.

arn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the component version.

componentName -> (string)

The name of the component.

componentVersion -> (string)

The version of the component.

recipe -> (blob)

The recipe of the component version.

vendorGuidance -> (string)

The vendor guidance state for the component version. This state indicates whether the component version has any issues that you should consider before you deploy it. The vendor guidance state can be:

- `ACTIVE` â This component version is available and recommended for use.
- `DISCONTINUED` â This component version has been discontinued by its publisher. You can deploy this component version, but we recommend that you use a different version of this component.
- `DELETED` â This component version has been deleted by its publisher, so you canât deploy it. If you have any existing deployments that specify this component version, those deployments will fail.

message -> (string)

A message that communicates details about the vendor guidance state of the component version. This message communicates why a component version is discontinued or deleted.