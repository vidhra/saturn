# create-service-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-service-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-service-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [proton](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html#cli-aws-proton) ]

# create-service-template

## Description

Create a service template. The administrator creates a service template to define standardized infrastructure and an optional CI/CD service pipeline. Developers, in turn, select the service template from Proton. If the selected service template includes a service pipeline definition, they provide a link to their source code repository. Proton then deploys and manages the infrastructure defined by the selected service template. For more information, see [Proton templates](https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html) in the *Proton User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/proton-2020-07-20/CreateServiceTemplate)

## Synopsis

```
create-service-template
[--description <value>]
[--display-name <value>]
[--encryption-key <value>]
--name <value>
[--pipeline-provisioning <value>]
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

`--description` (string)

A description of the service template.

`--display-name` (string)

The name of the service template as displayed in the developer interface.

`--encryption-key` (string)

A customer provided encryption key thatâs used to encrypt data.

`--name` (string)

The name of the service template.

`--pipeline-provisioning` (string)

By default, Proton provides a service pipeline for your service. When this parameter is included, it indicates that an Proton service pipeline *isnât* provided for your service. After itâs included, it *canât* be changed. For more information, see [Template bundles](https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles) in the *Proton User Guide* .

Possible values:

- `CUSTOMER_MANAGED`

`--tags` (list)

An optional list of metadata items that you can associate with the Proton service template. A tag is a key-value pair.

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

serviceTemplate -> (structure)

The service template detail data thatâs returned by Proton.

arn -> (string)

The Amazon Resource Name (ARN) of the service template.

createdAt -> (timestamp)

The time when the service template was created.

description -> (string)

A description of the service template.

displayName -> (string)

The service template name as displayed in the developer interface.

encryptionKey -> (string)

The customer provided service template encryption key thatâs used to encrypt data.

lastModifiedAt -> (timestamp)

The time when the service template was last modified.

name -> (string)

The name of the service template.

pipelineProvisioning -> (string)

If `pipelineProvisioning` is `true` , a service pipeline is included in the service template. Otherwise, a service pipeline *isnât* included in the service template.

recommendedVersion -> (string)

The recommended version of the service template.