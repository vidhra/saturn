# queryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/query.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/query.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dynamodb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html#cli-aws-dynamodb) ]

# query

## Description

You must provide the name of the partition key attribute and a single value for that attribute. `Query` returns all items with that partition key value. Optionally, you can provide a sort key attribute and use a comparison operator to refine the search results.

Use the `KeyConditionExpression` parameter to provide a specific value for the partition key. The `Query` operation will return all of the items from the table or index with that partition key value. You can optionally narrow the scope of the `Query` operation by specifying a sort key value and a comparison operator in `KeyConditionExpression` . To further refine the `Query` results, you can optionally provide a `FilterExpression` . A `FilterExpression` determines which items within the results should be returned to you. All of the other results are discarded.

A `Query` operation always returns a result set. If no matching items are found, the result set will be empty. Queries that do not return results consume the minimum number of read capacity units for that type of read operation.

### Note

DynamoDB calculates the number of read capacity units consumed based on item size, not on the amount of data that is returned to an application. The number of capacity units consumed will be the same whether you request all of the attributes (the default behavior) or just some of them (using a projection expression). The number will also be the same whether or not you use a `FilterExpression` .

`Query` results are always sorted by the sort key value. If the data type of the sort key is Number, the results are returned in numeric order; otherwise, the results are returned in order of UTF-8 bytes. By default, the sort order is ascending. To reverse the order, set the `ScanIndexForward` parameter to false.

A single `Query` operation will read up to the maximum number of items set (if using the `Limit` parameter) or a maximum of 1 MB of data and then apply any filtering to the results using `FilterExpression` . If `LastEvaluatedKey` is present in the response, you will need to paginate the result set. For more information, see [Paginating the Results](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html#Query.Pagination) in the *Amazon DynamoDB Developer Guide* .

`FilterExpression` is applied after a `Query` finishes, but before the results are returned. A `FilterExpression` cannot contain partition key or sort key attributes. You need to specify those attributes in the `KeyConditionExpression` .

### Note

A `Query` operation can return an empty result set and a `LastEvaluatedKey` if all the items read for the page of results are filtered out.

You can query a table, a local secondary index, or a global secondary index. For a query on a table or on a local secondary index, you can set the `ConsistentRead` parameter to `true` and obtain a strongly consistent result. Global secondary indexes support eventually consistent reads only, so do not specify `ConsistentRead` when querying a global secondary index.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/Query)

`query` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Items`, `Count`, `ScannedCount`

## Synopsis

```
query
--table-name <value>
[--index-name <value>]
[--select <value>]
[--attributes-to-get <value>]
[--consistent-read | --no-consistent-read]
[--key-conditions <value>]
[--query-filter <value>]
[--conditional-operator <value>]
[--scan-index-forward | --no-scan-index-forward]
[--return-consumed-capacity <value>]
[--projection-expression <value>]
[--filter-expression <value>]
[--key-condition-expression <value>]
[--expression-attribute-names <value>]
[--expression-attribute-values <value>]
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

`--table-name` (string)

The name of the table containing the requested items. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.

`--index-name` (string)

The name of an index to query. This index can be any local secondary index or global secondary index on the table. Note that if you use the `IndexName` parameter, you must also provide `TableName.`

`--select` (string)

The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.

- `ALL_ATTRIBUTES` - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index, DynamoDB fetches the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.
- `ALL_PROJECTED_ATTRIBUTES` - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying `ALL_ATTRIBUTES` .
- `COUNT` - Returns the number of matching items, rather than the matching items themselves. Note that this uses the same quantity of read capacity units as getting the items, and is subject to the same item size calculations.
- `SPECIFIC_ATTRIBUTES` - Returns only the attributes listed in `ProjectionExpression` . This return value is equivalent to specifying `ProjectionExpression` without specifying any value for `Select` . If you query or scan a local secondary index and request only attributes that are projected into that index, the operation will read only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB fetches each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency. If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table.

If neither `Select` nor `ProjectionExpression` are specified, DynamoDB defaults to `ALL_ATTRIBUTES` when accessing a table, and `ALL_PROJECTED_ATTRIBUTES` when accessing an index. You cannot use both `Select` and `ProjectionExpression` together in a single request, unless the value for `Select` is `SPECIFIC_ATTRIBUTES` . (This usage is equivalent to specifying `ProjectionExpression` without any value for `Select` .)

### Note

If you use the `ProjectionExpression` parameter, then the value for `Select` can only be `SPECIFIC_ATTRIBUTES` . Any other value for `Select` will return an error.

Possible values:

- `ALL_ATTRIBUTES`
- `ALL_PROJECTED_ATTRIBUTES`
- `SPECIFIC_ATTRIBUTES`
- `COUNT`

`--attributes-to-get` (list)

This is a legacy parameter. Use `ProjectionExpression` instead. For more information, see [AttributesToGet](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html) in the *Amazon DynamoDB Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--consistent-read` | `--no-consistent-read` (boolean)

Determines the read consistency model: If set to `true` , then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.

Strongly consistent reads are not supported on global secondary indexes. If you query a global secondary index with `ConsistentRead` set to `true` , you will receive a `ValidationException` .

`--key-conditions` (map)

This is a legacy parameter. Use `KeyConditionExpression` instead. For more information, see [KeyConditions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.KeyConditions.html) in the *Amazon DynamoDB Developer Guide* .

key -> (string)

value -> (structure)

Represents the selection criteria for a `Query` or `Scan` operation:

- For a `Query` operation, `Condition` is used for specifying the `KeyConditions` to use when querying a table or an index. For `KeyConditions` , only the following comparison operators are supported:  `EQ | LE | LT | GE | GT | BEGINS_WITH | BETWEEN` `Condition` is also used in a `QueryFilter` , which evaluates the query results and returns only the desired values.
- For a `Scan` operation, `Condition` is used in a `ScanFilter` , which evaluates the scan results and returns only the desired values.

AttributeValueList -> (list)

One or more values to evaluate against the supplied attribute. The number of values in the list depends on the `ComparisonOperator` being used.

For type Number, value comparisons are numeric.

String value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, `a` is greater than `A` , and `a` is greater than `B` . For a list of code values, see [http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters](http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters) .

For Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.

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

ComparisonOperator -> (string)

A comparator for evaluating attributes. For example, equals, greater than, less than, etc.

The following comparison operators are available:

`EQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN`

The following are descriptions of each comparison operator.

- `EQ` : Equal. `EQ` is supported for all data types, including lists and maps.  `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not equal `{"NS":["6", "2", "1"]}` .
- `NE` : Not equal. `NE` is supported for all data types, including lists and maps.  `AttributeValueList` can contain only one `AttributeValue` of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an `AttributeValue` of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not equal `{"NS":["6", "2", "1"]}` .
- `LE` : Less than or equal.   `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, or Binary (not a set type). If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}` .
- `LT` : Less than.   `AttributeValueList` can contain only one `AttributeValue` of type String, Number, or Binary (not a set type). If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}` .
- `GE` : Greater than or equal.   `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, or Binary (not a set type). If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}` .
- `GT` : Greater than.   `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, or Binary (not a set type). If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}` .
- `NOT_NULL` : The attribute exists. `NOT_NULL` is supported for all data types, including lists and maps.

### Note

This operator tests for the existence of an attribute, not its data type. If the data type of attribute â`a` â is null, and you evaluate it using `NOT_NULL` , the result is a Boolean `true` . This result is because the attribute â`a` â exists; its data type is not relevant to the `NOT_NULL` comparison operator.

- `NULL` : The attribute does not exist. `NULL` is supported for all data types, including lists and maps.

### Note

This operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute â`a` â is null, and you evaluate it using `NULL` , the result is a Boolean `false` . This is because the attribute â`a` â exists; its data type is not relevant to the `NULL` comparison operator.

- `CONTAINS` : Checks for a subsequence, or value in a set.  `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set (â`SS` â, â`NS` â, or â`BS` â), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating â`a CONTAINS b` â, â`a` â can be a list; however, â`b` â cannot be a set, a map, or a list.
- `NOT_CONTAINS` : Checks for absence of a subsequence, or absence of a value in a set.  `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set (â`SS` â, â`NS` â, or â`BS` â), then the operator evaluates to true if it *does not* find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating â`a NOT CONTAINS b` â, â`a` â can be a list; however, â`b` â cannot be a set, a map, or a list.
- `BEGINS_WITH` : Checks for a prefix.   `AttributeValueList` can contain only one `AttributeValue` of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).
- `IN` : Checks for matching elements in a list.  `AttributeValueList` can contain one or more `AttributeValue` elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true.
- `BETWEEN` : Greater than or equal to the first value, and less than or equal to the second value.   `AttributeValueList` must contain two `AttributeValue` elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not compare to `{"N":"6"}` . Also, `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}`

For usage examples of `AttributeValueList` and `ComparisonOperator` , see [Legacy Conditional Parameters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.html) in the *Amazon DynamoDB Developer Guide* .

JSON Syntax:

```
{"string": {
      "AttributeValueList": [
        {
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
        ...
      ],
      "ComparisonOperator": "EQ"|"NE"|"IN"|"LE"|"LT"|"GE"|"GT"|"BETWEEN"|"NOT_NULL"|"NULL"|"CONTAINS"|"NOT_CONTAINS"|"BEGINS_WITH"
    }
  ...}
```

`--query-filter` (map)

This is a legacy parameter. Use `FilterExpression` instead. For more information, see [QueryFilter](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.QueryFilter.html) in the *Amazon DynamoDB Developer Guide* .

key -> (string)

value -> (structure)

Represents the selection criteria for a `Query` or `Scan` operation:

- For a `Query` operation, `Condition` is used for specifying the `KeyConditions` to use when querying a table or an index. For `KeyConditions` , only the following comparison operators are supported:  `EQ | LE | LT | GE | GT | BEGINS_WITH | BETWEEN` `Condition` is also used in a `QueryFilter` , which evaluates the query results and returns only the desired values.
- For a `Scan` operation, `Condition` is used in a `ScanFilter` , which evaluates the scan results and returns only the desired values.

AttributeValueList -> (list)

One or more values to evaluate against the supplied attribute. The number of values in the list depends on the `ComparisonOperator` being used.

For type Number, value comparisons are numeric.

String value comparisons for greater than, equals, or less than are based on ASCII character code values. For example, `a` is greater than `A` , and `a` is greater than `B` . For a list of code values, see [http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters](http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters) .

For Binary, DynamoDB treats each byte of the binary data as unsigned when it compares binary values.

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

ComparisonOperator -> (string)

A comparator for evaluating attributes. For example, equals, greater than, less than, etc.

The following comparison operators are available:

`EQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS | BEGINS_WITH | IN | BETWEEN`

The following are descriptions of each comparison operator.

- `EQ` : Equal. `EQ` is supported for all data types, including lists and maps.  `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not equal `{"NS":["6", "2", "1"]}` .
- `NE` : Not equal. `NE` is supported for all data types, including lists and maps.  `AttributeValueList` can contain only one `AttributeValue` of type String, Number, Binary, String Set, Number Set, or Binary Set. If an item contains an `AttributeValue` of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not equal `{"NS":["6", "2", "1"]}` .
- `LE` : Less than or equal.   `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, or Binary (not a set type). If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}` .
- `LT` : Less than.   `AttributeValueList` can contain only one `AttributeValue` of type String, Number, or Binary (not a set type). If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}` .
- `GE` : Greater than or equal.   `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, or Binary (not a set type). If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}` .
- `GT` : Greater than.   `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, or Binary (not a set type). If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}` . Also, `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}` .
- `NOT_NULL` : The attribute exists. `NOT_NULL` is supported for all data types, including lists and maps.

### Note

This operator tests for the existence of an attribute, not its data type. If the data type of attribute â`a` â is null, and you evaluate it using `NOT_NULL` , the result is a Boolean `true` . This result is because the attribute â`a` â exists; its data type is not relevant to the `NOT_NULL` comparison operator.

- `NULL` : The attribute does not exist. `NULL` is supported for all data types, including lists and maps.

### Note

This operator tests for the nonexistence of an attribute, not its data type. If the data type of attribute â`a` â is null, and you evaluate it using `NULL` , the result is a Boolean `false` . This is because the attribute â`a` â exists; its data type is not relevant to the `NULL` comparison operator.

- `CONTAINS` : Checks for a subsequence, or value in a set.  `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is of type String, then the operator checks for a substring match. If the target attribute of the comparison is of type Binary, then the operator looks for a subsequence of the target that matches the input. If the target attribute of the comparison is a set (â`SS` â, â`NS` â, or â`BS` â), then the operator evaluates to true if it finds an exact match with any member of the set. CONTAINS is supported for lists: When evaluating â`a CONTAINS b` â, â`a` â can be a list; however, â`b` â cannot be a set, a map, or a list.
- `NOT_CONTAINS` : Checks for absence of a subsequence, or absence of a value in a set.  `AttributeValueList` can contain only one `AttributeValue` element of type String, Number, or Binary (not a set type). If the target attribute of the comparison is a String, then the operator checks for the absence of a substring match. If the target attribute of the comparison is Binary, then the operator checks for the absence of a subsequence of the target that matches the input. If the target attribute of the comparison is a set (â`SS` â, â`NS` â, or â`BS` â), then the operator evaluates to true if it *does not* find an exact match with any member of the set. NOT_CONTAINS is supported for lists: When evaluating â`a NOT CONTAINS b` â, â`a` â can be a list; however, â`b` â cannot be a set, a map, or a list.
- `BEGINS_WITH` : Checks for a prefix.   `AttributeValueList` can contain only one `AttributeValue` of type String or Binary (not a Number or a set type). The target attribute of the comparison must be of type String or Binary (not a Number or a set type).
- `IN` : Checks for matching elements in a list.  `AttributeValueList` can contain one or more `AttributeValue` elements of type String, Number, or Binary. These attributes are compared against an existing attribute of an item. If any elements of the input are equal to the item attribute, the expression evaluates to true.
- `BETWEEN` : Greater than or equal to the first value, and less than or equal to the second value.   `AttributeValueList` must contain two `AttributeValue` elements of the same type, either String, Number, or Binary (not a set type). A target attribute matches if the target value is greater than, or equal to, the first element and less than, or equal to, the second element. If an item contains an `AttributeValue` element of a different type than the one provided in the request, the value does not match. For example, `{"S":"6"}` does not compare to `{"N":"6"}` . Also, `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}`

For usage examples of `AttributeValueList` and `ComparisonOperator` , see [Legacy Conditional Parameters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.html) in the *Amazon DynamoDB Developer Guide* .

JSON Syntax:

```
{"string": {
      "AttributeValueList": [
        {
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
        ...
      ],
      "ComparisonOperator": "EQ"|"NE"|"IN"|"LE"|"LT"|"GE"|"GT"|"BETWEEN"|"NOT_NULL"|"NULL"|"CONTAINS"|"NOT_CONTAINS"|"BEGINS_WITH"
    }
  ...}
```

`--conditional-operator` (string)

This is a legacy parameter. Use `FilterExpression` instead. For more information, see [ConditionalOperator](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html) in the *Amazon DynamoDB Developer Guide* .

Possible values:

- `AND`
- `OR`

`--scan-index-forward` | `--no-scan-index-forward` (boolean)

Specifies the order for index traversal: If `true` (default), the traversal is performed in ascending order; if `false` , the traversal is performed in descending order.

Items with the same partition key value are stored in sorted order by sort key. If the sort key data type is Number, the results are stored in numeric order. For type String, the results are stored in order of UTF-8 bytes. For type Binary, DynamoDB treats each byte of the binary data as unsigned.

If `ScanIndexForward` is `true` , DynamoDB returns the results in the order in which they are stored (by sort key value). This is the default behavior. If `ScanIndexForward` is `false` , DynamoDB reads the results in reverse order by sort key value, and then returns the results to the client.

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

If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.

For more information, see [Accessing Item Attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html) in the *Amazon DynamoDB Developer Guide* .

`--filter-expression` (string)

A string that contains conditions that DynamoDB applies after the `Query` operation, but before the data is returned to you. Items that do not satisfy the `FilterExpression` criteria are not returned.

A `FilterExpression` does not allow key attributes. You cannot define a filter expression based on a partition key or a sort key.

### Note

A `FilterExpression` is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.

For more information, see [Filter Expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.FilterExpression.html) in the *Amazon DynamoDB Developer Guide* .

`--key-condition-expression` (string)

The condition that specifies the key values for items to be retrieved by the `Query` action.

The condition must perform an equality test on a single partition key value.

The condition can optionally perform one of several comparison tests on a single sort key value. This allows `Query` to retrieve one item with a given partition key value and sort key value, or several items that have the same partition key value but different sort key values.

The partition key equality test is required, and must be specified in the following format:

`partitionKeyName` *=* `:partitionkeyval`

If you also want to provide a condition for the sort key, it must be combined using `AND` with the condition for the sort key. Following is an example, using the **=** comparison operator for the sort key:

`partitionKeyName` `=` `:partitionkeyval` `AND` `sortKeyName` `=` `:sortkeyval`

Valid comparisons for the sort key condition are as follows:

- `sortKeyName` `=` `:sortkeyval` - true if the sort key value is equal to `:sortkeyval` .
- `sortKeyName` `<` `:sortkeyval` - true if the sort key value is less than `:sortkeyval` .
- `sortKeyName` `<=` `:sortkeyval` - true if the sort key value is less than or equal to `:sortkeyval` .
- `sortKeyName` `>` `:sortkeyval` - true if the sort key value is greater than `:sortkeyval` .
- `sortKeyName` `>=` `:sortkeyval` - true if the sort key value is greater than or equal to `:sortkeyval` .
- `sortKeyName` `BETWEEN` `:sortkeyval1` `AND` `:sortkeyval2` - true if the sort key value is greater than or equal to `:sortkeyval1` , and less than or equal to `:sortkeyval2` .
- `begins_with (` `sortKeyName` , `:sortkeyval` `)` - true if the sort key value begins with a particular operand. (You cannot use this function with a sort key that is of type Number.) Note that the function name `begins_with` is case-sensitive.

Use the `ExpressionAttributeValues` parameter to replace tokens such as `:partitionval` and `:sortval` with actual values at runtime.

You can optionally use the `ExpressionAttributeNames` parameter to replace the names of the partition key and sort key with placeholder tokens. This option might be necessary if an attribute name conflicts with a DynamoDB reserved word. For example, the following `KeyConditionExpression` parameter causes an error because *Size* is a reserved word:

- `Size = :myval`

To work around this, define a placeholder (such a `#S` ) to represent the attribute name *Size* . `KeyConditionExpression` then is as follows:

- `#S = :myval`

For a list of reserved words, see [Reserved Words](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html) in the *Amazon DynamoDB Developer Guide* .

For more information on `ExpressionAttributeNames` and `ExpressionAttributeValues` , see [Using Placeholders for Attribute Names and Values](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ExpressionPlaceholders.html) in the *Amazon DynamoDB Developer Guide* .

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

`--expression-attribute-values` (map)

One or more values that can be substituted in an expression.

Use the **:** (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the *ProductStatus* attribute was one of the following:

`Available | Backordered | Discontinued`

You would first need to specify `ExpressionAttributeValues` as follows:

`{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }`

You could then use these values in an expression, such as this:

`ProductStatus IN (:avail, :back, :disc)`

For more information on expression attribute values, see [Specifying Conditions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html) in the *Amazon DynamoDB Developer Guide* .

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To query a table**

The following `query` example queries items in the `MusicCollection` table. The table has a hash-and-range primary key (`Artist` and `SongTitle`), but this query only specifies the hash key value. It returns song titles by the artist named âNo One You Knowâ.

```
aws dynamodb query \
    --table-name MusicCollection \
    --projection-expression "SongTitle" \
    --key-condition-expression "Artist = :v1" \
    --expression-attribute-values file://expression-attributes.json \
    --return-consumed-capacity TOTAL
```

Contents of `expression-attributes.json`:

```
{
    ":v1": {"S": "No One You Know"}
}
```

Output:

```
{
    "Items": [
        {
            "SongTitle": {
                "S": "Call Me Today"
            },
            "SongTitle": {
                "S": "Scared of My Shadow"
            }
        }
    ],
    "Count": 2,
    "ScannedCount": 2,
    "ConsumedCapacity": {
        "TableName": "MusicCollection",
        "CapacityUnits": 0.5
    }
}
```

For more information, see [Working with Queries in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) in the *Amazon DynamoDB Developer Guide*.

**Example 2: To query a table using strongly consistent reads and traverse the index in descending order**

The following example performs the same query as the first example, but returns results in reverse order and uses strongly consistent reads.

```
aws dynamodb query \
    --table-name MusicCollection \
    --projection-expression "SongTitle" \
    --key-condition-expression "Artist = :v1" \
    --expression-attribute-values file://expression-attributes.json \
    --consistent-read \
    --no-scan-index-forward \
    --return-consumed-capacity TOTAL
```

Contents of `expression-attributes.json`:

```
{
    ":v1": {"S": "No One You Know"}
}
```

Output:

```
{
    "Items": [
        {
            "SongTitle": {
                "S": "Scared of My Shadow"
            }
        },
        {
            "SongTitle": {
                "S": "Call Me Today"
            }
        }
    ],
    "Count": 2,
    "ScannedCount": 2,
    "ConsumedCapacity": {
        "TableName": "MusicCollection",
        "CapacityUnits": 1.0
    }
}
```

For more information, see [Working with Queries in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) in the *Amazon DynamoDB Developer Guide*.

**Example 3: To filter out specific results**

The following example queries the `MusicCollection` but excludes results with specific values in the `AlbumTitle` attribute. Note that this does not affect the `ScannedCount` or `ConsumedCapacity`, because the filter is applied after the items have been read.

```
aws dynamodb query \
    --table-name MusicCollection \
    --key-condition-expression "#n1 = :v1" \
    --filter-expression "NOT (#n2 IN (:v2, :v3))" \
    --expression-attribute-names file://names.json \
    --expression-attribute-values file://values.json \
    --return-consumed-capacity TOTAL
```

Contents of `values.json`:

```
{
    ":v1": {"S": "No One You Know"},
    ":v2": {"S": "Blue Sky Blues"},
    ":v3": {"S": "Greatest Hits"}
}
```

Contents of `names.json`:

```
{
    "#n1": "Artist",
    "#n2": "AlbumTitle"
}
```

Output:

```
{
    "Items": [
        {
            "AlbumTitle": {
                "S": "Somewhat Famous"
            },
            "Artist": {
                "S": "No One You Know"
            },
            "SongTitle": {
                "S": "Call Me Today"
            }
        }
    ],
    "Count": 1,
    "ScannedCount": 2,
    "ConsumedCapacity": {
        "TableName": "MusicCollection",
        "CapacityUnits": 0.5
    }
}
```

For more information, see [Working with Queries in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) in the *Amazon DynamoDB Developer Guide*.

**Example 4: To retrieve only an item count**

The following example retrieves a count of items matching the query, but does not retrieve any of the items themselves.

```
aws dynamodb query \
    --table-name MusicCollection \
    --select COUNT \
    --key-condition-expression "Artist = :v1" \
    --expression-attribute-values file://expression-attributes.json
```

Contents of `expression-attributes.json`:

```
{
    ":v1": {"S": "No One You Know"}
}
```

Output:

```
{
    "Count": 2,
    "ScannedCount": 2,
    "ConsumedCapacity": null
}
```

For more information, see [Working with Queries in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) in the *Amazon DynamoDB Developer Guide*.

**Example 5: To query an index**

The following example queries the local secondary index `AlbumTitleIndex`. The query returns all attributes from the base table that have been projected into the local secondary index. Note that when querying a local secondary index or global secondary index, you must also provide the name of the base table using the `table-name` parameter.

```
aws dynamodb query \
    --table-name MusicCollection \
    --index-name AlbumTitleIndex \
    --key-condition-expression "Artist = :v1" \
    --expression-attribute-values file://expression-attributes.json \
    --select ALL_PROJECTED_ATTRIBUTES \
    --return-consumed-capacity INDEXES
```

Contents of `expression-attributes.json`:

```
{
    ":v1": {"S": "No One You Know"}
}
```

Output:

```
{
    "Items": [
        {
            "AlbumTitle": {
                "S": "Blue Sky Blues"
            },
            "Artist": {
                "S": "No One You Know"
            },
            "SongTitle": {
                "S": "Scared of My Shadow"
            }
        },
        {
            "AlbumTitle": {
                "S": "Somewhat Famous"
            },
            "Artist": {
                "S": "No One You Know"
            },
            "SongTitle": {
                "S": "Call Me Today"
            }
        }
    ],
    "Count": 2,
    "ScannedCount": 2,
    "ConsumedCapacity": {
        "TableName": "MusicCollection",
        "CapacityUnits": 0.5,
        "Table": {
            "CapacityUnits": 0.0
        },
        "LocalSecondaryIndexes": {
            "AlbumTitleIndex": {
                "CapacityUnits": 0.5
            }
        }
    }
}
```

For more information, see [Working with Queries in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) in the *Amazon DynamoDB Developer Guide*.

## Output

Items -> (list)

An array of item attributes that match the query criteria. Each element in this array consists of an attribute name and the value for that attribute.

(map)

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

Count -> (integer)

The number of items in the response.

If you used a `QueryFilter` in the request, then `Count` is the number of items returned after the filter was applied, and `ScannedCount` is the number of matching items before the filter was applied.

If you did not use a filter in the request, then `Count` and `ScannedCount` are the same.

ScannedCount -> (integer)

The number of items evaluated, before any `QueryFilter` is applied. A high `ScannedCount` value with few, or no, `Count` results indicates an inefficient `Query` operation. For more information, see [Count and ScannedCount](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html#Scan.Count) in the *Amazon DynamoDB Developer Guide* .

If you did not use a filter in the request, then `ScannedCount` is the same as `Count` .

LastEvaluatedKey -> (map)

The primary key of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request.

If `LastEvaluatedKey` is empty, then the âlast pageâ of results has been processed and there is no more data to be retrieved.

If `LastEvaluatedKey` is not empty, it does not necessarily mean that there is more data in the result set. The only way to know when you have reached the end of the result set is when `LastEvaluatedKey` is empty.

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

The capacity units consumed by the `Query` operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. `ConsumedCapacity` is only returned if the `ReturnConsumedCapacity` parameter was specified. For more information, see [Capacity unit consumption for read operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html#read-operation-consumption) in the *Amazon DynamoDB Developer Guide* .

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