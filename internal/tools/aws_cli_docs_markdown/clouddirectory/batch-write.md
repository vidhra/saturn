# batch-writeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/batch-write.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/batch-write.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [clouddirectory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/index.html#cli-aws-clouddirectory) ]

# batch-write

## Description

Performs all the write operations in a batch. Either all the operations succeed or none.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/clouddirectory-2017-01-11/BatchWrite)

## Synopsis

```
batch-write
--directory-arn <value>
--operations <value>
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

Represents the output of a `BatchWrite` operation.

CreateObject -> (structure)

Creates an object.

SchemaFacet -> (list)

A list of `FacetArns` that will be associated with the object. For more information, see  arns .

(structure)

A facet.

SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and [In-Place Schema Upgrade](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html) for a description of when to provide minor versions. If this value is set, FacetName must also be set.

FacetName -> (string)

The name of the facet. If this value is set, SchemaArn must also be set.

ObjectAttributeList -> (list)

An attribute map, which contains an attribute ARN as the key and attribute value as the map value.

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

ParentReference -> (structure)

If specified, the parent reference to which this object will be attached.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

LinkName -> (string)

The name of the link.

BatchReferenceName -> (string)

The batch reference name. See [Transaction Support](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html) for more information.

AttachObject -> (structure)

Attaches an object to a  Directory .

ParentReference -> (structure)

The parent object reference.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

ChildReference -> (structure)

The child object reference that is to be attached to the object.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

LinkName -> (string)

The name of the link.

DetachObject -> (structure)

Detaches an object from a  Directory .

ParentReference -> (structure)

Parent reference from which the object with the specified link name is detached.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

LinkName -> (string)

The name of the link.

BatchReferenceName -> (string)

The batch reference name. See [Transaction Support](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html) for more information.

UpdateObjectAttributes -> (structure)

Updates a given objectâs attributes.

ObjectReference -> (structure)

Reference that identifies the object.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

AttributeUpdates -> (list)

Attributes update structure.

(structure)

Structure that contains attribute update information.

ObjectAttributeKey -> (structure)

The key of the attribute being updated.

SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.

ObjectAttributeAction -> (structure)

The action to perform as part of the attribute update.

ObjectAttributeActionType -> (string)

A type that can be either `Update` or `Delete` .

ObjectAttributeUpdateValue -> (structure)

The value that you want to update to.

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

DeleteObject -> (structure)

Deletes an object in a  Directory .

ObjectReference -> (structure)

The reference that identifies the object.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

AddFacetToObject -> (structure)

A batch operation that adds a facet to an object.

SchemaFacet -> (structure)

Represents the facet being added to the object.

SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and [In-Place Schema Upgrade](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html) for a description of when to provide minor versions. If this value is set, FacetName must also be set.

FacetName -> (string)

The name of the facet. If this value is set, SchemaArn must also be set.

ObjectAttributeList -> (list)

The attributes to set on the object.

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

ObjectReference -> (structure)

A reference to the object being mutated.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

RemoveFacetFromObject -> (structure)

A batch operation that removes a facet from an object.

SchemaFacet -> (structure)

The facet to remove from the object.

SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and [In-Place Schema Upgrade](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html) for a description of when to provide minor versions. If this value is set, FacetName must also be set.

FacetName -> (string)

The name of the facet. If this value is set, SchemaArn must also be set.

ObjectReference -> (structure)

A reference to the object whose facet will be removed.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

AttachPolicy -> (structure)

Attaches a policy object to a regular object. An object can have a limited number of attached policies.

PolicyReference -> (structure)

The reference that is associated with the policy object.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

ObjectReference -> (structure)

The reference that identifies the object to which the policy will be attached.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

DetachPolicy -> (structure)

Detaches a policy from a  Directory .

PolicyReference -> (structure)

Reference that identifies the policy object.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

ObjectReference -> (structure)

Reference that identifies the object whose policy object will be detached.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

CreateIndex -> (structure)

Creates an index object. See [Indexing and search](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm) for more information.

OrderedIndexedAttributeList -> (list)

Specifies the attributes that should be indexed on. Currently only a single attribute is supported.

(structure)

A unique identifier for an attribute.

SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.

IsUnique -> (boolean)

Indicates whether the attribute that is being indexed has unique values or not.

ParentReference -> (structure)

A reference to the parent object that contains the index object.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

LinkName -> (string)

The name of the link between the parent object and the index object.

BatchReferenceName -> (string)

The batch reference name. See [Transaction Support](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html) for more information.

AttachToIndex -> (structure)

Attaches the specified object to the specified index.

IndexReference -> (structure)

A reference to the index that you are attaching the object to.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

TargetReference -> (structure)

A reference to the object that you are attaching to the index.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

DetachFromIndex -> (structure)

Detaches the specified object from the specified index.

IndexReference -> (structure)

A reference to the index object.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

TargetReference -> (structure)

A reference to the object being detached from the index.

Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html) . You can identify an object in one of the following ways:

- *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
- */some/path* - Identifies the object based on path
- *#SomeBatchReference* - Identifies the object in a batch call

AttachTypedLink -> (structure)

Attaches a typed link to a specified source and target object. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink) .

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

TypedLinkFacet -> (structure)

Identifies the typed link facet that is associated with the typed link.

SchemaArn -> (string)

The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName -> (string)

The unique name of the typed link facet.

Attributes -> (list)

A set of attributes that are associated with the typed link.

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

DetachTypedLink -> (structure)

Detaches a typed link from a specified source and target object. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink) .

TypedLinkSpecifier -> (structure)

Used to accept a typed link specifier as input.

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

UpdateLinkAttributes -> (structure)

Updates a given objectâs attributes.

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

AttributeUpdates -> (list)

The attributes update structure.

(structure)

Structure that contains attribute update information.

AttributeKey -> (structure)

The key of the attribute being updated.

SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.

AttributeAction -> (structure)

The action to perform as part of the attribute update.

AttributeActionType -> (string)

A type that can be either `UPDATE_OR_CREATE` or `DELETE` .

AttributeUpdateValue -> (structure)

The value that you want to update to.

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

JSON Syntax:

```
[
  {
    "CreateObject": {
      "SchemaFacet": [
        {
          "SchemaArn": "string",
          "FacetName": "string"
        }
        ...
      ],
      "ObjectAttributeList": [
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
      ],
      "ParentReference": {
        "Selector": "string"
      },
      "LinkName": "string",
      "BatchReferenceName": "string"
    },
    "AttachObject": {
      "ParentReference": {
        "Selector": "string"
      },
      "ChildReference": {
        "Selector": "string"
      },
      "LinkName": "string"
    },
    "DetachObject": {
      "ParentReference": {
        "Selector": "string"
      },
      "LinkName": "string",
      "BatchReferenceName": "string"
    },
    "UpdateObjectAttributes": {
      "ObjectReference": {
        "Selector": "string"
      },
      "AttributeUpdates": [
        {
          "ObjectAttributeKey": {
            "SchemaArn": "string",
            "FacetName": "string",
            "Name": "string"
          },
          "ObjectAttributeAction": {
            "ObjectAttributeActionType": "CREATE_OR_UPDATE"|"DELETE",
            "ObjectAttributeUpdateValue": {
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
    },
    "DeleteObject": {
      "ObjectReference": {
        "Selector": "string"
      }
    },
    "AddFacetToObject": {
      "SchemaFacet": {
        "SchemaArn": "string",
        "FacetName": "string"
      },
      "ObjectAttributeList": [
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
      ],
      "ObjectReference": {
        "Selector": "string"
      }
    },
    "RemoveFacetFromObject": {
      "SchemaFacet": {
        "SchemaArn": "string",
        "FacetName": "string"
      },
      "ObjectReference": {
        "Selector": "string"
      }
    },
    "AttachPolicy": {
      "PolicyReference": {
        "Selector": "string"
      },
      "ObjectReference": {
        "Selector": "string"
      }
    },
    "DetachPolicy": {
      "PolicyReference": {
        "Selector": "string"
      },
      "ObjectReference": {
        "Selector": "string"
      }
    },
    "CreateIndex": {
      "OrderedIndexedAttributeList": [
        {
          "SchemaArn": "string",
          "FacetName": "string",
          "Name": "string"
        }
        ...
      ],
      "IsUnique": true|false,
      "ParentReference": {
        "Selector": "string"
      },
      "LinkName": "string",
      "BatchReferenceName": "string"
    },
    "AttachToIndex": {
      "IndexReference": {
        "Selector": "string"
      },
      "TargetReference": {
        "Selector": "string"
      }
    },
    "DetachFromIndex": {
      "IndexReference": {
        "Selector": "string"
      },
      "TargetReference": {
        "Selector": "string"
      }
    },
    "AttachTypedLink": {
      "SourceObjectReference": {
        "Selector": "string"
      },
      "TargetObjectReference": {
        "Selector": "string"
      },
      "TypedLinkFacet": {
        "SchemaArn": "string",
        "TypedLinkName": "string"
      },
      "Attributes": [
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
    "DetachTypedLink": {
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
      }
    },
    "UpdateLinkAttributes": {
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
      "AttributeUpdates": [
        {
          "AttributeKey": {
            "SchemaArn": "string",
            "FacetName": "string",
            "Name": "string"
          },
          "AttributeAction": {
            "AttributeActionType": "CREATE_OR_UPDATE"|"DELETE",
            "AttributeUpdateValue": {
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
    }
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

Responses -> (list)

A list of all the responses for each batch write.

(structure)

Represents the output of a `BatchWrite` response operation.

CreateObject -> (structure)

Creates an object in a  Directory .

ObjectIdentifier -> (string)

The ID that is associated with the object.

AttachObject -> (structure)

Attaches an object to a  Directory .

attachedObjectIdentifier -> (string)

The `ObjectIdentifier` of the object that has been attached.

DetachObject -> (structure)

Detaches an object from a  Directory .

detachedObjectIdentifier -> (string)

The `ObjectIdentifier` of the detached object.

UpdateObjectAttributes -> (structure)

Updates a given objectâs attributes.

ObjectIdentifier -> (string)

ID that is associated with the object.

DeleteObject -> (structure)

Deletes an object in a  Directory .

AddFacetToObject -> (structure)

The result of an add facet to object batch operation.

RemoveFacetFromObject -> (structure)

The result of a batch remove facet from object operation.

AttachPolicy -> (structure)

Attaches a policy object to a regular object. An object can have a limited number of attached policies.

DetachPolicy -> (structure)

Detaches a policy from a  Directory .

CreateIndex -> (structure)

Creates an index object. See [Indexing and search](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm) for more information.

ObjectIdentifier -> (string)

The `ObjectIdentifier` of the index created by this operation.

AttachToIndex -> (structure)

Attaches the specified object to the specified index.

AttachedObjectIdentifier -> (string)

The `ObjectIdentifier` of the object that was attached to the index.

DetachFromIndex -> (structure)

Detaches the specified object from the specified index.

DetachedObjectIdentifier -> (string)

The `ObjectIdentifier` of the object that was detached from the index.

AttachTypedLink -> (structure)

Attaches a typed link to a specified source and target object. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink) .

TypedLinkSpecifier -> (structure)

Returns a typed link specifier as output.

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

DetachTypedLink -> (structure)

Detaches a typed link from a specified source and target object. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink) .

UpdateLinkAttributes -> (structure)

Represents the output of a `BatchWrite` response operation.