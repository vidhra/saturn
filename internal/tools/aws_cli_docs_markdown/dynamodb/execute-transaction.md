# execute-transactionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/execute-transaction.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/execute-transaction.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dynamodb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html#cli-aws-dynamodb) ]

# execute-transaction

## Description

This operation allows you to perform transactional reads or writes on data stored in DynamoDB, using PartiQL.

### Note

The entire transaction must consist of either read statements or write statements, you cannot mix both in one transaction. The EXISTS function is an exception and can be used to check the condition of specific attributes of the item in a similar manner to `ConditionCheck` in the [TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html#transaction-apis-txwriteitems) API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/ExecuteTransaction)

## Synopsis

```
execute-transaction
--transact-statements <value>
[--client-request-token <value>]
[--return-consumed-capacity <value>]
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

`--transact-statements` (list)

The list of PartiQL statements representing the transaction to run.

(structure)

Represents a PartiQL statement that uses parameters.

Statement -> (string)

A PartiQL statement that uses parameters.

Parameters -> (list)

The parameter values.

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

ReturnValuesOnConditionCheckFailure -> (string)

An optional parameter that returns the item attributes for a PartiQL `ParameterizedStatement` operation that failed a condition check.

There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.

JSON Syntax:

```
[
  {
    "Statement": "string",
    "Parameters": [
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
    "ReturnValuesOnConditionCheckFailure": "ALL_OLD"|"NONE"
  }
  ...
]
```

`--client-request-token` (string)

Set this value to get remaining results, if `NextToken` was returned in the statement response.

`--return-consumed-capacity` (string)

Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response. For more information, see [TransactGetItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactGetItems.html) and [TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html) .

Possible values:

- `INDEXES`
- `TOTAL`
- `NONE`

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

The response to a PartiQL transaction.

(structure)

Details for the requested item.

Item -> (map)

Map of attribute data consisting of the data type and attribute value.

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

ConsumedCapacity -> (list)

The capacity units consumed by the entire operation. The values of the list are ordered according to the ordering of the statements.

(structure)

The capacity units consumed by an operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. `ConsumedCapacity` is only returned if the request asked for it. For more information, see [Provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html) in the *Amazon DynamoDB Developer Guide* .

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