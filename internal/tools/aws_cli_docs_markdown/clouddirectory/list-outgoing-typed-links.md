# list-outgoing-typed-linksÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-outgoing-typed-links.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-outgoing-typed-links.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [clouddirectory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/index.html#cli-aws-clouddirectory) ]

# list-outgoing-typed-links

## Description

Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/ListOutgoingTypedLinks)

`list-outgoing-typed-links` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `TypedLinkSpecifiers`

## Synopsis

```
list-outgoing-typed-links
--directory-arn <value>
--object-reference <value>
[--filter-attribute-ranges <value>]
[--filter-typed-link <value>]
[--consistency-level <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

The Amazon Resource Name (ARN) of the directory where you want to list the typed links.

`--object-reference` (structure)

A reference that identifies the object whose attributes will be listed.

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

`--filter-attribute-ranges` (list)

Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.

(structure)

Identifies the range of attributes that are used by a specified filter.

AttributeName -> (string)

The unique name of the typed link attribute.

Range -> (structure)

The range of attribute values that are being selected.

StartMode -> (string)

The inclusive or exclusive range start.

StartValue -> (structure)

The value to start the range at.

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

EndMode -> (string)

The inclusive or exclusive range end.

EndValue -> (structure)

The attribute value to terminate the range at.

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
AttributeName=string,Range={StartMode=string,StartValue={StringValue=string,BinaryValue=blob,BooleanValue=boolean,NumberValue=string,DatetimeValue=timestamp},EndMode=string,EndValue={StringValue=string,BinaryValue=blob,BooleanValue=boolean,NumberValue=string,DatetimeValue=timestamp}} ...
```

JSON Syntax:

```
[
  {
    "AttributeName": "string",
    "Range": {
      "StartMode": "FIRST"|"LAST"|"LAST_BEFORE_MISSING_VALUES"|"INCLUSIVE"|"EXCLUSIVE",
      "StartValue": {
        "StringValue": "string",
        "BinaryValue": blob,
        "BooleanValue": true|false,
        "NumberValue": "string",
        "DatetimeValue": timestamp
      },
      "EndMode": "FIRST"|"LAST"|"LAST_BEFORE_MISSING_VALUES"|"INCLUSIVE"|"EXCLUSIVE",
      "EndValue": {
        "StringValue": "string",
        "BinaryValue": blob,
        "BooleanValue": true|false,
        "NumberValue": "string",
        "DatetimeValue": timestamp
      }
    }
  }
  ...
]
```

`--filter-typed-link` (structure)

Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.

SchemaArn -> (string)

The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName -> (string)

The unique name of the typed link facet.

Shorthand Syntax:

```
SchemaArn=string,TypedLinkName=string
```

JSON Syntax:

```
{
  "SchemaArn": "string",
  "TypedLinkName": "string"
}
```

`--consistency-level` (string)

The consistency level to execute the request at.

Possible values:

- `SERIALIZABLE`
- `EVENTUAL`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

TypedLinkSpecifiers -> (list)

Returns a typed link specifier as output.

(structure)

Contains all the information that is used to uniquely identify a typed link. The parameters discussed in this topic are used to uniquely specify the typed link being operated on. The  AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can also construct a typed link specifier from scratch.

TypedLinkFacet -> (structure)

Identifies the typed link facet that is associated with the typed link.

SchemaArn -> (string)

The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName -> (string)

The unique name of the typed link facet.

SourceObjectReference -> (structure)

Identifies the source object that the typed link will attach to.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

TargetObjectReference -> (structure)

Identifies the target object that the typed link will attach to.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

IdentityAttributeValues -> (list)

Identifies the attribute value to update.

(structure)

Identifies the attribute name and value for a typed link.

AttributeName -> (string)

The attribute name of the typed link.

Value -> (structure)

The value for the typed link.

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

NextToken -> (string)

The pagination token.