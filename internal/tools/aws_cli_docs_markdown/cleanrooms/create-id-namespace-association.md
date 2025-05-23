# create-id-namespace-associationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/create-id-namespace-association.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/create-id-namespace-association.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# create-id-namespace-association

## Description

Creates an ID namespace association.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/CreateIdNamespaceAssociation)

`create-id-namespace-association` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
create-id-namespace-association
--membership-identifier <value>
--input-reference-config <value>
[--tags <value>]
--name <value>
[--description <value>]
[--id-mapping-config <value>]
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

`--membership-identifier` (string)

The unique identifier of the membership that contains the ID namespace association.

`--input-reference-config` (structure)

The input reference configuration needed to create the ID namespace association.

inputReferenceArn -> (string)

The Amazon Resource Name (ARN) of the Entity Resolution resource that is being associated to the collaboration. Valid resource ARNs are from the ID namespaces that you own.

manageResourcePolicies -> (boolean)

When `TRUE` , Clean Rooms manages permissions for the ID namespace association resource.

When `FALSE` , the resource owner manages permissions for the ID namespace association resource.

Shorthand Syntax:

```
inputReferenceArn=string,manageResourcePolicies=boolean
```

JSON Syntax:

```
{
  "inputReferenceArn": "string",
  "manageResourcePolicies": true|false
}
```

`--tags` (map)

An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

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

`--name` (string)

The name for the ID namespace association.

`--description` (string)

The description of the ID namespace association.

`--id-mapping-config` (structure)

The configuration settings for the ID mapping table.

allowUseAsDimensionColumn -> (boolean)

An indicator as to whether you can use your column as a dimension column in the ID mapping table (`TRUE` ) or not (`FALSE` ).

Default is `FALSE` .

Shorthand Syntax:

```
allowUseAsDimensionColumn=boolean
```

JSON Syntax:

```
{
  "allowUseAsDimensionColumn": true|false
}
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

idNamespaceAssociation -> (structure)

The ID namespace association that was created.

id -> (string)

The unique identifier for this ID namespace association.

arn -> (string)

The Amazon Resource Name (ARN) of the ID namespace association.

membershipId -> (string)

The unique identifier of the membership resource for this ID namespace association.

membershipArn -> (string)

The Amazon Resource Name (ARN) of the membership resource for this ID namespace association.

collaborationId -> (string)

The unique identifier of the collaboration that contains this ID namespace association.

collaborationArn -> (string)

The Amazon Resource Name (ARN) of the collaboration that contains this ID namespace association.

name -> (string)

The name of this ID namespace association.

description -> (string)

The description of the ID namespace association.

createTime -> (timestamp)

The time at which the ID namespace association was created.

updateTime -> (timestamp)

The most recent time at which the ID namespace association was updated.

inputReferenceConfig -> (structure)

The input reference configuration for the ID namespace association.

inputReferenceArn -> (string)

The Amazon Resource Name (ARN) of the Entity Resolution resource that is being associated to the collaboration. Valid resource ARNs are from the ID namespaces that you own.

manageResourcePolicies -> (boolean)

When `TRUE` , Clean Rooms manages permissions for the ID namespace association resource.

When `FALSE` , the resource owner manages permissions for the ID namespace association resource.

inputReferenceProperties -> (structure)

The input reference properties for the ID namespace association.

idNamespaceType -> (string)

The ID namespace type for this ID namespace association.

idMappingWorkflowsSupported -> (list)

Defines how ID mapping workflows are supported for this ID namespace association.

(document)

idMappingConfig -> (structure)

The configuration settings for the ID mapping table.

allowUseAsDimensionColumn -> (boolean)

An indicator as to whether you can use your column as a dimension column in the ID mapping table (`TRUE` ) or not (`FALSE` ).

Default is `FALSE` .