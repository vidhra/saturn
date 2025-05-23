# delete-service-template-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-service-template-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-service-template-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [proton](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html#cli-aws-proton) ]

# delete-service-template-version

## Description

If no other minor versions of a service template exist, delete a major version of the service template if itâs not the `Recommended` version. Delete the `Recommended` version of the service template if no other major versions or minor versions of the service template exist. A major version of a service template is a version that *isnât* backwards compatible.

Delete a minor version of a service template if itâs not the `Recommended` version. Delete a `Recommended` minor version of the service template if no other minor versions of the service template exist. A minor version of a service template is a version thatâs backwards compatible.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/proton-2020-07-20/DeleteServiceTemplateVersion)

## Synopsis

```
delete-service-template-version
--major-version <value>
--minor-version <value>
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

`--major-version` (string)

The service template major version to delete.

`--minor-version` (string)

The service template minor version to delete.

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

The detailed data of the service template version being deleted.

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