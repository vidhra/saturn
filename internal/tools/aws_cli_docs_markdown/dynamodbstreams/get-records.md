# get-recordsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodbstreams/get-records.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodbstreams/get-records.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dynamodbstreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodbstreams/index.html#cli-aws-dynamodbstreams) ]

# get-records

## Description

Retrieves the stream records from a given shard.

Specify a shard iterator using the `ShardIterator` parameter. The shard iterator specifies the position in the shard from which you want to start reading stream records sequentially. If there are no stream records available in the portion of the shard that the iterator points to, `GetRecords` returns an empty list. Note that it might take multiple calls to get to a portion of the shard that contains stream records.

### Note

`GetRecords` can retrieve a maximum of 1 MB of data or 1000 stream records, whichever comes first.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/streams-dynamodb-2012-08-10/GetRecords)

## Synopsis

```
get-records
--shard-iterator <value>
[--limit <value>]
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

`--shard-iterator` (string)

A shard iterator that was retrieved from a previous GetShardIterator operation. This iterator can be used to access the stream records in this shard.

`--limit` (integer)

The maximum number of records to return from the shard. The upper limit is 1000.

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

**To get records from a Dynamodb stream**

The following `get-records` command retrieves records using the specified Amazon DynamoDB shard iterator.

```
aws dynamodbstreams get-records \
    --shard-iterator "arn:aws:dynamodb:us-west-1:123456789012:table/Music/stream/2019-10-22T18:02:01.576|1|AAAAAAAAAAGgM3YZ89vLZZxjmoQeo33r9M4x3+zmmTLsiL86MfrF4+B4EbsByi52InVmiONmy6xVW4IRcIIbs1zO7MNIlqZfx8WQzMwVDyINtGG2hCLg78JKbYxFasXeePGlApTyf3rJxR765uyOVaBvBHAJuwF2TXIuxhaAlOupNGHr52qAC3a49ZOmf+CjNPlqQjnyRSAnfOwWmKhL1/KNParWSfz2odf780oOObIDIWRRMkt7+Hyzh9SD+hFxFAWR5C7QIlOXPc8mRBfNIazfrVCjJK8/jsjCzsqNyXKzJbhh+GXCoxYN+Kpmg4nyj1EAsYhbGL35muvHFoHjcyuynbsczbWaXNfThDwRAyvoTmc8XhHKtAWUbJiaVd8ZPtQwDsThCrmDRPIdmTRGWllGfUr5ezN5LscvkQezzgpaU5p8BgCqRzjv5Vl8LB6wHgQWNG+w/lEGS05ha1qNP+Vl4+tuhz2TRnhnJo/pny9GI/yGpce97mWvSPr5KPwy+Dtcm5BHayBs+PVYHITaTliInFlT+LCwvaz1QH3MY3b8A05Z800wjpktm60iQqtMeDwN4NX6FrcxR34JoFKGsgR8XkHVJzz2xr1xqSJ12ycpNTyHnndusw=="
```

Output:

```
{
    "Records": [
        {
            "eventID": "c3b5d798eef6215d42f8137b19a88e50",
            "eventName": "INSERT",
            "eventVersion": "1.1",
            "eventSource": "aws:dynamodb",
            "awsRegion": "us-west-1",
            "dynamodb": {
                "ApproximateCreationDateTime": 1571849028.0,
                "Keys": {
                    "Artist": {
                        "S": "No One You Know"
                    },
                    "SongTitle": {
                        "S": "Call Me Today"
                    }
                },
                "NewImage": {
                    "AlbumTitle": {
                        "S": "Somewhat Famous"
                    },
                    "Artist": {
                        "S": "No One You Know"
                    },
                    "Awards": {
                        "N": "1"
                    },
                    "SongTitle": {
                        "S": "Call Me Today"
                    }
                },
                "SequenceNumber": "700000000013256296913",
                "SizeBytes": 119,
                "StreamViewType": "NEW_AND_OLD_IMAGES"
            }
        },
        {
            "eventID": "878960a6967867e2da16b27380a27328",
            "eventName": "INSERT",
            "eventVersion": "1.1",
            "eventSource": "aws:dynamodb",
            "awsRegion": "us-west-1",
            "dynamodb": {
                "ApproximateCreationDateTime": 1571849029.0,
                "Keys": {
                    "Artist": {
                        "S": "Acme Band"
                    },
                    "SongTitle": {
                        "S": "Happy Day"
                    }
                },
                "NewImage": {
                    "AlbumTitle": {
                        "S": "Songs About Life"
                    },
                    "Artist": {
                        "S": "Acme Band"
                    },
                    "Awards": {
                        "N": "10"
                    },
                    "SongTitle": {
                        "S": "Happy Day"
                    }
                },
                "SequenceNumber": "800000000013256297217",
                "SizeBytes": 100,
                "StreamViewType": "NEW_AND_OLD_IMAGES"
            }
        },
        {
            "eventID": "520fabde080e159fc3710b15ee1d4daa",
            "eventName": "MODIFY",
            "eventVersion": "1.1",
            "eventSource": "aws:dynamodb",
            "awsRegion": "us-west-1",
            "dynamodb": {
                "ApproximateCreationDateTime": 1571849734.0,
                "Keys": {
                    "Artist": {
                        "S": "Acme Band"
                    },
                    "SongTitle": {
                        "S": "Happy Day"
                    }
                },
                "NewImage": {
                    "AlbumTitle": {
                        "S": "Updated Album Title"
                    },
                    "Artist": {
                        "S": "Acme Band"
                    },
                    "Awards": {
                        "N": "10"
                    },
                    "SongTitle": {
                        "S": "Happy Day"
                    }
                },
                "OldImage": {
                    "AlbumTitle": {
                        "S": "Songs About Life"
                    },
                    "Artist": {
                        "S": "Acme Band"
                    },
                    "Awards": {
                        "N": "10"
                    },
                    "SongTitle": {
                        "S": "Happy Day"
                    }
                },
                "SequenceNumber": "900000000013256687845",
                "SizeBytes": 170,
                "StreamViewType": "NEW_AND_OLD_IMAGES"
            }
        }
    ],
    "NextShardIterator": "arn:aws:dynamodb:us-west-1:123456789012:table/Music/stream/2019-10-23T16:41:08.740|1|AAAAAAAAAAEhEI04jkFLW+LKOwivjT8d/IHEh3iExV2xK00aTxEzVy1C1C7Kbb5+ZOW6bT9VQ2n1/mrs7+PRiaOZCHJu7JHJVW7zlsqOi/ges3fw8GYEymyL+piEk35cx67rQqwKKyq+Q6w9JyjreIOj4F2lWLV26lBwRTrIYC4IB7C3BZZK4715QwYdDxNdVHiSBRZX8UqoS6WOt0F87xZLNB9F/NhYBLXi/wcGvAcBcC0TNIOH+N0NqwtoB/FGCkNrf8YZ0xRoNN6RgGuVWHF3pxOhxEJeFZoSoJTIKeG9YcYxzi5Ci/mhdtm7tBXnbw5c6xmsGsBqTirNjlDyJLcWl8Cl0UOLX63Ufo/5QliztcjEbKsQe28x8LM8o7VH1Is0fF/ITt8awSA4igyJS0P87GN8Qri8kj8iaE35805jBHWF2wvwT6Iy2xGrR2r2HzYps9dwGOarVdEITaJfWzNoL4HajMhmREZLYfM7Pb0PvRMO7JkENyPIU6e2w16W1CvJO2EGFIxtNk+V04i1YIeHMXJfcwetNRuIbdQXfJht2NQZa4PVV6iknY6d19MrdbSTMKoqAuvp6g3Q2jH4t7GKCLWgodcPAn8g5+43DaNkh4Z5zKOfNw=="
}
```

For more information, see [Capturing Table Activity with DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) in the *Amazon DynamoDB Developer Guide*.

## Output

Records -> (list)

The stream records from the shard, which were retrieved using the shard iterator.

(structure)

A description of a unique event within a stream.

eventID -> (string)

A globally unique identifier for the event that was recorded in this stream record.

eventName -> (string)

The type of data modification that was performed on the DynamoDB table:

- `INSERT` - a new item was added to the table.
- `MODIFY` - one or more of an existing itemâs attributes were modified.
- `REMOVE` - the item was deleted from the table

eventVersion -> (string)

The version number of the stream record format. This number is updated whenever the structure of `Record` is modified.

Client applications must not assume that `eventVersion` will remain at a particular value, as this number is subject to change at any time. In general, `eventVersion` will only increase as the low-level DynamoDB Streams API evolves.

eventSource -> (string)

The Amazon Web Services service from which the stream record originated. For DynamoDB Streams, this is `aws:dynamodb` .

awsRegion -> (string)

The region in which the `GetRecords` request was received.

dynamodb -> (structure)

The main body of the stream record, containing all of the DynamoDB-specific fields.

ApproximateCreationDateTime -> (timestamp)

The approximate date and time when the stream record was created, in [UNIX epoch time](http://www.epochconverter.com/) format and rounded down to the closest second.

Keys -> (map)

The primary key attribute(s) for the DynamoDB item that was modified.

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

NewImage -> (map)

The item in the DynamoDB table as it appeared after it was modified.

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

OldImage -> (map)

The item in the DynamoDB table as it appeared before it was modified.

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

SequenceNumber -> (string)

The sequence number of the stream record.

SizeBytes -> (long)

The size of the stream record, in bytes.

StreamViewType -> (string)

The type of data from the modified DynamoDB item that was captured in this stream record:

- `KEYS_ONLY` - only the key attributes of the modified item.
- `NEW_IMAGE` - the entire item, as it appeared after it was modified.
- `OLD_IMAGE` - the entire item, as it appeared before it was modified.
- `NEW_AND_OLD_IMAGES` - both the new and the old item images of the item.

userIdentity -> (structure)

Items that are deleted by the Time to Live process after expiration have the following fields:

- Records[].userIdentity.type âServiceâ
- Records[].userIdentity.principalId âdynamodb.amazonaws.comâ

PrincipalId -> (string)

A unique identifier for the entity that made the call. For Time To Live, the principalId is âdynamodb.amazonaws.comâ.

Type -> (string)

The type of the identity. For Time To Live, the type is âServiceâ.

NextShardIterator -> (string)

The next position in the shard from which to start sequentially reading stream records. If set to `null` , the shard has been closed and the requested iterator will not return any more data.