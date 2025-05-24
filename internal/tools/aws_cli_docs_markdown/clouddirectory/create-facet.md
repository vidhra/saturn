# create-facetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-facet.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-facet.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [clouddirectory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/index.html#cli-aws-clouddirectory) ]

# create-facet

## Description

Creates a new  Facet in a schema. Facet creation is allowed only in development or applied schemas.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/CreateFacet)

## Synopsis

```
create-facet
--schema-arn <value>
--name <value>
[--attributes <value>]
[--object-type <value>]
[--facet-style <value>]
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

`--schema-arn` (string)

The schema ARN in which the new  Facet will be created. For more information, see  arns .

`--name` (string)

The name of the  Facet , which is unique for a given schema.

`--attributes` (list)

The attributes that are associated with the  Facet .

(structure)

An attribute that is associated with the  Facet .

Name -> (string)

The name of the facet attribute.

AttributeDefinition -> (structure)

A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See [Attribute References](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html) for more information.

Type -> (string)

The type of the attribute.

DefaultValue -> (structure)

The default value of the attribute (if configured).

StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.

IsImmutable -> (boolean)

Whether the attribute is mutable or not.

Rules -> (map)

Validation rules attached to the attribute definition.

key -> (string)

value -> (structure)

Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

Type -> (string)

The type of attribute validation rule.

Parameters -> (map)

The minimum and maximum parameters that are associated with the rule.

key -> (string)

value -> (string)

AttributeReference -> (structure)

An attribute reference that is associated with the attribute. See [Attribute References](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html) for more information.

TargetFacetName -> (string)

The target facet name that is associated with the facet reference. See [Attribute References](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html) for more information.

TargetAttributeName -> (string)

The target attribute name that is associated with the facet reference. See [Attribute References](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html) for more information.

RequiredBehavior -> (string)

The required behavior of the `FacetAttribute` .

Shorthand Syntax:

```
Name=string,AttributeDefinition={Type=string,DefaultValue={StringValue=string,BinaryValue=blob,BooleanValue=boolean,NumberValue=string,DatetimeValue=timestamp},IsImmutable=boolean,Rules={KeyName1={Type=string,Parameters={KeyName1=string,KeyName2=string}},KeyName2={Type=string,Parameters={KeyName1=string,KeyName2=string}}}},AttributeReference={TargetFacetName=string,TargetAttributeName=string},RequiredBehavior=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "AttributeDefinition": {
      "Type": "STRING"|"BINARY"|"BOOLEAN"|"NUMBER"|"DATETIME"|"VARIANT",
      "DefaultValue": {
        "StringValue": "string",
        "BinaryValue": blob,
        "BooleanValue": true|false,
        "NumberValue": "string",
        "DatetimeValue": timestamp
      },
      "IsImmutable": true|false,
      "Rules": {"string": {
            "Type": "BINARY_LENGTH"|"NUMBER_COMPARISON"|"STRING_FROM_SET"|"STRING_LENGTH",
            "Parameters": {"string": "string"
              ...}
          }
        ...}
    },
    "AttributeReference": {
      "TargetFacetName": "string",
      "TargetAttributeName": "string"
    },
    "RequiredBehavior": "REQUIRED_ALWAYS"|"NOT_REQUIRED"
  }
  ...
]
```

`--object-type` (string)

Specifies whether a given object created from this facet is of type node, leaf node, policy or index.

- Node: Can have multiple children but one parent.
- Leaf node: Cannot have children but can have multiple parents.
- Policy: Allows you to store a policy document and policy type. For more information, see [Policies](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies) .
- Index: Can be created with the Index API.

Possible values:

- `NODE`
- `LEAF_NODE`
- `POLICY`
- `INDEX`

`--facet-style` (string)

There are two different styles that you can define on any given facet, `Static` and `Dynamic` . For static facets, all attributes must be defined in the schema. For dynamic facets, attributes can be defined during data plane operations.

Possible values:

- `STATIC`
- `DYNAMIC`

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

None