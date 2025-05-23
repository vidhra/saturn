# batch-readÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/batch-read.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/batch-read.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [clouddirectory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/index.html#cli-aws-clouddirectory) ]

# batch-read

## Description

Performs all the read operations in a batch.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/BatchRead)

## Synopsis

```
batch-read
--directory-arn <value>
--operations <value>
[--consistency-level <value>]
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

The Amazon Resource Name (ARN) that is associated with the  Directory . For more information, see  arns .

`--operations` (list)

A list of operations that are part of the batch.

(structure)

Represents the output of a `BatchRead` operation.

ListObjectAttributes -> (structure)

Lists all attributes that are associated with an object.

ObjectReference -> (structure)

Reference of the object whose attributes need to be listed.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of items to be retrieved in a single call. This is an approximate number.

FacetFilter -> (structure)

Used to filter the list of object attributes that are associated with a certain facet.

SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and [In-Place Schema Upgrade](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html) for a description of when to provide minor versions. If this value is set, FacetName must also be set.

FacetName -> (string)

The name of the facet. If this value is set, SchemaArn must also be set.

ListObjectChildren -> (structure)

Returns a paginated list of child objects that are associated with a given object.

ObjectReference -> (structure)

Reference of the object for which child objects are being listed.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

NextToken -> (string)

The pagination token.

MaxResults -> (integer)

Maximum number of items to be retrieved in a single call. This is an approximate number.

ListAttachedIndices -> (structure)

Lists indices attached to an object.

TargetReference -> (structure)

A reference to the object that has indices attached.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.

ListObjectParentPaths -> (structure)

Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see [Directory Structure](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html) .

ObjectReference -> (structure)

The reference that identifies the object whose attributes will be listed.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.

GetObjectInformation -> (structure)

Retrieves metadata about an object.

ObjectReference -> (structure)

A reference to the object.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

GetObjectAttributes -> (structure)

Retrieves attributes within a facet that are associated with an object.

ObjectReference -> (structure)

Reference that identifies the object whose attributes will be retrieved.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

SchemaFacet -> (structure)

Identifier for the facet whose attributes will be retrieved. See  SchemaFacet for details.

SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and [In-Place Schema Upgrade](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html) for a description of when to provide minor versions. If this value is set, FacetName must also be set.

FacetName -> (string)

The name of the facet. If this value is set, SchemaArn must also be set.

AttributeNames -> (list)

List of attribute names whose values will be retrieved.

(string)

ListObjectParents -> (structure)

Lists parent objects that are associated with a given object in pagination fashion.

ObjectReference -> (structure)

The reference that identifies an object.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of items to be retrieved in a single call. This is an approximate number.

ListObjectPolicies -> (structure)

Returns policies attached to an object in pagination fashion.

ObjectReference -> (structure)

The reference that identifies the object whose attributes will be listed.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.

ListPolicyAttachments -> (structure)

Returns all of the `ObjectIdentifiers` to which a given policy is attached.

PolicyReference -> (structure)

The reference that identifies the policy object.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.

LookupPolicy -> (structure)

Lists all policies from the root of the  Directory to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects donât have the policies attached, it returns the `ObjectIdentifier` for such objects. If policies are present, it returns `ObjectIdentifier` , `policyId` , and `policyType` . Paths that donât lead to the root from the target object are ignored. For more information, see [Policies](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies) .

ObjectReference -> (structure)

Reference that identifies the object whose policies will be looked up.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.

ListIndex -> (structure)

Lists objects attached to the specified index.

RangesOnIndexedValues -> (list)

Specifies the ranges of indexed values that you want to query.

(structure)

A range of attributes.

AttributeKey -> (structure)

The key of the attribute that the attribute range covers.

SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.

Range -> (structure)

The range of attribute values being selected.

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

IndexReference -> (structure)

The reference to the index to list.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

MaxResults -> (integer)

The maximum number of results to retrieve.

NextToken -> (string)

The pagination token.

ListOutgoingTypedLinks -> (structure)

Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink) .

ObjectReference -> (structure)

The reference that identifies the object whose attributes will be listed.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

FilterAttributeRanges -> (list)

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

FilterTypedLink -> (structure)

Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.

SchemaArn -> (string)

The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName -> (string)

The unique name of the typed link facet.

NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.

ListIncomingTypedLinks -> (structure)

Returns a paginated list of all the incoming  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink) .

ObjectReference -> (structure)

The reference that identifies the object whose attributes will be listed.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

FilterAttributeRanges -> (list)

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

FilterTypedLink -> (structure)

Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls.

SchemaArn -> (string)

The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName -> (string)

The unique name of the typed link facet.

NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.

GetLinkAttributes -> (structure)

Retrieves attributes that are associated with a typed link.

TypedLinkSpecifier -> (structure)

Allows a typed link specifier to be accepted as input.

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

AttributeNames -> (list)

A list of attribute names whose values will be retrieved.

(string)

JSON Syntax:

```
[
  {
    "ListObjectAttributes": {
      "ObjectReference": {
        "Selector": "string"
      },
      "NextToken": "string",
      "MaxResults": integer,
      "FacetFilter": {
        "SchemaArn": "string",
        "FacetName": "string"
      }
    },
    "ListObjectChildren": {
      "ObjectReference": {
        "Selector": "string"
      },
      "NextToken": "string",
      "MaxResults": integer
    },
    "ListAttachedIndices": {
      "TargetReference": {
        "Selector": "string"
      },
      "NextToken": "string",
      "MaxResults": integer
    },
    "ListObjectParentPaths": {
      "ObjectReference": {
        "Selector": "string"
      },
      "NextToken": "string",
      "MaxResults": integer
    },
    "GetObjectInformation": {
      "ObjectReference": {
        "Selector": "string"
      }
    },
    "GetObjectAttributes": {
      "ObjectReference": {
        "Selector": "string"
      },
      "SchemaFacet": {
        "SchemaArn": "string",
        "FacetName": "string"
      },
      "AttributeNames": ["string", ...]
    },
    "ListObjectParents": {
      "ObjectReference": {
        "Selector": "string"
      },
      "NextToken": "string",
      "MaxResults": integer
    },
    "ListObjectPolicies": {
      "ObjectReference": {
        "Selector": "string"
      },
      "NextToken": "string",
      "MaxResults": integer
    },
    "ListPolicyAttachments": {
      "PolicyReference": {
        "Selector": "string"
      },
      "NextToken": "string",
      "MaxResults": integer
    },
    "LookupPolicy": {
      "ObjectReference": {
        "Selector": "string"
      },
      "NextToken": "string",
      "MaxResults": integer
    },
    "ListIndex": {
      "RangesOnIndexedValues": [
        {
          "AttributeKey": {
            "SchemaArn": "string",
            "FacetName": "string",
            "Name": "string"
          },
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
      ],
      "IndexReference": {
        "Selector": "string"
      },
      "MaxResults": integer,
      "NextToken": "string"
    },
    "ListOutgoingTypedLinks": {
      "ObjectReference": {
        "Selector": "string"
      },
      "FilterAttributeRanges": [
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
      ],
      "FilterTypedLink": {
        "SchemaArn": "string",
        "TypedLinkName": "string"
      },
      "NextToken": "string",
      "MaxResults": integer
    },
    "ListIncomingTypedLinks": {
      "ObjectReference": {
        "Selector": "string"
      },
      "FilterAttributeRanges": [
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
      ],
      "FilterTypedLink": {
        "SchemaArn": "string",
        "TypedLinkName": "string"
      },
      "NextToken": "string",
      "MaxResults": integer
    },
    "GetLinkAttributes": {
      "TypedLinkSpecifier": {
        "TypedLinkFacet": {
          "SchemaArn": "string",
          "TypedLinkName": "string"
        },
        "SourceObjectReference": {
          "Selector": "string"
        },
        "TargetObjectReference": {
          "Selector": "string"
        },
        "IdentityAttributeValues": [
          {
            "AttributeName": "string",
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
      },
      "AttributeNames": ["string", ...]
    }
  }
  ...
]
```

`--consistency-level` (string)

Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.

Possible values:

- `SERIALIZABLE`
- `EVENTUAL`

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

Responses -> (list)

A list of all the responses for each batch read.

(structure)

Represents the output of a `BatchRead` response operation.

SuccessfulResponse -> (structure)

Identifies which operation in a batch has succeeded.

ListObjectAttributes -> (structure)

Lists all attributes that are associated with an object.

Attributes -> (list)

The attributes map that is associated with the object. `AttributeArn` is the key; attribute value is the value.

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

NextToken -> (string)

The pagination token.

ListObjectChildren -> (structure)

Returns a paginated list of child objects that are associated with a given object.

Children -> (map)

The children structure, which is a map with the key as the `LinkName` and `ObjectIdentifier` as the value.

key -> (string)

value -> (string)

NextToken -> (string)

The pagination token.

GetObjectInformation -> (structure)

Retrieves metadata about an object.

SchemaFacets -> (list)

The facets attached to the specified object.

(structure)

A facet.

SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and [In-Place Schema Upgrade](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html) for a description of when to provide minor versions. If this value is set, FacetName must also be set.

FacetName -> (string)

The name of the facet. If this value is set, SchemaArn must also be set.

ObjectIdentifier -> (string)

The `ObjectIdentifier` of the specified object.

GetObjectAttributes -> (structure)

Retrieves attributes within a facet that are associated with an object.

Attributes -> (list)

The attribute values that are associated with an object.

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

ListAttachedIndices -> (structure)

Lists indices attached to an object.

IndexAttachments -> (list)

The indices attached to the specified object.

(structure)

Represents an index and an attached object.

IndexedAttributes -> (list)

The indexed attribute values.

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

ObjectIdentifier -> (string)

In response to  ListIndex , the `ObjectIdentifier` of the object attached to the index. In response to  ListAttachedIndices , the `ObjectIdentifier` of the index attached to the object. This field will always contain the `ObjectIdentifier` of the object on the opposite side of the attachment specified in the query.

NextToken -> (string)

The pagination token.

ListObjectParentPaths -> (structure)

Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see [Directory Structure](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html) .

PathToObjectIdentifiersList -> (list)

Returns the path to the `ObjectIdentifiers` that are associated with the directory.

(structure)

Returns the path to the `ObjectIdentifiers` that is associated with the directory.

Path -> (string)

The path that is used to identify the object starting from directory root.

ObjectIdentifiers -> (list)

Lists `ObjectIdentifiers` starting from directory root to the object in the request.

(string)

NextToken -> (string)

The pagination token.

ListObjectPolicies -> (structure)

Returns policies attached to an object in pagination fashion.

AttachedPolicyIds -> (list)

A list of policy `ObjectIdentifiers` , that are attached to the object.

(string)

NextToken -> (string)

The pagination token.

ListPolicyAttachments -> (structure)

Returns all of the `ObjectIdentifiers` to which a given policy is attached.

ObjectIdentifiers -> (list)

A list of `ObjectIdentifiers` to which the policy is attached.

(string)

NextToken -> (string)

The pagination token.

LookupPolicy -> (structure)

Lists all policies from the root of the  Directory to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects donât have the policies attached, it returns the `ObjectIdentifier` for such objects. If policies are present, it returns `ObjectIdentifier` , `policyId` , and `policyType` . Paths that donât lead to the root from the target object are ignored. For more information, see [Policies](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies) .

PolicyToPathList -> (list)

Provides list of path to policies. Policies contain `PolicyId` , `ObjectIdentifier` , and `PolicyType` . For more information, see [Policies](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies) .

(structure)

Used when a regular object exists in a  Directory and you want to find all of the policies that are associated with that object and the parent to that object.

Path -> (string)

The path that is referenced from the root.

Policies -> (list)

List of policy objects.

(structure)

Contains the `PolicyType` , `PolicyId` , and the `ObjectIdentifier` to which it is attached. For more information, see [Policies](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies) .

PolicyId -> (string)

The ID of `PolicyAttachment` .

ObjectIdentifier -> (string)

The `ObjectIdentifier` that is associated with `PolicyAttachment` .

PolicyType -> (string)

The type of policy that can be associated with `PolicyAttachment` .

NextToken -> (string)

The pagination token.

ListIndex -> (structure)

Lists objects attached to the specified index.

IndexAttachments -> (list)

The objects and indexed values attached to the index.

(structure)

Represents an index and an attached object.

IndexedAttributes -> (list)

The indexed attribute values.

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

ObjectIdentifier -> (string)

In response to  ListIndex , the `ObjectIdentifier` of the object attached to the index. In response to  ListAttachedIndices , the `ObjectIdentifier` of the index attached to the object. This field will always contain the `ObjectIdentifier` of the object on the opposite side of the attachment specified in the query.

NextToken -> (string)

The pagination token.

ListOutgoingTypedLinks -> (structure)

Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink) .

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

ListIncomingTypedLinks -> (structure)

Returns a paginated list of all the incoming  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink) .

LinkSpecifiers -> (list)

Returns one or more typed link specifiers as output.

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

GetLinkAttributes -> (structure)

The list of attributes to retrieve from the typed link.

Attributes -> (list)

The attributes that are associated with the typed link.

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

ListObjectParents -> (structure)

The list of parent objects to retrieve.

ParentLinks -> (list)

Returns a list of parent reference and LinkName Tuples.

(structure)

A pair of ObjectIdentifier and LinkName.

ObjectIdentifier -> (string)

The ID that is associated with the object.

LinkName -> (string)

The name of the link between the parent and the child object.

NextToken -> (string)

The pagination token.

ExceptionResponse -> (structure)

Identifies which operation in a batch has failed.

Type -> (string)

A type of exception, such as `InvalidArnException` .

Message -> (string)

An exception message that is associated with the failure.