# create-service-template-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-service-template-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-service-template-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [proton](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html#cli-aws-proton) ]

# create-service-template-version

## Description

Create a new major or minor version of a service template. A major version of a service template is a version that *isnât* backward compatible. A minor version of a service template is a version thatâs backward compatible within its major version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/proton-2020-07-20/CreateServiceTemplateVersion)

## Synopsis

```
create-service-template-version
[--client-token <value>]
--compatible-environment-templates <value>
[--description <value>]
[--major-version <value>]
--source <value>
[--supported-component-sources <value>]
[--tags <value>]
--template-name <value>
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

`--client-token` (string)

When included, if two identical requests are made with the same client token, Proton returns the service template version that the first request created.

`--compatible-environment-templates` (list)

An array of environment template objects that are compatible with the new service template version. A service instance based on this service template version can run in environments based on compatible templates.

(structure)

Compatible environment template data.

majorVersion -> (string)

The major version of the compatible environment template.

templateName -> (string)

The compatible environment template name.

Shorthand Syntax:

```
majorVersion=string,templateName=string ...
```

JSON Syntax:

```
[
  {
    "majorVersion": "string",
    "templateName": "string"
  }
  ...
]
```

`--description` (string)

A description of the new version of a service template.

`--major-version` (string)

To create a new minor version of the service template, include a `major Version` .

To create a new major and minor version of the service template, *exclude* `major Version` .

`--source` (tagged union structure)

An object that includes the template bundle S3 bucket path and name for the new version of a service template.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.

s3 -> (structure)

An S3 source object that includes the template bundle S3 path and name for a template minor version.

bucket -> (string)

The name of the S3 bucket that contains a template bundle.

key -> (string)

The path to the S3 bucket that contains a template bundle.

Shorthand Syntax:

```
s3={bucket=string,key=string}
```

JSON Syntax:

```
{
  "s3": {
    "bucket": "string",
    "key": "string"
  }
}
```

`--supported-component-sources` (list)

An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.

For more information about components, see [Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the *Proton User Guide* .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  DIRECTLY_DEFINED
```

`--tags` (list)

An optional list of metadata items that you can associate with the Proton service template version. A tag is a key-value pair.

For more information, see [Proton resources and tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html) in the *Proton User Guide* .

(structure)

A description of a resource tag.

key -> (string)

The key of the resource tag.

value -> (string)

The value of the resource tag.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--template-name` (string)

The name of the service template.

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

serviceTemplateVersion -> (structure)

The service template version summary of detail data thatâs returned by Proton.

arn -> (string)

The Amazon Resource Name (ARN) of the version of a service template.

compatibleEnvironmentTemplates -> (list)

An array of compatible environment template names for the major version of a service template.

(structure)

Compatible environment template data.

majorVersion -> (string)

The major version of the compatible environment template.

templateName -> (string)

The compatible environment template name.

createdAt -> (timestamp)

The time when the version of a service template was created.

description -> (string)

A description of the version of a service template.

lastModifiedAt -> (timestamp)

The time when the version of a service template was last modified.

majorVersion -> (string)

The latest major version thatâs associated with the version of a service template.

minorVersion -> (string)

The minor version of a service template.

recommendedMinorVersion -> (string)

The recommended minor version of the service template.

schema -> (string)

The schema of the version of a service template.

status -> (string)

The service template version status.

statusMessage -> (string)

A service template version status message.

supportedComponentSources -> (list)

An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.

For more information about components, see [Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the *Proton User Guide* .

(string)

templateName -> (string)

The name of the version of a service template.