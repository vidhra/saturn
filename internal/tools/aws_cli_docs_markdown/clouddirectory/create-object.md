# create-objectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-object.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-object.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [clouddirectory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/index.html#cli-aws-clouddirectory) ]

# create-object

## Description

Creates an object in a  Directory . Additionally attaches the object to a parent, if a parent reference and `LinkName` is specified. An object is simply a collection of  Facet attributes. You can also use this API call to create a policy object, if the facet from which you create the object is a policy facet.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/CreateObject)

## Synopsis

```
create-object
--directory-arn <value>
--schema-facets <value>
[--object-attribute-list <value>]
[--parent-reference <value>]
[--link-name <value>]
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

`--directory-arn` (string)

The Amazon Resource Name (ARN) that is associated with the  Directory in which the object will be created. For more information, see  arns .

`--schema-facets` (list)

A list of schema facets to be associated with the object. Do not provide minor version components. See  SchemaFacet for details.

(structure)

A facet.

SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and [In-Place Schema Upgrade](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html) for a description of when to provide minor versions. If this value is set, FacetName must also be set.

FacetName -> (string)

The name of the facet. If this value is set, SchemaArn must also be set.

Shorthand Syntax:

```
SchemaArn=string,FacetName=string ...
```

JSON Syntax:

```
[
  {
    "SchemaArn": "string",
    "FacetName": "string"
  }
  ...
]
```

`--object-attribute-list` (list)

The attribute map whose attribute ARN contains the key and attribute value as the map value.

(structure)

The combination of an attribute key and an attribute value.

Key -> (structure)

The key of the attribute.

SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.

Value -> (structure)

The value of the attribute.

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

Shorthand Syntax:

```
Key={SchemaArn=string,FacetName=string,Name=string},Value={StringValue=string,BinaryValue=blob,BooleanValue=boolean,NumberValue=string,DatetimeValue=timestamp} ...
```

JSON Syntax:

```
[
  {
    "Key": {
      "SchemaArn": "string",
      "FacetName": "string",
      "Name": "string"
    },
    "Value": {
      "StringValue": "string",
      "BinaryValue": blob,
      "BooleanValue": true|false,
      "NumberValue": "string",
      "DatetimeValue": timestamp
    }
  }
  ...
]
```

`--parent-reference` (structure)

If specified, the parent reference to which this object will be attached.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

Shorthand Syntax:

```
Selector=string
```

JSON Syntax:

```
{
  "Selector": "string"
}
```

`--link-name` (string)

The name of link that is used to attach this object to a parent.

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

ObjectIdentifier -> (string)

The identifier that is associated with the object.