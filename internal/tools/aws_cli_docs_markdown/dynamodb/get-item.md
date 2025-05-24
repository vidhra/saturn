# get-itemÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/get-item.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/get-item.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dynamodb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html#cli-aws-dynamodb) ]

# get-item

## Description

The `GetItem` operation returns a set of attributes for the item with the given primary key. If there is no matching item, `GetItem` does not return any data and there will be no `Item` element in the response.

`GetItem` provides an eventually consistent read by default. If your application requires a strongly consistent read, set `ConsistentRead` to `true` . Although a strongly consistent read might take more time than an eventually consistent read, it always returns the last updated value.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/GetItem)

## Synopsis

```
get-item
--table-name <value>
--key <value>
[--attributes-to-get <value>]
[--consistent-read | --no-consistent-read]
[--return-consumed-capacity <value>]
[--projection-expression <value>]
[--expression-attribute-names <value>]
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

`--table-name` (string)

The name of the table containing the requested item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.

`--key` (map)

A map of attribute names to `AttributeValue` objects, representing the primary key of the item to retrieve.

For the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.

key -> (string)

value -> (structure)

Represents the data for an attribute.

Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.

For more information, see [Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes) in the *Amazon DynamoDB Developer Guide* .

S -> (string)

An attribute of type String. For example:

`"S": "Hello"`

N -> (string)

An attribute of type Number. For example:

`"N": "123.45"`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

`"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"`

SS -> (list)

An attribute of type String Set. For example:

`"SS": ["Giraffe", "Hippo" ,"Zebra"]`

(string)

NS -> (list)

An attribute of type Number Set. For example:

`"NS": ["42.2", "-19", "7.5", "3.14"]`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string)

BS -> (list)

An attribute of type Binary Set. For example:

`"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]`

(blob)

M -> (map)

An attribute of type Map. For example:

`"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}`

key -> (string)

value -> (structure)

Represents the data for an attribute.

Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.

For more information, see [Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes) in the *Amazon DynamoDB Developer Guide* .

S -> (string)

An attribute of type String. For example:

`"S": "Hello"`

N -> (string)

An attribute of type Number. For example:

`"N": "123.45"`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

`"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"`

SS -> (list)

An attribute of type String Set. For example:

`"SS": ["Giraffe", "Hippo" ,"Zebra"]`

(string)

NS -> (list)

An attribute of type Number Set. For example:

`"NS": ["42.2", "-19", "7.5", "3.14"]`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string)

BS -> (list)

An attribute of type Binary Set. For example:

`"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]`

(blob)

M -> (map)

An attribute of type Map. For example:

`"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}`

key -> (string)

( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

`"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N": "3.14159"}]`

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

`"NULL": true`

BOOL -> (boolean)

An attribute of type Boolean. For example:

`"BOOL": true`

L -> (list)

An attribute of type List. For example:

`"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N": "3.14159"}]`

(structure)

Represents the data for an attribute.

Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.

For more information, see [Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes) in the *Amazon DynamoDB Developer Guide* .

S -> (string)

An attribute of type String. For example:

`"S": "Hello"`

N -> (string)

An attribute of type Number. For example:

`"N": "123.45"`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

`"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"`

SS -> (list)

An attribute of type String Set. For example:

`"SS": ["Giraffe", "Hippo" ,"Zebra"]`

(string)

NS -> (list)

An attribute of type Number Set. For example:

`"NS": ["42.2", "-19", "7.5", "3.14"]`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string)

BS -> (list)

An attribute of type Binary Set. For example:

`"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]`

(blob)

M -> (map)

An attribute of type Map. For example:

`"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}`

key -> (string)

( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

`"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N": "3.14159"}]`

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

`"NULL": true`

BOOL -> (boolean)

An attribute of type Boolean. For example:

`"BOOL": true`

NULL -> (boolean)

An attribute of type Null. For example:

`"NULL": true`

BOOL -> (boolean)

An attribute of type Boolean. For example:

`"BOOL": true`

JSON Syntax:

```
{"string": {
      "S": "string",
      "N": "string",
      "B": blob,
      "SS": ["string", ...],
      "NS": ["string", ...],
      "BS": [blob, ...],
      "M": {"string": {
            "S": "string",
            "N": "string",
            "B": blob,
            "SS": ["string", ...],
            "NS": ["string", ...],
            "BS": [blob, ...],
            "M": {"string": { ... recursive ... }
              ...},
            "L": [
              { ... recursive ... }
              ...
            ],
            "NULL": true|false,
            "BOOL": true|false
          }
        ...},
      "L": [
        {
          "S": "string",
          "N": "string",
          "B": blob,
          "SS": ["string", ...],
          "NS": ["string", ...],
          "BS": [blob, ...],
          "M": {"string": { ... recursive ... }
            ...},
          "L": [
            { ... recursive ... }
            ...
          ],
          "NULL": true|false,
          "BOOL": true|false
        }
        ...
      ],
      "NULL": true|false,
      "BOOL": true|false
    }
  ...}
```

`--attributes-to-get` (list)

This is a legacy parameter. Use `ProjectionExpression` instead. For more information, see [AttributesToGet](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html) in the *Amazon DynamoDB Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--consistent-read` | `--no-consistent-read` (boolean)

Determines the read consistency model: If set to `true` , then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.

`--return-consumed-capacity` (string)

Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response:

- `INDEXES` - The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed. Note that some operations, such as `GetItem` and `BatchGetItem` , do not access any indexes at all. In these cases, specifying `INDEXES` will only return `ConsumedCapacity` information for table(s).
- `TOTAL` - The response includes only the aggregate `ConsumedCapacity` for the operation.
- `NONE` - No `ConsumedCapacity` details are included in the response.

Possible values:

- `INDEXES`
- `TOTAL`
- `NONE`

`--projection-expression` (string)

A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.

If no attribute names are specified, then all attributes are returned. If any of the requested attributes are not found, they do not appear in the result.

For more information, see [Specifying Item Attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html) in the *Amazon DynamoDB Developer Guide* .

`--expression-attribute-names` (map)

One or more substitution tokens for attribute names in an expression. The following are some use cases for using `ExpressionAttributeNames` :

- To access an attribute whose name conflicts with a DynamoDB reserved word.
- To create a placeholder for repeating occurrences of an attribute name in an expression.
- To prevent special characters in an attribute name from being misinterpreted in an expression.

Use the **#** character in an expression to dereference an attribute name. For example, consider the following attribute name:

- `Percentile`

The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see [Reserved Words](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html) in the *Amazon DynamoDB Developer Guide* ). To work around this, you could specify the following for `ExpressionAttributeNames` :

- `{"#P":"Percentile"}`

You could then use this substitution in an expression, as in this example:

- `#P = :val`

### Note

Tokens that begin with the **:** character are *expression attribute values* , which are placeholders for the actual value at runtime.

For more information on expression attribute names, see [Specifying Item Attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html) in the *Amazon DynamoDB Developer Guide* .

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To read an item in a table**

The following `get-item` example retrieves an item from the `MusicCollection` table. The table has a hash-and-range primary key (`Artist` and `SongTitle`), so you must specify both of these attributes. The command also requests information about the read capacity consumed by the operation.

```
aws dynamodb get-item \
    --table-name MusicCollection \
    --key file://key.json \
    --return-consumed-capacity TOTAL
```

Contents of `key.json`:

```
{
    "Artist": {"S": "Acme Band"},
    "SongTitle": {"S": "Happy Day"}
}
```

Output:

```
{
    "Item": {
        "AlbumTitle": {
            "S": "Songs About Life"
        },
        "SongTitle": {
            "S": "Happy Day"
        },
        "Artist": {
            "S": "Acme Band"
        }
    },
    "ConsumedCapacity": {
        "TableName": "MusicCollection",
        "CapacityUnits": 0.5
    }
}
```

For more information, see [Reading an Item](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html#WorkingWithItems.ReadingData) in the *Amazon DynamoDB Developer Guide*.

**Example 2: To read an item using a consistent read**

The following example retrieves an item from the `MusicCollection` table using strongly consistent reads.

```
aws dynamodb get-item \
    --table-name MusicCollection \
    --key file://key.json \
    --consistent-read \
    --return-consumed-capacity TOTAL
```

Contents of `key.json`:

```
{
    "Artist": {"S": "Acme Band"},
    "SongTitle": {"S": "Happy Day"}
}
```

Output:

```
{
    "Item": {
        "AlbumTitle": {
            "S": "Songs About Life"
        },
        "SongTitle": {
            "S": "Happy Day"
        },
        "Artist": {
            "S": "Acme Band"
        }
    },
    "ConsumedCapacity": {
        "TableName": "MusicCollection",
        "CapacityUnits": 1.0
    }
}
```

For more information, see [Reading an Item](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html#WorkingWithItems.ReadingData) in the *Amazon DynamoDB Developer Guide*.

**Example 3: To retrieve specific attributes of an item**

The following example uses a projection expression to retrieve only three attributes of the desired item.

```
aws dynamodb get-item \
    --table-name ProductCatalog \
    --key '{"Id": {"N": "102"}}' \
    --projection-expression "#T, #C, #P" \
    --expression-attribute-names file://names.json
```

Contents of `names.json`:

```
{
    "#T": "Title",
    "#C": "ProductCategory",
    "#P": "Price"
}
```

Output:

```
{
    "Item": {
        "Price": {
            "N": "20"
        },
        "Title": {
            "S": "Book 102 Title"
        },
        "ProductCategory": {
            "S": "Book"
        }
    }
}
```

For more information, see [Reading an Item](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html#WorkingWithItems.ReadingData) in the *Amazon DynamoDB Developer Guide*.

## Output

Item -> (map)

A map of attribute names to `AttributeValue` objects, as specified by `ProjectionExpression` .

key -> (string)

value -> (structure)

Represents the data for an attribute.

Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.

For more information, see [Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes) in the *Amazon DynamoDB Developer Guide* .

S -> (string)

An attribute of type String. For example:

`"S": "Hello"`

N -> (string)

An attribute of type Number. For example:

`"N": "123.45"`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

`"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"`

SS -> (list)

An attribute of type String Set. For example:

`"SS": ["Giraffe", "Hippo" ,"Zebra"]`

(string)

NS -> (list)

An attribute of type Number Set. For example:

`"NS": ["42.2", "-19", "7.5", "3.14"]`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string)

BS -> (list)

An attribute of type Binary Set. For example:

`"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]`

(blob)

M -> (map)

An attribute of type Map. For example:

`"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}`

key -> (string)

value -> (structure)

Represents the data for an attribute.

Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.

For more information, see [Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes) in the *Amazon DynamoDB Developer Guide* .

S -> (string)

An attribute of type String. For example:

`"S": "Hello"`

N -> (string)

An attribute of type Number. For example:

`"N": "123.45"`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

`"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"`

SS -> (list)

An attribute of type String Set. For example:

`"SS": ["Giraffe", "Hippo" ,"Zebra"]`

(string)

NS -> (list)

An attribute of type Number Set. For example:

`"NS": ["42.2", "-19", "7.5", "3.14"]`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string)

BS -> (list)

An attribute of type Binary Set. For example:

`"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]`

(blob)

M -> (map)

An attribute of type Map. For example:

`"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}`

key -> (string)

( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

`"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N": "3.14159"}]`

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

`"NULL": true`

BOOL -> (boolean)

An attribute of type Boolean. For example:

`"BOOL": true`

L -> (list)

An attribute of type List. For example:

`"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N": "3.14159"}]`

(structure)

Represents the data for an attribute.

Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.

For more information, see [Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes) in the *Amazon DynamoDB Developer Guide* .

S -> (string)

An attribute of type String. For example:

`"S": "Hello"`

N -> (string)

An attribute of type Number. For example:

`"N": "123.45"`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

`"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"`

SS -> (list)

An attribute of type String Set. For example:

`"SS": ["Giraffe", "Hippo" ,"Zebra"]`

(string)

NS -> (list)

An attribute of type Number Set. For example:

`"NS": ["42.2", "-19", "7.5", "3.14"]`

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

(string)

BS -> (list)

An attribute of type Binary Set. For example:

`"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]`

(blob)

M -> (map)

An attribute of type Map. For example:

`"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}`

key -> (string)

( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

`"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N": "3.14159"}]`

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

`"NULL": true`

BOOL -> (boolean)

An attribute of type Boolean. For example:

`"BOOL": true`

NULL -> (boolean)

An attribute of type Null. For example:

`"NULL": true`

BOOL -> (boolean)

An attribute of type Boolean. For example:

`"BOOL": true`

ConsumedCapacity -> (structure)

The capacity units consumed by the `GetItem` operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. `ConsumedCapacity` is only returned if the `ReturnConsumedCapacity` parameter was specified. For more information, see [Capacity unit consumption for read operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html#read-operation-consumption) in the *Amazon DynamoDB Developer Guide* .

TableName -> (string)

The name of the table that was affected by the operation. If you had specified the Amazon Resource Name (ARN) of a table in the input, youâll see the table ARN in the response.

CapacityUnits -> (double)

The total number of capacity units consumed by the operation.

ReadCapacityUnits -> (double)

The total number of read capacity units consumed by the operation.

WriteCapacityUnits -> (double)

The total number of write capacity units consumed by the operation.

Table -> (structure)

The amount of throughput consumed on the table affected by the operation.

ReadCapacityUnits -> (double)

The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits -> (double)

The total number of write capacity units consumed on a table or an index.

CapacityUnits -> (double)

The total number of capacity units consumed on a table or an index.

LocalSecondaryIndexes -> (map)

The amount of throughput consumed on each local index affected by the operation.

key -> (string)

value -> (structure)

Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits -> (double)

The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits -> (double)

The total number of write capacity units consumed on a table or an index.

CapacityUnits -> (double)

The total number of capacity units consumed on a table or an index.

GlobalSecondaryIndexes -> (map)

The amount of throughput consumed on each global index affected by the operation.

key -> (string)

value -> (structure)

Represents the amount of provisioned throughput capacity consumed on a table or an index.

ReadCapacityUnits -> (double)

The total number of read capacity units consumed on a table or an index.

WriteCapacityUnits -> (double)

The total number of write capacity units consumed on a table or an index.

CapacityUnits -> (double)

The total number of capacity units consumed on a table or an index.